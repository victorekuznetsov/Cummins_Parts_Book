#!/usr/bin/env python3
# Разведка №2: пройти по каталогу анонимно (раздел «Детали двигателя» -> модель
# -> узел -> список позиций) и записать ВСЕ вызовы gateway-API, чтобы понять,
# какими запросами тянутся дерево узлов, спецификации и чертежи.
import sys, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = Path(__file__).parent
SESS = BASE / "session"; SESS.mkdir(parents=True, exist_ok=True)
traffic = open(SESS / "traffic_catalog.jsonl", "w", encoding="utf-8")
seen = set()

def on_resp(resp):
    try:
        url = resp.url
        if "/gateway/" not in url:
            return
        req = resp.request
        ct = resp.headers.get("content-type", "")
        rec = {"method": req.method, "url": url, "status": resp.status, "ct": ct,
               "req_post": None, "resp_body": None}
        try: rec["req_post"] = req.post_data
        except Exception: pass
        if "json" in ct or "text" in ct:
            try: rec["resp_body"] = resp.text()[:20000]
            except Exception: pass
        traffic.write(json.dumps(rec, ensure_ascii=False) + "\n"); traffic.flush()
        key = f'{req.method} {re.sub(r"[0-9a-f]{8,}|\\d{4,}", "<id>", url.split("?")[0])}'
        if key not in seen:
            seen.add(key); print(f"  [API {resp.status}] {key}")
    except Exception as e:
        print("  [err]", e)

def dump(page, tag):
    (SESS / f"{tag}.html").write_text(page.content(), encoding="utf-8")
    try: page.screenshot(path=str(SESS / f"{tag}.png"), full_page=True)
    except Exception: pass
    txt = page.evaluate("() => document.body.innerText")
    (SESS / f"{tag}.txt").write_text(txt, encoding="utf-8")
    print(f"\n===== {tag} | {page.url}\n{txt[:1200]}\n")

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(viewport={"width": 1600, "height": 1200},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    page = ctx.new_page(); page.on("response", on_resp)

    print(">>> 1. Раздел «Детали двигателя»")
    page.goto("https://parts.cummins.com/engine-parts", wait_until="networkidle", timeout=90000)
    page.wait_for_timeout(3000)
    dump(page, "engine_parts")

    # собрать ссылки внутрь каталога
    links = page.evaluate("""() => [...document.querySelectorAll('a[href]')]
        .map(a => a.getAttribute('href')).filter(h => h && !h.startsWith('http'))""")
    inner = sorted(set(h for h in links if re.search(
        r"catalog|parts|product|engine|model|assembl|search", h, re.I)))
    print(">>> Внутренние ссылки каталога:")
    for h in inner[:50]: print("   ", h)
    (SESS / "links_engine_parts.json").write_text(
        json.dumps(inner, ensure_ascii=False, indent=1), encoding="utf-8")

    b.close()
traffic.close()
print("\nГотово ->", SESS)
