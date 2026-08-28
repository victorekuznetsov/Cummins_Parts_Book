---
aliases:
  - "Датчик температуры впускного коллектора — защита двигателя"
type: "Процедура"
doc: "19-fc155"
title_en: "Intake Manifold Temperature Sensor - Engine Protection"
title_ru: "Датчик температуры впускного коллектора — защита двигателя"
modified: "2010-08-01"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc155.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc155.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Intake Manifold Temperature Sensor - Engine Protection
**Датчик температуры впускного коллектора — защита двигателя**

> [!abstract] Процедура · `19-fc155`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-08-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc155.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc155.pdf)

### Fault Code: 155

### Intake Manifold Temperature Sensor - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 155 PID(P): P105 SPN: 105 FMI: 0 Lamp: Engine Protection SRT: 00-360 | High intake air manifold temperature has been detected. Voltage signal at intake manifold air temperature signal pin 23 indicates intake manifold air temperature above 104°C \[219°F\]. | Calibration-dependent progressive power and speed derate and engine shutdown as the temperature increases over thresholds. |

![[19400062.png]]

Intake Manifold Temperature Sensor Circuit

### Circuit Description

The intake manifold temperature sensor is used by the ECM to monitor the temperature of the air in the intake manifold after the aftercooler. The intake manifold temperature sensor is used by the ECM for the engine protection system, timing, and fueling control. The ECM monitors the voltage on pin 23. The ECM expects to see the voltage vary between 0.5 and 4.5-VDC. If the voltage is below 0.5-VDC, the ECM will log Fault Code 155. Voltage below 0.5-VDC on pin 23 can be caused by a cooling system malfunction or an in-range sensor malfunction.

### Component Location

QSK19 series engines - The intake manifold temperature sensor is located above the fuel pump, next to the intake manifold pressure sensor.

### Shoptalk

The following chart shows resistance of the intake manifold temperature sensor at various temperature readings.

| Temperature(°C) | Temperature\[°F\] | Resistance(ohms) |
|---|---|---|
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

Refer to Troubleshooting Fault Code 155.
