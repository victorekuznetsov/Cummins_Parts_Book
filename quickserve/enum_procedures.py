#!/usr/bin/env python3
import sys, io, re, glob, os, json, statistics
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace", write_through=True)

MAN = r"C:\Projects\cummins\bulletins\manual"
pat = re.compile(r"/qs3/pubsys2/xml/en/procedures/[A-Za-z0-9/_.-]+\.html")
procs = set(); per = {}
for f in glob.glob(os.path.join(MAN, "*-history.html")):
    h = open(f, encoding="utf-8", errors="replace").read()
    links = set(pat.findall(h))
    per[os.path.basename(f)] = len(links)
    procs |= links
print("страниц-историй:", len(per))
print("УНИКАЛЬНЫХ процедур:", len(procs))
if per:
    vals = list(per.values())
    print("процедур на мануал: min=%d med=%d max=%d" % (min(vals), int(statistics.median(vals)), max(vals)))
print("примеры:", sorted(procs)[:5])
json.dump(sorted("https://quickserve.cummins.com" + u for u in procs),
          open(r"C:\Projects\cummins\quickserve\procedures.json", "w", encoding="utf-8"), indent=1)
print("-> procedures.json")
