---
aliases:
  - "Индикатор воды в топливе — выше нормы — наивысший уровень"
type: "Процедура"
doc: "123-fc4642"
title_en: "Water in Fuel Indicator - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Индикатор воды в топливе — выше нормы — наивысший уровень"
modified: "2015-09-25"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 3
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc4642.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc4642.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# Water in Fuel Indicator - Data Valid But Above Normal Operating Range - Most Severe Level
**Индикатор воды в топливе — выше нормы — наивысший уровень**

> [!abstract] Процедура · `123-fc4642`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-09-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc4642.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc4642.pdf)

### Fault Code: 4642

### Water in Fuel Indicator - Data Valid But Above Normal Operating Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 4642 PID(P): SPN: 97 FMI: 0 Lamp: Red SRT: | Water in Fuel Indicator - Data Valid But Above Normal Operating Rage - Most Severe Level. Water has been detected in the fuel filter. | Possible white smoke, loss of power, or hard starting. Engine derate will occur on marine engines if optional engine protection feature is enabled. |

![[19401834.png]]

QSK19 CM2150 Industrial - Water In Fuel Indicator Sensor Circuit

![[19401835.png]]

QSK19 CM2150 Marine - Water In Fuel Indicator Sensor Circuit

![[r8f00016.png]]

QSK19 CM2150 Power Generation - Water In Fuel Indicator Sensor Circuit

### Circuit Description

The water in fuel indicator sensor is attached to the first stage fuel filter. The water in fuel indicator sensor sends a signal to the engine control module (ECM) when a set volume of water has accumulated in the fuel filter. The water in fuel indicator sensor circuit contains two wires; a water in fuel indicator return (sensor return 1) ground wire and a water in fuel indicator signal wire.

### Component Location

The water in fuel indicator sensor is integrated into the bottom of the first stage fuel filter. The first stage fuel filter is located on the intake side of the engine.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The ECM detected water in fuel for an extended period of time.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the red STOP ENGINE lamp immediately after the diagnostic runs and fails.

- On marine propulsion engines, if the optional engine protection feature has been enabled, a speed derate will occur.

### Conditions For Clearing The Fault Code

- To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.

- The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the red STOP ENGINE lamp immediately after the diagnostic runs and passes.

- The Reset All Faults command in INSITE™ electronic service tool can be used to clear active and inactive faults.

### Shoptalk

Water in the fuel can do extensive damage to the fuel system, due to the tight tolerances of the fuel system components.

Drain the Stage 1 and/or duplex fuel filters.

Bulk fuel supply may be contaminated.

If this fault code is active and there is no water in the fuel filter then a malfunctioning water in fuel sensor or water in the sensor connector could be causing the fault.

Refer to Troubleshooting Fault Code t05-4642.
