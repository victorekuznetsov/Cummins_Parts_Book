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
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-008-020.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-008-020.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Cooling System Diagnostics
**Диагностика системы охлаждения**

> [!abstract] Процедура · `20-008-020`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 8 - Cooling System - Group 08
> **Даты:** изменён 2003-04-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-008-020.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-008-020.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Испытание на давление

Используйте калибр давления с минимальной мощностью 275 кПа[40 psi]. Измерить давление охлаждающей жидкости на водяном коллекторе (1).

Работайте с двигателем до тех пор, пока температура охлаждающей жидкости не достигнет 80°C[180°F].

> [!note] Примечание
> Термостаты ** должны быть открыты.

![[14400009.png]]

Управляйте двигателем с номинальной оборотной стороной. Сравните показания давления со следующими спецификациями.

| Минимальное давление охлаждающей жидкости в водном коллекторе |  |  |
|---|---|---|
| Двигатель rpm | каша | пси |
| 1800 | 75 | 11 |
| 1900 | 82 | 12 |
| 2100 | 89 | 13 |

| каша |  | пси |
|---|---|---|
| 241 | Макс | 35 |

![[eg4gaka.png]]

Если вышеуказанное место измерения ** недоступно**, установите калибр в корпус масляного охладителя вместо дренажного клапана.

| Минимальное охлаждающее давление - на охладитель масла |  |  |
|---|---|---|
| Двигатель rpm | каша | пси |
| 1800 | 103 | 15 |
| 1900 | 117 | 17 |
| 2100 | 131 | 19 |

| каша |  | пси |
|---|---|---|
| 241 | Макс | 35 |

![[oi4gaka.png]]

Если давление охлаждающей жидкости высокое, проверьте термостат или радиатор на предмет ограничения. См. процедуру[[20-008-042 — Radiator|008-042]].

![[ec800sb.png]]

Если давление охлаждающей жидкости низкое, установите калибр (с максимальной емкостью 69 кПа \[10 psi\]) на входе водяного насоса.

![[wp4ilka.png]]

Управляйте двигателем с номинальной оборотной стороной. Если калибр считывает более 35 кПа[5 psi], проверьте радиатор. См. процедуру[[20-008-042 — Radiator|008-042]].

![[ra400sb.png]]


> [!quote]- Original (English) · английский оригинал
> ### Pressure Test
>
> Use a pressure gauge with a minimum capacity of 275 kPa \[40 psi\]. Measure the coolant pressure at the water manifold (1).
>
> Operate the engine until the coolant temperature reaches 80°C \[180°F\].
>
> **Note · Примечание**
> The thermostats **must** be open.
>
> Operate the engine at rated rpm. Compare the pressure readings to the following specifications.
>
> | Minimum Coolant Pressure-At-Water Manifold |  |  |
> |---|---|---|
> | Engine rpm | kPa | psi |
> | 1800 | 75 | 11 |
> | 1900 | 82 | 12 |
> | 2100 | 89 | 13 |
>
> | kpa |  | psi |
> |---|---|---|
> | 241 | MAX | 35 |
>
> If the above measurement location is **not** accessible, install the gauge in the oil cooler housing in place of the draincock.
>
> | Minimum Coolant Pressure-At-Oil Cooler Housing |  |  |
> |---|---|---|
> | Engine rpm | kPa | psi |
> | 1800 | 103 | 15 |
> | 1900 | 117 | 17 |
> | 2100 | 131 | 19 |
>
> | kpa |  | psi |
> |---|---|---|
> | 241 | MAX | 35 |
>
> If coolant pressure is high, check the thermostat or radiator for a restriction. Refer to Procedure [[20-008-042 — Radiator|008-042]].
>
> If the coolant pressure is low, install a gauge (with a maximum capacity of 69 kPa \[10 psi\]) at the water pump inlet.
>
> Operate the engine at rated rpm. If the gauge reads more than 35 kPa \[5 psi\], check the radiator. Refer to Procedure [[20-008-042 — Radiator|008-042]].
