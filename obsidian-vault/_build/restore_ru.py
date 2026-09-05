#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Разовый инструмент. Восстановление кэша русских переводов из заметок прошлой сборки
   + чистка «залипаний» офлайн-переводчика (xxxxx…, *****, повтор слова).

   Русский текст лежал только в заметках хранилища: кэш _cache_ru в
   репозиторий не попадал. Достаём его оттуда, чистим и кладём обратно
   в kb_build/_cache_ru, чтобы пересборка не теряла перевод."""
import os, re, sys, collections

OLD = sys.argv[1]                    # распакованные заметки прошлой сборки
OUT = "kb_build/_cache_ru"
EN = "kb_build/_cache"
INFO = "> [!info]- Перевод на русский"
QUOTE = "> [!quote]- Original (English)"
FOLD_CAT = {"Процедуры": "procedures", "TSB": "tsb", "Сервисные бюллетени": "bulletin",
            "Инструмент STI": "sti", "Инструкции по установке": "install_inst",
            "Габаритные чертежи": "outlines", "Руководства": "manual"}

def max_run(text, ch):
    return max((len(m.group(0)) for m in re.finditer(re.escape(ch) + "+", text)), default=0)

WORDS = re.compile(r"\b(\w{2,})((?:[  ]+\1){3,})", re.U)

def clean(ru, en, stat):
    """Схлопывание повторов, которых нет в английском оригинале."""
    def fix_runs(m):
        ch, run = m.group(1), m.group(0)
        keep = max_run(en, ch)
        if ch in "xX":
            keep = keep if keep else 1          # в таблицах «x» — отметка
        if len(run) <= max(keep, 2 if ch in "xX" else 5):
            return run
        stat["символ «%s»" % ch] += 1
        return ch * keep
    ru = re.sub(r"(.)\1{2,}", fix_runs, ru)
    def fix_words(m):
        stat["повтор слова"] += 1
        return m.group(1)
    return WORDS.sub(fix_words, ru)

def main():
    stat = collections.Counter()
    saved = skipped = 0
    for root, _dirs, files in os.walk(OLD):
        cat = None
        for folder, c in FOLD_CAT.items():
            if os.sep + folder in root + os.sep:
                cat = c
                break
        for fn in files:
            if not fn.endswith(".md"):
                continue
            s = open(os.path.join(root, fn), encoding="utf-8").read()
            if INFO not in s or QUOTE not in s:
                skipped += 1
                continue
            m = re.search(r'^doc:\s*"([^"]+)"', s, re.M)
            if not m or not cat:
                skipped += 1
                continue
            did = m.group(1)
            body = s.split(INFO, 1)[1]
            body = body.split("\n\n", 1)[1] if "\n\n" in body else body
            body = body.split(QUOTE, 1)[0]
            # блок «Детали, упомянутые в документе» дописывается при сборке заметки
            body = body.split("\n## Детали, упомянутые в документе", 1)[0].strip()
            enf = os.path.join(EN, cat, did + ".md")
            en = open(enf, encoding="utf-8").read() if os.path.exists(enf) else ""
            body = clean(body, en, stat)
            os.makedirs(os.path.join(OUT, cat), exist_ok=True)
            with open(os.path.join(OUT, cat, did + ".md"), "w", encoding="utf-8") as fh:
                fh.write(body.rstrip() + "\n")
            saved += 1
    print("восстановлено русских текстов:", saved, "| без перевода:", skipped)
    print("исправлено залипаний:", dict(stat.most_common()))

main()
