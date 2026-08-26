#!/usr/bin/env python3
# Только СЫРЬЁ: crawler.py -> crawl_details.py (с фото деталей) в rawdata/<esn>/.
# Каталог НЕ собираем — владелец соберёт позже. Идемпотентно, порядок: больше CPL -> меньше.
import sys, io, json, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                              errors="replace", write_through=True)
from pathlib import Path

BASE = Path(__file__).parent
PY = sys.executable
STATUS = BASE / "fetch_raw.status"

def status(s):
    STATUS.write_text(s, encoding="utf-8"); print(s, flush=True)

# представители недостающих CPL, от большего числа машин к меньшему
JOBS = [
    "33224404",  # CPL 3391 QSK50 Komatsu HD1500 (4)
    "37269910",  # CPL 1253 KTTA19-C700 БелАЗ 55т (3)
    "37280605",  # CPL 447  KTA19-C (3)
    "33210083",  # CPL 2699 QSK60-C (2)
    "71156161",  # CPL 8543 QSM11 40C3003 (2)
    "77804810",  # CPL 5977 15N CM2380 (2)
    "80248213",  # CPL 8760 QSX15 (2)
    "93948840",  # CPL 4858 QSZ13-C550 (2)
    "33224343",  # CPL 2849 QSK60 Komatsu PC-4000 (1)
    "35354607",  # CPL 8608 QSM11-C (1)
    "41340468",  # CPL 3728 QSK50 HD1500 поздн. (1)
    "77804793",  # CPL 6235 A8.5 CM2670 (1)
    "80141463",  # CPL 3088 QSX15 (1)
    "82099327",  # CPL 4375 QSB6.7-C190 (1)
    "85017333",  # CPL 2858 QSK23-C LiuGong (1)
    "93047320",  # CPL 3111 6BTA5.9-C155 (1)
]

def run(cmd):
    return subprocess.run([PY] + cmd, cwd=str(BASE)).returncode

def parts_ok(esn):
    rp = BASE / "rawdata" / esn / "report.json"
    if not rp.exists():
        return False, 0
    need = json.loads(rp.read_text(encoding="utf-8")).get("unique_parts_in_engine", 0)
    pd = BASE / "rawdata" / esn / "partdetails"
    have = len(list(pd.glob("*.json"))) if pd.exists() else 0
    return have >= need and need > 0, need

done = []
for i, esn in enumerate(JOBS, 1):
    if not (BASE / "rawdata" / esn / "report.json").exists():
        status(f"[{i}/{len(JOBS)}] {esn}: crawler (чертежи+узлы)")
        if run(["crawler.py", esn]) != 0:
            status(f"[{i}] {esn}: crawler FAILED, пропуск"); done.append((esn, "crawl_fail")); continue
    ok, need = parts_ok(esn)
    if not ok:
        status(f"[{i}/{len(JOBS)}] {esn}: crawl_details — карточки+фото ({need})")
        run(["crawl_details.py", esn, "--workers", "8"])
    ok, need = parts_ok(esn)
    done.append((esn, "ok" if ok else "partial"))
    status(f"[{i}/{len(JOBS)}] {esn}: {'готово' if ok else 'ЧАСТИЧНО'} ({need} деталей)")

status("ВСЁ ГОТОВО (raw): " + "; ".join(f"{e}={st}" for e, st in done))
