---
aliases:
  - "Цепь датчика температуры коллектора 2 — напряжение выше нормы"
type: "Процедура"
doc: "81-fc156"
title_en: "Intake Manifold 2 Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика температуры коллектора 2 — напряжение выше нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc156.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc156.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# Intake Manifold 2 Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика температуры коллектора 2 — напряжение выше нормы**

> [!abstract] Процедура · `81-fc156`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc156.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc156.pdf)

### Fault Code: 156

### Intake Manifold 2 Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 156 PID(P): 105 SPN: 1131 FMI: 3 Lamp: Yellow SRT: 00-696 | Intake Manifold 2 Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected on SIGNAL pin 06 of the main harness A ECM connector. | Fault Code 158 is disabled. |

![[19800776.png]]

Left Bank Rear Intake Manifold Temperature Sensor Circuit

### Circuit Description

The left bank rear intake manifold temperature sensor provides the left bank rear intake manifold air temperature signal to the CENSE™ ECM.

### Component Location

The left bank rear intake manifold temperature sensor is located on the left bank rear intake manifold. The sensor is located downstream of the aftercooler.

### Shoptalk

- The resistance of the sensor varies with temperature. The reading that you observe should compare to the following table if the sensor is functioning properly.

| Temperature | Temperature | Resistance |
|---|---|---|
| (°C) | (°F) | (ohms) |
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

Refer to Troubleshooting Fault Code t05-156
