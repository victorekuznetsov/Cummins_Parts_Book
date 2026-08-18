---
aliases:
  - "Диагностика драйверов топливной системы HPI-PT"
type: "Процедура"
doc: "01-fc1436"
title_en: "HPI-PT Fuel System Driver Diagnostic"
title_ru: "Диагностика драйверов топливной системы HPI-PT"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1436.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1436.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# HPI-PT Fuel System Driver Diagnostic
**Диагностика драйверов топливной системы HPI-PT**

> [!abstract] Процедура · `01-fc1436`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1436.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1436.pdf)

### Fault Code: 1436

### HPI-PT Fuel System Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1436 PID(P): SPN: FMI: Lamp: Warning SRT: | HPI-PT fuel system driver common diagnostic has detected an error. | No action is taken by the ECM. Possible loss of performance. |

![[19803591.png]]

HPI-PT Fuel System Driver Diagnostic Circuit

### Circuit Description

The electronic control module (ECM) checks the HPI-PT fuel system actuator drivers to sustain correct operation. The fuel system actuators are actuated by the ECM to control fuel metering. Each fuel actuator is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the fuel actuator from the ECM on the supply wire and returns to the ECM on the return wire. Each solenoid valve is normally closed, and it is **only** opened by an electrical pulse from the ECM during metering.

The ECM monitors the voltage, no voltage will trip Fault Code 1436, and can be caused by shorts, opens, or a failed fuel pump actuator driver in the ECM.

### Component Location

Refer to the OEM manual for location of the ECM. Refer to Procedure 100-002 for the component location.

### Shoptalk

The possible failure modes are open circuit, short to ground, high actuator resistance, and loss of boost voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1436
