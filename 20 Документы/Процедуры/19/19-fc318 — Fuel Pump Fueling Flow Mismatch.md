---
type: "Процедура"
doc: "19-fc318"
title_en: "Fuel Pump Fueling Flow Mismatch"
modified: "2022-05-04"
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
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc318.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc318.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Fuel Pump Fueling Flow Mismatch

> [!abstract] Процедура · `19-fc318`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2022-05-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc318.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc318.pdf)

### Fault Code: 318

### Fuel Pump Fueling Flow Mismatch

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 318 PID(P): S78 SPN: 931 FMI: 7 Lamp: Yellow SRT: 00-671 | Fuel pump pressure and desired fuel pump pressure is **not** within the calibrated values. | No action is taken by the ECM. |

![[19803917.png]]

Fuel Flow Signal Circuit - QSK19 Industrial

![[19803920.png]]

Fuel Flow Signal Circuit - QSK23 Industrial

![[19803919.png]]

Fuel Flow Signal Circuit - QSK23 Generator Drive

![[19803918.png]]

Fuel Flow Signal Circuit - QSK45 and QSK60

![[19803916.png]]

Fuel Flow Signal Circuit - QSK60

![[19803915.png]]

Fuel Flow Signal Circuit - QSK78

### Circuit Description

The Engine Control Module (ECM) uses the fuel pump pressure signal and engine speed to estimate the actual fueling the engine is receiving, and then constantly compares this value to the desired fueling for the given speed and load.

### Component Location

The fuel pump actuator is located on the fuel pump.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position or when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected a significant difference between actual and calculated fueling.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.

- The fault code status displayed by the recommended Cummins® electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.

- It is necessary to use the "Reset All Faults" command in the recommended Cummins® electronic service tool or equivalent to clear this fault.

### Shoptalk

This fault is a check on the ECM's control of the fuel pump actuator and subsequent fuel flow. If the desired fueling can **not** be met by commanding less current to the actuator, or if the desired fueling is being exceeded and can **not** be reduced by increasing the current to the actuator, then Fault Code 318 is logged.

Refer to Troubleshooting Fault Code t05-318
