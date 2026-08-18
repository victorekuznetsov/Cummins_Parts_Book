---
aliases:
  - "Цепь датчика давления ОЖ — замыкание на плюс"
type: "Процедура"
doc: "01-fc231"
title_en: "Engine Coolant Pressure Sensor Circuit - Shorted High"
title_ru: "Цепь датчика давления ОЖ — замыкание на плюс"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc231.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc231.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Coolant Pressure Sensor Circuit - Shorted High
**Цепь датчика давления ОЖ — замыкание на плюс**

> [!abstract] Процедура · `01-fc231`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc231.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc231.pdf)

### Fault Code: 231

### Engine Coolant Pressure Sensor Circuit - Shorted High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 231 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine coolant pressure sensor circuit - shorted high. | No engine protection for coolant pressure. |

![[19803583.png]]

Coolant Pressure Sensor Circuit

### Circuit Description

The coolant pressure sensor monitors coolant pressure and passes information to the electronic control module (ECM). High voltage will trip Fault Code 231 and can be caused by shorts in the supply, signal, or return wires, an open in the return wire, or a failed sensor.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Confirm that the radiator cap is installed correctly.

Check the radiator cap for proper operation.

Refer to specific engine wiring diagram for the output voltage of the pressure sensor.

Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.

Refer to Troubleshooting Fault Code t05-231
