---
aliases:
  - "Частота/положение коленвала выше нормы — наивысший уровень"
type: "Процедура"
doc: "60-fc234-ecm1"
title_en: "Engine Crankshaft Speed/Position - Data Valid but Above Normal Operational Range - Most Severe Level"
title_ru: "Частота/положение коленвала выше нормы — наивысший уровень"
modified: "2018-06-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc234-ecm1.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc234-ecm1.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Crankshaft Speed/Position - Data Valid but Above Normal Operational Range - Most Severe Level
**Частота/положение коленвала выше нормы — наивысший уровень**

> [!abstract] Процедура · `60-fc234-ecm1`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2018-06-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc234-ecm1.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc234-ecm1.pdf)

### Fault Code: 234-ECM1

### Engine Crankshaft Speed/Position - Data Valid but Above Normal Operational Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 234 PID(P): SPN: 190 FMI: 0 Lamp: Red SRT: | Engine Crankshaft Speed/Position - Data Valid but Above Normal Operational Range - Most Severe Level. Engine speed signal indicates engine speed above engine protection limit. | Fuel injection disabled until engine speed falls below the overspeed limit. |

![[19a00862.png]]

Crankshaft Speed/Position Circuit - QST30 Power Generation Interface Engine

### Circuit Description

The engine crankshaft speed sensor and engine camshaft speed sensor provide engine speed and position information to the ECM through the engine harness.

### Component Location

The engine crankshaft speed sensor is located in the flywheel housing. [[60-100-002 — Engine Diagrams|Refer to Procedure 100-002 in Section E.]]

### Shoptalk

There are multiple ECMs. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

Possible causes of this fault code include:

- External fuel sources drawn into the intake air passage

- Reverse powering (motoring) of the engine

- Tampering of the engine crankshaft speed sensor and the engine camshaft speed sensor.

Inspect the intake manifold for sources of flammable vapors. Check the turbocharger seals to verify that there are no oil leaks. Inspect the engine crankshaft speed sensor and the engine camshaft speed sensor for damage or tampering.

Refer to Troubleshooting Fault Code t05-234
