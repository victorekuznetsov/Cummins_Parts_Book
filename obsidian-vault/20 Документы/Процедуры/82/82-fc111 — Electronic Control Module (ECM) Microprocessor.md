---
aliases:
  - "Микропроцессор ЭБУ"
type: "Процедура"
doc: "82-fc111"
title_en: "Electronic Control Module (ECM) Microprocessor"
title_ru: "Микропроцессор ЭБУ"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Electronic Control Module (ECM) Microprocessor
**Микропроцессор ЭБУ**

> [!abstract] Процедура · `82-fc111`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc111.pdf)

### Fault Code: 111

### Electronic Control Module (ECM) Microprocessor

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 111 PID(P): S254 SPN: 629 FMI: 12/12 Lamp: Red SRT: | Error internal to the ECM related to the memory hardware failures or internal ECM voltage supply circuits. | Engine will **not** start. |

![[19c00010.png]]

ECM Microprocessor

### Circuit Description

The ECM is a computer that is responsible for engine control, diagnostics, and user features.

### Component Location

The ECM is bolted to the fuel pump side of the engine and can be located either above the air compressor (high-mount) or above the starter (low-mount).

### Shoptalk

This fault code can **only** be caused by an internal ECM problem. Repairs are **not** possible for the ECM.

Refer to Troubleshooting Fault Code t05-111
