---
type: "Процедура"
doc: "81-fc335"
title_en: "Internal Engine Control Module (ECM) Error"
modified: "2015-07-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc335.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc335.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# Internal Engine Control Module (ECM) Error

> [!abstract] Процедура · `81-fc335`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc335.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc335.pdf)

### Fault Code: 335

### Internal Engine Control Module (ECM) Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 335 PID(P): 254 SPN: 629 FMI: 12 Lamp: None SRT: 00-680 | Internal ECM error. | Data may be lost. |

![[19800425.png]]

Electronic Control Module

### Circuit Description

The CENSE™ ECM is a computer that is responsible for engine diagnostics.

### Component Location

The CENSE™ ECM is installed on a plate that is located above the flywheel housing.

### Shoptalk

This fault code indicates a possible internal ECM failure. The ECM can **not** be repaired in the field. Before replacing the ECM, use INSITE™ for CENSE™ to reset the fault codes and trend log using the CENSE™ data reset command under the Adjustments menu.

Refer to Troubleshooting Fault Code t05-335
