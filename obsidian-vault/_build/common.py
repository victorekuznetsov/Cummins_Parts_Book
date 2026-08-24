#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Общие константы и утилиты сборки базы знаний."""
import json
import os
import re
import unicodedata

SRC = os.environ.get("KB_SRC", "/home/user/Cummins_Parts_Book")
NHL = {
    "NTE200": os.environ.get("KB_NTE200", "/home/user/NHL_Parts_Book-NTE200"),
    "NTE240": os.environ.get("KB_NTE240", "/home/user/NHL_Parts_Book-NTE240"),
    "TR100A": os.environ.get("KB_TR100", "/home/user/NHL_Parts_Book-TR100"),
}
VAULT = os.environ.get("KB_VAULT", "/home/user/kb_vault")
BUILD = os.path.join(SRC, "kb_build")

# ссылка на исходные PDF в репозитории (ветка с полной выгрузкой)
PDF_BASE = ("https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/"
            "claude/cummins-parts-knowledge-base-qa0n50/bulletins/")

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
    "33239899": ("K38/K50 · QSK38, QSK50, QSK60", ["33239899", "33239746"]),
    "37292556": ("QST30", ["37292556", "37295879"]),
    "41353297": ("QSK19", ["41349633"]),
    "41370103": ("NT/NTA855 · ISM/QSM11", ["41343322"]),
    "93087701": ("C8.3 · 6C8.3", ["93058669"]),
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


def ru(dic, key, default=""):
    """Русский перевод из словаря (если словарь уже собран)."""
    v = dic.get(key)
    return v if v else default
