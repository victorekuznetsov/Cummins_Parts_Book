#!/usr/bin/env python3
# Второй проход: контент 35 мануалов через manualviewer (не только -history).
import sys, io, os, json, re, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", write_through=True)
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = r"C:\Projects\cummins\bulletins\manual"
idx = json.load(open(r"C:\Projects\cummins\bulletins\index.json", encoding="utf-8"))
manuals = sorted(set(re.sub(r"-history$", "", d["id"]) for d in idx if d["cat"] == "manual"))
print("мануалов:", len(manuals))

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True)
    ctx = b.new_context(storage_state=os.path.join(BASE, "storage_state.json"))
    pg = ctx.new_page()
    rows = []
    for i, mid in enumerate(manuals, 1):
        content_url = f"https://quickserve.cummins.com/qs3/portal/manualviewer.html?path=/qs3/pubsys2/xml/en/manual/{mid}/{mid}.html"
        fh = os.path.join(OUT, mid + "-content.html")
        fp = os.path.join(OUT, mid + "-content.pdf")
        try:
            pg.goto(content_url, wait_until="networkidle", timeout=45000)
            pg.wait_for_timeout(2000)
            txt = pg.inner_text("body")
            # ссылки внутри (признак дерева процедур)
            sub = pg.eval_on_selector_all("a[href]", "els=>els.map(e=>e.getAttribute('href')).filter(h=>h&&/manual|procedures|section|chapter/i.test(h))")
            open(fh, "w", encoding="utf-8").write(pg.content())
            pg.pdf(path=fp, format="A4", print_background=True)
            rows.append((mid, len(txt), len(sub)))
            print(f"[{i}/{len(manuals)}] {mid}: текст={len(txt)} симв, вложенных ссылок={len(sub)}")
        except Exception as e:
            print(f"[{i}/{len(manuals)}] {mid}: ERR {str(e)[:70]}")
        time.sleep(0.2)
    b.close()
tl = [r[1] for r in rows]
print(f"\nмедиана текста: {sorted(tl)[len(tl)//2] if tl else 0} симв; макс: {max(tl) if tl else 0}")
print("с вложенными ссылками (дерево процедур):", sum(1 for r in rows if r[2] > 0), "из", len(rows))
