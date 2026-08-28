---
aliases:
  - "Цепь подтверждения холостого хода"
type: "Процедура"
doc: "19-fc431"
title_en: "Idle Validation Circuit"
title_ru: "Цепь подтверждения холостого хода"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc431.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc431.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Idle Validation Circuit
**Цепь подтверждения холостого хода**

> [!abstract] Процедура · `19-fc431`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc431.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc431.pdf)

### Fault Code: 431

### Idle Validation Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 431 PID(P): P91 SPN: 091 FMI: 2 Lamp: Yellow SRT: 00-370 | Voltage detected simultaneously on both the idle validation off-idle and idle signal pins 12 and 13 of the OEM harness, or no voltage detected on either pin. | None on performance. |

![[19400175.png]]

Idle Validation Circuit

### Circuit Description

The idle validation signal is a safety feature that disables accelerator control while an improper validation signal is detected by the ECM. The idle validation switch provides on-idle and off-idle validation signals to the ECM through the OEM harness and OEM interface harness.

### Component Location

The accelerator pedal or lever location varies with each OEM. Refer to the OEM manual.

### Shoptalk

This fault code is usually caused by the improper wiring of the harnesses and idle validation switch.

Note:If the accelerator pedal or lever or accelerator pedal or lever position sensor is changed or after a calibration download, cycle the accelerator pedal pedal or lever (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator pedal or lever with the ECM.

Refer to Troubleshooting Fault Code t05-431
