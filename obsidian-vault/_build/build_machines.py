#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Разбор каталогов машин NHL (NTE200, NTE240, TR100A).

Собирает: главы и разделы каталога с составом (артикул, количество,
наименование), инструкции по ремонту (TR100A — из service.js, NTE240 —
из HTML-страниц, NTE200 — оглавление PDF-руководств), цены.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bs4 import BeautifulSoup

from common import BUILD, NHL, save_json

CACHE = os.path.join(BUILD, "_cache", "machines")


def load_js(path):
    if not os.path.exists(path):
        return None
    s = open(path, encoding="utf-8").read()
    return json.loads(s[s.find("=") + 1:].rstrip().rstrip(";"))


def html_service(path):
    """Страница ремонта NTE240 -> Markdown."""
    soup = BeautifulSoup(open(path, encoding="utf-8").read(), "lxml")
    for t in soup.find_all(["script", "style"]):
        t.decompose()
    doc = soup.select_one("#doc")
    if not doc:
        return "", []
    out, imgs = [], []
    for el in doc.find_all(["p", "h1", "h2", "h3", "h4", "img", "li", "table"]):
        if el.name == "img":
            src = el.get("src") or ""
            name = os.path.basename(src)
            if name:
                imgs.append(name)
                out.append(f"\n![[{os.path.splitext(name)[0]}.jpg]]\n")
            continue
        txt = re.sub(r"\s+", " ", el.get_text(" ", strip=True))
        if not txt:
            continue
        if el.name in ("h1", "h2", "h3", "h4"):
            out.append(f"\n### {txt}\n")
        elif el.name == "li":
            out.append(f"- {txt}")
        else:
            out.append(txt + "\n")
    return "\n".join(out), imgs


ITEM_RE = re.compile(r"^\s*\d{1,2}\s*[-—.]\s*\S")


def _flush(buf, out):
    """Подписи к рисункам («1-рама, 2-втулка …») собираем в одну строку."""
    if not buf:
        return
    if len(buf) > 2 and all(ITEM_RE.match(x) for x in buf):
        out.append("**Позиции на рисунке:** " + "; ".join(
            re.sub(r"\s+", " ", x).strip() for x in buf))
    else:
        out.extend(buf)
    buf.clear()


def service_items_md(items):
    """service.js TR100A: список элементов -> Markdown."""
    out, imgs, buf = [], [], []
    for it in items:
        kind, x = it.get("t"), it.get("x", "")
        if kind == "img":
            _flush(buf, out)
            name = os.path.basename(x)
            imgs.append(name)
            out.append(f"\n![[{os.path.splitext(name)[0]}.jpg]]\n")
        elif kind == "head":
            _flush(buf, out)
            out.append(f"\n### {x}\n")
        elif kind == "step":
            _flush(buf, out)
            out.append(f"{x}")
        elif kind == "warn":
            _flush(buf, out)
            out.append(f"\n> [!warning] Предупреждение\n> {x}\n")
        else:
            if re.match(r"^\s*[△⚠]", x):
                _flush(buf, out)
                out.append(f"\n> [!warning] {x.strip()}\n")
            elif ITEM_RE.match(x) and len(x) < 60:
                buf.append(x)
            else:
                _flush(buf, out)
                out.append(x)
    _flush(buf, out)
    return "\n\n".join(out), imgs


def main():
    os.makedirs(CACHE, exist_ok=True)
    machines = {}

    for name, base in NHL.items():
        parts = load_js(os.path.join(base, "data", "parts.js")) or {}
        prices = load_js(os.path.join(base, "data", "prices.js")) or {}
        rec = {
            "name": name,
            "title_en": parts.get("title_en", ""),
            "title_zh": parts.get("title_zh", ""),
            "maker": parts.get("maker", ""),
            "serial": parts.get("serial", ""),
            "chapters": parts.get("chapters", []),
            "sections": parts.get("sections", []),
            "stats": parts.get("stats", {}),
            "prices": len(prices),
            "service": [],
            "manuals": [],
            "engine_sections": [],
        }

        # двигатель отдельной книгой (TR100A)
        eng = load_js(os.path.join(base, "data", "engine.js"))
        if eng:
            rec["engine_sections"] = eng.get("sections", [])
            rec["engine_chapters"] = eng.get("chapters", [])

        # инструкции по ремонту
        svc = load_js(os.path.join(base, "data", "service.js"))
        if isinstance(svc, dict) and "sections" in svc:          # TR100A
            for code, sec in svc["sections"].items():
                md, imgs = service_items_md(sec.get("items", []))
                fn = f"{name}_{code}.md"
                with open(os.path.join(CACHE, fn), "w", encoding="utf-8") as fh:
                    fh.write(md)
                rec["service"].append({"code": code, "title": sec.get("en") or sec.get("zh") or code,
                                       "zh": sec.get("zh", ""), "cache": fn, "images": imgs})
        elif isinstance(svc, dict):                              # NTE240: код -> название
            sdir = os.path.join(base, "service")
            for code, title in svc.items():
                page = os.path.join(sdir, code + ".html")
                if not os.path.exists(page):
                    continue
                md, imgs = html_service(page)
                fn = f"{name}_{code}.md"
                with open(os.path.join(CACHE, fn), "w", encoding="utf-8") as fh:
                    fh.write(md)
                rec["service"].append({"code": code, "title": title, "zh": "",
                                       "cache": fn, "images": imgs})

        # PDF-руководства (NTE200)
        man = load_js(os.path.join(base, "data", "manuals.js"))
        if man:
            rec["manuals"] = man.get("files", [])
            rec["repair_toc"] = man.get("repairToc", [])
            rec["wiring_toc"] = man.get("wiring", [])

        machines[name] = rec
        print(f"{name}: разделов {len(rec['sections'])}, "
              f"инструкций {len(rec['service'])}, руководств {len(rec['manuals'])}, "
              f"цен {rec['prices']}")

    save_json(os.path.join(BUILD, "state_machines.json"), machines)


if __name__ == "__main__":
    main()
