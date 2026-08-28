---
aliases:
  - "Цепь датчика атмосферного давления"
type: "Процедура"
doc: "82-fc222"
title_en: "Ambient Air Pressure Sensor Circuit"
title_ru: "Цепь датчика атмосферного давления"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc222.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc222.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Ambient Air Pressure Sensor Circuit
**Цепь датчика атмосферного давления**

> [!abstract] Процедура · `82-fc222`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc222.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc222.pdf)

### Fault Code: 222

### Ambient Air Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 222 PID(P): P108 SPN: 108 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected at the ambient air pressure circuit. | Derate in power output of engine. |

![[19c00652.png]]

Ambient Air Pressure Sensor Circuit

### Circuit Description

The ambient air pressure sensor monitors atmospheric pressure and passes information to the electronic control module (ECM) through the sensor harness.

### Component Location

The ambient air pressure sensor is located below the ECM.

### Shoptalk

Monitor the ambient air pressure reading with a service tool to confirm that the pressure reading matches the actual air pressure.

Refer to Troubleshooting Fault Code t05-222
