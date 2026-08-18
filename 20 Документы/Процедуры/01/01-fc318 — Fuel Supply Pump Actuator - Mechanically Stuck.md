---
aliases:
  - "Исполнительный механизм топливоподающего насоса — механически заклинил"
type: "Процедура"
doc: "01-fc318"
title_en: "Fuel Supply Pump Actuator - Mechanically Stuck"
title_ru: "Исполнительный механизм топливоподающего насоса — механически заклинил"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc318.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc318.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Supply Pump Actuator - Mechanically Stuck
**Исполнительный механизм топливоподающего насоса — механически заклинил**

> [!abstract] Процедура · `01-fc318`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc318.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc318.pdf)

### Fault Code: 318

### Fuel Supply Pump Actuator - Mechanically Stuck

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 318 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel supply pump actuator - mechanically stuck. The error between the estimated fuel pump pressure and the desired fuel pump pressure is outside the allowable limits. | No action is taken by the ECM. Possible loss of performance. |

![[19400781.png]]

Fuel System Flow Schematic

### Circuit Description

The ECM uses the fuel pump pressure signal and engine speed to estimate the actual fueling the engine is receiving, and constantly compares this value to the desired fueling for the given speed and load. When there is too large of an error in these values for too long of a time, Fault Code 318 is logged.

### Component Location

The fuel pump actuator is on the fuel pump, just below the fuel pressure sensor.

### Shoptalk

This fault is a check on the ECM's control of the fuel pump actuator and subsequent fuel flow. If the desired fueling can **not** be met by commanding more current to the actuator or if the desired fueling is being exceeded and can **not** be reduced by limiting the amount of current to the actuator, then Fault Code 318 is logged. Fault Code 318 is **not** logged if the coolant temperature is below 0°C \[32°F\].

- Make sure that the correct calibration loaded into the ECM. For example, if a QSK45 calibration is loaded into a QSK60 ECM, this fault code will be activated.

- Check for air in the fuel system.

- Check for high fuel inlet restriction (plugged fuel filter, etc.)

Refer to Troubleshooting Fault Code t05-318
