---
aliases:
  - "Цепь датчика температуры топлива — замыкание на массу"
type: "Процедура"
doc: "87-fc265"
title_en: "Fuel Temperature Sensor Circuit - Shorted Low"
title_ru: "Цепь датчика температуры топлива — замыкание на массу"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc265.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc265.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Fuel Temperature Sensor Circuit - Shorted Low
**Цепь датчика температуры топлива — замыкание на массу**

> [!abstract] Процедура · `87-fc265`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc265.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc265.pdf)

### Fault Code: 265

### Fuel Temperature Sensor Circuit - Shorted Low

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 265 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine fuel temperature sensor signal is shorted low. | No engine protection for fuel temperature. No effect on performance. |

![[19803592.png]]

Fuel Temperature Sensor Circuit

### Circuit Description

The fuel temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the fuel. The fuel temperature is used by the ECM for the engine protection system, timing, and fueling control. If the voltage is low, the ECM will log Fault Code 265. Low voltage can be caused by shorts to ground on the supply or return wires or an internally grounded, failed sensor.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

The resistance of the sensor varies with the temperature.

Refer to Troubleshooting Fault Code t05-265
