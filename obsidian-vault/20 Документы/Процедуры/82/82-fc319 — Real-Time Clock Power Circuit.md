---
aliases:
  - "Цепь питания часов реального времени"
type: "Процедура"
doc: "82-fc319"
title_en: "Real-Time Clock Power Circuit"
title_ru: "Цепь питания часов реального времени"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc319.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc319.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Real-Time Clock Power Circuit
**Цепь питания часов реального времени**

> [!abstract] Процедура · `82-fc319`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc319.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc319.pdf)

### Fault Code: 319

Real-Time Clock Power Circuit

### Real-Time Clock Power Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 319 PID(P): P251 SPN: 251 FMI: 2/2 Lamp: Maintenance SRT: | Real-time clock lost power. | None on performance. Data in the ECM will **not** have accurate time and date information. |

![[19200382.png]]

Real-Time Clock Power Circuit

### Circuit Description

Under ordinary operating conditions, the real-time clock in the ECM is powered by the vehicle's batteries. If battery power to the ECM is lost, then the real-time clock will be powered by a battery backup module (if equipped).

### Component Location

The real-time clock battery backup module is secured to the wiring harness in the vicinity of the ECM. The ECM is located on the fuel pump side of the engine either above the air compressor (high-mount) or above the starter (low-mount).

### Shoptalk

This fault indicates that the real-time clock in the ECM lost power. Possible causes for this fault:

- A weak or failed battery backup module

- Failed wiring or connectors between the battery backup module and ECM

- The engine is **not** equipped with a battery backup module, and lost vehicle battery power to the ECM.

Refer to Troubleshooting Fault Code t05-319
