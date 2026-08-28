---
type: "Процедура"
doc: "19-fc261"
title_en: "Fuel Temperature - Engine Protection"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc261.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc261.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Fuel Temperature - Engine Protection

> [!abstract] Процедура · `19-fc261`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc261.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc261.pdf)

### Fault Code: 261

### Fuel Temperature - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 261 PID(P): P174 SPN: 174 FMI: 0 Lamp: Engine Protection SRT: 00-397 | High fuel temperature has been detected. Voltage signal at fuel temperature signal pin 26 of engine harness indicates fuel temperature above 71°C \[160°F\]. | Calibration-dependent progressive power and speed derate and engine shutdown with increasing time after alert. |

![[19800991.png]]

Fuel Temperature Sensor Circuit

### Circuit Description

The fuel temperature sensor is used by the ECM to monitor the temperature of the fuel. The ECM monitors the voltage on pin 26 and converts this voltage to a temperature value. The fuel temperature value is used by the ECM for the engine protection system.

### Component Location

QSK19 Series engines - The fuel temperature sensor is located on the left side of the control valve body, above the fuel shutoff valve. QSK45 and QSK60 Series engines - The fuel temperature sensor is located on the right side of the electronic control valve assembly between the rail and timing pressure sensors. QSK78 Series engines - The fuel temperature sensor is located on the right side of the electronic control valve assembly between the rail and timing pressure sensors.

### Shoptalk

All temperature sensors:

- The resistance of the sensor varies with the temperature. The reading that you observe could possibly compare to the following table if the sensor is functioning properly.

| Temperature(°C) | Temperature\[°F\] | Resistance(ohms) |
|---|---|---|
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

Refer to Troubleshooting Fault Code t05-261
