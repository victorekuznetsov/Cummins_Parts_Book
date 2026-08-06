#!/usr/bin/env python3
# Проба: отдаёт ли API русские названия (transDescription) при accept-language: ru
# и существует ли русский вариант пути чертежей (/rtgraphics/russian/...).
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from playwright.sync_api import sync_playwright

ESN  = "37292556"
HASH = ("5D63E08B292152EA1F52EC0033F719C6369EFF67C230603C157014D2DADF1888"
        "0ACCDA25E56FD4BA54444B308A07E8F9F4605F582B3B45CA9652E3218A47A13F")
G    = "/095/ah/095_ah0500500_06"
API  = "https://parts.cummins.com/gateway/api/IACDataServices"

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    for lang in ("en-US", "ru-RU"):
        ctx = b.new_context(locale=lang, extra_http_headers={"accept-language": f"{lang},ru;q=0.9"})
        page = ctx.new_page()
        page.goto("https://parts.cummins.com/home", wait_until="networkidle", timeout=90000)
        page.wait_for_timeout(2500)
        res = page.evaluate("""async ([api, esn, h]) => {
            const r = await fetch(`${api}/v2/componentDetails/option?esnType=mbom&componentHash=${h}&esn=${esn}`,
                                  {credentials:'include'});
            return {status: r.status, body: await r.text()};
        }""", [API, ESN, HASH])
        print(f"\n===== accept-language: {lang} -> HTTP {res['status']}")
        try:
            d = json.loads(res["body"])
            for g in d["groups"]:
                for pt in g["parts"]:
                    x = pt["data"]
                    print(f"   {x['callOut']:>3} {x['partNo']:>9}  desc={x['partDesc']!r}  trans={x['transDescription']!r}")
        except Exception as e:
            print("   разбор не удался:", e, res["body"][:300])

        # проверяем языковые варианты пути чертежа
        for seg in ("english", "russian", "ru"):
            u = f"{API}/graphics/rtgraphics/{seg}/parts{G}.png"
            r = ctx.request.get(u)
            print(f"   графика [{seg}]: HTTP {r.status}  {len(r.body()) if r.status==200 else ''}")
        ctx.close()
    b.close()
