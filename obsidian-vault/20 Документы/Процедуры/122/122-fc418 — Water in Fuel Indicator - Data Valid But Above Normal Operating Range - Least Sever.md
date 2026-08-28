---
aliases:
  - "Индикатор воды в топливе выше нормы — низший уровень"
type: "Процедура"
doc: "122-fc418"
title_en: "Water in Fuel Indicator - Data Valid But Above Normal Operating Range - Least Severe Level"
title_ru: "Индикатор воды в топливе выше нормы — низший уровень"
modified: "2015-11-17"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc418.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc418.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Water in Fuel Indicator - Data Valid But Above Normal Operating Range - Least Severe Level
**Индикатор воды в топливе выше нормы — низший уровень**

> [!abstract] Процедура · `122-fc418`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-11-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc418.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc418.pdf)

### Fault Code: 418

### Water in Fuel Indicator - Data Valid But Above Normal Operating Range - Least Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 418 PID(P): SPN: 97 FMI: 0/15 Lamp: Maintenance SRT: | Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Least Severe Level. Water has been detected in the fuel filter. | Possible white smoke, loss of power, or hard starting. |

![[19602251.png]]

QSK38 CM2150 Industrial/QSK38 CM2150 Marine with C Command™ Panel System - Water in Fuel Indicator Sensor Circuit

![[19602252.png]]

QSK38 CM2150 Marine with C Command Elite™ and C Command Elite Plus™ Panel System - Water in Fuel Indicator Sensor Circuit

![[19602253.png]]

QSK50 CM2150 Industrial - Water in Fuel Indicator Sensor Circuit

![[19e00977.png]]

QSK38 CM2150 Power Generation and QSK38 CM2150 Power Generation (Military Application) - Water in Fuel Indicator Sensor Circuit

![[19602254.png]]

QSK50 CM2150 Power Generation with Advanced Engine Monitoring/QSK50 CM2150 Power Generation without Advanced Engine Monitoring/QSK60 CM2150 Power Generation - Water in Fuel Indicator Sensor Circuit

![[19602255.png]]

QSK50 and QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - Water in Fuel Indicator Sensor Circuit

![[19602256.png]]

QSK60 CM2150 Industrial - Water in Fuel Indicator Sensor Circuit

### Circuit Description

The water in fuel indicator sensor is attached to the first stage fuel filter. The water in fuel indicator sensor sends a signal to the engine control module (ECM) when a set volume of water has accumulated in the fuel filter. The water in fuel indicator sensor circuit contains two wires; a water in fuel indicator RETURN (sensor RETURN 1) ground wire and a water in fuel indicator SIGNAL wire.

### Component Location

The water in fuel indicator sensor is integrated into the first stage fuel filter housing which is mounted off-engine. Refer to the equipment manufacturer service information.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position or when the engine is running.

### Conditions For Setting The Fault Codes

The ECM detected water in the fuel filter was above the sensor level.

### Action Taken When The Fault Code Is Active

The ECM illuminates the white MAINTENANCE lamp or flashes the amber CHECK ENGINE lamp, indicating a maintenance condition, immediately after the diagnostic runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.

- The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the flashing amber CHECK ENGINE lamp / MAINTENANCE lamp immediately after the diagnostic runs and passes.

- The "Reset All Faults" command in INSITE™ electronic service tool can be used to clear active and inactive faults.

### Shoptalk

Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

Water in the fuel can do extensive damage to the fuel system, due to the tight tolerances of the fuel system components.

Drain the Stage 1 and/or duplex fuel filters.

Bulk fuel supply may be contaminated.

If this fault code is active, and there is no water in the fuel filter, then a malfunctioning water in filter sensor or water in the sensor connector can cause the fault.

Refer to Troubleshooting Fault Code 418.
