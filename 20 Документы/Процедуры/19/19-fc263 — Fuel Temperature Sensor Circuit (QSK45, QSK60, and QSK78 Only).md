---
type: "Процедура"
doc: "19-fc263"
title_en: "Fuel Temperature Sensor Circuit (QSK45, QSK60, and QSK78 Only)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc263.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc263.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Fuel Temperature Sensor Circuit (QSK45, QSK60, and QSK78 Only)

> [!abstract] Процедура · `19-fc263`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc263.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc263.pdf)

### Fault Code: 263

### Fuel Temperature Sensor Circuit (QSK45, QSK60, and QSK78 Only)

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 263 PID(P): P174 SPN: 174 FMI: 3 Lamp: Yellow SRT: 00-398 | More than 4.95 VDC detected at the fuel temperature signal pin 26 of the engine harness. | No engine protection for fuel temperature. |

![[19800991.png]]

Fuel Temperature Sensor Circuit

### Circuit Description

The fuel temperature sensor is used by the ECM to monitor the temperature of the fuel. The fuel temperature is used by the ECM for the engine protection system, timing, and fueling control. The ECM monitors the voltage on pin 26. The ECM expects to see the voltage vary between 0.5 and 4.5 VDC. If the voltage is above 4.95 VDC, then the ECM will log Fault Code 263. Voltage above 4.95 VDC on pin 26 can be caused by an open in the signal or return wires, or voltage shorts to the signal or return wires, or a failed open sensor.

### Component Location

QSK19 series engines - The fuel temperature sensor is located on the left side of the control valve body, above the fuel shutoff valve.

QSK45 and QSK60 series engines - The fuel temperature sensor is located on the right side of the electronic control valve assembly between the rail and timing pressure sensors.

QSK78 series engines - The fuel temperature sensor is located on the right side of the electronic control valve assembly between the rail and timing pressure sensors.

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

Refer to Troubleshooting Fault Code t05-263
