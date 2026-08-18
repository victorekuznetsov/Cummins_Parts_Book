---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "82-fc341"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc341.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc341.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `82-fc341`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc341.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc341.pdf)

### Fault Code: 341

### Unswitched Battery Supply Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 341 PID(P): S253 SPN: 630 FMI: 2/2 Lamp: Yellow SRT: | Severe loss of data from the ECM. | Possibly no noticeable performance effects, **or** engine dying, **or** difficulty in starting the engine. Fault information, trip information, and maintenance monitor data can be inaccurate. |

![[19c00043.png]]

Unswitched Battery Supply Circuit

### Circuit Description

The ECM receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the positive (+) battery post. There are two in-line 15-amp fuses in the unswitched battery wires to protect the engine harness from overheating. The ECM receives switched battery input through the vehicle keyswitch wire when the vehicle keyswitch is turned on. The battery return wires are connected directly to the negative (-) battery post.

### Component Location

The ECM is connected to the battery by the OEM harness. This direct link provides a constant power supply for the ECM. The location of the battery will vary with the OEM. Refer to the OEM troubleshooting and repair manual.

Refer to Troubleshooting Fault Code t05-341
