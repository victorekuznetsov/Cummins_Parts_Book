#!/usr/bin/env python3
# Перечисление ВСЕХ документов сервисной библиотеки по каждому ESN.
import sys, io, os, json, re, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", write_through=True)
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
ESNS = ["33239899", "37292556", "41353297", "41370103", "93087701"]

# нормализация ссылки документа -> (категория, канонический путь)
CAT_RE = re.compile(r"/qs3/pubsys2/xml/\w+/(tsb|bulletin|manual|install_inst|sti|outlines|procedures)/")

def categorize(href):
    m = CAT_RE.search(href)
    return m.group(1) if m else None

docs = {}   # url -> {cat, engines:set}
def add(url, esn, cat=None):
    url = url.split("#")[0]
    cat = cat or categorize(url) or "other"
    d = docs.setdefault(url, {"cat": cat, "engines": set()})
    d["engines"].add(esn)

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True)
    ctx = b.new_context(storage_state=os.path.join(BASE, "storage_state.json"))
    pg = ctx.new_page()
    for esn in ESNS:
        pg.goto(f"https://quickserve.cummins.com/qs3/portal/includes/ajax/set_esn.json?esn={esn}", timeout=30000)
        pg.goto("https://quickserve.cummins.com/qs3/portal/service/index.html", wait_until="networkidle", timeout=60000)
        pg.wait_for_timeout(3500)
        hrefs = pg.eval_on_selector_all("a[href]", "els=>els.map(e=>e.getAttribute('href'))")
        cnt = 0
        for h in hrefs:
            if not h: continue
            # прямые pubsys ссылки
            if "/qs3/pubsys2/xml/" in h:
                # manualviewer?path=/qs3/pubsys2/...
                m = re.search(r"path=(/qs3/pubsys2/xml/[^&]+)", h)
                url = m.group(1) if m else h
                if not url.startswith("http"):
                    url = "https://quickserve.cummins.com" + url
                add(url, esn); cnt += 1
        # бюллетени из filter_tsb.json
        tsbf = os.path.join(BASE, f"tsb_{esn}.json")
        if os.path.exists(tsbf):
            for x in json.load(open(tsbf, encoding="utf-8"))["data"]:
                if x["doc_type"] == "37":
                    u = f"https://quickserve.cummins.com/qs3/pubsys2/xml/{x['language']}/tsb/{x['doc_year']}/{x['doc_num']}.html"
                else:
                    u = f"https://quickserve.cummins.com/qs3/pubsys2/xml/{x['language']}/bulletin/{x['doc_num']}.html"
                add(u, esn)
        print(f"{esn}: ссылок на странице сервиса={cnt}, накоплено уникальных={len(docs)}")
    b.close()

# сводка по категориям
from collections import Counter
cats = Counter(d["cat"] for d in docs.values())
print("\n=== по категориям ===")
for c, n in cats.most_common():
    print(f"  {c}: {n}")
print("ВСЕГО уникальных документов:", len(docs))

# сохранить манифест
out = [{"url": u, "cat": d["cat"], "engines": sorted(d["engines"])} for u, d in docs.items()]
json.dump(out, open(os.path.join(BASE, "doc_manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("манифест -> doc_manifest.json")
