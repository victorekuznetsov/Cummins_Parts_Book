---
aliases:
  - "Цепь коррекции регулирования частоты/нагрузки — напряжение ниже нормы"
type: "Процедура"
doc: "60-fc1979"
title_en: "Generator Speed/Load Governing Bias Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь коррекции регулирования частоты/нагрузки — напряжение ниже нормы"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1979.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1979.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Generator Speed/Load Governing Bias Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь коррекции регулирования частоты/нагрузки — напряжение ниже нормы**

> [!abstract] Процедура · `60-fc1979`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1979.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1979.pdf)

### Fault Code: 1979

### Generator Speed/Load Governing Bias Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1979 PID(P): SPN: 3938 FMI: 4/4 Lamp: Amber SRT: | Generator Speed/Load Governing Bias Circuit has detected voltage below normal or shorted to low source. | Engine will **not** synchronize with the grid, if connected. |

![[19a00879.png]]

Generator Speed/Load Governing Bias Circuit.

### Circuit Description

The generator speed/load governing bias circuit controls the engine speed in order to match a required grid frequency and phase.

### Component Location

The generator speed/load governing bias control is located in the generator set controller on the generator set.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active or when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected generator speed/load governing bias signal is out of range low.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged engine wiring harness.

Refer to Troubleshooting Fault Code 1979.
