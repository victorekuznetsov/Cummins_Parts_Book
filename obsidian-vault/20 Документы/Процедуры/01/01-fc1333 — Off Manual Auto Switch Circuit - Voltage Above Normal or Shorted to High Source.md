---
aliases:
  - "Цепь переключателя «Выкл/Ручной/Авто» — напряжение выше нормы"
type: "Процедура"
doc: "01-fc1333"
title_en: "Off/Manual/Auto Switch Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь переключателя «Выкл/Ручной/Авто» — напряжение выше нормы"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1333.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1333.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Off/Manual/Auto Switch Circuit - Voltage Above Normal or Shorted to High Source
**Цепь переключателя «Выкл/Ручной/Авто» — напряжение выше нормы**

> [!abstract] Процедура · `01-fc1333`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1333.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1333.pdf)

### Fault Code: 1333

### Off/Manual/Auto Switch Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1333 PID(P): SPN: FMI: Lamp: Warning SRT: | The Off/Manual/Auto switch signal is shorted high. | The ECM will default to an Off value when switch is in Manual. Auto and Off positions will function normally. |

![[19802777.png]]

Off/Manual/Auto Switch Circuit

### Circuit Description

The Off/Manual/Auto switch is monitored by the engine control module (ECM) to determine the operation mode of the generator set.

The ECM monitors the voltage on the operation mode switch manual SIGNAL pin and expects to see a voltage vary between 0.5 and 4.5-VDC during normal operation. The ECM monitors the voltage on the operation mode switch auto SIGNAL pin and expects to see a voltage of either 0 or 5-VDC during normal operation. High voltage will trip Fault Code 1333 and can be caused by shorts in the signal, or return wires, an open in the return wire, or a failed switch.

### Component Location

Reference Section E for location of the operator interface panel and the Off/Manual/Auto switch.

### Shoptalk

The possible failure modes are open circuit, short to battery positive (+), failed switch, and loss of supply voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1333.
