---
aliases:
  - "Обкатка двигателя (на моторном стенде)"
type: "Процедура"
doc: "89-014-006"
title_en: "Engine Run-in (Engine Dynamometer)"
title_ru: "Обкатка двигателя (на моторном стенде)"
modified: "2006-06-26"
engines:
  - "85017333"
families:
  - "QSK23"
manuals:
  - "4021375"
figures: 34
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-014-006.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-014-006.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
  - "перевод/машинный"
---

# Engine Run-in (Engine Dynamometer)
**Обкатка двигателя (на моторном стенде)**

> [!abstract] Процедура · `89-014-006`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2006-06-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-014-006.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-014-006.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

В настоящем документе предусмотрены процедуры использования системы управления двигателем, номер детали 3163890. Управление двигателем представляет собой портативное, портативное электронное управление, используемое для запуска и управления скоростью двигателя на следующих семействах электронных двигателей Cummins®. Он заменяет педаль дроссельной заслонки, панель интерфейса водителя и схемы мониторинга кода неисправности. Управление двигателем имеет положение шины данных CAN для подключения к электронному сервисному инструменту для мониторинга работы двигателя и кодов неисправностей. Рулевая проводка двигателя, необходимая для двигателей, приобретается отдельно. Усилители управления двигателем и проводов управления двигателем предназначены для использования как с (+) 12-VDC, так и с (+) 24-VDC аккумуляторными системами.

> [!note] Примечание
> Управление двигателем может быть использовано на двигателях с частотной калибровкой дроссельной заслонки путем первой загрузки линейной калибровки дроссельной заслонки в электронный модуль управления (ECM). После завершения тестирования/ремонта перезагрузите правильную калибровку частоты дроссельной заслонки.

![[ck800wa.png]]

### Установка

> [!warning] ОСТОРОЖНО
> Система моторного масла должна быть заряжена перед работой двигателя после реконструкции, чтобы избежать повреждения внутренних компонентов. Не загружайте систему из обходного фильтра, так как фильтр будет поврежден.

Удалите большую пробку из масляной винты.

![[14400032.png]]

Используйте насос, способный подавать 205 кПа \[30 psi\] непрерывного давления.

Подключите насос к масляной винте, как показано.

Используйте запас чистого моторного масла 15W-40.

Поверните насос в положение ON.

Проверьте датчик давления масла в двигателе. Когда калибр указывает на давление масла, начните мониторинг уровня масла в масляной кастрюле.

![[14400033.png]]

Проверьте уровень моторного масла двигателя, чтобы убедиться, что оно заполнено до нужного уровня.

![[oi8dsva.png]]

> [!danger] ОПАСНО
> Не снимайте пробку радиатора с горячего двигателя. Снимайте пробку радиатора только после того, как температура охлаждающей жидкости опустится ниже 50 °C \[120 °F\]. Струя горячей охлаждающей жидкости или пар могут привести к травме.

Проверьте уровень охлаждающей жидкости двигателя, чтобы убедиться, что он заполнен до надлежащего уровня. См. процедуру 008-018.

![[ra200sa.png]]

Используйте известный источник дизельного топлива хорошего качества № 2.

Это очень важно, поскольку дизельное топливо № 1, наряду с большинством других альтернативных видов топлива, легче (более низкая удельная гравитация, более высокая гравитация API), чем дизельное топливо № 2. Чем легче топливо, тем ниже содержание энергии (BTU на галлон (литр и т.д.).)

![[ck800wa.png]]

Двигатель Throttle Control

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Для уменьшения возможности дуги сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Отключите кабели аккумулятора перед началом следующей процедуры.

Отсоедините электропроводку OEM от электронного модуля управления (ECM) (если применимо).

![[22c00141.png]]

Отсоедините проводные упряжки OEM 21-контактный и 31-контактный разъемы Deutsch от электропроводки двигателя.

Подключите к проводах управления двигателем жгут № 3163891.

Подключите к ремню 21-контактную и 31-контактную проводку управления двигателем к ремню электропроводки двигателя.

![[19a00768.png]]

> [!note] Примечание
> Если для подключения управления двигателем требуется дополнительная длина кабеля, используйте электрический кабель, номер детали 3163895.

Подключите проводку управления двигателем (2) к управлению двигателем. Электронный инструмент, оснащенный персональным компьютером INSITETM, может использоваться для мониторинга цепей для правильной работы. Подключите комплект адаптера шины данных INLINETM5 CAN (3), Номер детали 4918416 и персональный компьютер к разъему шины данных CAN управления двигателем.

![[22c00125.png]]

Двигатели, которые работают на динамометре двигателя, требуют установки и подключения к двигателю электропроводки. Кроме того, двигатель, номер детали 3163890, должен быть использован для правильного управления двигателем во время работы динамометра.

![[wr8coac.png]]

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

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Подключите питание от батареи к стартеру.

Подключите динамометр теста OEM-проводов ремня стартера соленоидного свинца (желтого цвета) к стартерному соленоиду. Подключите грунтовый свинец (черный) к стартеру соленоида. Подключите заземляющий свинец (черный) к стартеру или аккумулятору отрицательной (-) или стороне земли. Подключите (+) 12 VDC power lead (красный) к стартеру или аккумулятору с положительной (+) стороной 12 VDC.

![[sb8coma.png]]

Вращайте ручку дроссельной заслонки полностью **против часовой стрелки**. Нажмите на ручку дроссельной заслонки, чтобы вернуть дроссель в положение холостого хода.

Повторите этот шаг три раза.

Переключатель зажигания в положение выключения в течение 30 секунд.

![[22c00156.png]]

> [!warning] ОСТОРОЖНО
> Проверьте уровень охлаждающей жидкости и моторного масла перед запуском и работой двигателя. Если охлаждающая жидкость и моторное масло не находятся на должном уровне, может возникнуть повреждение двигателя.

Включите переключатель зажигания в положение START до запуска двигателя и отпустите переключатель зажигания.

![[22c00129.png]]

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

> [!note] Примечание
> Некоторые двигатели оснащены фитингами, используемыми для датчиков тестирования Compucheck®. Датчики, используемые для тестирования Compucheck® и динамометра, не совместимы. Если используется одно и то же место, удалите установку Compucheck® и установите адаптеры для датчика динамометра.

Установите датчик давления охлаждающей жидкости (1).

Установите датчик температуры охлаждающей жидкости (2).

![[19400310.png]]

Возврат параметров к их первоначальному значению, когда тест или запуск завершены.

Подключите панель переключателя зажигания CAN кабеля шины данных к электронному сервисному инструменту Cummins.

Используйте инструмент электронного обслуживания INSITETM для настройки двигателя для динамометра. См. процедуру[[89-014-008 — Engine Testing (In Chassis)|014-008]]Для получения дополнительной информации об этой функции.

Настройка теперь завершена, и для управления скоростью двигателя можно использовать автоматическое / ручное дроссельное заслонки.

![[14c00040.png]]

Технические характеристики двигателя доступны в местных авторизованных местах ремонта Cummins.

![[lt800ga.png]]

### Запуск инструкций

См. Тестирование двигателя - Динамометр двигателя, Процедура[[89-014-005 — Engine Testing (Engine Dynamometer)|014-005]]Для общих операционных процедур и мер безопасности.

![[ck800wa.png]]

Используйте следующую диаграмму для определения испытательной нагрузки.

Испытание на включение **должно** проводиться с двигателем, работающим на пике крутящего момента оборотов в минуту. См. диаграммы производительности, доступные через Cummins Inc.

| RPM Rating RPM | Пик момента |
|---|---|
| 2100 | 1300 |
| 2100 | 1400 |

> [!warning] ОСТОРОЖНО
> Не проворачивайте пусковой двигатель более 30 секунд. Избыточное тепло повредит стартер.

> [!warning] ОСТОРОЖНО
> Если давление масла не соответствует спецификациям, немедленно остановите двигатель. Низкое и высокое давление масла может привести к повреждению двигателя.

Запускай двигатель. Если двигатель не работает через 30 секунд, дайте две минуты, чтобы двигатель остыл.

| каша |  | пси |
|---|---|---|
| 70 | Мин | 10 |

![[oi800vi.png]]

> [!warning] ОСТОРОЖНО
> Не работайте с двигателем на холостом ходу дольше, чем указано. Чрезмерное образование углерода приведет к повреждению двигателя.

Управляйте двигателем в положении холостого хода и проверяйте наличие утечек.

![[oi800vj.png]]

Настройка двигателя rpm до 1200 rpm. Нагрузка динамометра должна быть отрегулирована до испытательной нагрузки, как определено ранее. Работайте с двигателем при этой установке до тех пор, пока температура охлаждающей жидкости не покажет 70°C[160°F].

Проверьте и исправьте все утечки.

Проверьте все датчики и запишите показания.

**Не** переходите к следующему шагу, пока продувка не станет стабильной в пределах спецификаций.

![[oi800vk.png]]

Настройка оборотов двигателя на пиковый крутящий момент оборотов. Нагрузка динамометра должна быть в два раза больше испытательной нагрузки. Управляйте двигателем в течение двух минут.

Проверьте все датчики и запишите показания.

**Не** переходите к следующему шагу, пока продувка не станет стабильной в пределах спецификаций.

![[oi800vl.png]]

Поддерживайте обороты двигателя на пике крутящего момента оборотов в минуту. Увеличить нагрузку на динамометр до трехкратной испытательной нагрузки.

Работайте с двигателем при этой нагрузке в течение двух минут.

Проверьте все датчики и запишите показания.

**Не** переходите к следующему шагу, пока продувка не станет стабильной в пределах спецификаций.

![[oi800vm.png]]

Переместить рычаг дроссельной заслонки в полностью открытое положение. Увеличьте нагрузку до тех пор, пока обороты двигателя не достигнут пикового крутящего момента оборотов в минуту.

Работайте с двигателем в этой установке в течение 10 минут или до тех пор, пока продувка не станет стабильной в соответствии со спецификациями.

Проверьте все датчики и запишите показания.

![[oi800vn.png]]

Уменьшите нагрузку на динамометр до тех пор, пока обороты двигателя не увеличатся до номинального оборота.

Работайте с двигателем при этой нагрузке в течение пяти минут.

Проверьте все датчики и запишите показания.

![[oi800vo.png]]

> [!warning] ОСТОРОЖНО
> Не выключайте двигатель немедленно. Двигатель должен быть охлажден.

> [!warning] ОСТОРОЖНО
> Не работайте с двигателем на холостом ходу дольше, чем указано. Чрезмерное образование углерода может привести к повреждению двигателя.

Полностью снизить нагрузку на динамометр.

Переместить рычаг дроссельной заслонки в низкое положение холостого хода. Работайте с двигателем в этой установке в течение трех-пяти минут. Это позволит охладить турбокомпрессор и другие компоненты двигателя.

![[oi800vj.png]]

Выключи двигатель.

![[oi800vp.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> This document provides procedures for the use of an engine control, Part Number 3163890. The engine control is a portable, handheld electronic control, used to start and control engine speed on the following Cummins® electronic engine families. It replaces the throttle pedal, driver interface panel, and fault code monitoring circuits. The engine control has a datalink provision to connect to an electronic service tool to monitor engine operation and fault codes. The engine control harnesses required for the engines are purchased separately. The engine control and engine control harnesses are designed to be used with both (+) 12-VDC and (+) 24-VDC battery systems.
>
> **Note · Примечание**
> The engine control can be used on engines with frequency throttle calibrations by first downloading a linear throttle calibration to the electronic control module (ECM). After the testing/repair is complete, reload the correct frequency throttle calibration.
>
> ### Install
>
> **CAUTION · Осторожно**
> The lubricating oil system must be primed before operating the engine after rebuild to avoid internal component damage. Do not prime the system from the bypass filter as the filter will be damaged.
>
> Remove the large plug from the oil cooler rifle.
>
> Use a pump capable of supplying 205 kPa \[30 psi\] continuous pressure.
>
> Connect the pump to the oil cooler rifle, as shown.
>
> Use a supply of clean 15W-40 engine oil.
>
> Turn the pump to the ON position.
>
> Check the engine oil pressure gauge. When the gauge indicates oil pressure, begin monitoring the oil level in the oil pan.
>
> Check the engine lubricating oil level to be sure it is filled to the proper level.
>
> **WARNING · Опасно**
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.
>
> Check the engine coolant level to make sure it is filled to the proper level. Refer to Procedure 008-018.
>
> Use a known source of good quality number 2 diesel fuel.
>
> This is very important since number 1 diesel fuels, along with most other alternate fuels, are lighter (lower specific gravity, higher API gravity) than number 2 diesel fuels. The lighter the fuel, the lower the energy content (BTU per gallon (liter, etc.).
>
> Engine Throttle Control
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
> Connect the engine control harness Part Number 3163891.
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
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Connect battery power to the starter.
>
> Connect the dynamometer test OEM wiring harness starter solenoid lead (yellow) to the starter solenoid. Connect the ground lead (black) to the starter solenoid. Connect the ground lead (black) to the starter or battery negative (-) or ground side. Connect the (+) 12 VDC power lead (red) to either the starter or battery positive (+) 12 VDC side.
>
> Rotate the throttle knob fully **counterclockwise**. Push down on the throttle knob to return the throttle to the idle position.
>
> Repeat this step three times.
>
> Turn the keyswitch to the OFF position for 30 seconds.
>
> **CAUTION · Осторожно**
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level engine damage can result.
>
> Turn the keyswitch to the START position until the engine starts and release the keyswitch.
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
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level engine damage can result.
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
> **Note · Примечание**
> Some engines are equipped with fittings used for Compucheck® testing sensors. The sensor probes used for Compucheck® and dynamometer testing are **not** compatible. If the same location is used, remove the Compucheck® fitting and install adapters for the dynamometer sensor.
>
> Install the coolant pressure sensor (1).
>
> Install the coolant temperature sensor (2).
>
> Return parameters to their original value when the test or run-in is complete.
>
> Connect the keyswitch panel datalink cable to the Cummins electronic service tool.
>
> Use INSITE™ electronic service tool to set the engine up for the dynamometer. Refer to Procedure [[89-014-008 — Engine Testing (In Chassis)|014-008]] for more information on this feature.
>
> The setup is now complete, and the auto/manual throttle can be used to control engine speed.
>
> Engine operating specifications are available from local Cummins authorized repair locations.
>
> ### Run-In Instructions
>
> See the Engine Testing - Engine Dynamometer, Procedure [[89-014-005 — Engine Testing (Engine Dynamometer)|014-005]], for general operating procedures and safety precautions.
>
> Use the following chart to determine the test load.
>
> The run-in test **must** be performed with the engine operating at torque peak rpm. See the performance charts available through Cummins Inc.
>
> | Rated RPM | Torque Peak |
> |---|---|
> | 2100 | 1300 |
> | 2100 | 1400 |
>
> **CAUTION · Осторожно**
> Do not crank the starting motor for more than 30 seconds. Excessive heat will damage the starter.
>
> **CAUTION · Осторожно**
> If the oil pressure is not within specifications, stop the engine immediately. Both low and high oil pressure will cause engine damage.
>
> Start the engine. If the engine does **not** begin operating after 30 seconds, allow two minutes for the starter motor to cool.
>
> | kpa |  | psi |
> |---|---|---|
> | 70 | MIN | 10 |
>
> **CAUTION · Осторожно**
> Do not operate the engine at idle longer than specified. Excessive carbon formation will cause engine damage.
>
> Operate the engine in the idle position and check for leaks.
>
> Adjust the engine rpm to 1200 rpm. Adjust the dynamometer load to the test load as previously determined. Operate the engine at this setting until the coolant temperature indicates 70°C \[160°F\].
>
> Check for and fix all leaks.
>
> Check all gauges and record the readings.
>
> Do **not** proceed to the next step until the blowby becomes stable within specifications.
>
> Adjust the engine rpm to the torque peak rpm. Adjust the dynamometer load to equal two times the test load. Operate the engine for two minutes.
>
> Check all gauges and record the readings.
>
> Do **not** proceed to the next step until the blowby becomes stable within specifications.
>
> Maintain the engine rpm at torque peak rpm. Increase the dynamometer load to equal three times the test load.
>
> Operate the engine at this load for two minutes.
>
> Check all gauges and record the readings.
>
> Do **not** proceed to the next step until the blowby becomes stable within specifications.
>
> Move the throttle lever to the full open position. Increase the load until the engine rpm is at torque peak rpm.
>
> Operate the engine at this setting for 10 minutes or until the blowby becomes stable within specifications.
>
> Check all gauges and record the readings.
>
> Decrease the dynamometer load until the engine rpm increases to the rated rpm.
>
> Operate the engine at this load for five minutes.
>
> Check all gauges and record the readings.
>
> **CAUTION · Осторожно**
> Do not turn the engine off immediately. The engine must be allowed to cool.
>
> **CAUTION · Осторожно**
> Do not operate the engine at idle longer than specified. Excessive carbon formation can cause engine damage.
>
> Decrease the dynamometer load completely.
>
> Move the throttle lever to the low idle position. Operate the engine at this setting for three to five minutes. This will allow the turbocharger and the other engine components to cool.
>
> Turn the engine off.
