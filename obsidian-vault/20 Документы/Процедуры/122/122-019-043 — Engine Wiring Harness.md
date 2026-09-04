---
aliases:
  - "Жгут проводов двигателя"
type: "Процедура"
doc: "122-019-043"
title_en: "Engine Wiring Harness"
title_ru: "Жгут проводов двигателя"
modified: "2022-07-06"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
  - "QSK60"
  - "QSK60 CM2150 MCRS"
manuals:
  - "4021530"
  - "4022102"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-043.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-043.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "двигатель/QSK60"
  - "двигатель/QSK60CM2150MCRS"
  - "группа/122"
  - "перевод/машинный"
---

# Engine Wiring Harness
**Жгут проводов двигателя**

> [!abstract] Процедура · `122-019-043`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK60 CM2150 MCRS
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]], [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2022-07-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-043.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-043.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Двигатель использует несколько проводных ремней для управления двигателем и некоторыми операциями транспортного средства. Показаны порты модуля управления двигателем (ECM) для следующих разъемов:

- 4-контактный производитель оригинального оборудования (OEM) разъем для электропитания
- Разъем для подключения порта двигателя
- 60-контактный разъём жгута.

![[19803860.png]]

Двигатель имеет две основные ветви электропроводки, основную электропроводку левого берега и главную электропроводку правого берега.

Узел основной проводов левого берега также имеет узел проводов передней удлинитель, узел проводов датчика уровня охлаждающей жидкости двигателя, узел проводов датчика топлива и узел удлинения моторного масла. Связь электропроводки топливного форсунка левого берега и электропроводка температуры выхлопных газов (EGT) также подключаются к основной электропроводке левого берега.

Правобережная форсунка и правобережная удлинительная электропроводка EGT подключаются к основной электропроводке правого берега.

Существует удлинительная проводка, которая соединяет правый берег и основные проводов левого берега в задней части двигателя.

При необходимости электропроводку можно заменить на секциях.

Для конкретного промышленного датчика температуры выхлопных газов QSK60 MCRS (EGTS), форсунки и процедуры монтажной кронштейна см. Инструкцию по установке электропроводки QSK60 (MCRS), Бюллетень 5414606.

![[19600926.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи. См. информацию об услугах производителя оборудования.

![[ck800wa.png]]

### Снятие

Отсоедините проводку двигателя от датчиков и переключателей.

- Датчик скорости/положения коленчатого вала двигателя.
- Датчик скорости/положения вала двигателя.
- Датчик температуры коллектора 1.
- Датчик давления 1 впускного коллектора.
- Датчик температуры коллектора 2.
- Датчик давления 2-го коллектора.
- Датчик температуры коллектора 3.
- Датчик давления 3-го коллектора.
- Датчик температуры 4-го коллектора.
- Датчик давления 4-го коллектора.
- Датчик температуры охлаждающей жидкости двигателя 1.
- Сенсорная проводка уровня охлаждающей жидкости двигателя.
- Датчик давления охлаждающей жидкости.
- Датчик температуры моторного масла 1.
- Датчик давления винты 1.
- Датчик барометрического давления.
- Двигатель сжигает соленоидный клапан.
- Форсунка с датчиком давления 1.
- Датчик давления подачи топлива.
- Датчик температуры топлива двигателя 1.
- Нагнетательный узел топливного насоса.
- - форсунка соленоидный привод (каждый цилиндр).
- Вода в топливном датчике удлинитель проводов.
- Датчик давления в чемодане.
- Датчик температуры выхлопных газов (каждый цилиндр).
- Датчик давления фильтра перед маслом.
- Датчик давления после масляного фильтра.
- Турбокомпрессор 1 датчик скорости.
- Переключатель.
- Воздушный клапан отключения соленоид.

![[19400386.png]]

Обратите внимание на маршрутизацию жгута проводов двигателя и расположение проводных связей и монтажных зажимов, удерживающих жгут проводов двигателя, перед удалением.

Отсоедините разъёмы жгута проводов двигателя от ECM.

![[19600927.png]]

### Проверка при повторном использовании

Замените или отремонтируйте электропроводку двигателя, если есть открытая схема или короткое замыкание, обнаруженное под защитным покрытием корпуса электропроводки.

![[19400386.png]]

### Установка

> [!warning] ОСТОРОЖНО
> Не перегружайте, так как может произойти повреждение разъема.

Подключите жгут электропроводки двигателя к ECM.

Используйте крутящий момент в дюйме, номер детали 3376592, с 4 мм \[5/32 в \] шестиглавый адаптер для затягивания разъема винта.

> [!tip] Момент затяжки
> 2.8 Н·м [25 фунт-дюйм]

Установите зажимы жгута проводов, которые удерживают жгут проводов двигателя на блоке.

![[19600927.png]]

Подключите датчики и переключатели к электропроводке двигателя.

![[19803861.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подсоедините аккумуляторные батареи. См. информацию об услугах производителя оборудования.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The engine uses multiple wiring harnesses to control the engine and some of the vehicle operations. Shown are the engine control module (ECM) ports for the following connectors:
>
> - 4-pin original equipment manufacturer (OEM) power supply harness connector
> - Engine port harness connector
> - 60-pin harness connector.
>
> The engine has two main harness branches, a left bank main harness and a right bank main harness.
>
> The left bank main harness also has a front extension harness, engine coolant level sensor wiring harness, water in fuel sensor extension harness and a lubricating oil extension harness. The left bank injector harness and the exhaust gas temperature (EGT) harness also connects to the left bank main harness.
>
> The right bank injector harness and right bank EGT extension harness connects to the right bank main harness.
>
> There is an extension harness that joins the right bank and left bank main harnesses at the rear of the engine.
>
> The harness can be replaced in sections, if necessary.
>
> For the specific QSK60 MCRS Industrial Exhaust Gas Temperature Sensor (EGTS), Injector and Mounting Bracket procedure, see QSK60 Modular Common Rail System (MCRS) Harness Installation Instruction, Bulletin 5414606.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries. Refer to equipment manufacturer service information.
>
> ### Remove
>
> Disconnect the engine harness from the sensors and switches.
>
> - Engine crankshaft speed/position sensor.
> - Engine camshaft speed/position sensor.
> - Intake manifold 1 temperature sensor.
> - Intake manifold 1 pressure sensor.
> - Intake manifold 2 temperature sensor.
> - Intake manifold 2 pressure sensor.
> - Intake manifold 3 temperature sensor.
> - Intake manifold 3 pressure sensor.
> - Intake manifold 4 temperature sensor.
> - Intake manifold 4 pressure sensor.
> - Engine coolant temperature 1 sensor.
> - Engine coolant level sensor wiring harness.
> - Coolant pressure sensor.
> - Engine oil temperature sensor 1.
> - Engine oil rifle pressure 1 sensor.
> - Barometric pressure sensor.
> - Engine oil burn valve solenoid driver.
> - Injector metering rail 1 pressure sensor.
> - Fuel delivery pressure sensor.
> - Engine fuel temperature sensor 1.
> - Fuel pump pressurizing assembly.
> - Injector solenoid drive (each cylinder).
> - Water in fuel sensor extension wiring harness.
> - Crankcase pressure sensor.
> - Exhaust gas temperature sensor (each cylinder).
> - Pre-oil filter pressure sensor.
> - Post-oil filter pressure sensor.
> - Turbocharger 1 speed sensor.
> - Plunger switch.
> - Air shutoff valve solenoid.
>
> Note the engine harness routing and the location of the wire ties and mounting clips holding the engine harness, before removal.
>
> Disconnect the engine harness connectors from the ECM.
>
> ### Inspect for Reuse
>
> Replace or repair the engine harness if there is an open circuit or a short circuit found under the protective covering of the harness body.
>
> ### Install
>
> **CAUTION · Осторожно**
> Do not overtighten, as connector damage can occur.
>
> Connect the engine harness to the ECM.
>
> Use an inch-pound torque wrench, Part Number 3376592, with 4 mm \[5/32 in\] hex head adapter to tighten the connector jackscrew.
>
> **Момент затяжки · Torque Value**
> 2.8 n•m [25 in-lb]
>
> Install the harness clamps that hold the engine harness to the block.
>
> Connect the sensors and switches to the engine harness.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect the batteries. Refer to equipment manufacturer service information.
