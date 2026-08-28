---
aliases:
  - "Цепь входа реле стартера ICON™"
type: "Процедура"
doc: "82-fc588"
title_en: "ICON™ Starter Relay Input Circuit"
title_ru: "Цепь входа реле стартера ICON™"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc588.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc588.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# ICON™ Starter Relay Input Circuit
**Цепь входа реле стартера ICON™**

> [!abstract] Процедура · `82-fc588`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc588.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc588.pdf)

### Fault Code: 588

### ICON™ Starter Relay Input Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 588 PID(P): S121 SPN: 611 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at the alarm circuit when low voltage was expected by the ECM. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine can be started normally. |

![[19803220.png]]

Engine Start Alarm Circuit

### Circuit Description

The alarm circuit turns on the audible alarm to warn of an impending engine start.

### Component Location

The ICON™ alarm is mounted on the vehicle's fire wall on the intake side of the engine.

### Shoptalk

This fault typically indicates short circuit to battery or an open circuit. The fan 2 clutch feature is **not** used.

Refer to Troubleshooting Fault Code t05-588
