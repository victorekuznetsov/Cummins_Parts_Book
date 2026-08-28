---
aliases:
  - "Питание датчиков"
type: "Процедура"
doc: "82-fc187"
title_en: "Sensor Voltage Supply"
title_ru: "Питание датчиков"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc187.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc187.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Sensor Voltage Supply
**Питание датчиков**

> [!abstract] Процедура · `82-fc187`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc187.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc187.pdf)

### Fault Code: 187

### Sensor Voltage Supply

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 187 PID(P): S232 SPN: 620 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected on the ECM voltage supply line to some sensors (VSEN 2 supply). | Engine will run derated. No engine protection for oil pressure or coolant level. |

![[19200194.png]]

Sensor Supply Voltage Circuit

### Circuit Description

The ECM supplies each of these sensors with +5-VDC. If the supply line to any sensor is damaged, the sensor will **not** work correctly.

### Component Location

Fuel inlet restriction sensor is located on the fuel pump inlet.

Oil pressure/temperature sensor is located in front of the air compressor.

Oil level sensor is located in the oil pan.

Wet tank pressure sensor is located on the air compressor

Coolant level sensor. Refer to the OEM manual for proper location.

Top 2 transmission position sensor - located on the transmission if vehicle has a Spicer™ Top 2 Automate transmission. Refer to the OEM manual for proper location.

### Shoptalk

Low voltage on the sensor + 5-volt supply line will be caused by a short to ground in a supply line, a short circuit between a supply line or a return line, a failed sensor, or a failed ECM power supply.

During the fault code response test outlined for each sensor connected to sensor supply number 2, Fault Code 187 **must** be active before unplugging each sensor. If the fault code is **not** active, but can be easily duplicated by operating the engine, the following can be performed:

- Operate the engine under the conditions that will cause Fault Code 187 to become active, even if it logs for a short period of time, unplug one sensor at a time until Fault Code 187 stops logging under the test conditions. Each sensor can be unplugged with the engine running. Note: The engine may **not** start if the camshaft position sensor is unplugged.

Refer to Troubleshooting Fault Code t05-187
