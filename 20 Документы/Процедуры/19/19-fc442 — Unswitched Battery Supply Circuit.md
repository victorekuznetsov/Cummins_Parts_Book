---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "19-fc442"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc442.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc442.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `19-fc442`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc442.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc442.pdf)

### Fault Code: 442

### Unswitched Battery Supply Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 442 PID(P): P168 SPN: 168 FMI: 0 Lamp: Yellow SRT: 00-373 | More than 38.0-VDC battery voltage detected at the ECM. | ECM damage will occur. |

![[19400081.png]]

Unswitched Battery Supply Circuit

### Circuit Description

The ECM receives unswitched battery voltage through the OEM harness and engine harness. There are two in-line 10-amp fuses in the unswitched battery wire of the OEM interface harness to protect the ECM. The battery return wires in the engine harness are connected to the engine block ground.

### Component Location

The location of the battery will vary with the OEM. Refer to the OEM manual for the battery location.

### Shoptalk

Improper wiring of the battery circuit is the most likely cause of this fault.

Refer to Troubleshooting Fault Code t05-442
