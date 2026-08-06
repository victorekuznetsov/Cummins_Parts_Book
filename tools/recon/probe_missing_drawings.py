#!/usr/bin/env python3
# Проверка: существуют ли чертежи для узлов, по которым API не отдал ссылку.
# Имя файла выводим из номера узла: AH5005-06 -> /095/ah/095_ah0500500_06
import sys, io, json, re, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
import requests
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent.parent
ESN  = sys.argv[1] if len(sys.argv) > 1 else "37292556"
API  = "https://parts.cummins.com/gateway/api/IACDataServices"
UA   = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")


def graphic_path(option_no, plant):
    """AH5005-06 -> /095/ah/095_ah0500500_06 ; номер дополняется до 5 знаков + '00'."""
    m = re.match(r"^([A-Za-z]+)(\d+)(?:-(\w+))?$", option_no)
    if not m:
        return None
    letters, number, suffix = m.group(1).lower(), m.group(2), (m.group(3) or "00")
    return f"/{plant}/{letters}/{plant}_{letters}{number.zfill(5)}00_{suffix}"


with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(user_agent=UA)
    page = ctx.new_page()
    page.goto("https://parts.cummins.com/home", wait_until="networkidle", timeout=120000)
    page.wait_for_timeout(2500)
    cookies = {c["name"]: c["value"] for c in ctx.cookies()}
    b.close()

s = requests.Session()
s.headers.update({"User-Agent": UA, "Referer": "https://parts.cummins.com/esn-entry/main"})
for k, v in cookies.items():
    s.cookies.set(k, v, domain="parts.cummins.com")

# 1. Сверяем формулу на узлах, где ссылка известна
print(">>> Проверка формулы на известных чертежах")
ok = bad = 0
for f in sorted(glob.glob(str(ROOT / "data" / ESN / "options" / "*.json"))):
    d = json.loads(Path(f).read_text(encoding="utf-8"))
    gs = [g["fileName"] for g in (d.get("graphics") or []) if g.get("fileName")]
    if len(gs) != 1:
        continue                      # многолистовые проверим отдельно
    want = graphic_path(d.get("optionNo"), d.get("optionPlantCode") or "095")
    if want == gs[0]:
        ok += 1
    else:
        bad += 1
        if bad <= 5:
            print(f"    расхождение: {d.get('optionNo')} -> формула {want}, факт {gs[0]}")
print(f"    совпало {ok}, разошлось {bad}")

# 2. Пробуем выведенные адреса для узлов без чертежа
print("\n>>> Узлы с позициями, но без ссылки на чертёж")
found = []
for f in sorted(glob.glob(str(ROOT / "data" / ESN / "options" / "*.json"))):
    d = json.loads(Path(f).read_text(encoding="utf-8"))
    n = sum(len(g.get("parts") or []) for g in (d.get("groups") or []))
    if not n or (d.get("graphics") or []):
        continue
    no = d.get("optionNo")
    base = graphic_path(no, d.get("optionPlantCode") or "095")
    if not base:
        print(f"    {no}: не разобрать номер"); continue
    hits = []
    for cand in [base] + [f"{base}_{i}" for i in range(1, 6)]:
        r = s.get(f"{API}/graphics/rtgraphics/english/parts{cand}.png", timeout=45)
        if r.status_code == 200 and r.content:
            hits.append((cand, len(r.content)))
        elif not hits and cand == base:
            pass
    if hits:
        found.append((no, hits))
        print(f"    [ЕСТЬ] {no}: " + ", ".join(f"{c} ({sz//1024} КБ)" for c, sz in hits))
    else:
        print(f"    [нет ] {no}: {base}.png -> 404")

print(f"\nИТОГ: чертежи нашлись у {len(found)} из проверенных узлов")
