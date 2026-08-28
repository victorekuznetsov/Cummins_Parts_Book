---
aliases:
  - "Множественный код неисправности A"
type: "Процедура"
doc: "81-fcmfc01"
title_en: "Multiple Fault Code A"
title_ru: "Множественный код неисправности A"
modified: "2011-03-17"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fcmfc01.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fcmfc01.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# Multiple Fault Code A
**Множественный код неисправности A**

> [!abstract] Процедура · `81-fcmfc01`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fcmfc01.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fcmfc01.pdf)

### Fault Code: Multiple A

### Multiple Fault Code A

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: Multiple PID(P): SPN: FMI: Lamp: SRT: 00-517 | Sensor power supply A01 is shorted to +24 VDC. | Multiple sensor Fault Codes 156, 212, and 694 simultaneously occur. |

![[19800624.png]]

Multiple Fault Code A

### Circuit Description

The electronic control module (ECM) supplies sensors on the CENSE™ harness with +5 VDC from either pin 01 or pin 02 on the ECM A connector. A failure on this circuit will cause multiple fault codes.

### Component Location

Consult the engine diagrams. Circuits that have an extension/sensor harness in addition to the main harness are to be tested and inspected as part of the “main harness.”

### Shoptalk

Look for open circuits, short circuits, or shorts to ground in the supply or return wires, or a defective ECM power supply.

A failed pressure sensor can cause multiple active fault codes to go inactive once the engine has been started.

Refer to Troubleshooting Fault Code t05-mfc01
