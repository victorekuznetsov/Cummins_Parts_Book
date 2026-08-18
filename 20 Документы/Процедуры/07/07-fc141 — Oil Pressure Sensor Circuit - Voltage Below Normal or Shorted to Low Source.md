---
aliases:
  - "Цепь датчика давления масла — напряжение ниже нормы"
type: "Процедура"
doc: "07-fc141"
title_en: "Oil Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика давления масла — напряжение ниже нормы"
modified: "2012-12-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Oil Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика давления масла — напряжение ниже нормы**

> [!abstract] Процедура · `07-fc141`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc141.pdf)

### Fault Code: 141

### Oil Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 141 PID(P): P100 SPN: 100 FMI: 4 Lamp: Amber SRT: | Oil pressure sensor circuit - voltage below normal or shorted to low source. | Engine protection for oil pressure disabled. |

![[19a00194.png]]

Oil Pressure Sensor Circuit

### Circuit Description

The oil pressure sensor monitors oil pressure and passes information to the electronic control module (ECM) through the oil pressure signal pin of the engine harness. The ECM monitors the voltage on the oil pressure signal pin. Voltage exceeding the control threshold will trip Fault Code 141.

### Component Location

Reference Section E for a detailed component location view. The oil pressure sensor is located between the coolant filter and the heater solenoids.

### Shoptalk

If the fault occurs **only** in cold weather, allow the oil to warm up and see if the fault goes inactive.

If Fault Code 143 or 415 is **not** present, the problem is **not** base engine related.

Refer to Troubleshooting Fault Code t05-141
