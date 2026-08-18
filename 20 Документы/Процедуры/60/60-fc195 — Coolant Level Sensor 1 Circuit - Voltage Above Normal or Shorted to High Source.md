---
aliases:
  - "Цепь датчика уровня ОЖ 1 — напряжение выше нормы"
type: "Процедура"
doc: "60-fc195"
title_en: "Coolant Level Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика уровня ОЖ 1 — напряжение выше нормы"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc195.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc195.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Coolant Level Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика уровня ОЖ 1 — напряжение выше нормы**

> [!abstract] Процедура · `60-fc195`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc195.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc195.pdf)

### Fault Code: 195

### Coolant Level Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 195 PID(P): P111 SPN: 111 FMI: 3/3 Lamp: Amber SRT: | High signal voltage detected at the engine coolant level sensor circuit. | None on performance. |

![[19a00856.png]]

Coolant Level Sensor Circuit

### Circuit Description

The coolant level sensor is a variable resistance sensor used by the ECM to monitor the coolant level. The coolant level sensor has three circuits: 5 volt supply, return and signal circuits. The signal circuit voltage indicates the level of the coolant in the radiator top tank or surge tank.

### Component Location

The engine coolant level sensor is typically located in the radiator top tank or surge tank.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active or when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the coolant level signal voltage was out of range high.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

- No engine protection will be available for low coolant level.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged coolant level sensor.

- Malfunctioning or damaged engine wiring harness.

- Malfunctioning or damaged OEM wiring harness.

Refer to Troubleshooting Fault Code 195.
