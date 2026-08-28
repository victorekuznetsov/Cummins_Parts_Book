---
aliases:
  - "Ошибка коммутируемого выхода B"
type: "Процедура"
doc: "82-fc528"
title_en: "Switched Output B Error"
title_ru: "Ошибка коммутируемого выхода B"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc528.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc528.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Switched Output B Error
**Ошибка коммутируемого выхода B**

> [!abstract] Процедура · `82-fc528`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc528.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc528.pdf)

### Fault Code: 528 (INDUSTRIAL)

### Switched Output B Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 528 PID(P): P093 SPN: 93 FMI: 2/2 Lamp: Yellow SRT: | Less than + 17.0 VDC detected at the switch output B signal pin of the 31-pin OEM connector. | No action taken by the electronic control module (ECM). |

![[19c00574.png]]

Switched Output B Circuit

### Circuit Description

The solenoid driver will control engine and vehicle functions by closing or opening a switched solenoid output, based on 11 selected engine parameters. The solenoid output will control functions such as a fan clutch, intake grid heater, air cleaner restriction indicator, or an oil filter differential pressure indicator.

### Component Location

The solenoid driver is an OEM device, and the location of the solenoid is dependent upon the OEM.

Refer to Troubleshooting Fault Code t05-528
