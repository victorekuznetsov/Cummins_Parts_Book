#!/usr/bin/env python3
# Разведка №3: выполнить поиск в шапке (по номеру детали / описанию) и записать
# вызовы searchService, чтобы понять формат запроса и ответа.
# Если задан аргумент - ищем его (например, ESN), иначе номер детали по умолчанию.
import sys, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

from pathlib import Path
from playwright.sync_api import sync_playwright

QUERY = sys.argv[1] if len(sys.argv) > 1 else "3979820"
TAG   = re.sub(r"\W+", "_", QUERY)

BASE = Path(__file__).parent
SESS = BASE / "session"; SESS.mkdir(parents=True, exist_ok=True)
traffic = open(SESS / f"traffic_search_{TAG}.jsonl", "w", encoding="utf-8")
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
            try: rec["resp_body"] = resp.text()[:40000]
            except Exception: pass
        traffic.write(json.dumps(rec, ensure_ascii=False) + "\n"); traffic.flush()
        key = f'{req.method} {url.split("?")[0]}'
        if key not in seen:
            seen.add(key); print(f"  [API {resp.status}] {key}")
    except Exception as e:
        print("  [err]", e)

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(viewport={"width": 1600, "height": 1200},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    page = ctx.new_page(); page.on("response", on_resp)

    page.goto("https://parts.cummins.com/home", wait_until="networkidle", timeout=90000)
    page.wait_for_timeout(2500)

    print(f">>> Ищу: {QUERY}")
    page.fill("#criteria", QUERY)
    page.press("#criteria", "Enter")
    page.wait_for_timeout(9000)
    try: page.wait_for_load_state("networkidle", timeout=30000)
    except Exception: pass

    print(">>> URL результата:", page.url)
    txt = page.evaluate("() => document.body.innerText")
    (SESS / f"search_{TAG}.txt").write_text(txt, encoding="utf-8")
    (SESS / f"search_{TAG}.html").write_text(page.content(), encoding="utf-8")
    page.screenshot(path=str(SESS / f"search_{TAG}.png"), full_page=True)
    # обрезаем шапку/подвал — печатаем середину страницы
    print("\n--- ТЕКСТ РЕЗУЛЬТАТА ---\n", txt[:3000])

    hrefs = page.evaluate("""() => [...document.querySelectorAll('a[href]')]
        .map(a => a.getAttribute('href'))""")
    inner = sorted(set(h for h in hrefs if h and not h.startswith("http")
                       and not h.startswith("#") and len(h) > 1))
    print("\n--- ССЫЛКИ ---")
    for h in inner[:60]: print("   ", h)

    b.close()
traffic.close()
print("\nГотово ->", SESS)
