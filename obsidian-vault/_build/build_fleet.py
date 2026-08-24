#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Парк машин: привязка машина → VIN → ESN → CPL → каталог → документы.

Исходные данные: fleet/fleet.tsv (что стоит в парке) и fleet/fleet_report.json
(что о каждом двигателе знает parts.cummins.com).
"""
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import BUILD, DOC_ESN, FAMILY_OF_CAT, load_json, save_json

FLEET = os.path.join(os.path.dirname(BUILD), "fleet")
STATE = os.path.join(BUILD, "state_fleet.json")


def read_tsv(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        head = f.readline().rstrip("\n").split("\t")
        for line in f:
            if line.strip():
                rows.append(dict(zip(head, line.rstrip("\n").split("\t"))))
    return rows


def main():
    tsv = read_tsv(os.path.join(FLEET, "fleet.tsv"))
    rep = load_json(os.path.join(FLEET, "fleet_report.json"), {})
    checked = {c["esn"]: c for c in rep.get("checked", [])}
    cat_state = load_json(os.path.join(BUILD, "state_catalog.json"), {})
    engines = cat_state.get("engines", {})

    # какой ESN каталога соответствует CPL
    cat_of_cpl = {}
    for esn, e in engines.items():
        cat_of_cpl.setdefault(str(e.get("cpl")), esn)

    machines = []
    for r in tsv:
        esn = (r.get("esn") or "").strip()
        c = checked.get(esn, {})
        cpl = str(c.get("cpl") or "")
        cat_esn = cat_of_cpl.get(cpl, "")
        fam, doc_esn = FAMILY_OF_CAT.get(cat_esn, ("", ""))
        machines.append({
            "machine": r.get("machine", ""),
            "vin": r.get("vin", ""),
            "esn": esn,
            "ok": bool(c.get("ok")),
            "model": c.get("model", ""),
            "cpl": cpl,
            "config": c.get("config", ""),
            "build": c.get("build", ""),
            "parts": c.get("parts") or 0,
            "options": c.get("options") or 0,
            "cat_esn": cat_esn,
            "family": fam,
            "doc_esn": doc_esn,
            "err": c.get("err", ""),
        })

    # группы по CPL
    groups = collections.OrderedDict()
    for m in machines:
        if not m["cpl"]:
            continue
        g = groups.setdefault(m["cpl"], {
            "cpl": m["cpl"], "model": m["model"], "cat_esn": m["cat_esn"],
            "family": m["family"], "doc_esn": m["doc_esn"],
            "machines": [], "configs": set(), "kinds": set(),
        })
        g["machines"].append(m["esn"])
        if m["config"]:
            g["configs"].add(m["config"])
        if m["machine"]:
            g["kinds"].add(m["machine"])
    for g in groups.values():
        g["configs"] = sorted(g["configs"])
        g["kinds"] = sorted(g["kinds"])
        g["n"] = len(g["machines"])

    # сколько документов есть по каждой группе
    docs = load_json(os.path.join(BUILD, "state_docs.json"), {}).get("docs", {})
    per_doc_esn = collections.Counter()
    for d in docs.values():
        for e in (d.get("engines") or []):
            per_doc_esn[e] += 1
    for g in groups.values():
        g["docs"] = per_doc_esn.get(g["doc_esn"], 0)

    unknown = [m for m in machines if not m["ok"]]
    save_json(STATE, {
        "machines": machines,
        "groups": list(groups.values()),
        "нет в каталоге Cummins": [m["esn"] for m in unknown],
    })
    print(f"машин в парке: {len(machines)} · групп по CPL: {len(groups)} · "
          f"не найдено в каталоге: {len(unknown)}")
    for g in groups.values():
        mark = "" if g["docs"] else "  ← документации нет"
        print(f"  CPL {g['cpl']:>5} · {g['model']:<22} машин {g['n']:>2} · "
              f"каталог {g['cat_esn'] or '—'} · документов {g['docs']}{mark}")


if __name__ == "__main__":
    main()
