#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Перенос и сжатие графики в хранилище.

Чертежи и схемы (штриховая графика) -> PNG в оттенках серого с палитрой,
фотографии деталей и иллюстрации руководств -> JPEG.
Имена файлов сохраняются, чтобы ссылки [[имя]] в заметках не ломались.
"""
import os
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import VAULT


def _flatten(path):
    im = Image.open(path)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        im = Image.alpha_composite(bg, im)
    return im


def line_art(src, dst, maxside=1600, colors=16):
    """Штриховая графика: серый + палитра, PNG."""
    im = _flatten(src).convert("L")
    if max(im.size) > maxside:
        im.thumbnail((maxside, maxside), Image.LANCZOS)
    im.convert("P", palette=Image.ADAPTIVE, colors=colors).save(dst, "PNG", optimize=True)


def photo(src, dst, maxside=900, quality=78):
    """Фотографии и цветные иллюстрации: JPEG."""
    im = _flatten(src).convert("RGB")
    if max(im.size) > maxside:
        im.thumbnail((maxside, maxside), Image.LANCZOS)
    im.save(dst, "JPEG", quality=quality, optimize=True, progressive=True)


def convert_tree(src_dir, rel_out, mode="line", exts=(".png", ".jpg", ".jpeg"),
                 maxside=1600, rename=None, quality=78):
    """Обрабатывает каталог с картинками. Возвращает {исходное имя: имя в хранилище}."""
    out_dir = os.path.join(VAULT, rel_out)
    os.makedirs(out_dir, exist_ok=True)
    mapping = {}
    if not os.path.isdir(src_dir):
        return mapping
    for name in sorted(os.listdir(src_dir)):
        base, ext = os.path.splitext(name)
        if ext.lower() not in exts:
            continue
        src = os.path.join(src_dir, name)
        out_name = (rename(base) if rename else base) + (".png" if mode == "line" else ".jpg")
        dst = os.path.join(out_dir, out_name)
        try:
            if mode == "line":
                line_art(src, dst, maxside=maxside)
            else:
                photo(src, dst, maxside=maxside, quality=quality)
        except Exception:                                   # noqa: BLE001
            continue
        mapping[name] = out_name
    return mapping


def copy_file(src, rel_out):
    """Копирование как есть (PDF руководств машин)."""
    dst = os.path.join(VAULT, rel_out)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(src, "rb") as a, open(dst, "wb") as b:
        b.write(a.read())
    return os.path.basename(dst)
