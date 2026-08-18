---
aliases:
  - "Давление в топливной рампе 1 ниже нормы — умеренный уровень"
type: "Процедура"
doc: "122-fc559"
title_en: "Injector Metering Rail 1 Pressure - Data Valid but Below Normal Operating Range - Moderately Severe Level"
title_ru: "Давление в топливной рампе 1 ниже нормы — умеренный уровень"
modified: "2010-09-17"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 8
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc559.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc559.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Injector Metering Rail 1 Pressure - Data Valid but Below Normal Operating Range - Moderately Severe Level
**Давление в топливной рампе 1 ниже нормы — умеренный уровень**

> [!abstract] Процедура · `122-fc559`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc559.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc559.pdf)

### Fault Code: 559

### Injector Metering Rail 1 Pressure - Data Valid but Below Normal Operating Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 559 PID(P): SPN: 157 FMI: 1/18 Lamp: Amber SRT: | Injector Metering Rail 1 Pressure - Data Valid - but Below Normal Operating Range - Moderately Severe Level. The ECM has detected that the fuel pressure is lower than commanded. | Low Power, possible shutdown, or no start. |

![[19602101.png]]

QSK38 CM2150 Industrial - Injector Metering Rail 1 Pressure Circuit

![[19602102.png]]

QSK38 CM2150 Marine - Injector Metering Rail 1 Pressure Circuit

![[19e00958.png]]

QSK38 CM2150 Power Generation/QSK38 CM2150 Power Generation (Military Application) - Injector Metering Rail 1 Pressure Circuit

![[19602103.png]]

QSK50 CM2150 Industrial - Injector Metering Rail 1 Pressure Circuit

![[19602105.png]]

QSK50 CM2150 Marine - Injector Metering Rail 1 Pressure Circuit

![[19602106.png]]

QSK60 CM2150 Industrial - Injector Metering Rail 1 Pressure Circuit

![[19e00959.png]]

QSK50 CM2150 Power Generation without Advanced Engine Monitoring/QSK50 CM2150 Power Generation with Advanced Engine Monitoring/QSK60 CM2150 Power Generation - Injector Metering Rail 1 Pressure Circuit

![[19602107.png]]

QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - Injector Metering Rail 1 Pressure Circuit

### Circuit Description

The pressure control loop relies on fuel pressure supplied to the high-pressure pump by the gerotor pump. The ECM monitors the injector metering rail 1 pressure and engine operating conditions, and changes the flow command to maintain the proper injector metering rail 1 pressure. Changes to the flow command result in opening or closing of the fuel pump pressurizing assembly 1.

### Component Location

The high-pressure fuel pump is mounted to the front gear housing on the left bank of the engine.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

Possible causes of this fault code include:

- Fuel inlet restriction

- Fuel filter plugging

- Gerotor pump output low

- Gerotor pump pressure regulator sticking or leaking

- High-pressure pump capacity decay

- Mechanical dump valve leaks to drain

- Mechanical dump valve opens at low pressure

- High-pressure injector supply line inner wall leak

- Malfunctioning fuel pump pressurizing assembly.

Refer to Troubleshooting Fault Code 559.
