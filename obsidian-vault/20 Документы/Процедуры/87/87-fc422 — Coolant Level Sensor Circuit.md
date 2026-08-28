---
aliases:
  - "Цепь датчика уровня охлаждающей жидкости"
type: "Процедура"
doc: "87-fc422"
title_en: "Coolant Level Sensor Circuit"
title_ru: "Цепь датчика уровня охлаждающей жидкости"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc422.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc422.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Coolant Level Sensor Circuit
**Цепь датчика уровня охлаждающей жидкости**

> [!abstract] Процедура · `87-fc422`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc422.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc422.pdf)

### Fault Code: 422

### Coolant Level Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 422 PID(P): P111 SPN: 111 FMI: 2 Lamp: Yellow SRT: | Voltage detected simultaneously on both the coolant level high and low signal pins 27 and 37 of the engine harness, or no voltage detected on either pin. | Engine protection for coolant level is disabled. |

![[19a00217.png]]

Coolant Level Sensor Circuit

### Circuit Description

The coolant level sensor monitors the coolant level within the coolant system and passes information to the electronic control module (ECM) through the engine harness.

### Component Location

The coolant level sensor is located in the radiator top tank or surge tank.

### Shoptalk

This is an OEM-supplied component and will vary in sensor location.

- If a shorting plug is used in the coolant level circuit, verify that it is wired correctly.

- Inspect the wiring harness between the 4-pin Weather-Pack connector and the coolant level sensor for damage.

Refer to Troubleshooting Fault Code t05-422
