#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка целостности хранилища: битые ссылки и отсутствующие картинки."""
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import VAULT

LINK = re.compile(r"(!?)\[\[([^\]\|#]+)")


def main():
    notes, assets = set(), set()
    for root, _dirs, files in os.walk(VAULT):
        if os.sep + "." in root:
            continue
        for f in files:
            if f.endswith(".md"):
                notes.add(os.path.splitext(f)[0])
            else:
                assets.add(f)
                assets.add(os.path.splitext(f)[0])

    broken = collections.Counter()
    broken_img = collections.Counter()
    total = 0
    for root, _dirs, files in os.walk(VAULT):
        if os.sep + "." in root:
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            text = open(os.path.join(root, f), encoding="utf-8").read()
            for bang, target in LINK.findall(text):
                target = target.strip().replace("\\", "")
                total += 1
                if bang:
                    if target not in assets:
                        broken_img[target] += 1
                elif target not in notes and target not in assets:
                    broken[target] += 1

    print(f"заметок: {len(notes)}, файлов-вложений: {len(assets)//2}")
    print(f"ссылок всего: {total}")
    print(f"битых ссылок на заметки: {sum(broken.values())} "
          f"({len(broken)} уникальных целей)")
    for t, c in broken.most_common(15):
        print(f"   {c:>5}  [[{t}]]")
    print(f"битых вложений: {sum(broken_img.values())} "
          f"({len(broken_img)} уникальных)")
    for t, c in broken_img.most_common(10):
        print(f"   {c:>5}  ![[{t}]]")


if __name__ == "__main__":
    main()
