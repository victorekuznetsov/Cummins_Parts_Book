---
aliases:
  - "Потеря питания при включённом зажигании — данные нестабильны или неверны"
type: "Процедура"
doc: "60-fc1117"
title_en: "Power Supply Lost With Ignition On - Data Erratic, Intermittent, or Incorrect"
title_ru: "Потеря питания при включённом зажигании — данные нестабильны или неверны"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1117.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1117.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Power Supply Lost With Ignition On - Data Erratic, Intermittent, or Incorrect
**Потеря питания при включённом зажигании — данные нестабильны или неверны**

> [!abstract] Процедура · `60-fc1117`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1117.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1117.pdf)

### Fault Code: 1117

### Power Supply Lost With Ignition On - Data Erratic, Intermittent, or Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1117 PID(P): S251 SPN: 3597 FMI: 2/2 Lamp: None SRT: | Supply voltage to the ECM fell below a calibrated limit momentarily, or the ECM was **not** allowed to power down correctly. | Possible reduced engine performance. |

![[19a00873.png]]

Engine Control Module (ECM)

### Circuit Description

The ECM receives constant voltage from the batteries through the battery 1 voltage wires that are connected directly to the positive (+) battery post. There is a 10-ampere fuse in the battery 1 voltage wires to protect the OEM wiring harness from overheating. The ECM receives power supply through the vehicle keyswitch wire when the vehicle keyswitch is turned on. The battery 1 voltage return wires are connected directly to the negative (-) battery post.

### Component Location

The ECM is connected to the battery through a 4-pin connector on the engine wiring harness inside the generator set panel. The extension harness also has a 4-pin connector that provides battery power to both ECMs and the generator set control panel. The location of the battery will vary with the original equipment manufacturer (OEM).

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active or when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the ECM power supply was removed before power-down parameters could be saved. The fault code will be active when the keyswitch is turned ON following the incomplete power-down event.

### Action Taken When The Fault Code Is Active

- The generator set controller displays the fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Low battery voltage.

- Battery disconnect switch turned off before ECM is powered down.

Refer to Troubleshooting Fault Code 1117.
