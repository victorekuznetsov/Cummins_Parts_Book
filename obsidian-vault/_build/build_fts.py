#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Полнотекстовый индекс документов для поиска в каталоге.

Слова из русских и английских текстов (kb_build/_cache и _cache_ru) ->
data/kb_fts.js: словарь и списки документов на каждое слово. Файл грузится
по требованию — при первом текстовом поиске в базе знаний.

    python3 obsidian-vault/_build/build_fts.py
"""
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import BUILD, SRC

WEB = os.environ.get("KB_WEB", SRC)
CACHE = os.path.join(BUILD, "_cache")
CACHE_RU = os.path.join(BUILD, "_cache_ru")
# слово = латиница/кириллица от трёх букв либо число от четырёх цифр
# (номера деталей, годы, моменты затяжки)
TOK = re.compile(r"[a-zà-ÿ]{3,}|[а-яё]{3,}|\d{4,}")
STOP_SHARE = 0.5          # слово в половине документов — искать по нему нечего


def doc_ids():
    """Идентификаторы документов из data/kb_docs.js — только они попадают в индекс."""
    f = os.path.join(WEB, "data", "kb_docs.js")
    src = open(f, encoding="utf-8").read()
    return json.loads(src[src.find("=") + 1:].rstrip().rstrip(";"))


def main():
    docs = doc_ids()
    ids, index_of = [], {}
    post = collections.defaultdict(set)
    files = 0
    for base in (CACHE, CACHE_RU):
        for root, _dirs, fs in os.walk(base):
            for fn in fs:
                if not fn.endswith(".md"):
                    continue
                did = fn[:-3]
                if did not in docs:
                    continue                      # тексты машин и мусор в индекс не берём
                if did not in index_of:
                    index_of[did] = len(ids)
                    ids.append(did)
                i = index_of[did]
                text = open(os.path.join(root, fn), encoding="utf-8", errors="replace").read().lower()
                files += 1
                for m in TOK.finditer(text):
                    post[m.group(0)].add(i)
    limit = len(ids) * STOP_SHARE
    words = sorted(w for w, v in post.items() if len(v) <= limit)
    data = {"ids": ids, "w": words, "p": [sorted(post[w]) for w in words]}
    out = os.path.join(WEB, "data", "kb_fts.js")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("window.KB_FTS = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
    print(f"документов: {len(ids)} (файлов текста {files}) | слов: {len(words)} "
          f"(отсеяно частых: {len(post) - len(words)}) | "
          f"пар слово-документ: {sum(len(v) for v in data['p'])}")
    print(f"data/kb_fts.js — {os.path.getsize(out)/1048576:.1f} МБ")


main()
