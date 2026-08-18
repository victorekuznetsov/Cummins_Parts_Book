---
aliases:
  - "Ошибка электромагнита B"
type: "Процедура"
doc: "87-fc529"
title_en: "Solenoid B Error"
title_ru: "Ошибка электромагнита B"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc529.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc529.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Solenoid B Error
**Ошибка электромагнита B**

> [!abstract] Процедура · `87-fc529`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc529.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc529.pdf)

### Fault Code: 529

### Solenoid B Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 529 PID(P): S051 SPN: P02 FMI: 703 Lamp: Yellow SRT: | Less than 17 VDC detected at solenoid B supply pin 21 of the engine harness. | No action is taken by the electronic control module (ECM). |

![[19a00673.png]]

Solenoid B Circuit

### Circuit Description

The solenoid driver will control engine and vehicle functions by closing or opening a switched solenoid output, based on 11 selected engine parameters. The solenoid output will control functions such as a fan clutch, an intake grid heater, an air cleaner restriction indicator, or an oil filter differential pressure indicator.

### Component Location

The solenoid driver is an OEM device, and the location of the solenoid is dependent upon the OEM.

Refer to Troubleshooting Fault Code t05-529
