---
aliases:
  - "Ошибка вспомогательного входа частоты вращения"
type: "Процедура"
doc: "19-fc489"
title_en: "Auxiliary Speed Input Error"
title_ru: "Ошибка вспомогательного входа частоты вращения"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc489.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc489.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Auxiliary Speed Input Error
**Ошибка вспомогательного входа частоты вращения**

> [!abstract] Процедура · `19-fc489`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc489.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc489.pdf)

### Fault Code: 489

### Auxiliary Speed Input Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 489 PID(P): P191 SPN: 191 FMI: 1 Lamp: Yellow SRT: | Auxiliary speed frequency on input pin 17 indicates the frequency is below a calibration-dependent threshold. | Engine will go to idle. |

![[19400686.png]]

Auxiliary Speed Input Circuit

### Circuit Description

The auxiliary speed input is a frequency signal from an auxiliary speed or pressure pickup. It is sent to the ECM and is used to control the engine speed. Auxiliary reference speed is based on the accelerator position.

### Component Location

The auxiliary speed or pressure pickup device location is dependent on the OEM application. Refer to OEM manual for component location.

### Shoptalk

The auxiliary speed governor controls engine speed based on a measured auxiliary speed or pressure.

Refer to Troubleshooting Fault Code t05-489
