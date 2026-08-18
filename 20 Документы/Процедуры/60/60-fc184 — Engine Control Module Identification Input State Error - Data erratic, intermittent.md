---
aliases:
  - "Ошибка состояния входа идентификации ЭБУ — данные нестабильны или неверны"
type: "Процедура"
doc: "60-fc184"
title_en: "Engine Control Module Identification Input State Error - Data erratic, intermittent or incorrect"
title_ru: "Ошибка состояния входа идентификации ЭБУ — данные нестабильны или неверны"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc184.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc184.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Control Module Identification Input State Error - Data erratic, intermittent or incorrect
**Ошибка состояния входа идентификации ЭБУ — данные нестабильны или неверны**

> [!abstract] Процедура · `60-fc184`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc184.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc184.pdf)

### Fault Code: 184

### Engine Control Module Identification Input State Error - Data erratic, intermittent or incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 184 PID(P): S233 SPN: 609 FMI: 2/2 Lamp: Amber SRT: | The control module identification input state is incorrect. | Engine will shut down. Engine may **not** start. |

![[19a00854.png]]

Engine Control Module (ECM)

### Circuit Description

The engine control module (ECM) uses the control module identification circuit to verify its location in the harness. The combination of control module identification signal pins that are connected to return allow the ECM to make this determination.

### Component Location

The Engine Control Modules (ECM) are located on a plate that is above the flywheel housing.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the calibration does **not** match the control module identification input.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.

- The engine will be shut down if the Engine Protection Shutdown feature is enabled.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the shutdown indicator immediately after the user presses the reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.

Possible causes of this fault code include:

- Duplicate or incorrect ECM calibrations downloaded to the ECM(s).

- Two or more ECMs installed in the wrong location.

- Incorrect parameter settings.

- Malfunctioning or damaged engine wiring harness.

- Damaged or loose connectors.

Refer to Troubleshooting Fault Code 184.
