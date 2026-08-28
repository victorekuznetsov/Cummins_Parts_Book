---
aliases:
  - "Диагностика системы охлаждения"
type: "Процедура"
doc: "20-008-020"
title_en: "Cooling System Diagnostics"
title_ru: "Диагностика системы охлаждения"
modified: "2003-04-29"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-008-020.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-008-020.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Cooling System Diagnostics
**Диагностика системы охлаждения**

> [!abstract] Процедура · `20-008-020`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 8 - Cooling System - Group 08
> **Даты:** изменён 2003-04-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-008-020.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-008-020.pdf)

### Pressure Test

Use a pressure gauge with a minimum capacity of 275 kPa \[40 psi\]. Measure the coolant pressure at the water manifold (1).

Operate the engine until the coolant temperature reaches 80°C \[180°F\].

> [!note] Note · Примечание
> The thermostats **must** be open.

![[14400009.png]]

Operate the engine at rated rpm. Compare the pressure readings to the following specifications.

| Minimum Coolant Pressure-At-Water Manifold |  |  |
|---|---|---|
| Engine rpm | kPa | psi |
| 1800 | 75 | 11 |
| 1900 | 82 | 12 |
| 2100 | 89 | 13 |

| kpa |  | psi |
|---|---|---|
| 241 | MAX | 35 |

![[eg4gaka.png]]

If the above measurement location is **not** accessible, install the gauge in the oil cooler housing in place of the draincock.

| Minimum Coolant Pressure-At-Oil Cooler Housing |  |  |
|---|---|---|
| Engine rpm | kPa | psi |
| 1800 | 103 | 15 |
| 1900 | 117 | 17 |
| 2100 | 131 | 19 |

| kpa |  | psi |
|---|---|---|
| 241 | MAX | 35 |

![[oi4gaka.png]]

If coolant pressure is high, check the thermostat or radiator for a restriction. Refer to Procedure [[20-008-042 — Radiator|008-042]].

![[ec800sb.png]]

If the coolant pressure is low, install a gauge (with a maximum capacity of 69 kPa \[10 psi\]) at the water pump inlet.

![[wp4ilka.png]]

Operate the engine at rated rpm. If the gauge reads more than 35 kPa \[5 psi\], check the radiator. Refer to Procedure [[20-008-042 — Radiator|008-042]].

![[ra400sb.png]]
