---
aliases:
  - "Цепь датчика частоты/положения — недопустимая скорость изменения"
type: "Процедура"
doc: "07-fc121"
title_en: "Engine Speed/Position Sensor Circuit - Abnormal Rate of Change"
title_ru: "Цепь датчика частоты/положения — недопустимая скорость изменения"
modified: "2012-12-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc121.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc121.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Engine Speed/Position Sensor Circuit - Abnormal Rate of Change
**Цепь датчика частоты/положения — недопустимая скорость изменения**

> [!abstract] Процедура · `07-fc121`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc121.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc121.pdf)

### Fault Code: 121

### Engine Speed/Position Sensor Circuit - Abnormal Rate of Change

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 121 PID(P): P190 SPN: 190 FMI: 10 Lamp: Amber SRT: | Engine speed/position sensor circuit lost one of two signals from the magnetic pickup sensor - abnormal rate of change. Both the primary and secondary speed sensors are hall effect sensors. | Loss of backup engine speed sensor. No action by the ECM is taken. |

![[19901358.png]]

Engine Speed/Position Sensor Circuit

### Circuit Description

The secondary engine speed sensor provides a backup engine speed signal to the electronic control module (ECM) through the engine harness. The sensor generates a signal by sensing the movement of the target teeth of the flywheel.

### Component Location

The secondary engine speed sensor is located in the flywheel housing.

### Shoptalk

The engine speed sensor provides the main engine speed signal to the ECM through the engine harness. The engine speed signal is generated when the engine speed sensor detects teeth on the ring gear. The ECM determines the engine speed by counting the number of voltage switches for a given period of time.

Refer to Troubleshooting Fault Code t05-121
