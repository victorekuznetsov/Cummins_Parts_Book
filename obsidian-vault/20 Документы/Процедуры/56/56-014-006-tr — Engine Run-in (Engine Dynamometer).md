---
aliases:
  - "Обкатка двигателя (на моторном стенде)"
type: "Процедура"
doc: "56-014-006-tr"
title_en: "Engine Run-in (Engine Dynamometer)"
title_ru: "Обкатка двигателя (на моторном стенде)"
modified: "2007-05-07"
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
figures: 33
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-014-006-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-014-006-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "двигатель/QSK60CM2150MCRS"
  - "группа/56"
  - "перевод/машинный"
---

# Engine Run-in (Engine Dynamometer)
**Обкатка двигателя (на моторном стенде)**

> [!abstract] Процедура · `56-014-006-tr`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]]
> **Семейство:** QSK60, QSK60 CM2150 MCRS
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2007-05-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-014-006-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-014-006-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Установка

Проверка

> [!warning] ОСТОРОЖНО
> Система моторного масла должна быть заряжена перед работой двигателя после реконструкции, чтобы избежать повреждения внутренних компонентов. Не загружайте систему из обходного фильтра, так как фильтр будет поврежден.

Промышленные двигатели QSK45 и QSK60 оснащены системой автоматического прелюбирования с завода. Если двигатель **не** оборудован автоматической системой прелюбирования, следуйте инструкциям для прелюбирования системы вручную.

![[14400011.png]]

Для двигателей без автоматической прелюбы, используйте насос, способный подавать 205 кПа \[30 psi\] непрерывного давления. Подключите насос к передней части охладителя моторного масла, как показано.

Используйте запас чистого масла. Поверните насос в положение ON. Проверьте датчик давления масла в двигателе. Когда калибр указывает на давление масла, начните мониторинг уровня масла в масляной кастрюле.

![[pl4hoha.png]]

Проверьте уровень моторного масла двигателя, чтобы убедиться, что оно заполнено до нужного уровня.

![[oi8dsva.png]]

> [!danger] ОПАСНО
> Не снимайте пробку радиатора с горячего двигателя. Снимайте пробку радиатора только после того, как температура охлаждающей жидкости опустится ниже 50 °C \[120 °F\]. Струя горячей охлаждающей жидкости или пар могут привести к травме.

> [!warning] ОСТОРОЖНО
> Не добавляйте холодную охлаждающую жидкость в горячий двигатель. Это может привести к повреждению литья двигателя. Позвольте двигателю охладиться до температуры ниже 50°C \[120°F\] перед добавлением охлаждающей жидкости.

Проверьте уровень охлаждающей жидкости двигателя.[[56-008-018-tr — Cooling System|См. процедуру 008-018 (Система охлаждения) в разделе 8]]

Используйте известный источник качественного дизельного топлива No2. Дизельные топлива № 1, наряду с большинством других альтернативных видов топлива, легче (более низкая удельная гравитация, более высокая гравитация API), чем дизельное топливо № 2. Чем легче топливо, тем ниже содержание энергии (BTU) на галлон (литр и т.д.).

![[ra200sa.png]]

Двигатель Throttle Control

Механически приводимый в действие форсунка

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Для уменьшения возможности дуги сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Отключите кабели аккумулятора перед началом следующей процедуры.

Отсоедините электропроводку OEM от электронного модуля управления (ECM) (если применимо).

![[22c00141.png]]

Отсоедините проводные упряжки OEM 21-контактный и 31-контактный разъемы Deutsch от электропроводки двигателя.

Подключите электропроводку управления двигателем, номер детали 4918643.

Подключите к ремню 21-контактную и 31-контактную проводку управления двигателем к ремню электропроводки двигателя.

![[19a00768.png]]

> [!note] Примечание
> Если для подключения управления двигателем требуется дополнительная длина кабеля, используйте электрический кабель, номер детали 3163895.

Подключите проводку управления двигателем (2) к управлению двигателем. Электронный инструмент, оснащенный персональным компьютером INSITETM, может использоваться для мониторинга цепей для правильной работы. Подключите комплект адаптера шины данных INLINETM5 CAN (3), Номер детали 4918416 и персональный компьютер к разъему шины данных CAN управления двигателем.

![[22c00125.png]]

Двигатели, которые работают на динамометре двигателя, требуют установки и подключения к двигателю электропроводки. Кроме того, двигатель, номер детали 3163890, должен быть использован для правильного управления двигателем во время работы динамометра.

![[wr8coac.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Подключите питание от батареи к стартеру.

Подключите динамометр теста OEM-проводов ремня стартера соленоидного свинца (желтого цвета) к стартерному соленоиду. Подключите грунтовый свинец (черный) к стартеру соленоида. Подключите заземляющий свинец (черный) к стартеру или аккумулятору отрицательной (-) или стороне земли. Подключите (+) 12-VDC силовой привод (красный) к стартеру или положительной (+) 12-VDC стороне батареи.

![[sb8coma.png]]

Вращайте ручку дроссельной заслонки полностью **против часовой стрелки**. Нажмите на ручку дроссельной заслонки, чтобы вернуть дроссель в положение холостого хода.

Повторите этот шаг три раза.

Переключатель зажигания в положение выключения в течение 30 секунд.

![[22c00156.png]]

> [!warning] ОСТОРОЖНО
> Проверьте уровень охлаждающей жидкости и моторного масла перед запуском и работой двигателя. Если охлаждающая жидкость и моторное масло не находятся на должном уровне, может возникнуть повреждение двигателя.

Включите переключатель зажигания в положение START до запуска двигателя и отпустите переключатель зажигания.

![[22c00129.png]]

Электронный форсунка

Отсоедините проводку OEM-упряжи 16-контактных и 23-контактных разъемов Deutsch от электропроводки двигателя, если она подключена.

Удалите 3-контактный резистор Deutsch (кап будет иметь синюю вставку) из электропроводки.

Подключите 3-контактный разъем Deutsch для управления двигателем к разъему шины данных SAE J1939 CAN для проводов двигателя.

3-контактный резистор Deutsch концевой резисторной крышки должен быть установлен после того, как убрана проводка управления двигателем. Если крышка сломана или была неправильно расположена, замените резисторную крышку, номер детали 3163051.

![[22400280.png]]

Наземное соединение

Подключите черную проводку аллигатора к ремню управления двигателем к блоку двигателя, чтобы достичь электрического заземления.

![[19c01031.png]]

> [!warning] ОСТОРОЖНО
> Не подключайте зажим аллигатора к стартовому моторному соленоидному терминалу «S». Это может привести к повреждению оборудования.

Стартовое соединение

Если **не** уже оборудован, установите и проведите магнитный стартер.

Заткните разъем аллигатора к положительному (+) концевому клемму катушки магнитного стартера.

![[22400055.png]]

Air Starter

Если используется воздушный стартер, введите красный провод в петлю и закрепите петлю на электропроводке управления двигателем, чтобы защитить его от электрического короткого.

![[19c01032.png]]

Работа двигателя

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Прикрепите управляющую проводку упряжкой с помощью кольцевого терминала красного провода к положительному (+) терминалу батареи.

Прикрепите управляющую проводку упряжкой с помощью кольцевого терминала черного провода к отрицательному (-) терминалу батареи.

Прикрепите управляющую проводку упряжкой с помощью кольцевого терминала красного провода к положительному (+) терминалу батареи. Прикрепите управляющую проводку упряжкой с помощью кольцевого терминала черного провода к отрицательному (-) терминалу батареи.

![[sb8coma.png]]

> [!warning] ОСТОРОЖНО
> Проверить, что красный провод подключен к положительному (+) клемме батареи, а черный провод подключен к отрицательному (-) клемме батареи. Повреждение оборудования или двигателя может привести к неправильному подключению.

Силовой свет будет освещаться при подаче питания и переключатель зажигания поворачивается в положение аксессуара или Включено.

Если силовой свет не освещается, верните переключатель зажигания в положение выключения. Проверить, что красный провод подключен к положительному (+) клемме батареи, а черный провод подключен к отрицательному (-) клемме батареи.

Переведите замок зажигания в положение ON.

![[22c00127.png]]

Световые индикаторы на управлении двигателем, STOP, WARN, MAINT, WIF и WAIT TO START, будут освещаться, если это применимо. Световые индикаторы будут светиться в течение примерно 30 секунд. Если не будет найдено кодов неисправностей, световые индикаторы погаснут.

Если индикатор STOP (красный) или индикатор WARN (желтый) продолжает освещаться, используйте инструмент для электронного обслуживания INSITETM и литературу по обслуживанию OEM для диагностики кода неисправности двигателя.

![[22c00128.png]]

> [!warning] ОСТОРОЖНО
> Проверьте уровень охлаждающей жидкости и моторного масла перед запуском и работой двигателя. Если охлаждающая жидкость и моторное масло не находятся на должном уровне, может возникнуть повреждение двигателя.

Включите переключатель зажигания в положение START до запуска двигателя и отпустите переключатель зажигания.

![[22c00129.png]]

> [!note] Примечание
> Двигатель может быть возвращен в бездействие в любое время, нажав на ручку дросселя.

Медленно поверните ручку дроссельной заслонки **против часовой стрелки**, чтобы увеличить обороты двигателя.

Медленно поверните ручку дроссельной заслонки **по часовой стрелке**, чтобы уменьшить обороты двигателя.

![[22c00130.png]]

Включите переключатель зажигания в положение выключения, чтобы остановить двигатель.

![[22c00131.png]]

Возвращайте параметры к их исходным значениям, когда тест или запуск завершены.

Подключите панель переключателя зажигания CAN кабеля шины данных к электронному сервисному инструменту Cummins®.

Используйте инструмент электронного обслуживания INSITETM для настройки двигателя для динамометра.[[56-014-008-tr — Engine Testing (In Chassis)|См. процедуру 014-008 (Испытание двигателя (в шасси)) в разделе 14 для получения дополнительной информации об этой функции.]]

Настройка теперь завершена, и для управления скоростью двигателя можно использовать автоматическое / ручное дроссельное заслонки.

![[14c00040.png]]

Технические характеристики двигателя доступны в авторизованных местах ремонта Cummins®.

![[lt800ga.png]]

### Запуск инструкций

Проконсультируйтесь с литературой производителя динамометра для соответствующих значений динамометрических констант и расчетов.

В таблице 1 приводится краткая информация о процедуре взлома; в таблице 1 используется информация о данной процедуре.

| Таблица 1 |  |  |  |  |
|---|---|---|---|---|
| Шаг вперед | Время (протоколы) | Промышленный (50 Гц, 60 Гц) | Энергогенерация (50 Гц) | Энергогенерация (60 Гц) |
| 1 | 5 | 35% - Torque Peak Speed | 25% от Standby @ 1300 rpm | 35% от Standby @ 1500 об/мин |
| 2 | 10 | 75% Torque Peak Speed (Моменте Пик Скорость) | 50% от Standby @ 1300 rpm | 50% от Standby @ 1500 об/мин |
| 3 | 10 | 100% Torque Peak Speed (Моменте Пик Скорость) | 75% от Standby @ 1300 об/мин | 75% от Standby @ 1500 об/мин |
| 4 | 10 | 100% полной загрузки @ Rated Speed | 100% Prime @ 1500 об/мин | 100% Prime @ 1800 rpm |

В таблице 2 приведена соответствующая информация о загрузке двигателей QSK45 и QSK60 Industrial.

| Таблица 2 |  |  |  |  |
|---|---|---|---|---|
| Рейтинг rpm | Rated Horsepower Hp (kw) | Пиковый крутящий момент rpm фунт-фут (Nm) | Пиковый крутящий момент rpm | Модель двигателя |
| 1900 | 2700 (2013) | 7839 (10268) | 1500 | QSK60 |
| 1900 | 2500 (1864) | 7260 (9843) | 1500 | QSK60 |
| 1800 | 2200 (1641) | 6618 (8973) | 1500 | QSK60 |
| 1900 | 2300 (1715) | 6677 (9053) | 1500 | QSK60 |
| 1900 | 2000 (1491) | 6169 (8364) | 1500 | QSK60 |
| 1900 | 1875 (1398) | 6169 (8364) | 1500 | QSK60 |
| 1900 | 1800 (1342) | 6274 (8506) | 1500 | QSK60 |
| 1900 | 2250 (1678) | 6300 (8542) | 1500 | QSK45 |
| 1900 | 2000 (1491) | 5805 (7871) | 1500 | QSK45 |
| 1900 | 1600 (1193) | 5042 (6836) | 1500 | QSK45 |
| 1900 | 1500 (1119) | 5042 (6836) | 1300 | QSK45 |
| 1900 | 1500 (1119) | 4727 (6049) | 1500 | QSK45 |
| 1800 | 1350 (1007) | 4525 (6135) | 1300 | QSK45 |
| 1900 | 1200 (895) | 4425 (5999) | 1300 | QSK45 |
| 1900 | 2850 (2125) | 8274 (11218) | 1600 | QSK60 Tier 2 |
| 1900 | 2700 (2013) | 7839 (10628) | 1500 | QSK60 Tier 2 |
| 1900 | 2500 (1864) | 7528 (9841) | 1500 | QSK60 Tier 2 |
| 1800 | 2000 (1491) | 6169 (8363) | 1500 | QSK60 Tier 2 |

[[56-014-005-tr — Engine Testing (Engine Dynamometer)|См. процедуру 014-005 (Испытание двигателя - Динамометр двигателя) в разделе 14, для общих рабочих процедур и мер предосторожности.]]

Испытание на включение **должно** проводиться с двигателем, работающим на пике крутящего момента оборотов в минуту. Управляйте генераторным двигателем с номинальной оборотной массой. См. диаграммы производительности, доступные через Cummins Inc.

Используйте эту диаграмму для определения испытательной нагрузки.

![[00400005.png]]

> [!warning] ОСТОРОЖНО
> Не проворачивайте пусковой двигатель более 30 секунд. Избыточное тепло повредит стартер.

> [!warning] ОСТОРОЖНО
> Если давление масла не соответствует спецификациям, немедленно остановите двигатель. Низкое и высокое давление масла может привести к повреждению двигателя.

Запускай двигатель. Если двигатель не работает через 30 секунд, дайте 2 минуты, чтобы двигатель остыл.

Проверьте давление масла.

| каша |  | пси |
|---|---|---|
| 138 | Макс | 20 |
| 483 | Макс | 70 |

Если давление масла не соответствует спецификациям, двигатель должен быть выключен.

![[oi800vi.png]]

> [!warning] ОСТОРОЖНО
> Не работайте с двигателем на холостом ходу дольше, чем указано. Чрезмерное образование углерода приведет к повреждению двигателя.

Управляйте двигателем в положении холостого хода и проверяйте наличие утечек.

![[oi800vj.png]]

Настройка двигателя rpm до 1200 rpm. Нагрузка динамометра должна быть отрегулирована до испытательной нагрузки, как определено ранее. Работайте с двигателем при этой установке до тех пор, пока температура охлаждающей жидкости не покажет 71 ° C \[160° F \].

Проверка на утечку.

Ремонт любых утечек, обнаруженных во время проверки.

Проверьте **все **датчики и запишите показания.

**Не** переходите к следующему шагу, пока продувка не станет стабильной в пределах спецификаций.

![[14600050.png]]

Настройка оборотов двигателя на пиковый крутящий момент оборотов. Нагрузка динамометра должна быть в два раза больше испытательной нагрузки. Управляйте двигателем в течение двух минут.

Проверьте **все **датчики и запишите показания.

**Не** переходите к следующему шагу, пока продувка не станет стабильной в пределах спецификаций.

![[14600051.png]]

Поддерживайте обороты двигателя на пике крутящего момента оборотов в минуту. Увеличить нагрузку на динамометр до трехкратной испытательной нагрузки.

Работайте с двигателем при этой нагрузке в течение 2 минут.

Проверьте **все **датчики и запишите показания.

**Не** переходите к следующему шагу, пока продувка не станет стабильной в пределах спецификаций.

![[14600052.png]]

Переведите рычаг дроссельной заслонки в полностью открытое положение. Увеличьте нагрузку до тех пор, пока обороты двигателя не достигнут пикового крутящего момента оборотов в минуту.

Работайте с двигателем в этой установке в течение 10 минут или до тех пор, пока продувка не станет стабильной в соответствии со спецификациями.

Проверьте **все **датчики и запишите показания.

![[14600053.png]]

Уменьшите нагрузку на динамометр до тех пор, пока обороты двигателя не увеличатся до номинального оборота.

Работайте с двигателем при этой нагрузке в течение 5 минут.

Проверьте **все **датчики и запишите показания.

![[14600054.png]]

> [!warning] ОСТОРОЖНО
> Не выключайте двигатель немедленно. Двигатель должен быть охлажден.

> [!warning] ОСТОРОЖНО
> Не работайте с двигателем на холостом ходу дольше, чем указано. Чрезмерное образование углерода может привести к повреждению двигателя.

Полностью снизить нагрузку на динамометр.

Переключите двигатель на низкий холостой ход. Работайте с двигателем в этой установке в течение 3-5 минут. Это позволит охладить турбокомпрессор и другие компоненты двигателя.

![[oi800vj.png]]

Выключи двигатель.

![[oi800vp.png]]


> [!quote]- Original (English) · английский оригинал
> ### Install
>
> Test
>
> **CAUTION · Осторожно**
> The lubricating oil system must be primed before operating the engine after rebuild to avoid internal component damage. Do not prime the system from the bypass filter as the filter will be damaged.
>
> QSK45 and QSK60 industrial engines are equipped with an automatic prelube system from the factory. If the engine is **not** equipped with an automatic prelube system, follow the instructions to prelube the system manually.
>
> For engines without automatic prelube, use a pump capable of supplying 205 kPa \[30 psi\] continuous pressure. Connect the pump to the front of the engine oil cooler as shown.
>
> Use a supply of clean oil. Turn the pump to the ON position. Check the engine oil pressure gauge. When the gauge indicates oil pressure, begin monitoring the oil level in the oil pan.
>
> Check the engine lubricating oil level to be sure it is filled to the proper level.
>
> **WARNING · Опасно**
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.
>
> **CAUTION · Осторожно**
> Do not add cold coolant to a hot engine. This can cause engine casting damage. Allow the engine to cool to below 50°C \[120°F\] before adding coolant.
>
> Check the engine coolant level. [[56-008-018-tr — Cooling System|Refer to Procedure 008-018 (Cooling System) in Section 8]]
>
> Use a known source of good-quality number 2 diesel fuel. Number 1 diesel fuels, along with most other alternate fuels, are lighter (lower specific gravity, higher API gravity) than number 2 diesel fuel. The lighter the fuel, the lower the energy content (BTU) per gallon (liter, etc.).
>
> Engine Throttle Control
>
> Mechanically Actuated Injectors
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.
>
> Disconnect the battery cables before beginning the following procedure.
>
> Disconnect the OEM harness from the electronic control module (ECM) (if applicable).
>
> Disconnect the OEM harness 21-pin and 31-pin Deutsch connectors from the engine harness.
>
> Connect the engine control harness, Part Number 4918643.
>
> Connect the engine control harness 21-pin and 31-pin Deutsch connectors to the engine wiring harness.
>
> **Note · Примечание**
> If additional cable length is needed to connect the engine control, use electrical cable, Part Number 3163895.
>
> Connect the engine control harness (2) to the engine control. An INSITE™ electronic service tool equipped personal computer can be used to monitor circuits for proper operation. Connect the INLINE™5 datalink adapter kit (3), Part Number 4918416, and a personal computer to the datalink connector of the engine control.
>
> Engines that are run on an engine dynamometer require the engine harness be installed and connected to the engine. Additionally, the engine control, Part Number 3163890, **must** be used to properly control the engine during the dynamometer run.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Connect battery power to the starter.
>
> Connect the dynamometer test OEM wiring harness starter solenoid lead (yellow) to the starter solenoid. Connect the ground lead (black) to the starter solenoid. Connect the ground lead (black) to the starter or battery negative (-) or ground side. Connect the (+) 12-VDC power lead (red) to either the starter or battery positive (+) 12-VDC side.
>
> Rotate the throttle knob fully **counterclockwise**. Push down on the throttle knob to return the throttle to the idle position.
>
> Repeat this step three times.
>
> Turn the keyswitch to the OFF position for 30 seconds.
>
> **CAUTION · Осторожно**
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level, engine damage can result.
>
> Turn the keyswitch to the START position until the engine starts and release the keyswitch.
>
> Electronically Actuated Injectors
>
> Disconnect the OEM harness 16-pin and 23-pin Deutsch connectors from the engine harness if connected.
>
> Remove the 3-pin Deutsch terminal resistor cap (cap will have a blue insert) from the wiring harness.
>
> Connect the engine control harness 3-pin Deutsch connector to the SAE J1939 Datalink connector of the engine wiring harness.
>
> The 3-pin Deutsch terminal resistor cap **must** be installed after the engine control harness is removed. If the cap is broken or has been misplaced, replace with resistor cap, Part Number 3163051.
>
> Ground Connection
>
> Connect the black-wire alligator clip of the engine control harness to the engine block to achieve electrical ground.
>
> **CAUTION · Осторожно**
> Do not connect the alligator clip to the starter motor solenoid “S” terminal. Doing so can cause equipment damage.
>
> Starter Connection
>
> If **not** already equipped, install and wire a magnetic starter switch.
>
> Clip the alligator connector to the positive (+) coil terminal of the magnetic starter switch.
>
> Air Starter
>
> If an air starter is being used, coil the red wire into a loop and secure the loop to the engine control harness to protect it from an electrical short.
>
> Engine Operation
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Attach the control harness using the ring terminal of the red wire to the positive (+) terminal of the battery.
>
> Attach the control harness using the ring terminal of the black wire to the negative (-) terminal of the battery.
>
> Attach the control harness using the ring terminal of the red wire to the positive (+) terminal of the battery. Attach the control harness using the ring terminal of the black wire to the negative (-) terminal of the battery.
>
> **CAUTION · Осторожно**
> Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal. Equipment or engine damage can result if not connected properly.
>
> The power light will illuminate when power is supplied and the keyswitch is turned to the accessory or ON position.
>
> If the power light does **not** illuminate, return the keyswitch to the OFF position. Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal.
>
> Turn the keyswitch to the ON position.
>
> Light indicators on the engine control, STOP, WARN, MAINT, WIF, and WAIT TO START, will illuminate if applicable. The light indicators will illuminate for approximately 30 seconds. If no fault codes are found, the light indicators will extinguish.
>
> If the STOP light indicator (red) or WARN light indicator (yellow) continues to illuminate, use INSITE™ electronic service tool and the OEM service literature to diagnose the engine fault code.
>
> **CAUTION · Осторожно**
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level, engine damage can result.
>
> Turn the keyswitch to the START position until the engine starts and release the keyswitch.
>
> **Note · Примечание**
> The engine can be returned to idle at any time by pushing in on the throttle knob.
>
> Slowly rotate the throttle knob **counterclockwise** to increase the engine rpm.
>
> Slowly rotate the throttle knob **clockwise** to decrease the engine rpm.
>
> Turn the keyswitch to the OFF position to stop the engine.
>
> Return the parameters to their original values when the test or run-in is complete.
>
> Connect the keyswitch panel datalink cable to the Cummins® electronic service tool.
>
> Use INSITE™ electronic service tool to set the engine up for the dynamometer. [[56-014-008-tr — Engine Testing (In Chassis)|Refer to Procedure 014-008 (Engine Testing (In Chassis)) in Section 14 for more information on this feature.]]
>
> The setup is now complete, and the auto/manual throttle can be used to control engine speed.
>
> Engine operating specifications are available from Cummins® authorized repair locations.
>
> ### Run-In Instructions
>
> Consult the dynamometer manufacturer's literature for relevant dynamometer constant values and calculations.
>
> Table 1 provides a summary of the break-in procedure; information in Table 1 is used in this procedure.
>
> | Table 1 |  |  |  |  |
> |---|---|---|---|---|
> | Step | Time (Minutes) | Industrial (50 Hz, 60 Hz) | Power Generation (50 Hz) | Power Generation (60 Hz) |
> | 1 | 5 | 35% Torque Peak @ Torque Peak Speed | 25% of Standby @ 1300 rpm | 35% of Standby @ 1500 rpm |
> | 2 | 10 | 75% Torque Peak @ Torque Peak Speed | 50% of Standby @ 1300 rpm | 50% of Standby @ 1500 rpm |
> | 3 | 10 | 100% Torque Peak @ Torque Peak Speed | 75% of Standby @ 1300 rpm | 75% of Standby @ 1500 rpm |
> | 4 | 10 | 100% of Full Load @ Rated Speed | 100% of Prime @ 1500 rpm | 100% of Prime @ 1800 rpm |
>
> Table 2 provides the relevant loading information for the QSK45 and QSK60 Industrial engines.
>
> | Table 2 |  |  |  |  |
> |---|---|---|---|---|
> | Rated rpm | Rated Horsepower Hp (kw) | Peak Torque rpm lb-ft (Nm) | Peak Torque rpm | Engine Model |
> | 1900 | 2700 (2013) | 7839 (10268) | 1500 | QSK60 |
> | 1900 | 2500 (1864) | 7260 (9843) | 1500 | QSK60 |
> | 1800 | 2200 (1641) | 6618 (8973) | 1500 | QSK60 |
> | 1900 | 2300 (1715) | 6677 (9053) | 1500 | QSK60 |
> | 1900 | 2000 (1491) | 6169 (8364) | 1500 | QSK60 |
> | 1900 | 1875 (1398) | 6169 (8364) | 1500 | QSK60 |
> | 1900 | 1800 (1342) | 6274 (8506) | 1500 | QSK60 |
> | 1900 | 2250 (1678) | 6300 (8542) | 1500 | QSK45 |
> | 1900 | 2000 (1491) | 5805 (7871) | 1500 | QSK45 |
> | 1900 | 1600 (1193) | 5042 (6836) | 1500 | QSK45 |
> | 1900 | 1500 (1119) | 5042 (6836) | 1300 | QSK45 |
> | 1900 | 1500 (1119) | 4727 (6049) | 1500 | QSK45 |
> | 1800 | 1350 (1007) | 4525 (6135) | 1300 | QSK45 |
> | 1900 | 1200 (895) | 4425 (5999) | 1300 | QSK45 |
> | 1900 | 2850 (2125) | 8274 (11218) | 1600 | QSK60 Tier 2 |
> | 1900 | 2700 (2013) | 7839 (10628) | 1500 | QSK60 Tier 2 |
> | 1900 | 2500 (1864) | 7528 (9841) | 1500 | QSK60 Tier 2 |
> | 1800 | 2000 (1491) | 6169 (8363) | 1500 | QSK60 Tier 2 |
>
> [[56-014-005-tr — Engine Testing (Engine Dynamometer)|Refer to Procedure 014-005 (Engine Testing - Engine Dynamometer) in Section 14, for general operating procedures and safety precautions.]]
>
> The run-in test **must** be performed with the engine operating at torque peak rpm. Operate a generator set engine at rated rpm. See the performance charts available through Cummins Inc.
>
> Use this chart to determine the test load.
>
> **CAUTION · Осторожно**
> Do not crank the starting motor for more than 30 seconds. Excessive heat will damage the starter.
>
> **CAUTION · Осторожно**
> If the oil pressure is not within specifications, stop the engine immediately. Both low and high oil pressure will cause engine damage.
>
> Start the engine. If the engine does **not** begin operating after 30 seconds, allow 2 minutes for the starting motor to cool.
>
> Check the oil pressure.
>
> | kpa |  | psi |
> |---|---|---|
> | 138 | MAX | 20 |
> | 483 | MAX | 70 |
>
> If the oil pressure is **not** within specifications, the engine **must** be shut down.
>
> **CAUTION · Осторожно**
> Do not operate the engine at idle longer than specified. Excessive carbon formation will cause engine damage.
>
> Operate the engine in the idle position and check for leaks.
>
> Adjust the engine rpm to 1200 rpm. Adjust the dynamometer load to the test load as previously determined. Operate the engine at this setting until the coolant temperature indicates 71°C \[160°F\].
>
> Inspect for leaks.
>
> Repair any leaks found during inspection.
>
> Check **all** of the gauges and record the readings.
>
> Do **not** proceed to the next step until the blowby becomes stable within specifications.
>
> Adjust the engine rpm to the torque peak rpm. Adjust the dynamometer load to equal two times the test load. Operate the engine for two minutes.
>
> Check **all** the gauges and record the readings.
>
> Do **not** proceed to the next step until the blowby becomes stable within specifications.
>
> Maintain the engine rpm at torque peak rpm. Increase the dynamometer load to equal three times the test load.
>
> Operate the engine at this load for 2 minutes.
>
> Check **all** of the gauges and record the readings.
>
> Do **not** proceed to the next step until the blowby becomes stable within specifications.
>
> Move the throttle lever to the full-open position. Increase the load until the engine rpm is at torque peak rpm.
>
> Operate the engine at this setting for 10 minutes or until the blowby becomes stable within specifications.
>
> Check **all** of the gauges and record the readings.
>
> Decrease the dynamometer load until the engine rpm increases to the rated rpm.
>
> Operate the engine at this load for 5 minutes.
>
> Check **all** of the gauges and record the readings.
>
> **CAUTION · Осторожно**
> Do not turn the engine off immediately. The engine must be allowed to cool.
>
> **CAUTION · Осторожно**
> Do not operate the engine at idle longer than specified. Excessive carbon formation can cause engine damage.
>
> Decrease the dynamometer load completely.
>
> Switch the engine to low idle. Operate the engine at this setting for 3 to 5 minutes. This will allow the turbocharger and the other engine components to cool.
>
> Shut the engine off.
