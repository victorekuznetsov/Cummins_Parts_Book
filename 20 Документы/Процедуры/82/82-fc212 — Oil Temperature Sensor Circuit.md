---
aliases:
  - "Цепь датчика температуры масла"
type: "Процедура"
doc: "82-fc212"
title_en: "Oil Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры масла"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc212.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc212.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Oil Temperature Sensor Circuit
**Цепь датчика температуры масла**

> [!abstract] Процедура · `82-fc212`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc212.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc212.pdf)

### Fault Code: 212

### Oil Temperature Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 212 PID(P): P175 SPN: 175 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at the oil temperature circuit. | No engine protection for oil temperature. |

![[19c00506.png]]

Oil Temperature Sensor Circuit

### Circuit Description

The oil pressure/temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine oil. If the oil temperature becomes too high and the engine protection is enabled, a derate condition can be incurred, possibly leading to shutdown.

### Component Location

The oil pressure/temperature sensor is located on the engine block to the left of the fuel filter, behind the air compressor.

### Shoptalk

Sensor resistance varies with temperature. Compare your reading to this table:

| Temperature (°C) | Temperature \[°F\] | Resistance (ohms) |
|---|---|---|
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

Refer to Troubleshooting Fault Code t05-212
