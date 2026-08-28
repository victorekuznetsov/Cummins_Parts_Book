---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "10-101-007-om-ind"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2003-04-10"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666423"
figures: 42
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-101-007-om-ind.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-101-007-om-ind.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
  - "перевод/машинный"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `10-101-007-om-ind`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666423 — QSX15 Operation and Maintenance Manual|3666423]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2003-04-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-101-007-om-ind.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-101-007-om-ind.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Топливная система Signature/ISX представляет собой систему впрыска топлива с электронным управлением, которая оптимизирует экономию топлива и снижает выбросы выхлопных газов. Это делается путем управления крутящим моментом и кривой лошадиных сил, высокой скоростью двигателя, низким холостым ходом и скоростью дороги.

![[oi800v13.png]]

Signature/ISX имеет возможность управления приводом сцепления вентилятора, если используется сцепление вентилятора с электронным управлением.

Подпись/ISX также позволяет активировать тормоза двигателя, контролируя соленоиды тормоза двигателя.

Электронная функция, торможение двигателя с управлением вентилятором может быть включена для активации сцепления вентилятора во время торможения двигателя. Это увеличивает нагрузку на двигатель во время торможения двигателя.

![[17c00027.png]]

### Диагностические коды ошибок

Промышленное применение

Топливная система QSX15 может отображать и регистрировать определенные условия обнаружения неисправностей. Эти сбои отображаются в виде кодов неисправностей, что облегчает устранение неполадок. Коды неисправностей сохраняются в электронном модуле управления (ECM).

![[19400328.png]]

Существует два типа кодов неисправностей. Существуют коды неисправностей электронной топливной системы двигателя и коды неисправностей системы защиты двигателя.

Все коды ошибок, записанные в системе, будут либо активными (код ошибки в настоящее время активен в двигателе), либо неактивными (код ошибки был активен в какой-то момент, но в настоящее время активен не является).

| **Коды диагностики ошибок** |  |  |  |
|---|---|---|---|
| • Коды ошибок в системе электронного топлива |  |  |  |
| • Коды ошибок системы защиты двигателя. |  |  |  |

![[nobox.png]]

Активные коды неисправностей можно прочитать с помощью предупреждающих (янтарных) и стоп-сигналов (красных) в панели кабины или электронном сервисном оборудовании. Неактивные коды ошибок можно просматривать только с помощью электронного инструментария.

![[17c00177.png]]

Когда замок зажигания автомобиля включается и диагностический выключатель выключается, лампы с кодом неисправности (красный, желтый и техническое обслуживание) будут освещаться в течение примерно 2 секунд, одна за другой, чтобы проверить их работу.

![[19400331.png]]

Свет будет выключен до тех пор, пока не будет записан код неисправности. Если стоп (красный) свет включается во время работы двигателя, неисправность может привести к отключению двигателя. Остановите двигатель как можно скорее.

Если сигнальный (янтарный) свет горит, двигатель все еще может работать, но он может потерять некоторые системные функции, которые иногда могут привести к потере мощности. Неисправность должна быть исправлена, как только это удобно.

![[19400332.png]]

Система защиты двигателя записывает отдельные коды неисправностей, когда обнаруживается состояние вне зоны действия любого из датчиков в системе защиты двигателя. Защита двигателя доступна только тогда, когда включена функция защиты двигателя.

- Температура охлаждения
- Уровень охлаждающей жидкости
- Ввод многообразной температуры
- Масляное давление.

![[nobox.png]]

Система защиты двигателя будет зажигать лампу технического обслуживания (оранжевый), когда возникает состояние вне зоны действия.

> [!note] Примечание
> Цвета ламп и этикетки будут варьироваться в зависимости от OEM.

![[19400334.png]]

Если лампа технического обслуживания двигателя включается во время вождения, это означает, что был записан код неисправности. Свет будет гореть до тех пор, пока происходит ошибка.

Свет начнет мигать, если состояние продолжает ухудшаться. Мощность и/или скорость двигателя будут постепенно снижаться. Если функция защиты двигателя включена, двигатель отключится, чтобы предотвратить повреждение двигателя.

![[19400335.png]]

Для проверки активных кодов неисправностей сначала переключите переключатель зажигания транспортного средства в положение выключения. Переместить диагностический переключатель в положение ON.

> [!note] Примечание
> Некоторые OEM-производители используют шортинг-плагин.

![[19400336.png]]

Переключатель зажигания транспортного средства в положение Включения. Если не будет зарегистрировано активных кодов неисправностей, все три лампочки включатся и останутся включенными. Если активные коды неисправностей будут записаны, все три лампы будут включены на мгновение. Янтарные (предупреждающие) и красные (стоп) огни начнут мигать кодом зарегистрированной неисправности.

![[19400337.png]]

Код неисправности будет мигать в следующей последовательности. Во-первых, янтарная (предупредительная) лампа будет мигать. Затем будет короткая 1-секундная пауза, когда выключены как янтарный, так и красный свет. Затем номера записанного кода неисправности будут мигать красным цветом. Между каждым числом будет 1-секундная пауза. Когда число перестанет мигать, снова появится янтарный свет. Число будет повторяться в той же последовательности.

![[19400338.png]]

Светильники будут продолжать мигать по тому же коду, пока система не перейдет к следующему активному коду. Чтобы перейти ко второму коду неисправности, переместите переключатель настройки скорости холостого хода на «+», а затем отпустите его. Вы также можете вернуться к предыдущему коду ошибки, переместив переключатель на «-», а затем выпустив его. Чтобы проверить третий или четвертый код ошибки, переведите переключатель на «+», а затем выпустите его, когда все активные коды ошибок были просмотрены. Переключение переключателя на «+» будет возвращаться к первому коду ошибки.

Объяснение и исправление всех кодов неисправностей приведены в таблицах устранения неполадок руководства по топливу QSX15. См. Troubleshooting and Repair Manual, Electronic Control System, Signature, ISX and QSX15 Engines, Bulletin No. 3666259.

Электронный код неисправности деревьев находится в возрастающем численном порядке. Индекс находится в начале раздела.

![[19400339.png]]

Чтобы остановить диагностическую систему, переместить диагностический переключатель в положение OFF или удалить шортинг-розыгрыш. Переключатель зажигания транспортного средства в положение выключения.

> [!note] Примечание
> Некоторые OEM-производители используют шортинг-плагин.

![[gp8swvv.png]]

Код ошибки Snapshot Data

Когда диагностический код неисправности записывается в ECM, данные ввода и вывода ECM регистрируются со всех датчиков и коммутаторов. Данные снимка позволяют просматривать и использовать взаимосвязи между входами и выходами ECM во время устранения неполадок.

![[19400349.png]]

Генерация электроэнергии

Топливная система QSX15 может отображать и регистрировать определенные условия обнаружения неисправностей. Эти сбои отображаются в виде кодов неисправностей, что облегчает устранение неполадок. Коды неисправностей сохраняются в ECM.

Существует два типа диагностических кодов:

Информационные коды должны информировать оператора и электронную систему (параллельные контроллеры, интеллектуальные переключатели), что произошло событие.

Коды неисправностей должны сообщать оператору и электронной системе, что существует проблема или потенциальная проблема с двигателем или топливной системой.

![[19802544.png]]

Коды ошибок могут быть доступны тремя различными способами:

1. Флэш-на-выключателе
2. Инструмент электронного обслуживания
3. Панель интерфейса оператора.

![[nobox.png]]

Система управления приводом генератора ECM диагностические лампы

Система управления генераторным приводом ECM имеет пять светодиодов для диагностики. Типичные огни будут включать:

1. OS - Overspeed
2. LOP - низкое давление масла
3. Высокий температурный режим двигателя
4. Закрытие - Защита двигателя произошла
5. Предупреждение - состояние защиты двигателя существует.

![[19600091.png]]

Система управления генератором-драйвом Relay Drivers

Система управления генераторным приводом имеет семь ретрансляторов для реле, поставляемых клиентами.

- сверхскоростной
- Низкое давление масла
- Высокая температура двигателя
- Защита двигателя отключилась
- Предупреждение о защите двигателя существует
- Превышенное давление масла
- - высокая температура двигателя.

![[19600091.png]]

Fault Code Flash-out (перевод)

Чтобы «выбросить» код неисправности, ECM необходимо ввести в режим диагностики. Введите диагностический режим, удалив диагностический разъем, сокращающий вилку из жгута проводов двигателя, включив вилку и повторно включив ее, или используя диагностический переключатель режима.

Предупреждающая лампа будет мигать (означая начало нового кода неисправности), а затем код неисправности будет мигать на выключаемой лампе.

![[19600091.png]]

Коды ошибок - Инструменты электронного обслуживания

Инструменты электронного сервиса могут использоваться для считывания кодов неисправностей. Подключите персональный компьютер с установленной электронной сервисной оснасткой к двигателю с помощью служебной проводов жгута, номер детали. 3163156. См. руководство по инструменту электронного сервиса для подробностей о том, как использовать инструмент для показаний кодов ошибок.

![[19800902.png]]

Код ошибки - панель интерфейса оператора

Если клиент поставлял панель интерфейса оператора, она была интегрирована с системой управления приводом генератора с использованием шины данных RS485 CAN. Возможность отображения кодов неисправностей является одним из плюсов этой панели; обратитесь к руководствам, поставляемым с блоком для более подробной информации.

![[19800902.png]]

Код ошибки Snapshot Data

Когда диагностический код неисправности записывается в ECM, данные ввода и вывода ECM регистрируются со всех датчиков и переключателей. Данные снимка позволяют просматривать и использовать взаимосвязи между входами и выходами ECM во время устранения неполадок.

![[19800902.png]]

Чтобы очистить код ошибки

Неактивные коды неисправностей могут быть удалены. Существует два способа очистить неактивный код ошибки:

1. Переключатель сброса на панели интерфейса оператора
2. Инструменты электронного сервиса.

> [!note] Примечание
> Двигатель должен быть выключен для устранения неактивных неисправностей выключения.

Все коды ошибок, записанные в системе, будут либо активными (код ошибки в настоящее время активен в двигателе), либо неактивными (код ошибки был активен в какой-то момент, но в настоящее время активен не является).

![[19800902.png]]

### Система защиты двигателя

Двигатели QSX15 оснащены системой защиты двигателя. Система контролирует критические температуры и давления двигателя и регистрирует диагностические неисправности при ненормальном рабочем состоянии. Если существует вне зоны действия и должно быть инициировано действие по снижению скорости двигателя, оператор будет предупрежден предупреждающим светом в кабине. Предупреждающий свет мигает или мигает, когда условия вне зоны действия продолжают ухудшаться. Водитель должен тянуться к обочине дороги, когда это безопасно, чтобы уменьшить вероятность повреждения двигателя.

> [!note] Примечание
> Мощность и скорость двигателя будут постепенно снижаться в зависимости от уровня тяжести наблюдаемого состояния. Система защиты двигателя **не будет **выключать двигатель, если не выбрана функция отключения защиты двигателя. Если функция была выбрана и двигатель действительно выключен, двигатель можно запустить снова, выключив переключатель зажигания, а затем включив его обратно.

![[17c00028.png]]

### Описание топливной системы

Топливная система QSX15 с электронным управлением состоит из:

1. Клапан отсечки топлива
2. Датчик давления и температуры масла
3. Датчик давления и температуры впускного коллектора
4. Охлаждающая пластина (за ECM)
5. Электронный блок управления
6. Топливо в
7. Выгонять топливо
8. ECM Actuator Wiring Wring Port (только для промышленных предприятий)
9. ECM OEM проводка упряжка порта (только промышленное исполнение).

![[19c00617.png]]

Топливная система QSX15 с электронным управлением состоит из:

1. Датчик положения распределительного вала
2. Топливные приводы
3. Датчик атмосферного давления
4. Сроки работы актуаторов
5. Датчик давления топлива
6. Водный сепаратор
7. Датчик положения коленчатого вала
8. Передний и задний датчик давления
9. Датчик ограничения впуска топлива
10. Датчик уровня охлаждающей жидкости (в радиаторе) - опциональный.

Не в этом смысле.

Электронный модуль управления (ECM) Dataplate

промышленный

Тег данных для ECM расположен на передней части корпуса модуля.

![[17c00046.png]]

Генерация электроэнергии

Тег данных для ECM расположен на стороне ECM напротив разъемов ECM.

![[19802621.png]]

Вводы электронного модуля управления

Электронный модуль управления (ECM) Вводы:

1. Двигатель Camshaft или Crankshaft Position Sensor
2. Датчик положения дроссельной заслонки (промышленный **только**)
3. Idle Validation Switch (переключение)

![[19c00618.png]]

1. Датчик уровня охлаждения*
2. Датчик атмосферного давления
3. Датчик давления и температуры масла
4. Датчик давления в мокром резервуаре*
5. Непреднамеренный датчик топливной диагностики (только для промышленных целей)
6. Датчик давления топлива
7. Датчик воды в топливе (промышленный **только**).

Это датчики OEM, которые не установлены на двигателе.

![[19c00619.png]]

Датчики положения кулачка и коленчатого вала двигателя обеспечивают информацию о скорости двигателя и положении.

Датчик положения кулачка расположен между ECM и топливным насосом. Датчик положения коленчатого вала расположен ниже привода воздушного компрессора или заградительного устройства.

![[17c00050.png]]

Датчик положения дроссельной заслонки (промышленный **только**) расположен в педали дроссельной заслонки. Когда педаль стопы находится на холостом ходу, можно активировать тормоза двигателя. Когда педаль дроссельной заслонки находится в подавленном состоянии, датчик отключает тормоза двигателя и PTO. Педаль акселератора может переопределить круиз-контроль и PTO (если включено переопределение дроссельной заслонки в PTO).

![[en800kf.png]]

Переключатель проверки бездействия добавляется к педали дроссельной заслонки и проверяет, находится ли педаль дроссельной заслонки в положении с низким холостым ходом.

![[en800gf.png]]

Датчик давления/температуры впускного воздуха, расположенный в передней части впускного воздушного соединения, контролирует положительное давление коллектора и температуру впускного воздуха с турбонаддувом. Оба используются в функции управления топливом. Датчик давления/температуры впускного воздуха также используется в системе защиты двигателя.

![[17c00051.png]]

Датчик температуры охлаждающей жидкости двигателя, расположенный в корпусе термостата, контролирует температуру охлаждающей жидкости двигателя, используемую в функции управления топливом и системе защиты двигателя.

![[17c00053.png]]

Датчик уровня охлаждающей жидкости устанавливается в верхнем резервуаре радиатора или резервуаре для перенапряжения в зависимости от OEM. Это переключатель с жидкостным уровнем, необходимый для системы защиты двигателя.

> [!note] Примечание
> Это дополнительный датчик, который будет или не будет на всех транспортных средствах.

![[en800gd.png]]

Датчик давления окружающего воздуха расположен на стороне топливного насоса двигателя, чуть ниже ECM. Используется для контроля за топливом.

![[17c00054.png]]

Датчик давления/температуры масла, расположенный на стороне топливного насоса двигателя, контролирует давление и температуру моторного масла для системы защиты двигателя.

![[17c00055.png]]

Непреднамеренные датчики диагностики топлива, расположенные за топливными приводами на встроенном модуле топливной системы, контролируют давление прохождения топливного привода.

![[17c00143.png]]

Датчик давления топлива, расположенный на интегрированном модуле топливной системы, контролирует давление привода в рельсах питания.

![[17c00144.png]]

Датчик воды в топливе, расположенный на топливном фильтре, контролирует воду в топливе.

![[17c00145.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The Signature/ISX fuel system is an electronically controlled fuel injection system that optimizes fuel economy and reduces exhaust emissions. It does this by controlling the torque and horsepower curve, engine high speed, low idle, and road speed.
>
> Signature/ISX has the capability of controlling the fan clutch actuator if an electronically controlled fan clutch is used.
>
> Signature/ISX also allows the engine brakes to be activated by controlling the engine brake solenoids.
>
> The electronic feature, fan control engine braking can be enabled to activate the fan clutch during engine braking. This increases the load on the engine during engine braking.
>
> ### Diagnostic Fault Codes
>
> Industrial Applications
>
> The QSX15 fuel system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which make troubleshooting easier. The fault codes are retained in the electronic control module (ECM).
>
> There are two types of fault codes. There are engine electronic fuel system fault codes and engine protection system fault codes.
>
> All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at some time, but is **not** presently active).
>
> | **Diagnostic Fault Codes** |  |  |  |
> |---|---|---|---|
> | •Engine Electronic Fuel System Fault Codes |  |  |  |
> | •Engine Protection System Fault Codes. |  |  |  |
>
> Active fault codes can be read using the warning (amber) and stop lamps (red) in the cab panel or electronic service tool. Inactive fault codes can **only** be viewed with an electronic service tool.
>
> When the vehicle keyswitch is turned on and the diagnostic switch is off, the fault code lamps (red, yellow, and maintenance) will illuminate for approximately 2 seconds, one after the other, to check their operation.
>
> The lights will remain off until a fault code is recorded. If a stop (red) light comes on while the engine is in operation, the fault can be engine-disabling. Stop the engine in a safe manner as soon as possible.
>
> If the warning (amber) light illuminates, the engine can still be operated, but it can lose some system features that can sometimes result in a power loss. The failure **must** be repaired as soon as is convenient.
>
> The engine protection system records separate fault codes when an out-of-range condition is found for any of the sensors in the engine protection system. Engine protection is **only** available when the engine protection feature is enabled.
>
> - Coolant Temperature
> - Coolant Level
> - Intake Manifold Temperature
> - Oil Pressure.
>
> The engine protection system will light the maintenance lamp (orange) when an out-of-range condition occurs.
>
> **Note · Примечание**
> Lamp colors and labels will vary by OEM.
>
> If the engine protection maintenance lamp comes on while driving, it means that a fault code has been recorded. The light will remain on as long as the fault is occurring.
>
> The light will begin to flash if the condition continues to get worse. The engine power and/or speed will be gradually reduced. If the engine protection shutdown feature is enabled, the engine will shut down to prevent engine damage.
>
> To check for active fault codes, first turn the vehicle keyswitch to the OFF position. Move the diagnostic switch to the ON position.
>
> **Note · Примечание**
> Some OEMs use a shorting plug.
>
> Turn the vehicle keyswitch to the ON position. If no active fault codes are recorded, all three lights will come on and stay on. If active fault codes are recorded, all three lights will come on momentarily. The amber (warning) and red (stop) lights will begin to flash the code of the recorded fault.
>
> The fault code will flash in the following sequence. First, the amber (warning) lamp will flash. Then there will be a short 1-second pause when both the amber and red lights are off. Then the numbers of the recorded fault code will flash in red. There will be a 1-second pause between each number. When the number has stopped flashing, an amber light will appear again. The number will repeat in the same sequence.
>
> The lights will continue to flash the same fault code until the system has advanced to the next active fault code. To go to the second fault code, move the idle-speed adjust switch to “+,” then release it. You can also go back to the previous fault code by moving the switch to “-,” then releasing it. To check the third or fourth fault code, move the switch to “+,” then release it when all active fault codes have been viewed. Moving the switch to “+” will go back to the first fault code.
>
> The explanation and correction of all fault codes is in the troubleshooting charts of the QSX15 fuel manual. Refer to Troubleshooting and Repair Manual, Electronic Control System, Signature, ISX and QSX15 Engines, Bulletin No. 3666259.
>
> Electronic fault code troubleshooting trees are in ascending numerical order. An index is located at the beginning of the section.
>
> To stop the diagnostic system, move the diagnostic switch to the OFF position, or remove the shorting plug. Turn the vehicle keyswitch to the OFF position.
>
> **Note · Примечание**
> Some OEMs use a shorting plug.
>
> Fault Code Snapshot Data
>
> When a diagnostic fault code is recorded in the ECM, ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.
>
> Power Generation
>
> The QSX15 fuel system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which make troubleshooting easier. The fault codes are retained in the ECM.
>
> There are two types of diagnostic codes:
>
> Information codes are to inform the operator and electronic system (paralleling controllers, smart switch gear) that an event has occurred.
>
> Fault codes are to report to the operator and the electronic system that there is a problem or potential problem with the engine or fuel system.
>
> Fault codes can be accessed in three different ways:
>
> 1. Flash Out
> 2. Electronic Service Tool
> 3. Operator Interface Panel.
>
> Generator-Drive Control System ECM Diagnostic Lamps
>
> The generator-drive control system ECM has five LEDs for diagnostics. Typical lights will include:
>
> 1. OS - Overspeed
> 2. LOP - Low Oil Pressure
> 3. HET - High Engine Temperature
> 4. Shutdown - Engine Protection Shutdown Has Occurred
> 5. Warning - Engine Protection Warning Condition Exists.
>
> Generator-Drive Control System Relay Drivers
>
> The generator-drive control system has seven relay drivers for customer-supplied relays.
>
> - Overspeed
> - Low Oil Pressure
> - High Engine Temperature
> - Engine Protection Shutdown Has Occurred
> - Engine Protection Warning Condition Exists
> - Prelow Oil Pressure
> - Prehigh Engine Temperature.
>
> Fault Code Flash-out
>
> To “flash out” a fault code, the ECM **must** be put into the diagnostic mode. Enter the diagnostic mode by removing the diagnostic connector shorting the plug from the engine harness, turning the plug, and reinserting it, or using the diagnostic mode switch.
>
> The warning lamp will flash (signifying the start of a new fault code), and then the fault code will flash out on the shutdown lamp.
>
> Fault Codes - Electronic Service Tool
>
> The electronic service tool can be used to read the fault codes. Connect a personal computer, with the electronic service tool installed, to the engine using the service harness, Part No. 3163156. Refer to the electronic service tool manual for specifics about how to use the tool to read the fault codes.
>
> Fault Code - Operator Interface Panel
>
> If the customer supplied an operator interface panel, it has been integrated with the generator-drive control system using the RS485 datalink. The ability to display fault codes is one plus of this panel; refer to the manuals supplied with the unit for more details.
>
> Fault Code Snapshot Data\\
>
> When a diagnostic fault code is recorded in the ECM, the ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.
>
> To Clear a Fault Code
>
> **Only** inactive fault codes can be cleared. There are two ways to clear an inactive fault code:
>
> 1. The reset switch on the operator interface panel
> 2. The electronic service tool.
>
> **Note · Примечание**
> The engine **must** be shut down to clear inactive shutdown faults.
>
> All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at some time, but is **not** presently active).
>
> ### Engine Protection System
>
> QSX15 engines are equipped with an engine protection system. The system monitors critical engine temperatures and pressures and will log diagnostic faults when an abnormal operating condition occurs. If an out-of-range condition exists and engine derate action is to be initiated, the operator will be alerted by an in-cab warning light. The warning light will blink or flash when out-of-range conditions continue to worsen. The driver **must** pull to the side of the road, when it is safe to do so, to reduce the possibility of engine damage.
>
> **Note · Примечание**
> Engine power and speed will be gradually reduced, depending on the level of severity of the observed condition. The engine protection system will **not** shut down the engine unless the engine protection shutdown feature has been selected. If the feature has been selected and the engine does shut down, the engine can be started again by turning off the keyswitch and then turning it back on.
>
> ### Fuel System Description
>
> The QSX15 electronically controlled fuel system consists of:
>
> 1. Fuel shutoff valve
> 2. Oil pressure/temperature sensor
> 3. Intake manifold pressure/temperature sensor
> 4. Cooling plate (behind ECM)
> 5. Electronic control module
> 6. Fuel in
> 7. Fuel out
> 8. ECM actuator harness port (industrial only)
> 9. ECM OEM harness port (industrial only).
>
> The QSX15 electronically controlled fuel system consists of:
>
> 1. Camshaft Position Sensor
> 2. Fueling Actuators
> 3. Ambient Air Pressure Sensor
> 4. Timing Actuators
> 5. Fuel Pressure Sensor
> 6. Water-in-Fuel Separator
> 7. Crankshaft Position Sensor
> 8. Front and Rear Rail Pressure Sensor
> 9. Fuel Inlet Restriction Sensor
> 10. Coolant Level Sensor (In Radiator) - Optional\*.
>
> \* Not in this view.
>
> Electronic Control Module (ECM) Dataplate
>
> Industrial
>
> The data tag for the ECM is located on the front of the module housing.
>
> Power Generation
>
> The data tag for the ECM is located on the side of the ECM opposite the ECM connectors.
>
> Electronic Control Module Inputs
>
> Electronic Control Module (ECM) Inputs:
>
> 1. Engine Camshaft or Crankshaft Position Sensor
> 2. Throttle Position Sensor (industrial **only**)\*
> 3. Idle Validation Switch\*
>
> 1. Coolant Level Sensor\*
> 2. Ambient Air Pressure Sensor
> 3. Oil Pressure/Temperature Sensor
> 4. Wet Tank Pressure Sensor\*
> 5. Unintended Fuel Diagnostic Sensor (industrial **only**)
> 6. Fuel Pressure Sensor
> 7. Water-in-Fuel Sensor (industrial **only**).
>
> \*These are OEM sensors that are **not** installed on the engine.
>
> The engine cam and crank position sensors provide engine speed and position information.
>
> The cam position sensor is located between the ECM and fuel pump. The crank position sensor is located below the air compressor drive or the barring device.
>
> The throttle position sensor (industrial **only**) is located in the throttle foot pedal assembly. When the foot pedal is at idle, the engine brakes can be activated. When the throttle pedal is depressed, the sensor deactivates the engine brakes and the PTO. The accelerator pedal can override the cruise control and PTO (if the throttle override in PTO is enabled).
>
> The idle validation switch is added to the throttle pedal assembly and will verify that the throttle pedal is in the low-idle position.
>
> The intake air pressure/temperature sensor, located in the front of the intake air connection, monitors positive manifold pressure and turbocharged intake air temperature. Both are used in the fuel control function. The intake air pressure/temperature sensor is also used in the engine protection system.
>
> The engine coolant temperature sensor, located in the thermostat housing, monitors engine coolant temperature used in the fuel control function and engine protection system.
>
> The coolant level sensor is mounted in the radiator top tank or surge tank, depending on the OEM. It is a fluid-level-actuated switch required for the engine protection system.
>
> **Note · Примечание**
> This is an optional sensor that will or will **not** be on all vehicles.
>
> The ambient air pressure sensor is located on the fuel pump side of the engine, just below the ECM. It is used to control fueling.
>
> The oil pressure/temperature sensor, located on the fuel pump side of the engine, monitors lubricating oil pressure and temperature for the engine protection system.
>
> The unintended fuel diagnostic sensors, located behind the fuel actuators on the integrated fuel system module, monitor the fuel actuator's passage pressure.
>
> The fuel pressure sensor, located on the integrated fuel system module, monitors actuator supply rail pressure.
>
> The water-in-fuel sensor, located on the fuel filter, monitors water in fuel.
