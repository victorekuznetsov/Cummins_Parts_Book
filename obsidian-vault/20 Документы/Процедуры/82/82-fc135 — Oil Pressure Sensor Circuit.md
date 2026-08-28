---
aliases:
  - "Цепь датчика давления масла"
type: "Процедура"
doc: "82-fc135"
title_en: "Oil Pressure Sensor Circuit"
title_ru: "Цепь датчика давления масла"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc135.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc135.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Oil Pressure Sensor Circuit
**Цепь датчика давления масла**

> [!abstract] Процедура · `82-fc135`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc135.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc135.pdf)

### Fault Code: 135

### Oil Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 135 PID(P): P100 SPN: 100 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at the oil pressure circuit. | No engine protection for oil pressure. |

![[19c00506.png]]

Oil Pressure Sensor Circuit

### Circuit Description

The oil pressure/temperature sensor is used by the electronic control module (ECM) to monitor the lubricating oil pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The oil pressure value is used by the ECM for the engine protection system.

### Component Location

The oil pressure/temperature sensor is located on the engine block to the left of the fuel filter, behind the air compressor.

### Shoptalk

Does the fault occur **only** in cold weather? If so, allow the oil to warm up and see if the fault goes inactive.

Refer to Troubleshooting Fault Code t05-135
