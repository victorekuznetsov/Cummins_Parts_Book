---
aliases:
  - "Цепь датчика уровня масла в картере"
type: "Процедура"
doc: "82-fc472"
title_en: "Crankcase Oil Level Sensor Circuit"
title_ru: "Цепь датчика уровня масла в картере"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc472.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc472.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Crankcase Oil Level Sensor Circuit
**Цепь датчика уровня масла в картере**

> [!abstract] Процедура · `82-fc472`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc472.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc472.pdf)

### Fault Code: 472

### Crankcase Oil Level Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 472 PID(P): S017 SPN: 1380 FMI: 2/2 Lamp: Maintenance SRT: | Either high or low voltage detected on the crankcase oil level sensor circuit by the electronic control module (ECM). | None on performance. Centinel™ system deactivated. |

![[19c00362.png]]

Crankcase Oil Level Sensor Circuit

### Circuit Description

The crankcase oil level sensor is used by the ECM to monitor the lubricating oil level. The ECM monitors the voltage on the signal pin and converts this to an electronic value. The oil level value is used by the ECM for the engine protection system.

### Component Location

The oil level sensor is located in the side of the oil pan on the exhaust side of the engine.

### Shoptalk

Low voltage can be caused by an open circuit in the signal wire, a short circuit to ground in the signal wire, a short circuit to ground of the supply wire, an open circuit in the supply wire, or a faulty sensor.

High voltage can be caused by the signal wire shorting to another wire in the harness, an open circuit in the return wire, or a faulty sensor.

Refer to Troubleshooting Fault Code t05-472
