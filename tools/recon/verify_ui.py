#!/usr/bin/env python3
# Сверка с сайтом: открыть узел БЕЗ чертежа (Топливный фильтр) и узел С чертежом,
# посмотреть, что реально показывает UI, и найти кнопки экспорта/печати/PDF.
import sys, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from playwright.sync_api import sync_playwright

ESN = "37292556"
SESS = Path(__file__).parent / "session"; SESS.mkdir(exist_ok=True)
downloads = []

def on_resp(r):
    ct = r.headers.get("content-type", "")
    if "pdf" in ct or re.search(r"\.pdf(\?|$)", r.url, re.I) or "export" in r.url.lower():
        downloads.append((r.status, ct, r.url))
        print(f"  [PDF/EXPORT {r.status}] {r.url[:140]}")

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(viewport={"width": 1700, "height": 1400})
    page = ctx.new_page(); page.on("response", on_resp)
    page.goto("https://parts.cummins.com/home", wait_until="networkidle", timeout=120000)
    page.wait_for_timeout(2500)
    try:
        el = page.locator("#onetrust-accept-btn-handler").first
        if el.count() and el.is_visible(): el.click(timeout=6000)
    except Exception: pass
    page.wait_for_timeout(1200)
    page.fill("#criteria", ESN); page.press("#criteria", "Enter")
    page.wait_for_timeout(11000)
    page.locator('span.text-span:has-text("Каталог запасных частей, системы")').first.click(timeout=20000)
    page.wait_for_timeout(7000)

    def open_leaf(system, leaf, tag):
        print(f"\n>>> {system} -> {leaf}")
        page.locator(f'span.text-span:has-text("{system}")').first.click(timeout=20000)
        page.wait_for_timeout(6000)
        page.locator(f'span.text-span:has-text("{leaf}")').first.click(timeout=20000)
        page.wait_for_timeout(10000)
        page.screenshot(path=str(SESS / f"verify_{tag}.png"), full_page=True)
        imgs = page.evaluate("""() => [...document.querySelectorAll('img')].map(i=>i.src)
            .filter(s => /rtgraphics|graphics\\/parts/.test(s))""")
        txt = page.evaluate("() => document.body.innerText")
        core = txt.split("Список Выбранных Деталей")[-1].split("Главная страница\nО нас")[0]
        has_draw = any("rtgraphics" in s for s in imgs)
        print(f"    чертёж на странице: {'ДА' if has_draw else 'НЕТ'}")
        print(f"    фото деталей: {sum('graphics/parts' in s for s in imgs)}")
        print("    ---\n" + "\n".join("    " + l for l in core.splitlines()[:28]))
        # кнопки экспорта
        btns = page.evaluate("""() => [...document.querySelectorAll('button,a,i,span,div')]
            .filter(e => e.offsetParent)
            .map(e => ((e.innerText||'').trim()+' ~'+(e.className||'')+'~'+(e.title||'')))
            .filter(t => /pdf|print|export|download|печат|выгруз|скач/i.test(t))""")
        uniq = sorted({t[:110] for t in btns})
        print(f"    кнопки экспорта ({len(uniq)}):")
        for t in uniq[:12]: print("       ", t)
        # свернуть систему обратно
        page.locator(f'span.text-span:has-text("{system}")').first.click(timeout=20000)
        page.wait_for_timeout(3000)

    open_leaf("ТОПЛИВО", "Топливный фильтр", "fuel_filter_nodraw")
    open_leaf("ВОЗДУХОЗАБОРНИК", "Впускной коллектор", "intake_manifold")

    print("\n--- PDF/EXPORT ЗАПРОСЫ ---", downloads or "нет")
    b.close()
