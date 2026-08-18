#!/usr/bin/env python3
# Разведка входа в QuickServe Online (QSOL) + перехват трафика документов.
# Реальный Chrome, постоянный профиль (сессия переживёт перезапуск).
import sys, io, os, json, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(BASE, "storage_state.json")
TRAFFIC = open(os.path.join(BASE, "traffic.jsonl"), "w", encoding="utf-8")

USER = os.environ.get("QS_USER","")
PASSWORD = os.environ.get("QS_PWD","")
START = "https://quickserve.cummins.com/info/index.html"

seen = set()
def log_resp(resp):
    try:
        u = resp.url
        if not any(k in u for k in ("/qs3/", "/gateway/", "/api/", "/pubsys", "/service", "login", "auth")):
            return
        rec = {"method": resp.request.method, "url": u, "status": resp.status,
               "ct": resp.headers.get("content-type", "")}
        try: rec["post"] = resp.request.post_data
        except Exception: rec["post"] = None
        TRAFFIC.write(json.dumps(rec, ensure_ascii=False) + "\n"); TRAFFIC.flush()
        key = resp.request.method + " " + u.split("?")[0]
        if key not in seen:
            seen.add(key); print("  [API]", key)
    except Exception:
        pass

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False,
        args=["--disable-blink-features=AutomationControlled"])
    ctx = browser.new_context(viewport={"width": 1600, "height": 1000},
        storage_state=STATE if os.path.exists(STATE) else None)
    pg = ctx.new_page()
    pg.on("response", log_resp)

    print("Открываю QuickServe...")
    pg.goto(START, wait_until="domcontentloaded", timeout=60000)
    pg.wait_for_timeout(2500)

    # показать поля формы логина, чтобы понять структуру
    print("\n=== INPUT-поля на странице ===")
    for i in pg.eval_on_selector_all("input", """els=>els.map(e=>({type:e.type,name:e.name,id:e.id,ph:e.placeholder,vis:e.offsetParent!==null}))"""):
        if i["vis"] or i["type"] in ("text","password","email"):
            print("  ", i)
    print("=== BUTTONS/submit ===")
    for b in pg.eval_on_selector_all("button, input[type=submit], a.button", """els=>els.slice(0,15).map(e=>({t:(e.innerText||e.value||'').trim().slice(0,30),id:e.id}))"""):
        if b["t"]: print("  ", b)

    print("\n" + "="*64)
    print("  ВОЙДИТЕ вручную:", USER, "/", PASSWORD)
    print("  (если есть код на почту/MFA — введите). Логин/пароль можно")
    print("  скопировать отсюда. После входа ОТКРОЙТЕ раздел документации")
    print("  одного двигателя (введите ESN, зайдите в Service Bulletins /")
    print("  Service Topics / манулы) — чтобы я увидел API.")
    print("  Окно НЕ закрывайте ~6 минут; я слушаю трафик.")
    print("="*64)

    for _ in range(72):  # 6 мин
        pg.wait_for_timeout(5000)
    try:
        (open(os.path.join(BASE, "after_login.html"), "w", encoding="utf-8")).write(pg.content())
        pg.screenshot(path=os.path.join(BASE, "after_login.png"), full_page=True)
        ctx.storage_state(path=STATE)
        print("Сессия сохранена:", STATE)
    except Exception as e:
        print("save err:", e)
    ctx.close(); browser.close()
TRAFFIC.close()
print("\nГотово. traffic.jsonl записан.")
