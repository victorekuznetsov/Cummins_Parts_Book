#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Извлечение иллюстраций Cummins из скачанных PDF.

В HTML-страницах QuickServe картинки — это ссылки на сервер Cummins
(`/rtgraphics/...`), закрытый авторизацией. Но те же самые иллюстрации
лежат внутри скачанных PDF того же документа и в том же порядке.
Скрипт достаёт их из PDF, сопоставляет позиционно со списком ссылок из
HTML, сжимает (оттенки серого + палитра) и складывает в общий каталог
иллюстраций под именем из исходной ссылки.
"""
import hashlib
import io
import os

import pymupdf
from PIL import Image

LOGO_SIZES = {(150, 138), (149, 138), (150, 137)}   # шапка Cummins в PDF
MIN_PIXELS = 5000                                    # мелкие иконки не нужны


def pdf_images(path):
    """Картинки документа в порядке страниц; служебные логотипы отброшены."""
    out = []
    try:
        doc = pymupdf.open(path)
    except Exception:
        return out
    seen_on_page = None
    for page in doc:
        seen_on_page = set()
        for info in page.get_images(full=True):
            xref = info[0]
            if xref in seen_on_page:
                continue
            seen_on_page.add(xref)
            try:
                img = doc.extract_image(xref)
            except Exception:
                continue
            w, h = img.get("width", 0), img.get("height", 0)
            if (w, h) in LOGO_SIZES or w * h < MIN_PIXELS:
                continue
            out.append(img["image"])
    doc.close()
    return out


def compress(raw, colors=32):
    """PNG в оттенках серого с палитрой: чертежи не теряют читаемость."""
    im = Image.open(io.BytesIO(raw))
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        im = Image.alpha_composite(bg, im)
    im = im.convert("L")
    if max(im.size) > 1200:
        im.thumbnail((1200, 1200), Image.LANCZOS)
    im = im.convert("P", palette=Image.ADAPTIVE, colors=colors)
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    return buf.getvalue()


class FigureStore:
    """Каталог иллюстраций с дедупликацией по имени файла Cummins."""

    def __init__(self, outdir):
        self.outdir = outdir
        os.makedirs(outdir, exist_ok=True)
        self.saved = {}          # имя -> md5 исходника
        self.conflicts = set()   # имена с несовпадающим содержимым в разных PDF

    def add(self, name, raw):
        digest = hashlib.md5(raw).hexdigest()
        if name in self.saved:
            if self.saved[name] != digest:
                self.conflicts.add(name)
            return False
        try:
            data = compress(raw)
        except Exception:
            return False
        with open(os.path.join(self.outdir, name), "wb") as fh:
            fh.write(data)
        self.saved[name] = digest
        return True


def map_document(html_figs, pdf_path):
    """Сопоставляет ссылки из HTML с картинками из PDF.

    Возвращает (список пар (имя, байты), признак надёжности).
    Надёжно — когда количество совпало; иначе сопоставляем по порядку
    столько, сколько есть, а остаток помечаем как неуверенный.
    """
    names = [f.rsplit("/", 1)[-1] for f in html_figs]
    uniq_order = []
    for n in names:
        if n not in uniq_order:
            uniq_order.append(n)
    blobs = pdf_images(pdf_path)
    exact = len(blobs) == len(names)
    if exact:
        pairs = list(zip(names, blobs))
    elif len(blobs) == len(uniq_order):
        pairs = list(zip(uniq_order, blobs))
    else:
        pairs = list(zip(names, blobs))
    return pairs, (exact or len(blobs) == len(uniq_order))
