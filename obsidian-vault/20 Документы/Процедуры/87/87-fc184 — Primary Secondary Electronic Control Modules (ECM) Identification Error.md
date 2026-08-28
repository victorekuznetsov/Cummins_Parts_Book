---
aliases:
  - "Ошибка идентификации основного и резервного ЭБУ"
type: "Процедура"
doc: "87-fc184"
title_en: "Primary/Secondary Electronic Control Modules (ECM) Identification Error"
title_ru: "Ошибка идентификации основного и резервного ЭБУ"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc184.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc184.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Primary/Secondary Electronic Control Modules (ECM) Identification Error
**Ошибка идентификации основного и резервного ЭБУ**

> [!abstract] Процедура · `87-fc184`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc184.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc184.pdf)

### Fault Code: 184

### Primary/Secondary Electronic Control Modules (ECM) Identification Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 184 PID(P): S233 SPN: 609 FMI: 2 Lamp: Red SRT: | Primary and/or secondary ECM identification error. | Module identification at power-up will fail; both modules will run as secondary ECMs. Possible loss of performance. |

![[19a00382.png]]

Primary/Secondary ECM Identification Error

### Circuit Description

The QST30 control system utilizes two ECMs, one primary and one secondary.

### Component Location

One ECM is located on both sides of the engine in front of the fuel pumps.

### Shoptalk

Identification between primary and secondary modules is done at key-on through the harness. Pins 47 and 48 of the engine harness for each bank provide the determination of primary or secondary. Reference the following table for primary/secondary identification:

| ECM Identification | VDC at Pin 47 | VDC at Pin 48 |
|---|---|---|
| Primary | +5 VDC | 0 VDC |
| Secondary | 0 VDC | +5 VDC |

Refer to Troubleshooting Fault Code t05-184
