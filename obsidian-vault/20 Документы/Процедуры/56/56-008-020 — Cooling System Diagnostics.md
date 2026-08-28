---
aliases:
  - "Диагностика системы охлаждения"
type: "Процедура"
doc: "56-008-020"
title_en: "Cooling System Diagnostics"
title_ru: "Диагностика системы охлаждения"
modified: "2004-02-03"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "4021530"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-008-020.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-008-020.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/56"
---

# Cooling System Diagnostics
**Диагностика системы охлаждения**

> [!abstract] Процедура · `56-008-020`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 8 - Cooling System - Group 08
> **Даты:** изменён 2004-02-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-008-020.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-008-020.pdf)

### Pressure Test

Use a pressure gauge with a minimum capacity of 275 kPa \[40 psi\]. Measure the coolant pressure at the thermostat housing.

Operate the engine until the coolant temperature reaches 85°C \[185°F\].

The thermostats **must** be open.

![[19600079.png]]

Operate the engine at rated rpm. Compare the pressure readings to the following specifications.

|  | kpa |  | psi |
|---|---|---|---|
| 1800 rpm | 75 | MIN | 11 |
| 1900 rpm | 82 | MIN | 12 |
| 2100 rpm | 89 | MIN | 13 |

| kpa |  | psi |
|---|---|---|
| 241 | MAX | 35 |

![[eg4gaka.png]]

If the above measurement location is **not** accessible, install the gauge in the engine block in place of the draincock.

|  | kpa |  | psi |
|---|---|---|---|
| 1800 rpm | 103 | MIN | 15 |
| 1900 rpm | 117 | MIN | 17 |
| 2100 rpm | 131 | MIN | 19 |

| kpa |  | psi |
|---|---|---|
| 241 | MAX | 35 |

![[07600329.png]]

If the coolant pressure is high, make sure the thermostats are operating correctly. Refer to Procedure [[56-008-013-tr — Coolant Thermostat|008-013]].

If the thermostats are OK, inspect the radiator for restriction. Refer to Procedure [[56-008-042 — Radiator|008-042]].

![[ec800sb.png]]

If the cooling system pressure is low, install a gauge (with a maximum capacity of 69 kPa \[10 psi\]) at the water pump inlet.

![[08600226.png]]

Operate the engine at rated rpm. If the gauge reads more than 35 kPa \[5 psi\], check the radiator for restriction. Refer to Procedure [[56-008-042 — Radiator|008-042]].

![[ra400sb.png]]
