---
aliases:
  - "Низкое напряжение АКБ 1 — предупреждение"
type: "Процедура"
doc: "01-fc441"
title_en: "Battery 1 Voltage Low - Warning"
title_ru: "Низкое напряжение АКБ 1 — предупреждение"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc441.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc441.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Battery 1 Voltage Low - Warning
**Низкое напряжение АКБ 1 — предупреждение**

> [!abstract] Процедура · `01-fc441`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc441.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc441.pdf)

### Fault Code: 441

### Battery 1 Voltage Low - Warning

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 441 PID(P): SPN: FMI: Lamp: Warning SRT: | Battery 1 voltage low - warning. | ECM voltage supply approaching level at which unpredictable operation will occur. |

![[19803586.png]]

Unswitched Battery Supply Circuit

### Circuit Description

The electronic control module (ECM) receives unswitched battery input through the engine harness. There is an in-line 20-amp fuse in the unswitched positive (+) battery wire of the engine harness to protect the engine harness from overheating. The battery wires are connected to the starters. The customer connects the batteries to the starters.

### Component Location

The ECM is connected to the battery by the OEM harness. This direct link provides a constant power supply for the ECM. Refer to the OEM manual for the battery location.

### Shoptalk

This fault is usually caused by loose or corroded battery connections.

Refer to Troubleshooting Fault Code t05-441
