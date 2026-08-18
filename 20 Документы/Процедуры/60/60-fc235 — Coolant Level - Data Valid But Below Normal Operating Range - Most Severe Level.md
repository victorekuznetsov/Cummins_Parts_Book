---
aliases:
  - "Уровень ОЖ ниже нормы — наивысший уровень"
type: "Процедура"
doc: "60-fc235"
title_en: "Coolant Level - Data Valid But Below Normal Operating Range - Most Severe Level"
title_ru: "Уровень ОЖ ниже нормы — наивысший уровень"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc235.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc235.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Coolant Level - Data Valid But Below Normal Operating Range - Most Severe Level
**Уровень ОЖ ниже нормы — наивысший уровень**

> [!abstract] Процедура · `60-fc235`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc235.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc235.pdf)

### Fault Code: 235

### Coolant Level - Data Valid But Below Normal Operating Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 235 PID(P): P111 SPN: 111 FMI: 1/1 Lamp: Red SRT: | Low engine coolant level detected. | Engine will shut down. |

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

- The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.

- The engine will be shut down.

- Engine torque will be reduced if the engine is operated for an extended period of time with this fault active.

### Conditions For Clearing The Fault Code

- To validate the repair, bring the engine up to operating temperature and run it in normal loaded conditions for 5 minutes.

- The generator set controller will turn off the shutdown indicator immediately after the user presses the reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Low coolant level

- Malfunctioning or damaged coolant level sensor.

- Malfunctioning or damaged engine wiring harness.

- Malfunctioning or damaged OEM wiring harness.

Refer to Troubleshooting Fault Code 235.
