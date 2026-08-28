---
type: "Процедура"
doc: "19-fc253"
title_en: "Oil Level - Engine Protection"
modified: "2011-03-01"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc253.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc253.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Oil Level - Engine Protection

> [!abstract] Процедура · `19-fc253`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc253.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc253.pdf)

### Fault Code: 253

### Oil Level - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 253 PID(P): P98 SPN: 098 FMI: 1 Lamp: Engine Protection SRT: | Low oil level has been detected. Voltage signal on the oil level signal pin 12 of the engine harness indicates low oil level in the engine. | Calibration-dependent progressive power derate and engine shutdown with increasing time after alert. |

![[19400642.png]]

Oil Level Sensor

### Circuit Description

The oil level sensor is used by the ECM to monitor the amount of oil in the engine. Low oil level detected at pin 12 can cause the engine **not** to start.

### Component Location

The oil level sensor is located in the oil pan on the left side of the engine.

Refer to Troubleshooting Fault Code t05-253
