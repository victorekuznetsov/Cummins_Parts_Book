#!/usr/bin/env python3
# Сверка с живым сайтом: показывает ли Cummins чертёж для узлов, по которым
# API не отдал ссылку (Топливный фильтр, ЭБУ и т.п.).
import sys, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from playwright.sync_api import sync_playwright

ESN  = "37292556"
SESS = Path(__file__).resolve().parent.parent.parent / "session"; SESS.mkdir(exist_ok=True)

# система в дереве -> узел, у которого в выгрузке нет чертежа
TARGETS = [("ТОПЛИВО", "Топливный фильтр", "FF5088-08"),
           ("ЭЛЕКТРООБОРУДОВАНИЕ", "Электронный блок управления", "PH5745-16"),
           ("БАЗОВЫЙ ДВИГАТЕЛЬ", "Коромысло", "RL5701-13")]

seen_imgs = []

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(viewport={"width": 1700, "height": 1300})
    page = ctx.new_page()
    page.on("response", lambda r: seen_imgs.append((r.status, r.url))
            if "rtgraphics" in r.url else None)
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
    page.wait_for_timeout(7000)

    for system, leaf, optno in TARGETS:
        print(f"\n>>> {system} -> {leaf} ({optno})")
        try:
            page.locator(f'span.text-span:has-text("{system}")').first.click(timeout=20000)
            page.wait_for_timeout(5000)
        except Exception as e:
            print("    система не открылась:", str(e)[:80]); continue
        labels = page.evaluate("""() => [...document.querySelectorAll('span.text-span')]
            .filter(e => e.offsetParent).map(e => e.innerText.trim())""")
        print("    узлы системы:", [l for l in labels if len(l) < 60][:14])
        try:
            page.locator(f'span.text-span:has-text("{leaf}")').first.click(timeout=15000)
            page.wait_for_timeout(9000)
        except Exception as e:
            print("    узел не открылся:", str(e)[:80])
            page.locator(f'span.text-span:has-text("{system}")').first.click(timeout=20000)
            page.wait_for_timeout(3000)
            continue
        imgs = page.evaluate("""() => [...document.querySelectorAll('img')].map(i => i.src)
            .filter(s => /rtgraphics/.test(s))""")
        txt = page.evaluate("() => document.body.innerText")
        core = txt.split("Список Выбранных Деталей")[-1].split("Главная страница\nО нас")[0]
        head = "\n".join("    " + l for l in core.splitlines()[:12] if l.strip())
        print(head)
        print(f"    ЧЕРТЁЖ НА СТРАНИЦЕ: {'ДА -> ' + imgs[0] if imgs else 'НЕТ'}")
        page.screenshot(path=str(SESS / f"ui_{optno}.png"), full_page=True)
        page.locator(f'span.text-span:has-text("{system}")').first.click(timeout=20000)
        page.wait_for_timeout(3000)

    print("\n--- все запросы чертежей за сессию ---")
    for st, u in seen_imgs:
        print(f"    {st} {u.rsplit('/', 1)[-1]}")
    b.close()
