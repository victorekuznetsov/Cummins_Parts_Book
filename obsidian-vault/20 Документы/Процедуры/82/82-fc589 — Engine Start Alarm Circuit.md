---
aliases:
  - "Цепь сигнализации пуска двигателя"
type: "Процедура"
doc: "82-fc589"
title_en: "Engine Start Alarm Circuit"
title_ru: "Цепь сигнализации пуска двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc589.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc589.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Engine Start Alarm Circuit
**Цепь сигнализации пуска двигателя**

> [!abstract] Процедура · `82-fc589`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc589.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc589.pdf)

### Fault Code: 589

### Engine Start Alarm Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 589 PID(P): S121 SPN: 611 FMI: 4/4 Lamp: Yellow SRT: | Less than + 6 VDC detected at the engine start alarm circuit when high voltage was expected by the ECM. | The ICON™ idle control system will be disabled. **Only** mandatory shutdown will be enabled. Engine can be started normally. |

![[19803220.png]]

Engine Start Alarm Circuit

### Circuit Description

The engine start alarm circuit turns on the audible engine start alarm to warn of an impending automatic engine start.

### Component Location

The engine start alarm is located on the vehicle's fire wall on the intake side of the engine.

### Shoptalk

This fault typically indicates an open circuit between the alarm coil (pins A and B), or from pin B of the alarm to battery voltage, or from pin A of the alarm to pin 32 of the ECM. Another typical cause for this fault code is a short circuit from pin A or B of the alarm, or from ECM pin 32 to ground. The alarm **must** sound for 14 seconds before an engine start. The alarm is actuated by supplying a signal from pin 25 of the ECM connector to pin B of the alarm connector.

Refer to Troubleshooting Fault Code t05-589
