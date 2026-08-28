---
type: "Процедура"
doc: "19-fc499"
title_en: "Oil Level Sensor Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc499.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc499.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Oil Level Sensor Circuit

> [!abstract] Процедура · `19-fc499`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc499.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc499.pdf)

### Fault Code: 499

### Oil Level Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 499 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine oil level \#1 sensor signal - shorted low. | No engine protection for oil level. Centinel system is disabled. |

![[19803584.png]]

Oil Level Sensor Circuit

### Circuit Description

The oil level sensor is used by the electronic control module (ECM) to monitor the lubricating oil level. The ECM monitors the voltage on the oil level signal pin and converts this to an electronic value. The oil level value is used by the ECM for the engine protection system.

### Component Location

Refer to the Engine Diagrams in Section E of this manual for the component location.

### Shoptalk

Low voltage can be caused by an open circuit in the signal wire, a short to ground in the signal wire, a short to ground in the supply wire, an open circuit in the supply wire, or a faulty sensor.

A 4-pin oil level sensor will not trigger Fault Code 499.

Refer to Troubleshooting Fault Code t05-499
