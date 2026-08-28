---
aliases:
  - "Привод топливной рампы — неверные данные"
type: "Процедура"
doc: "01-fc468"
title_en: "Fuel Rail Actuator - Data Incorrect"
title_ru: "Привод топливной рампы — неверные данные"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc468.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc468.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Rail Actuator - Data Incorrect
**Привод топливной рампы — неверные данные**

> [!abstract] Процедура · `01-fc468`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc468.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc468.pdf)

### Fault Code: 468

### Fuel Rail Actuator - Data Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 468 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel rail actuator circuit - data incorrect. The error between desired rail fueling and commanded rail fueling exceeds a normal limit. | No action is taken by the ECM. Possible loss of performance. |

![[19400781.png]]

Fuel System Flow Schematic

### Circuit Description

The ECM uses the rail pressure signal and the engine speed to estimate the actual fueling that the engine is receiving, and then constantly compares this value to the desired fueling for the given speed and load. When there is too large of an error in these values for too long, this fault is logged.

### Component Location

The fuel rail actuator is located on the left-side (bottom) of the ECVA.

### Shoptalk

The estimated fuel railing and the desired fuel railing parameters can be monitored using the electronic service tool. This fault is a check on the ECM's control of the rail actuator and subsequent fuel flow. If the desired fuel railing can **not** be met by commanding more current to the actuator, or if the desired fuel railing is being exceeded and can **not** be reduced by limiting the amount of current to the actuator, then this fault is logged.

Refer to Troubleshooting Fault Code t05-468
