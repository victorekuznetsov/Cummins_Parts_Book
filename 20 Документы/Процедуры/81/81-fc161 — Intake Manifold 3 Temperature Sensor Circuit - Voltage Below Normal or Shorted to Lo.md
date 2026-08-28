---
aliases:
  - "Цепь датчика температуры коллектора 3 — напряжение ниже нормы"
type: "Процедура"
doc: "81-fc161"
title_en: "Intake Manifold 3 Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика температуры коллектора 3 — напряжение ниже нормы"
modified: "2018-10-15"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc161.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc161.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# Intake Manifold 3 Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика температуры коллектора 3 — напряжение ниже нормы**

> [!abstract] Процедура · `81-fc161`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc161.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc161.pdf)

### Fault Code: 161

### Intake Manifold 3 Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 161 PID(P): 105 SPN: 1132 FMI: 4 Lamp: Yellow SRT: 00-699 | Intake Manifold 3 Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source. Low voltage detected on SIGNAL pin-13 of the main harness A engine control module (ECM) connector. | Fault Code 162 is disabled. |

![[19800870.png]]

Intake Manifold 3 Temperature Sensor Circuit

### Circuit Description

The intake manifold 3 temperature sensor circuit provides the right bank front intake air temperature signal to the ECM. The resistance of the sensor varies with temperature. The ECM detects the change in resistance of the sensor by monitoring the voltage across an internal resistor that is in series with the sensor. The change in voltage across the internal resistor is translated into a temperature change.

### Component Location

The intake manifold 3 temperature sensor is located on the right bank front intake manifold. The sensor is located downstream of the aftercooler.

### Shoptalk

- The resistance of the sensor varies with the temperature. The reading that you observe should compare to the following table if the sensor is functioning properly.

| Temperature | Temperature | Resistance |
|---|---|---|
| (°C) | (°F) | (ohms) |
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

Refer to Troubleshooting Fault Code t05-161.
