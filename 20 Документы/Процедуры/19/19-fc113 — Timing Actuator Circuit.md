---
type: "Процедура"
doc: "19-fc113"
title_en: "Timing Actuator Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc113.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc113.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Timing Actuator Circuit

> [!abstract] Процедура · `19-fc113`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc113.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc113.pdf)

### Fault Code: 113

### Timing Actuator Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 113 PID(P): S20 SPN: 635 FMI: 3 Lamp: Yellow SRT: 00-343 | Timing actuator circuit is open, or supply pin 1 is shorted to ground, or return pin 20 is shorted to battery voltage. | No action by the ECM is taken. Actuator is closed or partially closed. Engine exhausts white smoke and loses power. Fault Code 112 can possibly be logged. |

![[19400028.png]]

Timing Actuator Circuit

### Circuit Description

The timing actuator circuit supplies current to the timing actuator. The ECM commands a varying amount of current to the timing actuator to control the amount of timing pressure to the injectors.

### Component Location

The timing actuator is located on the top of the control valve body, toward the front of the engine and behind the ECM.

### Shoptalk

- Confirm that the actuator connector is firmly in place.

- When there is no power to the actuator, the actuator closes and timing flow stops. This can cause Fault Code 112, timing fueling flow mismatch.

Refer to Troubleshooting Fault Code t05-113
