---
aliases:
  - "Привод топливной рампы — замыкание на плюс"
type: "Процедура"
doc: "01-fc455"
title_en: "Fuel Rail Actuator - Shorted High"
title_ru: "Привод топливной рампы — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc455.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc455.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Rail Actuator - Shorted High
**Привод топливной рампы — замыкание на плюс**

> [!abstract] Процедура · `01-fc455`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc455.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc455.pdf)

### Fault Code: 455

### Fuel Rail Actuator - Shorted High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 455 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Fuel control valve circuit - shorted high. This was formerly called the fuel rail actuator circuit. Fuel rail actuator circuit is open, the fuel rail actuator signal pin is shorted to battery voltage or ground, or the fuel rail actuator return pin is shorted to battery voltage or ground. | Engine will run at one speed or will shutdown. Fault Code 514 may also be logged. |

![[19803582.png]]

Fuel Rail Actuator Circuit

### Circuit Description

The fuel rail actuator is a device used by the electronic control module (ECM) to control the engine fuel supply. The ECM can shut down the engine by cutting off the power to the fuel rail actuator.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Confirm that the valve connector is firmly in place. When there is shorted power to the actuator, the actuator opens and fuel flow is uncontrolled. This will cause Fault Code 234, engine overspeed, or Fault Code 514, fueling flow mismatch.

Refer to Troubleshooting Fault Code t05-455
