---
aliases:
  - "Выключатель генераторной установки"
type: "Процедура"
doc: "01-fc1328"
title_en: "Generator Set Circuit Breaker"
title_ru: "Выключатель генераторной установки"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1328.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1328.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Generator Set Circuit Breaker
**Выключатель генераторной установки**

> [!abstract] Процедура · `01-fc1328`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1328.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1328.pdf)

### Fault Code: 1328

### Generator Set Circuit Breaker

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1328 PID(P): SPN: FMI: Lamp: Warning SRT: | The generator set circuit breaker has tripped. | Load dump will occur. Generator set continues to run. |

![[19802904.png]]

Generator Set Circuit Breaker Circuit

### Circuit Description

The generator set circuit breaker is the switch for the generator set's connection to the bus. The circuit breaker opens when events have occurred, which forces the generator set to no longer be connected to the bus. The circuit breaker closes when the generator set is to be connected to the bus.

This fault code is used by the ECM to tell the operator that, due to an event, the generator set is to be disconnected from the bus.

### Component Location

Refer to Section E for location of the ECM card cage.

Refer to customer/facility/installation documentation for the location of the generator set circuit breaker.

### Shoptalk

The possible failure modes are short circuit, open circuit, and failed generator set circuit breaker.

The circuit breaker is an overcurrent protection device.

In paralleling, the generator set circuit breaker acts as a switch to autoconnect generator set to system bus and other generator sets.

Refer to Troubleshooting Fault Code t05-1328
