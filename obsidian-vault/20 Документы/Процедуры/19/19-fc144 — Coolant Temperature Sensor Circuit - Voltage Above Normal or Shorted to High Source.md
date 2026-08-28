---
aliases:
  - "Цепь датчика температуры ОЖ — напряжение выше нормы"
type: "Процедура"
doc: "19-fc144"
title_en: "Coolant Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика температуры ОЖ — напряжение выше нормы"
modified: "2010-08-19"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc144.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc144.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Coolant Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика температуры ОЖ — напряжение выше нормы**

> [!abstract] Процедура · `19-fc144`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-08-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc144.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc144.pdf)

### Fault Code: 144

### Coolant Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 144 PID(P): P110 SPN: 110 FMI: 3 Lamp: Yellow SRT: 00-355 | Coolant Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source | Possible white smoke. No engine protection for coolant temperature. Centinel system may be disabled. |

![[19400019.png]]

Coolant Temperature Sensor Circuit

### Circuit Description

The engine coolant temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The engine coolant temperature is used by the ECM for the engine protection system, timing, and fueling control.

### Component Location

Refer to Section E for a detailed component location view.

### Shoptalk

All temperature sensors:

| Temperature (°C) | Temperature (°F) | Resistance (ohms) |
|---|---|---|
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

The resistance of the sensor varies with temperature. The reading that you observe will compare to the table is the sensor is functioning properly.

Fault Code 144 can be caused by the following:

- Open in the signal or return wires

- Voltage short in the signal or return wires

- Failed temperature sensor.

Refer to Troubleshooting Fault Code t05-144
