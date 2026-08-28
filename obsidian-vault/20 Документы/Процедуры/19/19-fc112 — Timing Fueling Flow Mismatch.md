---
type: "Процедура"
doc: "19-fc112"
title_en: "Timing Fueling Flow Mismatch"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc112.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc112.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Timing Fueling Flow Mismatch

> [!abstract] Процедура · `19-fc112`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc112.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc112.pdf)

### Fault Code: 112

### Timing Fueling Flow Mismatch

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 112 PID(P): S20 SPN: 635 FMI: 7 Lamp: Red SRT: 00-342 | The error between estimated timing fueling and desired timing fueling is outside acceptable limits. | Depending on the calibration, the engine will shut down or speed-derate or no action by the ECM is taken. |

![[19400109.png]]

Fuel System Flow Schematic

### Circuit Description

The electronic control module (ECM) uses the timing pressure signal and engine speed to estimate the actual timing the engine is receiving and then constantly compares this value to the desired timing for the given speed and load. When there is too large an error in these values for too long a time, this fault is logged.

### Component Location

The timing actuator is located on the top of the control valve body, toward the front of the engine and behind the ECM.

### Shoptalk

The estimated timing fueling and the desired timing fueling parameters can be monitored on INSITE™ electronic service tool. This fault is a check on the ECM's control of the timing actuator and subsequent fuel flow. If the desired timing fueling can **not** be met by commanding more current to the actuator or if the desired timing fueling is being exceeded and can **not** be reduced by reducing the current to the actuator, this fault is logged.

This fault is **not** logged when:

- Coolant temperature is below 0°C \[32°F\].

- Fault Code 116 or 117 is active.

- Once the keyswitch is cycled, this fault becomes inactive.

Refer to Troubleshooting Fault Code t05-112
