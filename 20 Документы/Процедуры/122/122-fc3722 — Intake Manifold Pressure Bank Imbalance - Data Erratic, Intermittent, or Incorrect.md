---
aliases:
  - "Разбаланс давления во впускных коллекторах рядов — данные нестабильны или неверны"
type: "Процедура"
doc: "122-fc3722"
title_en: "Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect"
title_ru: "Разбаланс давления во впускных коллекторах рядов — данные нестабильны или неверны"
modified: "2015-06-25"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 2
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc3722.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc3722.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect
**Разбаланс давления во впускных коллекторах рядов — данные нестабильны или неверны**

> [!abstract] Процедура · `122-fc3722`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc3722.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc3722.pdf)

### Fault Code: 3722

### Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 3722 PID(P): SPN: FMI: Lamp: Maintenance SRT: | Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect. | Engine shutdown or derate. |

![[19601948.png]]

QSK50 CM2150 Power Generation with Advanced Engine Monitoring - Intake Manifold 1 Pressure Sensor Circuit

![[19602218.png]]

QSK50 CM2150 Power Generation with Advanced Engine Monitoring - Intake Manifold 2 Pressure Sensor Circuits

### Circuit Description

The intake manifold 1 and 2 pressure sensors monitor intake manifold air pressure and pass information to the engine control module (ECM) through the engine harness. The ECM calculates a differential pressure between the left and right bank based on this information.

### Component Location

The intake manifold 1 pressure sensors are located in the left and right bank front air intake manifold.

### Conditions For Running The Diagnostics

- This diagnostic runs continuously when the ECM keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

- If the boost pressure differential between the left and right bank intake manifold pressure sensors exceeded a calibrated value for a calibrated amount of time, the fault will activate.

### Action Taken When The Fault Code Is Active

- N/A

### Conditions For Clearing The Fault Code

- N/A

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

Possible causes of this fault code include:

- Restricted air intake filters

- An intake air system boost leak

- A closed intake air shut off valve

- An issue with one of the turbochargers

- Multiple malfunctioning injectors on one bank.

Refer to Troubleshooting Fault Code t05-3722.
