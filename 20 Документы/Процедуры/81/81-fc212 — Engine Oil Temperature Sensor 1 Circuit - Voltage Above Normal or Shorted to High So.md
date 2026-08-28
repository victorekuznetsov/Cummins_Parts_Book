---
aliases:
  - "Цепь датчика температуры масла 1 — напряжение выше нормы"
type: "Процедура"
doc: "81-fc212"
title_en: "Engine Oil Temperature Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика температуры масла 1 — напряжение выше нормы"
modified: "2015-07-07"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc212.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc212.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# Engine Oil Temperature Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика температуры масла 1 — напряжение выше нормы**

> [!abstract] Процедура · `81-fc212`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc212.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc212.pdf)

### Fault Code: 212

### Engine Oil Temperature Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 212 PID(P): 175 SPN: 175 FMI: 3 Lamp: Yellow SRT: 00-501 | Engine Oil Temperature Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected on SIGNAL pin 35 of the main harness A ECM connector. | Fault Code 214 is disabled. |

![[19802518.png]]

Oil Temperature Sensor Circuit

### Circuit Description

The oil temperature sensor circuit provides the oil temperature signal to the ECM. The resistance of the oil temperature sensor varies with temperature. The ECM detects the change in resistance of the oil temperature sensor by monitoring the voltage across an internal resistor that is in series with the oil temperature sensor. The change in voltage across the internal resistor is translated into a temperature change.

### Component Location

The oil temperature sensor is located on the right side of the oil pan.

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

Refer to Troubleshooting Fault Code t05-212
