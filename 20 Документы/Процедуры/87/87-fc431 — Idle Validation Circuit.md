---
aliases:
  - "Цепь подтверждения холостого хода"
type: "Процедура"
doc: "87-fc431"
title_en: "Idle Validation Circuit"
title_ru: "Цепь подтверждения холостого хода"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc431.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc431.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Idle Validation Circuit
**Цепь подтверждения холостого хода**

> [!abstract] Процедура · `87-fc431`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc431.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc431.pdf)

### Fault Code: 431

### Idle Validation Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 431 PID(P): P91 SPN: 091, 607 FMI: 2 or 4 Lamp: Yellow or Red SRT: | Voltage detected simultaneously on both the idle validation off-idle and idle-signal pins 25 and 26 of the OEM interface harness. | None on performance. |

![[19900374.png]]

Idle Validation Circuit

### Circuit Description

The idle validation signal is a feature that disables accelerator control while an improper validation signal is detected by the electronic control module (ECM). The idle validation switch provides an on-idle and off-idle validation signal to the ECM through the OEM harness and OEM interface harness.

### Component Location

The accelerator pedal or lever location varies with each OEM. Refer to the OEM manual.

### Shoptalk

This fault code is usually caused by the improper wiring of the harnesses and idle validation switch.

Note: If the accelerator or accelerator position sensor is changed, or after a calibration download, cycle the accelerator pedal (keyswitch in the ON position) through its complete travel three times. This procedure calibrates the new accelerator with the ECM.

Refer to Troubleshooting Fault Code t05-431
