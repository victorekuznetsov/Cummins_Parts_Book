#!/usr/bin/env python3
# Разведка №5: вытащить разметку левой навигации ESN-страницы и реальные роуты вкладок.
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from playwright.sync_api import sync_playwright

ESN = sys.argv[1] if len(sys.argv) > 1 else "37292556"
SESS = Path(__file__).parent / "session"; SESS.mkdir(exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(viewport={"width": 1700, "height": 1300})
    page = ctx.new_page()
    page.goto("https://parts.cummins.com/home", wait_until="networkidle", timeout=90000)
    page.wait_for_timeout(2000)
    page.fill("#criteria", ESN); page.press("#criteria", "Enter")
    page.wait_for_timeout(10000)
    (SESS / f"esn_{ESN}_main.html").write_text(page.content(), encoding="utf-8")

    info = page.evaluate("""() => {
      const want = ['Каталог запасных частей','Информация об изделии',
                    'Комплекты прокладок','Kits and Sets'];
      const out = [];
      for (const el of document.querySelectorAll('*')) {
        const t = (el.textContent||'').trim();
        if (el.children.length === 0 && want.some(w => t.startsWith(w))) {
          const a = el.closest('a') || el;
          out.push({text: t.slice(0,60), tag: el.tagName, cls: el.className,
                    href: a.getAttribute && a.getAttribute('href'),
                    parentHTML: (el.parentElement ? el.parentElement.outerHTML : '').slice(0,400),
                    visible: !!(el.offsetParent)});
        }
      }
      return out;
    }""")
    print("--- ЭЛЕМЕНТЫ ВКЛАДОК ---")
    for i in info: print(json.dumps(i, ensure_ascii=False)[:600], "\n")
    b.close()
