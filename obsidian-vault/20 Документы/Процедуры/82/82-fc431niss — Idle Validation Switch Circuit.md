---
aliases:
  - "Цепь выключателя подтверждения холостого хода"
type: "Процедура"
doc: "82-fc431niss"
title_en: "Idle Validation Switch Circuit"
title_ru: "Цепь выключателя подтверждения холостого хода"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc431niss.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc431niss.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Idle Validation Switch Circuit
**Цепь выключателя подтверждения холостого хода**

> [!abstract] Процедура · `82-fc431niss`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc431niss.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc431niss.pdf)

### Fault Code: 431

### Idle Validation Switch Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 431 PID(P): P091 SPN: 91 FMI: 2/2 Lamp: Yellow SRT: | Voltage detected simultaneously on both the idle validation off-idle and on-idle signal pins. | None on performance. |

![[19c00644.png]]

Idle Validation Switch Circuit

### Circuit Description

The idle validation switch is used by the electronic control module (ECM) to indicate when the accelerator pedal is released (on-idle) or depressed (off-idle). The switch is adjusted at the factory to switch from on-idle to off-idle at the correct accelerator pedal position.

### Component Location

The nonintegrated sensor switch (NISS) is located on the accelerator pedal assembly.

### Shoptalk

- This fault code is usually caused by a loose connection, uncalibrated accelerator pedal, or miswired idle validation switch.

- The integrated sensor switch (ISS) has a different idle validation switch (IVS) resistance specification (125 ohms) as compared to nonintegrated sensor switch (NISS) (10 ohms).

Refer to Troubleshooting Fault Code t05-431niss
