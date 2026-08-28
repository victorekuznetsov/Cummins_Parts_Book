---
aliases:
  - "Диагностика драйвера топливной рампы"
type: "Процедура"
doc: "01-fc1419"
title_en: "Fuel Rail Driver Diagnostic"
title_ru: "Диагностика драйвера топливной рампы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1419.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1419.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Rail Driver Diagnostic
**Диагностика драйвера топливной рампы**

> [!abstract] Процедура · `01-fc1419`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1419.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1419.pdf)

### Fault Code: 1419

### Fuel Rail Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1419 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel rail driver diagnostic has detected an error. | No action is taken by the ECM. Possible loss of performance. |

![[19803582.png]]

Fuel Rail Actuator Circuit

### Circuit Description

The ECM checks the fuel rail actuator drivers to sustain correct operation. The fuel rail actuators are actuated by the electronic control module (ECM) to control fuel metering. Each fuel actuator is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the fuel actuator from the ECM on the supply wire and returns to the ECM on the return wire. Each solenoid valve is normally closed, and it is **only** opened by an electrical pulse from the ECM during metering. The ECM monitors the voltage, no voltage will trip Fault Code 1419, and can be caused by shorts, opens, or a failed fuel rail actuator driver in the ECM.

### Component Location

The fuel rail drivers are contained in the ECM.

### Shoptalk

The possible failure modes are open circuit, short to ground, high actuator resistance, and loss of boost voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1419
