---
aliases:
  - "Ошибка датчика давления в топливной рампе"
type: "Процедура"
doc: "01-fc554"
title_en: "Fuel Rail Pressure Sensor Error"
title_ru: "Ошибка датчика давления в топливной рампе"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc554.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc554.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Rail Pressure Sensor Error
**Ошибка датчика давления в топливной рампе**

> [!abstract] Процедура · `01-fc554`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc554.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc554.pdf)

### Fault Code: 554

### Fuel Rail Pressure Sensor Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 554 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel pressure sensor error. Fuel rail pressure sensor in-range error detected at key-on. Voltage signal indicates that the fuel rail pressure sensor signal can possibly **not** be accurate. | No action taken by the ECM. Possible loss of performance. |

![[19803583.png]]

Fuel Rail Pressure Sensor Circuit

### Circuit Description

The fuel rail pressure sensor provides the fuel rail pressure signal to the electronic control module (ECM), through the engine harness. The ECM uses the fuel rail pressure signal to monitor the fuel pressure going to the injectors from the control valve body.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

The fuel rail pressure sensor is located on the right side, toward the bottom of the ECVA, across from the fuel rail actuator.

### Shoptalk

Refer to specific engine wiring diagram for the output voltage of the pressure sensor.

Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.

Refer to Troubleshooting Fault Code t05-554
