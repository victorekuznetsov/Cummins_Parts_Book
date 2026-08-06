#!/usr/bin/env python3
# Сравнение состава двигателей с одинаковым CPL: чем отличаются наборы деталей
# у разных дат выпуска и покрывает ли один каталог весь парк.
#
#   python tools/diff_esn.py 33229400 33230182 33231740 33233617 33236214 33239899
import sys, json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, str(Path(__file__).resolve().parent))
# check_esn сам настраивает вывод в UTF-8, поэтому импорт идёт до печати
from check_esn import new_session, API                      # переиспользуем сессию

esns = sys.argv[1:]
if not esns:
    sys.exit("укажите ESN через пробел")

s, xsrf = new_session()


def fetch(esn, tries=4):
    import time
    for a in range(1, tries + 1):
        try:
            r = s.get(f"{API}/v2/esnInfo/{esn}?esnType=mbom", timeout=60,
                      headers={"Accept": "application/json", "x-xsrf-token": xsrf})
            if r.status_code == 200:
                d = r.json()
                break
        except Exception as e:
            if a == tries:
                raise
        time.sleep(1.5 * a)
    else:
        raise RuntimeError(f"{esn}: нет ответа")
    parts, opts = {}, {}
    for o in (d.get("optionList") or []):
        opts[o.get("optionNo")] = o.get("optionName")
        for p in (o.get("parts") or []):
            if p.get("partNo"):
                parts[p["partNo"]] = p.get("partDesc") or ""
    return {"esn": esn, "build": str(d.get("buildDate") or "")[:10],
            "cpl": d.get("cpl"), "parts": parts, "opts": opts}


with ThreadPoolExecutor(max_workers=6) as ex:
    data = list(ex.map(fetch, esns))
data.sort(key=lambda x: x["build"])

print(f"\n{'ESN':<10} {'СБОРКА':<12} {'CPL':<6} {'УЗЛОВ':>6} {'ДЕТАЛЕЙ':>8}")
for d in data:
    print(f"{d['esn']:<10} {d['build']:<12} {str(d['cpl']):<6} "
          f"{len(d['opts']):>6} {len(d['parts']):>8}")

base = data[0]
union = set()
for d in data:
    union |= set(d["parts"])
common = set(data[0]["parts"])
for d in data[1:]:
    common &= set(d["parts"])

print(f"\nВсего разных номеров по всем двигателям: {len(union)}")
print(f"Общих для всех: {len(common)}")

print("\n--- отличия относительно самого раннего ---")
for d in data[1:]:
    add = sorted(set(d["parts"]) - set(base["parts"]))
    rem = sorted(set(base["parts"]) - set(d["parts"]))
    print(f"\n{d['esn']} ({d['build']}): добавлено {len(add)}, убрано {len(rem)}")
    for p in add[:12]:
        print(f"    + {p}  {d['parts'][p]}")
    for p in rem[:12]:
        print(f"    − {p}  {base['parts'][p]}")

# какой ESN покрывает больше всего номеров
best = max(data, key=lambda d: len(d["parts"]))
print(f"\nШире всех состав у {best['esn']} ({best['build']}): {len(best['parts'])} номеров, "
      f"не покрывает {len(union - set(best['parts']))} из объединения")
miss = sorted(union - set(best["parts"]))
for p in miss[:20]:
    who = next(d for d in data if p in d["parts"])
    print(f"    нет: {p}  {who['parts'][p]}  (есть у {who['esn']})")
