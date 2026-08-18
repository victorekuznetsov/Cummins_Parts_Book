---
aliases:
  - "Высокая температура охлаждающей жидкости — предупреждение"
type: "Процедура"
doc: "01-fc146"
title_en: "Engine Coolant Temperature High - Warning"
title_ru: "Высокая температура охлаждающей жидкости — предупреждение"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc146.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc146.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Coolant Temperature High - Warning
**Высокая температура охлаждающей жидкости — предупреждение**

> [!abstract] Процедура · `01-fc146`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc146.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc146.pdf)

### Fault Code: 146

### Engine Coolant Temperature High - Warning

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 146 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine coolant temperature has exceeded the warning threshold for high coolant temperature. | Calibration dependent no action is taken by the ECM or engine shutdown as temperature increases over thresholds. Pre-High Engine Temperature relay driver is energized. |

![[19803592.png]]

Coolant Temperature Sensor Circuit

### Circuit Description

The coolant temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system, timing, and fueling control. If the voltage is low for more than 2 seconds, the ECM will log Fault Code 146.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Make sure the airflow through the radiator is **not** obstructed.The resistance of all the temperature sensors varies with the temperature.

Refer to Troubleshooting Fault Code t05-146
