#!/usr/bin/env python3
# Ищем, каким запросом подгружается чертёж по кнопке «View Graphics»
# у узлов, для которых componentDetails отдаёт graphics: [].
import sys, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from playwright.sync_api import sync_playwright

ESN  = "37292556"
SESS = Path(__file__).resolve().parent.parent.parent / "session"; SESS.mkdir(exist_ok=True)
traffic, seen = [], set()

def on_resp(r):
    u = r.url
    if "/gateway/" not in u:
        return
    ct = r.headers.get("content-type", "")
    rec = {"url": u, "status": r.status, "ct": ct, "body": None}
    if "json" in ct:
        try: rec["body"] = r.text()[:20000]
        except Exception: pass
    traffic.append(rec)
    k = u.split("?")[0]
    if k not in seen:
        seen.add(k); print(f"  [{r.status} {ct.split(';')[0]}] {k}")

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
    page.locator('span.text-span:has-text("Каталог запасных частей, системы")').first.click(timeout=20000)
    page.wait_for_timeout(6000)
    page.locator('span.text-span:has-text("ТОПЛИВО")').first.click(timeout=20000)
    page.wait_for_timeout(5000)
    page.locator('span.text-span:has-text("Топливный фильтр")').first.click(timeout=20000)
    page.wait_for_timeout(9000)

    # закрыть модальное окно «All assemblies are expanded»
    for sel in ('button:has-text("OK")', '.modal button', 'button.close'):
        try:
            el = page.locator(sel).first
            if el.count() and el.is_visible():
                el.click(timeout=4000); page.wait_for_timeout(1200); break
        except Exception: pass

    print("\n>>> Ищу кнопку View Graphics")
    info = page.evaluate("""() => [...document.querySelectorAll('*')]
        .filter(e => e.offsetParent && /view graphics/i.test(e.textContent || '')
                     && e.children.length < 3)
        .slice(0, 5).map(e => ({tag: e.tagName, cls: e.className,
                                html: e.outerHTML.slice(0, 300)}))""")
    for i in info: print("   ", json.dumps(i, ensure_ascii=False)[:320])

    print("\n>>> Кликаю")
    n_before = len(traffic)
    clicked = False
    for sel in ('*:has-text("View Graphics")', '[title*="Graphics" i]',
                '.graphic-thumb', 'img[src*="rtgraphics"]'):
        try:
            el = page.locator(sel).last
            if el.count() and el.is_visible():
                el.click(timeout=8000); clicked = True
                print(f"    кликнул по '{sel}'"); break
        except Exception:
            continue
    page.wait_for_timeout(9000)
    page.screenshot(path=str(SESS / "ui_view_graphics.png"), full_page=True)

    print("\n>>> Новые запросы после клика")
    for r in traffic[n_before:]:
        print(f"    [{r['status']}] {r['url'][:160]}")
        if r["body"] and len(r["body"]) < 3000:
            print("        ", r["body"][:800])

    imgs = page.evaluate("""() => [...document.querySelectorAll('img')].map(i => i.src)
        .filter(s => /graphic/i.test(s))""")
    print("\n>>> Картинки-чертежи на странице:")
    for s in sorted(set(imgs))[:10]: print("   ", s)
    b.close()
