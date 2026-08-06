#!/usr/bin/env python3
# Проба: можно ли качать картинки обычным requests с куками браузера
# (тогда скачивание распараллелится и пойдёт в разы быстрее).
import sys, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import requests
from playwright.sync_api import sync_playwright

API = "https://parts.cummins.com/gateway/api/IACDataServices"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(user_agent=UA)
    page = ctx.new_page()
    page.goto("https://parts.cummins.com/home", wait_until="networkidle", timeout=120000)
    page.wait_for_timeout(2500)
    cookies = {c["name"]: c["value"] for c in ctx.cookies()}
    xsrf = cookies.get("XSRF-TOKEN", "")
    b.close()

s = requests.Session()
s.headers.update({"User-Agent": UA, "Referer": "https://parts.cummins.com/esn-entry/main",
                  "Accept": "image/avif,image/webp,image/png,*/*"})
for k, v in cookies.items():
    s.cookies.set(k, v, domain="parts.cummins.com")

print("--- КАРТИНКИ через requests ---")
for u in (f"{API}/graphics/parts/309/3092129/3092129_iso.png",
          f"{API}/graphics/parts/309/3092129/3092129_front.png",
          f"{API}/graphics/rtgraphics/english/parts/095/ah/095_ah0500500_06.png"):
    t = time.time()
    try:
        r = s.get(u, timeout=45)
        print(f"   {r.status_code} {len(r.content):>8}b {time.time()-t:.1f}c  {u.rsplit('/',1)[-1]}")
    except Exception as e:
        print("   ошибка:", str(e)[:100])

print("--- JSON-API через requests (нужен x-xsrf-token) ---")
r = s.get(f"{API}/protected/partDetails?partNo=3092129&smn=",
          headers={"Accept": "application/json", "x-xsrf-token": xsrf}, timeout=45)
print(f"   partDetails: {r.status_code}, {len(r.content)} b")
if r.status_code == 200:
    print("   поля:", list(r.json().keys())[:8])
