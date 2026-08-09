#!/usr/bin/env python3
# Сверка карточки конкретной детали с живым сайтом: есть ли замены номера,
# влияет ли параметр smn (серийный номер двигателя) на ответ.
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
# check_esn сам настраивает вывод в UTF-8, поэтому импорт идёт до печати
from check_esn import new_session, API

PART = sys.argv[1] if len(sys.argv) > 1 else "3088389"
ESN  = sys.argv[2] if len(sys.argv) > 2 else "33239899"

s, xsrf = new_session()
H = {"Accept": "application/json", "x-xsrf-token": xsrf}


def show(tag, url):
    r = s.get(url, timeout=60, headers=H)
    print(f"\n### {tag} -> HTTP {r.status_code}")
    if r.status_code != 200:
        print("   ", r.text[:200]); return None
    d = r.json()
    if isinstance(d, list):
        print("   список из", len(d), "элементов:", json.dumps(d, ensure_ascii=False)[:500])
        return d
    print("   наименование:", d.get("partDesc"))
    sup = d.get("supersession") or []
    print(f"   supersession: {len(sup)} элем.")
    for x in sup:
        print(f"      {x.get('partNo')}  seq={x.get('sequence')}  "
              f"{x.get('partSscDesc')}  sellable={x.get('sellable')}")
    print("   reconEquivalent:", d.get("reconEquivalent"))
    print("   oversize:", d.get("oversize"))
    print("   storestatus:", d.get("storestatus"))
    print("   sell:", d.get("sell"), " type:", d.get("type"))
    return d


show("partDetails без smn", f"{API}/protected/partDetails?partNo={PART}&smn=")
show(f"partDetails с smn={ESN}", f"{API}/protected/partDetails?partNo={PART}&smn={ESN}")
show("relatedParts", f"{API}/protected/relatedParts?partNo={PART}&size=10")
show("глобальный поиск", f"{API}/protected/searchService/global?criteria={PART}")
