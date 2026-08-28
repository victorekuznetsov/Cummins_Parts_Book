---
aliases:
  - "Цепь вспомогательного датчика температуры 1 — напряжение ниже нормы"
type: "Процедура"
doc: "87-fc294"
title_en: "Auxiliary Temperature Sensor Input 1 Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь вспомогательного датчика температуры 1 — напряжение ниже нормы"
modified: "2018-08-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc294.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc294.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Auxiliary Temperature Sensor Input 1 Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь вспомогательного датчика температуры 1 — напряжение ниже нормы**

> [!abstract] Процедура · `87-fc294`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc294.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc294.pdf)

### Fault Code: 294

### Auxiliary Temperature Sensor Input 1 Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 294 PID(P): P441 SPN: 441 FMI: 4 Lamp: Amber SRT: | Auxiliary Temperature Sensor Input 1 Circuit - Voltage Below Normal or Shorted to Low Source. Voltage detected at the original equipment manufacturer (OEM) auxiliary temperature sensor supply pin of the left bank OEM interface wiring harness indicates the sensor has failed low. | None on performance. |

![[19n00476.png]]

OEM Auxiliary Temperature Sensor Circuit

### Circuit Description

The OEM auxiliary temperature sensor supply is used by the engine control module (ECM) to monitor OEM auxiliary temperature. An OEM auxiliary temperature sensor that has failed low can be caused by shorts to ground or opens in the supply and return wires, or an internally grounded sensor.

### Component Location

The component location will vary depending on the OEM. See equipment manufacturer service information.

### Shoptalk

The resistance of all temperature sensors varies with the temperature. Check the temperature thresholds using INSITE™ electronic service tool for QST Series engines.

Refer to Troubleshooting Fault Code t05-294
