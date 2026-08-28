---
aliases:
  - "Цепь датчика давления охлаждающей жидкости"
type: "Процедура"
doc: "19-fc232"
title_en: "Coolant Pressure Sensor Circuit"
title_ru: "Цепь датчика давления охлаждающей жидкости"
modified: "2026-05-28"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc232.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc232.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Coolant Pressure Sensor Circuit
**Цепь датчика давления охлаждающей жидкости**

> [!abstract] Процедура · `19-fc232`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc232.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc232.pdf)

### Fault Code: 232

### Coolant Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 232 PID(P): P109 SPN: 109 FMI: 4 Lamp: Yellow SRT: 00-388 | Less than 0.33-VDC detected at the coolant pressure sensor signal pin 16 of the engine harness. | No engine protection for coolant pressure. |

![[19800988.png]]

Coolant Pressure Sensor Circuit

### Circuit Description

The coolant pressure sensor monitors coolant pressure and passes information to the ECM through pin 16 of the engine harness. The ECM monitors the voltage on pin 16 and expects to see voltage vary between 0.5 and 4.5 VDC during normal operation. Voltage below 0.33-VDC on pin 16 will trip Fault Code 232 and can be caused by shorts in the supply, signal, or return wires, an open in the return wire, or a failed sensor.

### Component Location

The coolant pressure sensor is located on the exhaust side of the engine, below the oil cooler.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged coolant pressure sensor

- Malfunctioning or damaged engine wiring harness

Refer to Troubleshooting Fault Code t05-232
