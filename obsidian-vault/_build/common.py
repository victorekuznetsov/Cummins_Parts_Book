#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Общие константы и утилиты сборки базы знаний."""
import json
import os
import re
import unicodedata

SRC = os.environ.get("KB_SRC", "/home/user/Cummins_Parts_Book")
# Каталоги самих машин (NTE200, NTE240, TR100A) живут в отдельном репозитории
# NHL_Parts_Book: здесь только двигатели Cummins и документация к ним.
VAULT = os.environ.get("KB_VAULT", os.path.join(SRC, "obsidian-vault"))
BUILD = os.path.join(SRC, "kb_build")

# ссылка на исходные PDF в репозитории (ветка с полной выгрузкой)
PDF_BASE = ("https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/"
            "main/bulletins/")

DIRS = {
    "docs": "20 Документы",
    "proc": "20 Документы/Процедуры",
    "tsb": "20 Документы/TSB",
    "bulletin": "20 Документы/Сервисные бюллетени",
    "sti": "20 Документы/Инструмент STI",
    "install": "20 Документы/Инструкции по установке",
    "outline": "20 Документы/Габаритные чертежи",
    "manual": "20 Документы/Руководства",
    "engine": "10 Двигатели",
    "machine": "11 Машины",
    "part": "30 Детали",
    "option": "40 Узлы",
    "kit": "50 Комплекты",
    "topic": "60 Темы",
    "index": "01 Индексы",
    "fig": "90 Приложения/Иллюстрации",
    "draw": "90 Приложения/Чертежи",
    "media": "90 Приложения/Медиа машин",
    "photo": "90 Приложения/Фото деталей",
    "manpdf": "90 Приложения/Руководства машин",
}

CAT_RU = {
    "procedures": "Процедура",
    "tsb": "TSB",
    "bulletin": "Сервисный бюллетень",
    "sti": "Инструкция по инструменту",
    "install_inst": "Инструкция по установке",
    "outlines": "Габаритный чертёж",
    "manual": "Руководство",
}
CAT_DIR = {
    "procedures": DIRS["proc"],
    "tsb": DIRS["tsb"],
    "bulletin": DIRS["bulletin"],
    "sti": DIRS["sti"],
    "install_inst": DIRS["install"],
    "outlines": DIRS["outline"],
    "manual": DIRS["manual"],
}
CAT_TAG = {
    "procedures": "документ/процедура",
    "tsb": "документ/tsb",
    "bulletin": "документ/бюллетень",
    "sti": "документ/инструмент",
    "install_inst": "документ/установка",
    "outlines": "документ/чертёж",
    "manual": "документ/руководство",
}

# ESN документации -> семейство двигателей -> ESN каталогов
DOC_ESN = {
    "33239899": ("K38/K50 · QSK38, QSK50", ["33239899"]),
    # 33239746 (NTE240, QSK60 CM2150 MCRS) раньше ошибочно делил документацию
    # с 33239899 (NTE200, QSK50 CM2150 MCRS) — другой двигатель. Своя выгрузка
    # QuickServe довыгружена (qs_raw.py, см. quickserve/) и слита в bulletins/.
    "33239746": ("QSK60 CM2150 MCRS", ["33239746"]),
    "37292556": ("QST30", ["37292556", "37295879"]),
    "41353297": ("QSK19", ["41349633", "41353297"]),
    "41370103": ("NT/NTA855 · ISM/QSM11", ["41343322", "41370103"]),
    "93087701": ("C8.3 · 6C8.3", ["93058669", "93087701"]),

    # Документация парка «Полюс»: выгружалась по каждому двигателю отдельно,
    # поэтому doc-ESN совпадает с ESN каталога.
    "33210083": ("QSK60", ["33210083"]),
    "33219033": ("QSK60", ["33219033"]),
    "33224343": ("QSK60", ["33224343"]),
    "33224404": ("QSK50", ["33224404"]),
    "35354607": ("QSM11", ["35354607"]),
    "35373113": ("QSM11", ["35373113"]),
    "37269910": ("K19", ["37269910"]),
    "37280605": ("K19", ["37280605"]),
    "41340468": ("QSK50", ["41340468"]),
    "71156161": ("QSM11", ["71156161"]),
    "77804793": ("A8.5", ["77804793"]),
    "77804810": ("15N", ["77804810"]),
    "80141463": ("QSX15", ["80141463"]),
    "80248213": ("QSX15", ["80248213"]),
    "82099327": ("QSB6.7", ["82099327"]),
    "85017333": ("QSK23", ["85017333"]),
    "93047320": ("6B5.9", ["93047320"]),
    "93948840": ("QSZ13", ["93948840"]),
}
FAMILY_OF_CAT = {}
for _doc_esn, (_fam, _cats) in DOC_ESN.items():
    for _c in _cats:
        FAMILY_OF_CAT[_c] = (_fam, _doc_esn)

MONTHS = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}

BAD_CHARS = re.compile(r'[\\/:*?"<>|#\^\[\]]')


def iso_date(s):
    """'12-Mar-2013' -> '2013-03-12'"""
    if not s:
        return ""
    m = re.match(r"(\d{1,2})-([A-Za-z]{3})-(\d{4})", s.strip())
    if not m:
        return ""
    mm = MONTHS.get(m.group(2).lower())
    if not mm:
        return ""
    return f"{m.group(3)}-{mm:02d}-{int(m.group(1)):02d}"


def safe_name(s, limit=80):
    """Имя файла, безопасное для Windows/macOS/Linux и Obsidian."""
    s = unicodedata.normalize("NFC", s or "")
    s = BAD_CHARS.sub(" ", s)
    s = s.replace("·", "-").replace(" ", " ")
    s = re.sub(r"\s+", " ", s).strip(" .")
    if len(s) > limit:
        s = s[:limit].rstrip(" ,-.;")
    return s or "без названия"


def yaml_str(s):
    s = (s or "").replace('"', "'").replace("\n", " ")
    return '"%s"' % s


def frontmatter(fields):
    out = ["---"]
    for k, v in fields.items():
        if v is None or v == "" or v == [] or v == {}:
            continue
        if isinstance(v, list):
            out.append(f"{k}:")
            for x in v:
                out.append(f"  - {yaml_str(str(x))}")
        elif isinstance(v, (int, float)):
            out.append(f"{k}: {v}")
        else:
            out.append(f"{k}: {yaml_str(str(v))}")
    out.append("---")
    return "\n".join(out)


def write_note(relpath, text):
    path = os.path.join(VAULT, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text.rstrip() + "\n")
    return path


def load_json(path, default=None):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return default if default is not None else {}


def save_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)


def catalogs():
    """Разбор data/<ESN>.js -> список каталогов двигателей."""
    import glob
    out = []
    for f in sorted(glob.glob(os.path.join(SRC, "data", "*.js"))):
        s = open(f, encoding="utf-8").read()
        m = re.search(r'window\.CATALOGS\["\d+"\]\s*=\s*', s)
        if not m:
            continue
        out.append(json.loads(s[m.end():].rstrip().rstrip(";")))
    return out


def engine_registry():
    """engines.js -> {ESN: запись}. Там же машина, владелец и участок парка."""
    f = os.path.join(SRC, "engines.js")
    if not os.path.exists(f):
        return {}
    src = open(f, encoding="utf-8").read()
    m = re.search(r"window\.ENGINES\s*=\s*(\[.*\]);", src, re.S)
    return {e["esn"]: e for e in json.loads(m.group(1))} if m else {}


def ru(dic, key, default=""):
    """Русский перевод из словаря (если словарь уже собран)."""
    v = dic.get(key)
    return v if v else default
