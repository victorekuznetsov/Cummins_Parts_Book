---
aliases:
  - "Вход вспомогательного датчика давления 1 — особые указания"
type: "Процедура"
doc: "122-fc1544"
title_en: "Auxiliary Pressure Sensor Input 1 - Special Instructions"
title_ru: "Вход вспомогательного датчика давления 1 — особые указания"
modified: "2012-01-17"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 4
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc1544.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc1544.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Auxiliary Pressure Sensor Input 1 - Special Instructions
**Вход вспомогательного датчика давления 1 — особые указания**

> [!abstract] Процедура · `122-fc1544`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-01-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc1544.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc1544.pdf)

### Fault Code: 1544

### Auxiliary Pressure Sensor Input 1 - Special Instructions

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1544 PID(P): SPN: 1387 FMI: 14 Lamp: Maintenance SRT: | Auxiliary Pressure Sensor Input 1 - Special Instructions | Possible engine power derate or engine shutdown, depending on the OEM calibration. |

![[19602245.png]]

QSK38 CM2150 Industrial - Auxiliary Pressure Sensor Input 1 Circuit

![[19602246.png]]

QSK38 CM2150 Marine - Auxiliary Pressure Sensor Input 1 Circuit

![[19602247.png]]

QSK50 and QSK60 CM2150 Industrial - Auxiliary Pressure Sensor Input 1 Circuit

![[19602248.png]]

QSK50 and QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - Auxiliary Pressure Sensor Input 1 Circuit

### Circuit Description

The original equipment manufacturer (OEM) has the option of wiring a pressure sensor input to the electronic control module (ECM). A specific calibration is then created to recognize the auxiliary pressure sensor input 1. This fault code is activated when the pressure input from the OEM sensor exceeds the engine protection limit defined by the OEM. In marine applications, this sensor monitors gear oil pressure and the fault code is activated when the pressure falls below a threshold which is an INSITE™ electronic service tool adjustable parameter. Depending on the OEM requirements, an engine protection derate or even engine shutdown can be associated with the fault code.

### Component Location

The OEM pressure sensor input will vary depending on application. Refer to the OEM troubleshooting and repair manual for sensor location.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

This fault code is activated when the pressure input from the OEM sensor exceeds the engine protection limit defined by the OEM. An engine power derate is possible depending on the OEM application.

In marine applications, the default setting is intentionally set higher than any possible gear oil pressure. This is so the fault code will become active immediately after recalibration where the adjustable parameters were not overlaid on the new calibration. This prevents the customer from the assumption that he is protected by this lamp when the parameters were not adjusted properly. When the gear oil pressure sensor is not installed, the factory installed resistor is designed to signal to the ECM that gear oil pressure conditions are satisfactory at all times.

Note: The fault code will only go inactive if the ECM sees a known condition for a period (about five seconds) and with the engine running above 1000 RPM.

Refer to Troubleshooting Fault Code 1544.
