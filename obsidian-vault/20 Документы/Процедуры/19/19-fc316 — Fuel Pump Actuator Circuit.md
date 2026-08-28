---
type: "Процедура"
doc: "19-fc316"
title_en: "Fuel Pump Actuator Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc316.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc316.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Fuel Pump Actuator Circuit

> [!abstract] Процедура · `19-fc316`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc316.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc316.pdf)

### Fault Code: 316

### Fuel Pump Actuator Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 316 PID(P): S78 SPN: 931 FMI: 3 Lamp: Yellow SRT: 00-670 | Fuel pump actuator circuit is open, or supply pin 11 is shorted to battery voltage or ground, or return pin 40 is shorted to battery voltage or ground in the engine harness. | No action by the ECM is taken. Actuator is open or closed, or partially closed. |

![[19800999.png]]

Fuel Pump Actuator Circuit

### Circuit Description

The fuel pump actuator circuit supplies current to the fuel pump actuator. The ECM commands a varying amount of current to the fuel pump actuator to control the fuel pump output pressure to the control valve assembly.

### Component Location

The fuel pump actuator is located on the fuel pump.

### Shoptalk

- Confirm that the actuator connector is firmly in place.

- When there is no power to the actuator, the actuator closes and fuel flow continues.

Refer to Troubleshooting Fault Code t05-316
