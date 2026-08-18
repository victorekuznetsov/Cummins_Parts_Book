#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Заменяет ссылки на не извлечённые иллюстрации на понятную пометку."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DIRS, VAULT

EMB = re.compile(r"^!\[\[([^\]\|]+)\]\]$", re.M)


def main():
    have = set(os.listdir(os.path.join(VAULT, DIRS["fig"])))
    for d in (DIRS["draw"], DIRS["media"], DIRS["photo"]):
        base = os.path.join(VAULT, d)
        for root, _dirs, files in os.walk(base):
            have.update(files)
    fixed = files_touched = 0
    for root, _dirs, files in os.walk(VAULT):
        if os.sep + "." in root:
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            text = open(path, encoding="utf-8").read()

            def repl(m):
                nonlocal fixed
                name = m.group(1).split("|")[0].strip()
                if name in have:
                    return m.group(0)
                fixed += 1
                return (f"> [!missing]- Иллюстрация `{name}` не извлечена — "
                        "смотрите PDF-оригинал документа")

            new = EMB.sub(repl, text)
            if new != text:
                open(path, "w", encoding="utf-8").write(new)
                files_touched += 1
    print(f"заменено ссылок: {fixed} в {files_touched} заметках")


if __name__ == "__main__":
    main()
