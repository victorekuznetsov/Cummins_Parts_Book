---
aliases:
  - "Ошибка коммутируемого выхода B"
type: "Процедура"
doc: "82-fc529"
title_en: "Switched Output B Error"
title_ru: "Ошибка коммутируемого выхода B"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc529.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc529.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Switched Output B Error
**Ошибка коммутируемого выхода B**

> [!abstract] Процедура · `82-fc529`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc529.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc529.pdf)

### Fault Code: 529 (INDUSTRIAL)

### Switched Output B Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 529 PID(P): S51 SPN: 703 FMI: 3/3 Lamp: Yellow SRT: | Less than + 17 VDC detected at the switched output B signal pin at the electronic control module (ECM). | No action taken by the ECM. |

![[19c00574.png]]

Switched Output B Circuit

### Circuit Description

The solenoid driver will control engine and vehicle functions by closing or opening a switched solenoid output, based on 11 selected engine parameters. The solenoid output will control functions such as a fan clutch, intake grid heater, air cleaner restriction indicator, or an oil filter differential pressure indicator.

### Component Location

The solenoid driver is an OEM device, and the location of the solenoid is dependent upon the OEM.

Refer to Troubleshooting Fault Code t05-529
