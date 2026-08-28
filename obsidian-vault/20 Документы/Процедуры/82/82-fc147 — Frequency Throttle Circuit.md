---
aliases:
  - "Цепь частотного задания подачи"
type: "Процедура"
doc: "82-fc147"
title_en: "Frequency Throttle Circuit"
title_ru: "Цепь частотного задания подачи"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc147.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc147.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Frequency Throttle Circuit
**Цепь частотного задания подачи**

> [!abstract] Процедура · `82-fc147`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc147.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc147.pdf)

### Fault Code: 147 (Industrial)

### Frequency Throttle Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 147 PID(P): P091 SPN: 91 FMI: 8/8 Lamp: Red SRT: | A frequency of less than 100 Hz has been detected at frequency throttle signal pin 30 of the engine harness. | Calibration-dependent power and speed derate. |

![[19c00516.png]]

Frequency Throttle Circuit

### Circuit Description

The frequency throttle provides the driver's throttle command to the ECM through the OEM harness and the engine harness. The ECM uses this signal to determine the fueling command.

### Component Location

Throttle location varies with each OEM. Refer to the OEM manual.

### Shoptalk

The frequency throttle can either be used in conjunction with a voltage throttle or by itself.

Refer to Troubleshooting Fault Code t05-147
