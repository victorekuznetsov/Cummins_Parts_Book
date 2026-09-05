---
type: "Процедура"
doc: "40-010-072"
title_en: "Air Intake Manifold Heater"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 23
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-010-072.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-010-072.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Air Intake Manifold Heater

> [!abstract] Процедура · `40-010-072`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-010-072.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-010-072.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Эта процедура охватывает компоненты элементов впускного коллектора для автомобильных и промышленных двигателей в 1991 и 1994 годах. Эта процедура также охватывает дооснащение компонентов элементов впускного коллектора на двигателях **не**, первоначально построенных с возможностью впускного нагревателя (только передние двигатели редуктора).

> [!danger] ОПАСНО
> Чтобы уменьшить вероятность получения травм и повреждения имущества, никогда не используйте стартовую жидкость с воздухозаборником коллектора. Запуск жидкости, которая содержит эфир, может вызвать взрыв.

> [!danger] ОПАСНО
> Стартовая жидкость очень легковоспламеняющаяся и взрывоопасная. Держите пламя, искры и дуговые выключатели подальше от стартовой жидкости. Такое сочетание может вызвать взрыв и телесные повреждения.

Предупреждающие надписи, номер детали 3927335, должны быть установлены в местах, очевидных для оператора, вблизи наиболее вероятной точки входа эфира и на видимой стороне нагревателя. Солнцезащитный козырек и воздухоочиститель - два примера.

12-VDC B Series заряжают воздушные охлажденные, турбированные и естественно-аспирированные двигатели (6BTAA, 6BT и 6B) и используют воздухозаборный коллектор в качестве стартового средства для холодной погоды. В настоящее время нет впускного коллектора для водяного куртка после охлаждения двигателя (6BTA) или 24-VDC электрической системы, и воздухозаборный коллектор нагреватель не совместим с морскими применениями.

Преимущества от воздухозаборника коллектора нагревателя включают в себя:

- Быстрое время начала
- Двигатель, работающий после запуска
- Заменить эфир в качестве стартовой помощи
- Продлевает стартер и срок службы батареи за счет меньшего количества проворачиваний.

Водозаборный коллектор очень похож на популярный электронагреватель для грузовых автомобилей малой грузоподъемности, используемый с 1988 года. Этот нагреватель в электронном виде управляет двумя нагревательными элементами для оптимизации холодных запусков и улучшения работы холодного двигателя.

Аппаратное обеспечение, установленное на двигателе, включает:

- Водоприемный коллектор
- Датчик температуры
- Контроллер
- Жгут проводов.

> [!note] Примечание
> В комплекте **не** 6 проводных или кольцевых терминалов AWG, необходимых для аккумулятора и других соединений.

Белый дым указывает на несгоревшее топливо во время работы холодного двигателя.

Система впускного коллектора нагревателя **не** напрямую подключена к топливной системе, но она контролирует температуру воздуха к двигателю. Термистор посылает различные значения сопротивления электронному модулю управления (ECM) или эквиваленту. ECM, в свою очередь, управляет лампой WAIT-TO-START и соленоидами нагревателя.

Элементы впускного коллектора работают как в режиме предварительного нагрева, так и в режиме после нагрева.

- В предварительном нагреве включен переключатель зажигания, но двигатель **не** запущен.
- В посттепловом режиме двигатель работает.

Правильная работа системы впускного коллектора и процедуры запуска исключат чрезмерное использование стартера двигателя и минимизируют белый дым выхлопа при первом запуске двигателя.

| Нормальная работа системы нагревателя впускного коллектора |  |  |  |  |
|---|---|---|---|---|
| температура | Состояние | Элементы | Продолжительность | Процентный цикл ON/OFF |
| Ниже -19°C \[-2°F\] | Подогревать | Оба | 30 секунд | непрерывный |
|  | Посттепло | Оба | 15 секунд | непрерывный |
|  |  | Один | 15 секунд | непрерывный |
|  |  | Один | 40 секунд | 50/50 |
|  |  | Один | 106 секунд | 25/75 |
| -19 -8°C \[-2 - 18°F\] | Подогревать | Оба | 20 секунд | непрерывный |
|  | Посттепло | Оба | 20 секунд | непрерывный |
|  |  | Один | 20 секунд | непрерывный |
|  |  | Один | 20 секунд | непрерывный |
|  |  | Один | 40 секунд | 50/50 |
|  |  | Один | 106 секунд | 25/75 |
| -8-8°C[18-46°F] | Подогревать | Оба | 10 секунд | непрерывный |
|  | Посттепло | Оба | 10 секунд | непрерывный |
|  |  | Один | 10 секунд | непрерывный |
|  |  | Один | 10 секунд | непрерывный |
|  |  | Один | 40 секунд | 50/50 |
|  |  | Один | 106 секунд | 25/75 |
| Ниже 8°C[46°F] | Подогревать | Нет |  |  |
|  | Посттепло | Нет |  |  |
| Амперационный чертеж - 95 ампер на элемент |  |  |  |  |
| Чтобы предотвратить чрезмерный сток на батареях, контроллер электрического нагревателя включил функцию мониторинга батареи. Если аккумулятор VDC был сброшен слишком низко, контроллер нагревателя задержит цикл после нагрева, предотвращая дальнейшее слив на аккумуляторах. Эта функция защиты от аккумуляторов активируется только на транспортных средствах со слабыми или осушенными батареями. |  |  |  |  |

* Модули управления нагревателем или электронные модули управления с серийными номерами ниже 0080000A будут **не **иметь цикл предварительного нагрева в течение этого цикла.

Требования к размеру батареи для двигателей серии B (автомобильные и промышленные рейтинги)

1991 и 1994 6BTAA и 4BTAA автомобильные рейтинги

> [!note] Примечание
> Необходимый старт до 0°C \[+32°F\] или оборудование для впускного нагревателя

| 4BTAA двигатель |  |  |
|---|---|---|
| Тяжелый аксессуар | Cold Cranking Amps (CCA) | Резервные минуты |
| Световой аксессуар | 900 | 160 |
|  | 750 | 169 |
| Для установки оборудования для нагрева требуется генератор переменного тока 95 ампер или больше. |  |  |

| 6BTAA двигатель |  |  |
|---|---|---|
|  | Cold Cranking Amps (CCA) | Резервные минуты |
| Тяжелые аксессуары | 1000 | 160 |
| Световые аксессуары | 850 | 160 |
| Для установки оборудования для нагрева требуется генератор переменного тока 95 ампер или больше. |  |  |

> [!note] Примечание
> Неудавшийся старт до -12°C[10°F].

| 4BTAA двигатель |  |  |
|---|---|---|
|  | Cold Cranking Amps (CCA) | Резервные минуты |
| Тяжелые аксессуары | 1350 | 320 |
| Световые аксессуары | 1125 | 320 |

| 6BTAA двигатель |  |  |
|---|---|---|
|  | Cold Cranking Amps (CCA) | Резервные минуты |
| Тяжелые аксессуары | 1500 | 320 |
| Световые аксессуары | 1250 | 320 |

1994 6BTAA и 4BTAA промышленные рейтинги

| 4BTAA двигатель |  |  |
|---|---|---|
|  | Cold Cranking Amps (CCA) | Резервные минуты |
| Тяжелые аксессуары | 800 | 160 |
| Световые аксессуары | 625 | 160 |

| 6BTAA двигатель |  |  |
|---|---|---|
|  | Cold Cranking Amps (CCA) | Резервные минуты |
| Тяжелые аксессуары | 950 | 160 |
| Световые аксессуары | 800 | 160 |

> [!note] Примечание
> Типичные «легкие аксессуары» включают в себя генератор переменного тока, небольшой рулевой насос и отключенное сцепление.

> [!note] Примечание
> Типичные «тяжелые аксессуары» включают гидравлический насос и крутящий момент.

![[10900270.png]]

Диаграмма межсоединения контроллера воздушного впуска

![[10900271.png]]

Холодная система запуска

1. Сетчатый нагреватель
2. Датчик температуры воздуха

На следующей иллюстрации показаны компоненты нагревателя сетки.

Компоненты нагревателя сетки

1. Наземное соединение
2. Для WAIT-TO-START лампы (застегнутые)
3. Наземное соединение
4. Для плавления и аккумулятора
5. Наземное соединение

![[10900272.png]]

| Устранение неполадок в системе отопления |  |
|---|---|
| Ждать-начать (WTS) Лампа **Не** Функционирование | Проверьте проводку, розетку, лампочку, сигнал от контроллера и источник питания лампы от переключателя зажигания. Исправьте любые электрические проблемы с лампой WTS. Лампа WTS будет мигать один раз в секунду, если в датчике температуры будет обнаружена открытая схема. |
| Температурный датчик не работает | Проверяйте сопротивление через штифты датчика температуры J1A и J1B при комнатной температуре и в ледяной ванне 0°C \[32°F\]. Сопротивление должно составлять около 800 Ом при комнатной температуре и 2000 Ом для ледяной ванны. Проверьте сопротивление к земле (-) для открытой цепи. |
|  | Примечание: Проверяйте сопротивление с помощью переключателя зажигания в положении Включения, чтобы убедиться, что нет проблем с заземлением (-). |
|  | Заменить дефектный датчик. |
| Сбой реле или контактора | Проверьте реле или контакторы для звукового щелчка во время работы. Проверьте наличие проколов или горения в реле путем измерения сопротивления через терминалы с высоким уровнем расхода топлива, когда реле закрыто. Заменить реле (ы), если сопротивление высокое или звуковой щелчок **не** слышен при его вводе в действие. |
| Недостаточная наземная (-) связь | Проверьте штырь J1B для заземления контроллера. Проверьте ремешок земли (-) на нагреватель сетки на высокое сопротивление. Ремонт или замена проводов. |
| Неисправность контроллера | Проверьте штифт J2A на 12-VDC сигнал; проверьте электропроводку для шортинга, шофинга или горения. Контроллер работает между 6,5 и 16 VDC. Проверьте разъемы на наличие хороших соединений. Замените контроллер, если это необходимо. |
|  | Примечание: Контроллер прекратит перегрев, если он чувствует падение напряжения ниже 9,5 ВДК во время предварительного нагрева или 10-секундную задержку или более между выключенным и включаемым светильником WAIT-TO-START (WTS) или схемой открытой температуры. |

6B Промышленный нагреватель

Нагреватель коллектора воздухозаборника является предпочтительным вариантом начальной помощи при производстве на всех 185- и 200-сильный номинальных и опциональным на всех других двигателях с водяным охлаждением (WJAC) с встроенными насосами впрыска Bosch®. Для двигателей **не**, оснащенных вариантом воздухозаборного коллектора, вместо впускного нагревателя будет установлен блок прокладки.

Водоприемный нагреватель улучшает характеристики запуска холодной погоды, нагревая воздух во время проворачивания. Он также может служить для уменьшения белого дыма, если он заряжается во время низких температур окружающей среды, пока двигатель находится в режиме ожидания. Впускные обогреватели доступны как для систем 12-VDC, так и для систем 24-VDC, и оба вытягивают 195 ампер при подаче энергии.

Новое оборудование было разработано для поддержки установки нагревателя сети. Двигатель будет иметь одинаковую общую высоту установки. Решетки нагревателя также имеет резерв для воздухоприемной линии компрессора.

![[10900050.png]]

| Наименование | Номер детали | Количество |
|---|---|---|
| Сетчатый обогреватель (12 VDC) | 3928465 | 1 |
| Сетчатый обогреватель (24 VDC) | 3928463 | 1 |
| Спейсер Блок | 3928464 | 1 |
| Провод массы | 3928702 | 1 |

![[10900053.png]]

Перепроектированное оборудование, установленное на обогреватель для сетки двигателя, включает в себя:

1. Водяной пиджак послеохладитель
2. Водяная куртка послеохладитель сантехника
3. Топливные линии высокого давления
4. Топливные линии низкого давления
5. Крышка для кроссовера
6. Прокладка протока
7. Линия управления воздушным топливом.

> [!note] Примечание
> Это оборудование будет установлено на всех промышленных двигателях с водяным охлаждением с встроенным насосом Bosch®. Номера деталей будут указаны в каталоге деталей для промышленных двигателей 6B.

### Контроль при обслуживании

Проверьте напряжение батареи.

Минимум: 6.5 VDC

![[ea900sb.png]]

Проверьте терморезистор.

Отключите терморезистор.

Включите переключатель зажигания в положение Включения.

![[ee900wc.png]]

> [!note] Примечание
> Свет должен быть готов к началу.

Соленоиды должны нажать на.

![[ee900kb.png]]

Подожди 20 секунд.

Соленоиды должны отщелкиваться.

Свет от WAIT-TO-START должен начать мигать.

> [!note] Примечание
> Свет WAIT-TO-START будет мигать, указывая на открытую цепь в терморезисторной проводах. Отключение терморезистора имитирует это состояние.

![[ee900kc.png]]

Переключатель зажигания переключателя в положение выключения.

Подключите терморезисторную проводную упряжку.

![[ee900wd.png]]

Тепловой цикл - Проверка

Включите переключатель зажигания в положение Включения.

Не запускать двигатель.

![[ee900we.png]]

Соленоиды должны нажать на.

> [!note] Примечание
> Если двигатель работает, температура, вероятно, выше 15 ° C[59 ° F].

![[ee900kd.png]]

После периода предварительного нагрева свет WAIT-TO-START будет отключаться и **не **вспыхнет.

Установите многометровую шкалу для считывания напряжения постоянного тока.

Соедините мультиметр, номер детали 3822666, и выведите к впускному коллектору обогревателя. Проверяйте каждый терминал индивидуально.

![[ee900ke.png]]

Если напряжение присутствует, проверьте катушку втягивания соленоидов.

Проверьте напряжение на катушке соленоида.

1. Если напряжение на тяговой катушке, замените электронный модуль управления.
2. Если при тяге нет напряжения, замените соленоид.

![[ee900kf.png]]

Запускай двигатель.

Не удерживайте замок зажигания в стартовом положении дольше 10 секунд.

Если двигатель не запускается, поверните переключатель зажигания в положение выключения.

![[ee900kg.png]]

Верните переключатель зажигания в положение Включения; затем снова начните нормальный стартовый цикл.

![[ee900wf.png]]

### Снятие

> [!danger] ОПАСНО
> Всегда блокируйте и отметьте систему зажигания перед работой на двигателе. Отключить электрическую систему предварительного нагрева, чтобы уменьшить вероятность повреждения имущества и травмы от электрического шока.

Удалите локтевой воздухозаборник с крышки.

![[ic9tbaa.png]]

Удалите воздухозаборник, номер детали 3917938, из крышки и выбросьте. Если многообразный прокладочный элемент не используется, замените локтевой элемент на локтевой, номер детали 3918982 или эквивалентный.

![[im9cvmb.png]]

### Установка

Установите две прокладки, номер детали 3913352, выше и ниже сетевого нагревателя, номер детали 3924594, с наземным (-) ремешком под креплением болтов сетевого нагревателя.

> [!tip] Момент затяжки
> 24 Н·м [18 фунт-фут]

![[10900276.png]]

Установите зажимы воздухозаборника.

> [!tip] Момент затяжки
> 8 Н·м [71 фунт-дюйм]

![[ic9tbaa.png]]

Установите датчик температуры в крышке впуска, ближайшей к впускному локтю.

> [!tip] Момент затяжки
> 35 Н·м [26 фунт-фут]

![[10900275.png]]

> [!note] Примечание
> Упряжка проводов должна быть защищена в пределах 152 мм \[6 в\] любого соединения, чтобы уменьшить возможность повреждения разъёма или кольцевого терминала.

Установите проводку и защитите ее, чтобы избежать побоев или горения.

![[10900274.png]]

Если двигатель не имеет электрического выключателя соленоида или имеет модуль таймера для выключения соленоида, используйте 3-контактный соединительный трой для проводов транспортного средства, как показано на рисунке. Смотрите таблицу ниже.

| Письмо-коннектор | Функция | Рекомендуемое местоположение |
|---|---|---|
| А. | Модуль Power | переключатель зажигания на источнике питания |
| B | Crank Sensor | Терминал "S" на стартере или выключателе зажигания "Crank" |
| C | Земля (-) | Двигатель, шасси или аккумуляторная площадка (-) |

![[10900273.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> This procedure covers intake manifold heater element components for 1991 and 1994 Automotive and Industrial engine ratings. This procedure also covers upfit of intake manifold heater element components on engines **not** originally built with an intake heater option (front gear train engines only).
>
> **WARNING · Опасно**
> To reduce the possibility of personal injury and property damage, never use starting fluid with the air intake manifold heater. Starting fluid, which contains ether, can cause an explosion.
>
> **WARNING · Опасно**
> Starting fluid is highly flammable and explosive. Keep flames, sparks, and arcing switches away from starting fluid. This combination can cause an explosion and bodily injury.
>
> Warning labels, Part Number 3927335, **must** be installed in locations obvious to the operator, near the most likely point of entry of ether, and on a visible side of the heater. The sun visor and the air cleaner intake is two examples.
>
> The 12-VDC B Series charge air cooled, turbocharged, and naturally aspirated engines (6BTAA, 6BT, and 6B) use the air intake manifold heater as a cold weather starting aid. There is no air intake manifold heater for the water jacket aftercooled engine (6BTA) or 24-VDC electrical system at this time, and the air intake manifold heater is **not** compatible with marine applications.
>
> Benefits from an air intake manifold heater include:
>
> - Quicker start times
> - Smoother engine running after starting
> - Replaces ether as a starting aid
> - Extends starter and battery life through less cranking.
>
> The air intake manifold heater is very similar to the popular light-duty truck application grid heater in use since 1988. This heater electronically controls the two heating elements to optimize cold weather starts and improved cold engine running.
>
> Engine mounted hardware includes:
>
> - Air intake manifold heater
> - Temperature sensor
> - Controller
> - Wiring harness.
>
> **Note · Примечание**
> The kit does **not** include 6 AWG wire or ring terminals needed for the battery and other connections.
>
> White smoke indicates unburned fuel during cold engine operation.
>
> The intake manifold heater system is **not** directly connected to the fuel system, but it monitors the temperature of the air to the engine. The thermistor sends varying resistance values to the electronic control module (ECM), or equivalent. The ECM in turn controls the WAIT-TO-START lamp and the heater solenoids.
>
> The intake manifold heater elements operate in both the preheat and postheat modes.
>
> - In preheat, the ignition switch is on, but the engine has **not** been started.
> - In postheat, the engine is running.
>
> The proper operation of the intake manifold heater system and starting procedures will preclude excessive engine starter motor use and minimize white exhaust smoke when the engine is first started.
>
> | Normal Operation of the Intake Manifold Heater System |  |  |  |  |
> |---|---|---|---|---|
> | Temperature | Condition | Elements | Duration | Duty Cycle Percent ON/OFF |
> | Below -19°C \[-2°F\] | Preheat | Both | 30 seconds | Continuous |
> |  | Postheat | Both | 15 seconds | Continuous |
> |  |  | One | 15 seconds | Continuous |
> |  |  | One | 40 seconds | 50/50 |
> |  |  | One | 106 seconds | 25/75 |
> | -19 to -8°C \[-2 to 18°F\] | Preheat | Both | 20 seconds | Continuous |
> |  | Postheat | Both | 20 seconds | Continuous |
> |  |  | One | 20 seconds | Continuous |
> |  |  | One | 20 seconds | Continuous |
> |  |  | One | 40 seconds | 50/50 |
> |  |  | One | 106 seconds | 25/75 |
> | -8 to 8°C \[18 to 46°F\] | Preheat | Both | 10 seconds | Continuous |
> |  | Postheat | Both | 10 seconds | Continuous |
> |  |  | One | 10 seconds | Continuous |
> |  |  | One | 10 seconds | Continuous |
> |  |  | One | 40 seconds | 50/50 |
> |  |  | One | 106 seconds | 25/75 |
> | Below 8°C \[46°F\] | Preheat | None |  |  |
> |  | Postheat | None |  |  |
> | Amperage Draw - 95 amps per element |  |  |  |  |
> | To prevent excessive drain on the batteries, the electric heater controller has incorporated a battery monitoring feature. If the battery VDC were dropped too low, the heater controller will delay the postheat cycle, preventing further drain on the batteries. This battery protection feature is **only** activated on vehicles with weak or drained batteries. |  |  |  |  |
>
> \*Heater control modules or electronic control modules with serial numbers below 0080000A will **not** have a preheat cycle during this cycle.
>
> Battery Size Requirements for B Series Engines (automotive and industrial ratings)
>
> 1991 and 1994 6BTAA and 4BTAA automotive ratings
>
> **Note · Примечание**
> Unaided starting down to 0°C \[+32°F\] or intake heater equipment\*
>
> | 4BTAA Engine |  |  |
> |---|---|---|
> | Heavy accessory | Cold Cranking Amps (CCA) | Reserve Minutes |
> | Light accessory | 900 | 160 |
> |  | 750 | 169 |
> | \* Intake heater equipment option requires a 95-amp alternator or larger. |  |  |
>
> | 6BTAA Engine |  |  |
> |---|---|---|
> |  | Cold Cranking Amps (CCA) | Reserve Minutes |
> | Heavy accessories | 1000 | 160 |
> | Light accessories | 850 | 160 |
> | \* Intake heater equipment option requires a 95-amp alternator or larger. |  |  |
>
> **Note · Примечание**
> Unaided starting down to -12°C \[10°F\].
>
> | 4BTAA Engine |  |  |
> |---|---|---|
> |  | Cold Cranking Amps (CCA) | Reserve Minutes |
> | Heavy accessories | 1350 | 320 |
> | Light accessories | 1125 | 320 |
>
> | 6BTAA Engine |  |  |
> |---|---|---|
> |  | Cold Cranking Amps (CCA) | Reserve Minutes |
> | Heavy accessories | 1500 | 320 |
> | Light accessories | 1250 | 320 |
>
> 1994 6BTAA and 4BTAA industrial ratings
>
> | 4BTAA Engine |  |  |
> |---|---|---|
> |  | Cold Cranking Amps (CCA) | Reserve Minutes |
> | Heavy accessories | 800 | 160 |
> | Light accessories | 625 | 160 |
>
> | 6BTAA Engine |  |  |
> |---|---|---|
> |  | Cold Cranking Amps (CCA) | Reserve Minutes |
> | Heavy accessories | 950 | 160 |
> | Light accessories | 800 | 160 |
>
> **Note · Примечание**
> Typical “light accessories” include alternator, small steering pump, and disengaged clutch.
>
> **Note · Примечание**
> Typical “heavy accessories” include hydraulic pump and torque convertor.
>
> Air Intake Heater Controller Interconnection Diagram
>
> Cold Starting System
>
> 1. Grid heater
> 2. Air intake temperature sensor
>
> The following illustration shows grid heater components.
>
> Grid Heater Component Connections
>
> 1. Ground connection
> 2. To WAIT-TO-START lamp(s) (dash mounted)
> 3. Ground connection
> 4. To fuse and battery
> 5. Ground connection
>
> | Troubleshooting for Heater System |  |
> |---|---|
> | Wait-to-Start (WTS) Lamp **Not** Functioning | Check wiring, socket, bulb, ground signal from controller, and bulb power supply from the keyswitch. Correct any electrical problems with the WTS lamp. WTS lamp will flash one time a second if an open circuit is detected in the temperature sensor. |
> | Temperature Sensor Failed | Check resistance across the temperature sensor pins J1A and J1B at room temperature and in an ice bath 0°C \[32°F\]. The resistance should be approximately 800 ohms at room temperature and 2000 ohms for the ice bath. Check the resistance to ground (-) for an open circuit. |
> |  | Note: Make resistance checks with the keyswitch in the ON position to make sure there are no ground (-) problems. |
> |  | Replace defective sensor. |
> | Relay or Contactor Failure | Check relays or contactors for an audible click during operation. Check for pitting or burning in the relay by measuring resistance across the high-amperage terminals when relay is closed. Replace relay(s) if the resistance is high or an audible click is **not** heard when it is actuated. |
> | Insufficient Ground (-) Connections | Check pin J1B for ground to the controller. Check the ground (-) strap to the grid heater for high resistance. Repair or replace wiring. |
> | Controller Malfunctioning | Check pin J2A for 12-VDC signal; inspect the wiring harness for shorting, chafing, or burning. The controller operates between 6.5 VDC and 16 VDC. Check the connectors for good connections. Replace the controller, if necessary. |
> |  | Note: The controller will abort postheat if it senses a voltage drop below 9.5 VDC during preheat or a 10-second delay or more between WAIT-TO-START (WTS) lamp off and cranking, or an open temperature circuit. |
>
> 6B Industrial Grid Heater
>
> The air intake manifold heater is preferred starting aid option in production on all 185- and 200-hp ratings and optional on all other water jacket aftercooled (WJAC) engines with Bosch® in-line injection pumps. For engines **not** equipped with the air intake manifold heater option, a spacer block will be installed instead of an intake heater.
>
> The intake heater improves cold weather starting characteristics by heating the intake air during cranking. It can also serve to reduce white smoke if it is engergized during cold ambient temperatures while the engine is at idle. The intake heaters are available for both 12-VDC and 24-VDC systems, and both draw 195 amps while energized.
>
> New hardware has been designed to support the grid heater installation. The engine will have the same overall installation height. The grid heater also has a provision for an air compressor intake line.
>
> | Description | Part Number | Quantity |
> |---|---|---|
> | Grid Heater (12 VDC) | 3928465 | 1 |
> | Grid Heater (24 VDC) | 3928463 | 1 |
> | Spacer Block | 3928464 | 1 |
> | Ground Wire | 3928702 | 1 |
>
> Redesigned hardware installed on the engine to grid heater include:
>
> 1. Water jacket aftercooler
> 2. Water jacket aftercooler plumbing
> 3. High-pressure fuel lines
> 4. Low-pressure fuel lines
> 5. Crossover duct
> 6. Crossover duct gasket
> 7. Air-fuel control line.
>
> **Note · Примечание**
> This hardware will be installed on all water jacket aftercooled industrial engines with the Bosch® in-line pump. Part numbers will be listed in the 6B industrial engine parts catalog.
>
> ### Maintenance Check
>
> Check the battery voltage.
>
> Minimum: 6.5 VDC
>
> Check the thermistor.
>
> Disconnect the thermistor.
>
> Turn the ignition switch to the ON position.
>
> **Note · Примечание**
> The WAIT-TO-START light should come on.
>
> The solenoids should click on.
>
> Wait 20 seconds.
>
> The solenoids should click off.
>
> The WAIT-TO-START light should begin flashing.
>
> **Note · Примечание**
> The WAIT-TO-START light will flash, indicating an open circuit in the thermistor wiring. Disconnecting the thermistor simulates this condition.
>
> Turn the ignition switch to the OFF position.
>
> Connect the thermistor wire harness.
>
> Preheat Cycle - Check
>
> Turn the ignition switch to the ON position.
>
> Do **not** start the engine.
>
> The solenoids should click on.
>
> **Note · Примечание**
> If the engine has been running, the temperature is probably above 15°C \[59°F\].
>
> After the preheat period, the WAIT-TO-START light will go off and **not** flash.
>
> Set the multimeter scale to read DC voltage.
>
> Connect the multimeter, Part Number 3822666, lead to the intake manifold heater terminals. Check each terminal individually.
>
> If voltage is present, check the pull-in coil of the solenoids.
>
> Check for voltage at the pull-in coil of solenoid.
>
> 1. If voltage at pull-in coil, replace electronic control module.
> 2. If no voltage present at pull-in, replace solenoid.
>
> Start the engine.
>
> Do **not** hold the ignition switch in the start position longer than 10 seconds.
>
> If the engine does **not** start, turn the ignition switch to the OFF position.
>
> Return the ignition switch to the ON position; then begin the normal starting cycle again.
>
> ### Remove
>
> **WARNING · Опасно**
> Always lock and tag out the ignition system before working on the engine. Disable the preheater electrical system to reduce the possibility of property damage and personal injury from electrical shock.
>
> Remove the air intake elbow from the cover.
>
> Remove the air intake spacer, Part Number 3917938, from the intake cover and discard. If a manifold spacer is **not** used, replace the elbow with elbow, Part Number 3918982, or equivalent.
>
> ### Install
>
> Install the two gaskets, Part Number 3913352, above and below the grid heater, Part Number 3924594, with the ground (-) strap under the grid heater mounting capscrews.
>
> **Момент затяжки · Torque Value**
> 24 n•m [18 ft-lb]
>
> Install the air intake clamps.
>
> **Момент затяжки · Torque Value**
> 8 n•m [71 in-lb]
>
> Install the temperature sensor in the intake cover nearest the intake elbow.
>
> **Момент затяжки · Torque Value**
> 35 n•m [26 ft-lb]
>
> **Note · Примечание**
> The wiring harness **must** be secured within 152 mm \[6 in\] of any connection to reduce the possibility of connector or ring terminal damage.
>
> Install the wiring harness, and secure to avoid chafing or burning.
>
> If the engine does **not** have an electrical shutdown solenoid or it has a timer module for the shutdown solenoid, use the 3-pin connector tee to wire the vehicle as illustrated. See the table below.
>
> | Connector Letter | Function | Recommended Location |
> |---|---|---|
> | A | Module Power | Keyswitch ON power supply |
> | B | Crank Sensor | "S" Terminal on starter or keyswitch "Crank" |
> | C | Ground (-) | Engine, Chassis, or Battery Ground (-) |
