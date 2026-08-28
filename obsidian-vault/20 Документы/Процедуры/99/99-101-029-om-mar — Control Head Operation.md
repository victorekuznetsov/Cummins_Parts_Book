---
aliases:
  - "Работа поста управления"
type: "Процедура"
doc: "99-101-029-om-mar"
title_en: "Control Head Operation"
title_ru: "Работа поста управления"
modified: "2025-02-05"
engines:
  - "93047320"
  - "93058669"
  - "93087701"
families:
  - "6B5.9"
  - "C8.3 · 6C8.3"
manuals:
  - "3381968"
  - "4021538"
figures: 27
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-101-029-om-mar.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-101-029-om-mar.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "двигатель/C8.3"
  - "группа/99"
  - "перевод/машинный"
---

# Control Head Operation
**Работа поста управления**

> [!abstract] Процедура · `99-101-029-om-mar`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** 6B5.9, C8.3 · 6C8.3
> **Входит в руководства:** [[3381968 — C8.3 Recreational Marine Operation and Maintenance Manual|3381968]], [[4021538 — B3.9 and B5.9 Recreational Marine Operation and Maintenance Manual|4021538]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2025-02-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-101-029-om-mar.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-101-029-om-mar.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Панель инструментов

> [!note] Примечание
> Информация ниже написана для двигателей, оснащенных системой управления, поставляемой OEM. Для двигателей, оснащенных Cummins Inc. Для получения дополнительной информации, в комплект поставки включены системы управления, справочные C Command Connect и Connect Premier Marine Panel System PS102 & PS103 Owners Manual Bulletin, [[5411481 — C Command Connect and Connect Premier Marine Panel System PS102, PS103 and PS108\|5411481]], или Marine C Command HD Elite Panel System Owners Manual Bulletin, [[4332829 — Marine C Command HD Elite Panel System Owners Manual\|4332829]].

Панель управления состоит из следующего:

1. Указатель давления масла
2. Тахометр
3. часовой метр
4. Измеритель температуры охлаждающей жидкости двигателя
5. бледный
6. Кнопка сброса сигнала тревоги
7. Начать нажимать кнопку
8. переключатель зажигания
9. Будильник
10. Вольтметр батареи.

![[15900027.png]]

Калибр для измерения давления масла

Измеритель давления масла (1) показывает рабочее давление масла в двигателе.

![[15900028.png]]

Тахометр w/час

Тахометр (2) показывает скорость коленчатого вала двигателя в оборотах в минуту (об/мин).

Часовой счетчик показывает количество часов работы. Эта функция используется для обслуживания двигателя (двигателей).

![[15900029.png]]

Вольтметр

Вольтметр (10) показывает напряжение батареи.

![[15900030.png]]

Указатель температуры охлаждающей жидкости

Калибр (4) температуры охлаждающей жидкости показывает температуру охлаждающей жидкости двигателя во время работы.

![[15900031.png]]

### Панель инструментов

Электронный губернатор

Включение ручки (4) управления освещением будет управлять подсветкой панели и всей подсветкой панели переключателя.

Поворот ручки **по часовой стрелке** уменьшит освещенность. Повернуть его **против часовой стрелки** увеличит освещенность.

![[13200080.png]]

### Приборы

Все датчики, кроме вольтметра (9), используемые с двигателем, приводятся в электронное движение. Измерители получают показания от высокоскоростной шины данных CAN, которая подключена к различным датчикам. Если калибр не имеет информации из шины данных CAN, он будет медленно переключаться между высокими и низкими крайностями.

![[13200083.png]]

Калибр для измерения давления масла

Измеритель давления масла (2) показывает рабочее давление масла в двигателе.

![[13200084.png]]

Тахометр w/час

Тахометр (3) показывает скорость коленчатого вала двигателя в оборотах в минуту (об/мин).

Часовой счетчик показывает количество часов работы. Эта функция используется для обслуживания двигателя (двигателей).

![[13200087.png]]

Вольтметр

Вольтметр (9) показывает напряжение батареи.

![[13200086.png]]

Указатель температуры охлаждающей жидкости

Калибр (10) температуры охлаждающей жидкости показывает температуру охлаждающей жидкости двигателя во время работы.

![[13200085.png]]

### Обновление Throttle

Необязательный резервный дроссел был разработан для использования в случае отказа основного дросселя.

#### Использование Throttle Usage

- Поверните резервную ручку дроссельной заслонки **против часовой стрелки** в положение холостого хода или нажмите ручку, чтобы привести двигатель в холостое состояние.
- Положите главный рычаг дросселя в положение холостого хода.
- Переместить резервный дроссель в положение Включения.
- Поверните ручку дроссельной заслонки **по часовой стрелке** на желаемую скорость двигателя.

Резервный дроссельный переключатель имеет функцию предохранительной защелки; нажмите защелку вниз и переместите переключатель в положение Включения. Дроссель также имеет воротник регулирования трения. Поверните ошейник **по часовой стрелке**, чтобы затянуть, или **против часовой стрелки**, чтобы ослабить, пока не будет получено желаемое напряжение дроссельной заслонки.

Чтобы отключить резервный дроссел и восстановить контроль над скоростью двигателя с помощью основного рычага дросселя:

1. Запустить резервный дроссел на холостом ходу
2. Установите основной дроссель на холостяцкое
3. Поместите резервный дроссель в положение OFF, уплотнив дно переключателя коромысла

![[13200055.png]]

### Программируемые функции

Дополнительный элемент выбора станции позволяет активировать электронные элементы с панели управления первичным или вторичным переключателем.

![[15200050.png]]

Коммутатор синхронизации двигателя

> [!danger] ОПАСНО
> Функция синхронизации двигателя должна быть отключена перед стыковкой или маневрированием на низкой скорости; это позволяет полностью и отдельно управлять каждым двигателем. Невыключение функции синхронизации двигателя может привести к травмам, повреждению судна и / или дока.

> [!note] Примечание
> Функция синхронизации двигателя является опцией, доступной только на двухмоторных судах.

Функция синхронизации двигателя используется для электронного управления скоростью обоих двигателей с использованием одного рычага дроссельной заслонки.

![[15200040.png]]

Обычно правый дроссел используется в качестве главного дроссельного двигателя. Дистрибьютор или дилер может изменить его на дроссельную заслону порта, если это необходимо, путем замены вилки мастера и раба в проводах двигателя. Смотрите инсталляцию.

![[13200062.png]]

Для использования функции синхронизации двигателя:

- Оба двигателя **должны *** находиться в одном и том же положении дроссельной заслонки, работая при одной и той же оборотах в минуту.
- Поместите переключатель ENG SYNC (1) в положение ON, уплотнив верхнюю часть переключателя коромысла.

Оба двигателя будут настраиваться на один и тот же оборот. Мастер дросселя будет управлять обоими двигателями.

> [!note] Примечание
> Эта функция будет отключаться, когда двигатель выключен. Когда двигатель перезапускается, переключатель должен быть выключен, а затем снова включен, чтобы активировать функцию.

![[15200040.png]]

Чтобы отключить функцию синхронизации двигателя:

1. Поместите переключатель ENG SYNC (1) в положение OFF, уплотнив нижнюю часть переключателя коромысла.
2. Переместите любой рычаг дроссельной заслонки в пределах 100 об/мин от другого, и функция отключится. Теперь рычаги дросселя будут работать самостоятельно.

![[nobox.png]]

Морской круизный контроль

Функция морского круиз-контроля обеспечивает две регулируемые скорости двигателя. Круиз-контроль может использоваться для запуска двигателя (двигателей) на оптимальном крейсерском обороте или троллинговом обороте.

CRUISE 1 имеет настройку по умолчанию 2100 об/мин.

CRUISE 2 имеет настройку по умолчанию 1200 об/мин.

> [!note] Примечание
> Функция морского круиз-контроля может использоваться в сочетании с функцией синхронизации двигателя.

![[15200038.png]]

Для активации функции морского круиз-контроля:

1. Поставьте круизный переключатель (1) в нужное положение, КРУЗЬ 1 или КРУЗЬ 2.
2. Переместите дроссель (дроссель) мимо желаемой крейсерской скорости.

Скорость двигателя (двигателей) будет увеличиваться до круизной установки.

> [!note] Примечание
> При использовании функции синхронизации двигателя основным дроссельным механизмом является дроссель **только**, который должен быть перемещен мимо точки круиза.

![[15200038.png]]

Чтобы отключить морской круиз-контроль, поставьте круизный переключатель (1) в положение OFF (рокерский переключатель в центральном положении).

Двигатель (двигатели) rpm будет медленно наклоняться к регулировке рычага дроссельной заслонки.

![[15200038.png]]

Для изменения параметров CRUISE 1 или CRUISE 2 по умолчанию:

1. При запуске двигателя выберите нужный вам круиз-настрой, установив переключатель круиз-контроля (1) на CRUISE 1 или CRUISE 2.
2. Переместить дроссель, как если двухдвигательный, в полное положение дроссельной заслонки во время движения, или на стыке с передачей в нейтральном положении. Двигатель будет **не** превышать существующую круизную установку. Например, если CRUISE 2 находится на заводской установке 1200 об/мин, двигатель **только** достигнет 1200 об/мин при полном дроссельном заслоне.
3. Используя переключатель RPM ± (2), настройте крейсерскую оборотную силу на новую желаемую скорость двигателя.

> [!note] Примечание
> Круизные скорости могут быть установлены между холостым и номинальным оборотом двигателя. Эта новая настройка будет сохранена до тех пор, пока круиз не будет откорректирован.

![[15200038.png]]

Медленный холостый

Функция SLOW-IDLE позволяет снизить скорость простоя для работы в «зонах без пробуждения». При активации функция SLOW-IDLE уменьшает скорость двигателя до запрограммированной скорости.

![[15200035.png]]

> [!note] Примечание
> Один переключатель управляет обоими двигателями на двухдвигательных судах.

Для использования функции SLOW-IDLE:

1. Судно должно быть в снаряжении.
2. Дроссель **должен** находиться в положении холостого хода.
3. Поместите выключатель SLOW-IDLE в положение ON (1), уплотнив верхнюю часть выключателя коромысла.

Двигатель (двигатели) холостого хода будет уменьшаться до запрограммированной скорости.

> [!note] Примечание
> Эта функция будет отключаться, когда двигатель выключен. Когда двигатель перезапускается, переключатель должен быть выключен, а затем снова включен, чтобы активировать функцию.

![[15200036.png]]

Чтобы отключить функцию SLOW-IDLE, поместите выключатель SLOW-IDLE в положение выключения (2), уплотнив нижнюю часть выключателя коромысла.

Двигатель (двигатели) будет настраиваться на установленную скорость холостого хода.

> [!note] Примечание
> Когда включен выключатель SLOW-IDLE, увеличение дроссельной заслонки временно отключит функцию SLOW-IDLE. Когда дросселя перемещается обратно в положение холостого хода, функция SLOW-IDLE автоматически включается снова.

![[15200037.png]]

Управление скоростью двигателя

Переключатель 2 управления скоростью двигателя (rpm ±) позволяет регулировать скорость холостого хода с шагом 25 об/мин, нажимая переключатель качения.

Нажатие на верхнюю часть переключателя увеличивает (+) обороты двигателя.

Нажатие на нижнюю часть выключателя уменьшает (-) обороты двигателя.

> [!note] Примечание
> Используйте медленные преднамеренные клики, чтобы увеличить или уменьшить обороты двигателя.

Когда RPM ± переключатель (2) используется с двигателем на холостом ходу, переключатель будет работать только * от 600 до 1000 об/мин.

> [!note] Примечание
> Переключатель ± RPM (2) будет **не** изменять скорость холостого хода, когда двигатель находится в режиме SLOW-IDLE.

Использование функции SLOW-IDLE деактивирует функцию RPM ±.

![[15200038.png]]

Если скорости двигателя между двумя двигателями **не** одинаковы, отрегулируйте оба двигателя до минимальной регулировки оборотов в минуту, 600 оборотов в минуту, путем подавления нижней (-) переключателя, пока оба двигателя не достигнут 600 оборотов в минуту.

Затем с помощью RPM ± переключателя (1), отрегулировать холостую к желаемой скорости, rpm.

> [!missing]- Иллюстрация `15200039.png` не извлечена — смотрите PDF-оригинал документа

Двухмоторные суда

Если двигатели работают с разной скоростью:

1. Настройка круиза на минимальную или максимальную настройку с помощью переключателя RPM ±.
2. Настройте круиз в желаемую настройку с помощью переключателя RPM ±.

> [!note] Примечание
> Если двигатель **не** достигнет номинальной оборотной силы, убедитесь, что функция морского круиз-контроля находится в положении OFF. Если функция морского круиз-контроля оставлена в положении CRUISE 1 или CRUISE 2, максимальная скорость двигателя будет ограничена заданной точкой положения, в котором находится круизный переключатель.

![[15200035.png]]


> [!quote]- Original (English) · английский оригинал
> ### Instrument Panel
>
> **Note · Примечание**
> The information below is written for engines equipped with an OEM supplied control system. For engines equipped with the Cummins Inc. supplied controls system, reference C Command Connect and Connect Premier Marine Panel System PS102 & PS103 Owners Manual Bulletin, [[5411481 — C Command Connect and Connect Premier Marine Panel System PS102, PS103 and PS108\|5411481]], or the Marine C Command HD Elite Panel System Owners Manual Bulletin, [[4332829 — Marine C Command HD Elite Panel System Owners Manual\|4332829]], for additional information.
>
> The control panel consists of the following:
>
> 1. Lubricating oil pressure gauge
> 2. Tachometer
> 3. Hourmeter
> 4. Engine coolant temperature gauge
> 5. Blank
> 6. Alarm reset button
> 7. Start push-button
> 8. Keyswitch
> 9. Alarm panel
> 10. Battery voltmeter.
>
> Oil Pressure Gauge
>
> The oil pressure gauge (1) shows the operating oil pressure of the engine.
>
> Tachometer w/Hour Meter
>
> The tachometer (2) shows the engine's crankshaft speed in revolutions per minute (rpm).
>
> The hour meter shows the numbers of hours of operation. This function is used for maintenance of the engine(s).
>
> Voltmeter
>
> The voltmeter (10) shows the battery voltage.
>
> Coolant Temperature Gauge
>
> The coolant temperature gauge (4) shows the temperature of the engine coolant during operation.
>
> ### Instrument Panel
>
> Electronic Governor Operation
>
> Turning the illumination control knob (4) will control the panel illumination and all switch panel backlighting.
>
> Turning the knob **clockwise** will decrease the illumination. Turning it **counterclockwise** will increase the illumination.
>
> ### Gauges
>
> All of the gauges, except the voltmeter (9), used with the engine are electronically driven. The gauges receive the reading from a high-speed datalink that is connected to the different sensors. If a gauge has no information from the datalink, it will slowly toggle between its high and low extremes.
>
> Oil Pressure Gauge
>
> The oil pressure gauge (2) shows the operating oil pressure of the engine.
>
> Tachometer w/Hour Meter
>
> The tachometer (3) shows the engine's crankshaft speed in revolutions per minute (rpm).
>
> The hour meter shows the numbers of hours of operation. This function is used for maintenance of the engine(s).
>
> Voltmeter
>
> The voltmeter (9) shows the battery voltage.
>
> Coolant Temperature Gauge
>
> The coolant temperature gauge (10) shows the temperature of the engine coolant during operation.
>
> ### Backup Throttle
>
> The optional backup throttle was designed to be used in the event of a main throttle failure.
>
> #### Backup Throttle Usage
>
> - Rotate the backup throttle knob **counterclockwise** to the idle position, or depress the knob to bring the engine to idle.
> - Put the main throttle lever in the idle position.
> - Move the backup throttle switch to the ON position.
> - Rotate the throttle knob **clockwise** to desired engine speed.
>
> The backup throttle switch has a safety latch feature; press the latch down and move the switch to the ON position. The throttle also has a friction adjustment collar. Rotate the collar **clockwise** to tighten, or **counterclockwise** to loosen, until the desired throttle tension is obtained.
>
> To turn the backup throttle off and to regain control of the engine speed using the main throttle lever:
>
> 1. Set the backup throttle to idle
> 2. Set the main throttle to idle
> 3. Put the backup throttle switch in the OFF position by depressing the bottom of the rocker switch
>
> ### Programmable Features
>
> An optional station select feature allows activation of electronic features from either a primary or secondary switch control panel.
>
> Engine Synchronization Switch
>
> **WARNING · Опасно**
> The engine synchronization feature must be turned off before docking or low-speed maneuvering; this allows full and separate control of each engine. Failure to turn off the engine synchronization feature can cause personal injury, damage to the vessel, and/or the dock.
>
> **Note · Примечание**
> The engine synchronization feature is an option available **only** on twin-engine vessels.
>
> The engine synchronization feature is used to electronically control the speed of both engines using one throttle lever.
>
> Normally the starboard throttle is used as the master engine throttle. The distributor or dealer can change it to the port throttle, if desired, by changing the master and slave plugs in the engine wiring. Refer to the installation manual.
>
> To use the engine synchronization feature:
>
> - Both engines **must** be in the same throttle position, running at the same rpm.
> - Put the ENG SYNC switch (1) in the ON position by depressing the top of the rocker switch.
>
> Both engines will adjust to the same rpm. The master throttle will control both engines.
>
> **Note · Примечание**
> This feature will deactivate when the engine is shut down. When the engine is restarted, the switch **must** be turned OFF then turned ON again to activate the feature.
>
> To turn the engine synchronization feature off:
>
> 1. Put the ENG SYNC switch (1) in the OFF position by depressing the bottom of the rocker switch.
> 2. Move either throttle lever to within 100 rpm of the other and the feature will deactivate. The throttle levers will now operate independently.
>
> Marine Cruise Control
>
> The marine cruise control feature provides two adjustable engine speeds. The cruise control can be used to run the engine(s) at the optimal cruise rpm or trolling rpm.
>
> CRUISE 1 has a default setting of 2100 rpm.
>
> CRUISE 2 has a default setting of 1200 rpm.
>
> **Note · Примечание**
> The marine cruise control feature can be used in conjunction with the engine synchronization feature.
>
> To activate the marine cruise control feature:
>
> 1. Put the cruise switch (1) in the desired position, CRUISE 1 or CRUISE 2.
> 2. Move the throttle(s) past the desired cruise speed.
>
> The engine(s) speed will increase to the cruise setting.
>
> **Note · Примечание**
> When using the engine synchronization feature, the master throttle is the **only** throttle that **must** be moved past the cruise point.
>
> To turn the marine cruise control off, put the cruise switch (1) in the OFF position (rocker switch in the center position).
>
> The engine(s) rpm will slowly ramp to the throttle lever setting.
>
> To change the CRUISE 1 or CRUISE 2 default setting rpm:
>
> 1. With the engine running, select the cruise setting that you want by setting cruise control switch (1) to CRUISE 1 or CRUISE 2.
> 2. Move the throttle, both if twin-engine, to the full throttle position while underway, or at the dock with the gear in neutral. The engine will **not** exceed the existing cruise setting. For example; if CRUISE 2 is at the factory setting of 1200 rpm, the engine will **only** reach 1200 rpm at full throttle.
> 3. Using the RPM ± switch (2), adjust the cruise rpm to the new desired engine speed.
>
> **Note · Примечание**
> The cruise speeds can be set between idle and rated engine speed. This new setting will be saved until the cruise is readjusted.
>
> Slow Idle
>
> The SLOW-IDLE feature allows for lower idle speed for operation in “No Wake Zones”. When activated, the SLOW-IDLE feature reduces the engine speed to a programmed speed.
>
> **Note · Примечание**
> A single switch controls both engines on twin engine vessels.
>
> To use the SLOW-IDLE feature:
>
> 1. The vessel **must** be in gear.
> 2. The throttle **must** be in the idle position.
> 3. Put the SLOW-IDLE switch in the ON position (1) by depressing the top of the rocker switch.
>
> The engine(s) idle will decrease to programmed speed.
>
> **Note · Примечание**
> This feature will deactivate when the engine is shut down. When the engine is restarted, the switch **must** be turned OFF then turned ON again to activate the feature.
>
> To turn the SLOW-IDLE feature off, put the SLOW-IDLE switch in the OFF position (2) by depressing the bottom of the rocker switch.
>
> The engine(s) will adjust to the idle set speed.
>
> **Note · Примечание**
> When the SLOW-IDLE switch is on, increasing the throttle will temporarily turn off the SLOW-IDLE feature. When the throttle is moved back into the idle position, the SLOW-IDLE feature will automatically turn itself ON again.
>
> Engine Speed Control
>
> The engine speed control (rpm ±) switch (2) allows the idle speed to be adjusted in 25-rpm increments by pressing the rocker switch.
>
> Pressing the top of the switch increases (+) engine rpm.
>
> Pressing the bottom of the switch decreases (-) engine rpm.
>
> **Note · Примечание**
> Use slow deliberate clicks to increase or decrease the engine rpm.
>
> When the RPM ± switch (2) is used with the engine at idle, the switch will **only** work from 600 to 1000 rpm.
>
> **Note · Примечание**
> The RPM ± switch (2) will **not** change the idle speed when the engine is in SLOW-IDLE mode.
>
> Use of the SLOW-IDLE feature will deactivate the RPM ± feature.
>
> If the engine speeds between the two engines are **not** the same, adjust both engines to the minimum rpm setting, 600 rpm, by depressing the bottom (-) of the switch until both engines are at 600 rpm.
>
> Then using the RPM ± switch (1), adjust the idle to the desired speed, rpm.
>
> Twin-Engine Vessels
>
> If the engines are running at different speeds:
>
> 1. Adjust the cruise to the minimum or maximum setting using the RPM ± switch.
> 2. Adjust the cruise to the desired setting using the RPM ± switch.
>
> **Note · Примечание**
> If an engine will **not** reach rated rpm, make sure the marine cruise control feature is in the OFF position. If the marine cruise control feature is left in the CRUISE 1 or CRUISE 2 position, maximum engine speed will be limited to the set point of the position that the cruise switch is in.
