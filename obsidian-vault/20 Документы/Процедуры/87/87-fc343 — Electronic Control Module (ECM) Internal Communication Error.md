---
aliases:
  - "Внутренняя ошибка связи ЭБУ"
type: "Процедура"
doc: "87-fc343"
title_en: "Electronic Control Module (ECM) Internal Communication Error"
title_ru: "Внутренняя ошибка связи ЭБУ"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc343.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc343.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Electronic Control Module (ECM) Internal Communication Error
**Внутренняя ошибка связи ЭБУ**

> [!abstract] Процедура · `87-fc343`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc343.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc343.pdf)

### Fault Code: 343

### Electronic Control Module (ECM) Internal Communication Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 343 PID(P): S254 SPN: 629 FMI: 12 Lamp: Yellow SRT: | Microprocessor communication error internal to the ECM. | Variable; performance will or will **not** be affected. |

![[19900397.png]]

Electronic Control Module (ECM)

### Circuit Description

The ECM is a computer that is responsible for engine control, diagnostics, and user features.

### Component Location

An ECM is located on both sides of the engine in front of the fuel pump.

### Shoptalk

This is a fault with the internal circuitry of the ECM. There are no repairs possible for the module in the field.

Refer to Troubleshooting Fault Code t05-343
