---
aliases:
  - "Лампа ICON™"
type: "Процедура"
doc: "82-fc198"
title_en: "ICON™ Lamp"
title_ru: "Лампа ICON™"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc198.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc198.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# ICON™ Lamp
**Лампа ICON™**

> [!abstract] Процедура · `82-fc198`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc198.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc198.pdf)

### Fault Code: 198

### ICON™ Lamp

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 198 PID(P): S122, 3 SPN: 612 FMI: 3 Lamp: Yellow SRT: | High voltage detected at the ICON™ lamp circuit when low voltage was expected by the ECM. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. |

![[19803214.png]]

ICON™ Lamp Circuit

### Circuit Description

The ICON™ lamp circuit illuminates the ICON™ lamp to indicate when the ICON™ system is active. In addition, ICON™ fault codes will be flashed out on this lamp. The lamp circuit requires a specific flash timing (on/off timing). If the on/off voltage is incorrect, ICON™ will be disabled. The lamp circuit **must** be functional to enable ICON™.

### Component Location

The ICON™ lamp is located in the vehicle cab on the dash panel.

### Shoptalk

This fault indicates a short circuit to battery voltage. The ICON™ lamp will **only** flash out the active fault codes.

Refer to Troubleshooting Fault Code t05-198
