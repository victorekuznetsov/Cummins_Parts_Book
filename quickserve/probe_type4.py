#!/usr/bin/env python3
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", write_through=True)
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True)
    ctx = b.new_context(storage_state="storage_state.json")
    pg = ctx.new_page()
    pg.goto("https://quickserve.cummins.com/qs3/portal/includes/ajax/set_esn.json?esn=33239899&nocache=1",
            wait_until="domcontentloaded", timeout=30000)
    pg.goto("https://quickserve.cummins.com/qs3/portal/service/index.html",
            wait_until="networkidle", timeout=45000)
    pg.wait_for_timeout(3500)
    html = pg.content()
    # функции открытия документа
    print("doc-функции:", sorted(set(re.findall(r"function\s+(\w*(?:[Dd]oc|[Tt]sb|[Tt]opic)\w*)\s*\(", html))))
    # ссылки, ведущие к документам
    links = pg.eval_on_selector_all("a", """els=>els.map(e=>({t:(e.innerText||'').trim().slice(0,25),
        href:e.getAttribute('href')||'', onclick:e.getAttribute('onclick')||''}))
        .filter(x=>/tsb|pubsys|openDoc|5659|doc_type|topic|servlet/i.test(x.href+x.onclick))""")
    print("ссылок-документов:", len(links))
    for l in links[:20]:
        print("  ", l)
    # найдём в html любые строки с pubsys2 путями
    paths = sorted(set(re.findall(r"/qs3/pubsys2/[^\s\"'<>]+", html)))
    print("pubsys2-пути в HTML:", paths[:10])
    # как строится ссылка: ищем шаблоны с doc_type/file_name
    for m in re.finditer(r"[^\n]{0,80}(doc_type|file_name|pubsys2/xml)[^\n]{0,120}", html):
        s = m.group(0).strip()
        if "pubsys2" in s or "doc_type" in s:
            print("  ~", s[:180])
    b.close()
