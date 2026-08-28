---
aliases:
  - "Индикатор воды в топливе выше нормы — умеренный уровень"
type: "Процедура"
doc: "123-fc1852"
title_en: "Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Moderately Severe Level"
title_ru: "Индикатор воды в топливе выше нормы — умеренный уровень"
modified: "2015-09-24"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 3
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc1852.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc1852.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Moderately Severe Level
**Индикатор воды в топливе выше нормы — умеренный уровень**

> [!abstract] Процедура · `123-fc1852`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-09-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc1852.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc1852.pdf)

### Fault Code: 1852

### Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1852 PID(P): SPN: 97 FMI: 16 Lamp: Amber SRT: | Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Moderately Severe Level. Water has been detected in the fuel filter. | Possible white smoke, loss of power, or hard starting. Engine derate will occur on Marine engines if optional engine protection feature is enabled. |

![[19401834.png]]

QSK19 CM2150 Industrial - Water In Fuel Indicator Sensor Circuit

![[19401835.png]]

QSK19 CM2150 Marine - Water In Fuel Indicator Sensor Circuit

![[r8f00016.png]]

QSK19 CM2150 Power Generation - Water In Fuel Indicator Sensor Circuit

### Circuit Description

The water in fuel indicator sensor is attached to the first stage fuel filter. The water in fuel indicator sensor sends a signal to the engine control module (ECM) when a set volume of water has accumulated in the fuel filter. The water in fuel circuit contains two wires; a ground wire and SIGNAL wire.

### Component Location

The water in fuel indicator sensor is integrated into the bottom of the first stage fuel filter. The first stage fuel filter is located on the intake side of the engine.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The ECM detected water in the fuel filter was above the sensor level.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.

- On Marine Propulsion engines, if the optional engine protection feature has been enabled, a torque derate will occur.

### Conditions For Clearing The Fault Code

- To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.

- The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.

- The Reset All Faults command in INSITE™ electronic service tool can be used to clear active and inactive faults.

### Shoptalk

Water in the fuel can do extensive damage to the fuel system, due to the tight tolerances of the fuel system components.

Drain the Stage 1 and/or duplex fuel filters.

Bulk fuel supply may be contaminated.

If this fault code is active and there is no water in the fuel filter then a malfunctioning water in fuel sensor or water in the sensor connector could be causing the fault.

Refer to Troubleshooting Fault Code t05-1852.
