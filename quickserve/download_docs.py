#!/usr/bin/env python3
# Скачивание документов QSOL: каждый -> HTML + PDF. Резюмируемо.
import sys, io, os, json, re, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", write_through=True)
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = r"C:\Projects\cummins\bulletins"
MAN = json.load(open(os.path.join(BASE, "doc_manifest.json"), encoding="utf-8"))

def doc_id(url):
    seg = url.split("?")[0].rstrip("/").split("/")[-1]
    return re.sub(r"\.html?$", "", seg)

stats = {"ok": 0, "skip": 0, "notfound": 0, "err": 0}
index = []

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True)
    ctx = b.new_context(storage_state=os.path.join(BASE, "storage_state.json"))
    pg = ctx.new_page()
    for i, d in enumerate(MAN, 1):
        url, cat = d["url"], d["cat"]
        did = doc_id(url)
        cdir = os.path.join(OUT, cat)
        os.makedirs(cdir, exist_ok=True)
        fhtml = os.path.join(cdir, did + ".html")
        fpdf = os.path.join(cdir, did + ".pdf")
        rec = {"id": did, "cat": cat, "url": url, "engines": d["engines"],
               "html": os.path.relpath(fhtml, OUT), "pdf": os.path.relpath(fpdf, OUT)}
        if os.path.exists(fhtml) and os.path.exists(fpdf) and os.path.getsize(fpdf) > 1000:
            stats["skip"] += 1; index.append(rec); continue
        try:
            pg.goto(url, wait_until="networkidle", timeout=45000)
            pg.wait_for_timeout(900)
            txt = pg.inner_text("body")[:400]
            if "File not found" in txt and len(txt) < 40:
                stats["notfound"] += 1
                print(f"[{i}/{len(MAN)}] 404 {cat}/{did}")
                rec["missing"] = True; index.append(rec); continue
            open(fhtml, "w", encoding="utf-8").write(pg.content())
            pg.pdf(path=fpdf, format="A4", print_background=True,
                   margin={"top": "10mm", "bottom": "10mm", "left": "8mm", "right": "8mm"})
            stats["ok"] += 1; index.append(rec)
            if stats["ok"] % 25 == 0:
                print(f"[{i}/{len(MAN)}] ok={stats['ok']} skip={stats['skip']} 404={stats['notfound']}")
        except Exception as e:
            stats["err"] += 1
            print(f"[{i}/{len(MAN)}] ERR {cat}/{did}: {str(e)[:80]}")
        time.sleep(0.15)
    b.close()

json.dump(index, open(os.path.join(OUT, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"\nИТОГО ok={stats['ok']} skip={stats['skip']} 404={stats['notfound']} err={stats['err']}")
print("index.json ->", os.path.join(OUT, "index.json"))
