---
aliases:
  - "Цепь привода рампы опережения — замыкание на плюс"
type: "Процедура"
doc: "01-fc113"
title_en: "Timing Rail Actuator Circuit - Shorted High"
title_ru: "Цепь привода рампы опережения — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc113.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc113.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Timing Rail Actuator Circuit - Shorted High
**Цепь привода рампы опережения — замыкание на плюс**

> [!abstract] Процедура · `01-fc113`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc113.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc113.pdf)

### Fault Code: 113

### Timing Rail Actuator Circuit - Shorted High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 113 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine timing actuator circuit - shorted high. Timing actuator circuit is open, or the timing rail actuator signal pin is shorted to ground, or the timing rail actuator return pin is shorted to battery. | No action by the ECM is taken. Actuator is open, closed, or partially closed. Engine power output will vary and white smoke can occur. Fault Code 112 can also be logged. |

![[19803582.png]]

Timing Rail Actuator Circuit

### Circuit Description

The timing rail actuator circuit supplies current to the timing rail actuator(s). The engine control module (ECM) commands a varying amount of current to the timing rail actuator to control the amount of timing pressure to the injectors.

### Component Location

The timing rail actuators are located at the left side, toward top, of the ECVA.

### Shoptalk

Confirm that the actuator connector is firmly in place. When there is power to the actuator(s), the actuator opens. This can cause Fault Code 112, timing flow mismatch.

Refer to Troubleshooting Fault Code t05-113
