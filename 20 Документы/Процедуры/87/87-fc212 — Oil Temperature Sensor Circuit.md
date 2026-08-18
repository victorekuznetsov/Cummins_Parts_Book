---
aliases:
  - "Цепь датчика температуры масла"
type: "Процедура"
doc: "87-fc212"
title_en: "Oil Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры масла"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc212.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc212.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Oil Temperature Sensor Circuit
**Цепь датчика температуры масла**

> [!abstract] Процедура · `87-fc212`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc212.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc212.pdf)

### Fault Code: 212

### Oil Temperature Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 212 PID(P): P175 SPN: 175 FMI: 3 Lamp: Yellow SRT: | High voltage detected at the oil temperature signal pin 35 of the engine harness. | No action is taken by the electronic control module (ECM). |

![[19802862.png]]

Oil Temperature Sensor Circuit

### Circuit Description

The oil temperature sensor monitors oil temperature and passes the information to the ECM through the engine harness.

### Component Location

The oil temperature sensor is located in the oil pan on the left side of the engine. The oil temperature sensor is **only** on engines with CENSE™.

### Shoptalk

The resistance of the sensor varies with the temperature. Compare the reading that you observe to the following table if the sensor is functioning properly.

| Temperature (°C) | Temperature \[°F\] | Resistance (ohms) |
|---|---|---|
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

Refer to Troubleshooting Fault Code t05-212
