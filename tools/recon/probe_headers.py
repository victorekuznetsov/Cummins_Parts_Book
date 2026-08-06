#!/usr/bin/env python3
# Проба: какие заголовки Angular-приложение шлёт в componentDetails (почему наш
# сторонний fetch получает 403).
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from playwright.sync_api import sync_playwright

ESN = "37292556"
captured = []

def on_req(req):
    if "componentDetails" in req.url or "esnInfo" in req.url:
        captured.append({"url": req.url, "headers": dict(req.headers)})

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(viewport={"width": 1700, "height": 1200})
    page = ctx.new_page(); page.on("request", on_req)
    page.goto("https://parts.cummins.com/home", wait_until="networkidle", timeout=90000)
    page.wait_for_timeout(2000)
    for sel in ("#onetrust-accept-btn-handler",):
        try:
            el = page.locator(sel).first
            if el.count() and el.is_visible(): el.click(timeout=5000)
        except Exception: pass
    page.wait_for_timeout(1200)
    page.fill("#criteria", ESN); page.press("#criteria", "Enter")
    page.wait_for_timeout(9000)
    page.locator('span.text-span:has-text("Каталог запасных частей, системы")').first.click(timeout=15000)
    page.wait_for_timeout(7000)
    page.locator('span.text-span:has-text("ВОЗДУХОЗАБОРНИК")').first.click(timeout=15000)
    page.wait_for_timeout(7000)
    page.locator('span.text-span:has-text("Устройство для запуска холодного двигателя")').first.click(timeout=15000)
    page.wait_for_timeout(9000)

    print("--- ЗАХВАЧЕННЫЕ ЗАПРОСЫ ---")
    for c in captured:
        print("\nURL:", c["url"][:150])
        for k, v in sorted(c["headers"].items()):
            print(f"   {k}: {v[:120]}")

    # теперь тот же вызов из контекста страницы ESN — пройдёт ли?
    if captured:
        u = [c["url"] for c in captured if "componentDetails" in c["url"]]
        if u:
            r = page.evaluate("""async (u) => {
                const r = await fetch(u, {credentials:'include'});
                return {status: r.status, len: (await r.text()).length};
            }""", u[0])
            print("\nПовтор из контекста ESN-страницы:", r)
    # и cookies
    print("\n--- COOKIES ---")
    for c in ctx.cookies():
        print(f"   {c['name']} = {str(c['value'])[:60]}")
    b.close()
