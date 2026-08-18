---
aliases:
  - "Цепь датчика температуры охлаждающей жидкости"
type: "Процедура"
doc: "82-fc144"
title_en: "Coolant Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры охлаждающей жидкости"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc144.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc144.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Coolant Temperature Sensor Circuit
**Цепь датчика температуры охлаждающей жидкости**

> [!abstract] Процедура · `82-fc144`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc144.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc144.pdf)

### Fault Code: 144

### Coolant Temperature Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 144 PID(P): P110 SPN: 110 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at the coolant temperature circuit. | Possible white smoke. Fan will stay on if controlled by the electronic control module (ECM). No engine protection for coolant temperature. |

![[19200133.png]]

Coolant Temperature Sensor Circuit

### Circuit Description

The coolant temperature sensor is used by the ECM to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system, timing, and fueling control.

### Component Location

The coolant temperature sensor is located in front of the turbocharger.

### Shoptalk

The resistance of the sensor varies with the temperature. Compare your reading to this table:

| Temperature (°C) | Temperature \[°F\] | Resistance (ohms) |
|---|---|---|
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

Refer to Troubleshooting Fault Code t05-144
