---
aliases:
  - "Цепь выключателя альтернативного статизма"
type: "Процедура"
doc: "87-fc524"
title_en: "Alternate Droop Switch Circuit"
title_ru: "Цепь выключателя альтернативного статизма"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc524.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc524.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Alternate Droop Switch Circuit
**Цепь выключателя альтернативного статизма**

> [!abstract] Процедура · `87-fc524`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc524.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc524.pdf)

### Fault Code: 524

### Alternate Droop Switch Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 524 PID(P): P113 SPN: 113 FMI: 2 Lamp: Yellow SRT: | Electronic control module (ECM) has detected an invalid droop selection switch on pin 22 of the engine harness, indicating the value is out of range. | Droop selection is disabled. Droop setting defaults to switch position 1 (or normal) preprogrammed droop governor values. |

![[19a00760.png]]

Alternate Droop Switch Circuit

### Circuit Description

The alternate droop switch circuit allows the operator to select from three preprogrammed droop values using a tristate switch.

### Component Location

The location of the alternate droop switch circuit varies with each OEM and equipment model. Refer to the OEM manual.

### Shoptalk

The switch should be monitored for proper operation on INSITE™. If the switch is changing state correctly on the service tool, then the problem is **not** in the switch circuit. The switch has three states:

- Position 1 - open

- Position 2 - closed

- Position 3 - 1500-ohm resistance.

Refer to Troubleshooting Fault Code t05-524
