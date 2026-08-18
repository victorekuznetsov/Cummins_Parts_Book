---
aliases:
  - "Цепь переключателя «Выкл/Ручной/Авто» — напряжение ниже нормы"
type: "Процедура"
doc: "01-fc1332"
title_en: "Off/Manual/Auto Switch Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь переключателя «Выкл/Ручной/Авто» — напряжение ниже нормы"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1332.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1332.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Off/Manual/Auto Switch Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь переключателя «Выкл/Ручной/Авто» — напряжение ниже нормы**

> [!abstract] Процедура · `01-fc1332`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1332.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1332.pdf)

### Fault Code: 1332

### Off/Manual/Auto Switch Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1332 PID(P): SPN: FMI: Lamp: Warning SRT: | The Off/Manual/Auto switch signal is shorted low. | The ECM will **only** allow the generator set to run in Auto. |

![[19802777.png]]

Off/Manual/Auto Switch Circuit

### Circuit Description

The Off/Manual/Auto switch is monitored by the engine control module (ECM) to determine the operation mode of the generator set.

The ECM monitors the voltage on the operation mode switch manual SIGNAL pin and expects to see a voltage vary between 0.5 and 4.5-VDC during normal operation. The ECM monitors the voltage on the operation mode switch auto SIGNAL pin and expects to see a voltage of either 0 or 5-VDC during normal operation. Low voltage will trip Fault Code 1332 and can be caused by shorts in the signal, or return wires, an open in the return wire, or a failed switch.

### Component Location

Reference Section E for location of the operator interface panel and the Off/Manual/Auto switch.

### Shoptalk

The possible failure modes are open circuit, short to ground, failed switch, and loss of supply voltage inside the ECM.

The ECM will consider the switch to be in the Auto position when the auto SIGNAL pin is grounded, regardless of the state of the manual SIGNAL pin.

Refer to Troubleshooting Fault Code t05-1332.
