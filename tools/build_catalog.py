#!/usr/bin/env python3
# =====================================================================
# Сборка интерактивного веб-каталога из выгрузки crawler.py.
#
#   python tools/build_catalog.py 37292556 [--prices прайс.xlsx]
#
# Читает data/<ESN>/ (engine.json, systems.json, options/*.json, drawings/, parts/)
# и создаёт catalog/:
#   data.js      — все данные каталога одним файлом (window.CATALOG),
#                  чтобы index.html открывался двойным щелчком, без сервера
#   drawings/    — чертежи узлов
#   parts/       — фото деталей
# Оболочка (index.html, app.js, styles.css) статическая и не перезаписывается.
# =====================================================================
import sys, io, json, re, shutil, argparse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT  = ROOT / "catalog"

# Русские названия систем — как их показывает сайт Cummins
SYSTEM_RU = {
    "AIR INTAKE": "Воздухозаборник",
    "BASE ENGINE": "Базовый двигатель",
    "COMPRESSORS AND PUMPS": "Компрессоры и насосы",
    "COOLING": "Охлаждение",
    "DRIVES AND MOUNTINGS": "Приводы и крепления",
    "ELECTRICS": "Электрооборудование",
    "EXHAUST": "Выпуск",
    "FUEL": "Топливная система",
    "LUBRICATION": "Смазка",
    "MISCELLANEOUS": "Прочее",
    "RATINGS AND CALIBRATIONS": "Номиналы и калибровки",
    "UNCLASSIFIED": "Без системы",
}


def safe(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]+', "_", str(name)).strip(". ") or "unnamed"


def drawing_file(fname: str) -> str:
    """Имя файла чертежа так же, как его сохранил crawler.py."""
    return safe(fname.strip("/").replace("/", "_")) + ".png"


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
                "img":  bool(d.get("hasGraphic")),
            })
        for ch in (node.get("children") or []):
            walk(ch, level + 1)

    for g in (groups or []):
        for p in (g.get("parts") or []):
            walk(p, 0)
    return out


IN_MM, LB_KG = 25.4, 0.45359237


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
        # цепочка замен: sequence 1 — актуальный номер, дальше по убыванию — старые
        sup = []
        for s in (d.get("supersession") or []):
            if not isinstance(s, dict) or not s.get("partNo"):
                continue
            sup.append({
                "no":   str(s["partNo"]).strip(),
                "st":   re.sub(r"^\d+-\s*", "", str(s.get("partSscDesc") or s.get("partSsc") or "")).strip(),
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


def load_prices(path):
    """Прайс-лист xlsx: первый столбец с номером детали, ищем цену и аналитики."""
    if not path:
        return {}
    try:
        from openpyxl import load_workbook
    except ImportError:
        print("!! openpyxl не установлен (pip install openpyxl) — цены пропущены")
        return {}
    wb = load_workbook(path, read_only=True, data_only=True)
    ws = wb.active
    rows = ws.iter_rows(values_only=True)
    header = [str(c or "").strip().lower() for c in next(rows)]

    def col(*keys):
        for i, h in enumerate(header):
            if any(k in h for k in keys):
                return i
        return None

    i_no    = col("номер", "артикул", "part")
    i_price = col("цена", "price", "стоим")
    i_name  = col("наимен", "назв", "descr")
    i_grp   = col("группа", "group")
    i_alt   = col("взаимозамен", "аналог", "замена", "alt")
    if i_no is None or i_price is None:
        print(f"!! в прайсе не нашёл колонок номера/цены (заголовки: {header[:8]}) — цены пропущены")
        return {}
    prices = {}
    for r in rows:
        if not r or i_no >= len(r) or not r[i_no]:
            continue
        key = re.sub(r"\s+", "", str(r[i_no])).upper()
        val = r[i_price] if i_price < len(r) else None
        prices[key] = {
            "price": float(val) if isinstance(val, (int, float)) else None,
            "name":  str(r[i_name]).strip() if i_name is not None and i_name < len(r) and r[i_name] else "",
            "group": str(r[i_grp]).strip() if i_grp is not None and i_grp < len(r) and r[i_grp] else "",
            "alt":   str(r[i_alt]).strip() if i_alt is not None and i_alt < len(r) and r[i_alt] else "",
        }
    print(f">>> Прайс-лист: {len(prices)} позиций из {Path(path).name}")
    return prices


def build(esn, prices_path=None):
    src = ROOT / "data" / esn
    if not (src / "engine.json").exists():
        sys.exit(f"нет выгрузки {src} — сначала запустите crawler.py {esn}")

    engine = json.loads((src / "engine.json").read_text(encoding="utf-8"))
    prices = load_prices(prices_path)

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
            pr = prices.get(re.sub(r"\s+", "", p["no"]).upper())
            if pr:
                p["price"] = pr["price"]
                if pr["group"]: p["group"] = pr["group"]
                if pr["alt"]:   p["alt"] = pr["alt"]
            photo = f"{safe(p['no'])}_iso.png"
            if p["no"] and (src / "parts" / photo).exists():
                p["img"] = photo
                all_photos.add(photo)
            else:
                p["img"] = ""
        options.append({
            "no": no,
            "name": d.get("optionName") or no,
            "systems": sys_of_option.get(no, ["UNCLASSIFIED"]),
            "remarks": (d.get("remarks") or "").strip(),
            "sheets": sheets,
            "parts": parts,
        })

    # ремкомплекты
    kits = []
    kf = src / "kitSets.json"
    if kf.exists():
        for k in json.loads(kf.read_text(encoding="utf-8")):
            kits.append({
                "no": k.get("kitNo"), "name": k.get("kitDesc"),
                "notes": k.get("kitNotes") or "", "type": k.get("kitType") or "",
                "parts": [{"no": p.get("partNo"), "name": p.get("partDesc")}
                          for p in (k.get("parts") or [])],
            })

    # дерево систем
    systems = []
    for code in sorted({s for o in options for s in o["systems"]}):
        systems.append({
            "code": code,
            "name": SYSTEM_RU.get(code, code.title()),
            "options": sorted([o["no"] for o in options if code in o["systems"]]),
        })

    # карточки деталей (атрибуты, замены номеров, где применяется, ракурсы)
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
        "hasPrices": bool(prices),
        "systems": systems,
        "options": options,
        "kits": kits,
        "cards": cards,
    }

    CAT.mkdir(exist_ok=True)
    (CAT / "data.js").write_text(
        "window.CATALOG = " + json.dumps(catalog, ensure_ascii=False, separators=(",", ":")) + ";",
        encoding="utf-8")

    # картинки
    for sub, names in (("drawings", all_sheets), ("parts", all_photos)):
        dst = CAT / sub
        dst.mkdir(exist_ok=True)
        for n in names:
            s = src / sub / n
            if s.exists() and not (dst / n).exists():
                shutil.copy2(s, dst / n)

    total_pos = sum(len(o["parts"]) for o in options)
    uniq = {p["no"] for o in options for p in o["parts"] if p["no"]}
    print(f">>> Каталог собран: {CAT}")
    print(f"    систем {len(systems)}, узлов {len(options)}, позиций {total_pos}, "
          f"уникальных деталей {len(uniq)}")
    print(f"    чертежей {len(all_sheets)}, фото деталей {len(all_photos)}, "
          f"ремкомплектов {len(kits)}")
    print(f"    карточек деталей {len(cards)}, из них с заменами номеров {n_sup}")
    print(f"    data.js: {(CAT / 'data.js').stat().st_size / 1024:.0f} КБ")

    # контроль полноты: ни один номер из состава двигателя не потерян
    from_engine = {p["partNo"] for o in (engine.get("optionList") or [])
                   for p in (o.get("parts") or []) if p.get("partNo")}
    lost = sorted(from_engine - uniq)
    print(f"    ПОТЕРЯНО НОМЕРОВ: {len(lost)}" + (f" -> {lost[:10]}" if lost else "  (ноль)"))
    return len(lost) == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Сборка веб-каталога Cummins")
    ap.add_argument("esn")
    ap.add_argument("--prices", help="прайс-лист .xlsx (необязательно)")
    a = ap.parse_args()
    sys.exit(0 if build(a.esn, a.prices) else 1)
