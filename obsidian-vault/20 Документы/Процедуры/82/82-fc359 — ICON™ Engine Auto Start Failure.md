---
aliases:
  - "Отказ автоматического пуска двигателя ICON™"
type: "Процедура"
doc: "82-fc359"
title_en: "ICON™ Engine Auto Start Failure"
title_ru: "Отказ автоматического пуска двигателя ICON™"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc359.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc359.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# ICON™ Engine Auto Start Failure
**Отказ автоматического пуска двигателя ICON™**

> [!abstract] Процедура · `82-fc359`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc359.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc359.pdf)

### Fault Code: 359

### ICON™ Engine Auto Start Failure

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 359 PID(P): SPN: FMI: 11 Lamp: Yellow SRT: | The ICON™ system has failed to start the engine automatically. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Can possibly start engine normally. |

![[19803217.png]]

Integrated Idle ICON™ Circuit

### Circuit Description

The starter relay circuit controls and monitors both the starter relay coil and return signal. The starter relay is used by the ICON™ feature to perform automatic starts of the engine.

### Component Location

The starter relay is mounted on the fire wall of the vehicle on the intake side of the engine.

### Shoptalk

This fault code is set if two consecutive automatic starts fail. If a start is commanded by the ECM and 200 rpm is **not** reached within 2 seconds nor 450 rpm within 14 seconds, then the start failed. After the first failure, ICON™ waits one minute and tries again. If the second start fails, the fault is set. It is cleared as soon as a manual start is successful.

Refer to Troubleshooting Fault Code t05-359
