---
aliases:
  - "Цепь датчика температуры масла — замыкание на массу"
type: "Процедура"
doc: "01-fc213"
title_en: "Engine Oil Temperature Sensor Circuit - Shorted Low"
title_ru: "Цепь датчика температуры масла — замыкание на массу"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc213.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc213.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Oil Temperature Sensor Circuit - Shorted Low
**Цепь датчика температуры масла — замыкание на массу**

> [!abstract] Процедура · `01-fc213`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc213.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc213.pdf)

### Fault Code: 213

### Engine Oil Temperature Sensor Circuit - Shorted Low

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 213 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine oil temperature sensor signal is shorted low. | No engine protection for the oil temperature. No effect on performance. |

![[19803595.png]]

Oil Temperature Sensor Circuit

### Circuit Description

The oil temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine oil. If the oil temperature becomes too high and engine protection is enabled, a derate condition will be incurred, possibly leading to shutdown.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

The resistance of the sensor varies with the temperature.

Refer to Troubleshooting Fault Code t05-213
