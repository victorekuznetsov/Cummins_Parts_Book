---
aliases:
  - "Множественный код неисправности A"
type: "Процедура"
doc: "07-fcmfc01"
title_en: "Multiple Fault Code A"
title_ru: "Множественный код неисправности A"
modified: "2012-12-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fcmfc01.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fcmfc01.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Multiple Fault Code A
**Множественный код неисправности A**

> [!abstract] Процедура · `07-fcmfc01`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fcmfc01.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fcmfc01.pdf)

### Fault Code: A

### Multiple Fault Code A

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: A PID(P): SPN: FMI: Lamp: SRT: | Multiple fault codes are generated due to a common supply or return wire failure in the engine harness. | Fault Codes 122 and 135 are active. |

![[19900397.png]]

Electronic Control Module (ECM)

### Circuit Description

The electronic control module (ECM) supplies all engine pressure sensors on the engine harness with +5 VDC. The ECM has common returns for all the engine pressure and temperature sensors. Reference the wiring diagram, Bulletin 4021331, for the pin assignments of these circuits. A failure on either of these circuits causes multiple fault codes.

### Component Location

Reference Section E for a detailed component location view. The ECM is located at the top of the engine, mounted to the air intake manifold.

### Shoptalk

An open circuit in the common supply and return wires, short circuits from battery or ground to the supply, or a defective ECM power supply can cause multiple fault codes.

A failed pressure sensor can cause multiple fault codes.

A failed pressure sensor can cause multiple active fault codes to go inactive once the engine has been started.

Refer to Troubleshooting Fault Code t05-mfc01
