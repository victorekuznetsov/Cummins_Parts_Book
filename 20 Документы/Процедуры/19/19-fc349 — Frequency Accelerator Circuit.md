---
aliases:
  - "Цепь частотного задания акселератора"
type: "Процедура"
doc: "19-fc349"
title_en: "Frequency Accelerator Circuit"
title_ru: "Цепь частотного задания акселератора"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc349.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc349.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Frequency Accelerator Circuit
**Цепь частотного задания акселератора**

> [!abstract] Процедура · `19-fc349`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc349.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc349.pdf)

### Fault Code: 349

### Frequency Accelerator Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 349 PID(P): P91 SPN: 191 FMI: 0 Lamp: Yellow SRT: | A frequency of greater than a calibrated threshold has been detected at frequency accelerator signal pin 17 of the OEM interface harness. | Calibration-dependent power and speed derate. |

![[19400892.png]]

Frequency Accelerator Circuit

### Circuit Description

The frequency accelerator provides the driver's accelerator command to the ECM through the OEM harness and the OEM interface harness. The ECM uses this signal to determine the fueling command.

### Component Location

Accelerator location varies with each OEM. Refer to the OEM manual.

### Shoptalk

The frequency accelerator can be used either in conjunction with a voltage accelerator or by itself.

Refer to Troubleshooting Fault Code t05-349
