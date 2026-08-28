---
aliases:
  - "Диагностика драйвера рампы опережения №2"
type: "Процедура"
doc: "01-fc1422"
title_en: "Timing Rail Number 2 Driver Diagnostic"
title_ru: "Диагностика драйвера рампы опережения №2"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1422.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1422.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Timing Rail Number 2 Driver Diagnostic
**Диагностика драйвера рампы опережения №2**

> [!abstract] Процедура · `01-fc1422`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1422.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1422.pdf)

### Fault Code: 1422

### Timing Rail Number 2 Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1422 PID(P): SPN: FMI: Lamp: Warning SRT: | Timing rail Number 2 driver diagnostic has detected an error. | No action is taken by the ECM. Possible loss of performance. |

![[19803582.png]]

Timing Rail Number 2 Actuator Circuit

### Circuit Description

The ECM checks the timing rail Number 2 actuator driver to sustain correct operation. The timing rail Number 2 actuator is actuated by the electronic control module (ECM) to control fuel metering. Each fuel actuator is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the fuel actuator from the ECM on the supply wire and returns to the ECM on the return wire. Each solenoid valve is normally closed, and it is **only** opened by an electrical pulse from the ECM during metering. The ECM monitors the voltage, no voltage will trip Fault Code 1422, and can be caused by shorts, opens, or a failed fuel pump actuator driver in the ECM.

### Component Location

The timing rail Number 2 driver is located in the ECM.

### Shoptalk

The possible failure modes are open circuit, short to ground, high actuator resistance, and loss of boost voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1422
