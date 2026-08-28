---
aliases:
  - "Давление в топливной рампе 1 выше нормы — наивысший уровень"
type: "Процедура"
doc: "122-fc449"
title_en: "Injector Metering Rail 1 Pressure - Data Valid but Above Normal Operating Range - Most Severe Level"
title_ru: "Давление в топливной рампе 1 выше нормы — наивысший уровень"
modified: "2010-12-13"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc449.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc449.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Injector Metering Rail 1 Pressure - Data Valid but Above Normal Operating Range - Most Severe Level
**Давление в топливной рампе 1 выше нормы — наивысший уровень**

> [!abstract] Процедура · `122-fc449`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-12-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc449.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc449.pdf)

### Fault Code: 449

### Injector Metering Rail 1 Pressure - Data Valid but Above Normal Operating Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 449 PID(P): SPN: 157 FMI: 0 Lamp: Red SRT: | Injector Metering Rail 1 Pressure - Data Valid but Above Normal Operating Range - Most Severe Level. ECM detects that injector metering rail 1 pressure has exceeded high-pressure relief valve. | Fuel injection noise. |

![[19602101.png]]

QSK38 CM2150 Industrial - Injector Metering Rail 1 Circuit

![[19602102.png]]

QSK38 CM2150 Marine - Injector Metering Rail 1 Circuit

![[19e00958.png]]

QSK38 CM2150 Power Generation (Military Application)/QSK38 CM2150 Power Generation - Injector Metering Rail 1 Circuit

![[19602103.png]]

QSK50 CM2150 Industrial - Injector Metering Rail 1 Circuit

![[19602105.png]]

QSK50 CM2150 Marine - Injector Metering Rail 1 Pressure Circuit

![[19602106.png]]

QSK60 CM2150 Industrial - Injector Metering Rail 1 Pressure Circuit

![[19e00959.png]]

QSK50 CM2150 Power Generation without Advanced Engine Monitoring/QSK50 CM2150 Power Generation with Advanced Engine Monitoring/QSK60 CM2150 Power Generation - Injector Metering Rail 1 Circuit

![[19602107.png]]

QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - Injector Metering Rail 1 Pressure Circuit

### Circuit Description

The pressure control loop relies on fuel pressure supplied to the high-pressure pump by the gerotor pump. The electronic control module (ECM) monitors the injector metering rail 1 pressure and the engine operating conditions, and changes the flow command to maintain the proper injector metering rail 1 pressure. Changes to the flow command result in opening or closing of the fuel pump pressurizing assembly 1.

The high-pressure relief valve is set to trip at 1950 bar \[28,282 psi\]. After it trips, it then regulates at 900 to 1300 bar \[13,053 to 18,854 psi\].

**NOTE:** The mechanical dump valve has **not** popped.

### Component Location

The high-pressure fuel pump is mounted to the gear housing on the left side of the engine.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

**NOTE:** Replace the high-pressure mechanical dump valve even if the fault clears.

Refer to Troubleshooting Fault Code 449.
