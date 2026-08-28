---
aliases:
  - "Цепь датчика температуры ОЖ — напряжение выше нормы"
type: "Процедура"
doc: "07-fc144"
title_en: "Coolant Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика температуры ОЖ — напряжение выше нормы"
modified: "2012-12-18"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc144.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc144.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Coolant Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика температуры ОЖ — напряжение выше нормы**

> [!abstract] Процедура · `07-fc144`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc144.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc144.pdf)

### Fault Code: 144

### Coolant Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 144 PID(P): P110 SPN: 110 FMI: 3 Lamp: Amber SRT: | Coolant temperature sensor circuit - voltage above normal or shorted to high source. | Engine protection for coolant temperature is disabled. Possible white smoke. |

![[19900358.png]]

Coolant Temperature Sensor Circuit

### Circuit Description

The coolant temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system, timing, and fueling control.

### Component Location

Reference Section E for a detailed component location view. The coolant temperature sensor is located in the thermostat housing.

### Shoptalk

The resistance of the sensor varies with the temperature. The reading observed will compare to the following table if the sensor is functioning properly.

| Temperature (°F) | Temperature (°C) | Resistance (ohms) |
|---|---|---|
| 32 | 0 | 30k to 36k |
| 77 | 25 | 9k to 11k |
| 122 | 50 | 3k to 4k |
| 167 | 75 | 1350 to 1500 |
| 212 | 100 | 600 to 675 |

Refer to Troubleshooting Fault Code t05-144
