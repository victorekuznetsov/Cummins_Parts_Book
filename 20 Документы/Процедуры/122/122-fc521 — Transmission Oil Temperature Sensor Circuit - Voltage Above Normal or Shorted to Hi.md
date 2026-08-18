---
aliases:
  - "Цепь датчика температуры масла трансмиссии — напряжение выше нормы"
type: "Процедура"
doc: "122-fc521"
title_en: "Transmission Oil Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика температуры масла трансмиссии — напряжение выше нормы"
modified: "2016-12-07"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc521.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc521.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Transmission Oil Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика температуры масла трансмиссии — напряжение выше нормы**

> [!abstract] Процедура · `122-fc521`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-12-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc521.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc521.pdf)

### Fault Code: 521

### Transmission Oil Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 521 PID(P): SPN: 175 FMI: 3 Lamp: Amber SRT: | Transmission (Gear) Oil Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source. High signal voltage detected at transmission (gear) oil temperature sensor circuit. | **No** engine protection for transmission oil temperature. |

![[19k00131.png]]

Transmission (Gear) Oil Temperature Sensor Circuit

### Circuit Description

The transmission (gear) oil temperature sensor is used by the engine control module (ECM) to monitor the transmission oil temperature. The ECM monitors the voltage on the SIGNAL pin and converts it to a temperature value.

### Component Location

The transmission (gear) oil temperature sensor is located in the transmission.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

Before troubleshooting Fault Code 521, check for multiple faults.

The transmission (gear) oil temperature sensor share RETURN wires in the engine harness with other sensors. An open return can cause multiple fault codes to be active.

Possible causes for this fault code include:

- Open return circuit in the harness, connectors, or sensor

- Open signal circuit or shorted to a voltage source.

Refer to Troubleshooting Fault Code 521.
