---
aliases:
  - "Сопротивление на входе топлива"
type: "Процедура"
doc: "56-006-020"
title_en: "Fuel Inlet Restriction"
title_ru: "Сопротивление на входе топлива"
modified: "2006-08-17"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33239746"
families:
  - "QSK60"
  - "QSK60 CM2150 MCRS"
manuals:
  - "4021530"
figures: 19
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-006-020.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-006-020.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "двигатель/QSK60CM2150MCRS"
  - "группа/56"
  - "перевод/машинный"
---

# Fuel Inlet Restriction
**Сопротивление на входе топлива**

> [!abstract] Процедура · `56-006-020`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]]
> **Семейство:** QSK60, QSK60 CM2150 MCRS
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2006-08-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-006-020.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-006-020.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Измерение

с форсункой механического управления

Используйте фитинг Compuchek®, вакуумную измерительную приборную панель и адаптер. Подключите калибр к установке Compuchek® на впускном устройстве топливного насоса.

![[06400054.png]]

Запуск и эксплуатация двигателя на высоком холостом ходу, без нагрузки.

Сопротивление на входе топлива:

- С чистыми топливными фильтрами: 102 мм рт.ст. \[4 in-Hg\]
- С грязными топливными фильтрами: 203 мм рт.ст. \[8 in-Hg\].

![[06400053.png]]

Если ограничение выше спецификаций:

- Измените топливный фильтр. См. процедуру[[56-006-015-tr — Fuel Filter (Spin-On Type)|006-015]].
- Проверить топливные линии. См. процедуру[[56-006-024-tr — Fuel Supply Lines|006-024]].

![[fp8hoca.png]]

с форсункой электронного управления

1 этап фильтры

Удалите шланг (1) с воздушным кровоточащим клапаном (2).

Удалите проверяющий клапан (2) с воздушным кровотечением из блока сливного коллектора (3).

![[05600265.png]]

Установите тестер топливной системы, номер детали 4918612, вместо контрольного клапана с воздушным кровотечением.

| Тестер топливной системы | 55 Н·м | [41 фунт-фут] |
|---|---|---|

Установите шланг с воздушным кровотечением.

| Кровавая воздушная нора | 45 Н·м | [33 фунт-фут] |
|---|---|---|

![[05600266.png]]

Удалите резьбовую окольную пробку (1) во входе и резьбовую окольную пробку (2) в выходе головки фильтра Стадии 1 и замените их фитингами Compuchek®.

![[05600267.png]]

Подключите вакуумный калибр и адаптер к установке Compuchek® во входном порту (1).

Запуск и работа двигателя при низком холостом режиме, без нагрузки.

Запишите ограничение входа на 1-й этап.

Максимальное ограничение впуска топлива составляет: 102 мм рт.ст. \[4 in-Hg\].

Если ограничение выше спецификаций, проверьте топливные линии. См. руководство по устранению неполадок и ремонту OEM, чтобы определить источник высокого ограничения.

![[05600268.png]]

Удалите вакуумный калибр и адаптер из входного порта и установите его на фитинг Compuchek® в выходном порту (2).

Запуск и работа двигателя при низком холостом режиме, без нагрузки.

![[05600269.png]]

Запишите ограничение выхода 1-й стадии.

Вычтите измерение, полученное на входе стадии 1, из измерения, полученного на выходе стадии 1. Это ограничение 1-й стадии.

Пример:

Ограничение входа 1 стадии составляет 25 мм-Hg \[1 in-Hg\]

Ограничение выхода 1 стадии составляет 113 мм-Hg \[4,5 in-Hg\]

Ограничение 1 стадии составляет 113 мм-Hg \[4.5 in-Hg\] - 25 мм-Hg \[1 in-Hg\] = 88 мм-Hg \[3.5 in-Hg\]

| хг |  | в хг |
|---|---|---|
| 76 | Мин | 3 |
| 152 | Макс | 6 |

Если ограничение выше технических требований, замените топливные фильтры 1-й ступени. См. процедуру[[56-006-015-tr — Fuel Filter (Spin-On Type)|006-015]].

![[14400049.png]]

Удалите вакуумный калибр, адаптер и фитинг Compuchek® из головки установки топливного фильтра 1-го этапа.

![[05600269.png]]

Установите резьбовые окольные вилки входного порта (1) и выходного порта (2) в головке фильтра.

| Ударные кольцевые розетки | 27 Н·м | [20 фунт-фут] |
|---|---|---|

![[05600267.png]]

Удалите шланг с воздушным кровотечением и тестер топливной системы из блока сливного коллектора.

![[05600266.png]]

Установите оригинальный проверочный клапан (2) с воздушным кровотечением в блок сливного коллектора (3).

| Проверка клапана Air Bleed Check | 55 Н·м | [41 фунт-фут] |
|---|---|---|

Установите шланг с воздушным кровотечением на контрольный клапан с воздушным кровотечением.

| Кровавая воздушная нора | 45 Н·м | [33 фунт-фут] |
|---|---|---|

![[05600265.png]]

Фильтры 2-й стадии:

Удалите резьбовую впускную вилку (1) и выходную вилку (2) во впускной части головки фильтра 2-й стадии и замените их фитингами Compuchek®.

![[05600271.png]]

Подключите датчик измерения давления и адаптер к установке Compuchek® во входном порту (1).

Запуск и эксплуатация двигателя на высоком холостом ходу.

Зафиксируйте давление на входе 2-й стадии.

![[05600272.png]]

Удалите датчик и адаптер измерения давления из входного порта и установите датчик измерения давления и адаптер на выходном порту (2).

Запуск и эксплуатация двигателя на высоком холостом ходу.

![[05600273.png]]

Зафиксируйте давление на выходе 2-й стадии.

Вычтите измерение, полученное на выходе 2-й стадии, из измерения, полученного на входе 2-й стадии. Это ограничение фильтра 2-й стадии.

Пример:

Давление на входе 2 стадии составляет 731,5 кПа[104,5 psi]

Давление выхода 2 стадии составляет 714,0 кПа[102,0 psi]

Ограничение 2 стадии составляет 728,0 кПа \[104,5 psi\] - 714,0 кПа \[102,0 psi\] = 17,5 кПа \[2,5 psi\]

| каша |  | пси |
|---|---|---|
| 28 | Макс | 4 |

| каша |  | пси |
|---|---|---|
| 138 | Макс | 20 |

Если ограничение выше технических требований, замените топливные фильтры 2-го этапа. См. процедуру[[56-006-015-tr — Fuel Filter (Spin-On Type)|006-015]].

![[14400049.png]]

Удалите калибр и адаптер давления из головки фильтра 2-й ступени.

![[05600273.png]]

Удалите фитинги Compuchek® из головки фильтра 2-й стадии.

Установите резьбовые кольцевые заглушки во входной (1) и выходной (2) порты в головке фильтра.

Затяните заглушки.

| Ударные кольцевые розетки | 27 Н·м | [20 фунт-фут] |
|---|---|---|

![[05600271.png]]


> [!quote]- Original (English) · английский оригинал
> ### Measure
>
> with Mechanically Actuated Injector
>
> Use a Compuchek® fitting, vacuum gauge, and adapter. Connect the gauge to the Compuchek® fitting on the fuel pump inlet fitting.
>
> Start and operate the engine at high idle, no load.
>
> Fuel inlet restriction:
>
> - With clean fuel filters: 102 mm-Hg \[4 in-Hg\]
> - With dirty fuel filters: 203 mm-Hg \[8 in-Hg\].
>
> If the restriction is above specifications:
>
> - Change the fuel filter. Refer to Procedure [[56-006-015-tr — Fuel Filter (Spin-On Type)|006-015]].
> - Inspect the fuel lines. Refer to Procedure [[56-006-024-tr — Fuel Supply Lines|006-024]].
>
> with Electronically Actuated Injector
>
> Stage 1 Filters
>
> Remove the air bleed hose (1) from the air bleed check valve (2).
>
> Remove the air bleed check valve (2) from the drain manifold block (3).
>
> Install the fuel system tester, Part Number, 4918612, in place of the air bleed check valve.
>
> | Fuel System Tester | 55 n.m | \[41 ft-lb\] |
> |---|---|---|
>
> Install the air bleed hose.
>
> | Air Bleed Hose | 45 n.m | \[33 ft-lb\] |
> |---|---|---|
>
> Remove the threaded o-ring plug (1) in the inlet and the threaded o-ring plug (2) in the outlet of Stage 1 filter head and replace them with Compuchek® fittings.
>
> Connect a vacuum gauge and adapter to the Compuchek® fitting in the inlet port (1).
>
> Start and operate the engine at low idle, no load.
>
> Record the Stage 1 inlet restriction.
>
> The fuel inlet restriction maximum is: 102 mm-Hg \[4 in-Hg\].
>
> If the restriction is above specifications, inspect the fuel lines. Refer to the OEM Troubleshooting and Repair manual to determine the source of the high restriction.
>
> Remove the vacuum gauge and adapter from the inlet port and install it on the Compuchek® fitting in the outlet port (2).
>
> Start and operate the engine at low idle, no load.
>
> Record the Stage 1 outlet restriction.
>
> Subtract the measurement obtained at the Stage 1 inlet from the measurement obtained at the Stage 1 outlet. This is the Stage 1 restriction.
>
> Example:
>
> Stage 1 inlet restriction is 25 mm-Hg \[1 in-Hg\]
>
> Stage 1 outlet restriction is 113 mm-Hg \[4.5 in-Hg\]
>
> Stage 1 restriction is 113 mm-Hg \[4.5 in-Hg\] - 25 mm-Hg \[1 in-Hg\] = 88 mm-Hg \[3.5 in-Hg\]
>
> | mm-hg |  | in-hg |
> |---|---|---|
> | 76 | MIN | 3 |
> | 152 | MAX | 6 |
>
> If the restriction is above specifications, replace the Stage 1 fuel filters. Refer to Procedure [[56-006-015-tr — Fuel Filter (Spin-On Type)|006-015]].
>
> Remove the vacuum gauge, adapter and Compuchek® fittings from the Stage 1 fuel filter head.
>
> Install the threaded o-ring plugs inlet port (1), and outlet port (2) in the filter head.
>
> | Threaded O-ring Plugs | 27 n.m | \[20 ft-lb\] |
> |---|---|---|
>
> Remove the air bleed hose and fuel system tester from the drain manifold block.
>
> Install the original air bleed check valve (2) into the drain manifold block (3).
>
> | Air Bleed Check Valve | 55 n.m | \[41 ft-lb\] |
> |---|---|---|
>
> Install the air bleed hose to the air bleed check valve.
>
> | Air Bleed Hose | 45 n.m | \[33 ft-lb\] |
> |---|---|---|
>
> Stage 2 Filters:
>
> Remove the threaded o-ring inlet plug (1) and outlet plug (2) in the inlet of the Stage 2 filter head and replace them with Compuchek® fittings.
>
> Connect a pressure gauge and adapter to the Compuchek® fitting in the inlet port (1).
>
> Start and operate the engine at high idle.
>
> Record the Stage 2 inlet pressure.
>
> Remove the pressure gauge and adapter from the inlet port and install the pressure gauge and adapter on the outlet port (2).
>
> Start and operate the engine at high idle.
>
> Record the Stage 2 outlet pressure.
>
> Subtract the measurement obtained at the Stage 2 outlet from the measurement obtained at the Stage 2 inlet. This is the Stage 2 filter restriction.
>
> Example:
>
> Stage 2 inlet pressure is 731.5 kPa \[104.5 psi\]
>
> Stage 2 outlet pressure is 714.0 kPa \[102.0 psi\]
>
> Stage 2 restriction is 728.0 kPa \[104.5 psi\] - 714.0 kPa \[102.0 psi\] = 17.5 kPa \[2.5 psi\]
>
> | kpa |  | psi |
> |---|---|---|
> | 28 | MAX | 4 |
>
> | kpa |  | psi |
> |---|---|---|
> | 138 | MAX | 20 |
>
> If the restriction is above specifications, replace the Stage 2 fuel filters. Refer to Procedure [[56-006-015-tr — Fuel Filter (Spin-On Type)|006-015]].
>
> Remove the pressure gauge and adapter from the Stage 2 filter head.
>
> Remove the Compuchek® fittings from the Stage 2 filter head.
>
> Install the threaded o-ring plugs into the inlet (1) and outlet (2) ports in the filter head.
>
> Tighten the plugs.
>
> | Threaded O-ring Plugs | 27 n.m | \[20 ft-lb\] |
> |---|---|---|
