#!/usr/bin/env python3
# Добавить процедуры мануалов в doc_manifest.json (cat=procedures) с привязкой к двигателям.
import sys, io, os, re, json, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", write_through=True)

BASE = os.path.dirname(os.path.abspath(__file__))
MANDIR = r"C:\Projects\cummins\bulletins\manual"
idx = json.load(open(r"C:\Projects\cummins\bulletins\index.json", encoding="utf-8"))
# manual id -> engines
man_eng = {re.sub(r"-history$", "", d["id"]): d["engines"] for d in idx if d["cat"] == "manual"}

pat = re.compile(r"/qs3/pubsys2/xml/en/procedures/[A-Za-z0-9/_.-]+\.html")
proc_eng = {}
for f in glob.glob(os.path.join(MANDIR, "*-history.html")):
    mid = re.sub(r"-history$", "", os.path.splitext(os.path.basename(f))[0])
    engs = set(man_eng.get(mid, []))
    h = open(f, encoding="utf-8", errors="replace").read()
    for u in set(pat.findall(h)):
        u = u.replace("procedures//", "procedures/")
        full = "https://quickserve.cummins.com" + u
        proc_eng.setdefault(full, set()).update(engs)

man = json.load(open(os.path.join(BASE, "doc_manifest.json"), encoding="utf-8"))
have = {d["url"] for d in man}
added = 0
for u, engs in proc_eng.items():
    if u not in have:
        man.append({"url": u, "cat": "procedures", "engines": sorted(engs)}); added += 1
json.dump(man, open(os.path.join(BASE, "doc_manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("процедур добавлено в манифест:", added, "| всего в манифесте:", len(man))
