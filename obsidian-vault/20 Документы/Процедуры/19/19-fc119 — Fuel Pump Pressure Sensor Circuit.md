---
type: "Процедура"
doc: "19-fc119"
title_en: "Fuel Pump Pressure Sensor Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc119.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc119.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Fuel Pump Pressure Sensor Circuit

> [!abstract] Процедура · `19-fc119`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc119.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc119.pdf)

### Fault Code: 119

### Fuel Pump Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 119 PID(P): P135 SPN: 135 FMI: 4 Lamp: Yellow SRT: 00-384 | Less than 0.30-VDC detected at fuel pump pressure sensor signal pin 32 of the engine harness. | No action by the ECM is taken. |

![[19801091.png]]

Fuel Pump Pressure Sensor Circuit

### Circuit Description

The fuel pump pressure sensor provides the fuel pump pressure sensor signal to the ECM through the engine harness. The ECM uses the fuel pump pressure signal to monitor the fuel pump pressure going to the control valve body.

### Component Location

The fuel pump pressure sensor is located on the fuel pump.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged fuel pump pressure sensor

- Malfunctioning or damaged engine wiring harness

Refer to Troubleshooting Fault Code t05-119
