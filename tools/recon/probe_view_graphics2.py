#!/usr/bin/env python3
# Точный поиск кнопки «View Graphics» на странице узла и перехват её запроса.
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from playwright.sync_api import sync_playwright

ESN  = "37292556"
SESS = Path(__file__).resolve().parent.parent.parent / "session"; SESS.mkdir(exist_ok=True)
traffic = []

def on_resp(r):
    if "/gateway/" in r.url:
        ct = r.headers.get("content-type", "")
        body = None
        if "json" in ct:
            try: body = r.text()[:8000]
            except Exception: pass
        traffic.append({"url": r.url, "status": r.status, "ct": ct, "body": body})

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
    for sel in ('button:has-text("OK")', '.ui-dialog button'):
        try:
            el = page.locator(sel).first
            if el.count() and el.is_visible():
                el.click(timeout=4000); page.wait_for_timeout(1000); break
        except Exception: pass

    # элементы, чей СОБСТВЕННЫЙ текст — «View Graphics»
    print(">>> Элементы с собственным текстом «View Graphics»")
    found = page.evaluate("""() => {
        const out = [];
        const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        let n;
        while (n = walk.nextNode()) {
            if (/view graphics/i.test(n.nodeValue || '')) {
                const e = n.parentElement;
                const r = e.getBoundingClientRect();
                out.push({tag: e.tagName, cls: e.className, id: e.id,
                          html: e.outerHTML.slice(0, 260),
                          box: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
                          parentHtml: (e.parentElement ? e.parentElement.outerHTML.slice(0, 400) : '')});
            }
        }
        return out; }""")
    for f in found:
        print("   ", json.dumps(f, ensure_ascii=False)[:700], "\n")

    # все картинки в шапке узла
    print(">>> Все картинки на странице (не фото деталей)")
    imgs = page.evaluate("""() => [...document.querySelectorAll('img')]
        .map(i => ({src: i.src, w: i.naturalWidth, h: i.naturalHeight}))
        .filter(o => !/graphics\\/parts\\//.test(o.src) && !/\\/assets\\//.test(o.src))""")
    for i in imgs[:15]: print("   ", i)

    n0 = len(traffic)
    if found:
        box = found[0]["box"]
        print(f"\n>>> Кликаю по координатам {box[0] + box[2] // 2}, {box[1] + box[3] // 2}")
        page.mouse.click(box[0] + box[2] // 2, box[1] + box[3] // 2)
        page.wait_for_timeout(9000)
        page.screenshot(path=str(SESS / "ui_after_view_graphics.png"), full_page=True)
        print(">>> Запросы после клика:")
        for r in traffic[n0:]:
            print(f"    [{r['status']}] {r['url'][:170]}")
        big = page.evaluate("""() => [...document.querySelectorAll('img')]
            .filter(i => i.naturalWidth > 400).map(i => i.src)""")
        print(">>> Крупные изображения после клика:")
        for s in sorted(set(big))[:8]: print("   ", s)
    b.close()
