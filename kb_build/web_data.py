#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка данных для веб-каталога с базой знаний.

Читает состояния, собранные для хранилища Obsidian (state_*.json и
кэш Markdown), и превращает их в JS-файлы, которые грузятся в браузере
без сервера: индекс документов, тела документов чанками, индекс деталей,
каталоги машин, темы и поисковый индекс.
"""
import collections
import csv
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import BUILD, CAT_RU, DOC_ESN, FAMILY_OF_CAT, NHL, load_json, catalogs
from web_render import Renderer

WEB = os.environ.get("KB_WEB", "/home/user/kb_web")
CACHE = os.path.join(BUILD, "_cache")
CHUNK = 100                     # документов в одном файле тел

# оригинальный путь иллюстрации на сервере Cummins: 08600044.png ->
# /rtgraphics/english/service/08/6/08600044.png
QS_IMG = "https://quickserve.cummins.com/rtgraphics/english/service/{a}/{b}/{name}"


def js(path, varname, obj, mode="w"):
    full = os.path.join(WEB, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, mode, encoding="utf-8") as fh:
        fh.write(f"{varname}=" + json.dumps(obj, ensure_ascii=False,
                                            separators=(",", ":")) + ";\n")
    return os.path.getsize(full)


FIG_DIR = os.path.join(os.environ.get("KB_VAULT", "/home/user/kb_vault"),
                       "90 Приложения", "Иллюстрации")
FIGURES = set(os.listdir(FIG_DIR)) if os.path.isdir(FIG_DIR) else set()


def image_url(name):
    """(локальный путь либо None, запасной адрес на сервере Cummins)."""
    base = os.path.splitext(name)[0]
    fallback = ""
    if len(base) >= 3:
        fallback = QS_IMG.format(a=base[:2].lower(), b=base[2].lower(), name=name)
    local = "assets/figures/" + name if name in FIGURES else None
    return local, fallback


VAULT = os.environ.get("KB_VAULT", "/home/user/kb_vault")


def media_map():
    """Реальные имена файлов графики машин: основа имени -> файл."""
    out = {}
    root = os.path.join(VAULT, "90 Приложения", "Медиа машин")
    if not os.path.isdir(root):
        return out
    for machine in sorted(os.listdir(root)):
        d = os.path.join(root, machine)
        if not os.path.isdir(d):
            continue
        out[machine] = {os.path.splitext(f)[0]: f for f in os.listdir(d)}
    return out


def machine_parts():
    """Детали машин NHL из all_part_numbers.csv: русские имена, цены, разделы."""
    out = {}
    for machine, base in NHL.items():
        path = os.path.join(base, "data", "all_part_numbers.csv")
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8-sig", newline="") as fh:
            for row in csv.DictReader(fh):
                no = (row.get("Артикул (Part No.)") or "").strip()
                no = re.sub(r'^="?|"?"$|"', "", no).strip()
                if not no:
                    continue
                rec = out.setdefault(no, {"ru": "", "en": "", "zh": "", "gr": "",
                                          "alt": "", "m": {}})
                rec["ru"] = rec["ru"] or (row.get("Наименование (RU)") or "").strip()
                rec["en"] = rec["en"] or (row.get("Description (EN)") or "").strip()
                rec["zh"] = rec["zh"] or (row.get("Description (ZH)") or "").strip()
                rec["gr"] = rec["gr"] or (row.get("Группа") or "").strip()
                rec["alt"] = rec["alt"] or (row.get("Взаимозаменяемый артикул") or "").strip()
                price = (row.get("Цена, CNY без НДС") or "").strip()
                secs = [s for s in (row.get("Разделы") or "").split() if s]
                rec["m"][machine] = {"p": price, "s": secs}
    return out


def main():
    docs_state = load_json(os.path.join(BUILD, "state_docs.json"), {})
    cat_state = load_json(os.path.join(BUILD, "state_catalog.json"), {})
    machines = load_json(os.path.join(BUILD, "state_machines.json"), {})
    links = load_json(os.path.join(BUILD, "state_links.json"), {})
    ru_docs = load_json(os.path.join(BUILD, "ru_docs.json"), {})
    ru_parts = load_json(os.path.join(BUILD, "ru_parts.json"), {})

    docs = docs_state.get("docs", {})
    names = docs_state.get("names", {})       # "cat|id" -> имя заметки
    toc = docs_state.get("manual_toc", {})
    parts = cat_state.get("parts", {})
    part_docs = links.get("part_docs", {})

    # имя заметки -> маршрут
    note_route = {}
    for key, note in names.items():
        cat, did = key.split("|", 1)
        route = f"#/manual/{did.replace('-history', '')}" if cat == "manual" \
            else f"#/doc/{did}"
        note_route[note] = (route, "lnk doc")
    for no in parts:
        note_route[no] = (f"#/part/{no}", "lnk part")

    def resolve(target):
        if target in note_route:
            return note_route[target]
        return None

    # номера документов в тексте: процедуры, TSB, руководства и артикулы
    doc_ids = {d["id"] for d in docs.values() if d["cat"] != "manual"}
    man_ids = {d["id"].replace("-history", "") for d in docs.values()
               if d["cat"] == "manual"}

    def ref(kind, num):
        if kind == "manual":
            if num in man_ids:
                return f"#/manual/{num}"
            return f"#/part/{num}" if num in parts else None
        return f"#/doc/{num}" if num in doc_ids else None

    media = media_map()
    manuals_rows = toc
    rend = Renderer(resolve, image_url, ref)

    # ------------------------------------------------- документы: индекс и тела
    order = sorted(docs.keys())
    index = {}
    chunk_of = {}
    chunks = collections.defaultdict(dict)
    chunks_ru = collections.defaultdict(dict)
    cache_ru = os.path.join(BUILD, "_cache_ru")
    stats = collections.Counter()

    for n, key in enumerate(order):
        d = docs[key]
        did, cat = d["id"], d["cat"]
        ru = ru_docs.get(d.get("title") or "", "")
        body = ""
        cache_file = os.path.join(CACHE, cat, did + ".md")
        if os.path.exists(cache_file):
            body = rend.render(open(cache_file, encoding="utf-8").read())
        body_ru = ""
        ru_file = os.path.join(cache_ru, cat, did + ".md")
        if os.path.exists(ru_file):
            body_ru = rend.render(open(ru_file, encoding="utf-8").read())
        chunk = n // CHUNK
        if cat != "manual":
            chunks[chunk][did] = body
            if body_ru:
                chunks_ru[chunk][did] = body_ru
                stats["с переводом"] += 1
            chunk_of[did] = chunk
        fams = sorted({FAMILY_OF_CAT.get(e, ("", ""))[0]
                       for e in d.get("engines", []) if e in FAMILY_OF_CAT} |
                      {DOC_ESN[e][0] for e in d.get("engines", []) if e in DOC_ESN})
        index[did] = {
            "c": cat,
            "t": d.get("title") or did,
            "ru": ru,
            "d": d.get("released", ""),
            "mo": d.get("modified", ""),
            "g": d.get("group", ""),
            "e": sorted({c for e in d.get("engines", []) if e in DOC_ESN
                         for c in DOC_ESN[e][1]}),
            "f": [f for f in fams if f],
            "mn": d.get("manuals", []),
            "sec": d.get("sections", [])[:8],
            "p": d.get("parts", []),
            "u": d.get("url", ""),
            "pdf": d.get("pdf_rel", ""),
            "ok": 1 if d.get("present") else 0,
            "ch": chunk_of.get(did, -1),
            "ru_body": 1 if (body_ru and cat != "manual") else 0,
        }
        stats[cat] += 1

    # обратные ссылки: кто ссылается на этот документ
    back = collections.defaultdict(set)
    href = re.compile(r'href="#/(doc|manual)/([^"]+)"')
    for ch, obj in chunks.items():
        for src, body in obj.items():
            for kind, tgt in href.findall(body):
                if tgt != src:
                    back[tgt].add(src)
    for mid, m in manuals_rows.items():
        for r in m:
            if r["id"] != mid:
                back[r["id"]].add(mid)
    for did, ids in back.items():
        if did in index:
            index[did]["bl"] = sorted(ids)[:200]

    for ch, obj in chunks.items():
        js(f"data/kb/body_{ch}.js", f"window.KB_BODY[{ch}]", obj)
    for ch, obj in chunks_ru.items():
        js(f"data/kb/body_ru_{ch}.js", f"window.KB_BODY_RU[{ch}]", obj)

    js("data/kb_docs.js", "window.KB_DOCS", index)

    # ------------------------------------------------------------- руководства
    manuals = {}
    for mid, rows in toc.items():
        key = f"manual|{mid}-history"
        d = docs.get(key, {})
        secs = collections.OrderedDict()
        for r in rows:
            secs.setdefault(r["section"] or "Без секции", []).append(
                [r["id"], r["title"], r["date"] if r["date"] != "Not Available" else "",
                 1 if r["cat"] == "manual" else 0])
        manuals[mid] = {
            "t": d.get("title") or mid,
            "ru": ru_docs.get(d.get("title") or "", ""),
            "e": sorted({c for e in d.get("engines", []) if e in DOC_ESN
                         for c in DOC_ESN[e][1]}),
            "u": d.get("url", ""),
            "pdf": d.get("pdf_rel", ""),
            "n": len(rows),
            "s": [[name, items] for name, items in secs.items()],
        }
    js("data/kb_manuals.js", "window.KB_MANUALS", manuals)

    # ------------------------------------------------------------------ детали
    pindex = {}
    for no, p in parts.items():
        name = p.get("name", "")
        rec = {
            "ru": p.get("name_ru") or ru_parts.get(name.upper()) or ru_parts.get(name) or "",
            "n": name,
            "e": p.get("engines", []),
            "d": part_docs.get(no, []),
        }
        card = p.get("card") or {}
        if card.get("sup"):
            rec["sup"] = [[s["no"], s.get("st", ""), 1 if s.get("sell") else 0]
                          for s in card["sup"]]
        if p.get("price"):
            rec["pr"] = {m: v["price"] for m, v in p["price"].items()}
        if p.get("photos"):
            rec["ph"] = [u.rsplit("/", 1)[-1] for u in p["photos"][:4]]
        pindex[no] = rec
    js("data/kb_parts.js", "window.KB_PARTS", pindex)

    # русские названия узлов и комплектов — для каталога
    opt_ru = {}
    for key, o in cat_state.get("options", {}).items():
        nm = o.get("name") or ""
        r = ru_parts.get(nm.upper()) or ru_parts.get(nm) or ""
        if r:
            opt_ru[o["no"]] = r
    kit_ru = {}
    for key, k in cat_state.get("kits", {}).items():
        nm = k.get("name") or ""
        r = ru_parts.get(nm.upper()) or ru_parts.get(nm) or ""
        if r:
            kit_ru[k["no"]] = r
    js("data/kb_names.js", "window.KB_NAMES",
       {"opt": opt_ru, "kit": kit_ru, "part": {no: p["ru"] for no, p in pindex.items() if p["ru"]}})

    # ------------------------------------------------------------------ машины
    mparts = machine_parts()
    js("data/kb_mparts.js", "window.KB_MPARTS", mparts)

    mindex = {}
    for name, m in machines.items():
        secs = []
        for s in m.get("sections", []):
            secs.append({
                "c": s.get("code", ""), "en": s.get("en", ""), "zh": s.get("zh", ""),
                "ch": s.get("chapter", ""),
                "f": [{"i": [os.path.basename(x) for x in fig.get("images", [])],
                       "p": [[p.get("ref", ""), p.get("pn", ""), p.get("en", ""),
                              p.get("zh", ""), p.get("qty", "")]
                             for p in fig.get("parts", [])]}
                      for fig in s.get("figures", [])],
            })
        eng_secs = []
        for s in m.get("engine_sections", []):
            eng_secs.append({
                "c": s.get("code", ""), "en": s.get("en", ""), "zh": s.get("zh", ""),
                "g": s.get("group", ""),
                "f": [{"i": [os.path.basename(x) for x in fig.get("images", [])],
                       "p": [[p.get("ref", ""), p.get("pn", ""), p.get("en", ""),
                              p.get("zh", ""), p.get("qty", "")]
                             for p in fig.get("parts", [])]}
                      for fig in s.get("figures", [])],
            })
        svc = []
        for s in m.get("service", []):
            cache_file = os.path.join(CACHE, "machines", s["cache"])
            body = ""
            if os.path.exists(cache_file):
                md = open(cache_file, encoding="utf-8").read()
                md = re.sub(r"!\[\[([^\]]+)\]\]",
                            lambda mo: f"![[{name}_{mo.group(1)}]]", md)
                body = rend_machine(rend, name, media.get(name, {})).render(md)
            svc.append({"c": s["code"], "t": s["title"], "b": body})
        mindex[name] = {
            "t": m.get("title_en", ""), "zh": m.get("title_zh", ""),
            "maker": m.get("maker", ""),
            "ch": m.get("chapters", []),
            "s": secs, "es": eng_secs, "svc": svc,
            "man": m.get("manuals", []),
            "toc": m.get("repair_toc", []),
            "wir": m.get("wiring_toc", []),
        }
        js(f"data/kb/machine_{name}.js", f"window.KB_MACHINE['{name}']", mindex[name])

    js("data/kb_media.js", "window.KB_MEDIA", media)

    # какие фотографии деталей лежат локально
    photo_dir = os.path.join(WEB, "assets", "photos")
    photos = sorted(os.path.splitext(f)[0] for f in os.listdir(photo_dir)) \
        if os.path.isdir(photo_dir) else []
    js("data/kb_photos.js", "window.KB_PHOTOS", photos)

    js("data/kb_machines.js", "window.KB_MACHINE_LIST",
       {k: {"t": v["t"], "zh": v["zh"], "maker": v["maker"],
            "ns": len(v["s"]), "nsvc": len(v["svc"]), "nes": len(v["es"]),
            "ch": v["ch"], "man": v["man"]}
        for k, v in mindex.items()})

    # ------------------------------------------------------------------- темы
    from build_index import TOPICS, topic_match
    topics = []
    for tname, desc, keys in TOPICS:
        ids = [did for did, d in index.items()
               if topic_match(d["t"], keys) or topic_match(d["ru"], keys)]
        topics.append({"t": tname, "d": desc, "ids": sorted(ids)})
    js("data/kb_topics.js", "window.KB_TOPICS", topics)

    # --------------------------------------------------------- поисковый индекс
    search = []
    for did, d in index.items():
        search.append([did, d["t"], d["ru"], d["c"]])
    js("data/kb_search.js", "window.KB_SEARCH", search)

    total = 0
    for root, _dirs, files in os.walk(os.path.join(WEB, "data")):
        for f in files:
            total += os.path.getsize(os.path.join(root, f))
    print("документов:", dict(stats))
    print("чанков тел:", len(chunks), "| деталей:", len(pindex),
          "| деталей машин:", len(mparts), "| руководств:", len(manuals))
    print(f"объём data/: {total/1048576:.1f} МБ")


def rend_machine(base, machine, names):
    """Тот же рендерер, но картинки машин лежат в assets/machines/."""
    def image(name):
        real = names.get(os.path.splitext(name)[0])
        return (f"assets/machines/{machine}/{real}" if real else None), ""
    return Renderer(base.resolve, image, base.ref)


if __name__ == "__main__":
    main()
