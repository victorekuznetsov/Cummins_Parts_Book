#!/usr/bin/env python3
# Разведка №4: открыть ESN, пройти по вкладкам «Системы» / «Варианты исполнения»,
# открыть узел и записать ВСЕ запросы (включая картинки), чтобы найти URL чертежей.
import sys, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

from pathlib import Path
from playwright.sync_api import sync_playwright

ESN  = sys.argv[1] if len(sys.argv) > 1 else "37292556"
BASE = Path(__file__).parent
SESS = BASE / "session"; SESS.mkdir(parents=True, exist_ok=True)
traffic = open(SESS / f"traffic_esn_{ESN}.jsonl", "w", encoding="utf-8")
seen = set()

def on_resp(resp):
    try:
        url, req = resp.url, resp.request
        ct = resp.headers.get("content-type", "")
        interesting = ("/gateway/" in url or "image" in ct or "pdf" in ct
                       or re.search(r"\.(png|jpe?g|gif|svg|pdf)(\?|$)", url, re.I))
        if not interesting or "cookielaw" in url or "onetrust" in url:
            return
        rec = {"method": req.method, "url": url, "status": resp.status, "ct": ct,
               "req_post": None, "resp_body": None}
        try: rec["req_post"] = req.post_data
        except Exception: pass
        if "json" in ct or ("text" in ct and "html" not in ct):
            try: rec["resp_body"] = resp.text()[:60000]
            except Exception: pass
        traffic.write(json.dumps(rec, ensure_ascii=False) + "\n"); traffic.flush()
        key = f'{req.method} {url.split("?")[0]}'
        if key not in seen:
            seen.add(key); print(f"  [{resp.status} {ct.split(';')[0]}] {key}")
    except Exception as e:
        print("  [err]", e)

def snap(page, tag):
    try: page.screenshot(path=str(SESS / f"{tag}.png"), full_page=True)
    except Exception: pass
    txt = page.evaluate("() => document.body.innerText")
    # выкидываем общую шапку/подвал, печатаем содержательную часть
    core = txt.split("Список Выбранных Деталей")[-1].split("Главная страница\nО нас")[0]
    (SESS / f"{tag}.txt").write_text(txt, encoding="utf-8")
    print(f"\n===== {tag} | {page.url}\n{core[:2000]}\n")

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(viewport={"width": 1700, "height": 1300},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
    page = ctx.new_page(); page.on("response", on_resp)

    page.goto("https://parts.cummins.com/home", wait_until="networkidle", timeout=90000)
    page.wait_for_timeout(2000)
    page.fill("#criteria", ESN); page.press("#criteria", "Enter")
    page.wait_for_timeout(10000)
    snap(page, f"esn_{ESN}_main")

    def click_tab(name):
        for sel in (f'a:has-text("{name}")', f'button:has-text("{name}")',
                    f'li:has-text("{name}")', f'*:text-is("{name}")'):
            try:
                el = page.locator(sel).first
                if el.count() and el.is_visible():
                    el.click(timeout=8000); return True
            except Exception:
                continue
        return False

    for tab, tag in (("Каталог запасных частей, системы", "systems"),
                     ("Каталог запасных частей, варианты исполнения", "options")):
        print(f"\n>>> Вкладка: {tab}")
        if click_tab(tab):
            page.wait_for_timeout(8000)
            snap(page, f"esn_{ESN}_{tag}")
            # раскрыть первый элемент дерева/списка
            for sel in ("table tbody tr", "li.tree-node", "div.panel-heading",
                        "a.list-group-item", "div[class*=accordion] div[class*=header]"):
                loc = page.locator(sel)
                if loc.count():
                    print(f"    найдено {loc.count()} эл. по '{sel}' — кликаю первый")
                    try:
                        loc.first.click(timeout=8000); page.wait_for_timeout(8000)
                        snap(page, f"esn_{ESN}_{tag}_open")
                    except Exception as e:
                        print("    клик не удался:", e)
                    break
        else:
            print("    вкладка не найдена")

    # какие кнопки/иконки есть на странице (ищем экспорт в PDF)
    btns = page.evaluate("""() => [...document.querySelectorAll('button,a,i,span[class*=icon]')]
        .map(e => ((e.innerText||'')+' |'+(e.className||'')+'| '+(e.title||'')).trim())
        .filter(t => /pdf|print|export|download|печат|выгруз|скач/i.test(t))""")
    print("\n--- КНОПКИ ЭКСПОРТА/ПЕЧАТИ ---")
    for t in sorted(set(btns))[:30]: print("   ", t[:150])

    b.close()
traffic.close()
print("\nГотово ->", SESS)
