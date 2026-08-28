---
aliases:
  - "Цепь потенциометра статизма — напряжение ниже нормы"
type: "Процедура"
doc: "122-fc3696"
title_en: "Droop Adjust Potentiometer Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь потенциометра статизма — напряжение ниже нормы"
modified: "2010-09-27"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc3696.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc3696.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Droop Adjust Potentiometer Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь потенциометра статизма — напряжение ниже нормы**

> [!abstract] Процедура · `122-fc3696`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc3696.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc3696.pdf)

### Fault Code: 3696

### Droop Adjust Potentiometer Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 3696 PID(P): SPN: 4183 FMI: 4 Lamp: Amber SRT: | Droop Adjust Potentiometer Circuit - Voltage Below Normal or Shorted to Low Source | The droop adjust potentiometer will go to the default value. |

![[19e00970.png]]

QSK38 CM2150 Power Generation -Droop Adjust Potentiometer Circuit

![[19602288.png]]

QSK50 CM2150 without Advanced Engine Monitoring/QSK50 CM2150 with Advanced Engine Monitoring/QSK60 CM2150 Power Generation - Droop Adjust Potentiometer Circuit

![[19602296.png]]

QSK38 CM2150 Marine Auxiliary with C Command Elite™ and C Command Elite Plus™ Panel System - Droop Adjust Potentiometer Circuit

![[19602297.png]]

QSK38 CM2150 Marine Auxiliary with C Command™ Panel System - Droop Adjust Potentiometer Circuit

![[19602288.png]]

QSK50 and QSK60 CM2150 Marine Auxiliary with C Command Elite™ and C Command Elite Plus™ Panel System/QSK60 CM2150 Drill Rig - Droop Adjust Potentiometer Circuit

![[19602299.png]]

QSK50 and QSK60 CM2150 Marine Auxiliary with C Command™ Panel System - Droop Adjust Potentiometer Circuit

### Circuit Description

The droop adjust potentiometer is used to regulate the engine droop.

### Component Location

The droop adjust potentiometer is located on the generator control panel. Refer to the OEM service manual.

### Shoptalk

There are multiple electronic control module (ECM)s for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

Possible causes of the fault code include:

- SIGNAL wire open or shorted to ground

- SUPPLY wire open or shorted to ground.

Refer to Troubleshooting Fault Code 3696.
