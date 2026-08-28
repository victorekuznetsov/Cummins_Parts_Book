---
aliases:
  - "Привод рампы опережения — неверные данные"
type: "Процедура"
doc: "01-fc467"
title_en: "Timing Rail Actuator - Data Incorrect"
title_ru: "Привод рампы опережения — неверные данные"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc467.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc467.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Timing Rail Actuator - Data Incorrect
**Привод рампы опережения — неверные данные**

> [!abstract] Процедура · `01-fc467`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc467.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc467.pdf)

### Fault Code: 467

### Timing Rail Actuator - Data Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 467 PID(P): SPN: FMI: Lamp: Warning SRT: | Timing rail actuator circuit - data incorrect. The error between desired timing fueling and commanded timing fueling exceeds a normal limit. | No action taken by the ECM. Possible loss of performance. |

![[19400781.png]]

Fuel System Flow Schematic

### Circuit Description

The ECM uses the timing pressure signal and engine speed to estimate the actual timing the engine is receiving, and then constantly compares this value to the desired timing for the given speed and load. When there is too large of an error in these values for too long, Fault Code 467 is logged.

### Component Location

The timing rail actuators are located on the left-side (top) of the ECVA.

### Shoptalk

The estimated timing fueling and the desired timing fueling parameters can be monitored on the electronic service tool. This fault is a check on the ECM's control of the timing actuator and subsequent fuel flow. If the desired timing fueling can **not** be met by commanding more current to the actuator, or if the desired timing fueling is being exceeded and can **not** be reduced by limiting the amount of current to the actuator, then Fault Code 467 is logged.

Refer to Troubleshooting Fault Code t05-467
