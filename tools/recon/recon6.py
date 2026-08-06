#!/usr/bin/env python3
# Разведка №6: раскрыть дерево «Каталог запасных частей, системы», дойти до листа
# (узел -> список позиций + чертёж) и записать все запросы, включая картинки/PDF.
import sys, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from playwright.sync_api import sync_playwright

ESN  = sys.argv[1] if len(sys.argv) > 1 else "37292556"
TREE = sys.argv[2] if len(sys.argv) > 2 else "Каталог запасных частей, системы"
SESS = Path(__file__).parent / "session"; SESS.mkdir(exist_ok=True)
traffic = open(SESS / f"traffic_tree_{ESN}.jsonl", "w", encoding="utf-8")
seen = set()

def on_resp(resp):
    try:
        url, req = resp.url, resp.request
        ct = resp.headers.get("content-type", "")
        if "/assets/" in url or "cookielaw" in url or "onetrust" in url: return
        if not ("/gateway/" in url or "image" in ct or "pdf" in ct): return
        rec = {"method": req.method, "url": url, "status": resp.status, "ct": ct,
               "req_post": None, "resp_body": None}
        try: rec["req_post"] = req.post_data
        except Exception: pass
        if "json" in ct:
            try: rec["resp_body"] = resp.text()[:60000]
            except Exception: pass
        traffic.write(json.dumps(rec, ensure_ascii=False) + "\n"); traffic.flush()
        key = f'{req.method} {url.split("?")[0]}'
        if key not in seen:
            seen.add(key); print(f"  [{resp.status} {ct.split(';')[0]}] {key}")
    except Exception as e:
        print("  [err]", e)

def visible_tree_labels(page):
    return page.evaluate("""() => [...document.querySelectorAll('span.text-span')]
        .filter(e => e.offsetParent).map(e => e.innerText.trim()).filter(Boolean)""")

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(viewport={"width": 1700, "height": 1300})
    page = ctx.new_page(); page.on("response", on_resp)
    page.goto("https://parts.cummins.com/home", wait_until="networkidle", timeout=90000)
    page.wait_for_timeout(2000)
    # баннер cookie перехватывает клики — принимаем
    for sel in ("#onetrust-accept-btn-handler", "button:has-text('Согласиться')"):
        try:
            el = page.locator(sel).first
            if el.count() and el.is_visible():
                el.click(timeout=5000); print("  cookie-баннер принят"); break
        except Exception:
            pass
    page.wait_for_timeout(1500)
    page.fill("#criteria", ESN); page.press("#criteria", "Enter")
    page.wait_for_timeout(10000)

    print(f">>> Кликаю: {TREE}")
    page.locator(f'span.text-span:has-text("{TREE}")').first.click(timeout=15000)
    page.wait_for_timeout(9000)
    labels = visible_tree_labels(page)
    print(f"\n--- УЗЛЫ ДЕРЕВА ({len(labels)}) ---")
    for l in labels[:60]: print("   ", l)
    (SESS / f"tree_{ESN}_level1.json").write_text(
        json.dumps(labels, ensure_ascii=False, indent=1), encoding="utf-8")
    page.screenshot(path=str(SESS / f"tree_{ESN}_level1.png"), full_page=True)

    # раскрываем первый содержательный дочерний узел
    child = [l for l in labels if l != TREE and not l.startswith("Каталог")
             and l not in ("Информация об изделии", "Комплекты прокладок", "Kits and Sets")]
    if child:
        target = child[0]
        print(f"\n>>> Раскрываю узел: {target}")
        page.locator(f'span.text-span:has-text("{target}")').first.click(timeout=15000)
        page.wait_for_timeout(9000)
        labels2 = visible_tree_labels(page)
        new = [l for l in labels2 if l not in labels]
        print(f"--- НОВЫЕ ПОДУЗЛЫ ({len(new)}) ---")
        for l in new[:60]: print("   ", l)
        page.screenshot(path=str(SESS / f"tree_{ESN}_level2.png"), full_page=True)
        if new:
            leaf = new[0]
            print(f"\n>>> Открываю лист: {leaf}")
            page.locator(f'span.text-span:has-text("{leaf}")').first.click(timeout=15000)
            page.wait_for_timeout(12000)
            page.screenshot(path=str(SESS / f"tree_{ESN}_leaf.png"), full_page=True)
            txt = page.evaluate("() => document.body.innerText")
            (SESS / f"tree_{ESN}_leaf.txt").write_text(txt, encoding="utf-8")
            core = txt.split("Список Выбранных Деталей")[-1].split("Главная страница\nО нас")[0]
            print("\n--- СОДЕРЖИМОЕ ЛИСТА ---\n", core[:2500])
            imgs = page.evaluate("""() => [...document.querySelectorAll('img')]
                .map(i => i.src).filter(s => !/\\/assets\\//.test(s))""")
            print("\n--- КАРТИНКИ НА СТРАНИЦЕ ---")
            for s in sorted(set(imgs))[:20]: print("   ", s)
    b.close()
traffic.close()
print("\nГотово ->", SESS)
