#!/usr/bin/env python3
# Оценка объёма: число TSB по каждому ESN каталога.
import sys, io, os, json, re, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", write_through=True)

BASE = os.path.dirname(os.path.abspath(__file__))
ST = json.load(open(os.path.join(BASE, "storage_state.json"), encoding="utf-8"))
ck = "; ".join(f"{c['name']}={c['value']}" for c in ST["cookies"] if "cummins.com" in c.get("domain",""))
H = {"Cookie": ck, "User-Agent": "Mozilla/5.0", "X-Requested-With": "XMLHttpRequest",
     "Referer": "https://quickserve.cummins.com/qs3/portal/service/index.html"}
ROOT = "https://quickserve.cummins.com"

def get(path):
    req = urllib.request.Request(ROOT + path, headers=H)
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "replace")

ESNS = sys.argv[1:] or ["33239899", "37292556", "41353297", "41370103", "93087701"]
grand = {}
for esn in ESNS:
    try:
        se = get(f"/qs3/portal/includes/ajax/set_esn.json?esn={esn}&nocache=1")
        m = {k: (re.search(rf'"{k}":"([^"]*)"', se) or [None, ""])[1] for k in ("ef","fs","da","ma","pc","cpl","service","parts")}
        if not m["ef"]:
            print(f"{esn}: set_esn не дал фильтров -> {se[:120]}"); continue
        tsb = get(f"/qs3/portal/service/filter_tsb.json?group_num=&ef={m['ef']}&fs={m['fs']}&da={m['da']}&ma={m['ma']}&nocache=1")
        data = json.loads(tsb).get("data", [])
        open(os.path.join(BASE, f"tsb_{esn}.json"), "w", encoding="utf-8").write(tsb)
        grand[esn] = len(data)
        print(f"{esn}: CPL={m['cpl']} pc={m['pc']} service={m['service']} -> TSB={len(data)}")
    except Exception as e:
        print(f"{esn}: ОШИБКА {str(e)[:120]}")
print("\nИТОГО TSB (с дублями между двигателями):", sum(grand.values()))
