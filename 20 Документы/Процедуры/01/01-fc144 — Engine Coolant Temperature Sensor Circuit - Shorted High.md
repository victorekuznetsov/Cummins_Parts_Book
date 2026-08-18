---
aliases:
  - "Цепь датчика температуры ОЖ — замыкание на плюс"
type: "Процедура"
doc: "01-fc144"
title_en: "Engine Coolant Temperature Sensor Circuit - Shorted High"
title_ru: "Цепь датчика температуры ОЖ — замыкание на плюс"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc144.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc144.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Coolant Temperature Sensor Circuit - Shorted High
**Цепь датчика температуры ОЖ — замыкание на плюс**

> [!abstract] Процедура · `01-fc144`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc144.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc144.pdf)

### Fault Code: 144

### Engine Coolant Temperature Sensor Circuit - Shorted High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 144 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine coolant temperature sensor signal is shorted high. | No engine protection for coolant temperature. Possible white smoke. |

![[19803592.png]]

Engine Coolant Temperature Sensor Circuit

### Circuit Description

The coolant temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system, timing, and fueling control. If the voltage is high, the ECM will log Fault Code 144. Voltage high can be caused by opens in the signal or return wires, voltage shorts to the signal or return wires, or a failed open sensor.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

The resistance of the sensor varies with the temperature.

Refer to Troubleshooting Fault Code t05-144
