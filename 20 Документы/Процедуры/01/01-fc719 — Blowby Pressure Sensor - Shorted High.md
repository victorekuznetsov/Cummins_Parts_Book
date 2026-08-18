---
aliases:
  - "Датчик давления прорыва газов — замыкание на плюс"
type: "Процедура"
doc: "01-fc719"
title_en: "Blowby Pressure Sensor - Shorted High"
title_ru: "Датчик давления прорыва газов — замыкание на плюс"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc719.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc719.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Blowby Pressure Sensor - Shorted High
**Датчик давления прорыва газов — замыкание на плюс**

> [!abstract] Процедура · `01-fc719`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc719.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc719.pdf)

### Fault Code: 719

### Blowby Pressure Sensor - Shorted High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 719 PID(P): SPN: FMI: Lamp: Warning SRT: | Crankcase blowby pressure sensor circuit - shorted high. | No engine protection for blowby pressure. |

![[19803587.png]]

Blowby Pressure Sensor Circuit

### Circuit Description

The blowby pressure sensor monitors crankcase blowby pressure and passes information to the electronic control module (ECM). High voltage will trip Fault Code 719 and can be caused by shorts in the supply, signal, or return wires, an open in the return wire, or a failed sensor.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Confirm that the crankcase breathers, breather tubes, and blowby sensor are **not** obstructed.

Refer to Troubleshooting Fault Code t05-719
