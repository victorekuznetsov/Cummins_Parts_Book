#!/usr/bin/env python3
# Формирует FLEET.md — привязка «машина - VIN - ESN - CPL» и какой ESN
# представляет каждую группу (по нему собирается каталог).
#
#   python tools/make_fleet_md.py [fleet_report.json] [fleet.tsv]
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
rep_file = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "fleet_report.json"
tsv_file = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "fleet.tsv"

d = json.loads(rep_file.read_text(encoding="utf-8"))
good = {r["esn"]: r for r in d["checked"] if r.get("ok")}
bad = [r for r in d["checked"] if not r.get("ok")]

vin = {}
if tsv_file.exists():
    for ln in tsv_file.read_text(encoding="utf-8").splitlines()[1:]:
        c = ln.split("	")
        if len(c) >= 3:
            vin[c[2].strip()] = c[1].strip()


def downloaded(esn):
    return (ROOT / "data" / esn / "engine.json").exists()


L = ["# Парк машин: двигатели и каталоги", "",
     "Каталог определяется **CPL**, а не серийным номером: на каждый CPL нужен",
     "один каталог, остальные машины той же группы им покрываются.", "",
     "Проверено по parts.cummins.com; отчёт — `fleet_report.json`, исходный",
     "список — `fleet.tsv`.", "", "## Группы по CPL", ""]

for g in sorted(d["groups"], key=lambda x: str(x["cpl"])):
    rows = sorted((good[e] for e in g["esns"]), key=lambda r: (r["build"], r["esn"]))
    have = [r for r in rows if downloaded(r["esn"])]
    rep = have[-1] if have else rows[-1]          # уже выгруженный, иначе самый свежий
    status = "выгружен" if downloaded(rep["esn"]) else "к выгрузке"
    L += [f"### CPL {g['cpl']} · {g['model']} · {', '.join(g['machines'])}", "",
          f"Двигателей в парке: {len(rows)}. Каталог по **{rep['esn']}** "
          f"({rep['machine']}, сборка {rep['build']}) — {status}.", "",
          "| Машина | VIN | ESN | Конфигурация | Сборка | Деталей |",
          "| --- | --- | --- | --- | --- | ---: |"]
    for r in rows:
        mark = " **←каталог**" if r["esn"] == rep["esn"] else ""
        L.append(f"| {r['machine']} | {vin.get(r['esn'], '')} | {r['esn']}{mark} | "
                 f"{r['config']} | {r['build']} | {r['parts']} |")
    cfgs = sorted({r["config"] for r in rows if r["config"]})
    if len(cfgs) > 1:
        L += ["", f"> В этом CPL две конфигурации ({', '.join(cfgs)}) — состав по "
                  "редким позициям может отличаться."]
    L.append("")

L += ["## Нет в каталоге Cummins", "",
      "Эти серийные номера parts.cummins.com не находит — двигатель другой марки",
      "либо номер не тот. Каталог по ним не собрать.", "",
      "| Машина | VIN | ESN |", "| --- | --- | --- |"]
for r in sorted(bad, key=lambda x: (x.get("machine", ""), x["esn"])):
    L.append(f"| {r.get('machine', '')} | {vin.get(r['esn'], '')} | {r['esn']} |")
L.append("")

(ROOT / "FLEET.md").write_text("\n".join(L), encoding="utf-8")
print(f"FLEET.md: групп {len(d['groups'])}, машин в EPC {len(good)}, не найдено {len(bad)}")
