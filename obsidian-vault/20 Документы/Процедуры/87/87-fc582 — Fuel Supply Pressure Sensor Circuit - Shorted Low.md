---
aliases:
  - "Цепь датчика давления подачи топлива — замыкание на массу"
type: "Процедура"
doc: "87-fc582"
title_en: "Fuel Supply Pressure Sensor Circuit - Shorted Low"
title_ru: "Цепь датчика давления подачи топлива — замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc582.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc582.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Fuel Supply Pressure Sensor Circuit - Shorted Low
**Цепь датчика давления подачи топлива — замыкание на массу**

> [!abstract] Процедура · `87-fc582`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc582.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc582.pdf)

### Fault Code: 582

### Fuel Supply Pressure Sensor Circuit - Shorted Low

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 582 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel supply pressure sensor circuit - shorted low. | No action taken by the ECM. Possible loss of performance. |

![[19803583.png]]

Fuel Supply Pressure Sensor Circuit

### Circuit Description

The fuel supply pressure sensor provides the fuel pressure supply signal to the electronic control module (ECM). This fault indicates that the signal pin on the ECM has been shorted to ground.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Refer to specific engine wiring diagram for the output voltage of the pressure sensor.

Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.

Refer to Troubleshooting Fault Code t05-582
