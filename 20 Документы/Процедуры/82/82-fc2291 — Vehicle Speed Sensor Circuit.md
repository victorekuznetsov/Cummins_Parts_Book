---
aliases:
  - "Цепь датчика скорости машины"
type: "Процедура"
doc: "82-fc2291"
title_en: "Vehicle Speed Sensor Circuit"
title_ru: "Цепь датчика скорости машины"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc2291.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc2291.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Vehicle Speed Sensor Circuit
**Цепь датчика скорости машины**

> [!abstract] Процедура · `82-fc2291`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc2291.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc2291.pdf)

### Fault Code: 2291

### Vehicle Speed Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2291 PID(P): SPN: FMI: Lamp: Yellow SRT: | More than 0-mph vehicle speed detected when ICON™ is enabled. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. |

![[19803217.png]]

Integrated Idle ICON™ Circuit

### Circuit Description

The ECM monitors vehicle speed when ICON™ is enabled for safety violation. The ECM reviews data through the magnetic pickup. This fault code indicates that vehicle speed has been detected.

### Component Location

The vehicle speed sensor circuit is located on the vehicle transmission side.

### Shoptalk

This fault indicates a vehicle speed greater than 0 mph when ICON™ is enabled. Typically, a loose or faulty ground will generate noise in the vehicle speed sensor circuit.

Refer to Troubleshooting Fault Code t05-2291
