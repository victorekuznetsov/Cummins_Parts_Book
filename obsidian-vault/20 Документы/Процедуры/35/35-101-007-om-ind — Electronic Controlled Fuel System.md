---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "35-101-007-om-ind"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2013-03-05"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4021942"
figures: 19
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-101-007-om-ind.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-101-007-om-ind.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `35-101-007-om-ind`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4021942 — QSM11 Industrial Operation and Maintenance Manual|4021942]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2013-03-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-101-007-om-ind.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-101-007-om-ind.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система представляет собой электронно-управляемую систему впрыска топлива, которая оптимизирует экономию топлива. Это делается путем управления кривой крутящего момента и лошадиных сил, функцией управления воздушным топливом (AFC), высокой скоростью двигателя, низким холостым ходом и скоростью движения.

![[oi800v13.png]]

Двигатель имеет возможность управления приводом сцепления вентилятора, если используется сцепление вентилятора с электронным управлением.

Двигатель также позволяет активировать тормоза двигателя, управляя соленоидами тормоза двигателя.

![[20200005.png]]

### Диагностические коды ошибок

Промышленное применение

Система может показывать и записывать неровности в работе, которые представляются кодами неисправностей. Эти коды облегчат устранение неполадок. Коды неисправностей регистрируются в ECM. Их можно прочитать с помощью двух неисправных ламп в кабине или с помощью INSITETM.

> [!note] Примечание
> Не все неровности двигателя указаны в качестве кодов неисправностей.

![[17c00067.png]]

Существует два типа кодов неисправностей:

- Коды электронных топливных систем двигателя
- Коды систем защиты двигателя.

![[17c00066.png]]

Коды неисправностей электронной топливной системы двигателя можно увидеть на сигнальных и стоп-сигналах в панели кабины.

> [!note] Примечание
> Неактивные коды неисправностей могут быть выбиты на двух огнях в кабине. Инструмент службы INSITETM должен использоваться для считывания неактивных ошибок в ECM. Ссылка на авторизованное место ремонта Cummins®.

![[17c00030.png]]

Светильник STOP будет красным. Предупреждающий свет будет желтым или красным, в зависимости от предпочтений OEM-производителя. Когда замок зажигания автомобиля включен и диагностический выключатель выключен, все три лампы будут освещаться, чтобы проверить их работу. Свет будет поступать последовательно через 2 секунды.

![[19200053.png]]

Свет будет выключен до тех пор, пока не будет записан код неисправности. Если свет включен, то существует активная ошибка.

Если стоп-сигнал (красный) освещается во время работы, неисправность может привести к отключению двигателя. Оборудование должно быть отключено, как только это можно сделать безопасным способом. Оборудование должно оставаться припаркованным до тех пор, пока существует эта неисправность. Если свет ПРЕДУПРЕЖДЕНИЯ (желтый или красный) освещен, оборудование может безопасно эксплуатироваться, но неисправность должна быть исправлена как можно скорее.

![[19200435.png]]

Система защиты двигателя регистрирует отдельные коды неисправностей для вне диапазона условий, связанных с любым из следующих датчиков:

- Температура охлаждающей жидкости
- Уровень охлаждающей жидкости
- Температура масла
- Масляное давление
- Температура коллектора.

![[17c00068.png]]

Эта система активирует устройство предупреждения в кабине, когда возникает вне зоны действия. Предупреждающее устройство - это свет, зуммер или оба. Эта система также активирует желтую жидкостную лампу, если она оборудована.

![[oi803vz.png]]

Если система защиты двигателя включает свет или зуммер во время вождения, это означает, что был записан код неисправности. Лампа будет оставаться включенной до тех пор, пока существует неисправность, а мощность и скорость двигателя будут постепенно снижаться. Если вне диапазона условия продолжаются, свет начнет мигать или мигать. Если функция защиты двигателя включена, двигатель будет отключен, чтобы предотвратить повреждение двигателя.

Виновность должна быть исправлена как можно скорее.

![[17c00069.png]]

Выключи двигатель. Для проверки электронной топливной системы двигателя и кодов неисправностей системы защиты двигателя переместить диагностический переключатель в положение Включения или подключить шортинг-розетку к диагностическому разъему.

![[gp8swvs.png]]

Переведите замок зажигания в положение ON.

Если не будет зарегистрировано активных кодов неисправностей, оба огня будут включены и оставаться включенными.

Если активные коды неисправностей записаны, оба огня загорятся на мгновение, то начинают мигать коды зафиксированных неисправностей.

![[gp8swgr.png]]

Код неисправности будет мигать в следующей последовательности:

Во-первых, будет мигать предупреждающий (желтый) свет. Затем будет короткая 1- или 2-секундная пауза, после которой в STOP (красный) вспыхнет номер записанного кода неисправности. Между каждым числом будет 1- или 2-секундная пауза. Когда число закончило мигать красным, снова появится желтый свет. Трехзначный код будет повторяться в той же последовательности.

![[gp800kd.png]]

Свет будет продолжать мигать тем же кодом, пока система не будет вынуждена сделать что-то еще. Чтобы перейти к следующему коду неисправности, переведите CRUISE CONTROL/PTO на некоторое время в положение RESUME/ACCEL. Вы можете вернуться к предыдущему коду ошибки, на мгновение переместив CRUISE CONTROL/PTO в положение SET/COAST. Если регистрируется только один активный сбой, система будет непрерывно отображать один и тот же код сбоя, когда выключатель RESUME/ACCEL или SET/COAST находится в депрессии.

![[gp8swkq.png]]

### Система защиты двигателя

> [!note] Примечание
> Мощность и скорость двигателя будут постепенно снижаться в зависимости от уровня тяжести наблюдаемого состояния. Система защиты двигателя **не будет **выключать двигатель, если не выбрана функция отключения защиты двигателя. Если функция была выбрана и двигатель действительно выключен, двигатель может быть перезапущен, выключив переключатель зажигания, а затем включив его обратно.

Двигатели оснащены системой защиты двигателя. Система контролирует критические температуры и давления двигателя и регистрирует диагностические неисправности при ненормальном рабочем состоянии. Если существует вне зоны действия и должно быть инициировано действие по снижению скорости двигателя, оператор будет предупрежден предупреждающим светом в кабине. Предупреждающий свет мигает или мигает, когда условия вне зоны действия продолжают ухудшаться. Водитель должен тянуться к обочине дороги, когда это безопасно, чтобы уменьшить вероятность повреждения двигателя.

![[17c00028.png]]

### Описание топливной системы

Автомобильное применение

Топливная система ISM на двигателе состоит из:

1. Клапан отсечки топлива
2. Датчик давления масла и датчик температуры
3. Датчик повышения давления коллектора
4. Охлаждающая пластина
5. Модуль управления двигателем (ECM)
6. Двигатель электропроводки ремня разъема Deutsch.

![[19200112.png]]

1. Жгут проводов OEM
2. Двигатель электропроводки ремня разъема Deutsch
3. Топливо в
4. Выгонять топливо
5. Топливный шестеренок насоса
6. Датчик положения коленчатого вала (EPS)
7. Датчик температуры охлаждающей жидкости (в термостате)
8. Датчик уровня охлаждающей жидкости (в переполненном резервуаре) - необязательно
9. Датчик температуры коллектора
10. Датчик атмосферного давления.

![[19200113.png]]

Регулировка холостого хода находится в кабине. Используйте этот переключатель для настройки скорости холостого хода двигателя с шагом 25 об/мин.

- Автомобильный - 600-800 об/мин
- Транзитный шина - 650-800 об/мин.

![[gp2swkp01.png]]

Каждый раз, когда переключатель ненадолго перемещается в положение минус (-), скорость холостого хода уменьшается на 25 об/мин. Когда переключатель ненадолго перемещается в положение плюс (+), скорость холостого хода увеличивается на 25 об/мин.

![[gp8swki.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The system is an electronically controlled fuel injection system that optimizes fuel economy. It does this by controlling the torque and horsepower curve, air-fuel control (AFC) function, engine high speed, low idle, and road speed.
>
> The engine has the capability of controlling the fan clutch actuator if an electronically controlled fan clutch is used.
>
> The engine also allows the engine brakes to be activated by controlling the engine brake solenoids.
>
> ### Diagnostic Fault Codes
>
> Industrial Applications
>
> The system can show and record operation irregularities that present themselves as fault codes. These codes will make troubleshooting easier. The fault codes are recorded in the ECM. They can be read using the two fault lamps in the cab panel or with INSITE™.
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
> Inactive fault codes can **not** be blinked out on the two lights in the cab panel. An INSITE™ service tool **must** be used to read inactive faults in the ECM. Reference a Cummins® Authorized Repair Location.
>
> The STOP fault light will be red. The WARNING light will be yellow or red, depending on the OEM's preference. When the vehicle keyswitch is turned on and the diagnostic switch is off, all three lights will illuminate to check their operation. The lights will go off in sequence after about 2 seconds.
>
> The lights will remain off until a fault code is recorded. If a light remains on, an active fault exists.
>
> If the STOP light (red) is illuminated while operating, the fault can be engine disabling. The equipment **must** be shut off as soon as it can be done in a safe manner. The equipment **must** remain parked as long as this fault exists. If the WARNING light (yellow or red) is illuminated, the equipment can be safely operated, but the fault **must** be corrected as soon as possible.
>
> The engine protection system logs separate fault codes for out-of-range conditions associated with any of the following sensors:
>
> - Coolant temperature
> - Coolant level
> - Oil temperature
> - Oil pressure
> - Intake manifold temperature.
>
> This system will activate an in-cab warning device when an out-of-range condition occurs. The warning device is a light, a buzzer, or both. This system will also activate the yellow fluid lamp, if equipped.
>
> If the engine protection system light or buzzer comes on while driving, it means a fault code has been recorded. The lamp will remain on as long as the fault exists, and engine power and speed will gradually be reduced. If the out-of-range conditions continue, the light will start to flash or blink. If the engine protection shutdown feature is enabled, the engine will be shut down to help prevent engine damage.
>
> The fault **must** be corrected as soon as possible.
>
> Turn off the engine. To check for engine electronic fuel system and engine protection system fault codes, move the diagnostic switch to the ON position, or connect the shorting plug into the diagnostic connector.
>
> Turn the keyswitch to the ON position.
>
> If no active fault codes are recorded, both lights will come on and stay on.
>
> If active fault codes are recorded, both lights will come on momentarily, then begin to flash the code of the recorded faults.
>
> The fault code will flash in the following sequence:
>
> First, a WARNING (yellow) light will flash. Then there will be a short 1- or 2-second pause after which the number of the recorded fault code will flash in STOP (red). There will be a 1- or 2-second pause between each number. When the number has finished flashing in red, a yellow light will appear again. The three-digit code will repeat in the same sequence.
>
> The lights will continue to flash the same code until the system is told to do something else. To go to the next fault code, move the CRUISE CONTROL/PTO switch momentarily to the RESUME/ACCEL position. You can go back to the previous fault code by momentarily moving the CRUISE CONTROL/PTO switch to the SET/COAST position. If **only** one active fault is recorded, the system will continuously display the same fault code when either RESUME/ACCEL or SET/COAST switch is depressed.
>
> ### Engine Protection System
>
> **Note · Примечание**
> Engine power and speed will be gradually reduced, depending on the level of severity of the observed condition. The engine protection system will **not** shut down the engine unless the engine protection shutdown feature has been selected. If the feature has been selected and the engine does shut down, the engine can be restarted by turning OFF the keyswitch, then turning it back ON.
>
> The engines are equipped with an engine protection system. The system monitors critical engine temperatures and pressures, and will log diagnostic faults when an abnormal operating condition occurs. If an out-of-range condition exists and engine derate action is to be initiated, the operator will be alerted by an in-cab warning light. The warning light will blink or flash when out-of-range conditions continue to get worse. The driver **must** pull to the side of the road, when it is safe to do so, to reduce the possibility of engine damage.
>
> ### Fuel System Description
>
> Automotive Applications
>
> The ISM fuel system on an engine consists of:
>
> 1. Fuel shutoff valve
> 2. Oil pressure sensor and temperature sensor
> 3. Intake manifold boost sensor
> 4. Cooling plate
> 5. Engine control module (ECM)
> 6. Engine wiring harness Deutsch connector.
>
> 1. OEM wiring harness
> 2. Engine wiring harness Deutsch connector
> 3. Fuel in
> 4. Fuel out
> 5. Fuel gear pump
> 6. Engine position sensor (EPS)
> 7. Coolant temperature sensor (in thermostat support)
> 8. Coolant level sensor (in overflow tank) - optional
> 9. Intake manifold temperature sensor
> 10. Ambient air pressure sensor.
>
> The idle adjustment is in the cab panel. Use this switch to adjust the engine idle speed in increments of 25 rpm.
>
> - Automotive - 600 to 800 rpm
> - Transit Bus - 650 to 800 rpm.
>
> Each time the switch is briefly moved to the minus (-) position, the idle speed is decreased by 25 rpm. When the switch is briefly moved to the plus (+) position, the idle speed is increased by 25 rpm.
