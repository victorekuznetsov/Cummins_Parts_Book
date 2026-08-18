---
aliases:
  - "Цепь датчика давления и температуры масла"
type: "Процедура"
doc: "82-fc141"
title_en: "Engine Oil Pressure/Temperature Sensor Circuit"
title_ru: "Цепь датчика давления и температуры масла"
modified: "2015-08-07"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Engine Oil Pressure/Temperature Sensor Circuit
**Цепь датчика давления и температуры масла**

> [!abstract] Процедура · `82-fc141`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-08-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc141.pdf)

### Fault Code: 141

### Engine Oil Pressure/Temperature Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 141 PID(P): P100 SPN: 100 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected at the oil pressure circuit. | No engine protection for oil pressure. |

![[19c00506.png]]

Oil Pressure Sensor Circuit

### Circuit Description

The oil pressure/temperature sensor is used by the electronic control module (ECM) to monitor the lubricating oil pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The oil pressure value is used by the ECM for the engine protection system.

### Component Location

The oil pressure/temperature sensor is located on the engine block to the left of the fuel filter, behind the air compressor.

### Shoptalk

If Fault Code 143 or 415 is present, the problem is probably base engine related.

Refer to Troubleshooting Fault Code t05-141
