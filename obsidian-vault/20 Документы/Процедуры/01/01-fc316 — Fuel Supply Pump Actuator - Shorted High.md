---
aliases:
  - "Исполнительный механизм топливоподающего насоса — замыкание на плюс"
type: "Процедура"
doc: "01-fc316"
title_en: "Fuel Supply Pump Actuator - Shorted High"
title_ru: "Исполнительный механизм топливоподающего насоса — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc316.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc316.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Supply Pump Actuator - Shorted High
**Исполнительный механизм топливоподающего насоса — замыкание на плюс**

> [!abstract] Процедура · `01-fc316`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc316.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc316.pdf)

### Fault Code: 316

### Fuel Supply Pump Actuator - Shorted High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 316 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel supply pump actuator circuit - shorted high. Fuel pump actuator circuit is open, the fuel pump actuator signal pin is shorted to battery voltage or ground, or fuel pump actuator return pin is shorted to battery voltage or ground. | No action is taken by the ECM. Possible loss of performance. Actuator is open, closed, or partially closed. |

![[19803582.png]]

Fuel Supply Pump Actuator Circuit

### Circuit Description

The fuel pump actuator circuit supplies current to the fuel pump actuator. The ECM commands a varying amount of current to the fuel pump actuator to control the fuel pump output pressure to the control valve assembly.

### Component Location

The fuel pump actuator is on the fuel pump, just below the fuel pump sensor.

### Shoptalk

Confirm that the actuator connector is firmly in place. When there is no power to the actuator, the actuator closes and fuel flow continues.

Refer to Troubleshooting Fault Code t05-316
