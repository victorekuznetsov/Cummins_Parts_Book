---
aliases:
  - "Ошибка отключения питания ЭБУ"
type: "Процедура"
doc: "87-fc346"
title_en: "Electronic Control Module (ECM) Power-down Error"
title_ru: "Ошибка отключения питания ЭБУ"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc346.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc346.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Electronic Control Module (ECM) Power-down Error
**Ошибка отключения питания ЭБУ**

> [!abstract] Процедура · `87-fc346`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc346.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc346.pdf)

### Fault Code: 346

### Electronic Control Module (ECM) Power-down Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 346 PID(P): S253 SPN: 630 FMI: 12 Lamp: Yellow SRT: | ECM power-down internal data store error. | Power-down data (which include maintenance monitoring, present ECM and engine delta times, past fault data) are lost. |

![[19a00581.png]]

Battery Power and Ground Circuit

### Circuit Description

The ECM is a computer that is responsible for engine control, diagnostics, and user features.

### Component Location

An ECM is located on both sides of the engine in front of the fuel pump.

### Shoptalk

- This is a fault with the internal memory of the ECM. This fault can be caused by a power interruption to the ECM or a loss of battery power.

- An OEM master disconnect switch can cause this fault if the operator is using the master disconnect to shut the machine off or if the operator is **not** waiting 30 seconds from key-off until turning the master disconnect switch off. The ECM **must** go through an internal shutdown sequence before unswitched battery power is removed.

Refer to Troubleshooting Fault Code t05-346
