---
aliases:
  - "Привод опережения №1 — обрыв (передний)"
type: "Процедура"
doc: "01-fc394"
title_en: "Timing Actuator Number 1 - Open Circuit (Front)"
title_ru: "Привод опережения №1 — обрыв (передний)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc394.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc394.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Timing Actuator Number 1 - Open Circuit (Front)
**Привод опережения №1 — обрыв (передний)**

> [!abstract] Процедура · `01-fc394`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc394.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc394.pdf)

### Fault Code: 394

### Timing Actuator Number 1 - Open Circuit (Front)

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 394 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Timing actuator Number 1 circuit - open circuit. (front) | Engine will shut down. |

![[19c01394.png]]

Timing Actuator Number 1 Circuit

### Circuit Description

The timing actuators are actuated by the ECM to control fuel metering. Each timing actuator is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the timing actuator from the ECM on the supply wire and returns to the ECM on the return wire. Each solenoid valve is normally closed, and it is **only** opened by an electrical pulse from the ECM during metering.

### Component Location

The front timing actuator is mounted on the fuel delivery housing. It is the second actuator from the front of the QSX15 engine.

### Shoptalk

The possible failure modes are open circuit, short to ground, high actuator resistance, and loss of boost voltage inside of ECM.

Refer to Troubleshooting Fault Code t05-394
