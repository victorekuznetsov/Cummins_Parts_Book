---
aliases:
  - "Индикатор воды в топливе 2 — выше нормы — наивысший уровень"
type: "Процедура"
doc: "122-fc5367"
title_en: "Water in Fuel Indicator 2 - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Индикатор воды в топливе 2 — выше нормы — наивысший уровень"
modified: "2017-01-02"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc5367.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc5367.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Water in Fuel Indicator 2 - Data Valid But Above Normal Operating Range - Most Severe Level
**Индикатор воды в топливе 2 — выше нормы — наивысший уровень**

> [!abstract] Процедура · `122-fc5367`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-01-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc5367.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc5367.pdf)

### Fault Code: 5367

### Water in Fuel Indicator 2 - Data Valid But Above Normal Operating Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 4642 PID(P): SPN: 6301 FMI: 0 Lamp: Red SRT: | Water in Fuel Indicator 2 - Data Valid But Above Normal Operating Range - Most Severe Level. Water has been detected in the fuel filter. | Possible white smoke, loss of power, or hard starting. Engine derate will occur on Marine engines if optional engine protection feature is enabled. |

![[19k00130.png]]

Water In Fuel 2 Indicator Sensor Circuit

### Circuit Description

The water in fuel indicator 2 sensor is attached to the Stage 0 (original equipment manufacturer (OEM)) fuel filter for Marine applications. The water in fuel indicator 2 sensor sends a signal to the engine control module (ECM) when a set volume of water has accumulated in the fuel filter. The water in fuel indicator 2 sensor circuit contains two wires; a water in fuel indicator RETURN (sensor RETURN 1) ground wire and a water in fuel indicator SIGNAL wire.

### Component Location

The water in fuel indicator 2 sensor is installed as an option into the Stage 0 (OEM) fuel filter housing which is mounted off-engine. See equipment manufacturer service information.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The ECM detected water in fuel for an extended period of time.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the red STOP ENGINE lamp immediately after the diagnostic runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, perform a key cycle, start the engine, and let it idle for 1 minute.

- The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the red STOP ENGINE lamp immediately after the diagnostic runs and passes.

- The Reset All Faults command in INSITE™ electronic service tool can be used to clear active and inactive faults.

### Shoptalk

Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

Water in the fuel can do extensive damage to the fuel system due to the tight tolerances of the fuel system components.

Drain the Stage 0 and/or duplex fuel filters.

Bulk fuel supply may be contaminated.

If this fault code is active and there is no water in the fuel filter, then a malfunctioning water in fuel sensor or water in the sensor connector could be causing the fault.

Refer to Troubleshooting Fault Code 5367.
