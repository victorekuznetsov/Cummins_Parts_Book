---
aliases:
  - "Высокая частота вращения — выше нормы — наивысший уровень"
type: "Процедура"
doc: "60-fc234-ecm2"
title_en: "Engine Speed High - Data Valid but Above Normal Operational Range - Most Severe Level"
title_ru: "Высокая частота вращения — выше нормы — наивысший уровень"
modified: "2018-06-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc234-ecm2.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc234-ecm2.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Speed High - Data Valid but Above Normal Operational Range - Most Severe Level
**Высокая частота вращения — выше нормы — наивысший уровень**

> [!abstract] Процедура · `60-fc234-ecm2`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2018-06-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc234-ecm2.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc234-ecm2.pdf)

### Fault Code: 234-ECM2

### Engine Speed High - Data Valid but Above Normal Operational Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 234 PID(P): SPN: 190 FMI: 0 Lamp: Red SRT: | Engine Speed High - Data Valid but Above Normal Operational Range - Most Severe Level | The fuel shutoff valve is de-energized (closed). The fuel shutoff valve is re-engergized (opened) when engine speed falls below the calibrated value (2130 rpm). |

![[19a00863.png]]

Engine Speed High Circuit - QST30 Power Generation Interface Engine

### Circuit Description

The engine speed sensor monitors the engine position and the engine speed and passes this information to the electronic control module (ECM) through the engine harness.

### Component Location

The engine speed sensor and the engine position sensor are located in the flywheel housing.

### Shoptalk

- Inspect the intake manifold for sources of flammable vapors. Check the turbocharger seals to verify that there are no oil leaks.

- Inspect the engine speed sensor for signs of damage or tampering.

Refer to Troubleshooting Fault Code t05-234
