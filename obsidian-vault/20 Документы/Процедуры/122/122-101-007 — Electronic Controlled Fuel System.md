---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "122-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2015-04-14"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "4022102"
figures: 14
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `122-101-007`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2015-04-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-101-007.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Описание системы QSK

Топливная система QSK представляет собой электронную систему управления двигателем, предназначенную для оптимизации управления двигателем и снижения выбросов выхлопных газов. Топливная система QSK управляет скоростью двигателя и давлением топлива на основе ввода от электрического дроссельного заслонка и других специфических для оборудования и/или модели особенностей.

![[19400349.png]]

### Диагностические коды ошибок

Топливная система QSK может отображать и регистрировать определенные условия обнаружения неисправностей. Эти неисправности отображаются в виде кодов неисправностей, что облегчает устранение неполадок. Коды неисправностей сохраняются в модуле управления двигателем (ECM).

![[19400328.png]]

Существует два типа кодов неисправностей:

- Коды неисправностей в электронной топливной системе двигателя
- Коды неисправностей системы защиты двигателя.

Все коды ошибок, записанные в системе, будут либо активными (код ошибки в настоящее время активен в двигателе), либо неактивными (код ошибки был активен в одно время, но не был активен в данный момент).

Активные коды неисправностей можно прочитать с помощью предупреждающих (янтарных) и останавливающих ламп (красных) в панели кабины или инструментария электронного обслуживания INSITETM.

Неактивные коды ошибок могут быть просмотрены только с помощью инструментария электронного обслуживания INSITETM.

![[19400330.png]]

Когда замок зажигания транспортного средства включается и диагностический выключатель выключается, огни с кодом неисправности (красный, янтарный и защита двигателя) будут освещаться в течение примерно 2 секунд, одна за другой, чтобы проверить их работу.

![[19400331.png]]

Свет будет оставаться выключенным до тех пор, пока не будет записан код неисправности. Если во время работы двигателя включен стоп (красный) свет, неисправность может отключить двигатель. Запретите двигатель как можно скорее.

Если свет янтарного цвета освещается, двигатель все еще может работать, но он может потерять некоторые системные функции, которые иногда могут привести к потере мощности. Неисправность должна быть исправлена как можно скорее.

![[19400332.png]]

Система защиты двигателя записывает отдельные коды неисправностей, когда обнаруживается состояние вне зоны действия любого из датчиков в системе защиты двигателя.

Ниже приведены коды неисправностей системы защиты двигателя вне зоны действия:

1. Температура охлаждающей жидкости
2. Уровень охлаждения (необязательно)
3. Давление масла.

![[19400328.png]]

> [!note] Примечание
> Цвета ламп и этикетки варьируются в зависимости от производителя оригинального оборудования (OEM).

Система защиты двигателя будет зажигать лампу технического обслуживания (оранжевую), когда возникает состояние вне зоны действия.

![[19400334.png]]

Если во время вождения включается жидкостная лампа системы защиты двигателя, это означает, что был записан код неисправности. Свет будет гореть до тех пор, пока происходит ошибка.

Свет начнет мигать, если состояние продолжает ухудшаться. Мощность и/или скорость двигателя будут постепенно снижаться. Если функция защиты двигателя включена, двигатель отключится, чтобы предотвратить повреждение двигателя.

![[19400335.png]]

> [!note] Примечание
> Некоторые OEM-производители используют шортинг-плагин.

Для проверки активных кодов неисправностей переключатель зажигания транспортного средства переключается в положение выключения и переключатель диагностики переключается в положение Включения.

![[19400336.png]]

Переключатель зажигания транспортного средства в положение Включения. Если не будет зарегистрировано активных кодов неисправностей, все три лампочки включатся и останутся включенными. Если активные коды неисправностей будут записаны, все три лампы будут включены на мгновение. Янтарный (ПРЕДУПРЕЖДЕНИЕ) и красный (СТОП) огни начнут мигать кодом зарегистрированного неисправности.

![[19400337.png]]

Код неисправности будет мигать в следующей последовательности: Во-первых, янтарная лампа (предупреждение) будет мигать. Затем будет короткая, 1 секундная пауза, когда желтый и красный свет выключены. Затем номера записанного кода неисправности будут мигать красным цветом. Между каждым числом будет 1 секунда паузы. Когда число будет сверкать, снова появится янтарный свет. Число будет повторяться в той же последовательности.

![[19400338.png]]

Светильники будут продолжать мигать по тому же коду неисправности, пока система не будет переведена на следующий активный код неисправности.

Чтобы перейти ко второму коду неисправности, переведите переключатель настройки скорости холостого хода на «+», затем отпустите. Вы также можете вернуться к предыдущему коду неисправности, переместив переключатель на «-», а затем выпустив. Чтобы проверить третий или четвертый код ошибки, переведите переключатель на «+», а затем выпустите его, когда все активные коды ошибок были просмотрены.

Переключение переключателя на «+» будет возвращаться к первому коду ошибки. Краткое объяснение всех кодов неисправностей приведено в разделе TF настоящего руководства.

![[19400339.png]]

> [!note] Примечание
> Некоторые OEM-производители используют шортинг-плагин.

Чтобы остановить диагностическую систему, переведите диагностический переключатель в положение OFF или удалите шортинг-розыгрыш. Переключатель зажигания транспортного средства в положение выключения.

![[gp8swvv.png]]

### Код ошибки Snapshot Data

Когда диагностический код неисправности записывается в ECM, данные ввода и вывода ECM регистрируются со всех датчиков и переключателей. Данные снимка позволяют просматривать и использовать взаимосвязи между входами и выходами ECM во время устранения неполадок.

Данные снимка кода ошибки могут быть просмотрены только с помощью инструментария электронного обслуживания INSITETM.

![[19400349.png]]

### Система защиты двигателя

Двигатели топливной системы QSK оснащены системой защиты двигателя. Система контролирует критические температуры двигателя, уровень жидкости, положение переключателя и давление и регистрирует диагностические неисправности, когда происходит превышение или при нормальном рабочем диапазоне. Если существует вне диапазона, может быть инициировано действие разрушителя двигателя. Оператор будет предупрежден о освещении лампы технического обслуживания в кабине. Предупреждающая лампа начнет мигать, когда состояние вне зоны действия будет ухудшаться, и произойдет отключение двигателя. Оператор должен тянуться к обочине дороги, когда это безопасно, чтобы уменьшить вероятность повреждения двигателя.

#### Система защиты двигателя мониторы:

- Температура охлаждающей жидкости
- Уровень охлаждения (необязательно)
- температура коллектора
- Давление масла.

#### Система защиты двигателя мониторы для:

- Высокая температура охлаждающей жидкости
- Низкий уровень охлаждающей жидкости (необязательно)
- Высокая температура коллектора впуска
- Низкое/очень низкое давление масла.

Система защиты двигателя может иметь две выбираемые функции: Включается защита двигателя и отключение защиты двигателя. Если функция защиты двигателя выбрана, мощность и скорость двигателя постепенно снижаются в зависимости от уровня тяжести наблюдаемого состояния. Если выберите функцию отключения защиты двигателя, двигатель отключится. Двигатель можно перезапустить, выключив переключатель зажигания, а затем включив его обратно.

#### Особенности защиты двигателя:

- Защита двигателя позволяет
- Защита двигателя отключена.


> [!quote]- Original (English) · английский оригинал
> ### QSK System Description
>
> The QSK fuel system is an electronic engine control system designed to optimize engine control and reduce exhaust emissions. The QSK fuel system controls engine speed and fuel pressure based on input from the electric throttle and other equipment-specific and/or model-specific features.
>
> ### Diagnostic Fault Codes
>
> The QSK fuel system can display and record certain detectable fault conditions. These malfunctions are displayed as fault codes, which makes troubleshooting easier. The fault codes are retained in the engine control module (ECM).
>
> There are two types of fault codes:
>
> - Engine electronic fuel system fault codes
> - Engine protection system fault codes.
>
> All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at one time, but **not** at the moment).
>
> Active fault codes can be read using the WARNING (amber) and STOP lamps (red) in the cab panel or INSITE™ electronic service tool.
>
> Inactive fault codes can **only** be viewed with INSITE™ electronic service tool.
>
> When the vehicle keyswitch is turned ON and the diagnostic switch OFF, the fault code lamps (red, amber, and engine protection) will illuminate for approximately 2 seconds, one after another, to check their operation.
>
> The lights will remain OFF until a fault code is recorded. If a STOP (red) light comes on while the engine is in operation, the fault can disable the engine. STOP the engine in a safe manner as soon as possible.
>
> If the WARNING (amber) light illuminates, the engine can still be operated, but it can lose some system features that can sometimes result in a power loss. The malfunction **must** be corrected as soon as possible.
>
> The engine protection system records separate fault codes when an out-of-range condition is found for any of the sensors in the engine protection system.
>
> The following are engine protection system out-of-range fault codes:
>
> 1. Coolant temperature
> 2. Coolant level (optional)
> 3. Oil pressure.
>
> **Note · Примечание**
> Lamp colors and labels vary by the original equipment manufacturer (OEM).
>
> The engine protection system will light the Maintenance Lamp (orange) when an out-of-range condition occurs.
>
> If the engine protection system fluid lamp comes on while driving, it means a fault code has been recorded. The light will remain on as long as the fault is occurring.
>
> The light will begin to flash if the condition continues to get worse. The engine power and/or speed will gradually reduce. If the engine protection shutdown feature is enabled, the engine will shut down to prevent engine damage.
>
> **Note · Примечание**
> Some OEMs use a shorting plug.
>
> To check for active fault codes, turn the vehicle keyswitch to the OFF position and move the diagnostic switch to the ON position.
>
> Turn the vehicle keyswitch to the ON position. If no active fault codes are recorded, all three lights will come on and stay on. If active fault codes are recorded, all three lights will come on momentarily. The amber (WARNING) and red (STOP) lights will begin to flash the code of the recorded fault.
>
> The fault code will flash in the following sequence: First, the amber (WARNING) lamp will flash. Then there will be a short, 1 second pause when both the yellow and red lights are OFF. The numbers of the recorded fault code will then flash in red. There will be a 1 second pause between each number. When the number is done flashing, an amber light will appear again. The number will repeat in the same sequence.
>
> The lights will continue to flash the same fault code until the system is advanced to the next active fault code.
>
> To go to the second fault code, move the idle speed adjust switch to "+", then release. You can also go back to the previous fault code by moving the switch to "-", then releasing. To check the third or fourth fault code, move the switch to "+", then release it when all active fault codes have been viewed.
>
> Moving the switch to "+" will go back to the first fault code. A brief explanation of all of the fault codes are in Section TF of this manual.
>
> **Note · Примечание**
> Some OEMs use a shorting plug.
>
> To stop the diagnostic system, move the diagnostic switch to the OFF position or remove the shorting plug. Turn the vehicle keyswitch to the OFF position.
>
> ### Fault Code Snapshot Data
>
> When a diagnostic fault code is recorded in the ECM, the ECM input and output data is recorded from all sensors and switches. Snapshot data allows the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.
>
> Fault code snapshot data can **only** be viewed with INSITE™ electronic service tool.
>
> ### Engine Protection System
>
> The QSK fuel system engines are equipped with an engine protection system. The system monitors critical engine temperatures, fluid level, switch position, and pressure, and will log diagnostic faults when an over or under normal operating range condition occurs. If an out-of-range condition exists, engine derate action can be initiated. The operator will be alerted by the illumination of the in-cab Maintenance Lamp. The WARNING lamp will start to flash when an out-of-range condition continues to get worse and engine shutdown will occur. The operator **must** pull to the side of the road when it is safe to do so, to reduce the possibility of engine damage.
>
> #### Engine protection system monitors:
>
> - Coolant temperature
> - Coolant level (optional)
> - Intake manifold temperature
> - Oil pressure.
>
> #### Engine protection system monitors for:
>
> - High coolant temperature
> - Low coolant level (optional)
> - High intake manifold temperature
> - Low/very low oil pressure.
>
> The engine protection system can have two selectable features: Engine protection enable and engine protection shutdown. If the engine protection enable feature is selected, engine power and speed are gradually reduced, depending on the level of severity of the observed condition. If engine protection shutdown feature is selected, the engine will shut down. The engine can be restarted by turning the keyswitch OFF and then back ON.
>
> #### Engine protection features:
>
> - Engine protection enable
> - Engine protection shutdown.
