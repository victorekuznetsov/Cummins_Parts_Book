#!/usr/bin/env python3
# Разведка №7: что ещё отдаёт сайт по ESN —
#   вкладка «Информация об изделии», карточка детали (View Part Details),
#   картинки систем и общий вид двигателя.
import sys, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from playwright.sync_api import sync_playwright

ESN  = sys.argv[1] if len(sys.argv) > 1 else "37292556"
SESS = Path(__file__).parent / "session"; SESS.mkdir(exist_ok=True)
traffic = open(SESS / f"traffic_extra_{ESN}.jsonl", "w", encoding="utf-8")
seen = set()

def on_resp(resp):
    try:
        url, req = resp.url, resp.request
        ct = resp.headers.get("content-type", "")
        if "/gateway/" not in url: return
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

def core_text(page, n=25):
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
    page.fill("#criteria", ESN); page.press("#criteria", "Enter")
    page.wait_for_timeout(11000)

    def click(txt, wait=8000):
        try:
            page.locator(f'span.text-span:has-text("{txt}")').first.click(timeout=20000)
            page.wait_for_timeout(wait); return True
        except Exception as ex:
            print(f"    не кликнулось «{txt}»: {str(ex)[:80]}"); return False

    print("\n>>> ВКЛАДКА «Информация об изделии»")
    if click("Информация об изделии"):
        labels = page.evaluate("""() => [...document.querySelectorAll('span.text-span')]
            .filter(e => e.offsetParent).map(e => e.innerText.trim())""")
        print("    подпункты:", [l for l in labels if not l.startswith("Каталог")][:20])
        page.screenshot(path=str(SESS / f"extra_{ESN}_productinfo.png"), full_page=True)
        # открыть первый подпункт
        subs = [l for l in labels if l not in
                ("Каталог запасных частей, системы", "Каталог запасных частей, варианты исполнения",
                 "Информация об изделии", "Комплекты прокладок", "Kits and Sets")]
        if subs:
            print(f"    открываю: {subs[0]}")
            if click(subs[0], 9000):
                print(core_text(page))
                page.screenshot(path=str(SESS / f"extra_{ESN}_productinfo_open.png"), full_page=True)

    print("\n>>> КАРТОЧКА ДЕТАЛИ (View Part Details)")
    click("Каталог запасных частей, системы", 6000)
    click("ВОЗДУХОЗАБОРНИК", 6000)
    click("Устройство для запуска холодного двигателя", 10000)
    try:
        vp = page.locator('a:has-text("View Part Details"), button:has-text("View Part Details")').first
        if vp.count():
            vp.click(timeout=15000); page.wait_for_timeout(10000)
            print("    URL:", page.url)
            print(core_text(page, 30))
            page.screenshot(path=str(SESS / f"extra_{ESN}_partdetails.png"), full_page=True)
        else:
            print("    ссылка не найдена")
    except Exception as ex:
        print("    ошибка:", str(ex)[:120])

    b.close()
traffic.close()
print("\nГотово ->", SESS)
