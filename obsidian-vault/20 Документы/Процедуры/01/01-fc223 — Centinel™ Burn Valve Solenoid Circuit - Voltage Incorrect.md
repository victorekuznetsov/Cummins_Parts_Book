---
aliases:
  - "Цепь электромагнита клапана впрыска Centinel™ — неверное напряжение"
type: "Процедура"
doc: "01-fc223"
title_en: "Centinel™ Burn Valve Solenoid Circuit - Voltage Incorrect"
title_ru: "Цепь электромагнита клапана впрыска Centinel™ — неверное напряжение"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc223.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc223.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Centinel™ Burn Valve Solenoid Circuit - Voltage Incorrect
**Цепь электромагнита клапана впрыска Centinel™ — неверное напряжение**

> [!abstract] Процедура · `01-fc223`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc223.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc223.pdf)

### Fault Code: 223

### Centinel™ Burn Valve Solenoid Circuit - Voltage Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 223 PID(P): S85 SPN: 1265 FMI: 4 Lamp: Yellow SRT: | The Centinel™ burn valve solenoid circuit is open or shorted. Less than 18.0 VDC detected at the Centinel™ burn valve solenoid supply pin of the engine harness or resistance of the solenoid has dropped below 80 ohms. | ECM turns off the burn valve supply voltage and the Centinel™ system is disabled. |

![[19803602.png]]

Burn Valve Solenoid Circuit

### Circuit Description

The burn valve solenoid controls the flow of oil in the oil control valve during the burn cycle.

### Component Location

The burn valve solenoid is located on top of the oil control valve.

Refer to Troubleshooting Fault Code t05-223
