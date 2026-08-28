---
aliases:
  - "Микропроцессор ЭБУ"
type: "Процедура"
doc: "19-fc111"
title_en: "Electronic Control Module (ECM) Microprocessor"
title_ru: "Микропроцессор ЭБУ"
modified: "2011-03-01"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Electronic Control Module (ECM) Microprocessor
**Микропроцессор ЭБУ**

> [!abstract] Процедура · `19-fc111`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc111.pdf)

### Fault Code: 111

### Electronic Control Module (ECM) Microprocessor

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 111 PID(P): S254 SPN: 629 FMI: 12 Lamp: Red SRT: 00-606 | Error internal to the ECM related to memory hardware failures or internal processor communication failures. | Mission-disabling failure. Engine **not** allowed to start. |

![[19400316.png]]

ECM Microprocessor

### Circuit Description

The ECM is a computer that is responsible for engine control, diagnostics, and user features.

### Component Location

The ECM is bolted to the electronic control valve assembly on the intake side of the engine.

### Shoptalk

This fault code can **only** be caused by an internal ECM problem. It is impossible to repair an ECM.

Refer to Troubleshooting Fault Code t05-111
