---
aliases:
  - "Цепь драйвера клапана отсечки топлива — напряжение ниже нормы"
type: "Процедура"
doc: "60-fc254"
title_en: "Engine Fuel Shutoff Valve Driver Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь драйвера клапана отсечки топлива — напряжение ниже нормы"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc254.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc254.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Fuel Shutoff Valve Driver Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь драйвера клапана отсечки топлива — напряжение ниже нормы**

> [!abstract] Процедура · `60-fc254`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc254.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc254.pdf)

### Fault Code: 254

### Engine Fuel Shutoff Valve Driver Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 254 PID(P): S17 SPN: 632 FMI: 4/4 Lamp: Red SRT: | Low voltage detected on the fuel shutoff control circuit. | Engine will shut down. |

![[19a00865.png]]

Fuel Shutoff Valve

### Circuit Description

The fuel shutoff valve is a device used by the ECM to control the fuel supply into the injection pump.

### Component Location

The fuel shutoff valves are located on the oil pan rail near the middle of the block on both banks.

### Conditions For Running The Diagnostics

This diagnostic runs when the fuel shutoff valve is commanded ON.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) has detected the fuel shutoff control is out of range low.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.

- The engine will be shut down.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the shutdown indicator immediately after the user presses the reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Each ECM has an individual source address that displays when the recommended Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in the recommended Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.

Possible causes of this fault code include:

- Malfunctioning or damaged engine wiring harness.

- A malfunctioning fuel shutoff valve.

- Damaged or loose connections.

Refer to Troubleshooting Fault Code 254.
