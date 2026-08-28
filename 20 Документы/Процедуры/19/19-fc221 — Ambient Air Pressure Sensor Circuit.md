---
aliases:
  - "Цепь датчика атмосферного давления"
type: "Процедура"
doc: "19-fc221"
title_en: "Ambient Air Pressure Sensor Circuit"
title_ru: "Цепь датчика атмосферного давления"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc221.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc221.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Ambient Air Pressure Sensor Circuit
**Цепь датчика атмосферного давления**

> [!abstract] Процедура · `19-fc221`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc221.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc221.pdf)

### Fault Code: 221

### Ambient Air Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 221 PID(P): P108 SPN: 108 FMI: 3 Lamp: Yellow SRT: 00-361 | More than 4.78-VDC detected at the ambient air pressure sensor signal pin 34 of the engine harness. | Derate in power output of the engine. |

![[19400069.png]]

Ambient Air Pressure Sensor Circuit

### Circuit Description

The ambient air pressure sensor provides the ambient air pressure signal to the ECM through the engine harness. The ECM uses the ambient air pressure sensor to adjust fueling based on the altitude.

### Component Location

The ambient air pressure sensor is located below the ECM on the control valve body.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged ambient air pressure sensor

- Malfunctioning or damaged engine wiring harness

Refer to Troubleshooting Fault Code t05-221
