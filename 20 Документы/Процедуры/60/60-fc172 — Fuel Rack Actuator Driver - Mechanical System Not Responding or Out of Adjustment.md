---
aliases:
  - "Драйвер привода рейки — механическая система не отвечает или разрегулирована"
type: "Процедура"
doc: "60-fc172"
title_en: "Fuel Rack Actuator Driver - Mechanical System Not Responding or Out of Adjustment"
title_ru: "Драйвер привода рейки — механическая система не отвечает или разрегулирована"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc172.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc172.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Fuel Rack Actuator Driver - Mechanical System Not Responding or Out of Adjustment
**Драйвер привода рейки — механическая система не отвечает или разрегулирована**

> [!abstract] Процедура · `60-fc172`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc172.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc172.pdf)

### Fault Code: 172

### Fuel Rack Actuator Driver - Mechanical System Not Responding or Out of Adjustment

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 172 PID(P): S23 SPN: 638 FMI: 7/7 Lamp: Red SRT: | Fuel control rack is in a stuck position. | Engine will shut down. |

![[19a00845.png]]

Fuel Rack Actuator Driver Circuit

### Circuit Description

The fuel control rack and solenoid determine the quantity of fuel metered to the engine.

### Component Location

The fuel control rack and solenoid are internal parts of the fuel injection pump.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the fuel rack is stuck or **not** responding to fueling commands.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.

- The engine will be shut down.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the shutdown indicator immediately after the user presses the reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Loose or damaged actuator connector.

- Malfunctioning fuel pump.

Refer to Troubleshooting Fault Code 172.
