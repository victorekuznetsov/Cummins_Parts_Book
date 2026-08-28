---
type: "Процедура"
doc: "19-fc225"
title_en: "Make-Up Valve Solenoid Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc225.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc225.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Make-Up Valve Solenoid Circuit

> [!abstract] Процедура · `19-fc225`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc225.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc225.pdf)

### Fault Code: 225

### Make-Up Valve Solenoid Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 225 PID(P): S85 SPN: 1266 FMI: 4 Lamp: Yellow SRT: | The Centinel™ make-up valve solenoid circuit is open or shorted. Less than 18.0 VDC detected at Centinel™ make-up valve solenoid supply pin 2 of the engine harness or resistance of the solenoid has dropped below 80 ohms. | ECM turns off the Centinel™ make-up valve supply voltage and the Centinel™ system is disabled. |

![[19400728.png]]

Make-Up Valve Solenoid Circuit

### Circuit Description

The make-up valve solenoid controls the flow of oil within the oil control valve during the make-up cycle.

### Component Location

The make-up valve solenoid is located on top of the oil control valve.

Refer to Troubleshooting Fault Code t05-225
