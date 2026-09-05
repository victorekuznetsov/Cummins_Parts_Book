#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Реестр парка Cummins «Полюс Алдан»: что стоит, где и в каком количестве.

CPL и каталог по этим двигателям ещё не определены — для этого нужен запрос
к parts.cummins.com по каждому серийному номеру (см. FLEET-TODO в заметке).
"""
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import SRC, frontmatter, write_note

# списки парка лежат в корне репозитория (fleet/), а не рядом с хранилищем
FLEET = os.path.join(SRC, "fleet")
FOLDER = "11 Машины/Парк"


def read_tsv(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        head = f.readline().rstrip("\n").split("\t")
        for line in f:
            if line.strip():
                rows.append(dict(zip(head, line.rstrip("\n").split("\t"))))
    return rows


def main():
    have = read_tsv(os.path.join(FLEET, "polyus.tsv"))
    none = read_tsv(os.path.join(FLEET, "polyus_no_esn.tsv"))
    by_model = collections.Counter(r["model_doc"] for r in have + none)
    by_place = collections.Counter(r["place"] for r in have + none)

    out = [
        frontmatter({
            "type": "Парк",
            "aliases": ["Полюс Алдан", "Парк Полюс"],
            "двигателей": len(have) + len(none),
            "с серийным номером": len(have),
            "tags": ["парк"],
        }), "",
        "# Парк Cummins · АО «Полюс Алдан»",
        "",
        "> [!abstract] Что в парке",
        f"> **{len(have) + len(none)}** двигателей Cummins · "
        f"**{len(by_model)}** моделей · **{len(by_place)}** участков.",
        f"> С пригодным серийным номером — **{len(have)}**, без номера "
        f"(«Н/Д», «#») — **{len(none)}**.",
        "",
        "> [!warning] Каталоги и документация по этому парку ещё не выгружены",
        "> Каталог определяется CPL, а CPL узнаётся по серийному номеру через "
        "parts.cummins.com. Ни один из этих двигателей не совпал с уже "
        "выгруженными каталогами — парк новый.",
        "> Порядок работы — в заметке [[Что выгрузить дальше]].",
        "",
        "См. также [[Парк машин]] — парк, по которому каталоги уже собраны.",
        "",
        "## По моделям двигателя",
        "",
        "| Модель | Двигателей | С серийным номером |",
        "|---|---:|---:|",
    ]
    have_by_model = collections.Counter(r["model_doc"] for r in have)
    for m, n in by_model.most_common():
        out.append(f"| {m or '—'} | {n} | {have_by_model.get(m, 0)} |")

    out += ["", "## По участкам", "", "| Участок | Двигателей |", "|---|---:|"]
    for p, n in by_place.most_common():
        out.append(f"| {p or '—'} | {n} |")

    out += ["", "## Двигатели с серийным номером", "",
            "| Серийный номер | Модель | Участок | Год |", "|---|---|---|---|"]
    for r in sorted(have, key=lambda x: (x["model_doc"], x["esn"])):
        out.append(f"| `{r['esn']}` | {r['model_doc']} | {r['place']} | {r['year']} |")

    if none:
        out += ["", "## Без серийного номера", "",
                "> [!missing] Каталог по ним не собрать",
                "> В учётной выгрузке в поле серийного номера стоит «Н/Д» или «#». "
                "Номер нужно взять с таблички двигателя.", "",
                "| Модель | Участок | Год |", "|---|---|---|"]
        for r in sorted(none, key=lambda x: (x["model_doc"], x["place"])):
            out.append(f"| {r['model_doc']} | {r['place']} | {r['year']} |")

    write_note(f"{FOLDER}/Парк Полюс Алдан.md", "\n".join(out))
    print(f"реестр записан: {len(have) + len(none)} двигателей, "
          f"{len(by_model)} моделей")


if __name__ == "__main__":
    main()
