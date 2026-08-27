#!/usr/bin/env python3
# =====================================================================
# Сборка каталога Cummins из сырья crawler.py / crawl_details.py.
#
#   python3 build/build_catalog.py 33210083            # один двигатель
#   python3 build/build_catalog.py --all               # всё сырьё в rawdata/
#   python3 build/build_catalog.py --all --photos      # плюс вендорить фото
#
# Сырьё лежит в rawdata/<ESN>/ (engine.json, options/, partdetails/, parts/,
# drawings/, kitSets.json, gasketSets.json). Скрипт создаёт/обновляет:
#   data/<ESN>.js     — данные двигателя (window.CATALOGS[<ESN>])
#   engines.js        — список двигателей для переключателя в шапке
#   drawings/<ESN>/   — чертежи узлов
#   parts/<ESN>/      — фотографии деталей (только с --photos: это ~150 МБ
#                       на двигатель; без флага фото берутся из rawdata/,
#                       базы знаний или с CDN parts.cummins.com — цепочку
#                       подстановки см. в photoFallback() в app.js)
#   index.html        — <script> на файлы данных
# Оболочка (app.js, styles.css, разметка index.html) не трогается.
#
# Цены здесь не подставляются: каталог берёт их из data/prices.js
# (прайс «Горная Евразия»: текущий и несогласованный) уже в браузере.
# =====================================================================
import sys, io, json, re, shutil, argparse, csv
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW  = ROOT / "rawdata"

# Русские названия систем — как их показывает сайт Cummins
SYSTEM_RU = {
    "AFTERTREATMENT": "Система нейтрализации",
    "AIR INTAKE": "Воздухозаборник",
    "BASE ENGINE": "Базовый двигатель",
    "COMPRESSORS AND PUMPS": "Компрессоры и насосы",
    "COOLING": "Система охлаждения",
    "DRIVES AND MOUNTINGS": "Приводы и крепления",
    "ELECTRICS": "Электрооборудование",
    "EXHAUST": "Система выпуска",
    "FUEL": "Топливная система",
    "LUBRICATION": "Система смазки",
    "MISCELLANEOUS": "Прочее",
    "RATINGS AND CALIBRATIONS": "Номиналы и калибровки",
    "UNCLASSIFIED": "Без системы",
}

# Участок парка -> машина. Участки называет владелец парка, и не в каждом
# названии есть машина: где её нет, поле «Машина» остаётся пустым.
PLACE_MACHINE = {
    "АТЦ_Парк автосамосвалов Komatsu HD1500": "Komatsu HD1500",
    "Парк Komatsu HD1500": "Komatsu HD1500",
    "АТЦ_Парк автосамосвалов Komatsu 730E": "Komatsu 730E",
    "УОГР_ПаркЭкскаватор_Komatsu PC-4000": "Komatsu PC-4000",
    "СЭБТ - Коматсу - 220 тн": "Komatsu 220 т",
    "СЭБТ - Коматсу - 141 тн": "Komatsu 141 т",
    "Парк экскаваторов LiuGong 9125F": "LiuGong 9125F",
    "Парк экскаваторов LiuGongCLG942": "LiuGong CLG942",
    "АТЦ_Парк погрузчиков LiuGong": "LiuGong",
    "Парк БелАз 55 т": "БелАЗ 55 т",
    "АТЦ_Парк БелАЗ 75473 (ПЩК)": "БелАЗ 75473",
    "СЭБТ - Белазы": "БелАЗ",
    "Парк бульдозеров Shantui SD60-C5": "Shantui SD60-C5",
    "Парк бульдозеров Shantui SD34": "Shantui SD34",
    "Парк буровых IR DML": "IR DML",
    "Парк буровых DM-75": "DM-75",
    "Парк буровых Sandvik DE": "Sandvik DE",
    "Парк ZEGA D480A": "ZEGA D480A",
    "Парк Yangzi DR75": "Yangzi DR75",
}

IN_MM, LB_KG = 25.4, 0.45359237


def safe(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]+', "_", str(name)).strip(". ") or "unnamed"


def drawing_file(fname: str) -> str:
    return safe(fname.strip("/").replace("/", "_")) + ".png"


def _num(v):
    m = re.search(r"-?\d+(?:[.,]\d+)?", str(v or ""))
    return float(m.group(0).replace(",", ".")) if m else None


def _conv(value, to):
    """'7.25 in' -> мм, '2.32 lb' -> кг."""
    n = _num(value)
    if n is None:
        return ""
    s = str(value).lower()
    if to == "mm":
        return f"{n * IN_MM if 'in' in s else n:.0f}"
    n = n * LB_KG if "lb" in s else n
    return f"{n:.2f}".rstrip("0").rstrip(".")


def flatten_parts(groups):
    """Плоский список позиций с сохранением уровня вложенности подкомпонентов."""
    out = []

    def walk(node, level):
        d = node.get("data") or {}
        pn = d.get("partNo")
        if pn or d.get("partDesc"):
            out.append({
                "pos":  (d.get("callOut") or "").strip(),
                "no":   (pn or "").strip(),
                "name": (d.get("partDesc") or "").strip(),
                "qty":  (d.get("qty") or "").strip(),
                "dim":  (d.get("dimensions") or "").strip(),
                "rem":  (d.get("remarks") or "").strip(),
                "lvl":  level,
                "img":  "",
            })
        for ch in (node.get("children") or []):
            walk(ch, level + 1)

    for g in (groups or []):
        for p in (g.get("parts") or []):
            walk(p, 0)
    return out


def load_part_cards(src, part_nos):
    """Карточки деталей: атрибуты, замены номеров, где применяется, ракурсы фото."""
    pdir, cards, views = src / "partdetails", {}, set()
    n_sup = 0
    if not pdir.exists():
        return cards, views, 0
    for pn in sorted(part_nos):
        f = pdir / f"{safe(pn)}.json"
        if not f.exists():
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        attrs = {}
        for block in (d.get("metadata") or []):
            for a in (block.get("attributes") or []):
                for _, v in a.items():
                    nm, val = (v.get("name") or "").strip(), (v.get("value") or "").strip()
                    if nm and val:
                        attrs[nm] = val
        # цепочка замен: sequence 1 — действующий номер, дальше по убыванию — старые
        sup = []
        for s in (d.get("supersession") or []):
            if not isinstance(s, dict) or not s.get("partNo"):
                continue
            sup.append({
                "no":   str(s["partNo"]).strip(),
                "st":   re.sub(r"^\d+-\s*", "",
                               str(s.get("partSscDesc") or s.get("partSsc") or "")).strip(),
                "sell": (s.get("sellable") == "Y"),
                "seq":  int(_num(s.get("sequence")) or 0),
            })
        sup.sort(key=lambda x: -x["seq"])       # от старого номера к новому
        if len(sup) > 1:
            n_sup += 1
        vs = []
        for g in (d.get("graphics") or []):
            fn = g.get("fileName")
            if fn:
                nm = safe(fn.rsplit("/", 1)[-1])
                if (src / "parts" / nm).exists():
                    vs.append(nm); views.add(nm)
        card = {
            "wt":    _conv(attrs.get("Weight"), "kg"),
            "dim":   "×".join(x for x in (_conv(attrs.get("Length"), "mm"),
                                          _conv(attrs.get("Width"), "mm"),
                                          _conv(attrs.get("Height"), "mm")) if x),
            "attrs": attrs,
            "sup":   sup,
            "recon": d.get("reconEquivalent") or "",
            "used":  [{"o": w.get("item"), "n": w.get("itemDesc") or ""}
                      for w in (d.get("whereUsed") or []) if w.get("itemType") == "O"][:60],
            "views": sorted(vs, key=lambda x: (0 if "_iso." in x else 1, x)),
        }
        cards[pn] = {k: v for k, v in card.items() if v not in ("", [], {}, None)}
    return cards, views, n_sup


def load_kits(src):
    """Ремкомплекты (kitSets.json) и комплекты прокладок (gasketSets.json).

    У комплекта прокладок нет отдельного номера: номер набора — это первая
    позиция в его составе, там же и наименование."""
    kits = []
    kf = src / "kitSets.json"
    if kf.exists():
        for k in json.loads(kf.read_text(encoding="utf-8")):
            if not k.get("kitNo"):
                continue
            kits.append({
                "no": k["kitNo"], "name": k.get("kitDesc") or k["kitNo"],
                "notes": k.get("kitNotes") or "", "type": k.get("kitType") or "",
                "parts": [{"no": p.get("partNo"), "name": p.get("partDesc")}
                          for p in (k.get("parts") or [])],
            })
    gf = src / "gasketSets.json"
    have = {k["no"] for k in kits}
    if gf.exists():
        for g in json.loads(gf.read_text(encoding="utf-8")):
            parts = g.get("parts") or []
            no = (parts[0].get("partNo") if parts else "") or ""
            if not no or no in have:
                continue
            have.add(no)
            kits.append({
                "no": no, "name": g.get("description") or parts[0].get("partDesc") or no,
                "notes": "", "type": "GASKET",
                "parts": [{"no": p.get("partNo"), "name": p.get("partDesc")} for p in parts],
            })
    return kits


def fleet_info(esn):
    """Машина / владелец / участок по спискам парка в fleet/."""
    info = {"machine": "", "owner": "", "place": ""}
    f = ROOT / "fleet" / "fleet.tsv"          # прежний парк: machine vin esn epc
    if f.exists():
        for row in csv.DictReader(f.open(encoding="utf-8"), delimiter="\t"):
            if (row.get("esn") or "").strip() == esn:
                info["machine"] = (row.get("machine") or "").strip()
                break
    p = ROOT / "fleet" / "polyus.tsv"         # esn owner place name model_doc year
    if p.exists():
        for row in csv.DictReader(p.open(encoding="utf-8"), delimiter="\t"):
            if (row.get("esn") or "").strip() == esn:
                info["owner"] = (row.get("owner") or "").strip()
                info["place"] = (row.get("place") or "").strip()
                if not info["machine"]:
                    info["machine"] = PLACE_MACHINE.get(info["place"], "")
                break
    return info


def update_registry(catalog, info):
    """engines.js — список двигателей для переключателя в шапке."""
    reg = ROOT / "engines.js"
    engines = {}
    if reg.exists():
        m = re.search(r"window\.ENGINES\s*=\s*(\[.*?\]);", reg.read_text(encoding="utf-8"), re.S)
        if m:
            for e in json.loads(m.group(1)):
                engines[e["esn"]] = e
    prev = engines.get(catalog["esn"], {})
    rec = {
        "esn": catalog["esn"], "model": catalog["model"], "cpl": catalog["cpl"],
        "machine": info.get("machine") or prev.get("machine", ""),
        "build": catalog["buildDate"], "config": catalog["config"],
        "options": len(catalog["options"]),
        "parts": len({p["no"] for o in catalog["options"] for p in o["parts"] if p["no"]}),
        "fleet": prev.get("fleet", []),
    }
    for k in ("owner", "place"):
        v = info.get(k) or prev.get(k, "")
        if v:
            rec[k] = v
    engines[catalog["esn"]] = rec
    rows = sorted(engines.values(), key=lambda e: (str(e.get("machine") or "я"), str(e["model"])))
    reg.write_text("window.ENGINES = " + json.dumps(rows, ensure_ascii=False, indent=1) + ";\n",
                   encoding="utf-8")
    return rows


def update_index(engines):
    """index.html: подключён только engines.js. Сами данные двигателей каталог
    подгружает по требованию (loadCatalog в app.js): вместе они весят десятки
    мегабайт, и грузить их все при открытии страницы нельзя."""
    idx = ROOT / "index.html"
    html = idx.read_text(encoding="utf-8")
    new, n = re.subn(r'<script src="engines\.js"></script>(?:\s*<script src="data/\d+\.js"></script>)*',
                     '<script src="engines.js"></script>', html, count=1)
    if not n:
        sys.exit('!! в index.html не найден <script src="engines.js">')
    if new != html:
        idx.write_text(new, encoding="utf-8")


def build(esn, copy_photos=False):
    src = RAW / esn
    if not (src / "engine.json").exists():
        sys.exit(f"нет сырья {src}/engine.json — сначала crawler.py {esn}")

    engine = json.loads((src / "engine.json").read_text(encoding="utf-8"))

    # система -> варианты исполнения (берём из состава двигателя)
    sys_of_option = {}
    for o in (engine.get("optionList") or []):
        s = {x for p in (o.get("parts") or []) for x in (p.get("systems") or [])}
        sys_of_option[o.get("optionNo")] = sorted(s) or ["UNCLASSIFIED"]

    options, all_sheets, all_photos = [], set(), set()
    for f in sorted((src / "options").glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        no = d.get("optionNo") or f.stem
        parts = flatten_parts(d.get("groups"))
        sheets = [drawing_file(g["fileName"]) for g in (d.get("graphics") or [])
                  if g.get("fileName") and (src / "drawings" / drawing_file(g["fileName"])).exists()]
        all_sheets.update(sheets)
        for p in parts:
            photo = f"{safe(p['no'])}_iso.png"
            if p["no"] and (src / "parts" / photo).exists():
                p["img"] = photo
                all_photos.add(photo)
        options.append({
            "no": no,
            "name": d.get("optionName") or no,
            "systems": sys_of_option.get(no, ["UNCLASSIFIED"]),
            "remarks": (d.get("remarks") or "").strip(),
            "sheets": sheets,
            "parts": parts,
        })

    kits = load_kits(src)

    systems = []
    for code in sorted({s for o in options for s in o["systems"]}):
        systems.append({
            "code": code,
            "name": SYSTEM_RU.get(code, code.title()),
            "options": sorted([o["no"] for o in options if code in o["systems"]]),
        })

    uniq_nos = {p["no"] for o in options for p in o["parts"] if p["no"]}
    cards, card_views, n_sup = load_part_cards(src, uniq_nos)
    all_photos.update(card_views)

    catalog = {
        "esn": esn,
        "model": engine.get("serviceModel"),
        "cpl": engine.get("cpl"),
        "buildDate": str(engine.get("buildDate") or "")[:10],
        "config": engine.get("marketingConfig"),
        "group": engine.get("engineGroup"),
        "plant": engine.get("enginePlantCode"),
        "hasPrices": False,
        "systems": systems,
        "options": options,
        "kits": kits,
        "cards": cards,
    }
    # фото не вендорим — каталог берёт их из rawdata/<ESN>/parts (см. app.js)
    if not copy_photos:
        catalog["photos"] = "rawdata/" + esn + "/parts"

    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / f"{esn}.js").write_text(
        'window.CATALOGS = window.CATALOGS || {};\nwindow.CATALOGS["' + esn + '"] = ' +
        json.dumps(catalog, ensure_ascii=False, separators=(",", ":")) + ";\n",
        encoding="utf-8")

    copied = {"drawings": 0, "parts": 0}
    jobs = [("drawings", all_sheets)] + ([("parts", all_photos)] if copy_photos else [])
    for sub, names in jobs:
        dst = ROOT / sub / esn
        dst.mkdir(parents=True, exist_ok=True)
        for n in names:
            s = src / sub / n
            if s.exists() and not (dst / n).exists():
                shutil.copy2(s, dst / n); copied[sub] += 1

    info = fleet_info(esn)
    engines = update_registry(catalog, info)
    update_index(engines)

    total_pos = sum(len(o["parts"]) for o in options)
    size = (ROOT / "data" / f"{esn}.js").stat().st_size / 1024
    print(f">>> {esn} · {catalog['model']} · CPL {catalog['cpl']}"
          f"{' · ' + info['machine'] if info['machine'] else ''}"
          f"{' · ' + info['place'] if info['place'] else ''}")
    print(f"    систем {len(systems)}, узлов {len(options)}, позиций {total_pos}, "
          f"деталей {len(uniq_nos)}, карточек {len(cards)} (с заменами {n_sup})")
    print(f"    комплектов {len(kits)}, чертежей {len(all_sheets)} (скопировано {copied['drawings']}), "
          f"фото {len(all_photos)}" + (f" (скопировано {copied['parts']})" if copy_photos else " (из rawdata)"))
    print(f"    data/{esn}.js — {size:.0f} КБ; всего двигателей в каталоге: {len(engines)}")

    from_engine = {p["partNo"] for o in (engine.get("optionList") or [])
                   for p in (o.get("parts") or []) if p.get("partNo")}
    lost = sorted(from_engine - uniq_nos)
    if lost:
        print(f"    !! ПОТЕРЯНО НОМЕРОВ: {len(lost)} -> {lost[:10]}")
    return not lost


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Сборка каталога Cummins из rawdata/")
    ap.add_argument("esn", nargs="*", help="серийные номера двигателей")
    ap.add_argument("--all", action="store_true", help="все двигатели из rawdata/")
    ap.add_argument("--photos", action="store_true",
                    help="скопировать фотографии деталей в parts/<ESN>/ (~150 МБ на двигатель)")
    a = ap.parse_args()
    esns = a.esn
    if a.all:
        esns = sorted(d.name for d in RAW.iterdir() if (d / "engine.json").exists())
    if not esns:
        ap.error("укажите ESN или --all")
    ok = True
    for i, e in enumerate(esns, 1):
        print(f"--- [{i}/{len(esns)}] {e} " + "-" * 40)
        ok = build(e, a.photos) and ok
    sys.exit(0 if ok else 1)
