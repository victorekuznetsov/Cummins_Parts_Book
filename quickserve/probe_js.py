#!/usr/bin/env python3
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", write_through=True)
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True)
    ctx = b.new_context(storage_state="storage_state.json"); pg = ctx.new_page()
    pg.goto("https://quickserve.cummins.com/qs3/portal/includes/ajax/set_esn.json?esn=33239899", timeout=30000)
    pg.goto("https://quickserve.cummins.com/qs3/portal/service/index.html", wait_until="networkidle", timeout=45000)
    pg.wait_for_timeout(2500)
    js = pg.evaluate("()=>{let s='';document.querySelectorAll('script').forEach(e=>s+=(e.textContent||'')+'\\n');return s;}")
    b.close()

# все строки buffer.push со ссылками
for m in re.finditer(r"buffer\.push\([^\n]{0,220}", js):
    seg = m.group(0)
    if any(k in seg for k in ("href", "pubsys", "onclick", "file_name", "doc_num", ".html", "<a ")):
        print("PUSH:", seg.strip()[:220])
print("\n--- любые шаблоны pubsys2 в JS ---")
for m in set(re.findall(r"['\"][^'\"]*pubsys2[^'\"]*['\"]", js)):
    print("  ", m[:160])
print("\n--- переменные с путями (var xxx = '/qs3...') ---")
for m in re.finditer(r"(var\s+\w+\s*=\s*['\"][^'\"]*(?:tsb|pubsys|install|sti|manual)[^'\"]*['\"])", js):
    print("  ", m.group(1)[:160])
