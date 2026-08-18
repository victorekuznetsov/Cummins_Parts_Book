---
aliases:
  - "Предупреждение о внутреннем аппаратном отказе ЭБУ"
type: "Процедура"
doc: "82-fc343"
title_en: "Electronic Control Module Warning Internal Hardware Failure - Bad Intelligent Device or Component"
title_ru: "Предупреждение о внутреннем аппаратном отказе ЭБУ"
modified: "2014-01-23"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc343.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc343.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Electronic Control Module Warning Internal Hardware Failure - Bad Intelligent Device or Component
**Предупреждение о внутреннем аппаратном отказе ЭБУ**

> [!abstract] Процедура · `82-fc343`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2014-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc343.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc343.pdf)

### Fault Code: 343

### Electronic Control Module Warning Internal Hardware Failure - Bad Intelligent Device or Component

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 343 PID(P): S254 SPN: 629 FMI: 12/12 Lamp: Yellow SRT: | Internal ECM error. | Possibly none on performance, or severe derate. |

![[19c00010.png]]

Electronic Control Module

### Circuit Description

The ECM monitors both signal voltage output to the injectors and ECM input from the engine position sensor.

### Component Location

The ECM is located on the fuel pump side of the engine.

### Shoptalk

- Loose engine or chassis ground connections can cause Fault Code 343 to be logged. Pay special attention to the negative starter post connection.

- Moisture in the ECM connectors can also cause the ECM to log Fault Code 343.

- Symptoms can include intermittent stumble or rough running.

Note: It is **always** a good idea to check the resistance of the meter leads by reading the resistance displayed by the tool when touching the positive and negative leads together. Subtract this reading from any readings taken for resistance. This will provide a more accurate resistance measurement. Note: **Always** reapply dielectric grease when reconnecting an electrical connection.

Refer to Troubleshooting Fault Code t05-343
