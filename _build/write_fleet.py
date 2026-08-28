#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Заметки парка: сводка, группы по CPL и связь с каталогом и документами."""
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import BUILD, DIRS, frontmatter, load_json, safe_name, write_note

FOLDER = "11 Машины/Парк"


def eng_note(cat_state, esn):
    e = cat_state.get("engines", {}).get(esn)
    return safe_name(f"{esn} — {e['model']} CPL {e['cpl']}") if e else ""


def main():
    fleet = load_json(os.path.join(BUILD, "state_fleet.json"), {})
    if not fleet:
        print("нет state_fleet.json — сначала build_fleet.py")
        return
    cat_state = load_json(os.path.join(BUILD, "state_catalog.json"), {})
    machines = fleet["machines"]
    groups = {g["cpl"]: g for g in fleet["groups"]}
    by_cpl = collections.defaultdict(list)
    for m in machines:
        by_cpl[m["cpl"]].append(m)

    group_note = {c: safe_name(f"CPL {c} — {g['model']}") for c, g in groups.items()}

    # ------------------------------------------------------------- сводка
    ok = [m for m in machines if m["ok"]]
    head = [
        frontmatter({
            "type": "Парк",
            "aliases": ["Парк машин", "Fleet"],
            "машин": len(machines),
            "групп": len(groups),
            "tags": ["парк"],
        }), "",
        "# Парк машин",
        "",
        "> [!abstract] Что здесь",
        f"> **{len(machines)}** машин · **{len(groups)}** групп по CPL · "
        f"**{len(machines) - len(ok)}** двигателей каталог Cummins не знает.",
        "> Каталог запчастей определяется **CPL**, а не серийным номером: на "
        "каждый CPL нужен один каталог, остальные машины группы им покрываются.",
        "",
        "## Группы по CPL",
        "",
        "| CPL | Двигатель | Машины | Машин | Каталог | Документов |",
        "|---|---|---|---:|---|---:|",
    ]
    for cpl, g in sorted(groups.items(), key=lambda kv: -kv[1]["n"]):
        cat = eng_note(cat_state, g["cat_esn"])
        cat_cell = "[[" + cat + "\\|" + g["cat_esn"] + "]]" if cat else "—"
        docs_cell = str(g["docs"]) if g["docs"] else "**нет**"
        kinds = ", ".join(g["kinds"])
        head.append(f"| [[{group_note[cpl]}\\|{cpl}]] | {g['model']} | "
                    f"{kinds} | {g['n']} | {cat_cell} | {docs_cell} |")

    head += ["", "## Все машины", "",
             "| Машина | VIN | ESN | CPL | Двигатель | Сборка |",
             "|---|---|---|---|---|---|"]
    for m in sorted(machines, key=lambda x: (x["machine"], x["esn"])):
        cpl = ("[[" + group_note[m["cpl"]] + "\\|" + m["cpl"] + "]]"
               if m["cpl"] else "—")
        head.append(f"| {m['machine']} | `{m['vin']}` | `{m['esn']}` | {cpl} | "
                    f"{m['model'] or '—'} | {m['build'] or ''} |")

    bad = [m for m in machines if not m["ok"]]
    if bad:
        head += ["", "## Нет в каталоге Cummins", "",
                 "> [!warning] Каталог по этим номерам не собрать",
                 "> parts.cummins.com не находит эти серийные номера — двигатель "
                 "другой марки либо номер не тот.", "",
                 "| Машина | VIN | ESN |", "|---|---|---|"]
        for m in sorted(bad, key=lambda x: (x["machine"], x["esn"])):
            head.append(f"| {m['machine']} | `{m['vin']}` | `{m['esn']}` |")

    write_note(f"{FOLDER}/Парк машин.md", "\n".join(head))

    # ------------------------------------------------------- группы по CPL
    n = 0
    for cpl, g in groups.items():
        cat = eng_note(cat_state, g["cat_esn"])
        out = [
            frontmatter({
                "type": "Группа CPL",
                "aliases": [f"CPL {cpl}", g["model"]],
                "cpl": cpl,
                "модель": g["model"],
                "каталог": g["cat_esn"],
                "машин": g["n"],
                "документов": g["docs"],
                "tags": ["парк/cpl"],
            }), "",
            f"# CPL {cpl} · {g['model']}",
            f"**{', '.join(g['kinds'])}** · машин в парке: {g['n']}",
            "",
            "> [!abstract] Чем покрывается группа",
            "> Каталог запчастей — по двигателю "
            + (("[[" + cat + "\\|" + g["cat_esn"] + "]]") if cat else "—") + ".",
        ]
        out.append("> Документация QuickServe: "
                   + (f"{g['docs']} документов семейства {g['family'] or g['model']}."
                      if g["docs"] else "**не выгружена**."))
        out += ["", "Входит в [[Парк машин]].", ""]
        if len(g["configs"]) > 1:
            out += ["> [!warning] Несколько конфигураций",
                    f"> В группе {len(g['configs'])} конфигурации "
                    f"({', '.join(g['configs'])}) — состав по редким позициям "
                    "может отличаться.", ""]
        out += ["## Машины группы", "",
                "| Машина | VIN | ESN | Конфигурация | Сборка | Позиций |",
                "|---|---|---|---|---|---:|"]
        for m in sorted(by_cpl[cpl], key=lambda x: x["build"] or ""):
            mark = " **←каталог**" if m["esn"] == g["cat_esn"] else ""
            out.append(f"| {m['machine']} | `{m['vin']}` | `{m['esn']}`{mark} | "
                       f"{m['config']} | {m['build']} | {m['parts'] or ''} |")
        write_note(f"{FOLDER}/{group_note[cpl]}.md", "\n".join(out))
        n += 1

    print(f"заметок парка записано: {n + 1}")


if __name__ == "__main__":
    main()
