---
aliases:
  - "Цепь датчика температуры топлива — замыкание на плюс"
type: "Процедура"
doc: "87-fc263"
title_en: "Fuel Temperature Sensor Circuit - Shorted High"
title_ru: "Цепь датчика температуры топлива — замыкание на плюс"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc263.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc263.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Fuel Temperature Sensor Circuit - Shorted High
**Цепь датчика температуры топлива — замыкание на плюс**

> [!abstract] Процедура · `87-fc263`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc263.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc263.pdf)

### Fault Code: 263

### Fuel Temperature Sensor Circuit - Shorted High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 263 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine fuel temperature sensor signal is shorted high. | No engine protection for fuel temperature. No effect on performance. |

![[19803592.png]]

Fuel Temperature Sensor Circuit

### Circuit Description

The fuel temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the fuel. The fuel temperature is used by the ECM for the engine protection system, timing, and fueling control. If the voltage is high, the ECM will log Fault Code 263. High voltage can be caused by opens in the signal or return wires, voltage shorts to the signal or return wires, or a failed open sensor.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

The resistance of the sensor varies with the temperature.

Refer to Troubleshooting Fault Code t05-263
