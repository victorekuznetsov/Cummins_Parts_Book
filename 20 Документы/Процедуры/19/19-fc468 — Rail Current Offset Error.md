---
type: "Процедура"
doc: "19-fc468"
title_en: "Rail Current Offset Error"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc468.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc468.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Rail Current Offset Error

> [!abstract] Процедура · `19-fc468`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc468.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc468.pdf)

### Fault Code: 468

### Rail Current Offset Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 468 PID(P): S18 SPN: 633 FMI: 2 Lamp: Yellow SRT: 00-673 | The rail current offset, used to adjust fueling flow, has reached the maximum or minimum threshold. | No action taken by the ECM. |

![[19400109.png]]

Fuel System Flow Schematic

### Circuit Description

The ECM uses the rail pressure signal and the engine speed to estimate the actual fueling that the engine is receiving and then constantly compares this value to the desired fueling for the given speed and load. When there is an error in these values, the current offset is adjusted to minimize the error. If the offset can **not** compensate to eliminate the error, it will reach its maximum/minimum threshold and Fault Code 468 is logged.

### Component Location

The rail actuator is located on the bottom of the control valve body, toward the engine front, behind the ECM.

### Shoptalk

The estimated rail fueling and the desired rail fueling parameters can be monitored on INSITE™. This fault is a check on the ECM's control of the rail actuator and rail current offset. If the desired rail fueling can **not** be met by commanding more current to the actuator or if the desired rail fueling is being exceeded and can **not** be reduced by reducing the current to the actuator, then Fault Code 468 is logged.

Refer to Troubleshooting Fault Code t05-468
