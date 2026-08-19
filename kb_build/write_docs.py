#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Запись заметок документов: TSB, процедуры, бюллетени, STI, установка,
габаритные чертежи и руководства с полным оглавлением."""
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import (BUILD, CAT_DIR, CAT_RU, CAT_TAG, DIRS, DOC_ESN, PDF_BASE,
                    frontmatter, load_json, safe_name, save_json, write_note)

STATE = os.path.join(BUILD, "state_docs.json")
CACHE = os.path.join(BUILD, "_cache")
CACHE_RU = os.path.join(BUILD, "_cache_ru")


def engine_note_names(cat_state):
    out = {}
    for esn, e in cat_state.get("engines", {}).items():
        out[esn] = safe_name(f"{esn} — {e['model']} CPL {e['cpl']}")
    return out


# ------------------------------- номера документов в тексте -> wiki-ссылки
PROT = re.compile(r"\[\[[^\]]*\]\]|`[^`]*`|\]\([^)]*\)|https?://\S+")
REF_PROC = re.compile(r"\b(\d{2,3}-\d{3}-\d{3}(?:-[a-zA-Z]{2})?)\b")
REF_TSB = re.compile(r"\bTSB[\s\u00a0]?(\d{6})\b", re.I)
REF_MAN = re.compile(r"\b(\d{7})\b")


def make_linkifier(note_of):
    """note_of(вид, номер) -> имя заметки либо None."""

    def one(text):
        def proc(m):
            n = note_of("doc", m.group(1))
            return f"[[{n}\\|{m.group(1)}]]" if n else m.group(0)

        def tsb(m):
            n = note_of("doc", "tsb" + m.group(1))
            return f"[[{n}\\|{m.group(0)}]]" if n else m.group(0)

        def man(m):
            n = note_of("manual", m.group(1))
            return f"[[{n}\\|{m.group(1)}]]" if n else m.group(0)

        text = REF_TSB.sub(tsb, text)
        text = REF_PROC.sub(proc, text)
        return REF_MAN.sub(man, text)

    def run(md):
        """Подставляет ссылки только вне уже готовых ссылок и кода."""
        out = []
        pos = 0
        for m in PROT.finditer(md):
            out.append(one(md[pos:m.start()]))
            out.append(m.group(0))
            pos = m.end()
        out.append(one(md[pos:]))
        return "".join(out)

    return run


def en_fold(body):
    """Английский оригинал в свёрнутом callout.

    Иллюстрации не дублируем — они показаны в русском тексте выше; вложенные
    callout-ы разворачиваем в жирные подзаголовки, иначе Obsidian рисует
    callout внутри callout-а."""
    out = []
    for ln in body.split("\n"):
        s = ln.rstrip()
        if s.lstrip().startswith("!["):
            continue
        m = re.match(r"^>\s*\[!(\w+)\][+-]?\s*(.*)$", s.strip())
        if m:
            out.append("**" + (m.group(2).strip() or m.group(1).upper()) + "**")
            continue
        if s.lstrip().startswith(">"):
            s = re.sub(r"^\s*>\s?", "", s)
        out.append(s)
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out).strip())
    if not text:
        return ""
    quoted = "\n".join(("> " + l) if l.strip() else ">" for l in text.split("\n"))
    return "\n> [!quote]- Original (English) · английский оригинал\n" + quoted + "\n"


def doc_folder(cat, doc_id, meta):
    """Куда положить заметку документа."""
    if cat == "procedures":
        pref = doc_id.split("-")[0]
        pref = pref if re.match(r"^[0-9]{1,3}$", pref) else "прочие"
        return f"{DIRS['proc']}/{pref}"
    if cat == "tsb":
        year = meta.get("year") or (meta.get("released") or "")[:4]
        m = re.match(r"tsb(\d{2})", doc_id)
        if not year and m:
            yy = int(m.group(1))
            year = f"20{m.group(1)}" if yy < 80 else f"19{m.group(1)}"
        return f"{DIRS['tsb']}/{year or 'без года'}"
    return CAT_DIR.get(cat, DIRS["docs"])


def main():
    state = load_json(STATE, {})
    docs = state.get("docs", {})
    toc = state.get("manual_toc", {})
    cat_state = load_json(os.path.join(BUILD, "state_catalog.json"), {})
    ru_titles = load_json(os.path.join(BUILD, "ru_docs.json"), {})
    ru_parts = load_json(os.path.join(BUILD, "ru_parts.json"), {})
    parts_db = cat_state.get("parts", {})
    eng_names = engine_note_names(cat_state)

    # обратные связи
    by_engine = collections.defaultdict(list)
    part_docs = collections.defaultdict(list)
    for key, d in docs.items():
        for esn in d["engines"]:
            by_engine[esn].append(key)
        for p in d.get("parts", []):
            part_docs[p].append(key)

    manual_titles = {}
    for key, d in docs.items():
        if d["cat"] == "manual":
            manual_titles[d["id"].replace("-history", "")] = d

    # номер документа в тексте -> имя заметки, на которую ставим ссылку
    note_by_doc = {}
    note_by_man = {}
    for key, d in docs.items():
        if d["cat"] == "manual":
            note_by_man[d["id"].replace("-history", "")] = d["note"]
        else:
            note_by_doc[d["id"]] = d["note"]

    def note_of(kind, num):
        return note_by_man.get(num) if kind == "manual" else note_by_doc.get(num)

    linkify = make_linkifier(note_of)

    written = 0
    for key, d in sorted(docs.items()):
        cat, did, note = d["cat"], d["id"], d["note"]
        title_en = d["title"]
        title_ru = ru_titles.get(title_en, "")
        body = ""
        cache_file = os.path.join(CACHE, cat, did + ".md")
        if os.path.exists(cache_file):
            body = open(cache_file, encoding="utf-8").read().strip()
        body_ru = ""
        ru_file = os.path.join(CACHE_RU, cat, did + ".md")
        if cat != "manual" and os.path.exists(ru_file):
            body_ru = open(ru_file, encoding="utf-8").read().strip()

        families = sorted({DOC_ESN[e][0] for e in d["engines"] if e in DOC_ESN})
        cat_engines = sorted({c for e in d["engines"] if e in DOC_ESN
                              for c in DOC_ESN[e][1]})

        tags = [CAT_TAG.get(cat, "документ")]
        for fam in families:
            tags.append("двигатель/" + fam.split(" · ")[0].replace(" ", ""))
        if cat == "tsb":
            year = (d.get("released") or "")[:4]
            if year:
                tags.append("год/" + year)
        if cat == "procedures" and re.match(r"^[0-9]{1,3}-", did):
            tags.append("группа/" + did.split("-")[0])
        if body_ru:
            tags.append("перевод/машинный")
        if d.get("group"):
            tags.append("тема/" + re.sub(r"[^0-9A-Za-zА-Яа-я]+", "-",
                                         d["group"].split(" - ")[-1]).strip("-").lower())

        fm = {
            "aliases": [x for x in [title_ru] if x],
            "type": CAT_RU.get(cat, cat),
            "doc": did,
            "title_en": title_en,
            "title_ru": title_ru,
            "released": d.get("released", ""),
            "modified": d.get("modified", ""),
            "revision": d.get("revision", ""),
            "group": d.get("group", ""),
            "engines": cat_engines,
            "families": families,
            "manuals": d.get("manuals", []),
            "parts": d.get("parts", []),
            "figures": d.get("figures", 0) or None,
            "lang": "ru+en" if body_ru else "en",
            "translation": "машинный черновик" if body_ru else "",
            "source": d.get("url", ""),
            "pdf": PDF_BASE + d.get("pdf_rel", ""),
            "tags": tags,
        }

        head = [frontmatter(fm), ""]
        head.append(f"# {title_en}")
        if title_ru:
            head.append(f"**{title_ru}**")
        head.append("")

        info = [f"> [!abstract] {CAT_RU.get(cat, cat)} · `{did}`"]
        if d.get("group"):
            info.append(f"> **Раздел Cummins:** {d['group']}")
        if cat_engines:
            info.append("> **Двигатели:** " + ", ".join(
                f"[[{eng_names[e]}|{e}]]" for e in cat_engines if e in eng_names))
        if families:
            info.append("> **Семейство:** " + ", ".join(families))
        if d.get("manuals"):
            mans = []
            for mid in d["manuals"]:
                m = manual_titles.get(mid)
                mans.append(f"[[{m['note']}|{mid}]]" if m else mid)
            info.append("> **Входит в руководства:** " + ", ".join(mans))
        if d.get("sections"):
            info.append("> **Секции:** " + " · ".join(d["sections"][:6]))
        dates = " · ".join(x for x in [
            f"выпущен {d['released']}" if d.get("released") else "",
            f"изменён {d['modified']}" if d.get("modified") else "",
            f"ревизия {d['revision']}" if d.get("revision") else "",
        ] if x)
        if dates:
            info.append(f"> **Даты:** {dates}")
        info.append(f"> **Источник:** [QuickServe]({d['url']}) · "
                    f"[PDF-оригинал]({PDF_BASE + d.get('pdf_rel','')})")
        head.append("\n".join(info))
        head.append("")

        if body_ru:
            head.append(
                "> [!info]- Перевод на русский — машинный черновик\n"
                "> Русский текст получен автоматическим переводом с английского\n"
                "> с подстановкой отраслевой терминологии Cummins; он не\n"
                "> проходил редакторскую вычитку.\n"
                "> **Юридически значим только английский оригинал** — он\n"
                "> приведён в свёрнутом блоке в конце заметки и в PDF.\n")
            head.append("")

        if not d.get("present"):
            head.append("> [!missing] Файл документа не выгружен\n"
                        "> В выгрузке QuickServe этот документ отсутствует — "
                        "доступна только карточка и ссылка на источник.\n")

        parts_block = ""
        if d.get("parts"):
            rows = ["", "## Детали, упомянутые в документе", ""]
            rows.append("| Артикул | Наименование | Русское название |")
            rows.append("|---|---|---|")
            for p in d["parts"][:80]:
                rec = parts_db.get(p, {})
                nm = rec.get("name", "")
                rows.append(f"| [[{p}]] | {nm} | {ru_parts.get(nm.upper(), ru_parts.get(nm, ''))} |")
            parts_block = "\n".join(rows)

        # руководство: оглавление вместо тела
        if cat == "manual":
            mid = did.replace("-history", "")
            rows = toc.get(mid, [])
            secs = collections.OrderedDict()
            for r in rows:
                secs.setdefault(r["section"] or "Без секции", []).append(r)
            out = [f"", f"## Оглавление руководства ({len(rows)} процедур)", ""]
            for sec, items in secs.items():
                out.append(f"### {sec}")
                out.append("")
                out.append("| Номер | Название | Дата |")
                out.append("|---|---|---|")
                for r in items:
                    tgt = state["names"].get(f"{r['cat']}|{r['id']}")
                    link = f"[[{tgt}\\|{r['id']}]]" if tgt else r["id"]
                    date = r["date"] if r["date"] != "Not Available" else ""
                    out.append(f"| {link} | {r['title']} | {date} |")
                out.append("")
            body = "\n".join(out)

        if body_ru:
            text = ("\n".join(head) + "\n" + linkify(body_ru) + "\n" + parts_block
                    + "\n" + linkify(en_fold(body)))
        else:
            text = "\n".join(head) + "\n" + linkify(body) + "\n" + parts_block
        write_note(os.path.join(doc_folder(cat, did, d), note + ".md"), text)
        written += 1

    save_json(os.path.join(BUILD, "state_links.json"), {
        "by_engine": {k: v for k, v in by_engine.items()},
        "part_docs": {k: v for k, v in part_docs.items()},
    })
    print("заметок документов записано:", written)


if __name__ == "__main__":
    main()
