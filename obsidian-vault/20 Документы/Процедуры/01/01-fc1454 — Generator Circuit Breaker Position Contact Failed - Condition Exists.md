---
aliases:
  - "Отказ контакта положения выключателя генератора — условие возникло"
type: "Процедура"
doc: "01-fc1454"
title_en: "Generator Circuit Breaker Position Contact Failed - Condition Exists"
title_ru: "Отказ контакта положения выключателя генератора — условие возникло"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1454.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1454.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Generator Circuit Breaker Position Contact Failed - Condition Exists
**Отказ контакта положения выключателя генератора — условие возникло**

> [!abstract] Процедура · `01-fc1454`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1454.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1454.pdf)

### Fault Code: 1454

### Generator Circuit Breaker Position Contact Failed - Condition Exists

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1454 PID(P): SPN: FMI: Lamp: Warning SRT: | Generator circuit breaker position contact failed. | No action is taken by the ECM. |

![[19802904.png]]

Generator Circuit

### Circuit Description

The generator set circuit breaker is the switch for the generator set's connection to the bus. The circuit breaker opens when events have occurred, which forces the generator set to no longer be connected to the bus. The circuit breaker closes when the generator set is to be connected to the bus.

This fault code is used by the engine control module (ECM) to tell the operator that, due to an event, the ECM can **not** determine the position of the circuit breaker.

### Component Location

Refer to Section E for location of the ECM card cage.

Refer to customer/facility/installation documentation for the location of the generator set circuit breaker.

### Shoptalk

The possible failure modes are that the generator set circuit breaker was **not** wired properly, an open circuit, shorted circuit, or short pin-to-pin condition exists.

Refer to Troubleshooting Fault Code t05-1454.
