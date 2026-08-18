---
aliases:
  - "Низкое давление охлаждающей жидкости — критично"
type: "Процедура"
doc: "01-fc228"
title_en: "Engine Coolant Pressure Low - Critical"
title_ru: "Низкое давление охлаждающей жидкости — критично"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc228.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc228.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Coolant Pressure Low - Critical
**Низкое давление охлаждающей жидкости — критично**

> [!abstract] Процедура · `01-fc228`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc228.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc228.pdf)

### Fault Code: 228

### Engine Coolant Pressure Low - Critical

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 228 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine coolant pressure low - critical. Voltage signal indicates coolant pressure has dropped below the shutdown threshold for low coolant pressure. | Engine will shut down. |

![[19803583.png]]

Coolant Pressure Sensor Circuit

### Circuit Description

The coolant pressure sensor is used by the electronic control module (ECM) to monitor coolant pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The coolant pressure value is used by the ECM for the engine protection system.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Confirm that the coolant pressure sensor supply voltage is between 4.75 and 5.25 VDC at the sensor. See Fault Code 232.

Refer to specific engine wiring diagram for the output voltage of the pressure sensor.

NOTE: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.

Refer to Troubleshooting Fault Code t05-228
