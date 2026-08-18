---
aliases:
  - "Уровень масла в выносном баке ниже нормы — умеренный уровень"
type: "Процедура"
doc: "60-fc1357"
title_en: "Engine Oil Level Remote Reservoir - Data Valid But Below Normal Operating Range - Moderately Severe Level"
title_ru: "Уровень масла в выносном баке ниже нормы — умеренный уровень"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1357.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1357.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Oil Level Remote Reservoir - Data Valid But Below Normal Operating Range - Moderately Severe Level
**Уровень масла в выносном баке ниже нормы — умеренный уровень**

> [!abstract] Процедура · `60-fc1357`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1357.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1357.pdf)

### Fault Code: 1357

### Engine Oil Level Remote Reservoir - Data Valid But Below Normal Operating Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1357 PID(P): P17 SPN: 1380 FMI: 1/18 Lamp: Amber SRT: | The remote engine oil reservoir is below the normal operating level. | Possible damage to engine if left unresolved. |

![[19a00874.png]]

Engine Oil Remote Reservoir Level Sensor Circuit

### Circuit Description

The engine oil remote reservoir level sensor is used to monitor the oil level inside the remote reservior.

### Component Location

The engine oil remote reservoir level sensor is located in the engine oil remote reservoir and the location is OEM dependent.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the remote reservoir engine oil level was low.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Low engine oil level in the remote reservior

- Malfunctioning engine oil remote reservior level sensor.

- Malfunctioning or damaged OEM wiring harness.

Refer to Troubleshooting Fault Code 1357.
