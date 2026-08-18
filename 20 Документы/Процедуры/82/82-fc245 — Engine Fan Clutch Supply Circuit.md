---
aliases:
  - "Цепь питания муфты вентилятора"
type: "Процедура"
doc: "82-fc245"
title_en: "Engine Fan Clutch Supply Circuit"
title_ru: "Цепь питания муфты вентилятора"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc245.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc245.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Engine Fan Clutch Supply Circuit
**Цепь питания муфты вентилятора**

> [!abstract] Процедура · `82-fc245`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc245.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc245.pdf)

### Fault Code: 245

### Engine Fan Clutch Supply Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 245 PID(P): S033 SPN: 647 FMI: 4/4 Lamp: Yellow SRT: | Less than 6 VDC detected at fan clutch when on. Indicates an excessive current draw from the electronic control module (ECM) or a faulty ECM output circuit. | The fan can stay on all the time. |

![[19c00263.png]]

Engine Fan Clutch Supply Circuit

### Circuit Description

The fan clutch solenoid is a device used by the ECM to control the engine fan by sending a signal to open or close the fan clutch solenoid.

### Component Location

Refer to an OEM diagram for the location of the fan clutch solenoid.

### Shoptalk

Possible cause for this fault code:

- ECM fan clutch supply has a short circuit to ground.

Refer to Troubleshooting Fault Code t05-245
