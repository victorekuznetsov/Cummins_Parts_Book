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
    """Список ESN. Понимает два формата:
       - TSV с заголовком machine/vin/esn — тогда берём колонку esn и модель машины
         (серийные номера бывают буквенно-цифровыми: 1024E008268, 4P25J004736);
       - произвольный текст — вытаскиваем номера из 6-10 цифр, игнорируя разметку.
       Возвращает список (esn, машина, vin)."""
    import re
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    if lines and "	" in lines[0] and "esn" in lines[0].lower():
        head = [h.strip().lower() for h in lines[0].split("	")]
        i_esn = head.index("esn")
        i_m = head.index("machine") if "machine" in head else None
        i_v = head.index("vin") if "vin" in head else None
        out, seen = [], set()
        for ln in lines[1:]:
            if not ln.strip():
                continue
            c = ln.split("	")
            if len(c) <= i_esn:
                continue
            esn = c[i_esn].strip()
            if not esn or esn in seen:
                continue
            seen.add(esn)
            out.append((esn,
                        c[i_m].strip() if i_m is not None and i_m < len(c) else "",
                        c[i_v].strip() if i_v is not None and i_v < len(c) else ""))
        return out
    nos, seen = [], set()
    for m in re.finditer(r"\d{6,10}", "\n".join(lines)):
        n = m.group(0)
        if n not in seen:
            seen.add(n); nos.append((n, "", ""))
    return nos


def main():
    ap = argparse.ArgumentParser(description="Проверка ESN и группировка по CPL")
    ap.add_argument("list", help="файл со списком ESN")
    ap.add_argument("--json", default="esn_report.json")
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()

    rows = read_list(a.list)
    esns = [r[0] for r in rows]
    info = {r[0]: {"machine": r[1], "vin": r[2]} for r in rows}
    print(f">>> Номеров в списке: {len(esns)}")

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
                            "machine": info.get(esn, {}).get("machine", ""),
                            "vin": info.get(esn, {}).get("vin", ""),
                            "model": d.get("serviceModel"), "cpl": d.get("cpl"),
                            "config": d.get("marketingConfig"),
                            "build": str(d.get("buildDate") or "")[:10],
                            "group": d.get("engineGroup"),
                            "plant": d.get("enginePlantCode"),
                            "options": len(opts), "parts": len(parts)}
                if r.status_code in (400, 404):
                    return {"esn": esn, "ok": False,
                            "machine": info.get(esn, {}).get("machine", ""),
                            "err": f"нет в EPC ({r.status_code})"}
            except Exception as e:
                if attempt == 2:
                    return {"esn": esn, "ok": False,
                            "machine": info.get(esn, {}).get("machine", ""),
                            "err": str(e)[:60]}
            time.sleep(1.5 * (attempt + 1))
        return {"esn": esn, "ok": False,
                "machine": info.get(esn, {}).get("machine", ""), "err": "нет ответа"}

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
    print(f"  {'МАШИНА':<12} {'ESN':<12} {'ДВИГАТЕЛЬ':<20} {'CPL':<6} "
          f"{'КОНФИГУРАЦИЯ':<14} {'СБОРКА':<11} {'ДЕТАЛЕЙ':>8}")
    print("=" * 92)
    for r in sorted(good, key=lambda x: (x.get("machine", ""), x["esn"])):
        print(f"  {r.get('machine',''):<12} {r['esn']:<12} {str(r['model'] or ''):<20} "
              f"{str(r['cpl'] or ''):<6} {str(r['config'] or ''):<14} {r['build']:<11} "
              f"{r['parts']:>8}")
    if bad:
        print("\n  НЕТ В КАТАЛОГЕ CUMMINS (двигатель другой марки или номер не подходит):")
        for r in sorted(bad, key=lambda x: (x.get("machine", ""), x["esn"])):
            print(f"    {r.get('machine',''):<12} {r['esn']:<12} {r['err']}")

    # группировка по CPL
    groups = {}
    for r in good:
        groups.setdefault((r["cpl"], r["model"]), []).append(r)
    print("\n" + "=" * 76)
    print(f"  РАЗНЫХ CPL: {len(groups)}")
    print("=" * 76)
    to_crawl = []
    for (cpl, model), rows in sorted(groups.items(), key=lambda x: str(x[0][0])):
        # представитель группы — самый свежий по дате сборки
        rep = sorted(rows, key=lambda r: (r["build"], r["esn"]))[-1]
        configs = sorted({r["config"] for r in rows if r["config"]})
        to_crawl.append(rep["esn"])
        machines = sorted({r.get("machine", "") for r in rows if r.get("machine")})
        print(f"\n  CPL {cpl} · {model} · двигателей: {len(rows)} · "
              f"машины: {', '.join(machines) or '—'}")
        print(f"    конфигурации: {', '.join(configs)}")
        print(f"    качаем по: {rep['esn']} ({rep.get('machine','')}, сборка {rep['build']})")
        others = [r["esn"] for r in sorted(rows, key=lambda r: r["esn"]) if r["esn"] != rep["esn"]]
        if others:
            print(f"    остальные того же CPL ({len(others)}): {', '.join(others)}")

    print("\n" + "=" * 76)
    print(f"  ИТОГО КАЧАТЬ КАТАЛОГОВ: {len(to_crawl)} вместо {len(good)}")
    print(f"  Команда: " + "; ".join(f"python crawler.py {e}" for e in to_crawl[:3]) +
          (" ..." if len(to_crawl) > 3 else ""))
    print("=" * 76)

    Path(a.json).write_text(json.dumps(
        {"checked": res, "groups": [{"cpl": k[0], "model": k[1],
                                     "machines": sorted({r.get("machine", "") for r in v
                                                         if r.get("machine")}),
                                     "esns": [r["esn"] for r in v],
                                     "representative": sorted(v, key=lambda r: (r["build"], r["esn"]))[-1]["esn"]}
                                    for k, v in groups.items()],
         "to_crawl": to_crawl}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nОтчёт: {a.json}")


if __name__ == "__main__":
    main()
