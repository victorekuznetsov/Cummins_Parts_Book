#!/usr/bin/env python3
# QSOL-документация для НОВЫХ двигателей -> rawdata/quickserve/<cat>/ (HTML+PDF).
# Сверяется с уже скачанным в bulletins/ (по index.json) и НЕ дублирует.
# Этапы: перечисление -> скачивание (кроме процедур) -> процедуры из историй
# мануалов -> скачивание процедур. Резюмируемо.
import sys, io, os, json, re, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                              errors="replace", write_through=True)
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = r"C:\Projects\cummins"
OUT = os.path.join(ROOT, "rawdata", "quickserve")
BULL = os.path.join(ROOT, "bulletins")
STATE = os.path.join(BASE, "storage_state.json")
STATUS = os.path.join(BASE, "qs_raw.status")

NEW_ESNS = ["33210083","33219033","33224343","33224404","35354607","35373113",
            "37269910","37280605","41340468","71156161","77804793","77804810",
            "80141463","80248213","82099327","85017333","93047320","93948840",
            "33239746"]  # NTE240, QSK60 CM2150 MCRS, CPL 3451 — своей выгрузки не было

CAT_RE = re.compile(r"/qs3/pubsys2/xml/\w+/(tsb|bulletin|manual|install_inst|sti|outlines|procedures)/")
PROC_RE = re.compile(r"/qs3/pubsys2/xml/en/procedures/[A-Za-z0-9/_.-]+\.html")

def status(s): open(STATUS,"w",encoding="utf-8").write(s); print(s, flush=True)
def categorize(h):
    m = CAT_RE.search(h); return m.group(1) if m else "other"
def doc_id(url):
    seg = url.split("?")[0].rstrip("/").split("/")[-1]
    return re.sub(r"\.html?$", "", seg)

# --- уже скачанное ранее (bulletins/) — для дедупликации ---
existing = set()
bidx = os.path.join(BULL, "index.json")
if os.path.exists(bidx):
    for d in json.load(open(bidx, encoding="utf-8")):
        existing.add((d["cat"], d["id"]))
status(f"уже в bulletins/: {len(existing)} документов (пропустим их)")

def add(docs, url, esn, cat=None):
    url = url.split("#")[0]
    cat = cat or categorize(url)
    d = docs.setdefault(url, {"cat": cat, "engines": set()})
    d["engines"].add(esn)

def download(pg, url, cat, engines, stats):
    did = doc_id(url)
    if (cat, did) in existing:
        stats["dedup"] += 1
        return {"id": did, "cat": cat, "url": url, "engines": engines,
                "in_bulletins": True}
    cdir = os.path.join(OUT, cat); os.makedirs(cdir, exist_ok=True)
    fhtml = os.path.join(cdir, did + ".html"); fpdf = os.path.join(cdir, did + ".pdf")
    rec = {"id": did, "cat": cat, "url": url, "engines": engines,
           "html": os.path.relpath(fhtml, OUT), "pdf": os.path.relpath(fpdf, OUT)}
    if os.path.exists(fhtml) and os.path.exists(fpdf) and os.path.getsize(fpdf) > 1000:
        stats["skip"] += 1; return rec
    try:
        pg.goto(url, wait_until="networkidle", timeout=45000)
        pg.wait_for_timeout(800)
        txt = pg.inner_text("body")[:400]
        if "File not found" in txt and len(txt) < 40:
            stats["notfound"] += 1; rec["missing"] = True; return rec
        open(fhtml, "w", encoding="utf-8").write(pg.content())
        pg.pdf(path=fpdf, format="A4", print_background=True,
               margin={"top":"10mm","bottom":"10mm","left":"8mm","right":"8mm"})
        stats["ok"] += 1
    except Exception as e:
        stats["err"] += 1; print(f"  ERR {cat}/{did}: {str(e)[:70]}")
    return rec

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True)
    ctx = b.new_context(storage_state=STATE)
    pg = ctx.new_page()

    # ---- Этап 1: перечисление (сервисные страницы + tsb-файлы) ----
    docs = {}
    for esn in NEW_ESNS:
        pg.goto(f"https://quickserve.cummins.com/qs3/portal/includes/ajax/set_esn.json?esn={esn}", timeout=30000)
        pg.goto("https://quickserve.cummins.com/qs3/portal/service/index.html",
                wait_until="networkidle", timeout=60000)
        pg.wait_for_timeout(3000)
        hrefs = pg.eval_on_selector_all("a[href]", "els=>els.map(e=>e.getAttribute('href'))")
        for h in hrefs:
            if not h or "/qs3/pubsys2/xml/" not in h: continue
            m = re.search(r"path=(/qs3/pubsys2/xml/[^&]+)", h)
            url = m.group(1) if m else h
            if not url.startswith("http"):
                url = "https://quickserve.cummins.com" + url
            add(docs, url, esn)
        tsbf = os.path.join(BASE, f"tsb_{esn}.json")
        if os.path.exists(tsbf):
            for x in json.load(open(tsbf, encoding="utf-8")).get("data", []):
                if x["doc_type"] == "37":
                    u = f"https://quickserve.cummins.com/qs3/pubsys2/xml/{x['language']}/tsb/{x['doc_year']}/{x['doc_num']}.html"
                else:
                    u = f"https://quickserve.cummins.com/qs3/pubsys2/xml/{x['language']}/bulletin/{x['doc_num']}.html"
                add(docs, u, esn)
        status(f"перечисление {esn}: всего уникальных {len(docs)}")

    from collections import Counter
    status("по категориям: " + json.dumps(Counter(d["cat"] for d in docs.values())))

    # ---- Этап 2: скачивание всего, кроме процедур ----
    stats = {"ok":0,"skip":0,"dedup":0,"notfound":0,"err":0}
    index = []
    round1 = [(u,d) for u,d in docs.items() if d["cat"] != "procedures"]
    for i,(u,d) in enumerate(round1,1):
        index.append(download(pg, u, d["cat"], sorted(d["engines"]), stats))
        if i % 25 == 0:
            status(f"[1/{len(round1)}] i={i} ok={stats['ok']} skip={stats['skip']} "
                   f"dedup={stats['dedup']} 404={stats['notfound']}")

    # ---- Этап 3: процедуры из историй мануалов (новые мануалы в rawdata) ----
    man_eng = {re.sub(r'-history$','',doc_id(u)): sorted(d["engines"])
               for u,d in docs.items() if d["cat"]=="manual"}
    proc = {}
    mandir = os.path.join(OUT, "manual")
    if os.path.isdir(mandir):
        import glob
        for f in glob.glob(os.path.join(mandir, "*-history.html")):
            mid = re.sub(r'-history$','', os.path.splitext(os.path.basename(f))[0])
            engs = set(man_eng.get(mid, []))
            h = open(f, encoding="utf-8", errors="replace").read()
            for uu in set(PROC_RE.findall(h)):
                uu = uu.replace("procedures//","procedures/")
                proc.setdefault("https://quickserve.cummins.com"+uu, set()).update(engs)
    status(f"процедур найдено в новых мануалах: {len(proc)}")

    # ---- Этап 4: скачивание процедур ----
    plist = list(proc.items())
    for i,(u,engs) in enumerate(plist,1):
        index.append(download(pg, u, "procedures", sorted(engs), stats))
        if i % 50 == 0:
            status(f"[2/{len(plist)}] i={i} ok={stats['ok']} skip={stats['skip']} "
                   f"dedup={stats['dedup']} 404={stats['notfound']}")
    b.close()

os.makedirs(OUT, exist_ok=True)
json.dump(index, open(os.path.join(OUT,"index.json"),"w",encoding="utf-8"),
          ensure_ascii=False, indent=1)
status(f"ГОТОВО: ok={stats['ok']} skip={stats['skip']} dedup(bulletins)={stats['dedup']} "
       f"404={stats['notfound']} err={stats['err']} | index -> {OUT}\\index.json")
