#!/usr/bin/env python3
# Вызовы QSOL API с сохранённой сессией (storage_state.json).
import sys, io, os, json, urllib.request, urllib.parse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", write_through=True)

BASE = os.path.dirname(os.path.abspath(__file__))
ST = json.load(open(os.path.join(BASE, "storage_state.json"), encoding="utf-8"))
cookies = "; ".join(f"{c['name']}={c['value']}" for c in ST.get("cookies", [])
                    if "cummins.com" in c.get("domain", ""))
HDR = {
    "Cookie": cookies,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://quickserve.cummins.com/qs3/portal/index.html",
}
ROOT = "https://quickserve.cummins.com"

def get(path, raw=False):
    req = urllib.request.Request(ROOT + path, headers=HDR)
    with urllib.request.urlopen(req, timeout=40) as r:
        data = r.read()
    return data if raw else data.decode("utf-8", "replace")

print("cookies:", [c["name"] for c in ST.get("cookies", []) if "cummins.com" in c.get("domain","")][:12])

esn = sys.argv[1] if len(sys.argv) > 1 else "33239899"
print("\n=== set_esn", esn, "===")
print(get(f"/qs3/portal/includes/ajax/set_esn.json?esn={esn}&nocache=1")[:300])

print("\n=== filter_tsb.json ===")
body = get("/qs3/portal/service/filter_tsb.json?group_num=&ef=28&fs=41&da=2&ma=4&nocache=1")
open(os.path.join(BASE, f"tsb_{esn}.json"), "w", encoding="utf-8").write(body)
print("длина:", len(body))
try:
    d = json.loads(body)
    print("тип:", type(d).__name__)
    if isinstance(d, dict):
        print("ключи:", list(d.keys()))
        for k, v in d.items():
            if isinstance(v, list):
                print(f"  {k}: список из {len(v)}; пример:", json.dumps(v[0], ensure_ascii=False)[:300] if v else "—")
    elif isinstance(d, list):
        print("список из", len(d), "; пример:", json.dumps(d[0], ensure_ascii=False)[:300])
except Exception as e:
    print("не JSON:", e, "| начало:", body[:200])
