---
type: "Процедура"
doc: "19-fc514"
title_en: "Rail Fueling Flow Mismatch"
modified: "2011-03-01"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc514.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc514.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Rail Fueling Flow Mismatch

> [!abstract] Процедура · `19-fc514`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc514.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc514.pdf)

### Fault Code: 514

### Rail Fueling Flow Mismatch

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 514 PID(P): S18 SPN: 633 FMI: 7 Lamp: Red SRT: 00-378 | The error between the estimated rail fueling and the desired rail fueling is outside the acceptable limits. | Calibration-dependent engine shutdown or power derate or no action by the ECM is taken. Engine will overspeed, or run at one speed or **not** run. |

![[19400109.png]]

Fuel System Flow Schematic

### Circuit Description

The electronic control module (ECM) uses the rail pressure signal and the engine speed to estimate the actual fueling that the engine is receiving and then constantly compares this value to the desired fueling for the given speed and load. When there is too large an error in these values for too long a time, this fault is logged.

### Component Location

The rail actuator is located on the bottom of the control valve body, toward the engine front, behind the ECM.

### Shoptalk

The estimated rail fueling and the desired rail fueling parameters can be monitored on INSITE™ electronic service tool. This fault is a check on the ECM's control of the rail actuator and subsequent fuel flow. If the desired rail fueling can **not** be met by commanding more current to the actuator, or if the desired fuel railing is being exceeded and can **not** be reduced by reducing the current to the actuator, this fault is logged.

This fault is **not** logged when:

- Engine speed is below 1200 rpm

- Coolant temperature is below 0°C \[32°F\]

- Fault Code 451 or 452 is active. Once the keyswitch is cycled, the fault becomes inactive.

Refer to Troubleshooting Fault Code t05-514
