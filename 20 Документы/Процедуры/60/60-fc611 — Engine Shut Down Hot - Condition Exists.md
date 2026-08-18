---
aliases:
  - "Останов горячего двигателя — условие возникло"
type: "Процедура"
doc: "60-fc611"
title_en: "Engine Shut Down Hot - Condition Exists"
title_ru: "Останов горячего двигателя — условие возникло"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc611.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc611.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Shut Down Hot - Condition Exists
**Останов горячего двигателя — условие возникло**

> [!abstract] Процедура · `60-fc611`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc611.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc611.pdf)

### Fault Code: 611

### Engine Shut Down Hot - Condition Exists

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 611 PID(P): S116 SPN: 1383 FMI: 11/31 Lamp: None SRT: | Engine shut down hot without a proper cool down run period. | None on performance. |

![[19a00867.png]]

Engine Control Module (ECM)

### Circuit Description

The engine control module (ECM) uses inputs from the engine coolant temp sensor, engine speed sensor, keyswitch, and calculated engine torque for this diagnostic.

### Component Location

The emergency stop switch is located on the generator set control panel.

The Engine Control Modules (ECM) are located on a plate that is above the flywheel housing.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected engine speed is 0 within 15 seconds of the engine operating under a load.

### Action Taken When The Fault Code Is Active

- The generator set controller displays the fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the fault code immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

This is an information **only** fault code that will **only** become active if the engine was shut down before proper engine cooldown.

Refer to Troubleshooting Fault Code 611.
