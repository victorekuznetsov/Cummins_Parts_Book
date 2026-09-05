---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "98-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2003-03-24"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 44
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `98-101-007`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-101-007.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Программируемые функции

Центр

Подсистема двигателя содержит:

1. Электронный модуль управления (ECM)
2. Главная струя двигателя
3. Датчик давления в топливной рампе
4. Двигатель Speed Sensor
5. Электронный клапан управления топливом (EFC).

![[19801566.png]]

Система CENTRYTM была разработана для электрических систем производителя оригинального оборудования (OEM) 12- и 24-VDC. Следующие компоненты отличаются между 12- и 24-VDC системами:

1. ЭКМ
2. EFC клапан
3. Клапан отсечки топлива
4. Электрический привод STC (если используется)
5. Вспомогательные устройства отключения (если используется)

![[19801567.png]]

Следующие компоненты одинаковы как в 12-, так и в 24-VDC системах:

1. Главная струя двигателя
2. Датчик давления в топливной рампе
3. Двигатель Speed Sensor
4. Интерфейс переключателя дроссельной заслонки OEM.

![[19801568.png]]

ECM CENTRYTM загружен калибровкой, содержащей управление двигателем и информацию о конкретных приложениях OEM. Авторизованное место ремонта Cummins может перекалибровать ECM на оборудовании с помощью INSITETM, CompulinkTM или EcheckTM и электронной базы данных и сети программного обеспечения (ESDN). Некоторые корректировки могут быть сделаны с помощью Cummins INSITETM, CompulinkTM или EchekTM при использовании картриджа CENTRYTM.

![[19800109.png]]

Функции CENTRYTM, используемые в приложении, будут отображаться в режиме монитора INSITETM, CompulinkTM или EchekTM и на экранах параметров просмотра. OEM и калибровка определяют, какие функции используются и какие параметры могут быть регулируемыми.

![[19800109.png]]

Основная проводка двигателя CENTRYTM содержит следующие соединения и предохранители:

1. Коннектор ECM
2. EFC клапан 90-градусные коннекторы
3. Закрытие терминала клапан Ring
4. 5-AMP предохранители
5. Интерфейс шины данных Engine-Side CAN Connector
6. Сенсор давления Rail Pressure Connector
7. OEM 9-контактный коннектор (C-5)
8. OEM 9-контактный коннектор (C-6)
9. Терминал наземного кольца CentryTM
10. Электрический STC Ring Terminal (необязательно)
11. Коннекторы датчиков скорости двигателя.

> [!note] Примечание
> Расположения веток соединительной проводов ремня разъемной проводов различаются между семействами двигателей.

![[19801570.png]]

Компоненты интерфейса OEM

**Компоненты интерфейса OEM**

Система CENTRYTM подключена к OEM-оборудованию через два OEM-разъема 9-контактной проводов на основной ремне электропроводки двигателя.

![[19801575.png]]

Оборудование OEM будет поставлять электронный сигнал дроссельной заслонки.

Он может поставляться электронным дросселем для ног, ручным дросселем, переключателем или оборудованием ECM (модуль управления OEM).

![[19801576.png]]

Большинство механических приложений передачи привода (вехикулярных) будут использовать переключатель проверки бездействия в интерфейсе дросселя. Выключатель проверки на холостом ходу представляет собой переключатель включения/выключения, который указывает на холостом ходу или выключенном холостом ходу. Этот переключатель будет проверять, когда дросселя находится в положении холостого хода.

Большинство стационарных источников питания, гидравлического привода насоса или приложений для электропривода **не **используют валидацию бездействия.

![[19801577.png]]

OEM-оборудование может взаимодействовать с одной или несколькими из следующих функций переключателя CENTRYTM:

1. Альтернативный контроль крутящего момента
2. Альтернативный контроль низкого уровня холостого хода
3. Промежуточное управление скоростью
4. Альтернативный Droop/High Idle Control

![[19801578.png]]

Большинство механических приложений передачи привода (вехико) будут использовать резервный валидационный переключатель на альтернативных выключателях управления свисанием / высоким холостым ходом и переключателях управления с промежуточной скоростью. Валидация коммутатора обеспечивает вторичный сигнал, чтобы указать, включен ли выключатель или нет.

Большинство стационарных источников питания, гидравлического привода насоса или приложений с электроприводом **не **используют валидацию переключателя.

![[19801579.png]]

Если ни одна из переключаемых функций не используется, OEM-оборудование может использовать систему CENTRYTM для считывания температуры охлаждающей жидкости, давления масла и температуры вспомогательного масла (температура передачи). Эти данные доступны OEM через публичную шину данных CAN и требуют электронного интерфейса OEM.

![[19801580.png]]

OEM-оборудование может использовать дополнительный вспомогательный привод водителя. Это может быть использовано для питания вспомогательных устройств отключения или обеспечения выходного сигнала крутящего момента двигателя.

![[19801581.png]]

Оборудование OEM содержит лампу неисправности и переключатель в кабине или месте расположения оператора. Неисправность лампы будет светиться в течение 1-2 секунд после включения ключа. Лампа погаснет, если в системе CENTRYTM не будут обнаружены неисправности.

![[19801582.png]]

Электронный губернатор

**Электронная губернаторская операция**

Электронный регулятор CENTRYTM был разработан, чтобы быть гибким, чтобы удовлетворить широкий спектр потребностей в управлении двигателем внедорожного оборудования.

![[19801583.png]]

OEM выбирает настройки с низким и высоким холостым ходом вместе с оптимальными характеристиками регулятора отклика двигателя для приложения. OEM-производители также решают, будут ли некоторые из этих настроек настраиваться на CompulinkTM или EchekTM.

![[19801584.png]]

Оперативные особенности

**Операционные особенности**

Система CENTRYTM содержит дополнительные функции, выбранные OEM, для максимизации скорости двигателя, мощности, крутящего момента, отклика и производительности дыма для удовлетворения конкретных потребностей приложения. На всех дополнительных функциях OEM будет определять тип используемого переключателя и его местоположение.

![[19801586.png]]

Альтернативный контроль крутящего момента

**Альтернативный контроль крутящего момента**

Эта функция позволяет использовать альтернативную максимальную кривую крутящего момента двигателя с электронным управлением для оптимальной эффективности работы в условиях нагрузки и разгрузки.

Функция альтернативного крутящего момента активируется всякий раз, когда обычно закрытый альтернативный переключатель крутящего момента открыт и 5 VDC обнаруживаются на линии сигнала альтернативного крутящего момента. Пять точек рельсового давления против скорости двигателя определяют альтернативную кривую крутящего момента.

Показано график, иллюстрирующий альтернативную кривую крутящего момента, которая находится ниже нормальной кривой крутящего момента.

![[19801587.png]]

Альтернативный контроль низкого уровня

**Альтернативный контроль на низком уровне**

Эта функция позволяет использовать две различные настройки скорости с низким уровнем холостого хода с нормальным управлением дроссельной заслонки над установкой скорости с низким уровнем холостого хода. Эта функция часто используется на электроприводных грузовиках, когда они движутся выше 5 км / ч [3 миль в час ].

![[19801588.png]]

Альтернативная функция с низким уровнем холостого хода активируется всякий раз, когда обычно закрытый альтернативный переключатель с низким уровнем холостого хода открыт и 5 VDC обнаруживаются на альтернативной линии сигнала с низким уровнем холостого хода. Следующее искусство иллюстрирует альтернативную скорость низкого холостого хода, которая выше нормальной скорости низкого холостого хода.

![[19801589.png]]

Контроль средней скорости

**Промежуточное управление скоростью**

Эта функция будет переопределять дросселя и управлять скоростью двигателя до калиброванной настройки скорости. Эта функция часто используется в сочетании с взлётом мощности (PTO) на некотором оборудовании или динамической тормозной скоростью двигателя на электроприводных грузовых автомобилях.

![[19801590.png]]

Функция промежуточной скорости активируется всякий раз, когда обычно открытый переключатель управления промежуточной скоростью закрыт и на линии сигнала промежуточной скорости обнаруживается менее 1 VDC. Если используется валидация переключателя, то сигналы валидации как на промежуточной скорости, так и на переключателе должны быть менее 1 VDC до того, как эта функция будет обнаружена.

![[19801591.png]]

Альтернативный спуск/высокий контроль холостого хода

**Альтернативный режим контроля скользящего/высокоспилотного режима**

Эта функция позволяет два различных отклика двигателя и настройки высокого холостого хода. Это позволяет двум различным режимам работы оптимизировать производительность губернатора.

![[19801592.png]]

Альтернативная функция droop/high-idle активируется всякий раз, когда обычно открытый альтернативный переключатель droop/high-idle закрыт и менее 1 VDC обнаруживается на альтернативной линии сигнала droop/high-idle. Если используется валидация переключателя, то оба альтернативных сигнала валидации сбрасывания/высокого холостого хода и сигнала валидации переключателя должны быть менее 1 VDC до активации этой функции.

![[19801593.png]]

Монитор

**Монитор**

Эта функция может быть использована, когда ни одна из переключаемых функций не используется. Он позволяет системе CENTRYTM считывать давление масла, температуру охлаждающей жидкости и/или вспомогательный датчик температуры и передает эти входные данные на шине данных CAN в электронный прибор управления OEM или модуль управления OEM.

![[19801594.png]]

Показано схема проводов, иллюстрирующая схемы функций монитора.

![[19801595.png]]

Вспомогательный контроль за выключением

**Вспомогательный контроль остановки**

Вспомогательный драйвер в системе CENTRYTM может использоваться для питания вспомогательных устройств отключения, таких как клапаны воздухозаборника или дополнительные устройства отключения топлива. Он также может быть использован для отключения другого оборудования, когда двигатель выключается.

Вспомогательный контроль выключения будет отводить электроэнергию вспомогательному водителю, когда замок зажигания выключен или если двигатель выключен из-за состояния сверхскоростной скорости.

![[19801581.png]]

Сигнал крутящего момента

**Сигнал крутящего момента**

Выходной сигнал крутящего момента является стандартной трансляцией на шине данных CAN. Кроме того, вспомогательный привод драйвера может использоваться для обеспечения выходного сигнала крутящего момента двигателя в приложениях, где используется вспомогательная функция управления выключением CENTRYTM **не**.

Выходной сигнал крутящего момента используется в некоторых интерфейсах передачи для оптимизации графиков сдвига и обеспечения более плавного сдвига.

![[19801601.png]]

Транзиторный контроль черного дыма

Контроль над дымом в черном

Эта функция ограничивает заправку топливом в зависимости от времени и доставки топлива, в дополнение к функциям гидромеханического управления дымом AFC и STC, установленными транспортными средствами CENTRYTM.

![[19801602.png]]

Переходная функция черного дыма CENTRYTM ограничивает скорость увеличения давления в топливной рельсе за единицу времени. В некоторых приложениях электронная скорость безвоздушной, задержки и пружины может быть регулируемой CompulinkTM / EcheckTM. Эти электронные параметры аналогичны параметрам на гидромеханическом АФК в топливном насосе.

![[19801603.png]]

### ВАШАЯ ПОДДЕРЖКА

Общие сведения

Многие сельскохозяйственные приложения будут использовать электронный регулятор CENTRYTM для обеспечения крутящего момента и управления мощностью ADVANTAGETM.

![[19801596.png]]

Управление ADVANTAGETM позволяет двигателю выдавать дополнительную мощность и крутящий момент, поскольку двигатель вяжется ниже номинальной скорости. Это обеспечивает повышенную эффективность работы в приложениях, где требуется устойчивая скорость на земле с непрерывно изменяющейся нагрузкой двигателя.

![[19801597.png]]

CENTRYTM ADVANTAGETM в электронном виде контролирует максимальное давление в топливном рельсе, доступное в соответствии с электронной калибровкой пиковой точки давления в рельсах питания (точка преимущества) и электронно калиброванное максимальное давление в рельсах при номинальной точке оборота двигателя.

![[19801598.png]]

ADVANTAGETM обеспечивает более крутой подъем крутящего момента между пиковой мощностью и номинальными условиями, чем это возможно с гидромеханической топливной системой. Это приводит к снижению скорости падения и большей доступной мощности в условиях внешней нагрузки.

![[19801599.png]]

### Диагностические коды ошибок

Общие сведения

Система CENTRYTM может отображать и записывать обнаруживаемые условия неисправности в своих системах и схемах. Желтая диагностическая лампа возле органов управления оператора будет освещена, когда система неисправности станет активной.

![[19801604.png]]

Лампа неисправности должна загораться в течение примерно 1 - 2 секунд после включения ключа, а затем выходить после того, как не было обнаружено неисправностей.

![[19802499.png]]

В то время как состояние неисправности обнаруживается, лампа неисправности включается или включается. CENTRYTM включает лампу для предупреждения неисправностей и ON FLASHING для более серьезных неисправностей, которые могут повлиять на работу двигателя и которые требуют немедленного внимания. Условия активного отказа должны быть исправлены как можно скорее.

![[19801605.png]]

Для определения активного кода неисправности CENTRYTM выключите двигатель и включите переключатель зажигания в положение ON (двигатель **не** работает). Переключите диагностический переключатель на положение ON в течение 1 - 2 секунд, а затем отпустите его. Неисправная лампа будет освещаться, пока диагностический выключатель удерживается в положении Включения.

![[19801606.png]]

После выпуска диагностического выключателя наступает короткая пауза, за которой следует первый код неисправности. Коды ошибок CENTRYTM состоят из трех цифр с пятью вспышками для каждой цифры. Между каждой цифрой кода неисправности есть короткая пауза. После того, как три цифры мигнули и код известен, возникает более длительная пауза с последующим повторением одной и той же последовательности кода ошибки.

![[19801607.png]]

Переключение диагностического переключателя перейдет к следующему коду ошибки. После того, как все активные коды неисправностей будут отображены, последовательность флэш-кодов неисправностей будет повторяться, начиная с первого кода неисправности.

![[19801608.png]]

Запуск двигателя или поворот переключателя зажигания в OFF выведут из режима диагностического вспышки неисправности.

![[19801609.png]]

Операция Back-up Mode

**Режим обновления**

Когда определенные системные неисправности обнаружены, двигатель будет по умолчанию резервного режима. Определение режима резервного копирования отличается для разных ошибок. В общем, если выключатель проверки бездействия **не используется**, режим резервного копирования будет иметь некоторую постоянную калиброванную скорость. Если используется переключатель проверки бездействия, режим резервного копирования будет иметь две скорости в зависимости от положения переключателя: Низкая скорость при включении холостого хода, высокая скорость при выключении холостого хода.

![[19801610.png]]

### Режим монитора Insite

Общие сведения

Режим монитора инструментальных средств обслуживания является полезным средством устранения неполадок, которое отображает ключевые входы и выходы ECM. Эта функция может использоваться для определения постоянных или аномально колеблющихся значений.

> [!note] Примечание
> Каждый экран монитора содержит одну и ту же информацию, но экраны будут выглядеть по-разному.

![[19400360.png]]

Показано, что монитор CENTRYTM отображает все возможные параметры, которые могут отображаться в режиме монитора, как они будут видны на экране INSITETM. Количество этих параметров, которые отображаются, будет варьироваться между приложениями двигателя.

Режим монитора может использоваться для поиска аномально колеблющихся показаний при устранении неполадок. Датчики, которые не работают в диапазоне, также можно найти, ища фиксированные показания. Например, показания давления на рельсах **не** изменяются при скорости двигателя.

![[18800003.png]]


> [!quote]- Original (English) · английский оригинал
> ### Programmable Features
>
> CENTRY™
>
> The engine subsystem contains:
>
> 1. Electronic Control Module (ECM)
> 2. Main Engine Harness
> 3. Rail Pressure Sensor
> 4. Engine Speed Sensor
> 5. Electronic Fuel Control Valve (EFC).
>
> The CENTRY™ system has been designed for both 12- and 24- VDC original equipment manufacturer (OEM) electrical systems. The following components are different between 12- and 24-VDC systems:
>
> 1. ECM
> 2. EFC Valve
> 3. Fuel Shutoff Valve
> 4. Electric STC Actuator (if used)
> 5. Auxiliary Shutdown Device (if used)
>
> The following components are the same in both 12- and 24-VDC systems:
>
> 1. Main Engine Harness
> 2. Rail Pressure Sensor
> 3. Engine Speed Sensor
> 4. OEM throttle switch interface.
>
> The CENTRY™ ECM is loaded with a calibration containing engine control and OEM application-specific information. A Cummins Authorized Repair Location can recalibrate an ECM on the equipment with INSITE™, Compulink™, or Echeck™ and the Electronic Software Database and Network (ESDN). Some adjustments can be made with the Cummins INSITE™, Compulink™, or Echek™ when a CENTRY™ cartridge is used.
>
> CENTRY™ features used in an application will be displayed in INSITE™, Compulink™, or Echek™ monitor mode and view parameter screens. The OEM and calibration will determine which features are used and which parameters can be adjustable.
>
> The CENTRY™ main engine harness contains the following connections and fuses:
>
> 1. ECM Connector
> 2. EFC Valve 90-Degree Connectors
> 3. Fuel Shutoff Valve Ring Terminal
> 4. 5-AMP Fuses
> 5. Engine-Side Datalink Connector
> 6. Rail Pressure Sensor Connector
> 7. OEM 9-pin Connector (C-5)
> 8. OEM 9-pin Connector (C-6)
> 9. CENTRY™ Ground Ring Terminal
> 10. Electric STC Ring Terminal (optional)
> 11. Engine Speed Sensor Connectors.
>
> **Note · Примечание**
> Harness connector breakout locations differ between engine families.
>
> OEM Interface Components
>
> **OEM Interface Components**
>
> The CENTRY™ system is connected to the OEM equipment through the two OEM 9-pin connectors on the main engine harness.
>
> The OEM equipment will supply an electronic throttle signal.
>
> It can be supplied by an electronic foot throttle, hand throttle, switch, or equipment ECM (OEM control module).
>
> Most mechanical drive transmission (vehicular) applications will use an idle validation switch in the throttle interface. The idle validation switch is an on/off switch which indicates idle or off idle. This switch will verify when the throttle is in the idle position.
>
> Most stationary power, hydraulic pump drive, or electric drive applications will **not** use idle validation.
>
> The OEM equipment can interface with one or more of the following CENTRY™ switch features:
>
> 1. Alternate Torque Control
> 2. Alternate Low Idle Control
> 3. Intermediate Speed Control
> 4. Alternate Droop/High Idle Control.
>
> Most mechanical drive transmission (vehicular) applications will use a redundant validation switch on the alternate droop/high-idle control and intermediate-speed control switches. Switch validation provides a secondary signal to indicate whether or **not** the switch is on.
>
> Most stationary power, hydraulic pump drive, or electric-drive applications will **not** use switch validation.
>
> If none of the switched features are used, the OEM equipment can use the CENTRY™ system to read coolant temperature, oil pressure, and auxiliary oil temperature (transmission temperature). These data are available to the OEM through the public datalink and require an OEM electronic interface.
>
> The OEM equipment can utilize the optional auxiliary driver lead. This can be used to power auxiliary shutdown devices or provide an engine torque output signal.
>
> The OEM equipment contains a fault lamp and switch in the cab or operator location. The fault lamp will light for 1 to 2 seconds after the key is turned on. The lamp will go out if no faults are detected in the CENTRY™ system.
>
> Electronic Governor Operation
>
> **Electronic Governor Operation**
>
> The CENTRY™ electronic governor has been designed to be flexible to meet the wide variety of engine control needs of off-highway equipment.
>
> The OEM selects low- and high-idle settings along with the optimum engine response governor droop characteristics for the application. The OEMs also decide whether or **not** some of these settings will be Compulink™ or Echek™ adjustable.
>
> Operational Features
>
> **Operational Features**
>
> The CENTRY™ system contains optional OEM-selected features to maximize engine speed, power, torque, response, and smoke performance to meet specific application needs. On all optional features, the OEM will determine the type of switch used and its location.
>
> Alternate Torque Control
>
> **Alternate Torque Control**
>
> This feature enables an alternative electronically controlled maximum engine torque curve for optimum operating efficiency in loaded-versus-unloaded conditions.
>
> The alternate torque feature is activated whenever the normally closed alternate torque switch is opened and 5 VDC are detected on the alternate torque signal line. Five rail-pressure-versus-engine-speed points define the alternate torque curve.
>
> Shown is a graph illustrating an alternate torque curve that is below the normal torque curve.
>
> Alternate Low-Idle Control
>
> **Alternate Low-Idle Control**
>
> This feature allows for two different low-idle speed settings with normal throttle control above the low-idle speed setting. This feature is often used on electric drive haul trucks when they are traveling above 5 kph \[3 mph\].
>
> The alternate low-idle feature is activated whenever the normally closed alternate low-idle switch is opened and 5 VDC are detected on the alternate low-idle signal line. The following art illustrates an alternate low-idle speed that is above the normal low-idle speed.
>
> Intermediate-Speed Control
>
> **Intermediate Speed Control**
>
> This feature will override the throttle and control the engine speed to the calibrated speed setting. This feature is often used in conjunction with power take-off (PTO) on some equipment or dynamic brake engine speed on electric-drive haul trucks.
>
> The intermediate-speed feature is activated whenever the normally open intermediate-speed control switch is closed and less than 1 VDC is detected on the intermediate-speed signal line. If switch validation is used, both intermediate-speed and switch validation signals **must** be less than 1 VDC before this feature can be detected.
>
> Alternate Droop/High Idle Control
>
> **Alternate Droop/High-Idle Control**
>
> This feature allows two different engine response and high-idle settings. This allows two different operating modes to optimize governor performance.
>
> The alternate droop/high-idle feature is activated whenever the normally open alternate droop/high-idle switch is closed and less than 1 VDC is detected on the alternate droop/high-idle signal line. If switch validation is used, both alternate droop/high-idle and switch validation signals **must** be less than 1 VDC before this feature can be activated.
>
> Monitor
>
> **Monitor**
>
> This feature can be used when none of the switched features are used. It allows for the CENTRY™ system to read oil pressure, coolant temperature, and/or an auxiliary temperature sensor and broadcasts these inputs on the datalink to an OEM electronic dash or OEM control module.
>
> Shown is a wiring diagram illustrating the monitor feature circuits.
>
> Auxiliary Shutdown Control
>
> **Auxiliary Shutdown Control**
>
> The auxiliary driver in the CENTRY™ system can be used to power auxiliary shutdown devices such as air intake flaps or additional fuel shutdown devices. It can also be used to shut off other equipment when the engine shuts down.
>
> Auxiliary shutdown control will remove electrical power to the auxiliary driver when the keyswitch in turned off or if the engine shuts down due to an overspeed condition.
>
> Torque Output Signal
>
> **Torque Output Signal**
>
> The torque output signal is a standard broadcast on the datalink. In addition, the auxiliary driver lead can be used to provide an engine torque output signal in applications where the CENTRY™ auxiliary shutdown control feature is **not** used.
>
> The torque output signal is used in some transmission interfaces for optimization of shift schedules and to provide smoother shifting.
>
> Transient Black Smoke Control
>
> **Transient Black Smoke Control**
>
> This feature limits fueling based on time and fuel delivery, in addition to the AFC and STC hydromechanical smoke control functions CENTRY™ vehicles have installed.
>
> The CENTRY™ transient black smoke feature limits the rate of fuel rail pressure increase per unit time. On some applications, the electronic no-air, delay, and spring rate can be Compulink™/Echeck™ adjustable. These electronic parameters are similar to those on the hydromechanical AFC in the fuel pump.
>
> ### ADVANTAGE™
>
> General Information
>
> Many agricultural applications will use the CENTRY™ electronic governor to provide ADVANTAGE™ torque and power control.
>
> ADVANTAGE™ control allows the engine to deliver additional horsepower and torque rise as the engine is lugged below rated speed. This provides improved operating efficiency in applications where steady ground speeds are desired with continuously changing engine load.
>
> CENTRY™ ADVANTAGE™ electronically controls the maximum fuel rail pressure available according to the electronically calibrated peak power rail pressure point (advantage point) and the electronically calibrated maximum rail pressure at rated engine speed point.
>
> ADVANTAGE™ provides a steeper torque rise between peak power and rated conditions than is obtainable with the hydromechanical fuel system. This results in reduced speed drop and more available power under external loading conditions.
>
> ### Diagnostic Fault Codes
>
> General Information
>
> The CENTRY™ system can display and record detectable fault conditions within its systems and circuits. A yellow diagnostic lamp near the operator's controls will be illuminated when a system fault becomes active.
>
> The fault lamp should light for about 1 to 2 seconds after key-on, and then go out after no faults have been detected.
>
> While a fault condition is being detected, the fault lamp will turn ON or ON FLASHING. CENTRY™ will turn the lamp ON for warning faults, and ON FLASHING for more severe faults that can affect engine operation and that need immediate attention. Active fault conditions **must** be corrected as soon as possible.
>
> To determine an active CENTRY™ fault code, shut off the engine and turn keyswitch to the ON position (engine **not** running). Toggle the diagnostic switch to the ON position for 1 to 2 seconds and then release it. The fault lamp will illuminate while the diagnostic switch is held in the ON position.
>
> After releasing the diagnostic switch, there is a short pause, followed by the first fault code. CENTRY™ fault codes consist of three digits with up to five flashes for each digit. There is a short pause, between each digit of the fault code. Once the three digits have flashed and the code is known, there is a longer pause followed by a repeating of the same fault code sequence.
>
> Toggling the diagnostic switch will advance to the next fault code. Once all active fault codes have been displayed, the fault code flash sequence will be repeated starting from the first fault code.
>
> Starting the engine or turning the keyswitch to OFF will exit the diagnostical fault flash mode.
>
> Back-up Mode Operation
>
> **Backup Mode Operation**
>
> When certain system faults are detected, the engine will default to backup mode. The definition of backup mode is different for different faults. In general, if an idle validation switch is **not** used, the backup mode will be some constant calibrated speed. If an idle validation switch is used, the backup mode will be two speeds based on switch position: Low speed when switch on-idle, high speed when switch off-idle.
>
> ### INSITE™ Monitor Mode
>
> General Information
>
> The service tool monitor mode is a useful troubleshooting aid that displays the key ECM inputs and outputs. This feature can be used to spot constant or abnormally fluctuating values.
>
> **Note · Примечание**
> Each service tool monitor mode screen contains the same information, but the screens will appear differently.
>
> Shown is the CENTRY™ monitor screen showing all of the possible parameters that can be displayed in monitor mode as they would be seen on an INSITE™ screen. The number of these parameters that are displayed will vary between engine applications.
>
> Monitor mode can be used to look for abnormally fluctuating readings while troubleshooting. Sensors that are failed in range can also be found by looking for fixed readings. For example, rail pressure reading does **not** change with engine speed.
