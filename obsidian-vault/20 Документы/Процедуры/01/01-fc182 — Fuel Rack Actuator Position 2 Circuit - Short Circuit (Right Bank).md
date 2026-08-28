---
aliases:
  - "Цепь положения привода рейки 2 — короткое замыкание (правый ряд)"
type: "Процедура"
doc: "01-fc182"
title_en: "Fuel Rack Actuator Position 2 Circuit - Short Circuit (Right Bank)"
title_ru: "Цепь положения привода рейки 2 — короткое замыкание (правый ряд)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc182.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc182.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Rack Actuator Position 2 Circuit - Short Circuit (Right Bank)
**Цепь положения привода рейки 2 — короткое замыкание (правый ряд)**

> [!abstract] Процедура · `01-fc182`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc182.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc182.pdf)

### Fault Code: 182

### Fuel Rack Actuator Position 2 Circuit - Short Circuit (Right Bank)

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 182 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Fuel rack actuator position 2 circuit - short circuit (right bank). | Engine can possibly shut down due to an overspeed. Fault Code 2975 can possibly also activate. |

![[19803599.png]]

Fuel Rack Actuator Position 2 Circuit

### Circuit Description

The fuel rack actuators are actuated by the ECM to control fuel metering. Each rack actuator is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the rack actuator from the ECM on the supply wire and returns to the ECM on the return wire. Each solenoid valve is normally closed, and it is **only** opened by an electrical pulse from the ECM during metering. This test checks to see that the current being supplied from the ECM to the actuator is being fed back to the ECM on the return circuit.

### Component Location

The rack actuator is part of the right bank fuel pump.

### Shoptalk

This fault requires engine speed greater than zero before the fault will go active.

The possible failure modes are low actuator resistance or the fuel rack actuator PWM2 supply shorted to battery.

This fault code procedure also provides for troubleshooting when the fuel rack actuator PWM2 return is shorted to ground. This type of failure will **not** cause a fault code at this time, but will cause the engine to run rough.

If Fault Code 2975 and Fault Code 182 are active, troubleshoot Fault Code 182 first.

Refer to Troubleshooting Fault Code t05-182
