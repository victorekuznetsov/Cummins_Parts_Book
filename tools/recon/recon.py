#!/usr/bin/env python3
# Разведка parts.cummins.com (Cummins ePartsCatalog, Angular SPA):
# что грузится анонимно, какие API дёргает фронт, нужен ли логин.
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = Path(__file__).parent
SESS = BASE / "session"; SESS.mkdir(parents=True, exist_ok=True)
traffic = open(SESS / "traffic_anon.jsonl", "w", encoding="utf-8")
seen = set()

def on_resp(resp):
    try:
        url = resp.url
        if not any(k in url for k in ("/api/", "/service", "/rest/", "graphql", "/v1/", "/v2/")):
            return
        req = resp.request
        ct = resp.headers.get("content-type", "")
        rec = {"method": req.method, "url": url, "status": resp.status, "ct": ct,
               "req_headers": dict(req.headers), "req_post": None, "resp_body": None}
        try: rec["req_post"] = req.post_data
        except Exception: pass
        if "json" in ct or "text" in ct:
            try: rec["resp_body"] = resp.text()[:6000]
            except Exception: pass
        traffic.write(json.dumps(rec, ensure_ascii=False) + "\n"); traffic.flush()
        key = f'{req.method} {url.split("?")[0]}'
        if key not in seen:
            seen.add(key); print(f"  [API {resp.status}] {key}")
    except Exception as e:
        print("  [err]", e)

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(viewport={"width": 1600, "height": 1000},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    page = ctx.new_page()
    page.on("response", on_resp)
    print("Открываю https://parts.cummins.com/home ...")
    page.goto("https://parts.cummins.com/home", wait_until="networkidle", timeout=90000)
    page.wait_for_timeout(4000)
    print("URL после загрузки:", page.url)
    (SESS / "home_dom.html").write_text(page.content(), encoding="utf-8")
    page.screenshot(path=str(SESS / "home.png"), full_page=True)
    txt = page.evaluate("() => document.body.innerText")
    (SESS / "home_text.txt").write_text(txt, encoding="utf-8")
    print("\n--- ВИДИМЫЙ ТЕКСТ (первые 2500 симв.) ---\n", txt[:2500])
    inputs = page.evaluate("""() => [...document.querySelectorAll('input,button,a')]
        .slice(0,80).map(e => ({t:e.tagName, ph:e.placeholder||'', id:e.id||'',
                                nm:e.name||'', txt:(e.innerText||'').trim().slice(0,60)}))""")
    print("\n--- ЭЛЕМЕНТЫ УПРАВЛЕНИЯ ---")
    for i in inputs:
        if i["ph"] or i["txt"] or i["id"]:
            print(" ", i)
    b.close()
traffic.close()
print("\nГотово ->", SESS)
