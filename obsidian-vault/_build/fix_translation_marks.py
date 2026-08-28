#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Маркеры жирного в русских текстах: «** текст **», «***», непарные «**»
и осиротевшие одиночные звёздочки, оставшиеся от перевода."""
import os, re, collections

ROOT = "kb_build/_cache_ru"
OPEN = re.compile(r"(?<=[\s(\[|])\*\*[  ]+(?=\S)")
CLOSE = re.compile(r"(?<=\S)[  ]+\*\*(?=[\s.,;:!?)\]|]|$)")
STARS = re.compile(r"\*{3,}")
# одиночная «*» внутри строки; маркер списка в начале строки не трогаем
LONE = re.compile(r"(?<=\S)[  ]+\*(?=[\s,.;:)\]|]|$)")

def main():
    st = collections.Counter(); files = 0
    for root, _d, fs in os.walk(ROOT):
        for fn in fs:
            p = os.path.join(root, fn)
            s = open(p, encoding="utf-8").read(); orig = s
            s, n = OPEN.subn("**", s);  st["пробел после **"] += n
            s, n = CLOSE.subn("**", s); st["пробел перед **"] += n
            s, n = STARS.subn("**", s); st["*** -> **"] += n
            lines = s.split("\n")
            for i, l in enumerate(lines):
                body = l
                bullet = ""
                m = re.match(r"^([  ]*[*\-+][  ]+)", body)   # маркер списка
                if m:
                    bullet, body = m.group(1), body[m.end():]
                body, n = LONE.subn("", body); st["одиночная *"] += n
                l = bullet + body
                if l.count("**") % 2:                        # непарный маркер
                    j = l.rfind("**"); l = l[:j] + l[j + 2:]
                    st["непарный **"] += 1
                lines[i] = l
            s = "\n".join(lines)
            if s != orig:
                open(p, "w", encoding="utf-8").write(s); files += 1
    print("файлов:", files, "|", dict(st.most_common()))

main()
