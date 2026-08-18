#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Перенос графики в хранилище: чертежи узлов Cummins, фотографии деталей,
чертежи и иллюстрации машин NHL, PDF-руководства машин."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import DIRS, NHL, SRC, save_json, BUILD
from media import convert_tree, copy_file

PHOTO_SRC = os.path.join(NHL["NTE240"], "engine", "parts", "33239746")


def main():
    report = {}

    # чертежи узлов двигателей Cummins
    total = 0
    root = os.path.join(SRC, "drawings")
    for esn in sorted(os.listdir(root)):
        d = os.path.join(root, esn)
        if os.path.isdir(d):
            m = convert_tree(d, f"{DIRS['draw']}/{esn}", mode="line", maxside=1800)
            total += len(m)
    report["чертежи узлов"] = total

    # фотографии деталей (локальная выгрузка QSK60)
    m = convert_tree(PHOTO_SRC, DIRS["photo"], mode="photo", maxside=520, quality=80)
    report["фото деталей"] = len(m)

    # графика машин NHL
    for machine, base in NHL.items():
        cnt = 0
        for sub, mode, side in (("drawings", "line", 1600),
                                ("service", "photo", 1100),
                                ("service_media", "photo", 1100),
                                ("manual_media", "photo", 1100),
                                ("engine", "photo", 1100)):
            src = os.path.join(base, sub)
            if not os.path.isdir(src):
                continue
            mm = convert_tree(src, f"{DIRS['media']}/{machine}", mode=mode,
                              maxside=side, rename=lambda b, mc=machine: f"{mc}_{b}")
            cnt += len(mm)
        report[f"графика {machine}"] = cnt

        # PDF-руководства машины
        pdfs = 0
        mdir = os.path.join(base, "manuals")
        if os.path.isdir(mdir):
            for f in sorted(os.listdir(mdir)):
                if f.lower().endswith(".pdf"):
                    copy_file(os.path.join(mdir, f),
                              f"{DIRS['manpdf']}/{machine}_{f}")
                    pdfs += 1
        report[f"PDF {machine}"] = pdfs

    save_json(os.path.join(BUILD, "state_media.json"), report)
    for k, v in report.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
