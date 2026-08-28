---
type: "Процедура"
doc: "19-fcmfc00"
title_en: "Multiple Fault Code A on the Engine Harness"
modified: "2010-08-19"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fcmfc00.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fcmfc00.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Multiple Fault Code A on the Engine Harness

> [!abstract] Процедура · `19-fcmfc00`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-08-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fcmfc00.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fcmfc00.pdf)

### Fault Code: Multiple A

### Multiple Fault Code A on the Engine Harness

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: Multiple A PID(P): SPN: FMI: Lamp: SRT: 00-381 | On engines without an electronic fuel pump, the supply voltage from pin 5 of the engine harness has: Failed internally in the ECM Been shorted to ground An open circuit external to the ECM. | Multiple fault codes. |

![[nobox.png]]

### Circuit Description

The ECM supplies all of the engine pressure sensors on the engine harness with +5 VDC from either pin 5 or pin 6. The ECM has common returns for all of the engine pressure sensors and all of the temperature sensors on either pin 17 or pin 18. A failure on either of these wires will cause multiple fault codes.

### Component Location

Refer to the engine diagrams.

### Shoptalk

Look for open circuits in the common supply and return wires and shorts from battery or ground to the supply and return wires or defective ECM power supply. A failed pressure sensor can cause multiple fault codes.

Refer to Troubleshooting Fault Code t05-mfc00
