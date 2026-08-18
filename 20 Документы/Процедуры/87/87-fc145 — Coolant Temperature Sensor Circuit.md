---
aliases:
  - "Цепь датчика температуры охлаждающей жидкости"
type: "Процедура"
doc: "87-fc145"
title_en: "Coolant Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры охлаждающей жидкости"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc145.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc145.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Coolant Temperature Sensor Circuit
**Цепь датчика температуры охлаждающей жидкости**

> [!abstract] Процедура · `87-fc145`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc145.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc145.pdf)

### Fault Code: 145

### Coolant Temperature Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 145 PID(P): P110 SPN: 110 FMI: 4 Lamp: Yellow SRT: | Less than 0.21 VDC detected at the coolant temperature signal pin 23 of the engine harness. | Engine protection for coolant temperature is disabled. |

![[19900358.png]]

Coolant Temperature Sensor Circuit

### Circuit Description

The coolant temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system, timing, and fueling control.

The ECM monitors the voltage on pin 23. The ECM expects to see the voltage vary between 0.5 and 4.5 VDC. If the voltage is below 0.21 VDC for more than 2 seconds, then the ECM will log Fault Code 145.

Voltage below 0.21 VDC on pin 23 can be caused by short circuits to ground on the supply or return wires, or an internally grounded, failed sensor.

### Component Location

The coolant temperature sensor is located on the left side of the engine in the thermostat housing.

### Shoptalk

All temperature sensors:

- The resistance of the sensor varies with the temperature. The reading you observe will compare to the following table if the sensor is functioning properly.

| Temperature (°C) | Temperature \[°F\] | Resistance (ohms) |
|---|---|---|
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

Refer to Troubleshooting Fault Code t05-145
