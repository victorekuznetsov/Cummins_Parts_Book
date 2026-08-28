---
aliases:
  - "Температура охлаждающей жидкости — особые указания"
type: "Процедура"
doc: "60-fc1847"
title_en: "Engine Coolant Temperature - Special Instructions"
title_ru: "Температура охлаждающей жидкости — особые указания"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1847.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc1847.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Coolant Temperature - Special Instructions
**Температура охлаждающей жидкости — особые указания**

> [!abstract] Процедура · `60-fc1847`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1847.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc1847.pdf)

### Fault Code: 1847

### Engine Coolant Temperature - Special Instructions

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1847 PID(P): P110 SPN: 110 FMI: 14/14 Lamp: Red SRT: | Engine coolant temperature is above the engine protection warning limit. | Engine will shut down. Generator set will disconnect from the grid. |

![[19a00848.png]]

Engine Coolant Temperature Sensor Circuit

### Circuit Description

The engine coolant temperature sensor is a variable resistor sensor used by the ECM to monitor the engine coolant temperature. The engine coolant temperature sensor has two circuits: signal, and return circuits. The signal voltage indicates the coolant temperature.

### Component Location

The engine coolant temperature sensor is located on the thermostat housing.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the engine coolant temperature was greater than the engine protection limit.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.

- The engine will be shut down.

### Conditions For Clearing The Fault Code

- To validate the repair, bring the engine up to operating temperature and run it in normal loaded conditions for 15 minutes.

- The generator set controller will turn off the shutdown indicator immediately after the user presses the reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Obstructed airflow through the radiator.

- Engine coolant level low

- Collapsed or restricted cooling system hoses.

- Malfunctioning engine coolant thermostat.

- A malfunctioning water pump.

- Malfunctioning engine coolant temperature sensor

Refer to Troubleshooting Fault Code 1847.
