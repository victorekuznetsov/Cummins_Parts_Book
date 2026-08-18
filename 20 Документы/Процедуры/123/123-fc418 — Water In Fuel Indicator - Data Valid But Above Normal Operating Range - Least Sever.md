---
aliases:
  - "Индикатор воды в топливе выше нормы — низший уровень"
type: "Процедура"
doc: "123-fc418"
title_en: "Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Least Severe Level"
title_ru: "Индикатор воды в топливе выше нормы — низший уровень"
modified: "2015-11-17"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 3
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc418.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc418.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Least Severe Level
**Индикатор воды в топливе выше нормы — низший уровень**

> [!abstract] Процедура · `123-fc418`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-11-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc418.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc418.pdf)

### Fault Code: 418

### Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Least Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 418 PID(P): SPN: 97 FMI: 0/15 Lamp: Maintenance SRT: | Water in Fuel Indicator Sensor Circuit - Data Valid But Above Normal Operating Range - Least Severe Level. Water has been detected in the fuel filter. | Possible white smoke, loss of power, or hard starting. |

![[19401834.png]]

QSK19 CM2150 Industrial - Water In Fuel Indicator Sensor Circuit

![[19401835.png]]

QSK19 CM2150 Marine - Water In Fuel Indicator Sensor Circuit

![[r8f00016.png]]

QSK19 CM2150 Power Generation - Water In Fuel Indicator Sensor Circuit

### Circuit Description

The water in fuel indicator sensor is attached to the first stage fuel filter. The water in fuel indicator sensor sends a signal to the engine control module (ECM) when a set volume of water has accumulated in the fuel filter. The water in fuel indicator sensor circuit contains two wires; a water in fuel indicator RETURN (sensor RETURN 1) ground wire and a water in fuel indicator SIGNAL wire.

### Component Location

The water in fuel indicator sensor is integrated into the bottom of the first stage fuel filter. The first stage fuel filter is located on the intake side of the engine.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position or when the engine is running.

### Conditions For Setting The Fault Codes

The ECM detected water in the fuel filter was above the sensor level.

### Action Taken When The Fault Code Is Active

The ECM illuminates the white MAINTENANCE lamp or flashes the amber CHECK ENGINE lamp, indicating a maintenance condition, immediately after the diagnostic runs and fails.

### Conditions For Clearing The Fault Code

To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.

The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately after the diagnostic runs and passes.

The ECM will turn off the flashing amber CHECK ENGINE lamp / MAINTENANCE lamp immediately after the diagnostic runs and passes.

The "Reset All Faults" command in INSITE™ electronic service tool can be used to clear active and inactive faults.

### Shoptalk

Water in the fuel can do extensive damage to the fuel system, due to the tight tolerances of the fuel system components.

Drain the Stage 1 and/or duplex fuel filters.

Bulk fuel supply may be contaminated.

If this fault code is active, and there is no water in the fuel filter then, a malfunctioning water in fuel sensor or water in the sensor connector could be causing the fault.

Refer to Troubleshooting Fault Code t05-418
