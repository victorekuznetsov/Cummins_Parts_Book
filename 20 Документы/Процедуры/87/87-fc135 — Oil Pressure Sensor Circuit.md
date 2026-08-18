---
aliases:
  - "Цепь датчика давления масла"
type: "Процедура"
doc: "87-fc135"
title_en: "Oil Pressure Sensor Circuit"
title_ru: "Цепь датчика давления масла"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc135.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc135.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Oil Pressure Sensor Circuit
**Цепь датчика давления масла**

> [!abstract] Процедура · `87-fc135`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc135.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc135.pdf)

### Fault Code: 135

### Oil Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 135 PID(P): P100 SPN: 100 FMI: 3 Lamp: Yellow SRT: | More than 4.88 VDC detected at the oil pressure sensor signal pin 33 of the engine harness. | Engine protection for oil pressure is disabled. |

![[19a00194.png]]

Oil Pressure Sensor Circuit

### Circuit Description

The oil pressure sensor monitors oil pressure and passes information to the electronic control module (ECM) through pin 33 of the engine harness.

The ECM monitors the voltage on pin 33 and expects to see the voltage vary between 0.5 and 4.5 VDC during normal engine operation.

Voltage above 4.88 VDC on pin 33 will trip Fault Code 135 and can be caused by short circuits in the supply, signal or return wires, an open in the return wire, or a failed sensor.

### Component Location

The oil pressure sensor is located on the left side of the engine block to the rear of the fuel pump.

### Shoptalk

- Does the fault occur **only** in cold weather? If so, allow the oil to warm up and see if the fault goes inactive.

- If Fault Code 143 or 415 is **not** present, the problem is **not** base engine related.

Refer to Troubleshooting Fault Code t05-135
