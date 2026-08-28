---
aliases:
  - "Цепь датчика сопротивления на входе топлива"
type: "Процедура"
doc: "82-fc583"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc583.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc583.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Fuel Inlet Restriction Sensor Circuit
**Цепь датчика сопротивления на входе топлива**

> [!abstract] Процедура · `82-fc583`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc583.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc583.pdf)

### Fault Code: 583

### Fuel Inlet Restriction Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 583 PID(P): P015 SPN: 1381 FMI: 1/18 Lamp: Yellow SRT: | Restriction has been detected by the fuel inlet restriction sensor. | Fuel inlet restriction monitor warning is set. |

![[19c00578.png]]

Fuel Inlet Restriction Sensor Circuit

### Circuit Description

The fuel inlet restriction sensor provides a signal to the electronic control module (ECM).

### Component Location

The fuel inlet restriction sensor is located on the inlet to the fuel filter head.

### Shoptalk

This fault indicates that the fuel inlet restriction has exceeded 12 in Hg. Typical causes for this fault code include a plugged fuel filter and a collapsed fuel supply hose.

Refer to Troubleshooting Fault Code t05-583
