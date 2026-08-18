#!/usr/bin/env python3
# Вход в QuickServe (Cummins IAM / mylogin.cummins.com) + захват сессии и API.
import sys, io, os, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                              errors="replace", write_through=True)  # без буферизации
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(BASE, "storage_state.json")
TRAFFIC = open(os.path.join(BASE, "traffic.jsonl"), "w", encoding="utf-8")
STATUS = os.path.join(BASE, "status.txt")
def status(s):
    open(STATUS, "w", encoding="utf-8").write(s); print(s, flush=True)

USER = os.environ.get("QS_USER","")
PWD  = os.environ.get("QS_PWD","")
PORTAL = "https://quickserve.cummins.com/qs3/portal/index.html"

seen = set()
def log_resp(resp):
    try:
        u = resp.url
        if not any(k in u for k in ("/qs3/", "/gateway/", "/api/", "pubsys",
                                    "servlet", "aura", "DataServices")):
            return
        rec = {"m": resp.request.method, "url": u, "st": resp.status,
               "ct": resp.headers.get("content-type", "")}
        try: rec["post"] = resp.request.post_data
        except Exception: rec["post"] = None
        TRAFFIC.write(json.dumps(rec, ensure_ascii=False) + "\n"); TRAFFIC.flush()
        k = resp.request.method + " " + u.split("?")[0]
        if k not in seen and "/qs3/" in u:
            seen.add(k); print("  [DOC]", k, flush=True)
    except Exception:
        pass

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False,
        args=["--disable-blink-features=AutomationControlled", "--start-maximized"])
    ctx = browser.new_context(no_viewport=True,
        storage_state=STATE if os.path.exists(STATE) else None)
    pg = ctx.new_page()
    pg.on("response", log_resp)

    status("Открываю портал/логин...")
    try:
        pg.goto(PORTAL, wait_until="commit", timeout=45000)
    except Exception as e:
        status("goto warn: " + str(e)[:80])
    # ждём появления поля username (редирект на mylogin) до 60с
    try:
        pg.wait_for_selector('input[name="username"]', timeout=60000)
    except Exception:
        pass
    pg.wait_for_timeout(1500)

    # автозаполнение логина/пароля, если мы на странице mylogin
    if "mylogin.cummins.com" in pg.url:
        try:
            pg.fill('input[name="username"]', USER, timeout=15000)
            pg.fill('input[name="password"]', PWD)
            status("Логин и пароль подставлены. ВВЕДИТЕ Company Id и нажмите Login.")
        except Exception as e:
            status("Не удалось автозаполнить: " + str(e)[:100])
    else:
        status("Уже авторизованы? URL: " + pg.url)

    # ждём успешного входа: возвращаемся на quickserve (не mylogin)
    ok = False
    for _ in range(120):  # 10 мин
        if "mylogin.cummins.com" not in pg.url and "quickserve.cummins.com" in pg.url:
            ok = True; break
        pg.wait_for_timeout(5000)

    if ok:
        pg.wait_for_timeout(3000)
        ctx.storage_state(path=STATE)
        status("ВХОД ВЫПОЛНЕН. Сессия сохранена. Теперь откройте документацию "
               "одного двигателя (ESN 33239899 -> Service Bulletins/Topics/мануалы). "
               "Окно закроется через 5 мин.")
        pg.screenshot(path=os.path.join(BASE, "after_login.png"), full_page=False)
        for _ in range(60):
            pg.wait_for_timeout(5000)
        ctx.storage_state(path=STATE)
        open(os.path.join(BASE, "after_login.html"), "w", encoding="utf-8").write(pg.content())
    else:
        status("Вход не обнаружен за 10 мин.")

    ctx.close(); browser.close()
TRAFFIC.close()
status("Готово.")
