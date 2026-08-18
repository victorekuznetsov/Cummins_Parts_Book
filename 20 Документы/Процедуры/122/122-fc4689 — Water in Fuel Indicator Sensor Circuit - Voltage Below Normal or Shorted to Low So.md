---
aliases:
  - "Цепь датчика воды в топливе — напряжение ниже нормы"
type: "Процедура"
doc: "122-fc4689"
title_en: "Water in Fuel Indicator Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика воды в топливе — напряжение ниже нормы"
modified: "2016-12-12"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc4689.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc4689.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Water in Fuel Indicator Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика воды в топливе — напряжение ниже нормы**

> [!abstract] Процедура · `122-fc4689`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-12-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc4689.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc4689.pdf)

### Fault Code: 4689

### Water in Fuel Indicator Sensor Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 4689 PID(P): SPN: 97 FMI: 4 Lamp: Maintenance SRT: | Water in Fuel Indicator Sensor Circuit - Voltage Below Normal or Shorted to Low Source. Low voltage detected at the water in fuel indicator sensor circuit. | None on performance. No water in fuel warning available. |

![[19k00130.png]]

Water in Fuel Indicator Sensor Circuit

### Circuit Description

The water in fuel indicator sensor is installed by the original equipment manufacturer (OEM). The water in fuel indicator sensor sends a signal to the engine control module (ECM) when a set volume of water has accumulated in the fuel filter. The water in fuel indicator sensor circuit contains two wires: a water in fuel indicator RETURN (sensor return 1) ground wire and a water in fuel indicator SIGNAL wire.

### Component Location

The water in fuel indicator sensor is mounted by the OEM. See equipment manufacturer service information.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM or circuit is affected.

Possible causes for this fault code include:

- Signal circuit shorted to ground in the harness, sensor, or connector.

Refer to Troubleshooting Fault Code t05-4689.
