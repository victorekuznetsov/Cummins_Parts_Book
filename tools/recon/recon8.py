#!/usr/bin/env python3
# Разведка №8: карточка детали — атрибуты, размеры, замены номеров (supersession).
# Пробуем два пути: ссылка «View Part Details» в таблице узла и глобальный поиск по номеру.
import sys, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from playwright.sync_api import sync_playwright

ESN  = "37292556"
PART = sys.argv[1] if len(sys.argv) > 1 else "3092129"
SESS = Path(__file__).parent / "session"; SESS.mkdir(exist_ok=True)
traffic = open(SESS / f"traffic_part_{PART}.jsonl", "w", encoding="utf-8")
seen = set()

def on_resp(resp):
    try:
        url, req = resp.url, resp.request
        if "/gateway/" not in url: return
        ct = resp.headers.get("content-type", "")
        rec = {"method": req.method, "url": url, "status": resp.status, "ct": ct,
               "req_post": None, "resp_body": None}
        try: rec["req_post"] = req.post_data
        except Exception: pass
        if "json" in ct:
            try: rec["resp_body"] = resp.text()[:40000]
            except Exception: pass
        traffic.write(json.dumps(rec, ensure_ascii=False) + "\n"); traffic.flush()
        key = f'{req.method} {url.split("?")[0]}'
        if key not in seen:
            seen.add(key); print(f"  [{resp.status}] {key}")
    except Exception as e:
        print("  [err]", e)

def core(page, n=40):
    t = page.evaluate("() => document.body.innerText")
    c = t.split("Список Выбранных Деталей")[-1].split("Главная страница\nО нас")[0]
    return "\n".join("    " + l for l in c.splitlines()[:n] if l.strip())

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(viewport={"width": 1700, "height": 1300})
    page = ctx.new_page(); page.on("response", on_resp)
    page.goto("https://parts.cummins.com/home", wait_until="networkidle", timeout=120000)
    page.wait_for_timeout(2500)
    try:
        e = page.locator("#onetrust-accept-btn-handler").first
        if e.count() and e.is_visible(): e.click(timeout=6000)
    except Exception: pass
    page.wait_for_timeout(1200)

    print(f">>> ГЛОБАЛЬНЫЙ ПОИСК ПО НОМЕРУ ДЕТАЛИ {PART}")
    page.fill("#criteria", PART); page.press("#criteria", "Enter")
    page.wait_for_timeout(10000)
    print("    URL:", page.url)
    print(core(page, 30))
    page.screenshot(path=str(SESS / f"part_{PART}_search.png"), full_page=True)

    # ищем кликабельный результат-деталь
    clicked = False
    for sel in (f'a:has-text("{PART}")', f'*:text-is("{PART}")',
                'div[class*="result"] a', 'table tbody tr'):
        try:
            loc = page.locator(sel).first
            if loc.count() and loc.is_visible():
                print(f"    кликаю по '{sel}'")
                loc.click(timeout=10000); page.wait_for_timeout(10000)
                clicked = True; break
        except Exception:
            continue
    if clicked:
        print("    URL после клика:", page.url)
        print(core(page, 45))
        page.screenshot(path=str(SESS / f"part_{PART}_detail.png"), full_page=True)
        (SESS / f"part_{PART}_detail.html").write_text(page.content(), encoding="utf-8")

    # какие эндпоинты вообще есть для детали — пробуем известные варианты
    print("\n>>> ПРОБА ЭНДПОИНТОВ КАРТОЧКИ ДЕТАЛИ")
    xsrf = next((c["value"] for c in ctx.cookies() if c["name"] == "XSRF-TOKEN"), "")
    API = "https://parts.cummins.com/gateway/api/IACDataServices"
    cands = [
        f"/v2/partDetails/{PART}", f"/partDetails/{PART}",
        f"/v2/partInfo/{PART}", f"/protected/partService/part/{PART}",
        f"/v2/part/{PART}", f"/protected/searchService/filtered?criteria={PART}",
        f"/v2/parts/{PART}/supersession", f"/v2/partDetails?partNo={PART}",
    ]
    for c in cands:
        r = page.evaluate("""async ([u, x]) => {
            try {
              const r = await fetch(u, {credentials:'include',
                headers:{'accept':'application/json','x-xsrf-token':x}});
              const t = await r.text();
              return {s: r.status, n: t.length, head: t.slice(0,180)};
            } catch (e) { return {s:-1, n:0, head:String(e)}; }
        }""", [API + c, xsrf])
        print(f"    {r['s']:>4} {r['n']:>7}b  {c}")
        if r["s"] == 200 and r["n"] > 40:
            print("          ", r["head"][:170])
    b.close()
traffic.close()
print("\nГотово ->", SESS)
