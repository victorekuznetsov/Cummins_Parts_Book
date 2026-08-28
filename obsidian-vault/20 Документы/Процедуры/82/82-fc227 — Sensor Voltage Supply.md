---
aliases:
  - "Питание датчиков"
type: "Процедура"
doc: "82-fc227"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc227.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc227.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Sensor Voltage Supply
**Питание датчиков**

> [!abstract] Процедура · `82-fc227`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc227.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc227.pdf)

### Fault Code: 227

### Sensor Voltage Supply

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 227 PID(P): S232 SPN: 620 FMI: 3 Lamp: Yellow SRT: | High voltage detected on the electronic control module (ECM) voltage supply line to some sensors. (VSEN 2) | Engine will run derated. No engine protection for oil pressure and coolant level. |

![[19200194.png]]

Sensor Supply Voltage Circuit

### Circuit Description

The ECM supplies each of these sensors with + 5 VDC. If the supply wire to any sensor is damaged, the sensor will **not** work correctly.

Note: In the above picture, the circuits for the wet tank pressure sensor/air compressor and Top 2 Gear Position wires are labeled differently on the industrial wiring diagram. The equivalent differences in the industrial labels are as follows:

- Wet Tank Pressure Sensor + 5-Volt Supply = OEM Pressure Supply (Pins 1 to 18)

- Wet Tank Pressure Signal = OEM Pressure Signal (Pins 3 to 19)

- Wet Tank Pressure Return = OEM Pressure Return (Pins 2 to 20)

- Air Compressor Actuator = Switched Output A (Pins 5 to 14)

- Air Compressor Return = Spare (Pins 6 to 11)

- Top 2 Gear Position + 5-Volt Supply = Spare (Pins 14 to 19)

- Top 2 Gear Position Input = Spare (Pins 15 to 18)

- Top 2 Gear Position Return = Spare (Pins 16 to 17)

### Component Location

Fuel inlet restriction sensor is located on the fuel pump inlet.

Oil pressure/temperature sensor is located in front of the air compressor.

Oil level sensor is located in the oil pan.

Wet tank pressure sensor is located on the air compressor.

Coolant level sensor. Refer to OEM for proper location.

Top 2 transmission position sensor - located on the transmission if vehicle has a Spicer™ Top 2 Automate transmission. Refer to OEM for proper location.

### Shoptalk

High voltage on the sensor + 5-VDC supply line will be caused by a short to battery in the supply line or a short between an actuator wire and the supply wire.

Refer to Troubleshooting Fault Code t05-227
