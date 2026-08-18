---
aliases:
  - "Ошибка вспомогательного входа частоты вращения"
type: "Процедура"
doc: "82-fc489"
title_en: "Auxiliary Speed Input Error"
title_ru: "Ошибка вспомогательного входа частоты вращения"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc489.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc489.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Auxiliary Speed Input Error
**Ошибка вспомогательного входа частоты вращения**

> [!abstract] Процедура · `82-fc489`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc489.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc489.pdf)

### Fault Code: 489 (INDUSTRIAL)

### Auxiliary Speed Input Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 489 PID(P): P191 SPN: 191 FMI: 1/18 Lamp: Yellow SRT: | Auxiliary speed frequency on input pin indicates the frequency is below a calibration-dependent threshold. | Engine will **only** idle. |

![[19c00656.png]]

Auxiliary Speed Input Circuit

### Circuit Description

The auxiliary speed input is a frequency signal from an auxiliary speed or pressure pickup. It is sent to the electronic control module (ECM) and is used to control the engine speed. Auxiliary reference speed is based on the throttle position.

### Component Location

The auxiliary speed or pressure pickup device location is dependent on the OEM application. Refer to the OEM troubleshooting and repair manual for component location.

### Shoptalk

The auxiliary speed governor controls engine speed based on a measured auxiliary speed or pressure.

Refer to Troubleshooting Fault Code t05-489
