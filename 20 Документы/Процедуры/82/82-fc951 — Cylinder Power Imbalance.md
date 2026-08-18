---
aliases:
  - "Разбаланс мощности по цилиндрам"
type: "Процедура"
doc: "82-fc951"
title_en: "Cylinder Power Imbalance"
title_ru: "Разбаланс мощности по цилиндрам"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc951.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc951.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Cylinder Power Imbalance
**Разбаланс мощности по цилиндрам**

> [!abstract] Процедура · `82-fc951`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc951.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc951.pdf)

### Fault Code: 951

### Cylinder Power Imbalance

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 951 PID(P): P166 SPN: 166 FMI: 2/2 Lamp: None SRT: | Cylinder Power Imbalance Between Cylinders. A power imbalance between cylinders was detected by the electronic control module (ECM). | Engine can have rough idle or misfire. |

![[19202458.png]]

Cylinder Power Imbalance

### Circuit Description

The ECM calculates the power output of each cylinder at engine idle speeds.

### Component Location

The ECM is located on the fuel system side of the engine. It is attached at the cylinder head between cylinders 2 and 3.

### Shoptalk

At engine idle speeds, the ECM measures the instantaneous acceleration of each cylinder as it fires, to determine the cylinder's power. The ECM adjusts fueling to individual cylinders if the imbalance is within pre-defined limits. If the imbalance is greater than the pre-defined limits, Fault Code 951 will be set active.

Refer to Troubleshooting Fault Code t05-951
