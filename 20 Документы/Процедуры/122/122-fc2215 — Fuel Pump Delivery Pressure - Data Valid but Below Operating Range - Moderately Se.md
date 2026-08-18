---
aliases:
  - "Давление подачи топливного насоса ниже рабочего диапазона — умеренный уровень"
type: "Процедура"
doc: "122-fc2215"
title_en: "Fuel Pump Delivery Pressure - Data Valid but Below Operating Range - Moderately Severe Level"
title_ru: "Давление подачи топливного насоса ниже рабочего диапазона — умеренный уровень"
modified: "2010-12-13"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 8
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc2215.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc2215.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Fuel Pump Delivery Pressure - Data Valid but Below Operating Range - Moderately Severe Level
**Давление подачи топливного насоса ниже рабочего диапазона — умеренный уровень**

> [!abstract] Процедура · `122-fc2215`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-12-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc2215.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc2215.pdf)

### Fault Code: 2215

### Fuel Pump Delivery Pressure - Data Valid but Below Operating Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2215 PID(P): SPN: 94 FMI: 18 Lamp: Amber SRT: | Fuel Pump Delivery Pressure - Data Valid but Below Operating Range - Moderately Severe Level. Fuel pump supply pressure low. | Low power. |

![[19602267.png]]

QSK38 CM2150 Industrial - Fuel Delivery Pressure Sensor Circuit

![[19e00960.png]]

QSK38 CM2150 Power Generation/QSK38 CM2150 Power Generation (Military Application) - Fuel Delivery Pressure Sensor Circuit

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

The fuel delivery pressure sensor is used by the electronic control module (ECM) to monitor fuel supply pressure directly before the second stage filter. The ECM monitors the voltage on the fuel delivery pressure signal pin and converts it to a pressure value.

### Component Location

The fuel delivery pressure sensor is located in the second stage fuel filter head.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

Possible causes of this fault code include:

- Stage 1 fuel filter restriction high

- Fuel inlet restriction high

- Low fuel flow from gerotor

- Stuck mechanical dump valve in gerotor housing

- Stuck low-pressure regulator in high-pressure fuel pump

- Air in fuel.

Refer to Troubleshooting Fault Code 2215.
