---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "19-fc115"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2011-03-01"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc115.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc115.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `19-fc115`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc115.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc115.pdf)

### Fault Code: 115

### Engine Speed Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 115 PID(P): P190 SPN: 190 FMI: 2 Lamp: Red SRT: 00-345 | No engine speed signal detected at pins 27, 28, 37, and 38 of the engine harness. | Engine is shut down and can **not** be run. |

![[19400001.png]]

Engine Speed Sensor Circuit

### Circuit Description

The engine speed sensor is a dual-coil circuit that provides the engine speed signal to the ECM through the engine harness.

### Component Location

The engine speed sensor is located above the accessory drive.

### Shoptalk

- If the problem occurs **only** at a certain engine temperature, be sure to check the engine speed sensor (engine speed sensor) circuit while the engine is at that particular temperature.

- Check camshaft end play to make sure that the camshaft gear is **not** moving too far away from the end of the engine speed sensor.

Refer to Troubleshooting Fault Code t05-115
