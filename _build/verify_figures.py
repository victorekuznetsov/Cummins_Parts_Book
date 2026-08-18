#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка сопоставления иллюстраций «голосованием».

Одна и та же иллюстрация Cummins встречается в нескольких документах.
Берём только документы, где количество картинок в PDF точно совпало с
количеством ссылок в HTML (надёжное сопоставление), и для каждого имени
выбираем содержимое, встретившееся чаще всего. Это убирает ошибки
позиционного сопоставления в документах со сбитым порядком.
"""
import collections
import hashlib
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import BUILD, DIRS, VAULT, load_json, save_json
from figures import compress, pdf_images

SRC = os.environ.get("KB_SRC", "/home/user/Cummins_Parts_Book")


def main():
    t0 = time.time()
    state = load_json(os.path.join(BUILD, "state_docs.json"), {})
    docs = state.get("docs", {})
    cache = os.path.join(BUILD, "_cache")

    votes = collections.defaultdict(collections.Counter)   # имя -> хэш -> голосов
    blobs = {}                                             # хэш -> байты
    exact = 0
    for n, (key, d) in enumerate(sorted(docs.items()), 1):
        if not d.get("present") or not d.get("figures"):
            continue
        md_path = os.path.join(cache, d["cat"], d["id"] + ".md")
        if not os.path.exists(md_path):
            continue
        md = open(md_path, encoding="utf-8").read()
        names = [line[3:-2] for line in md.split("\n")
                 if line.startswith("![[") and line.endswith("]]")]
        if not names:
            continue
        pdf = os.path.join(SRC, "bulletins", d["pdf_rel"])
        imgs = pdf_images(pdf)
        if len(imgs) != len(names):
            continue
        exact += 1
        for nm, blob in zip(names, imgs):
            h = hashlib.md5(blob).hexdigest()
            votes[nm][h] += 1
            blobs.setdefault(h, blob)
        if n % 500 == 0:
            print(f"  {n}/{len(docs)}, надёжных {exact}, "
                  f"имён {len(votes)}, {time.time()-t0:.0f} c", flush=True)

    out_dir = os.path.join(VAULT, DIRS["fig"])
    os.makedirs(out_dir, exist_ok=True)
    rewritten = ambiguous = 0
    for nm, cnt in votes.items():
        best, n_best = cnt.most_common(1)[0]
        if len(cnt) > 1:
            ambiguous += 1
        try:
            data = compress(blobs[best])
        except Exception:                                   # noqa: BLE001
            continue
        path = os.path.join(out_dir, nm)
        old = b""
        if os.path.exists(path):
            old = open(path, "rb").read()
        if old != data:
            with open(path, "wb") as fh:
                fh.write(data)
            rewritten += 1

    save_json(os.path.join(BUILD, "state_figures.json"), {
        "имён с голосованием": len(votes),
        "надёжных документов": exact,
        "переписано файлов": rewritten,
        "имён с расхождением": ambiguous,
    })
    print(f"имён {len(votes)}, надёжных документов {exact}, "
          f"переписано {rewritten}, спорных имён {ambiguous}, {time.time()-t0:.0f} c")


if __name__ == "__main__":
    main()
