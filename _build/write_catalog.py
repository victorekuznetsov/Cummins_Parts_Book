#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Запись заметок каталога: двигатели, узлы (опции), комплекты, детали."""
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import (engine_registry, BUILD, DIRS, DOC_ESN, FAMILY_OF_CAT, VAULT, frontmatter,
                    load_json, safe_name, write_note)




def ru_name(ru_parts, name):
    if not name:
        return ""
    return ru_parts.get(name.upper()) or ru_parts.get(name) or ""


def main():
    cat = load_json(os.path.join(BUILD, "state_catalog.json"), {})
    docs_state = load_json(os.path.join(BUILD, "state_docs.json"), {})
    links = load_json(os.path.join(BUILD, "state_links.json"), {})
    ru_parts = load_json(os.path.join(BUILD, "ru_parts.json"), {})
    docs = docs_state.get("docs", {})

    engines = cat.get("engines", {})
    options = cat.get("options", {})
    kits = cat.get("kits", {})
    parts = cat.get("parts", {})
    part_docs = links.get("part_docs", {})
    by_engine = links.get("by_engine", {})

    eng_note = {esn: safe_name(f"{esn} — {e['model']} CPL {e['cpl']}")
                for esn, e in engines.items()}
    opt_note = {k: safe_name(f"{v['esn']} {v['no']} — {v['name']}", 90)
                for k, v in options.items()}
    kit_note = {k: safe_name(f"Комплект {v['no']} — {v['name']}", 90)
                for k, v in kits.items()}

    photos_dir = os.path.join(VAULT, DIRS["photo"])
    local_photos = set(os.listdir(photos_dir)) if os.path.isdir(photos_dir) else set()

    draw_dir = os.path.join(VAULT, DIRS["draw"])
    local_sheets = set()
    if os.path.isdir(draw_dir):
        for sub in os.listdir(draw_dir):
            p = os.path.join(draw_dir, sub)
            if os.path.isdir(p):
                local_sheets |= set(os.listdir(p))

    # ---------------------------------------------------------------- детали
    for no, p in parts.items():
        name_en = p.get("name", "")
        name_ru = ru_name(ru_parts, name_en)
        card = p.get("card") or {}
        attrs = card.get("attrs") or {}
        systems = sorted({s["name"] for o in p["options"]
                          for s in options.get(f"{o['esn']}|{o['opt']}", {}).get("systems", [])})
        tags = ["деталь"]
        for esn in p["engines"]:
            fam = DOC_ESN.get(esn, ("", ""))[0] if esn in DOC_ESN else ""
            if fam:
                tags.append("двигатель/" + fam.split(" · ")[0].replace(" ", ""))
        for s in systems:
            tags.append("система/" + s.lower().replace(" ", "-"))
        if p.get("price"):
            tags.append("есть-цена")

        sup = card.get("sup") or []
        fm = {
            "aliases": [x for x in [name_ru, name_en] if x],
            "type": "Деталь",
            "part": no,
            "name_en": name_en,
            "name_ru": name_ru,
            "weight": card.get("wt", ""),
            "dims_mm": card.get("dim", ""),
            "engines": p["engines"],
            "options": sorted({o["opt"] for o in p["options"]}),
            "kits": sorted({k["kit"] for k in p["kits"]}),
            "supersedes": [s["no"] for s in sup],
            "docs": len(part_docs.get(no, [])) or None,
            "tags": sorted(set(tags)),
        }
        out = [frontmatter(fm), "", f"# {no} — {name_ru or name_en}"]
        if name_ru and name_en:
            out.append(f"*{name_en}*")
        out.append("")

        # фото
        shown = 0
        for url in p.get("photos", []):
            fn = url.rsplit("/", 1)[-1]
            local = os.path.splitext(fn)[0] + ".jpg"
            if local in local_photos:
                out.append(f"![[{local}|280]]")
                shown += 1
            elif shown == 0:
                out.append(f"![Фото {no}]({url})")
                shown += 1
        out.append("")

        info = ["> [!abstract] Карточка детали"]
        if card.get("wt"):
            info.append(f"> **Масса, кг (данные каталога):** {card['wt']}")
        if card.get("dim"):
            info.append(f"> **Габариты, мм:** {card['dim']}")
        for k in ("Service Part Topic", "Sellable", "Hazardous Material", "Dimensions"):
            if attrs.get(k):
                info.append(f"> **{k}:** {attrs[k]}")
        if p.get("alt_names"):
            info.append("> **Другие наименования:** " + "; ".join(p["alt_names"][:4]))
        out.append("\n".join(info))
        out.append("")

        if p.get("price"):
            out.append("## Цена")
            out.append("")
            out.append("| Прайс «Горная Евразия» | Цена |")
            out.append("|---|---|")
            if p["price"].get("cur") is not None:
                out.append(f"| текущая | {p['price']['cur']} |")
            if p["price"].get("new") is not None:
                out.append(f"| несогласованная | {p['price']['new']} |")
            out.append("")

        if p["options"]:
            out.append("## Где применяется (узлы двигателей)")
            out.append("")
            out.append("| Двигатель | Узел | Поз. | Кол-во | Размер / примечание |")
            out.append("|---|---|---|---|---|")
            for o in sorted(p["options"], key=lambda x: (x["esn"], x["opt"])):
                onote = opt_note.get(f"{o['esn']}|{o['opt']}")
                link = f"[[{onote}\\|{o['opt']} {o['opt_name']}]]" if onote else o["opt"]
                enote = eng_note.get(o["esn"], o["esn"])
                extra = " ".join(x for x in [o.get("dim", ""), o.get("rem", "")] if x)
                out.append(f"| [[{enote}\\|{o['esn']}]] | {link} | {o.get('pos','')} | "
                           f"{o.get('qty','')} | {extra} |")
            out.append("")

        if p["kits"]:
            out.append("## Входит в комплекты")
            out.append("")
            for k in sorted(p["kits"], key=lambda x: x["kit"]):
                knote = kit_note.get(f"{k['esn']}|{k['kit']}")
                out.append(f"- [[{knote}|{k['kit']} — {k['kit_name']}]] "
                           f"({eng_note.get(k['esn'], k['esn'])})")
            out.append("")

        if sup:
            out.append("## Цепочка замен номера")
            out.append("")
            out.append("| Номер | Статус | Продаётся |")
            out.append("|---|---|---|")
            for s in sorted(sup, key=lambda x: x.get("seq", 0)):
                other = f"[[{s['no']}]]" if s["no"] in parts and s["no"] != no else s["no"]
                out.append(f"| {other} | {s.get('st','')} | "
                           f"{'да' if s.get('sell') else 'нет'} |")
            out.append("")

        if part_docs.get(no):
            out.append("## Упоминается в документах")
            out.append("")
            for key in sorted(part_docs[no])[:60]:
                d = docs.get(key)
                if d:
                    out.append(f"- [[{d['note']}]] — {d['title']}")
            out.append("")

        used = card.get("used") or []
        if used:
            out.append("> [!note]- Где применяется по данным Cummins "
                       f"({len(used)} позиций каталога)")
            groups = collections.Counter(u.get("n", "") or "—" for u in used)
            out.append("> " + "; ".join(f"{n} ({c})" for n, c in groups.most_common(25)))
            out.append("")

        shard = no[0] if no[:1].isdigit() else "буквенные"
        write_note(f"{DIRS['part']}/{shard}/{no}.md", "\n".join(out))

    # ------------------------------------------------------------------ узлы
    for key, o in options.items():
        esn, name_en = o["esn"], o["name"]
        name_ru = ru_name(ru_parts, name_en)
        fm = {
            "aliases": [x for x in [name_ru] if x],
            "type": "Узел",
            "option": o["no"],
            "engine": esn,
            "name_en": name_en,
            "name_ru": name_ru,
            "systems": [s["name"] for s in o["systems"]],
            "parts_count": len(o["parts"]),
            "tags": ["узел"] + ["система/" + s["name"].lower().replace(" ", "-")
                                for s in o["systems"]],
        }
        out = [frontmatter(fm), "",
               f"# {o['no']} — {name_ru or name_en}"]
        if name_ru and name_en:
            out.append(f"*{name_en}*")
        out.append("")
        out.append(f"> [!abstract] Узел каталога · двигатель [[{eng_note.get(esn, esn)}|{esn}]]")
        if o["systems"]:
            out.append("> **Системы:** " + ", ".join(
                f"{s['name']} ({s['code']})" for s in o["systems"]))
        out.append("")
        for sheet in o["sheets"]:
            if sheet in local_sheets:
                out.append(f"![[{sheet}]]")
        out.append("")
        if o["parts"]:
            out.append("## Состав")
            out.append("")
            out.append("| Поз. | Артикул | Наименование | Русское название | Кол-во | Размер |")
            out.append("|---|---|---|---|---|---|")
            for p in o["parts"]:
                if not p.get("no"):
                    continue
                nm = p.get("name") or ""
                out.append(f"| {p.get('pos','')} | [[{p['no']}]] | {nm} | "
                           f"{ru_name(ru_parts, nm)} | {p.get('qty','')} | {p.get('dim','')} |")
            out.append("")
        if o["remarks"]:
            out.append("## Характеристики узла")
            out.append("")
            for r in o["remarks"]:
                out.append(f"- {r}")
            out.append("")
        write_note(f"{DIRS['option']}/{esn}/{opt_note[key]}.md", "\n".join(out))

    # ------------------------------------------------------------ комплекты
    for key, k in kits.items():
        name_ru = ru_name(ru_parts, k["name"])
        fm = {
            "aliases": [x for x in [name_ru] if x],
            "type": "Комплект",
            "kit": k["no"],
            "engine": k["esn"],
            "name_en": k["name"],
            "name_ru": name_ru,
            "kit_type": k.get("type", ""),
            "parts_count": len(k["parts"]),
            "tags": ["комплект"],
        }
        out = [frontmatter(fm), "", f"# Комплект {k['no']} — {name_ru or k['name']}"]
        if name_ru:
            out.append(f"*{k['name']}*")
        out.append("")
        out.append(f"> [!abstract] Ремкомплект · двигатель "
                   f"[[{eng_note.get(k['esn'], k['esn'])}|{k['esn']}]]"
                   + (f" · тип {k['type']}" if k.get("type") else ""))
        if k.get("notes"):
            out.append(f"> {k['notes']}")
        out.append("")
        out.append("## Состав комплекта")
        out.append("")
        out.append("| Артикул | Наименование | Русское название |")
        out.append("|---|---|---|")
        for p in k["parts"]:
            if not p.get("no"):
                continue
            nm = p.get("name") or ""
            out.append(f"| [[{p['no']}]] | {nm} | {ru_name(ru_parts, nm)} |")
        write_note(f"{DIRS['kit']}/{k['esn']}/{kit_note[key]}.md", "\n".join(out))

    # ------------------------------------------------------------ двигатели
    reg = engine_registry()
    for esn, e in engines.items():
        fam, doc_esn = FAMILY_OF_CAT.get(esn, ("", ""))
        eng_docs = by_engine.get(doc_esn, []) if doc_esn else []
        cnt = collections.Counter(docs[k]["cat"] for k in eng_docs if k in docs)
        fm = {
            "type": "Двигатель",
            "esn": esn,
            "model": e["model"],
            "cpl": e["cpl"],
            "config": e.get("config", ""),
            "build_date": e.get("build", ""),
            "family": fam,
            "machine": reg.get(esn, {}).get("machine", ""),
            "options_count": len(e["options"]),
            "kits_count": len(e["kits"]),
            "parts_rows": e["parts_total"],
            "tags": ["двигатель"] + (["двигатель/" + fam.split(" · ")[0].replace(" ", "")]
                                     if fam else []),
        }
        out = [frontmatter(fm), "", f"# {esn} — {e['model']} (CPL {e['cpl']})", ""]
        info = ["> [!abstract] Паспорт двигателя",
                f"> **Модель:** {e['model']} · **CPL:** {e['cpl']} · "
                f"**Конфигурация:** {e.get('config','')}",
                f"> **Дата сборки:** {e.get('build','')} · **Завод:** {e.get('plant','')} · "
                f"**Группа:** {e.get('group','')}"]
        if fam:
            info.append(f"> **Семейство документации:** {fam}")
        info.append(f"> **Узлов:** {len(e['options'])} · **Комплектов:** {len(e['kits'])} · "
                    f"**Позиций в составе:** {e['parts_total']}")
        out.append("\n".join(info))
        out.append("")

        if eng_docs:
            out.append("## Документация этого семейства")
            out.append("")
            names = {"procedures": "процедур", "tsb": "TSB", "bulletin": "бюллетеней",
                     "sti": "инструкций по инструменту", "manual": "руководств",
                     "install_inst": "инструкций по установке", "outlines": "габаритных чертежей"}
            out.append(", ".join(f"{cnt[c]} {names.get(c, c)}" for c in cnt))
            out.append("")
            mans = [docs[k] for k in eng_docs if k in docs and docs[k]["cat"] == "manual"]
            if mans:
                out.append("### Руководства")
                out.append("")
                for m in sorted(mans, key=lambda x: x["title"]):
                    out.append(f"- [[{m['note']}|{m['title']}]]")
                out.append("")

        out.append("## Узлы по системам")
        out.append("")
        for s in e["systems"]:
            out.append(f"### {s['name']} · {s['code']}")
            out.append("")
            for ono in s["options"]:
                k = f"{esn}|{ono}"
                if k in options:
                    o = options[k]
                    ru = ru_name(ru_parts, o["name"])
                    out.append(f"- [[{opt_note[k]}|{ono}]] — {ru or o['name']}")
            out.append("")

        if e["kits"]:
            out.append("## Ремкомплекты")
            out.append("")
            for kno in e["kits"]:
                k = f"{esn}|{kno}"
                if k in kits:
                    ru = ru_name(ru_parts, kits[k]["name"])
                    out.append(f"- [[{kit_note[k]}|{kno}]] — {ru or kits[k]['name']}")
            out.append("")

        write_note(f"{DIRS['engine']}/{eng_note[esn]}.md", "\n".join(out))

    print(f"записано: деталей {len(parts)}, узлов {len(options)}, "
          f"комплектов {len(kits)}, двигателей {len(engines)}")


if __name__ == "__main__":
    main()
