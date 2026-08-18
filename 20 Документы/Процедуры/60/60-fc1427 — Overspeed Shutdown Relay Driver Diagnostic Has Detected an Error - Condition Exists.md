---
aliases:
  - "Диагностика драйвера реле останова по разносу выявила ошибку — условие возникло"
type: "Процедура"
doc: "60-fc1427"
title_en: "Overspeed Shutdown Relay Driver Diagnostic Has Detected an Error - Condition Exists"
title_ru: "Диагностика драйвера реле останова по разносу выявила ошибку — условие возникло"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1427.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1427.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Overspeed Shutdown Relay Driver Diagnostic Has Detected an Error - Condition Exists
**Диагностика драйвера реле останова по разносу выявила ошибку — условие возникло**

> [!abstract] Процедура · `60-fc1427`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1427.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1427.pdf)

### Fault Code: 1427

### Overspeed Shutdown Relay Driver Diagnostic Has Detected an Error - Condition Exists

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1427 PID(P): SPN: 4185 FMI: 11/31 Lamp: Amber SRT: | Error detected in the overspeed lamp driver circuit. | The overspeed shutdown lamp will **not** turn on. |

![[19a00878.png]]

Overspeed shutdown lamp Circuit

### Circuit Description

The overspeed shutdown lamp will indicate when the engine has reached overspeed.

### Component Location

The overspeed shutdown lamp is located on the generator set control panel.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected an error in the engine overspeed lamp circuit.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Damaged or malfunctioning overspeed shutdown lamp

- Low voltage to the overspeed shutdown lamp

- Malfunctioning or damaged engine wiring harness.

- Malfunctioning or damaged OEM wiring harness.

Refer to Troubleshooting Fault Code 1427.
