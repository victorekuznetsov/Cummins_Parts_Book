#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Главная страница, индексы, тематические карты и настройки Obsidian."""
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import (BUILD, CAT_RU, DIRS, FAMILY_OF_CAT, VAULT, load_json,
                    safe_name, write_note)

# тематические карты: (файл, описание, ключевые слова EN/RU)
TOPICS = [
    ("Моменты затяжки и крепёж", "Значения моментов, маркировка болтов, методики затяжки",
     ["torque", "capscrew", "tightening", "момент затяжк", "болт"]),
    ("Диагностика и коды неисправностей", "Деревья диагностики, коды, цепи датчиков",
     ["fault code", "troubleshooting", "circuit", "symptom", "diagnos",
      "код неисправ", "диагностик", "цепь", "дерево"]),
    ("Топливная аппаратура и форсунки", "Форсунки, ТНВД, магистрали, MCRS, фильтры топлива",
     ["injector", "fuel pump", "fuel filter", "fuel line", "rail", "mcrs",
      "форсунк", "топливн", "тнвд", "рампа"]),
    ("Система смазки", "Масло, фильтры, насосы, давление масла",
     ["lubricating oil", "oil pan", "oil pump", "oil cooler", "oil filter",
      "масл", "смазк"]),
    ("Система охлаждения", "ОЖ, насосы, термостаты, радиаторы, теплообменники",
     ["cooling", "coolant", "water pump", "thermostat", "radiator", "aftercooler",
      "охлажд", "термостат", "радиатор", "водян"]),
    ("Турбокомпрессор и наддув", "Турбина, компрессор, наддувочный воздух, впуск/выпуск",
     ["turbocharger", "wastegate", "charge-air", "intake manifold", "exhaust",
      "турбокомпрессор", "наддув", "впускн", "выпускн"]),
    ("Электрика и электронное управление", "ЭБУ, жгуты, датчики, стартер, генератор",
     ["ecm", "electronic control", "wiring harness", "sensor", "starter",
      "alternator", "battery", "эбу", "жгут", "датчик", "стартер", "генератор"]),
    ("Блок, ГБЦ и поршневая группа", "Капремонт: блок, головки, поршни, коленвал, вкладыши",
     ["cylinder block", "cylinder head", "piston", "crankshaft", "camshaft",
      "bearing", "liner", "connecting rod", "блок цилиндр", "головк", "поршн",
      "коленчат", "распредел", "вкладыш", "гильз"]),
    ("ТО, интервалы и регламенты", "Регламент ТО, ежедневные и периодические работы",
     ["maintenance schedule", "maintenance procedures", "service interval",
      "регламент", "обслуживан", "интервал"]),
    ("Эксплуатация и хранение", "Пуск, останов, обкатка, консервация, холодный климат",
     ["operating", "starting procedure", "storage", "run-in", "cold weather",
      "эксплуатац", "пуск", "хранени", "обкатк"]),
    ("Жидкости и ГСМ", "Масла, охлаждающие жидкости, топливо, присадки, анализы",
     ["coolant recommend", "fuel recommend", "oil analysis", "fluids", "biodiesel",
      "sca", "жидкост", "анализ масла", "топливо для"]),
    ("Сервисный инструмент", "Инструмент, приспособления, INSITE, адаптеры",
     ["service tool", "insite", "inline", "gauge", "installer", "remover",
      "инструмент", "калибр", "оправк", "съёмник"]),
]


def topic_match(text, keys):
    t = (text or "").lower()
    return any(k in t for k in keys)


def main():
    docs_state = load_json(os.path.join(BUILD, "state_docs.json"), {})
    cat = load_json(os.path.join(BUILD, "state_catalog.json"), {})
    machines = load_json(os.path.join(BUILD, "state_machines.json"), {})
    figs = load_json(os.path.join(BUILD, "state_figures.json"), {})
    media = load_json(os.path.join(BUILD, "state_media.json"), {})
    ru_docs = load_json(os.path.join(BUILD, "ru_docs.json"), {})
    docs = docs_state.get("docs", {})
    toc = docs_state.get("manual_toc", {})

    engines = cat.get("engines", {})
    parts = cat.get("parts", {})
    options = cat.get("options", {})
    kits = cat.get("kits", {})
    eng_note = {esn: safe_name(f"{esn} — {e['model']} CPL {e['cpl']}")
                for esn, e in engines.items()}

    by_cat = collections.defaultdict(list)
    for key, d in docs.items():
        by_cat[d["cat"]].append(d)
    for v in by_cat.values():
        v.sort(key=lambda x: x["id"])

    n_docs = len(docs)
    n_parts = len(parts)
    n_figs = len(os.listdir(os.path.join(VAULT, DIRS["fig"]))) \
        if os.path.isdir(os.path.join(VAULT, DIRS["fig"])) else 0

    def title(d):
        return d.get("title") or d["id"]

    def ru(d):
        return ru_docs.get(title(d), "")

    def link(d, label=None):
        return f"[[{d['note']}\\|{label or d['id']}]]"

    # ------------------------------------------------------------- главная
    home = [
        "---",
        'type: "Главная"',
        'cssclasses:',
        '  - "wide"',
        "---",
        "",
        "# База знаний Cummins · «Развитие»",
        "",
        "> [!abstract] Что здесь есть",
        f"> **{n_docs}** документов QuickServe (TSB, процедуры ремонта, сервисные "
        f"бюллетени, инструкции по инструменту, руководства) · "
        f"**{n_parts}** деталей · **{len(options)}** узлов · **{len(kits)}** комплектов · "
        f"**{len(engines)}** двигателей · **{len(machines)}** машин · "
        f"**{n_figs}** иллюстраций офлайн.",
        "> Всё связано перекрёстными ссылками: деталь → узел → двигатель → "
        "документы, где она упоминается.",
        "",
        "## С чего начать",
        "",
        "| Задача | Куда идти |",
        "|---|---|",
        "| Найти деталь по артикулу | `Ctrl+O` → введите номер (например `3930319`) |",
        "| Найти деталь по названию | `Ctrl+O` → «форсунка», «прокладка ГБЦ» — работает по-русски |",
        "| Понять, как ремонтировать узел | [[Процедуры — по группам]] или [[Все руководства]] |",
        "| Проверить, нет ли бюллетеня по проблеме | [[TSB — по годам]] · [[TSB — по темам]] |",
        "| Собрать комплект на ремонт | [[Комплекты и ремкомплекты]] |",
        "| Узнать цену | [[Детали с ценами]] |",
        "| Разобраться в поиске | [[Как искать в этой базе]] |",
        "",
        "## Двигатели",
        "",
        "| ESN | Модель | CPL | Машина | Узлов | Позиций |",
        "|---|---|---|---|---|---|",
    ]
    machine_of = {"33239899": "NTE200", "33239746": "NTE240", "37295879": "TR100A"}
    for esn, e in sorted(engines.items()):
        m = machine_of.get(esn, "")
        home.append(f"| [[{eng_note[esn]}\\|{esn}]] | {e['model']} | {e['cpl']} | "
                    f"{('[['+m+']]') if m else '—'} | {len(e['options'])} | {e['parts_total']} |")
    home += [
        "",
        "## Машины",
        "",
    ]
    for name, m in sorted(machines.items()):
        home.append(f"- [[{name}]] — {m.get('title_en','')} · разделов каталога "
                    f"{len(m.get('sections',[]))}, инструкций по ремонту "
                    f"{len(m.get('service',[]))}, позиций с ценой {m.get('prices',0)}")
    home += [
        "",
        "## Индексы",
        "",
        "- [[Все руководства]] — 35 руководств Cummins с полным оглавлением",
        "- [[Процедуры — по группам]] — процедуры ремонта и обслуживания",
        "- [[TSB — по годам]] · [[TSB — по темам]] — технические бюллетени",
        "- [[Сервисные бюллетени и STI]] — бюллетени, инструмент, установка",
        "- [[Детали — алфавитный указатель]] · [[Детали с ценами]]",
        "- [[Узлы двигателей]] · [[Комплекты и ремкомплекты]]",
        "- [[Карта хранилища]] — что где лежит",
        "",
        "## Темы",
        "",
    ]
    for name, desc, _ in TOPICS:
        home.append(f"- [[{name}]] — {desc}")
    home += [
        "",
        "> [!tip] Как всё связано",
        "> Откройте любую деталь — внизу будут узлы, комплекты, цепочка замен и "
        "документы, где её артикул упоминается. Откройте процедуру — сверху "
        "двигатели и руководства, снизу список упомянутых деталей.",
        "> Граф связей (`Ctrl+G`) показывает всю базу целиком.",
        "",
        "---",
        "",
        "> [!info]- Источники и оговорки",
        "> Документы выгружены из **quickserve.cummins.com**, каталоги — из "
        "**parts.cummins.com** по серийным номерам двигателей. Иллюстрации "
        "процедур извлечены из PDF-оригиналов и сопоставлены с текстом "
        "автоматически: в редких случаях к абзацу может относиться соседний рисунок — "
        f"проверка голосованием по {figs.get('надёжных документов', 0)} документам "
        "совпала с исходной раскладкой почти везде.",
        "> Массы деталей приведены как в каталоге Cummins (поле «Масса, кг»); "
        "для мелкого крепежа значения в источнике встречаются в разных единицах — "
        "сверяйтесь с оригинальными атрибутами в карточке.",
        "> Тексты документов — оригинальные, на английском. Переведены названия "
        "документов, деталей, узлов и вся навигация.",
        "> Вопросы и замечания — Кузнецов В.Е., KuznetsovVE@industrservice.ru",
    ]
    write_note("00 Главная.md", "\n".join(home))

    # --------------------------------------------------------- как искать
    search = [
        "---", 'type: "Справка"', "---", "",
        "# Как искать в этой базе",
        "",
        "> [!tip] Три главных сочетания клавиш",
        "> `Ctrl+O` — быстрый переход по названию заметки (работает и по русским "
        "названиям — они прописаны в поле `aliases`).",
        "> `Ctrl+Shift+F` — полнотекстовый поиск по всем документам.",
        "> `Ctrl+G` — граф связей.",
        "",
        "## Поиск по артикулу",
        "",
        "Введите номер в `Ctrl+O` — откроется карточка детали. "
        "Через `Ctrl+Shift+F` тот же номер найдётся ещё и в текстах процедур, "
        "бюллетеней и составах узлов.",
        "",
        "## Поисковые запросы, которые стоит знать",
        "",
        "| Запрос | Что найдёт |",
        "|---|---|",
        "| `tag:#документ/tsb` | все технические бюллетени |",
        "| `tag:#документ/процедура` | все процедуры ремонта |",
        '| `tag:#двигатель/QST30` | всё по семейству QST30 |',
        "| `tag:#деталь tag:#есть-цена` | детали, для которых есть цена |",
        '| `"Torque Value"` | все места, где указан момент затяжки |',
        '| `path:"20 Документы/TSB" 2019` | бюллетени 2019 года |',
        '| `file:(3930319)` | заметка конкретной детали |',
        '| `["Регулировка клапанного механизма"]` | по русскому названию |',
        "",
        "## Что означают поля заметки",
        "",
        "| Поле | Смысл |",
        "|---|---|",
        "| `doc` | номер документа Cummins |",
        "| `engines` | ESN двигателей, к которым относится документ |",
        "| `families` | семейство двигателей (QSK50, QST30, C8.3 …) |",
        "| `manuals` | руководства, в которые входит процедура |",
        "| `parts` | артикулы, упомянутые в тексте |",
        "| `supersedes` | цепочка замен номера детали |",
        "| `source` | ссылка на оригинал в QuickServe |",
        "| `pdf` | ссылка на исходный PDF в репозитории |",
        "",
        "## Callout'ы в текстах процедур",
        "",
        "> [!danger] WARNING · Опасно",
        "> Риск травмы — оригинальное предупреждение Cummins.",
        "",
        "> [!warning] CAUTION · Осторожно",
        "> Риск повреждения техники.",
        "",
        "> [!tip] Момент затяжки · Torque Value",
        "> Значение момента из оригинала процедуры.",
        "",
        "## Полезные плагины (не обязательны)",
        "",
        "База полностью работает **без плагинов**. Если хотите больше:",
        "",
        "- **Dataview** — динамические таблицы и фильтры по полям заметок.",
        "- **Omnisearch** — нечёткий поиск с учётом опечаток.",
        "- **Recent Files**, **Better Word Count** — мелкие удобства.",
        "",
        "> [!example]- Пример запроса Dataview (если плагин установлен)",
        "> ````",
        "> ```dataview",
        "> TABLE title_ru AS \"Название\", released AS \"Выпущен\"",
        '> FROM #документ/tsb',
        "> WHERE contains(families, \"QST30\")",
        "> SORT released DESC",
        "> ```",
        "> ````",
    ]
    write_note("Как искать в этой базе.md", "\n".join(search))

    # ------------------------------------------------------------ индексы
    idx = DIRS["index"]

    # руководства
    rows = ["---", 'type: "Индекс"', "---", "", "# Все руководства", "",
            f"Оглавления {len(by_cat.get('manual', []))} руководств Cummins. "
            "Внутри каждого — секции и ссылки на процедуры.", "",
            "| Руководство | Название | Процедур |", "|---|---|---|"]
    for d in sorted(by_cat.get("manual", []), key=lambda x: title(x)):
        mid = d["id"].replace("-history", "")
        rows.append(f"| {link(d, mid)} | {title(d)}"
                    + (f"<br>*{ru(d)}*" if ru(d) else "")
                    + f" | {len(toc.get(mid, []))} |")
    write_note(f"{idx}/Все руководства.md", "\n".join(rows))

    # процедуры по группам
    groups = collections.defaultdict(list)
    for d in by_cat.get("procedures", []):
        g = d["id"].split("-")[0]
        groups[g if re.match(r"^[0-9]{1,3}$", g) else "прочие"].append(d)
    rows = ["---", 'type: "Индекс"', "---", "", "# Процедуры — по группам", "",
            f"Всего {len(by_cat.get('procedures', []))} процедур. "
            "Номер группы — первая часть номера процедуры Cummins.", ""]
    for g in sorted(groups, key=lambda x: (len(x), x)):
        items = groups[g]
        mans = collections.Counter(m for d in items for m in d.get("manuals", []))
        man_hint = ""
        if mans:
            top = mans.most_common(1)[0][0]
            md = docs.get(f"manual|{top}-history")
            if md:
                man_hint = f" · в основном из «{title(md)}»"
        rows += [f"## Группа {g} ({len(items)}){man_hint}", "",
                 "| Номер | Название | Русское название |", "|---|---|---|"]
        for d in sorted(items, key=lambda x: x["id"]):
            rows.append(f"| {link(d)} | {title(d)} | {ru(d)} |")
        rows.append("")
    write_note(f"{idx}/Процедуры — по группам.md", "\n".join(rows))

    # TSB по годам и по темам
    tsbs = by_cat.get("tsb", [])
    by_year = collections.defaultdict(list)
    for d in tsbs:
        y = (d.get("released") or "")[:4]
        if not y:
            m = re.match(r"tsb(\d{2})", d["id"])
            y = ("20" + m.group(1)) if m and int(m.group(1)) < 80 else "—"
        by_year[y].append(d)
    rows = ["---", 'type: "Индекс"', "---", "", "# TSB — по годам", "",
            f"{len(tsbs)} технических бюллетеней Cummins.", ""]
    for y in sorted(by_year, reverse=True):
        rows += [f"## {y} ({len(by_year[y])})", "",
                 "| Номер | Название | Русское название | Дата |", "|---|---|---|---|"]
        for d in sorted(by_year[y], key=lambda x: x.get("released") or "", reverse=True):
            rows.append(f"| {link(d)} | {title(d)} | {ru(d)} | {d.get('released','')} |")
        rows.append("")
    write_note(f"{idx}/TSB — по годам.md", "\n".join(rows))

    by_group = collections.defaultdict(list)
    for d in tsbs:
        by_group[d.get("group") or "Без раздела"].append(d)
    rows = ["---", 'type: "Индекс"', "---", "", "# TSB — по темам", "",
            "Разделы — как в QuickServe (группы 00–19 по системам двигателя).", ""]
    for g in sorted(by_group):
        rows += [f"## {g} ({len(by_group[g])})", "",
                 "| Номер | Название | Русское название | Дата |", "|---|---|---|---|"]
        for d in sorted(by_group[g], key=lambda x: x.get("released") or "", reverse=True):
            rows.append(f"| {link(d)} | {title(d)} | {ru(d)} | {d.get('released','')} |")
        rows.append("")
    write_note(f"{idx}/TSB — по темам.md", "\n".join(rows))

    # бюллетени, STI, установка, чертежи
    rows = ["---", 'type: "Индекс"', "---", "", "# Сервисные бюллетени и STI", ""]
    for c, head in (("bulletin", "Сервисные бюллетени"),
                    ("sti", "Инструкции по сервисному инструменту (STI)"),
                    ("install_inst", "Инструкции по установке"),
                    ("outlines", "Габаритные чертежи")):
        items = by_cat.get(c, [])
        if not items:
            continue
        rows += [f"## {head} ({len(items)})", "",
                 "| Номер | Название | Русское название | Дата |", "|---|---|---|---|"]
        for d in sorted(items, key=lambda x: title(x)):
            rows.append(f"| {link(d)} | {title(d)} | {ru(d)} | {d.get('released','')} |")
        rows.append("")
    write_note(f"{idx}/Сервисные бюллетени и STI.md", "\n".join(rows))

    # детали
    shards = collections.defaultdict(list)
    for no, p in parts.items():
        p = dict(p, no=no)
        shards[no[0] if no[:1].isdigit() else "буквенные"].append(p)
    rows = ["---", 'type: "Индекс"', "---", "", "# Детали — алфавитный указатель", "",
            f"{n_parts} артикулов. Разделы — по первой цифре номера.", ""]
    for s in sorted(shards):
        items = sorted(shards[s], key=lambda x: x["no"])
        rows += [f"## {s} ({len(items)})", "",
                 "| Артикул | Наименование | Русское название | Двигатели |", "|---|---|---|---|"]
        for p in items:
            rows.append(f"| [[{p['no']}]] | {p.get('name','')} | {p.get('name_ru','')} | "
                        f"{', '.join(p.get('engines', []))} |")
        rows.append("")
    write_note(f"{idx}/Детали — алфавитный указатель.md", "\n".join(rows))

    priced = [dict(p, no=no) for no, p in parts.items() if p.get("price")]
    rows = ["---", 'type: "Индекс"', "---", "", "# Детали с ценами", "",
            f"{len(priced)} артикулов Cummins, для которых есть цена в прайсах машин NHL.", "",
            "| Артикул | Наименование | Русское название | Машина | Цена |",
            "|---|---|---|---|---|"]
    for p in sorted(priced, key=lambda x: x.get("no") or ""):
        for machine, pr in sorted(p["price"].items()):
            rows.append(f"| [[{p['no']}]] | {p.get('name','')} | {p.get('name_ru','')} | "
                        f"[[{machine}]] | {pr['price']} |")
    write_note(f"{idx}/Детали с ценами.md", "\n".join(rows))

    # узлы и комплекты
    rows = ["---", 'type: "Индекс"', "---", "", "# Узлы двигателей", "",
            f"{len(options)} узлов (опций каталога) по всем двигателям.", ""]
    by_eng = collections.defaultdict(list)
    for key, o in options.items():
        by_eng[o["esn"]].append(o)
    for esn in sorted(by_eng):
        e = engines.get(esn, {})
        rows += [f"## {esn} — {e.get('model','')} ({len(by_eng[esn])})", "",
                 "| Узел | Название | Система | Позиций |", "|---|---|---|---|"]
        for o in sorted(by_eng[esn], key=lambda x: x["no"]):
            note = safe_name(f"{o['esn']} {o['no']} — {o['name']}", 90)
            syst = ", ".join(s["name"] for s in o["systems"])
            rows.append(f"| [[{note}\\|{o['no']}]] | {o['name']} | {syst} | {len(o['parts'])} |")
        rows.append("")
    write_note(f"{idx}/Узлы двигателей.md", "\n".join(rows))

    rows = ["---", 'type: "Индекс"', "---", "", "# Комплекты и ремкомплекты", "",
            f"{len(kits)} комплектов по всем двигателям.", "",
            "| Комплект | Название | Двигатель | Тип | Позиций |", "|---|---|---|---|---|"]
    for key, k in sorted(kits.items(), key=lambda kv: (kv[1]["esn"], kv[1]["no"])):
        note = safe_name(f"Комплект {k['no']} — {k['name']}", 90)
        rows.append(f"| [[{note}\\|{k['no']}]] | {k['name']} | "
                    f"[[{eng_note.get(k['esn'], k['esn'])}\\|{k['esn']}]] | "
                    f"{k.get('type','')} | {len(k['parts'])} |")
    write_note(f"{idx}/Комплекты и ремкомплекты.md", "\n".join(rows))

    # ------------------------------------------------------------- темы
    for name, desc, keys in TOPICS:
        hits = [d for d in docs.values()
                if topic_match(title(d), keys) or topic_match(ru(d), keys)]
        rows = ["---", 'type: "Тема"', f'tags:\n  - "тема"', "---", "",
                f"# {name}", "", f"*{desc}*", "",
                f"Найдено {len(hits)} документов по ключевым словам темы.", ""]
        by_c = collections.defaultdict(list)
        for d in hits:
            by_c[d["cat"]].append(d)
        for c in ("manual", "tsb", "procedures", "bulletin", "sti",
                  "install_inst", "outlines"):
            items = by_c.get(c)
            if not items:
                continue
            rows += [f"## {CAT_RU.get(c, c)} ({len(items)})", "",
                     "| Номер | Название | Русское название |", "|---|---|---|"]
            for d in sorted(items, key=lambda x: x["id"]):
                rows.append(f"| {link(d)} | {title(d)} | {ru(d)} |")
            rows.append("")
        write_note(f"{DIRS['topic']}/{name}.md", "\n".join(rows))

    # ----------------------------------------------------- карта хранилища
    rows = ["---", 'type: "Справка"', "---", "", "# Карта хранилища", "",
            "| Папка | Что внутри | Заметок |", "|---|---|---|",
            f"| `00 Главная` | стартовая страница | 1 |",
            f"| `01 Индексы` | указатели по всем разделам | — |",
            f"| `10 Двигатели` | паспорта двигателей по ESN | {len(engines)} |",
            f"| `11 Машины` | NTE200, NTE240, TR100A: каталоги и ремонт | "
            f"{sum(len(m.get('sections', [])) + len(m.get('service', [])) for m in machines.values()) + len(machines)} |",
            f"| `20 Документы` | TSB, процедуры, бюллетени, STI, руководства | {n_docs} |",
            f"| `30 Детали` | карточки артикулов | {n_parts} |",
            f"| `40 Узлы` | опции каталога с составом | {len(options)} |",
            f"| `50 Комплекты` | ремкомплекты | {len(kits)} |",
            f"| `60 Темы` | тематические карты | {len(TOPICS)} |",
            "| `90 Приложения` | иллюстрации, чертежи, фото деталей, PDF машин | — |",
            "| `_build` | скрипты пересборки базы | — |",
            "",
            "## Графика",
            "",
            "| Что | Файлов |", "|---|---|",
            f"| Иллюстрации процедур (из PDF) | {n_figs} |",
            f"| Чертежи узлов двигателей | {media.get('чертежи узлов', 0)} |",
            f"| Фотографии деталей | {media.get('фото деталей', 0)} |",
            f"| Графика машин NHL | "
            f"{sum(v for k, v in media.items() if k.startswith('графика'))} |",
            f"| PDF-руководства машин | "
            f"{sum(v for k, v in media.items() if k.startswith('PDF'))} |",
            ]
    write_note(f"{idx}/Карта хранилища.md", "\n".join(rows))

    print("индексы и темы записаны")


if __name__ == "__main__":
    main()
