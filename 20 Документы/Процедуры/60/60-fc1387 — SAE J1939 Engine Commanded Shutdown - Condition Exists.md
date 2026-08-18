---
aliases:
  - "Команда останова двигателя по SAE J1939 — условие возникло"
type: "Процедура"
doc: "60-fc1387"
title_en: "SAE J1939 Engine Commanded Shutdown - Condition Exists"
title_ru: "Команда останова двигателя по SAE J1939 — условие возникло"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1387.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1387.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# SAE J1939 Engine Commanded Shutdown - Condition Exists
**Команда останова двигателя по SAE J1939 — условие возникло**

> [!abstract] Процедура · `60-fc1387`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1387.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1387.pdf)

### Fault Code: 1387

### SAE J1939 Engine Commanded Shutdown - Condition Exists

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1387 PID(P): S117 SPN: 1384 FMI: 11/31 Lamp: None SRT: | The generator set controller detected a shutdown from the Engine Control Module on the J1939 network. | None on performance. |

![[19a00871.png]]

J1939 Data Link Circuit

### Circuit Description

This fault code will be logged if the engine is shutdown by anything other then the engine keyswitch.

### Component Location

The Engine Control Modules (ECM) are located on a plate that is above the flywheel housing.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active or when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) received a shutdown message from the J1939 datalink network.

### Action Taken When The Fault Code Is Active

- The generator set controller displays the fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the fault code immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

This fault code is information ONLY. Troubleshoot other fault codes that are presently active in the ECM.

Refer to Troubleshooting Fault Code 1387.
