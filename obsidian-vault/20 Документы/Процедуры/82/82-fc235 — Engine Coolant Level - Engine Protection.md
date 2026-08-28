---
aliases:
  - "Уровень охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "82-fc235"
title_en: "Engine Coolant Level - Engine Protection"
title_ru: "Уровень охлаждающей жидкости — защита двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc235.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc235.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Engine Coolant Level - Engine Protection
**Уровень охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `82-fc235`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc235.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc235.pdf)

### Fault Code: 235

### Engine Coolant Level - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 235 PID(P): P111 SPN: 111 FMI: 1/1 Lamp: Red SRT: | Coolant level signal at pin 22 of the sensor harness connector indicates coolant level is below the normal range. | Progressive power and speed derate with increasing time after alert. If engine protection shutdown is enabled, engine will shut down 30 seconds after the engine protection lamp starts flashing. |

![[19c00538.png]]

Engine Coolant Level - Engine Protection

### Circuit Description

The coolant level sensor monitors the coolant level within the coolant system and passes information to the electronic control module (ECM) through the engine harness. Because this sensor is complex, do **not** use a multimeter to check it. If the radiator coolant level drops below a certain level, a progressive power and/or speed derate will occur. Engine can shut down if the engine protection shutdown feature is enabled.

### Component Location

The coolant level sensor is located in the radiator top tank or surge tank.

### Shoptalk

This is an OEM-supplied component and can vary in location.

- If a shorting plug is used in the coolant level circuit, verify that it is wired correctly.

- Inspect the wiring harness between the Weather-Pack four-way connector and the coolant level sensor for damage.

- Make sure the coolant level sensor is located in the middle of the tank rather than off to one side where the coolant level can change when the vehicle turns a corner.

Refer to Troubleshooting Fault Code t05-235
