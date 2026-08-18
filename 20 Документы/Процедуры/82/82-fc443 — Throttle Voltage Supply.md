---
aliases:
  - "Питание датчика подачи топлива"
type: "Процедура"
doc: "82-fc443"
title_en: "Throttle Voltage Supply"
title_ru: "Питание датчика подачи топлива"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc443.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc443.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Throttle Voltage Supply
**Питание датчика подачи топлива**

> [!abstract] Процедура · `82-fc443`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc443.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc443.pdf)

### Fault Code: 443

### Throttle Voltage Supply

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 443 PID(P): S221 SPN: 1043 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected on the electronic control module (ECM) voltage supply line to the throttle(s). | Engine will **only** idle. |

![[19c00644.png]]

Throttle Position Supply Voltage Circuit

### Circuit Description

The ECM supplies the accelerator and the remote throttle with +5 VDC. If the supply line to the accelerators is damaged, the accelerators will **not** work correctly.

### Component Location

Accelerator pedal is located in the cab. Refer to the OEM manual for remote throttle location.

### Shoptalk

Low voltage on the +5-VDC supply line will be caused by a short circuit to ground in a supply line, a short circuit between a supply line or a return line, a failed accelerator, or a failed ECM power supply.

Refer to Troubleshooting Fault Code t05-443
