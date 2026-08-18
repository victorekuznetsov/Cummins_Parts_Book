---
aliases:
  - "Микропроцессор электронного блока управления"
type: "Процедура"
doc: "87-fc111"
title_en: "Electronic Control Module Microprocessor"
title_ru: "Микропроцессор электронного блока управления"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Electronic Control Module Microprocessor
**Микропроцессор электронного блока управления**

> [!abstract] Процедура · `87-fc111`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc111.pdf)

### Fault Code: 111

### Electronic Control Module Microprocessor

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 111 PID(P): S254 SPN: 629 FMI: 12 Lamp: Red SRT: | Error internal to the ECM, related to the memory hardware failures or internal microprocessor communication failures. | Engine will **not** start. |

![[19900397.png]]

ECM

### Circuit Description

The CM 552 ECM is a computer that is responsible for engine control, diagnostics, and user features.

### Component Location

Two ECMs are on board the QST30 engine, one on each side, in front of the fuel pumps.

### Shoptalk

This fault code can **only** be caused by an internal ECM problem. There are no repairs possible for the module in the field.

Refer to Troubleshooting Fault Code t05-111
