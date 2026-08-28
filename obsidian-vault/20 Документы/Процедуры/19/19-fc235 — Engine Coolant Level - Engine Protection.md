---
aliases:
  - "Уровень охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "19-fc235"
title_en: "Engine Coolant Level - Engine Protection"
title_ru: "Уровень охлаждающей жидкости — защита двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc235.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc235.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Engine Coolant Level - Engine Protection
**Уровень охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `19-fc235`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc235.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc235.pdf)

### Fault Code: 235

### Engine Coolant Level - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 235 PID(P): P111 SPN: 111 FMI: 1 Lamp: Engine Protection SRT: 00-364 | Low coolant level has been detected. Voltage signal on the coolant level signal pin 23 of the OEM harness indicates low radiator coolant level on the vehicle. | Calibration-dependent progressive power and speed derate and engine shutdown with increasing time after alert. |

![[19400153.png]]

Engine Coolant Level - Engine Protection

### Circuit Description

The coolant level sensor monitors the coolant level within the coolant system and passes information to the ECM through the OEM harness.

### Component Location

The coolant level sensor is located in the radiator top tank or surge tank.

### Shoptalk

This is an OEM-supplied component and will vary in sensor location.

- When the coolant level drops below a certain level, a power derate will be activated, which will decrease the power output by 50 percent over a 30-second period.

- If a shorting plug is used in the coolant level circuit, verify that it is wired correctly.

- Inspect the wiring harness between the four-way Weather-Pack connector and the coolant level sensor for damage.

- Make sure the coolant level sensor is located in the middle of the tank, rather than off to one side where the coolant level can change when the vehicle turns a corner.

Refer to Troubleshooting Fault Code t05-235
