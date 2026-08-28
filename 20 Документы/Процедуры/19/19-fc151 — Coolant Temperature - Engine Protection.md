---
aliases:
  - "Температура охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "19-fc151"
title_en: "Coolant Temperature - Engine Protection"
title_ru: "Температура охлаждающей жидкости — защита двигателя"
modified: "2011-03-01"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc151.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc151.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Coolant Temperature - Engine Protection
**Температура охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `19-fc151`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc151.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc151.pdf)

### Fault Code: 151

### Coolant Temperature - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 151 PID(P): P110 SPN: 110 FMI: 0 Lamp: Engine Protection SRT: 00-357 | High coolant temperature has been detected. Voltage signal at coolant temperature signal pin 22 indicates the coolant temperature is above 100°C \[212°F\]. | Calibration-dependent progressive power and speed derate and engine shutdown as temperature increases over thresholds. Centinel™ system is disabled. |

![[19400019.png]]

Coolant Temperature Sensor Circuit

### Circuit Description

The coolant temperature sensor is used by the ECM to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system, timing, and fueling control. The ECM monitors the voltage on pin 22. The ECM expects to see the voltage vary between 0.21 and 4.95 VDC. If the voltage is below 0.21 VDC for more than 2 seconds, then the ECM will log Fault Code 151. Voltage below 0.21 VDC on pin 22 can be caused by a cooling system failure or an in-range sensor failure.

### Component Location

QSK19 series engines - The coolant temperature sensor is located on the side of the thermostat housing on most applications.

### Shoptalk

- Make sure the airflow through the radiator is **not** obstructed.

- The resistance of all the temperature sensors varies with the temperature. The reading that you observe could possibly compare to the following table if the sensor is functioning properly.

| Temperature(°C) | Temperature\[°F\] | Resistance(ohms) |
|---|---|---|
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

Refer to Troubleshooting Fault Code t05-151
