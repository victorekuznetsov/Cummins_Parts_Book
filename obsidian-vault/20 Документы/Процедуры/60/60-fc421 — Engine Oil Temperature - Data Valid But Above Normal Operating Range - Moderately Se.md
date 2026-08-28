---
aliases:
  - "Температура моторного масла выше нормы — умеренный уровень"
type: "Процедура"
doc: "60-fc421"
title_en: "Engine Oil Temperature - Data Valid But Above Normal Operating Range - Moderately Severe Level"
title_ru: "Температура моторного масла выше нормы — умеренный уровень"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc421.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc421.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Oil Temperature - Data Valid But Above Normal Operating Range - Moderately Severe Level
**Температура моторного масла выше нормы — умеренный уровень**

> [!abstract] Процедура · `60-fc421`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc421.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc421.pdf)

### Fault Code: 421

### Engine Oil Temperature - Data Valid But Above Normal Operating Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 421 PID(P): P175 SPN: 175 FMI: 0/16 Lamp: Amber SRT: | Engine oil temperature is above the engine protection limit. | Possible reduced engine performance. |

![[19a00857.png]]

Engine Oil Temperature Sensor Circuit

### Circuit Description

The engine oil temperature sensor is a variable resistor sensor used by the ECM to monitor the engine oil temperature. The engine oil temperature sensor has two circuits: signal, and return circuits. The signal voltage indicates the engine oil temperature.

### Component Location

The engine oil temperature sensor is located in the oil pan adapter on the left bank.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active or when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the engine oil temperature was greater than the engine protection limit.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

- The torque output of the engine will be reduced.

### Conditions For Clearing The Fault Code

- To validate the repair, bring the engine up to operating temperature and run it in normal loaded conditions for 15 minutes.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning lubricating oil cooler.

- A malfunctioning or damaged engine oil temperature sensor.

Refer to Troubleshooting Fault Code 421.
