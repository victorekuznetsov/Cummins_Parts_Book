---
aliases:
  - "Привод опережения не отвечает на команды ЭБУ"
type: "Процедура"
doc: "01-fc112"
title_en: "Engine Timing Actuator is Not Responding to ECM Commands"
title_ru: "Привод опережения не отвечает на команды ЭБУ"
modified: "2011-10-03"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc112.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc112.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Timing Actuator is Not Responding to ECM Commands
**Привод опережения не отвечает на команды ЭБУ**

> [!abstract] Процедура · `01-fc112`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-10-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc112.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc112.pdf)

### Fault Code: 112

### Engine Timing Actuator is Not Responding to ECM Commands

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 112 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine Timing Actuator is Not Responding to ECM Commands. The error between the estimated timing fueling and the desired timing fueling is outside the allowable limits. | Calibration-dependent engine shutdown or no action is taken by ECM. |

![[19400781.png]]

Fuel System Flow Schematic

### Circuit Description

The ECM uses the timing pressure signal and engine speed to estimate the actual timing the engine is receiving and then constantly compares this value to the desired timing for the given speed and load. When the error in these values is too large for too long, Fault Code 112 is logged.

### Component Location

The timing rail actuators are located at the left side toward the top of the ECVA.

### Shoptalk

The estimated timing fueling and the desired timing fueling parameters can be monitored on the electronic service tool. This fault is a check on the ECM's control of the timing rail actuator and subsequent fuel flow. If the desired timing fueling can **not** be met by commanding more current to the actuator or if the desired timing fueling is being exceeded and can **not** be reduced by reducing the current to the actuator, Fault Code 112 is logged.

- Fault Code 112 will not be triggered if Fault Code 116 or 117 is active

- Once the run/stop switch is cycled, Fault Code 112 becomes inactive.

Follow the troubleshooting steps before replacing the actuator. This fault code is commonly caused by:

- Air in the fuel system

- External power source on harness wiring (battery charger)

- Timing rail actuator malfunction.

Refer to Troubleshooting Fault Code t05-112
