---
aliases:
  - "Цепь датчика сопротивления на входе топлива"
type: "Процедура"
doc: "82-fc581"
title_en: "Fuel Inlet Restriction Sensor Circuit"
title_ru: "Цепь датчика сопротивления на входе топлива"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc581.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc581.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Fuel Inlet Restriction Sensor Circuit
**Цепь датчика сопротивления на входе топлива**

> [!abstract] Процедура · `82-fc581`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc581.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc581.pdf)

### Fault Code: 581

### Fuel Inlet Restriction Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 581 PID(P): P015 SPN: 1381 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected on fuel inlet restriction sensor signal pin. | Fuel inlet restriction monitor deactivated. |

![[19c00578.png]]

Fuel Inlet Restriction Sensor Circuit

### Circuit Description

The fuel inlet restriction sensor provides a fuel pressure signal to the electronic control module (ECM).

### Component Location

The fuel inlet restriction sensor is located on the fuel filter head.

### Shoptalk

This fault indicates that a short circuit of at least positive + 5 VDC has occurred at signal pin 28 on the actuator harness connector at the ECM.

Refer to Troubleshooting Fault Code t05-581
