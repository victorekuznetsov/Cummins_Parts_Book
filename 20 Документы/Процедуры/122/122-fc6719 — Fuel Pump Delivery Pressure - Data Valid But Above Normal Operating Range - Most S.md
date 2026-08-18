---
aliases:
  - "Давление подачи топливного насоса — данные достоверны, но выше нормы — наивысший уровень"
type: "Процедура"
doc: "122-fc6719"
title_en: "Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Давление подачи топливного насоса — данные достоверны, но выше нормы — наивысший уровень"
modified: "2017-05-30"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 8
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc6719.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc6719.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level
**Давление подачи топливного насоса — данные достоверны, но выше нормы — наивысший уровень**

> [!abstract] Процедура · `122-fc6719`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-05-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc6719.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc6719.pdf)

### Fault Code: 6719

### Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 6719 PID(P): SPN: 94 FMI: 0/0 Lamp: Red SRT: | Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level. Fuel pump supply pressure very high. | Possible engine speed derate. Low power or engine smoke. |

![[19602267.png]]

QSK38 CM2150 Industrial - Fuel Delivery Pressure Sensor Circuit

![[19e00960.png]]

QSK38 CM2150 Power Generation/QSK38 Power Generation (Military Application) - Fuel Delivery Pressure Sensor Circuit

![[19602268.png]]

QSK38 CM2150 Marine - Fuel Delivery Pressure Sensor Circuit

![[19602269.png]]

QSK50 CM2150 Power Generation without Advanced Engine Monitoring/QSK50 CM2150 Power Generation with Advanced Engine Monitoring and QSK60 CM2150 Power Generation - Fuel Delivery Pressure Sensor Circuit

![[19602270.png]]

QSK50 CM2150 Industrial - Fuel Delivery Pressure Sensor Circuit

![[19602271.png]]

QSK60 CM2150 Industrial - Fuel Delivery Pressure Sensor Circuit

![[19602272.png]]

QSK50 CM2150 Marine - Fuel Delivery Pressure Sensor Circuit

![[19602273.png]]

QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - Fuel Delivery Pressure Sensor Circuit

### Circuit Description

The fuel delivery pressure sensor is used by the engine control module (ECM) to monitor fuel delivery pressure directly before the Stage 2 filter. The ECM monitors the voltage on the fuel delivery pressure SIGNAL pin and converts it to a pressure value.

### Component Location

The fuel delivery pressure sensor is located in the Stage 2 fuel filter head.

### Conditions For Running The Diagnostics

- The engine speed **must** be above 500 RPM for 10 seconds, and fueling **must** be above 20 mg/stk for 5 seconds before a diagnostic decision begins to be made.

- The fuel temperature **must** be greater than, or equal to -10 ⁰C.

### Conditions For Setting The Fault Codes

- When the fuel supply pressure is greater than 1200 kPa (174 psi) for more than 3 seconds, FC4615 is initially set.

- FC4615 also activates an engine speed derate that attempts to bring down the fuel supply pressure at or below 1000 kPa.

- If after 30 minutes, the speed derate is unable to bring down the fuel supply pressure to 1000 kPa, then FC 6719 (Red) is activated.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the red CHECK ENGINE lamp immediately when the diagnostics detects high fuel supply pressure.

### Conditions For Clearing The Fault Code

- FC 6719 (Red Lamp) is cleared at every key-cycle. However, it is strongly recommended to stop engine operation and follow the troubleshooting steps for resolution immediately.

- Once the engine has been restarted, the fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately.

- The Reset All Faults command in INSITE™ electronic service tool can be used to clear active and inactive faults.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

Possible causes of this fault code include:

- Stage 2 fuel filter restriction high

- Pinched or damaged fuel supply line

- Stuck gerotor pump fuel pressure regulator located in high-pressure pump.

Refer to Troubleshooting Fault Code t05-6719.
