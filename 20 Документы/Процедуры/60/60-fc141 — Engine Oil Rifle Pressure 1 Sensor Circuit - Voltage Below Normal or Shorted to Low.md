---
aliases:
  - "Цепь датчика давления масла в главной магистрали 1 — напряжение ниже нормы"
type: "Процедура"
doc: "60-fc141"
title_en: "Engine Oil Rifle Pressure 1 Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика давления масла в главной магистрали 1 — напряжение ниже нормы"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Oil Rifle Pressure 1 Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика давления масла в главной магистрали 1 — напряжение ниже нормы**

> [!abstract] Процедура · `60-fc141`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc141.pdf)

### Fault Code: 141

### Engine Oil Rifle Pressure 1 Sensor Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 141 PID(P): P100 SPN: 100 FMI: 4/4 Lamp: Amber SRT: | Low signal voltage or open circuit detected at the engine oil pressure circuit. | None on performance. |

![[19a00847.png]]

Engine Oil Rifle Pressure Sensor Circuit

### Circuit Description

The engine oil rifle pressure sensor is a variable resistance sensor used by the ECM to monitor the lubricating oil pressure. The engine oil rifle pressure sensor has three circuits: 5 volt supply, return, and signal circuits. The signal circuit voltage indicates the oil pressure in the oil rifle.

### Component Location

The engine oil pressure sensor is located in the oil rifle.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active or when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the engine oil pressure signal voltage was out of range low.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

- A default value for the engine oil pressure reading is used.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged engine wiring harness.

- Malfunctioning or damaged engine oil rifle pressure sensor.

Refer to Troubleshooting Fault Code 141.
