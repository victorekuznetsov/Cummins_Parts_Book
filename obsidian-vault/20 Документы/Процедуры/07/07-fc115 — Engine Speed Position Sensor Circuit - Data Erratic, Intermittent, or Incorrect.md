---
aliases:
  - "Цепь датчика частоты/положения — данные нестабильны или неверны"
type: "Процедура"
doc: "07-fc115"
title_en: "Engine Speed/Position Sensor Circuit - Data Erratic, Intermittent, or Incorrect"
title_ru: "Цепь датчика частоты/положения — данные нестабильны или неверны"
modified: "2012-12-18"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc115.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc115.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Engine Speed/Position Sensor Circuit - Data Erratic, Intermittent, or Incorrect
**Цепь датчика частоты/положения — данные нестабильны или неверны**

> [!abstract] Процедура · `07-fc115`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc115.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc115.pdf)

### Fault Code: 115

### Engine Speed/Position Sensor Circuit - Data Erratic, Intermittent, or Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 115 PID(P): P190 SPN: 190 FMI: 2 Lamp: Red SRT: | Engine speed/position sensor circuit lost both of two signals from the magnetic pickup sensor. Data is erratic, intermittent, or incorrect. Both the primary and secondary speed sensors are hall effect sensors. | Engine will die and will **not** restart. |

![[19901358.png]]

Engine Speed/Position Sensor Circuit

### Circuit Description

The primary engine speed sensor provides the engine speed signal to the electronic control module (ECM) through the engine harness. The sensor generates a signal by sensing the movement of the target teeth of the flywheel.

### Component Location

The primary engine speed sensor is located in the flywheel housing.

### Shoptalk

The engine speed sensor provides the main engine speed signal to the ECM through the engine harness. The engine speed signal is generated when the engine speed sensor detects teeth on the ring gear. The ECM determines the engine speed by counting the number of voltage switches for a given period of time.

Refer to Troubleshooting Fault Code t05-115
