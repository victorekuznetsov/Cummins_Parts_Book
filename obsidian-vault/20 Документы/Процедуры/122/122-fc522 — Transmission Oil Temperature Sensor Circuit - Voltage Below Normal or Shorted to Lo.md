---
aliases:
  - "Цепь датчика температуры масла трансмиссии — напряжение ниже нормы"
type: "Процедура"
doc: "122-fc522"
title_en: "Transmission Oil Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика температуры масла трансмиссии — напряжение ниже нормы"
modified: "2017-01-02"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc522.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc522.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Transmission Oil Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика температуры масла трансмиссии — напряжение ниже нормы**

> [!abstract] Процедура · `122-fc522`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-01-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc522.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc522.pdf)

### Fault Code: 522

### Transmission Oil Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 522 PID(P): SPN: 175 FMI: 4 Lamp: Amber SRT: | Transmission Oil Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source. Low signal voltage detected at transmission (gear) oil temperature circuit. | **No** engine protection for transmission oil temperature. |

![[19k00131.png]]

Transmission (Gear) Oil Temperature Sensor Circuit

### Circuit Description

Transmission (gear) oil temperature sensor is used by the engine control module (ECM) to monitor the transmission oil temperature. The ECM monitors the voltage on the SIGNAL pin and converts it to a temperature value.

### Component Location

The transmission (gear) oil temperature sensor is located in the transmission.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

The transmission (gear) oil temperature sensor shares RETURN wires in the engine harness with other sensors. A shorted return can cause multiple fault codes to be active. Before troubleshooting Fault Code 522, check for multiple fault codes.

Possible causes of this fault code include:

- Signal shorted to ground in the harness.

- Signal shorted to return or ground in the sensor.

Refer to Troubleshooting Fault Code 522.
