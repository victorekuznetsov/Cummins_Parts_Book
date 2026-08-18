#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Запись заметок машин NHL: обзор машины, разделы каталога с составом,
инструкции по ремонту, оглавления PDF-руководств."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import BUILD, DIRS, frontmatter, load_json, safe_name, write_note

CACHE = os.path.join(BUILD, "_cache", "machines")

MACHINE_INFO = {
    "NTE200": {"engine": "33239899", "desc": "Карьерный самосвал NHL NTE200, "
                                             "электромеханическая трансмиссия GE, двигатель Cummins QSK50"},
    "NTE240": {"engine": "33239746", "desc": "Карьерный самосвал NHL NTE240, "
                                             "двигатель Cummins QSK60"},
    "TR100A": {"engine": "37295879", "desc": "Карьерный самосвал NHL TR100A, "
                                             "двигатель Cummins QST30 CM552"},
}


def part_link(pn, parts_db):
    pn = (pn or "").strip()
    if not pn:
        return ""
    return f"[[{pn}]]" if pn in parts_db else pn


def sec_title(sec):
    t = " · ".join(x for x in [sec.get("en", ""), sec.get("zh", "")] if x)
    return t or sec.get("code", "")


def write_sections(machine, sections, parts_db, folder, kind="Раздел каталога"):
    notes = []
    for sec in sections:
        code = sec.get("code", "")
        title = sec_title(sec)
        note = safe_name(f"{machine} {code} — {title}", 90)
        fm = {
            "type": kind,
            "machine": machine,
            "code": code,
            "title": title,
            "chapter": sec.get("chapter", ""),
            "tags": [f"машина/{machine}", "каталог-машины"],
        }
        out = [frontmatter(fm), "", f"# {code} — {title}", "",
               f"> [!abstract] {kind} · машина [[{machine}]]"
               + (f" · глава `{sec.get('chapter','')}`" if sec.get("chapter") else ""), ""]
        total = 0
        for i, fig in enumerate(sec.get("figures", []), 1):
            if len(sec.get("figures", [])) > 1:
                out.append(f"## Рисунок {i}")
                out.append("")
            for img in fig.get("images", []):
                base = os.path.splitext(os.path.basename(img))[0]
                ext = ".png" if "/drawings/" in img or img.startswith("drawings/") else ".jpg"
                out.append(f"![[{machine}_{base}{ext}]]")
            out.append("")
            rows = fig.get("parts", [])
            if rows:
                out.append("| № | Артикул | Наименование | 中文 | Кол-во |")
                out.append("|---|---|---|---|---|")
                for p in rows:
                    total += 1
                    out.append(f"| {p.get('ref','')} | {part_link(p.get('pn',''), parts_db)} | "
                               f"{p.get('en','')} | {p.get('zh','')} | {p.get('qty','')} |")
                out.append("")
        write_note(f"{folder}/{note}.md", "\n".join(out))
        notes.append((code, title, note, total))
    return notes


def main():
    machines = load_json(os.path.join(BUILD, "state_machines.json"), {})
    cat = load_json(os.path.join(BUILD, "state_catalog.json"), {})
    parts_db = cat.get("parts", {})
    engines = cat.get("engines", {})
    eng_note = {esn: safe_name(f"{esn} — {e['model']} CPL {e['cpl']}")
                for esn, e in engines.items()}

    for machine, m in machines.items():
        base_dir = f"{DIRS['machine']}/{machine}"
        secs = write_sections(machine, m.get("sections", []), parts_db,
                              f"{base_dir}/Разделы каталога")
        eng_secs = write_sections(machine, m.get("engine_sections", []), parts_db,
                                  f"{base_dir}/Двигатель (книга машины)",
                                  kind="Раздел каталога двигателя")

        # инструкции по ремонту
        svc_notes = []
        for s in m.get("service", []):
            body = ""
            cache = os.path.join(CACHE, s["cache"])
            if os.path.exists(cache):
                body = open(cache, encoding="utf-8").read()
            body = re.sub(r"!\[\[([^\]]+)\]\]", lambda mo: f"![[{machine}_{mo.group(1)}]]", body)
            note = safe_name(f"{machine} ремонт {s['code']} — {s['title']}", 90)
            fm = {
                "type": "Инструкция по ремонту",
                "machine": machine,
                "code": s["code"],
                "title": s["title"],
                "tags": [f"машина/{machine}", "ремонт-машины"],
            }
            out = [frontmatter(fm), "", f"# {s['code']} — {s['title']}", "",
                   f"> [!abstract] Инструкция по ремонту и обслуживанию · машина [[{machine}]]",
                   "", body]
            write_note(f"{base_dir}/Ремонт и обслуживание/{note}.md", "\n".join(out))
            svc_notes.append((s["code"], s["title"], note))

        # карточка машины
        info = MACHINE_INFO.get(machine, {})
        esn = info.get("engine", "")
        fm = {
            "type": "Машина",
            "machine": machine,
            "title_en": m.get("title_en", ""),
            "maker": m.get("maker", ""),
            "engine_esn": esn,
            "sections": len(secs),
            "service_docs": len(svc_notes),
            "prices": m.get("prices", 0),
            "tags": [f"машина/{machine}", "машина"],
        }
        out = [frontmatter(fm), "", f"# {machine}", "",
               f"> [!abstract] {info.get('desc','')}",
               f"> **Изготовитель:** {m.get('maker','')}",
               f"> **Каталог:** {m.get('title_en','')}"]
        if esn and esn in eng_note:
            out.append(f"> **Двигатель:** [[{eng_note[esn]}|{esn}]]")
        out.append(f"> **Разделов каталога:** {len(secs)} · "
                   f"**Инструкций по ремонту:** {len(svc_notes)} · "
                   f"**Позиций с ценой:** {m.get('prices',0)}")
        out.append("")

        # PDF-руководства
        if m.get("manuals"):
            out.append("## Руководства (PDF)")
            out.append("")
            for f in m["manuals"]:
                fn = f"{machine}_{os.path.basename(f['file'])}"
                out.append(f"- [[{fn}|{f['title']}]] — {f.get('desc','')} "
                           f"({f.get('pages','?')} с.)")
            out.append("")
            if m.get("repair_toc"):
                out.append("### Оглавление руководства по ремонту")
                out.append("")
                out.append("| Раздел | Название | Стр. |")
                out.append("|---|---|---|")
                pdfname = f"{machine}_repair.pdf"
                for t in m["repair_toc"]:
                    out.append(f"| {t['code']} | [[{pdfname}#page={t['page']}\\|{t['title']}]] "
                               f"| {t['page']} |")
                out.append("")

        if svc_notes:
            out.append("## Ремонт и обслуживание")
            out.append("")
            for code, title, note in svc_notes:
                out.append(f"- [[{note}|{code} — {title}]]")
            out.append("")

        # разделы каталога по главам
        chapters = {c["code"]: c for c in m.get("chapters", [])}
        out.append("## Каталог запчастей по главам")
        out.append("")
        by_chapter = {}
        for sec in m.get("sections", []):
            by_chapter.setdefault(sec.get("chapter", ""), []).append(sec)
        for ch, items in sorted(by_chapter.items()):
            c = chapters.get(ch, {})
            head = " · ".join(x for x in [c.get("en", ""), c.get("zh", "")] if x)
            out.append(f"### {ch} {head}")
            out.append("")
            for sec in items:
                note = safe_name(f"{machine} {sec.get('code','')} — {sec_title(sec)}", 90)
                out.append(f"- [[{note}|{sec.get('code','')} — {sec_title(sec)}]]")
            out.append("")

        if eng_secs:
            out.append("## Двигатель в книге машины")
            out.append("")
            for code, title, note, _ in eng_secs:
                out.append(f"- [[{note}|{code} — {title}]]")
            out.append("")

        write_note(f"{DIRS['machine']}/{machine}.md", "\n".join(out))
        print(f"{machine}: разделов {len(secs)}, двигательных {len(eng_secs)}, "
              f"ремонт {len(svc_notes)}")


if __name__ == "__main__":
    main()
