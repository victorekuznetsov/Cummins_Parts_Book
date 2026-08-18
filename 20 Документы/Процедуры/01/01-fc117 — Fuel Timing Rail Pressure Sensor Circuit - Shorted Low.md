---
aliases:
  - "Цепь датчика давления рампы опережения — замыкание на массу"
type: "Процедура"
doc: "01-fc117"
title_en: "Fuel Timing Rail Pressure Sensor Circuit - Shorted Low"
title_ru: "Цепь датчика давления рампы опережения — замыкание на массу"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc117.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc117.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Timing Rail Pressure Sensor Circuit - Shorted Low
**Цепь датчика давления рампы опережения — замыкание на массу**

> [!abstract] Процедура · `01-fc117`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc117.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc117.pdf)

### Fault Code: 117

### Fuel Timing Rail Pressure Sensor Circuit - Shorted Low

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 117 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Fuel timing pressure sensor circuit - shorted low. | Calibration-dependent engine shutdown occurs, or no action is taken by ECM. |

![[19803583.png]]

Fuel Timing Rail Pressure Sensor Circuit

### Circuit Description

The timing rail pressure sensor provides the timing rail pressure signal to the electronic control module (ECM), through the engine harness. The ECM uses the timing rail pressure signal to monitor the timing rail pressure going to the injector's timing chamber from the control valve body.

### Component Location

The timing rail pressure sensor is located on the right-side, toward the top, of the ECVA (toward top), across from the timing rail actuators.

### Shoptalk

Refer to specific engine wiring diagram for the output voltage of the pressure sensor.

Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.

Refer to Troubleshooting Fault Code t05-117
