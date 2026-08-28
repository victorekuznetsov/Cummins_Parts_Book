---
aliases:
  - "Цепь датчика давления охлаждающей жидкости"
type: "Процедура"
doc: "87-fc231"
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
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc231.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc231.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Coolant Pressure Sensor Circuit
**Цепь датчика давления охлаждающей жидкости**

> [!abstract] Процедура · `87-fc231`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc231.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc231.pdf)

### Fault Code: 231

### Coolant Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 231 PID(P): P109 SPN: 109 FMI: 3 Lamp: Yellow SRT: | More than 4.69 VDC detected at the coolant pressure sensor signal pin 24 of the engine harness. | Engine protection for coolant pressure is disabled. |

![[19a00215.png]]

Coolant Pressure Sensor Circuit

### Circuit Description

The coolant pressure sensor monitors coolant pressure and passes information to the electronic control module (ECM) through pin 24 of the engine harness. The ECM monitors the voltage on pin 24 and expects to see the voltage vary between 0.5 and 4.5 VDC during normal engine operation. Voltage above 4.69 VDC on pin 24 will trip Fault Code 231 and can be caused by short circuits in the supply, signal, or return wires, an open in the return wire, or a failed sensor. Voltage below 0.30 VDC on pin 24 will trip Fault Code 232.

### Component Location

The coolant pressure sensor is located on the left side of the engine in the thermostat housing.

### Shoptalk

- Confirm that the radiator cap is installed correctly.

- Check the radiator cap for proper operation.

Refer to Troubleshooting Fault Code t05-231
