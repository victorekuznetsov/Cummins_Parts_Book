---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "10-101-007-om-auto"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2003-04-10"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666251"
figures: 26
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-101-007-om-auto.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-101-007-om-auto.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
  - "перевод/машинный"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `10-101-007-om-auto`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666251 — Signature and ISX Operation and Maintenance Manual|3666251]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2003-04-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-101-007-om-auto.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-101-007-om-auto.pdf)

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

Автомобильное применение

Электронно управляемая топливная система может показывать и регистрировать определенные неисправности двигателя. Неисправности показаны как коды неисправностей. Эти коды облегчат устранение неполадок. Коды неисправностей регистрируются в ECM.

См. Signature and ISM Features Manual, Bulletin No. 3666320, для описания кодов неисправностей.

> [!note] Примечание
> Не все неровности двигателя указаны в качестве кодов неисправностей.

![[17c00067.png]]

Существует два типа кодов неисправностей:

- Коды электронных топливных систем двигателя
- Коды систем защиты двигателя.

![[17c00066.png]]

Коды неисправностей электронной топливной системы двигателя можно увидеть на сигнальных и стоп-сигналах в панели кабины.

> [!note] Примечание
> Неактивные коды неисправностей могут **не** быть выброшены. Электронный инструмент обслуживания должен использоваться для считывания неактивных ошибок в ECM. Посмотрите авторизованное место ремонта Cummins.

![[17c00030.png]]

Светильник STOP будет красным. Предупреждающий свет будет желтым или красным, в зависимости от предпочтений OEM-производителя. Когда замок зажигания автомобиля включен и диагностический выключатель выключен, все три лампы будут освещаться, чтобы проверить их работу. Свет будет поступать последовательно через 2 секунды.

![[19200053.png]]

Свет будет выключен до тех пор, пока не будет записан код неисправности. Если свет включен, то существует активная ошибка.

Если стоп-сигнал (красный) освещается во время вождения, неисправность может привести к отключению двигателя. Транспортное средство должно быть перемещено на обочину дороги и остановлено, как только это можно сделать безопасным способом. Автомобиль должен оставаться припаркованным до тех пор, пока существует эта ошибка. Если свет ПРЕДУПРЕЖДЕНИЯ (желтый) освещен, транспортное средство может безопасно управляться, но ошибка должна быть исправлена как можно скорее.

![[19200068.png]]

Система защиты двигателя регистрирует отдельные коды неисправностей для вне диапазона условий, связанных с любым из следующих датчиков:

- Температура охлаждения
- Уровень охлаждающей жидкости
- Температура масла
- Масляное давление
- Ввод многообразной температуры
- Вода в топливе.

![[17c00068.png]]

Эта система активирует устройство предупреждения в кабине, когда возникает вне зоны действия. Предупреждающее устройство - это свет, зуммер или оба. Эта система также активирует желтую жидкостную лампу, если она оборудована.

![[oi803vz.png]]

Если во время вождения включается свет или зуммер, это означает, что был записан код неисправности. Лампа будет оставаться включенной до тех пор, пока существует неисправность, а мощность и скорость двигателя будут постепенно снижаться. Если вне диапазона условия продолжаются, свет начнет мигать или мигать. Автомобиль должен быть припаркован всякий раз, когда замечены серьезные нарушения мощности.

Виновность должна быть исправлена как можно скорее.

![[17c00069.png]]

Выключите машину. Для проверки электронной топливной системы двигателя и кодов неисправностей системы защиты двигателя переместить диагностический переключатель в положение Включения или подключить шортинг-розетку к диагностическому разъему.

![[gp8swvs.png]]

Включите замок зажигания автомобиля. Если во время отключения системы активизировались какие-либо коды неисправностей, то в огнях начнет мигать код зарегистрированных неисправностей. Если не будет зафиксировано кодов неисправностей, лампы будут **не** мигать, но будут освещены.

![[gp8swgr.png]]

Код неисправности будет мигать в следующей последовательности:

Во-первых, будет мигать предупреждающий (желтый) свет. Затем будет короткая 1- или 2-секундная пауза, после которой в (красном) STOP вспыхнет номер записанного кода неисправности. Между каждым числом будет 1- или 2-секундная пауза. Когда число закончило мигать красным, снова появится желтый свет. Трехзначный код будет повторяться в той же последовательности.

![[gp800kd.png]]

Свет будет продолжать мигать тем же кодом, пока система не будет вынуждена сделать что-то еще. Чтобы перейти к следующему коду неисправности, перенесите круиз-контроль / PTO на некоторое время в положение RESUME / ACCEL. Вы можете вернуться к предыдущему коду неисправности, на мгновение переместив круиз-контроль / PTO в положение SET / COAST. Если регистрируется только один активный сбой, система будет непрерывно отображать один и тот же код сбоя, когда выключатель RESUME/ACCEL или SET/COAST находится в депрессии.

![[gp8swkq.png]]

При **не** использовании диагностической системы выключите диагностический выключатель или удалите шортинг-розыгрыш. Если диагностический выключатель включен или шортинг вставлен, ECM будет **не** регистрировать некоторые ошибки. Монитор технического обслуживания будет работать **не** правильно.

Чтобы остановить диагностическую систему, переместить диагностический переключатель в положение OFF или удалить шортинг-розыгрыш. Выключите выключатель автомобиля.

![[gp8swvv.png]]

### Система защиты двигателя

Двигатели Signature/ISX оснащены системой защиты двигателя. Система контролирует критические температуры и давления двигателя и регистрирует диагностические неисправности при ненормальном рабочем состоянии. Если существует вне зоны действия и должно быть инициировано действие по снижению скорости двигателя, оператор будет предупрежден предупреждающим светом в кабине. Предупреждающий свет мигает или мигает, когда условия вне зоны действия продолжают ухудшаться. Водитель должен тянуться к обочине дороги, когда это безопасно, чтобы уменьшить вероятность повреждения двигателя.

> [!note] Примечание
> Мощность и скорость двигателя будут постепенно снижаться в зависимости от уровня тяжести наблюдаемого состояния. Система защиты двигателя **не будет **выключать двигатель, если не выбрана функция отключения защиты двигателя. Если функция была выбрана и двигатель действительно выключен, двигатель можно запустить снова, выключив переключатель зажигания, а затем включив его обратно.

![[17c00028.png]]

### Описание топливной системы

Один тег данных для ECM расположен на передней части корпуса модуля.

![[17c00046.png]]

Датчики положения кулачка и коленчатого вала двигателя обеспечивают информацию о скорости двигателя и положении.

Датчик положения кулачка расположен между ECM и топливным насосом. Датчик положения коленчатого вала расположен ниже привода воздушного компрессора.

![[17c00050.png]]

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
> Automotive Applications
>
> The electronically controlled fuel system can show and record certain engine faults. The faults are shown as fault codes. These codes will make troubleshooting easier. The fault codes are recorded in the ECM.
>
> Refer to the Signature and ISM Features Manual, Bulletin No. 3666320, for the description of the fault codes.
>
> **Note · Примечание**
> **Not** all engine irregularities are shown as fault codes.
>
> There are two types of fault codes:
>
> - Engine electronic fuel system codes
> - Engine protection system codes.
>
> The engine electronic fuel system fault codes can be seen on the WARNING and STOP lights in the cab panel.
>
> **Note · Примечание**
> Inactive fault codes can **not** be flashed out. An electronic service tool **must** be used to read inactive faults in the ECM. Refer to your Cummins Authorized Repair Location.
>
> The STOP fault light will be red. The WARNING light will be yellow or red, depending on the OEM's preference. When the vehicle keyswitch is turned on and the diagnostic switch is off, all three lights will illuminate to check their operation. The lights will go off in sequence after about 2 seconds.
>
> The lights will remain off until a fault code is recorded. If a light remains on, an active fault exists.
>
> If the STOP light (red) is illuminated while driving, the fault can be engine disabling. The vehicle **must** be driven to the side of the road and shut off as soon as it can be done in a safe manner. The vehicle **must** remain parked as long as this fault exists. If the WARNING light (yellow) is illuminated, the vehicle can be safely driven, but the fault **must** be corrected as soon as possible.
>
> The engine protection system logs separate fault codes for out-of-range conditions associated with any of the following sensors:
>
> - Coolant Temperature
> - Coolant Level
> - Oil Temperature
> - Oil Pressure
> - Intake Manifold Temperature
> - Water in Fuel.
>
> This system will activate an in-cab warning device when an out-of-range condition occurs. The warning device is a light, a buzzer, or both. This system will also activate the yellow fluid lamp, if equipped.
>
> If the light or buzzer comes on while driving, it means a fault code has been recorded. The lamp will remain on as long as the fault exists, and engine power and speed will gradually be reduced. If the out-of-range conditions continue, the light will start to flash or blink. the vehicle **must** be parked whenever severe power derates are noticed.
>
> The fault **must** be corrected as soon as possible.
>
> Turn off the vehicle. To check for engine electronic fuel system and engine protection system fault codes, move the diagnostic switch to the ON position, or connect the shorting plug into the diagnostic connector.
>
> Turn on the vehicle keyswitch. If any fault codes were active during system power-down, the lights will begin to flash the code of the recorded faults. If no fault codes are recorded, the lamps will **not** flash, but will be illuminated.
>
> The fault code will flash in the following sequence:
>
> First, a WARNING (yellow) light will flash. Then there will be a short 1- or 2-second pause after which the number of the recorded fault code will flash in (red) STOP. There will be a 1- or 2-second pause between each number. When the number has finished flashing in red, a yellow light will appear again. The three-digit code will repeat in the same sequence.
>
> The lights will continue to flash the same code until the system is told to do something else. To go to the next fault code, move the cruise control/PTO switch momentarily to the RESUME/ACCEL position. You can go back to the previous fault code by momentarily moving the cruise control/PTO switch to the SET/COAST position. If **only** one active fault is recorded, the system will continuously display the same fault code when either the RESUME/ACCEL or SET/COAST switch is depressed.
>
> When **not** using the diagnostic system, turn off the diagnostic switch, or remove the shorting plug. If the diagnostic switch is left on or the shorting plug left in, the ECM will **not** log some faults. The maintenance monitor will **not** function correctly, either.
>
> To stop the diagnostic system, move the diagnostic switch to the OFF position, or remove the shorting plug. Turn off the vehicle switch.
>
> ### Engine Protection System
>
> Signature/ISX engines are equipped with an engine protection system. The system monitors critical engine temperatures and pressures and will log diagnostic faults when an abnormal operating condition occurs. If an out-of-range condition exists and engine derate action is to be initiated, the operator will be alerted by an in-cab warning light. The warning light will blink or flash when out-of-range conditions continue to worsen. The driver **must** pull to the side of the road, when it is safe to do so, to reduce the possibility of engine damage.
>
> **Note · Примечание**
> Engine power and speed will be gradually reduced, depending on the level of severity of the observed condition. The engine protection system will **not** shut down the engine unless the engine protection shutdown feature has been selected. If the feature has been selected and the engine does shut down, the engine can be started again by turning off the keyswitch and then turning it back on.
>
> ### Fuel System Description
>
> The one data tag for the ECM is located on the front of the module housing.
>
> The engine cam and crank position sensors provide engine speed and position information.
>
> The cam position sensor is located between the ECM and fuel pump. The crank position sensor is located below the air compressor drive.
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
