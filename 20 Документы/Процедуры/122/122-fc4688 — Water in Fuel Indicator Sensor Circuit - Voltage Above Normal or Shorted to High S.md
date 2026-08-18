---
aliases:
  - "Цепь датчика воды в топливе — напряжение выше нормы"
type: "Процедура"
doc: "122-fc4688"
title_en: "Water in Fuel Indicator Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика воды в топливе — напряжение выше нормы"
modified: "2017-01-02"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc4688.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc4688.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Water in Fuel Indicator Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика воды в топливе — напряжение выше нормы**

> [!abstract] Процедура · `122-fc4688`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-01-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc4688.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc4688.pdf)

### Fault Code: 4688

### Water in Fuel Indicator Sensor Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 4688 PID(P): SPN: 97 FMI: 3 Lamp: Maintenance SRT: | Water in Fuel Indicator Sensor Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the water in fuel indicator circuit. | None on performance. No water in fuel warning available. |

![[19k00130.png]]

Water in Fuel Indicator Sensor Circuit

### Circuit Description

The water in fuel indicator sensor is fitted by the original engine manufacturer (OEM). The water in fuel indicator sensor sends a signal to the engine control module (ECM) when a set volume of water has accumulated in the fuel filter. The water in fuel indicator sensor circuit contains two wires: a water in fuel indicator RETURN (sensor return 1) ground wire and a water in fuel indicator SIGNAL wire.

### Component Location

The water in fuel indicator sensor is mounted by the original equipment manufacturer (OEM). Refer to the OEM service manual.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected.. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

Possible causes of this fault code include:

- Open return or signal circuit in the harness, connectors, or sensor

- SIGNAL wire shorted to sensor supply or battery voltage.

Refer to Troubleshooting Fault Code t05-4688.
