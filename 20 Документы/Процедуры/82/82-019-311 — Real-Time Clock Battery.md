---
aliases:
  - "Батарея часов реального времени"
type: "Процедура"
doc: "82-019-311"
title_en: "Real-Time Clock Battery"
title_ru: "Батарея часов реального времени"
modified: "2002-06-03"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 3
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-311.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-311.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Real-Time Clock Battery
**Батарея часов реального времени**

> [!abstract] Процедура · `82-019-311`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-311.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-311.pdf)

### General Information

The real-time clock battery backup module is connected to the engine harness main branch near the 50-pin ECM sensor port connector.

The ECM uses the real-time clock feature to time-stamp faults and other data with the time and date. The battery backup module is used to power the real-time clock circuitry in the ECM when vehicle battery power is removed from the ECM. If a battery backup module is installed, the ECM clock will maintain the correct time and date with power removed from the ECM, provided the actuator harness connector remains plugged into the ECM.

If a real-time clock battery backup module is **not** installed on the engine, it will be necessary to set the time and date using INSITE™ whenever the real-time clock feature is enabled in the ECM and vehicle battery power is removed from the ECM.

![[19c00747.png]]

### Remove

Locate the real-time clock battery backup module on the main engine harness. Cut the wire tie securing the module case to the harness.

Clean the area around the battery backup module harness connector.

Disconnect the battery backup module from the engine harness.

![[19c00748.png]]

### Install

Use quick-dry electrical contact cleaner, Part No. 3824510, to clean all dirt and moisture from the the battery backup module and harness connector.

Do **not** apply grease or oil to either the harness connector or battery backup module.

Connect the battery backup module to the engine harness.

Secure the battery backup module to the main engine harness using wire ties.

![[19c00748.png]]
