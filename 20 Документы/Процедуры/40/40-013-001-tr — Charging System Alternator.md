---
aliases:
  - "Генератор системы зарядки"
type: "Процедура"
doc: "40-013-001-tr"
title_en: "Charging System Alternator"
title_ru: "Генератор системы зарядки"
modified: "2024-11-11"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 22
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-001-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-001-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Charging System Alternator
**Генератор системы зарядки**

> [!abstract] Процедура · `40-013-001-tr`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2024-11-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-001-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-001-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Из-за количества различных марок и конфигураций генератора, была обобщена следующая процедура для охвата наиболее распространенных конфигураций. Проконсультируйтесь с производителем генератора переменного тока для получения любой информации, которая **не** охвачена этой процедурой.

Типичная система DelcoTM Alternator Wiring

Терминал индикатора (I)

Основная функция терминала индикатора (I) заключается в том, чтобы указать, работает ли генератор переменного тока правильно. Как правило, индикаторный свет подключается к этому терминалу. Если генератор **не** заряжается должным образом, свет включается. Другая функция терминала индикатора (I) заключается в том, что он может использоваться для подачи до 1 ампера выходного сигнала при напряжении системы.

Лампа (L) Терминал

Как и терминал I, терминал L используется для указания правильности работы генератора. Разница между терминалом L и терминалом I заключается в том, что терминал L является током **только **и может **не** использоваться для уменьшения скорости включения.

Терминал реле (R)

Функция реле (R) терминала изменяется. Он может подавать до 4 ампер выходного напряжения при полуноминомном напряжении генератора для питания таких элементов, как тахометр или часовой метр.

Система One-Wire

Это самая простая из систем проводов, потому что провода, подключенные к генератору переменного тока, находятся в аккумуляторе (BAT) и наземных терминалах. (См. таблицу 5.) Подключение к терминалу R, терминалу L и терминалу I является необязательным.

Трехпроводная система

Эта система требует больше проводов, потому что она имеет терминал батареи (BAT), R-терминал, два лезвия, идентифицированные как числа 1 и 2, и наземный терминал. Как правило, в трехпроводной системе терминал с лезвием номер 1 служит терминалом I. (См. таблицу 5.) Преимущество трехпроводной системы заключается в том, что она обеспечивает те же функции, что и однопроводная система, плюс удаленное чувство. Подключая клеммный терминал с числом 2 к положительному (+) клемму батареи, напряжение одновременно ощущается и регулируется в батарее, а не в генераторе переменного тока. Это исключает возможность потери напряжения в проводах от генератора к батарее.

![[13900200.png]]

Одна беспроводная система, типичный альтернативатор (Delco-RemyTM) с комбинированным коннектором Metri-PackTM

| Одна беспроводная система, типичный альтернативатор (Delco-RemyTM) с комбинированным коннектором Metri-PackTM |  |  |  |
|---|---|---|---|
| 1 | ГРД* | земля |  |
| 4 | R* | Индикатор зарядки, автоматическая система блокировки, тахометр |  |
| 5 | НИМ | батарея |  |
| 7 | L | Ламповый терминал |  |

 Не все генераторы имеют эту функцию.

\*\* Предоставляет импульсы напряжения при примерно половине системного напряжения на частоте одной десятой оборотов генератора.

![[13900134.png]]

Одна беспроводная система, типичный альтернативатор (Delco-RemyTM)

| Одна беспроводная система, типичный альтернативатор (Delco-RemyTM) |  |  |
|---|---|---|
| 3 | ГРД* | земля |
| 4 | R* | Индикатор зарядки, автоматическая система блокировки, тахометр |
| 5 | НИМ | батарея |
| 6 | Я* | Световой индикатор |

 Не все генераторы имеют эту функцию.

\*\* Предоставляет импульсы напряжения при примерно половине напряжения системы на частоте одной десятой оборота генератора переменного тока.

![[13900135.png]]

Трехпроводная система, типичный альтернативатор (Delco-RemyTM)

| Трехпроводная система, типичный альтернативатор (Delco-RemyTM) |  |  |
|---|---|---|
| Ключ | Терминал | Подключен к |
| 1 | Лезвие № 1* | Световой индикатор |
| 2 | Лезвие номер 2. | Напряжение чувств |
| 3 | ГРД* | земля |
| 4 | R* | Индикатор зарядки, автоматическая система блокировки, тахометр |
| 5 | НИМ | батарея |
| 6 | Я* | Световой индикатор |

 Не все генераторы имеют эту функцию.

\*\* Предоставляет импульсы напряжения при примерно половине системного напряжения на частоте одной десятой оборотов генератора.

![[13900133.png]]

Таблица 6, Типичный Альтернативатор (BoschTM K1)

| Типичная система проводов BoschTM K1 |  |  |
|---|---|---|
| Ключ | Терминал | Подключенный к |
| 1 | D+ | Электрическая система зарядки Status Light |
| 2 | B++ | Положительная батарея |
| 3 | Вау | Тахометр |
| 4 | — | Земля/сборка |

### Первичная проверка

Проверьте приводной ремень и шкив генератора, чтобы убедиться, что генератор вращается должным образом.

Если есть какие-либо проблемы, проверьте следующее:

1. Если приводной ремень проскальзывает на шкиве генератора, используйте следующую процедуру для проверки приводного ремня.[[40-008-002-tr — Drive Belt, Cooling Fan|См. процедуру 008-002 в разделе 8.]]Используйте следующую процедуру, чтобы засечь натяжитель ремня.[[40-008-087-tr — Cooling Fan Belt Tensioner|См. процедуру 008-087 в разделе 8.]]
2. Снимите жгут проводов.[[40-008-002-tr — Drive Belt, Cooling Fan|См. процедуру 008-002 в разделе 8.]]. Проверьте, не выключен ли шкив генератора на валу. Если вырваться, удалите шкив и проверьте на повреждение.[[40-013-006-tr — Alternator Pulley|См. процедуру 013-006 в разделе 13.]]
3. Если генератор переменного тока **не** вращается или делает **не** свободно вращающийся, то генератор переменного тока должен быть заменен. См. разделы Удалить и установить этой процедуры.

![[13d00028.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

Проверьте аккумулятор и все проводные соединения.

Проверьте проводку на наличие дефектов.

Проверьте все соединения на герметичность и чистоту, включая разъёмы скольжения на переборке генератора и моторного отделения, а также соединения на батарее.

![[13d00008.png]]

### Проверка

> [!note] Примечание
> Любое многометровое считывание нулевого напряжения указывает на открытую цепь.

Проверьте открытые цепи.

Переведите замок зажигания в положение ON.

Подключите мультиметр, Cummins® Part Number 3164488 или 3164489, к следующим местам:

Альтернативные делько

1. Терминал «BAT» переключается на землю
2. Терминал лезвия альтернатора «Номер 1» на землю
3. Терминал лезвия альтернатора «Номер 2» на землю.

Найдите и отремонтируйте открытый контур.

![[es900kz.png]]

Подключите углеродный заряд (батарею / тестер-альтернатор) через батареи в одном из аккумуляторных ящиков.

Закрепите ампер-часовой счетчик индукционного типа вокруг кабеля батареи; или используйте цифровой мультиметр, Часть Номер 3164488 или 3164489, с зажимным датчиком тока, Часть Номер 3164490.

![[ea8tohc.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!danger] ОПАСНО
> Кислота чрезвычайно опасна и может повредить оборудование, а также вызвать серьезные ожоги. Всегда предоставляйте резервуар с сильной содовой в качестве нейтрализующего агента при обслуживании батарей. Носите очки и защитную одежду, чтобы уменьшить вероятность серьезных травм.

Отключите любые кабели, которые ведут к любым другим аккумуляторным коробкам в цепи, сначала отрицательные (-) кабели.

Работайте с двигателем на высоком холостом ходу и измеряйте выходное напряжение генератора на батареи с цифровым мультиметром, Номер детали 3164488 или 3164489. См. сервисное руководство изготовителя машины.

![[ea800kc.png]]

Управляйте двигателем на высоком холостом ходу и регулируйте оборудование для испытания нагрузки на углекислоту, чтобы применить максимальную номинальную нагрузку на генератор. См. сервисное руководство изготовителя машины.

> [!note] Примечание
> Максимальный выходной коэффициент ампеража генератора обычно маркируется или маркируется на генераторе.

Измерить выходной коэффициент тока генератора. См. сервисное руководство изготовителя машины.

Если выходной сигнал генератора (ампер) **не** в пределах 10 процентов от номинального значения, отремонтируйте или замените генератор. См. руководство по обслуживанию OEM для процедур ремонта.

![[ea800kd.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

> [!danger] ОПАСНО
> Кислота чрезвычайно опасна и может повредить оборудование, а также вызвать серьезные ожоги. Всегда предоставляйте резервуар с сильной содовой в качестве нейтрализующего агента при обслуживании батарей. Носите очки и защитную одежду, чтобы уменьшить вероятность серьезных травм.

Выключите двигатель и удалите испытательное оборудование.

Подключите все кабели аккумулятора, отрицательный (-) кабель последний.

![[ea8toma.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!danger] ОПАСНО
> Кислота чрезвычайно опасна и может повредить оборудование, а также вызвать серьезные ожоги. Всегда предоставляйте резервуар с сильной содовой в качестве нейтрализующего агента при обслуживании батарей. Носите очки и защитную одежду, чтобы уменьшить вероятность серьезных травм.

- Отсоедините аккумуляторные батареи.

![[13900050.png]]

- Снимите приводной ремень с шкива генератора.[[40-008-002-tr — Drive Belt, Cooling Fan|См. процедуру 008-002 в разделе 8.]].
- Пометьте и пометьте все провода на генераторе.
- Отключите провода.

![[ck800wa.png]]

### Снятие

Гора Спул.

Удалите болты верхнего генератора.

Удалите крепежные болты и гайку в нижней части крепежных кронштейнов генератора и генератора.

Удалите генератор.

![[13d00057.png]]

Гора Хингэ

Удалите болты связи генератора.

![[13d00019.png]]

Удалите крепежные болты генератора.

Удалите генератор.

![[13d00020.png]]

### Установка

Гора Спул

Установите генератор переменного тока и нижние крепежные болты и гайку генератора переменного тока.

Установите верхние болты крепления линии генератора в верхней части генератора.

Затяните болты.

Момент затяжки:

Нижние монтажные болты

Момент затяжки:

Верхний линковый болт

![[13d00057.png]]

Гора Хингэ

Установите генератор.

Установите и затяните крепежные болты генератора.

> [!tip] Момент затяжки
> 40 Н·м [30 фунт-фут]

![[13d00020.png]]

Установите болты линии генератора.

> [!tip] Момент затяжки
> 24 Н·м [212 фунт-дюйм]

![[13d00019.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

> [!danger] ОПАСНО
> Кислота чрезвычайно опасна и может повредить оборудование, а также вызвать серьезные ожоги. Всегда предоставляйте резервуар с сильной содовой в качестве нейтрализующего агента при обслуживании батарей. Носите очки и защитную одежду, чтобы уменьшить вероятность серьезных травм.

Альтернативный Delco-Remy

- Подключите все провода к генератору.
- Установите приводной ремень. См. процедуру 008-002 в разделе 8.

![[ck800wa.png]]

Bosch K1 Alternator

- Подключите все провода к генератору.

> [!tip] Момент затяжки
> 2.7 - 9.8 Н·м [23.9 - 86.7 фунт-дюйм]

> [!tip] Момент затяжки
> 7.5-8.0 Н·м [66.4-70.8 фунт-дюйм]

- Установите приводной ремень. См. процедуру 008-002 в разделе 8.

![[nobox.png]]

- Подсоедините аккумуляторные батареи.
- Запустите двигатель и проверьте правильность работы.

![[13900050.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Due to the number of different alternator brands and configurations, the following procedure has been generalized to cover the most common configurations. Consult the alternator manufacturer for any information that is **not** covered in this procedure.
>
> Typical Delco™ Alternator Wiring System
>
> Indicator (I) Terminal
>
> The main function of the indicator (I) terminal is to indicate if the alternator is working correctly. Typically, an indicator light is wired to this terminal. If the alternator is **not** charging properly, the light turns on. Another function of the indicator (I) terminal is that it can be used to supply up to 1 ampere of output at system voltage.
>
> Lamp (L) Terminal
>
> Similar to the I terminal, the L terminal is used to indicate if the alternator is working correctly. The difference between the L terminal and the I terminal is that the L terminal is a current sink **only** and can **not** be used to reduce turn on speed.
>
> Relay (R) Terminal
>
> The function of the relay (R) terminal varies. It can supply up to 4 amperes of output at one-half nominal alternator voltage to power items such as a tachometer or an hour meter.
>
> One-Wire System
>
> This is the simplest of the wiring systems because the **only** wires connected to the alternator are at the battery (BAT) and ground terminals. (See Table 5.) Connecting to the R terminal, L terminal, and I terminal is optional.
>
> Three-Wire System
>
> This system requires more wiring because it has a battery (BAT) terminal, R terminal, two blade terminals identified as number 1 and number 2, and a ground terminal. Typically, in the three-wire system, the number 1 blade terminal serves as the I terminal. (See Table 5.) The advantage of the three-wire system is that it provides the same features as the one-wire system, plus remote sense. By connecting the number 2 blade terminal to the battery's positive (+) terminal, the voltage is both sensed and regulated at the battery, instead of at the alternator. This eliminates the potential for voltage losses in the wiring from the alternator to the battery.
>
> One Wire System, Typical Alternator (Delco-Remy™) with Combined Metri-Pack™ Connector
>
> | One Wire System, Typical Alternator (Delco-Remy™) with Combined Metri-Pack™ Connector |  |  |  |
> |---|---|---|---|
> | 1 | GRD\* | Ground |  |
> | 4 | R\* | Charge indicator, automatic lockout system, tachometer\*\* |  |
> | 5 | BAT | Battery |  |
> | 7 | L | Lamp Terminal |  |
>
> \* **Not** all alternators have this feature.
>
> \*\*Provides voltage pulses at about one-half system voltage at a frequency of one-tenth of generator rpm.
>
> One Wire System, Typical Alternator (Delco-Remy™)
>
> | One Wire System, Typical Alternator (Delco-Remy™) |  |  |
> |---|---|---|
> | 3 | GRD\* | Ground |
> | 4 | R\* | Charge indicator, automatic lockout system, tachometer\*\* |
> | 5 | BAT | Battery |
> | 6 | I\* | Indicator light |
>
> \* **Not** all alternators have this feature.
>
> \*\*Provides voltage pulses at about one-half system voltage at a frequency of one-tenth of alternator rpm.
>
> Three Wire System, Typical Alternator (Delco-Remy™)
>
> | Three Wire System, Typical Alternator (Delco-Remy™) |  |  |
> |---|---|---|
> | Key | Terminal | Connected To |
> | 1 | Blade number 1\* | Indicator light |
> | 2 | Blade number 2 | Voltage sense |
> | 3 | GRD\* | Ground |
> | 4 | R\* | Charge indicator, automatic lockout system, tachometer\*\* |
> | 5 | BAT | Battery |
> | 6 | I\* | Indicator light |
>
> \* **Not** all alternators have this feature.
>
> \*\*Provides voltage pulses at about one-half system voltage at a frequency of one-tenth of generator rpm.
>
> Table 6, Typical Alternator (Bosch™ K1)
>
> | Typical Bosch™ K1 Wiring System |  |  |
> |---|---|---|
> | Key | Terminal | Connected to |
> | 1 | D+ | Electrical charging system status light |
> | 2 | B+ | Positive battery |
> | 3 | W | Tachometer |
> | 4 | — | Ground/assembly |
>
> ### Initial Check
>
> Check the drive belt and alternator pulley to be sure the alternator is rotating properly.
>
> If any problems exist, check the following:
>
> 1. If the drive belt is slipping on the alternator pulley, use the following procedure to inspect the drive belt. [[40-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8.]] Use the following procedure to inpect the belt tensioner. [[40-008-087-tr — Cooling Fan Belt Tensioner|Refer to Procedure 008-087 in Section 8.]]
> 2. Remove the drive belt. [[40-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8]]. Check if the alternator pulley is loose on the shaft. If loose, remove the pulley and inspect for damage. [[40-013-006-tr — Alternator Pulley|Refer to Procedure 013-006 in Section 13.]]
> 3. If the alternator will **not** rotate or does **not** rotate freely, the alternator **must** be replaced. See the Remove and Install sections of this procedure.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Check the battery and all wiring connections.
>
> Inspect the wiring for defects.
>
> Check all connections for tightness and cleanliness, including the slip connectors at the alternator and engine compartment bulkhead, and the connections at the battery.
>
> ### Test
>
> **Note · Примечание**
> Any multimeter reading of zero voltage indicates an open circuit.
>
> Check for open circuits.
>
> Turn the keyswitch to the ON position.
>
> Connect a multimeter, Cummins® Part Number 3164488 or 3164489, to the following locations:
>
> Delco™ Alternators
>
> 1. Alternator “BAT” terminal to ground
> 2. Alternator blade terminal “Number 1” to ground
> 3. Alternator blade terminal “Number 2” to ground.
>
> Locate and repair the open circuit.
>
> Connect a carbon-pile load (battery/alternator tester) across the batteries in one of the battery boxes.
>
> Clamp an induction pickup-type ampere-hour meter around the battery cable; or use the digital multimeter, Part Number 3164488 or 3164489, with the clamp-on current probe, Part Number 3164490.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **WARNING · Опасно**
> Acid is extremely dangerous and can damage the machinery and can also cause serious burns. Always provide a tank of strong soda water as a neutralizing agent when servicing the batteries. Wear goggles and protective clothing to reduce the possibility of serious personal injury.
>
> Disconnect any cables that lead to any other battery boxes in the circuit, negative (-) cables first.
>
> Operate the engine at high idle; and measure the alternator voltage output to the batteries with digital multimeter, Part Number 3164488 or 3164489. Refer to the OEM service manual.
>
> Operate the engine at high idle and adjust the carbon-pile load-testing equipment to apply the maximum rated amperage load to the alternator. Refer to the OEM service manual.
>
> **Note · Примечание**
> The alternator maximum rated amperage output is normally stamped or labeled on the alternator.
>
> Measure the alternator amperage output. Refer to the OEM service manual.
>
> If the alternator output (amps) is **not** within 10 percent of rated output, repair or replace the alternator. Refer to the OEM service manual for repair procedures.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **WARNING · Опасно**
> Acid is extremely dangerous and can damage the machinery and can also cause serious burns. Always provide a tank of strong soda water as a neutralizing agent when servicing the batteries. Wear goggles and protective clothing to reduce the possibility of serious personal injury.
>
> Shut off the engine and remove the test equipment.
>
> Connect all battery cables, negative (-) cable last.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **WARNING · Опасно**
> Acid is extremely dangerous and can damage the machinery and can also cause serious burns. Always provide a tank of strong soda water as a neutralizing agent when servicing the batteries. Wear goggles and protective clothing to reduce the possibility of serious personal injury.
>
> - Disconnect the batteries.
>
> - Remove the drive belt from the alternator pulley. [[40-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8.]].
> - Tag and label all wires on the alternator.
> - Disconnect the wires.
>
> ### Remove
>
> Spool Mount.
>
> Remove the upper alternator link capscrew.
>
> Remove the mounting capscrew and nut at the bottom of the alternator and alternator mounting bracket.
>
> Remove the alternator.
>
> Hinge Mount
>
> Remove the alternator link capscrew.
>
> Remove the alternator mounting capscrew.
>
> Remove the alternator.
>
> ### Install
>
> Spool Mount
>
> Install the alternator and the bottom alternator mounting capscrew and nut.
>
> Install the upper alternator link mounting capscrew at the top of the alternator.
>
> Tighten the capscrews.
>
> Torque Value:
>
> Lower Mounting Capscrew
>
> Torque Value:
>
> Upper Link Mounting Capscrew
>
> Hinge Mount
>
> Install the alternator.
>
> Install and tighten the alternator mounting capscrew.
>
> **Момент затяжки · Torque Value**
> 40 n•m [30 ft-lb]
>
> Install the alternator link capscrew.
>
> **Момент затяжки · Torque Value**
> 24 n•m [212 in-lb]
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **WARNING · Опасно**
> Acid is extremely dangerous and can damage the machinery and can also cause serious burns. Always provide a tank of strong soda water as a neutralizing agent when servicing the batteries. Wear goggles and protective clothing to reduce the possibility of serious personal injury.
>
> Delco-Remy™ Alternator
>
> - Connect all wires to the alternator.
> - Install the drive belt. Refer to Procedure 008-002 in Section 8.
>
> Bosch™ K1 Alternator
>
> - Connect all wires to the alternator.
>
> **Момент затяжки · Torque Value**
> 2.7 to 9.8 n•m [23.9 to 86.7 in-lb]
>
> **Момент затяжки · Torque Value**
> 7.5 to 8.0 n•m [66.4 to 70.8 in-lb]
>
> - Install the drive belt. Refer to Procedure 008-002 in Section 8.
>
> - Connect the batteries.
> - Start the engine and check for correct operation.
