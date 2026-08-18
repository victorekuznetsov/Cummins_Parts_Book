---
aliases:
  - "Выключатель генератора не включился — условие возникло"
type: "Процедура"
doc: "01-fc1452"
title_en: "Generator Circuit Breaker - Failed to Close - Condition Exists"
title_ru: "Выключатель генератора не включился — условие возникло"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1452.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1452.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Generator Circuit Breaker - Failed to Close - Condition Exists
**Выключатель генератора не включился — условие возникло**

> [!abstract] Процедура · `01-fc1452`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1452.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1452.pdf)

### Fault Code: 1452

### Generator Circuit Breaker - Failed to Close - Condition Exists

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1452 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Generator circuit breaker failed to close. | Generator set will shut down. |

![[19802904.png]]

Generator Set Circuit Breaker Circuit

### Circuit Description

The generator set circuit breaker is the switch for the generator set's connection to the bus. The circuit breaker opens when events have occurred, which forces the generator set to no longer be connected to the bus. The circuit breaker closes when the generator set is to be connected to the bus.

This fault code is used by the engine control module (ECM) to tell the operator that due to an event, the generator set can **not** connect to the bus.

### Component Location

Refer to Section E for location of the ECM card cage.

Refer to customer/facility/installation documentation for the location of the generator set circuit breaker.

### Shoptalk

Verify that the charging mechanism of the paralleling breaker is functioning properly.

Check the closed signal to the breaker.

Verify that the auxiliary contact signals from the breaker to ECM are operational.

Refer to Troubleshooting Fault Code t05-1452.
