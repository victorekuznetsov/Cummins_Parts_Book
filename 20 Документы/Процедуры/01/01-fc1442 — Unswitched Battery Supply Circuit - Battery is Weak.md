---
aliases:
  - "Цепь постоянного питания от АКБ — АКБ разряжена"
type: "Процедура"
doc: "01-fc1442"
title_en: "Unswitched Battery Supply Circuit - Battery is Weak"
title_ru: "Цепь постоянного питания от АКБ — АКБ разряжена"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1442.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1442.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Unswitched Battery Supply Circuit - Battery is Weak
**Цепь постоянного питания от АКБ — АКБ разряжена**

> [!abstract] Процедура · `01-fc1442`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1442.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1442.pdf)

### Fault Code: 1442

### Unswitched Battery Supply Circuit - Battery is Weak

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1442 PID(P): SPN: FMI: Lamp: Warning SRT: | Battery is weak. | No action is taken by the ECM. |

![[19802506.png]]

Unswitched Battery Supply Circuit

### Circuit Description

The engine control module (ECM) receives unswitched battery input through the engine harness. There is an in-line 20 amp fuse in the unswitched positive (+) battery wire of the engine harness to protect the engine harness from overheating. The battery return wires are connected directly to the negative (-) battery post.

### Component Location

The ECM is connected to the battery by the OEM harness. This direct link provides a constant power supply for the ECM. Refer to the OEM manual for the battery location.

### Shoptalk

This fault is usually caused by loose or corroded battery connections.

Refer to Troubleshooting Fault Code t05-1442.
