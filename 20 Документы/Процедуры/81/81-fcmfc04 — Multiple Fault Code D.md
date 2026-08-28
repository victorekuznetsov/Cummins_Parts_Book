---
type: "Процедура"
doc: "81-fcmfc04"
title_en: "Multiple Fault Code D"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fcmfc04.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fcmfc04.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# Multiple Fault Code D

> [!abstract] Процедура · `81-fcmfc04`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fcmfc04.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fcmfc04.pdf)

### Fault Code: Multiple D

### Multiple Fault Code D

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: Multiple PID(P): SPN: FMI: Lamp: SRT: 00-517 | One of the two sensor power supply or sensor return wires is shorted to ground, or has an open circuit. | Multiple sensor Fault Codes 129, 137, 161, 164, and 2155 simultaneously occur. |

![[19800629.png]]

Multiple Fault Code D

### Circuit Description

The electronic control module (ECM) supplies sensors on the CENSE™ harness with +5 VDC from either pin 01 or pin 02 on the ECM A connector. The ECM has common returns for all pressure sensors on pin 33 of the ECM B connector. A failure on this circuit will cause multiple fault codes.

### Component Location

Consult the engine diagrams. Circuits that have an extension/sensor harness in addition to the main harness are to be tested and inspected as part of the “main harness.”

### Shoptalk

Look for open circuits, short circuits, or shorts to ground in the supply or return wires, or a defective ECM power supply.

A failed pressure sensor can cause multiple active fault codes to go inactive once the engine has been started.

Refer to Troubleshooting Fault Code t05-mfc04
