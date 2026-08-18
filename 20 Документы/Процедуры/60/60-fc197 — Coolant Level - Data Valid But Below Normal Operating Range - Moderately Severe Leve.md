---
aliases:
  - "Уровень охлаждающей жидкости ниже нормы — умеренный уровень"
type: "Процедура"
doc: "60-fc197"
title_en: "Coolant Level - Data Valid But Below Normal Operating Range - Moderately Severe Level"
title_ru: "Уровень охлаждающей жидкости ниже нормы — умеренный уровень"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc197.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc197.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Coolant Level - Data Valid But Below Normal Operating Range - Moderately Severe Level
**Уровень охлаждающей жидкости ниже нормы — умеренный уровень**

> [!abstract] Процедура · `60-fc197`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc197.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc197.pdf)

### Fault Code: 197

### Coolant Level - Data Valid But Below Normal Operating Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 197 PID(P): P111 SPN: 111 FMI: 1/18 Lamp: Amber SRT: | Low engine coolant level detected. | Possible reduced engine performance. |

![[19a00856.png]]

Coolant Level Sensor Circuit

### Circuit Description

The coolant level sensor is a variable resistance sensor used by the ECM to monitor the coolant level. The coolant level sensor has three circuits: 5 volt supply, return and signal circuits. The signal circuit voltage indicates the level of the coolant in the radiator top tank or surge tank.

### Component Location

The engine coolant level sensor is typically located in the radiator top tank or surge tank.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active or when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the coolant level was below normal.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

- The torque output of the engine will be reduced.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Low coolant level

- Malfunctioning or damaged coolant level sensor.

- Malfunctioning or damaged engine wiring harness.

- Malfunctioning or damaged OEM wiring harness.

Refer to Troubleshooting Fault Code 197.
