---
aliases:
  - "Расхождение измеренной частоты вращения и частоты тока генератора — условие возникло"
type: "Процедура"
doc: "01-fc1469"
title_en: "Generator Set Measured Speed and AC Output Frequency Conflict - Condition Exists"
title_ru: "Расхождение измеренной частоты вращения и частоты тока генератора — условие возникло"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1469.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1469.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Generator Set Measured Speed and AC Output Frequency Conflict - Condition Exists
**Расхождение измеренной частоты вращения и частоты тока генератора — условие возникло**

> [!abstract] Процедура · `01-fc1469`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1469.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1469.pdf)

### Fault Code: 1469

### Generator Set Measured Speed and AC Output Frequency Conflict - Condition Exists

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1469 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Generator measured speed and measured AC output frequency do **not** agree. | Generator set will shut down. |

![[19802913.png]]

Generator Circuit

### Circuit Description

The generator set monitors engine speed and AC output frequency. The AC output frequency is dependent on the engine speed. Therefore, if the engine speed does **not** match what the AC output frequency would expect, the engine control module (ECM) will make this fault code active.

### Component Location

Reference Section E for location of the engine speed sensor and the PT/CT board.

Reference customer/facility/installation documentation for the location of the generator set circuit breaker and interface with the electric bus.

### Shoptalk

This fault code could be caused by a faulty PT/CT board, a problem with the engine speed sensor circuit, and a problem with the generator control harness.

Refer to Troubleshooting Fault Code t05-1469.
