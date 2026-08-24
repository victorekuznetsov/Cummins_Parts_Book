#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Разбор каталогов запчастей data/<ESN>.js в состояние для заметок.

Собирает: двигатели, узлы (опции), комплекты, детали (карточки),
обратные связи деталь -> узлы/комплекты/двигатели, цены из каталогов NHL,
чертежи листов узлов.
"""
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import BUILD, NHL, SRC, catalogs, load_json, save_json

PHOTO = "https://parts.cummins.com/graphics/parts/{p3}/{no}/{img}"


def nhl_prices():
    """Цены из каталогов машин NHL: артикул -> {машина: {цена, группа, имя}}."""
    out = collections.defaultdict(dict)
    for machine, path in NHL.items():
        f = os.path.join(path, "data", "prices.js")
        if not os.path.exists(f):
            continue
        s = open(f, encoding="utf-8").read()
        data = json.loads(s[s.find("=") + 1:].rstrip().rstrip(";"))
        for no, rec in data.items():
            out[no][machine] = {
                "price": rec.get("p"),
                "group": rec.get("g", ""),
                "name": rec.get("n", ""),
            }
    return out


def main():
    prices = nhl_prices()
    engines, options, kits, parts = {}, {}, {}, {}

    for cat in catalogs():
        esn = cat["esn"]
        sheets = set()
        engines[esn] = {
            "esn": esn, "model": cat["model"], "cpl": cat["cpl"],
            "build": cat.get("buildDate", ""), "config": cat.get("config", ""),
            "group": cat.get("group", ""), "plant": cat.get("plant", ""),
            "systems": cat["systems"],
            "options": [o["no"] for o in cat["options"]],
            "kits": [k["no"] for k in cat["kits"]],
            "parts_total": sum(len(o["parts"]) for o in cat["options"]),
        }
        sys_of_option = {}
        for s in cat["systems"]:
            for o in s["options"]:
                sys_of_option.setdefault(o, []).append(s)

        for o in cat["options"]:
            key = f"{esn}|{o['no']}"
            systems = [{"code": s["code"], "name": s["name"]}
                       for s in sys_of_option.get(o["no"], [])]
            options[key] = {
                "esn": esn, "no": o["no"], "name": o.get("name") or "",
                "systems": systems,
                "remarks": [x.strip() for x in (o.get("remarks") or "").split("|") if x.strip()],
                "sheets": o.get("sheets") or [],
                "parts": o["parts"],
            }
            sheets.update(o.get("sheets") or [])
            for p in o["parts"]:
                rec = parts.setdefault(p["no"], {
                    "no": p["no"], "names": collections.Counter(), "engines": set(),
                    "options": [], "kits": [], "card": {}, "img": "",
                })
                if p.get("name"):
                    rec["names"][p["name"].strip()] += 1
                rec["engines"].add(esn)
                rec["options"].append({"esn": esn, "opt": o["no"],
                                       "opt_name": o.get("name") or "",
                                       "pos": p.get("pos", ""), "qty": p.get("qty", ""),
                                       "dim": p.get("dim", ""), "rem": p.get("rem", "")})
                if p.get("img") and not rec["img"]:
                    rec["img"] = p["img"]

        for k in cat["kits"]:
            key = f"{esn}|{k['no']}"
            kits[key] = {"esn": esn, "no": k["no"], "name": k.get("name") or "",
                         "notes": k.get("notes", ""), "type": k.get("type", ""),
                         "parts": k["parts"]}
            for p in k["parts"]:
                rec = parts.setdefault(p["no"], {
                    "no": p["no"], "names": collections.Counter(), "engines": set(),
                    "options": [], "kits": [], "card": {}, "img": "",
                })
                if p.get("name"):
                    rec["names"][p["name"].strip()] += 1
                rec["engines"].add(esn)
                rec["kits"].append({"esn": esn, "kit": k["no"], "kit_name": k.get("name") or ""})

        for no, card in cat["cards"].items():
            rec = parts.setdefault(no, {
                "no": no, "names": collections.Counter(), "engines": set(),
                "options": [], "kits": [], "card": {}, "img": "",
            })
            if not rec["card"]:
                rec["card"] = card
            rec["engines"].add(esn)

        engines[esn]["sheets"] = sorted(sheets)

    # финализация
    for no, rec in parts.items():
        rec["name"] = rec["names"].most_common(1)[0][0] if rec["names"] else ""
        rec["alt_names"] = [n for n, _ in rec["names"].most_common()[1:]]
        rec.pop("names")
        rec["engines"] = sorted(rec["engines"])
        rec["price"] = prices.get(no, {})
        card = rec.get("card") or {}
        views = card.get("views") or ([rec["img"]] if rec["img"] else [])
        rec["photos"] = [PHOTO.format(p3=no[:3], no=no, img=v) for v in views[:4]]

    state = {
        "engines": engines,
        "options": options,
        "kits": kits,
        "parts": parts,
    }
    save_json(os.path.join(BUILD, "state_catalog.json"), state)
    print("двигателей", len(engines), "| узлов", len(options),
          "| комплектов", len(kits), "| деталей", len(parts),
          "| с ценой", sum(1 for p in parts.values() if p["price"]))


if __name__ == "__main__":
    main()
