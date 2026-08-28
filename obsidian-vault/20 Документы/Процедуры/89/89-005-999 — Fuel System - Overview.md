---
aliases:
  - "Топливная система — обзор"
type: "Процедура"
doc: "89-005-999"
title_en: "Fuel System - Overview"
title_ru: "Топливная система — обзор"
modified: "2003-07-08"
engines:
  - "85017333"
families:
  - "QSK23"
manuals:
  - "4021375"
figures: 3
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-005-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-005-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
---

# Fuel System - Overview
**Топливная система — обзор**

> [!abstract] Процедура · `89-005-999`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-005-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-005-999.pdf)

### General Information

Fuel System

The QSK23 engine is equipped with the Quantum™ fuel system. The Quantum™ fuel system provides full electronic control of the engine with high-pressure fuel injection.

Operation

The QSK23 fuel pump supplies regulated pressure to the control valve assembly for the rail and timing as a function of speed. The fuel is supplied to both the rail and timing actuators. The actuators act as throttles to control the amount of fuel metered to the injector and timing supply lines. Timing and rail pressure sensors, after the actuators, measure the actual supplied pressures. The ECM compares the actual supplied pressures to the desired supply pressures. Desired supply pressure is based on throttle position and speed inputs. The ECM then communicates to the actuator to change spool plunger position which changes the flow orifice area until the desired pressures are obtained.

Fuel Filter

The QSK23 requires two 10-micron fuel filters with water separators, Fleetguard® Part Number FS1006, to provide injector and control valve protection.

![[05400181.png]]

Fuel Pump

The QSK23 has an electronically-controlled fuel pump that regulates output pressure to specific values based on a given engine speed. The pump has a fuel bypass regulator circuit controlled by an actuator. The actuator receives its command from the ECM based on the pump pressure sensor and the engine speed sensor.

The QSK23 fuel pump is very similar to the pump used on QSK45, QSK60, and QSK78 series engines.

![[05400183.png]]

Electronic Control Valve Assembly (ECVA)

The electronic control valve assembly is located on the fuel pump side of the engine. The assembly contains the following actuators and sensors:

1. Timing rail pressure sensor
2. Fuel rail pressure sensor
3. Barometric pressure sensor
4. Fuel rail actuator
5. Fuel temperature sensor
6. Timing rail actuator
7. Fuel supply inlet
8. Timing rail outlet
9. Fuel rail outlet
10. Fuel shutoff valve.

![[05400182.png]]
