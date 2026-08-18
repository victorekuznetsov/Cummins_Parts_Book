---
aliases:
  - "Исполнительный механизм подачи №1 — обрыв (передний)"
type: "Процедура"
doc: "01-fc378"
title_en: "Fueling Actuator Number 1 - Open Circuit (Front)"
title_ru: "Исполнительный механизм подачи №1 — обрыв (передний)"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc378.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc378.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fueling Actuator Number 1 - Open Circuit (Front)
**Исполнительный механизм подачи №1 — обрыв (передний)**

> [!abstract] Процедура · `01-fc378`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc378.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc378.pdf)

### Fault Code: 378

### Fueling Actuator Number 1 - Open Circuit (Front)

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 378 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Fueling actuator Number 1 circuit - open circuit. (front) | Engine will shut down. |

![[19c01394.png]]

Fueling Actuator Number 1 Circuit

### Circuit Description

The fuel actuators are actuated by the ECM to control fuel metering. Each fuel actuator is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the fuel actuator from the ECM on the supply wire and returns to the ECM on the return wire. Each solenoid valve is normally closed, and it is **only** opened by an electrical pulse from the ECM during metering.

### Component Location

The front fueling actuator is mounted on the fuel delivery housing. It is the actuator closest to the front of the QSX15 engine.

### Shoptalk

The possible failure modes are open circuit, short to ground, high actuator resistance, supply wire shorted to battery, and loss of boost voltage inside of ECM.

Refer to Troubleshooting Fault Code t05-378
