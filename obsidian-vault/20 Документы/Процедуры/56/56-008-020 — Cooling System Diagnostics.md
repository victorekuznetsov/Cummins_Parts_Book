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
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-008-020.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-008-020.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/56"
  - "перевод/машинный"
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

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Испытание на давление

Используйте калибр давления с минимальной мощностью 275 кПа[40 psi]. Измерьте давление охлаждающей жидкости в корпусе термостата.

Работайте с двигателем до тех пор, пока температура охлаждающей жидкости не достигнет 85 ° C[185 ° F].

Термостаты должны быть открыты.

![[19600079.png]]

Управляйте двигателем с номинальной оборотной стороной. Сравните показания давления со следующими спецификациями.

|  | каша |  | пси |
|---|---|---|---|
| 1800 об/мин | 75 | Мин | 11 |
| 1900 об/мин | 82 | Мин | 12 |
| 2100 об/мин | 89 | Мин | 13 |

| каша |  | пси |
|---|---|---|
| 241 | Макс | 35 |

![[eg4gaka.png]]

Если вышеуказанное место измерения **недоступно**, установите калибр в блоке двигателя вместо дренажного клапана.

|  | каша |  | пси |
|---|---|---|---|
| 1800 об/мин | 103 | Мин | 15 |
| 1900 об/мин | 117 | Мин | 17 |
| 2100 об/мин | 131 | Мин | 19 |

| каша |  | пси |
|---|---|---|
| 241 | Макс | 35 |

![[07600329.png]]

Если давление охлаждающей жидкости высокое, убедитесь, что термостаты работают правильно. См. процедуру[[56-008-013-tr — Coolant Thermostat|008-013]].

Если термостаты в порядке, проверьте радиатор на предмет ограничения. См. процедуру[[56-008-042 — Radiator|008-042]].

![[ec800sb.png]]

Если давление в системе охлаждения низкое, установите калибр (максимальная емкость 69 кПа[10 psi]) на входе водяного насоса.

![[08600226.png]]

Управляйте двигателем с номинальной оборотной стороной. Если калибр считывает более 35 кПа[5 psi], проверьте радиатор на предмет ограничения. См. процедуру[[56-008-042 — Radiator|008-042]].

![[ra400sb.png]]


> [!quote]- Original (English) · английский оригинал
> ### Pressure Test
>
> Use a pressure gauge with a minimum capacity of 275 kPa \[40 psi\]. Measure the coolant pressure at the thermostat housing.
>
> Operate the engine until the coolant temperature reaches 85°C \[185°F\].
>
> The thermostats **must** be open.
>
> Operate the engine at rated rpm. Compare the pressure readings to the following specifications.
>
> |  | kpa |  | psi |
> |---|---|---|---|
> | 1800 rpm | 75 | MIN | 11 |
> | 1900 rpm | 82 | MIN | 12 |
> | 2100 rpm | 89 | MIN | 13 |
>
> | kpa |  | psi |
> |---|---|---|
> | 241 | MAX | 35 |
>
> If the above measurement location is **not** accessible, install the gauge in the engine block in place of the draincock.
>
> |  | kpa |  | psi |
> |---|---|---|---|
> | 1800 rpm | 103 | MIN | 15 |
> | 1900 rpm | 117 | MIN | 17 |
> | 2100 rpm | 131 | MIN | 19 |
>
> | kpa |  | psi |
> |---|---|---|
> | 241 | MAX | 35 |
>
> If the coolant pressure is high, make sure the thermostats are operating correctly. Refer to Procedure [[56-008-013-tr — Coolant Thermostat|008-013]].
>
> If the thermostats are OK, inspect the radiator for restriction. Refer to Procedure [[56-008-042 — Radiator|008-042]].
>
> If the cooling system pressure is low, install a gauge (with a maximum capacity of 69 kPa \[10 psi\]) at the water pump inlet.
>
> Operate the engine at rated rpm. If the gauge reads more than 35 kPa \[5 psi\], check the radiator for restriction. Refer to Procedure [[56-008-042 — Radiator|008-042]].
