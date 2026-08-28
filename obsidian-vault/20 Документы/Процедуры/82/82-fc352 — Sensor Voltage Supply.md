---
aliases:
  - "Питание датчиков"
type: "Процедура"
doc: "82-fc352"
title_en: "Sensor Voltage Supply"
title_ru: "Питание датчиков"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc352.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc352.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Sensor Voltage Supply
**Питание датчиков**

> [!abstract] Процедура · `82-fc352`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc352.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc352.pdf)

### Fault Code: 352

### Sensor Voltage Supply

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 352 PID(P): S232 SPN: 620 FMI: 4 Lamp: Yellow SRT: | Low voltage detected on the internal electronic control module (ECM) supply line to some of the sensors. | Engine is derated to no-air setting. |

![[19200188.png]]

Sensor Supply Circuit

### Circuit Description

The ECM supplies each of these sensors with +5 VDC. If the supply line to any sensor is damaged, the sensor will **not** work correctly.

### Component Location

There are two components involved in the sensor voltage supply: The intake manifold pressure sensor and the ambient air pressure sensor. The ambient air pressure sensor is located to the left of the ECM when looking at the side of the engine opposite of the intake manifold. The intake manifold pressure sensor is located on the topside of the air intake manifold toward the front of the engine.

### Shoptalk

Low voltage on the sensor +5-VDC supply line will be caused by a short to ground in a supply line, a short circuit between a supply line or a return line, a failed sensor, or a failed ECM power supply.

Refer to Troubleshooting Fault Code t05-352
