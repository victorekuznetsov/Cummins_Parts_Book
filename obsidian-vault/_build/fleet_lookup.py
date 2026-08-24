#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Определяет по серийному номеру двигателя его модель, CPL и конфигурацию
через открытый API parts.cummins.com (логин не нужен) и группирует парк по CPL:
на каждый CPL нужен один каталог, остальные машины группы им покрываются.
"""
import json
import os
import sys
import time

import requests
from playwright.sync_api import sync_playwright

API = "https://parts.cummins.com/gateway/api/IACDataServices"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")


def new_session():
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get(
            "CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"))
        ctx = b.new_context(user_agent=UA)
        pg = ctx.new_page()
        for _ in range(3):
            try:
                pg.goto("https://parts.cummins.com/home",
                        wait_until="networkidle", timeout=120000)
                break
            except Exception:                                  # noqa: BLE001
                pass
        pg.wait_for_timeout(2500)
        cookies = {c["name"]: c["value"] for c in ctx.cookies()}
        b.close()
    s = requests.Session()
    s.headers.update({"User-Agent": UA,
                      "Referer": "https://parts.cummins.com/esn-entry/main"})
    for k, v in cookies.items():
        s.cookies.set(k, v, domain="parts.cummins.com")
    xsrf = cookies.get("XSRF-TOKEN", "")
    if not xsrf:
        sys.exit("не удалось завести сессию с parts.cummins.com (нет XSRF-TOKEN)")
    return s, xsrf


def lookup(s, xsrf, esn):
    r = s.get(f"{API}/engine/{esn}", timeout=45,
              headers={"Accept": "application/json", "x-xsrf-token": xsrf})
    if r.status_code == 404:
        return {"ok": False, "err": "нет в каталоге Cummins (404)"}
    r.raise_for_status()
    d = r.json()
    if not isinstance(d, dict) or not d:
        return {"ok": False, "err": "пустой ответ"}
    return {"ok": True, "raw": d}


def main():
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "fleet/polyus_report.json"
    esns = []
    with open(src, encoding="utf-8") as f:
        head = f.readline().rstrip("\n").split("\t")
        for line in f:
            if line.strip():
                esns.append(dict(zip(head, line.rstrip("\n").split("\t"))))

    s, xsrf = new_session()
    res = []
    t0 = time.time()
    for i, rec in enumerate(esns, 1):
        esn = rec["esn"]
        try:
            r = lookup(s, xsrf, esn)
        except Exception as exc:                               # noqa: BLE001
            r = {"ok": False, "err": str(exc)[:80]}
        r.update({k: v for k, v in rec.items()})
        res.append(r)
        if i % 20 == 0:
            print(f"  {i}/{len(esns)} · {time.time()-t0:.0f} c", flush=True)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    ok = sum(1 for r in res if r.get("ok"))
    print(f"готово: {ok} из {len(res)} найдено, отчёт {out}")


if __name__ == "__main__":
    main()
