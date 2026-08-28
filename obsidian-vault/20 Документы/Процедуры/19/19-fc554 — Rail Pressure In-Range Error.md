---
type: "Процедура"
doc: "19-fc554"
title_en: "Rail Pressure In-Range Error"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc554.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc554.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Rail Pressure In-Range Error

> [!abstract] Процедура · `19-fc554`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc554.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc554.pdf)

### Fault Code: 554

### Rail Pressure In-Range Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 554 PID(P): P157 SPN: 157 FMI: 2 Lamp: Yellow SRT: | More than 0.67 VDC detected at the rail pressure signal pin 31 of the engine harness at engine key-on. | Calibration-dependent engine derate. |

![[19400880.png]]

Rail Pressure Sensor Circuit

### Circuit Description

The rail pressure sensor provides a signal to the ECM through the engine harness. The ECM uses the rail pressure sensor signal to monitor the pressure going to the injectors from the control valve body. At start-up, the ECM expects to see the voltage on signal pin 31 between 0.40 and 4.60 VDC. If the voltage is other than the specified range on start-up, the ECM will log this fault.

### Component Location

The rail pressure sensor is located in the control valve body.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged rail pressure sensor

- Malfunctioning or damaged engine wiring harness

- Fuel drain line restriction

Refer to Troubleshooting Fault Code t05-554
