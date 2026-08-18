---
aliases:
  - "Цепь датчика давления охлаждающей жидкости"
type: "Процедура"
doc: "87-fc232"
title_en: "Coolant Pressure Sensor Circuit"
title_ru: "Цепь датчика давления охлаждающей жидкости"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc232.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc232.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Coolant Pressure Sensor Circuit
**Цепь датчика давления охлаждающей жидкости**

> [!abstract] Процедура · `87-fc232`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc232.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc232.pdf)

### Fault Code: 232

### Coolant Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 232 PID(P): P102 SPN: 102 FMI: 4 Lamp: Yellow SRT: | Less than 0.30 VDC detected at the coolant pressure sensor signal pin 24 of the engine harness. | Engine protection for coolant pressure is disabled. |

![[19a00215.png]]

Coolant Pressure Sensor Circuit

### Circuit Description

The coolant pressure sensor monitors coolant pressure and passes information to the electronic control module (ECM) through pin 24 of the engine harness. The ECM monitors the voltage on pin 24 and expects to see the voltage vary between 0.5 and 4.5 VDC during normal engine operation. Voltage below 0.30 VDC on pin 24 will result in Fault Code 232.

### Component Location

The coolant pressure sensor is located on the left side of the engine in the thermostat housing.

### Shoptalk

- Confirm that the radiator cap is installed correctly.

- Check the radiator cap for proper operation.

Refer to Troubleshooting Fault Code t05-232
