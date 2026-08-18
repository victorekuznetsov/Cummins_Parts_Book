---
aliases:
  - "Функция ограничения крутящего момента — особые указания"
type: "Процедура"
doc: "123-fc2998"
title_en: "Engine Torque Limit Feature - Special Instructions"
title_ru: "Функция ограничения крутящего момента — особые указания"
modified: "2010-08-20"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc2998.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc2998.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# Engine Torque Limit Feature - Special Instructions
**Функция ограничения крутящего момента — особые указания**

> [!abstract] Процедура · `123-fc2998`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc2998.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc2998.pdf)

### Fault Code: 2998

### Engine Torque Limit Feature - Special Instructions

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2998 PID(P): SPN: 1632 FMI: 14 Lamp: Amber SRT: | Engine Torque Limit Feature - Special Instructions. Engine overloaded. | Possible engine derate if enabled. |

![[19c01042.png]]

ECM CM2150

### Circuit Description

N/A

### Component Location

N/A

### Shoptalk

This fault code is designed to keep the engine from overloading.

The fault code is triggered when the engine speed fails to attain the commanded speed.

Potential causes of this fault code are:

- Low engine power

- High idle adjustment is too high

- Excessive hull fouling

- Incorrect transmission or propeller.

Refer to the OEM service manual for causes associated with excessive hull fouling and incorrect transmission or propeller, as these are external to engine.

Refer to Troubleshooting Fault Code 2998.
