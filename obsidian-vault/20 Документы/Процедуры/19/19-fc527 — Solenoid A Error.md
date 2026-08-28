---
aliases:
  - "Ошибка электромагнита A"
type: "Процедура"
doc: "19-fc527"
title_en: "Solenoid A Error"
title_ru: "Ошибка электромагнита A"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc527.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc527.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Solenoid A Error
**Ошибка электромагнита A**

> [!abstract] Процедура · `19-fc527`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc527.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc527.pdf)

### Fault Code: 527

### Solenoid A Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 527 PID(P): S40 SPN: 702 FMI: 3 Lamp: Yellow SRT: | The dual output A signal pin 1 of the OEM interface harness indicates an open or short circuit. | OEM-dependent. |

![[19400894.png]]

Solenoid A Circuit

### Circuit Description

The solenoid driver will control engine and vehicle functions by closing or opening a switched solenoid output, based on 11 selected engine parameters. The solenoid output will control functions such as a fan clutch, intake grid heater, air cleaner restriction indicator, or an oil filter differential pressure indicator.

### Component Location

The solenoid driver is an OEM device and the location of the solenoid is dependent upon the OEM.

Refer to Troubleshooting Fault Code t05-527
