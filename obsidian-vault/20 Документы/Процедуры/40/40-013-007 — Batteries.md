---
aliases:
  - "Аккумуляторные батареи"
type: "Процедура"
doc: "40-013-007"
title_en: "Batteries"
title_ru: "Аккумуляторные батареи"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 13
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Batteries
**Аккумуляторные батареи**

> [!abstract] Процедура · `40-013-007`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-007.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

> [!danger] ОПАСНО
> Кислота чрезвычайно опасна и может повредить оборудование, а также вызвать серьезные ожоги. Всегда предоставляйте бак с сильной содовой в качестве нейтрализующего агента при обслуживании батарей. Носите очки и защитную одежду, чтобы избежать серьезных телесных повреждений.

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Наклейте этикетку и отсоедините все кабели аккумулятора.

![[13800025.png]]

Чистая коррозия и мусор от аккумуляторов и терминалов.

![[ea8coea.png]]

> [!note] Примечание
> Аккумуляторы без технического обслуживания герметичны и не требуют добавления воды.

Если используются обычные батареи, удалите крышки или крышки ячеек и проверьте уровень электролита.

> [!note] Примечание
> Если вода добавляется в аккумулятор, она должна быть заряжена до того, как будет проведено какое-либо тестирование.

Заполните каждый аккумулятор дистиллированной водой. Смотрите спецификации производителя аккумуляторов.

![[ea800sa.png]]

Проверьте «Глаз» на аккумуляторе без обслуживания. См. спецификации OEM.

![[13800022.png]]

Удалите поверхностный заряд, прикрепив батарею к 300-амперной нагрузке в течение 30 секунд для тяжелых батарей.

![[13800019.png]]

Снимите нагрузку и подождите 1 минуту; если напряжение батареи больше или равно 12,4 ВДК, продолжайте тестирование. Если напряжение ниже 12,4 ВДК, перезарядите или замените батарею.

![[13800023.png]]

Испытание на нагрузку батарей на 1/2 от холодного коленчатого усилителя (рейтинг при -18 ° C \[0°F \] в течение 15 секунд).

![[13800019.png]]

Проверьте напряжение батареи и сравните с таблицей:

| Температура и отношение напряжения |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| Темп (F) | 70 | 60 | 50 | 40 | 30 | 20 | 10 | 0 |
| Темп (C) | 21 | 16 | 10 | 4 | -1 | -7 | -12 | -18 |
| Мин. VDC | 9.6 | 9.5 | 9.4 | 9.3 | 9.1 | 8.9 | 8.7 | 8.5 |

Выключи груз.

Замените батарею, если она не соответствует вышеуказанным спецификациям.

![[13800024.png]]

Используйте рефрактометр Fleetguard®, номер детали CC-2800, для проверки удельной гравитации электролита батареи.

Смотрите колонку жидкости батареи в рефрактометре, чтобы определить состояние заряда каждого элемента батареи.

Если вода была добавлена в сухую ячейку, перезарядите батарею, чтобы смешать добавленную воду с существующим электролитом батареи, чтобы предотвратить неправильные показания.

![[ra8todb.png]]

> [!warning] ОСТОРОЖНО
> Не подключайте кабели зарядки аккумулятора к любой части электронной системы управления. Это может повредить части электронной системы управления.

Используйте системный анализатор/испытатель батареи, номер детали 3377193, для проверки выходного тока аккумуляторов без обслуживания или обычных вентиляционных колпачков.

Если выходная мощность низкая, используйте зарядное устройство для зарядки батареи. См. указания изготовителя.

Замените батарею, если она будет **не** заряжаться в соответствии со спецификациями производителя или **не** поддерживать заряд.

См. прилагаемую таблицу для определения состояния заряда батареи на основе показаний с удельной гравитацией.

| Состояние зарядки аккумулятора | Специфическая гравитация @ 27°C \[80°F\] |
|---|---|
| 100% | 1.260 - 1.280 |
| 75% | 1.230 - 1.250 |
| 50% | 1.200 - 1.220 |

![[ea800kb.png]]

Все батареи, включая батареи без обслуживания, можно проверить, измерив напряжение между кабелем положительной (+) батареи и заземлением блока двигателя (-). Заметьте напряжение.

![[ea900sa.png]]

Используя удаленное стартовое соединение, попробуйте включить стартер при наблюдении напряжения.

Если напряжение считывает менее 10 VDC, заряжайте батарею.

Если напряжение падает быстрее, чем 2 ВДК, замените аккумулятор.

![[ea900wa.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Подключите все кабели аккумулятора.

![[13800025.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> **WARNING · Опасно**
> Acid is extremely dangerous and can damage the machinery and can also cause serious burns. Always provide a tank of strong soda water as a neutralizing agent when servicing batteries. Wear goggles and protective clothing to avoid serious bodily injury.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Label and disconnect all battery cables.
>
> Clean corrosion and debris from battery and terminals.
>
> **Note · Примечание**
> Maintenance-free batteries are sealed and do **not** require the addition of water.
>
> If conventional batteries are used, remove the cell caps or covers, and check the electrolyte level.
>
> **Note · Примечание**
> If water is added to the battery it **must** be charged before any testing can be accomplished.
>
> Fill each battery cell with distilled water. Refer to the battery manufacturer's specifications.
>
> Check the “Eye” on the maintenance-free battery. Refer to the OEM specifications.
>
> Remove the surface charge by attaching the battery to a 300-amp load for 30 seconds for heavy-duty batteries.
>
> Remove the load, and wait 1 minute; if the battery voltage is greater than or equal to 12.4 VDC, continue testing. If the voltage is below 12.4 VDC, recharge or replace the battery.
>
> Load-test the batteries at 1/2 of the cold cranking amp rating of the battery (rating at -18°C \[0°F\] for 15 seconds).
>
> Check the battery voltage, and compare to the table:
>
> | Temperature and Voltage Relationship |  |  |  |  |  |  |  |  |
> |---|---|---|---|---|---|---|---|---|
> | Temp (F) | 70 | 60 | 50 | 40 | 30 | 20 | 10 | 0 |
> | Temp (C) | 21 | 16 | 10 | 4 | -1 | -7 | -12 | -18 |
> | Min. VDC | 9.6 | 9.5 | 9.4 | 9.3 | 9.1 | 8.9 | 8.7 | 8.5 |
>
> Turn the load off.
>
> Replace the battery if it does **not** meet the above specifications.
>
> Use the Fleetguard® Refractometer, Part Number CC-2800, to check the specific gravity of the battery electrolyte.
>
> Refer to the battery fluid column in the refractometer to determine the state of charge of each battery cell.
>
> If water has been added to a dry cell, recharge the battery to mix the added water with the existing battery electrolyte to prevent incorrect readings.
>
> **CAUTION · Осторожно**
> Do not connect battery charging cables to any electronic control system part. This can damage the electronic control system parts.
>
> Use the systems analyzer/battery tester, Part Number 3377193, to test the output amperage of maintenance-free or conventional vent-cap batteries.
>
> If the output amperage is low, use a battery charger to charge the battery. Refer to the manufacturer's instructions.
>
> Replace the battery if it will **not** charge to the manufacturer's specifications or will **not** maintain a charge.
>
> Refer to the accompanying table to determine the battery state of charge based on the specific-gravity readings.
>
> | Battery State of Charge | Specific Gravity @ 27°C \[80°F\] |
> |---|---|
> | 100% | 1.260 to 1.280 |
> | 75% | 1.230 to 1.250 |
> | 50% | 1.200 to 1.220 |
>
> All batteries, including maintenance-free ones, can be checked by measuring the voltage between the positive (+) battery cable and the engine block ground (-). Note the voltage.
>
> Using a remote start connection, attempt to engage the starter while observing the voltage.
>
> If the voltage reads less than 10 VDC, charge the battery.
>
> If the voltage drops rapidly more than 2 VDC, replace the battery.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Connect all battery cables.
