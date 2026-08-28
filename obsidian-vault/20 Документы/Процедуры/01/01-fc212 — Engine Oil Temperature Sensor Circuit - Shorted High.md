---
aliases:
  - "Цепь датчика температуры масла — замыкание на плюс"
type: "Процедура"
doc: "01-fc212"
title_en: "Engine Oil Temperature Sensor Circuit - Shorted High"
title_ru: "Цепь датчика температуры масла — замыкание на плюс"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc212.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc212.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Oil Temperature Sensor Circuit - Shorted High
**Цепь датчика температуры масла — замыкание на плюс**

> [!abstract] Процедура · `01-fc212`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc212.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc212.pdf)

### Fault Code: 212

### Engine Oil Temperature Sensor Circuit - Shorted High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 212 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine oil temperature sensor signal is shorted high. | No engine protection for oil temperature. No effect on performance. |

![[19803595.png]]

Oil Temperature Sensor Circuit

### Circuit Description

The oil temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine oil. If the oil temperature becomes too high and the engine protection is enabled, a derate condition can be incurred, possibly leading to shutdown.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

The resistance of the sensor varies with the temperature.

Refer to Troubleshooting Fault Code t05-212
