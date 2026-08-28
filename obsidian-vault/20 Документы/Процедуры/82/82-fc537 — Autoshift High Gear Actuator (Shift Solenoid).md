---
aliases:
  - "Привод повышающей передачи автопереключения (электромагнит)"
type: "Процедура"
doc: "82-fc537"
title_en: "Autoshift High Gear Actuator (Shift Solenoid)"
title_ru: "Привод повышающей передачи автопереключения (электромагнит)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc537.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc537.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Autoshift High Gear Actuator (Shift Solenoid)
**Привод повышающей передачи автопереключения (электромагнит)**

> [!abstract] Процедура · `82-fc537`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc537.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc537.pdf)

### Fault Code: 537

### Autoshift High Gear Actuator (Shift Solenoid)

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 537 PID(P): S043 SPN: 717 FMI: 11/11 Lamp: Yellow SRT: | Either low voltage detected on autoshift high gear actuator circuit when (+) 12 VDC are commanded or voltage detected when no voltage is commanded. | Top 2 shift solenoid will **not** function properly. Transmission will **not** shift properly. |

![[19c00352.png]]

Top 2 Shift Solenoid Circuit

### Circuit Description

The autoshift high gear actuator is an ECM-driven solenoid that controls a Top 2 transmission.

### Component Location

The autoshift high gear actuator is located on the topside of the transmission toward the back. Refer to an OEM diagram for the specific location.

Refer to Troubleshooting Fault Code t05-537
