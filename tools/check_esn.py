#!/usr/bin/env python3
# =====================================================================
# Проверка списка серийных номеров двигателей (ESN): модель, CPL,
# конфигурация, дата сборки, число узлов и деталей.
#
#   python tools/check_esn.py esn_list.txt [--json отчёт.json]
#
# Каталог имеет смысл качать по одному ESN на каждый CPL — остальные
# двигатели того же CPL повторяют его состав. Скрипт показывает
# группировку по CPL и какие номера можно пропустить.
# =====================================================================
import sys, io, json, argparse, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from playwright.sync_api import sync_playwright

API = "https://parts.cummins.com/gateway/api/IACDataServices"
UA  = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
       "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")


def new_session():
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        ctx = b.new_context(user_agent=UA)
        page = ctx.new_page()
        for _ in range(3):
            try:
                page.goto("https://parts.cummins.com/home",
                          wait_until="networkidle", timeout=120000)
                break
            except Exception:
                pass
        page.wait_for_timeout(2500)
        cookies = {c["name"]: c["value"] for c in ctx.cookies()}
        b.close()
    s = requests.Session()
    s.headers.update({"User-Agent": UA,
                      "Referer": "https://parts.cummins.com/esn-entry/main"})
    for k, v in cookies.items():
        s.cookies.set(k, v, domain="parts.cummins.com")
    xsrf = cookies.get("XSRF-TOKEN", "")
    if not xsrf:
        sys.exit("не удалось завести сессию (нет XSRF-TOKEN)")
    return s, xsrf


def read_list(path):
    """Список ESN из файла: игнорируем разметку таблиц, [[ссылки]] и мусор."""
    import re
    txt = Path(path).read_text(encoding="utf-8")
    nos, seen = [], set()
    for m in re.finditer(r"\d{6,10}", txt):
        n = m.group(0)
        if n not in seen:
            seen.add(n); nos.append(n)
    return nos


def main():
    ap = argparse.ArgumentParser(description="Проверка ESN и группировка по CPL")
    ap.add_argument("list", help="файл со списком ESN")
    ap.add_argument("--json", default="esn_report.json")
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()

    esns = read_list(a.list)
    print(f">>> Номеров в списке: {len(esns)}")
    short = [e for e in esns if len(e) != 8]
    if short:
        print(f"    ! непохожи на ESN (не 8 цифр), проверю отдельно: {short}")

    s, xsrf = new_session()

    def one(esn):
        for attempt in range(3):
            try:
                r = s.get(f"{API}/v2/esnInfo/{esn}?esnType=mbom", timeout=60,
                          headers={"Accept": "application/json", "x-xsrf-token": xsrf})
                if r.status_code == 200:
                    d = r.json()
                    opts = d.get("optionList") or []
                    parts = {p["partNo"] for o in opts for p in (o.get("parts") or [])
                             if p.get("partNo")}
                    return {"esn": esn, "ok": True,
                            "model": d.get("serviceModel"), "cpl": d.get("cpl"),
                            "config": d.get("marketingConfig"),
                            "build": str(d.get("buildDate") or "")[:10],
                            "group": d.get("engineGroup"),
                            "plant": d.get("enginePlantCode"),
                            "options": len(opts), "parts": len(parts)}
                if r.status_code in (400, 404):
                    return {"esn": esn, "ok": False, "err": f"не найден ({r.status_code})"}
            except Exception as e:
                if attempt == 2:
                    return {"esn": esn, "ok": False, "err": str(e)[:60]}
            time.sleep(1.5 * (attempt + 1))
        return {"esn": esn, "ok": False, "err": "нет ответа"}

    res = []
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(one, e): e for e in esns}
        for i, f in enumerate(as_completed(futs), 1):
            res.append(f.result())
            if i % 10 == 0 or i == len(esns):
                print(f"    проверено {i}/{len(esns)}")

    res.sort(key=lambda x: x["esn"])
    good = [r for r in res if r.get("ok")]
    bad  = [r for r in res if not r.get("ok")]

    print("\n" + "=" * 76)
    print(f"  {'ESN':<10} {'МОДЕЛЬ':<16} {'CPL':<6} {'КОНФИГУРАЦИЯ':<14} "
          f"{'СБОРКА':<11} {'УЗЛОВ':>6} {'ДЕТАЛЕЙ':>8}")
    print("=" * 76)
    for r in good:
        print(f"  {r['esn']:<10} {str(r['model'] or ''):<16} {str(r['cpl'] or ''):<6} "
              f"{str(r['config'] or ''):<14} {r['build']:<11} "
              f"{r['options']:>6} {r['parts']:>8}")
    if bad:
        print("\n  НЕ ОТКРЫЛИСЬ:")
        for r in bad:
            print(f"    {r['esn']}: {r['err']}")

    # группировка по CPL
    groups = {}
    for r in good:
        groups.setdefault((r["cpl"], r["model"]), []).append(r)
    print("\n" + "=" * 76)
    print(f"  РАЗНЫХ CPL: {len(groups)}")
    print("=" * 76)
    to_crawl = []
    for (cpl, model), rows in sorted(groups.items(), key=lambda x: str(x[0][0])):
        rep = sorted(rows, key=lambda r: r["esn"])[0]
        configs = sorted({r["config"] for r in rows if r["config"]})
        to_crawl.append(rep["esn"])
        print(f"\n  CPL {cpl} · {model} · двигателей: {len(rows)}")
        print(f"    конфигурации: {', '.join(configs)}")
        print(f"    качаем каталог по: {rep['esn']}")
        others = [r["esn"] for r in sorted(rows, key=lambda r: r["esn"])[1:]]
        if others:
            print(f"    остальные того же CPL ({len(others)}): {', '.join(others)}")

    print("\n" + "=" * 76)
    print(f"  ИТОГО КАЧАТЬ КАТАЛОГОВ: {len(to_crawl)} вместо {len(good)}")
    print(f"  Команда: " + "; ".join(f"python crawler.py {e}" for e in to_crawl[:3]) +
          (" ..." if len(to_crawl) > 3 else ""))
    print("=" * 76)

    Path(a.json).write_text(json.dumps(
        {"checked": res, "groups": [{"cpl": k[0], "model": k[1],
                                     "esns": [r["esn"] for r in v],
                                     "representative": sorted(r["esn"] for r in v)[0]}
                                    for k, v in groups.items()],
         "to_crawl": to_crawl}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nОтчёт: {a.json}")


if __name__ == "__main__":
    main()
