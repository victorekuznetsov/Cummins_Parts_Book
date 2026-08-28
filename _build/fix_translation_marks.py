#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Чистка типовых огрехов офлайн-перевода в kb_build/_cache_ru.

Модель «залипает» на коротких ячейках таблиц и на разметке: вместо одиночной
отметки «x» выдаёт сотню символов подряд, размножает «*» и «_», повторяет
слово, разносит маркеры жирного («** текст **») и теряет закрывающий «**».
Скрипт правит это по всему корпусу; длина повтора сверяется с английским
оригиналом того же документа, поэтому законные разделители и прочерки
остаются на месте.

    python3 obsidian-vault/_build/fix_translation_marks.py
"""
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import BUILD

RU = os.path.join(BUILD, "_cache_ru")
EN = os.path.join(BUILD, "_cache")

RUNS = re.compile(r"(.)\1{2,}")
WORDS = re.compile(r"\b(\w{2,})((?:[  ]+\1){3,})", re.U)
OPEN = re.compile(r"(?<=[\s(\[|])\*\*[  ]+(?=\S)")
CLOSE = re.compile(r"(?<=\S)[  ]+\*\*(?=[\s.,;:!?)\]|]|$)")
STARS = re.compile(r"\*{3,}")
LONE = re.compile(r"(?<=\S)[  ]+\*(?=[\s,.;:)\]|]|$)")
TERMS = [
    (re.compile(r"Часть номер\(ы\)"), "Номер(а) детали"),
    (re.compile(r"Часть номера"), "Номера деталей"),
    (re.compile(r"Часть номер"), "Номер детали"),
    (re.compile(r"\bСКА\b"), "SCA"),
    # промахи модели, которые проходят мимо словаря перевода (например, через
    # память переводов): washer, nut, bus, liner, screw, tie, oil-компаунды
    (re.compile(r"\bстиральн\w*\s+машин\w*", re.I), "шайба"),
    (re.compile(r"\bорех(и|ов|ами|ах|ам|а|ом|е)?\b", re.I), "гайки"),
    (re.compile(r"\bавтобусн(ый|ая|ое|ые|ых|ым|ими|ого|ому)\b", re.I), "шинный"),
    (re.compile(r"\bлайнер(а|у|ом|е|ы|ов|ам|ами|ах)?\b", re.I), "гильза"),
    (re.compile(r"\bвинтовк(а|и|е|у|ой|ам|ами)?\b", re.I), "винт"),
    (re.compile(r"\bгалстук(а|у|ом|и|ов|ами|ах)?\b", re.I), "стяжка"),
    (re.compile(r"\bнефтепровод"), "маслопровод"),
    (re.compile(r"\bнефтеснабжени(я|е|ю|ем|и)\b"), "маслоподачи"),
    (re.compile(r"\bнефтеотсасывающ"), "маслозаборн"),
    (re.compile(r"интервал(ы|ов|а)? нефтедобычи"), "интервалы замены масла"),
]


def max_run(text, ch):
    return max((len(m.group(0)) for m in re.finditer(re.escape(ch) + "+", text)), default=0)


def fix_runs(ru, en, stat):
    """Повторы символов и слов, которых нет в английском оригинале."""
    def one(m):
        ch, run = m.group(1), m.group(0)
        keep = max_run(en, ch)
        if ch in "xX":
            keep = keep or 1                      # «x» в таблице — отметка
        if len(run) <= max(keep, 2 if ch in "xX" else 5):
            return run
        stat["повтор символа «%s»" % ch] += 1
        return ch * keep

    ru = RUNS.sub(one, ru)

    def word(m):
        stat["повтор слова"] += 1
        return m.group(1)

    return WORDS.sub(word, ru)


def fix_marks(text, stat):
    """Маркеры жирного: пробелы внутри, «***», одиночные и непарные «**»."""
    for _ in range(2):                            # второй проход добирает «** ***»
        text, n = OPEN.subn("**", text);  stat["пробел после **"] += n
        text, n = CLOSE.subn("**", text); stat["пробел перед **"] += n
        text, n = STARS.subn("**", text); stat["*** -> **"] += n
    lines = text.split("\n")
    for i, line in enumerate(lines):
        bullet = ""
        m = re.match(r"^([  ]*[*\-+][  ]+)", line)  # маркер списка не трогаем
        if m:
            bullet, line = m.group(1), line[m.end():]
        line, n = LONE.subn("", line); stat["одиночная *"] += n
        line = bullet + line
        if line.count("**") % 2:
            j = line.rfind("**")
            line = line[:j] + line[j + 2:]
            stat["непарный **"] += 1
        lines[i] = line
    return "\n".join(lines)


def main():
    stat = collections.Counter()
    files = 0
    for root, _dirs, fs in os.walk(RU):
        cat = os.path.basename(root)
        for fn in fs:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(root, fn)
            ru = open(p, encoding="utf-8").read()
            orig = ru
            enf = os.path.join(EN, cat, fn)
            en = open(enf, encoding="utf-8").read() if os.path.exists(enf) else ""
            ru = fix_runs(ru, en, stat)
            ru = fix_marks(ru, stat)
            for rx, rep in TERMS:
                ru, n = rx.subn(rep, ru)
                if n:
                    stat["термин " + rep] += n
            if ru != orig:
                open(p, "w", encoding="utf-8").write(ru)
                files += 1
    print("файлов правлено:", files)
    for k, v in stat.most_common():
        if v:
            print(f"  {k}: {v}")


main()
