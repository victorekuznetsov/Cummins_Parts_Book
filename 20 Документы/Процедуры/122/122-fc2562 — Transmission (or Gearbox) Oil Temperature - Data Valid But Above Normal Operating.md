---
aliases:
  - "Температура масла трансмиссии выше нормы — наивысший уровень"
type: "Процедура"
doc: "122-fc2562"
title_en: "Transmission (or Gearbox) Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Температура масла трансмиссии выше нормы — наивысший уровень"
modified: "2016-12-12"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc2562.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc2562.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Transmission (or Gearbox) Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level
**Температура масла трансмиссии выше нормы — наивысший уровень**

> [!abstract] Процедура · `122-fc2562`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-12-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc2562.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc2562.pdf)

### Fault Code: 2562

### Transmission (or Gearbox) Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2562 PCODE(P): SPN: 175 FMI: 0 Lamp: Red SRT: | Transmission (or Gearbox) Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level. Transmission (or gearbox) oil temperature sensor indicates the transmission (or gearbox) oil temperature is above the protection limit. | **No** engine protection for transmission oil temperature. |

![[19k00131.png]]

Transmission (or Gearbox) Oil Temperature Sensor Circuit

### Circuit Description

Transmission (or gearbox) oil temperature sensor is used by the engine control module (ECM) to monitor the transmission oil temperature. The ECM monitors the voltage on the SIGNAL pin and converts it to a temperature value.

### Component Location

The Transmission (or gearbox) oil temperature sensor is located in the transmission.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

This fault code indicates that the transmission (or gearbox) temperature has exceeded the protection limits for high transmission (or gearbox) temperature.

Refer to Troubleshooting Fault Code 2562.
