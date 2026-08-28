---
aliases:
  - "Цепь датчика уровня охлаждающей жидкости"
type: "Процедура"
doc: "82-fc422"
title_en: "Coolant Level Sensor Circuit"
title_ru: "Цепь датчика уровня охлаждающей жидкости"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc422.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc422.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Coolant Level Sensor Circuit
**Цепь датчика уровня охлаждающей жидкости**

> [!abstract] Процедура · `82-fc422`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc422.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc422.pdf)

### Fault Code: 422

### Coolant Level Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 422 PID(P): P111 SPN: 111 FMI: 2/2 Lamp: Yellow SRT: | Voltage detected simultaneously on both the coolant level high and low signal circuits **or** no voltage detected on **both** circuits. | No engine protection for coolant level. |

![[19c00538.png]]

Coolant Level Sensor Circuit

### Circuit Description

The coolant level sensor monitors the coolant level within the coolant system and passes information to the electronic control module (ECM) through the sensor harness. This sensor is very complex. Do **not** use a multimeter to check the coolant level sensor. If the radiator coolant level drops below a certain level, a power derate will occur and become greater as time goes by.

### Component Location

The coolant level sensor is located in the radiator top tank or surge tank.

### Shoptalk

Possible causes for this fault code include:

- Open circuit

- Short circuit to ground

- Short circuit to another wire.

Refer to Troubleshooting Fault Code t05-422
