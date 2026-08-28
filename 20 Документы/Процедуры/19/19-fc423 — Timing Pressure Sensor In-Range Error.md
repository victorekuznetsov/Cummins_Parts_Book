---
type: "Процедура"
doc: "19-fc423"
title_en: "Timing Pressure Sensor In-Range Error"
modified: "2026-05-28"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc423.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc423.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Timing Pressure Sensor In-Range Error

> [!abstract] Процедура · `19-fc423`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc423.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc423.pdf)

### Fault Code: 423

### Timing Pressure Sensor In-Range Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 423 PID(P): P156 SPN: 156 FMI: 2 Lamp: Yellow SRT: 00-369 | More than 1.83 VDC detected at the timing pressure signal pin 33 of the engine harness at engine key on. | Calibration-dependent power and speed derate. |

![[19400803.png]]

Timing Pressure Sensor Circuit

### Circuit Description

The timing pressure sensor provides a signal to the ECM through the engine harness. The ECM uses the timing pressure sensor signal to monitor the amount of fuel going to the injector's timing chamber from the control valve body.

### Component Location

The timing pressure sensor is located on the upper right side of the control valve body.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged timing pressure sensor

- Malfunctioning or damaged engine wiring harness

- Fuel drain line restriction

Refer to Troubleshooting Fault Code t05-423
