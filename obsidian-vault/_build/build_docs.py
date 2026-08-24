#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка заметок по документам QuickServe: TSB, процедуры, бюллетени,
STI, инструкции по установке, руководства (с полным оглавлением).

Результат: заметки в хранилище + kb_build/state_docs.json для индексов.
"""
import collections
import hashlib
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bs4 import BeautifulSoup

from common import (BUILD, CAT_DIR, CAT_RU, CAT_TAG, DIRS, DOC_ESN, PDF_BASE,
                    SRC, catalogs, frontmatter, iso_date, load_json, safe_name,
                    save_json, write_note)
from figures import FigureStore, pdf_images
from qs2md import Converter

BUL = os.path.join(SRC, "bulletins")
NUM_RE = re.compile(r"(?<![\w\-/])(\d{7,8})(?![\w\-/])")


# --------------------------------------------------------------- регистр
def html_title(path):
    try:
        head = open(path, encoding="utf-8", errors="replace").read(400000)
    except OSError:
        return ""
    m = re.search(r"<title>(.*?)</title>", head, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def build_registry():
    idx = load_json(os.path.join(BUL, "index.json"), [])
    tsb_meta = {}
    for f in os.listdir(os.path.join(SRC, "quickserve")):
        if f.startswith("tsb_") and f.endswith(".json"):
            for row in load_json(os.path.join(SRC, "quickserve", f), {}).get("data", []):
                tsb_meta.setdefault(row["doc_num"], row)

    reg = {}
    for d in idx:
        did, cat = d["id"], d["cat"]
        html = os.path.join(BUL, d["html"].replace("\\", "/"))
        pdf = os.path.join(BUL, d["pdf"].replace("\\", "/"))
        present = os.path.exists(html)
        title = html_title(html) if present else ""
        meta = tsb_meta.get(did, {})
        if not title:
            title = (meta.get("doc_title") or "").strip()
        entry = {
            "id": did, "cat": cat, "html": html, "pdf": pdf, "url": d["url"],
            "engines": d.get("engines", []), "title": title.strip() or did,
            "present": present,
            "group": (meta.get("group_name") or "").strip(),
            "released": meta.get("doc_date", ""),
            "year": meta.get("doc_year", ""),
            "pdf_rel": d["pdf"].replace("\\", "/"),
        }
        reg[(cat, did)] = entry
    return reg


def note_name(e):
    """Имя заметки документа: номер + английское название."""
    base = e["id"]
    if e["cat"] == "manual":
        base = re.sub(r"-history$", "", base)
    title = e["title"]
    if title and title.lower() != base.lower():
        return safe_name(f"{base} — {title}", 95)
    return safe_name(base, 95)


# ------------------------------------------------------- оглавления руководств
def manual_toc():
    """Из страниц истории руководств: оглавление и связь процедура->руководство."""
    toc = {}
    proc_man = collections.defaultdict(set)
    proc_sec = collections.defaultdict(set)
    for fn in sorted(os.listdir(os.path.join(BUL, "manual"))):
        if not fn.endswith("-history.html"):
            continue
        mid = fn.replace("-history.html", "")
        soup = BeautifulSoup(open(os.path.join(BUL, "manual", fn),
                                  encoding="utf-8", errors="replace").read(), "lxml")
        tab = soup.select_one("table.outline-history-table")
        rows = []
        if tab:
            for tr in tab.select("tbody tr"):
                tds = tr.find_all("td")
                if len(tds) < 4:
                    continue
                a = tds[2].find("a")
                if not a:
                    continue
                pid = a.get_text(strip=True)
                href = a.get("href", "")
                cat = "manual" if "/manual/" in href else "procedures"
                sec = re.sub(r"\s+", " ", tds[1].get_text(" ", strip=True))
                rows.append({
                    "date": tds[0].get_text(" ", strip=True),
                    "section": sec,
                    "id": pid,
                    "cat": cat,
                    "title": re.sub(r"\s+", " ", tds[3].get_text(" ", strip=True)),
                    "reason": tds[4].get_text(" ", strip=True) if len(tds) > 4 else "",
                })
                proc_man[(cat, pid)].add(mid)
                proc_sec[(cat, pid)].add(sec)
        toc[mid] = rows
    return toc, proc_man, proc_sec


# ------------------------------------------------------------------- сборка
def main():
    t0 = time.time()
    reg = build_registry()
    toc, proc_man, proc_sec = manual_toc()

    # каталожные артикулы — для перекрёстных ссылок из текста документов
    part_names = {}
    for cat in catalogs():
        for o in cat["options"]:
            for p in o["parts"]:
                part_names.setdefault(p["no"], p.get("name") or "")
        for k in cat["kits"]:
            for p in k["parts"]:
                part_names.setdefault(p["no"], p.get("name") or "")
        for no in cat["cards"]:
            part_names.setdefault(no, "")

    names = {}          # (cat, id) -> имя заметки
    for key, e in reg.items():
        names[key] = note_name(e)

    def resolve(cat, doc_id):
        for k in ((cat, doc_id), (cat, doc_id + "-history"),
                  ("manual", doc_id + "-history"), ("procedures", doc_id)):
            if k in names:
                return names[k]
        return None

    figs_dir = os.path.join(os.environ.get("KB_VAULT", "/home/user/kb_vault"), DIRS["fig"])
    store = FigureStore(figs_dir)
    known_hash = {}       # md5 -> имя файла
    retry = []            # документы с несовпавшим количеством картинок

    state = {"docs": {}, "manuals": {}, "figures": 0}
    stats = collections.Counter()

    order = sorted(reg.items(), key=lambda kv: (kv[1]["cat"], kv[0][1]))
    for n, ((cat, did), e) in enumerate(order, 1):
        if n % 250 == 0:
            print(f"  {n}/{len(order)} документов, {time.time()-t0:.0f} c", flush=True)
        used_parts = []
        md, meta, figs = "", {}, []
        if e["present"] and cat == "manual":
            # у руководств тело — это таблица истории; оглавление собираем отдельно
            meta = {"title": e["title"]}
        elif e["present"]:
            try:
                meta, md, figs = Converter(link_resolver=resolve).convert(
                    open(e["html"], encoding="utf-8", errors="replace").read())
            except Exception as exc:                      # noqa: BLE001
                stats["ошибка разбора"] += 1
                md = f"> [!bug] Документ не удалось разобрать: {exc}"
        else:
            stats["нет файла"] += 1

        # артикулы каталога, упомянутые в тексте
        found = {m for m in NUM_RE.findall(md) if m in part_names}
        if found:
            used_parts = sorted(found)

            def linkify(mo):
                v = mo.group(1)
                return f"[[{v}]]" if v in found else v

            out_lines = []
            for line in md.split("\n"):
                if line.startswith("![[") or "[[" in line:
                    out_lines.append(line)
                else:
                    out_lines.append(NUM_RE.sub(linkify, line))
            md = "\n".join(out_lines)

        # иллюстрации
        if figs and e["present"]:
            fnames = [f.rsplit("/", 1)[-1] for f in figs]
            blobs = pdf_images(e["pdf"])
            if len(blobs) == len(fnames):
                for nm, blob in zip(fnames, blobs):
                    if store.add(nm, blob):
                        known_hash.setdefault(hashlib.md5(blob).hexdigest(), nm)
                stats["картинки точно"] += 1
            else:
                retry.append(((cat, did), fnames))
                stats["картинки отложены"] += 1

        state["docs"][f"{cat}|{did}"] = {
            "id": did, "cat": cat, "note": names[(cat, did)],
            "title": e["title"], "engines": e["engines"], "group": e["group"],
            "released": iso_date(meta.get("released") or "") or (
                iso_date(e["released"]) if e["released"] else ""),
            "modified": iso_date(meta.get("modified") or ""),
            "revision": meta.get("revision", ""),
            "parts": used_parts,
            "manuals": sorted(proc_man.get((cat, did), [])),
            "sections": sorted(proc_sec.get((cat, did), [])),
            "present": e["present"],
            "figures": len(figs),
            "url": e["url"],
            "pdf_rel": e["pdf_rel"],
        }
        state["docs"][f"{cat}|{did}"]["meta"] = meta
        cache = os.path.join(BUILD, "_cache", cat)
        os.makedirs(cache, exist_ok=True)
        with open(os.path.join(cache, did + ".md"), "w", encoding="utf-8") as fh:
            fh.write(md)

    # второй проход по «сложным» документам: сопоставляем по уже известным хэшам
    print(f"  второй проход: {len(retry)} документов", flush=True)
    for (cat, did), fnames in retry:
        e = reg[(cat, did)]
        blobs = pdf_images(e["pdf"])
        free = list(fnames)
        rest = []
        for blob in blobs:
            h = hashlib.md5(blob).hexdigest()
            nm = known_hash.get(h)
            if nm and nm in free:
                free.remove(nm)
                store.add(nm, blob)
            else:
                rest.append(blob)
        for nm, blob in zip(free, rest):
            if store.add(nm, blob):
                known_hash.setdefault(hashlib.md5(blob).hexdigest(), nm)

    state["figures"] = len(store.saved)
    state["manual_toc"] = toc
    state["names"] = {f"{c}|{i}": v for (c, i), v in names.items()}
    save_json(os.path.join(BUILD, "state_docs.json"), state)
    print("картинок сохранено:", len(store.saved),
          "| конфликтов:", len(store.conflicts), "|", dict(stats),
          f"| {time.time()-t0:.0f} c")


if __name__ == "__main__":
    main()
