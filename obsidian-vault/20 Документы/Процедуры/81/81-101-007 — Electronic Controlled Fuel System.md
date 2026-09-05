---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "81-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2013-01-18"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 26
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `81-101-007`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2013-01-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-101-007.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Описание системы CENSETM

Система CENSETM представляет собой систему электронного мониторинга двигателя. Эта система используется в основном для обеспечения расширенной диагностики двигателя и записи эксплуатационных данных двигателя с течением времени.

![[cent337.png]]

Модуль управления двигателем CENSETM (ECM) физически идентичен некоторым другим модулям управления двигателем Cummins® (ECM). См. номера частей ECM, чтобы определить разницу между ECM. Номер детали ECM показан на внешней табличке данных ECM.

Система CENSETM работает аналогично любой другой электронной системе Cummins® и измеряет многие из тех же температур и давлений. Кроме того, система CENSETM измеряет некоторые дополнительные параметры, такие как температура выхлопных газов и дифференциальное давление в фильтрах.

![[19800559.png]]

Система CENSETM использует термопару, установленную в выхлопном порту каждого цилиндра, для измерения температуры выхлопных газов. Низкая температура выхлопа указывает на то, что цилиндр имеет низкую мощность. Высокая температура выхлопных газов указывает на то, что цилиндр получает слишком много топлива.

Система CENSETM измеряет различные давления на двигатель. Измеряя падение давления на фильтре, система CENSETM может определить, когда фильтр необходимо изменить.

![[nobox.png]]

Существует два поколения систем CENSETM. CENSETM CM530 и CENSETM CM2330 следующего поколения.

Модуль CENSETM CM530 поддерживает связь J1587 и интерфейсы RS422 и RS232. Инструменты для электронных услуг INSITETM для CENSETM должны использоваться для связи с этим модулем.

Модуль CENSETM CM2330 оснащен коммуникацией J1939. Базовый инструмент электронного сервиса INSITETM должен использоваться для связи с этим модулем.

![[nobox.png]]

### Программируемые функции

Система CENSETM разработана с учетом широкого спектра потребностей в мониторинге двигателя.

Ссылка на электронный сервис INSITETM, инструмент Руководство пользователя для получения полной информации о программируемых функциях.

![[19400357.png]]

### Данные о тренде двигателя

Система CENSETM способна хранить информацию о работе двигателя для последующего анализа. Инструменты электронного сервиса INSITETM могут использоваться для корректировки скорости отбора проб данных и загрузки данных о тенденциях.

Ссылка на электронный сервис INSITETM, инструмент Руководство пользователя для получения дополнительной информации.

![[19800902.png]]

### Диагностические коды ошибок

Система CENSETM может отображать и записывать определенные условия обнаружения неисправностей. Эти неисправности отображаются в виде кодов неисправностей, что облегчает устранение неполадок. Коды неисправностей сохраняются в ECM.

![[19400328.png]]

Существует два типа кодов неисправностей. Существуют системные неисправности CENSETM и неисправности защиты двигателя.

Система CENSETM неисправна, зажигайте синюю предупредительную лампу. Неисправности защиты двигателя зажигают красную или желтую лампу.

![[19800561.png]]

Все коды ошибок, записанные в протоколе, будут либо активными (в настоящее время происходит ошибка), либо неактивными (некоторое время ошибка была активной, но в настоящее время она не активна).

Активные коды неисправностей можно прочитать с помощью предупреждающих ламп в кабине автомобиля или электронного инструментария обслуживания INSITETM. Неактивные ошибки можно **только **просматривать с помощью инструментария электронного обслуживания INSITETM.

![[19800562.png]]

Если красная лампа включается во время работы двигателя, возникает неисправность, которая может привести к серьезным повреждениям двигателя. Остановите двигатель как можно скорее.

Если желтый предупредительный фонарь зажжет, то двигатель все равно можно будет эксплуатировать. Этот тип неисправности может быть исправлен на следующем запланированном мероприятии по техническому обслуживанию.

![[19800563.png]]

Синий светильник указывает на проблему системы CENSETM. Эти неисправности не влияют на производительность двигателя, но снижают способность системы CENSETM обнаруживать проблемы с двигателем.

![[19800564.png]]

Когда замок зажигания автомобиля включается, все лампы будут гореть в течение 2 секунд, чтобы показать, что они работают.

![[19800565.png]]

Через две секунды после срабатывания лампы желтая предупредительная лампа начнет выдавать все активные коды неисправностей, если есть какие-либо активные коды неисправностей.

![[19800566.png]]

Цифры для активных кодов неисправностей будут отображаться в следующей последовательности. Желтая лампа будет выдавать цифры активных кодов неисправностей.

В данном коде неисправности будет 2-секундная задержка между цифрами и 3-секундная задержка между различными кодами неисправностей.

Активные коды неисправностей будут продолжать мигать до тех пор, пока включен переключатель зажигания автомобиля.

![[19800567.png]]

Процедуры устранения неисправностей кода ошибок содержатся в разделе TF настоящего руководства.

Процедуры устранения неисправностей кода неисправности также можно найти в информационной системе по неисправностям INSITETM.

Ссылка на Руководство пользователя INSITETM для получения дополнительной информации.

![[19400340.png]]

Деталог кода ошибки

Когда диагностический код неисправности записывается в ECM, значения определенных значений датчика фиксируются в журнале данных моментального снимка. В этом журнале данных регистрируются значения датчиков за определенный период до и после возникновения неисправности. Для получения дополнительной информации о функции журнала данных кода ошибки, обратитесь к Руководству пользователя INSITETM.

![[19400357.png]]

### Система защиты двигателя

Если система CENSETM обнаруживает проблему с двигателем, все, что она может сделать, это включить предупредительную лампу в кабине автомобиля и передать неисправность по системе модульной добычи, если она установлена.

![[19800568.png]]

### Системные компоненты CENSETM

Система CENSETM предназначена для мониторинга и записи широкого спектра параметров работы двигателя. Существуют параметры, которые являются уникальными для системы CENSETM, а также параметры, которые должны быть совместно использованы с контроллером топливной системы двигателя.

![[19800569.png]]

Ввод модуля управления двигателем

Следующие датчики будут доступны только с CENSETM на двигателе QSK45 CENSETM или QSK60 CENSETM:

1. Предфильтровый и постфильтровый датчик давления масла
2. J1939 - канальная шина данных
3. Компрессор с турбокомпрессором впускной датчик температуры
4. Датчик температуры отработавших газов
5. Датчик температуры масла.

![[19802670.png]]

Система CENSETM может принимать информацию о датчиках через шину данных J1939 CAN. Система CENSETM может обойтись без определенных датчиков, если желаемая информация передается по шине данных J1939 CAN системой двигателя ECM.

Система CENSETM **только** получает информацию на этой шине данных CAN. CENSETM ECM **не может** передавать информацию через шину данных J939 CAN.

![[19800573.png]]

Выходы модуля управления двигателем

CENSETM CM530 имеет следующие характеристики:

1. Предупреждающие лампы
2. RS422 CAN шина данных
3. RS232 CAN Data Bus (Шина данных).

CENSETM CM2330 имеет следующие характеристики:

1. Предупреждающие лампы
2. J1939 - канальная шина данных.

![[19800574.png]]

Шина данных RS422 CAN используется для связи с модульной системой майнинга и некоторыми другими электронными системами транспортных средств. Разъем шины данных CAN обычно расположен в кабине транспортного средства.

> [!note] Примечание
> Для двигателей с модулем CENSETM CM2330 потребуется модульная система майнинга J1939.

![[cent337.png]]

Для CENSETM CM530: Шина данных RS232 CAN используется для связи с инструментами электронного обслуживания INSITETM. Эта шина данных CAN расположена на ремне электропроводки двигателя и, как правило, также находится в кабине автомобиля.

Для CENSETM CM2330: Шина данных J1939 CAN используется для связи с инструментами электронного обслуживания INSITETM. Эта шина данных CAN расположена на ремне электропроводки двигателя.

![[19400357.png]]

### Монитор технического обслуживания

Система CENSETM имеет функцию мониторинга технического обслуживания, которая контролирует интервалы изменения для топливного фильтра, моторного масла, фильтров моторного масла, охлаждающей жидкости и фильтров охлаждающей жидкости. Ссылка на электронный сервис INSITETM, инструмент Руководство пользователя для получения дополнительной информации.

![[ff6etha.png]]

### Часы реального времени

CENSE ECM имеет часы реального времени, которые можно установить в местное время суток. ECM записывает время суток, когда происходят события. Например, ECM будет записывать точное время суток, когда был зарегистрирован код ошибки.

![[nobox.png]]

### Мониторинг возможностей

Инструменты электронного обслуживания INSITETM могут использоваться для мониторинга любого из датчиков CENSETM в режиме реального времени во время работы двигателя.

![[19400357.png]]


> [!quote]- Original (English) · английский оригинал
> ### CENSE™ System Description
>
> The CENSE™ system is an electronic engine monitoring system. This system is used primarily to provide enhanced engine diagnostics and to record engine operating data over time.
>
> The CENSE™ engine control module (ECM) is physically identical to some other Cummins® engine control modules (ECMs). Refer to the ECM part numbers to tell the difference between ECMs. The ECM part number is shown on the ECM external dataplate.
>
> The CENSE™ system operates similarly to any other Cummins® electronic system and measures many of the same temperatures and pressures. In addition, the CENSE™ system measures some additional parameters such as exhaust temperatures and differential pressures across filters.
>
> The CENSE™ system uses a thermocouple mounted in the exhaust port of each cylinder to measure the exhaust gas temperature. A low exhaust temperature indicates that the cylinder is low on power. A high exhaust temperature indicates that the cylinder is receiving too much fuel.
>
> The CENSE™ system measures a number of differential pressures on the engine. By measuring the pressure drop across a filter, the CENSE™ system can tell when a filter needs to be changed.
>
> There are two generations of CENSE™ systems. The CENSE™ CM530 and the next generation, CENSE™ CM2330.
>
> The CENSE™ CM530 module features J1587 communication and supports the RS422 and RS232 interfaces. INSITE™ electronic service tool for CENSE™ **must** be used to communicate with this module.
>
> The CENSE™ CM2330 module features J1939 communication. The base INSITE™ electronic service tool **must** be used to communicate with this module.
>
> ### Programmable Features
>
> The CENSE™ system has been designed to be flexible to meet a wide variety of engine monitoring needs.
>
> Reference the INSITE™ Electronic Service Tool User's Manual for complete information on programmable features.
>
> ### Engine Trend Data
>
> The CENSE™ system is capable of storing engine operating information for later analysis. INSITE™ electronic service tool can be used to adjust the data sampling rate and to download the trend data.
>
> Reference the INSITE™ Electronic Service Tool User's Manual for more information.
>
> ### Diagnostic Fault Codes
>
> The CENSE™ system can display and record certain detectable fault conditions. These malfunctions are displayed as fault codes which makes troubleshooting easier. The fault codes are retained in the ECM.
>
> There are two types of fault codes. There are CENSE™ system faults and engine protection faults.
>
> CENSE™ system faults light the blue warning lamp. Engine protection faults light the red or yellow lamp.
>
> All fault codes recorded will either be active (fault is presently occurring) or inactive (the fault was active for some time, but it is **not** presently active).
>
> Active fault codes can be read using the warning lamps in the vehicle cab or INSITE™ electronic service tool. Inactive faults can **only** be viewed with INSITE™ electronic service tool.
>
> If the red lamp comes on while the engine is in operation, there is a fault occurring that can cause severe engine damage. Stop the engine in a safe manner as soon as possible.
>
> If the yellow warning lamp lights, the engine can still be operated. This type of failure can be repaired at the next scheduled maintenance event.
>
> The blue lamp indicates a CENSE™ system problem. These faults do **not** affect engine performance, but do reduce the ability of the CENSE™ system to detect engine problems.
>
> When the vehicle key switch is turned ON, all lamps will light for 2 seconds to show that they are working.
>
> Two seconds after the lamps go off, the yellow warning lamp will begin to flash out all active fault codes, if there are any active fault codes.
>
> The numbers for the active fault codes will flash out in the following sequence. The yellow lamp will flash out the digits of the active fault codes.
>
> There will be a 2 second delay between digits in a given fault code and a 3 second delay between different fault codes.
>
> Active fault codes will continue to flash out as long as the vehicle key switch is ON.
>
> The procedures for fault code troubleshooting are contained in Section TF of this manual.
>
> The fault code troubleshooting procedures can also be found in the INSITE™ Fault Information System.
>
> Reference the INSITE™ User's Manual for more information.
>
> Fault Code Datalog
>
> When a diagnostic fault code is recorded in the ECM, the values of certain sensor values are captured in a snapshot datalog. This datalog records sensor values for a certain period before and after the fault occurred. For more information on the fault code datalog feature, reference the INSITE™ User's Manual.
>
> ### Engine Protection System
>
> If the CENSE™ system detects an engine problem, all it can do is turn on the warning lamp in the vehicle cab and broadcast the fault over the Modular Mining system, if installed.
>
> ### CENSE™ System Components
>
> The CENSE™ system has been designed to monitor and record a wide variety of engine operating parameters. There are parameters that are unique to the CENSE™ system, as well as parameters that **must** be shared with the engine fuel system controller.
>
> Engine Control Module Inputs
>
> The following sensors will **only** be available with CENSE™ on a QSK45 CENSE™ or QSK60 CENSE™ engine:
>
> 1. Pre-filter and Post-filter Oil Pressure Sensor
> 2. J1939 Data Link
> 3. Turbocharger Compressor Inlet Temperature Sensor
> 4. Exhaust Temperature Sensor
> 5. Oil Pan Temperature Sensor.
>
> The CENSE™ system can receive sensor information over the J1939 data link. The CENSE™ system can do without certain sensors if the desired information is broadcast over the J1939 data link by the engine fuel system ECM.
>
> The CENSE™ system **only** receives information on this data link. The CENSE™ ECM **cannot** send information over the J939 data link.
>
> Engine Control Module Outputs
>
> The CENSE™ CM530 has the following outputs:
>
> 1. Warning Lamps
> 2. RS422 Data Link
> 3. RS232 Data Link.
>
> The CENSE™ CM2330 has the following outputs:
>
> 1. Warning Lamps
> 2. J1939 Data Link.
>
> The RS422 data link is used to communicate with the Modular Mining system and certain other vehicle electronic systems. The data link connector is typically located in the vehicle cab.
>
> **Note · Примечание**
> For engines with a CENSE™ CM2330 module, a J1939-capable Modular Mining system will have to be used.
>
> For CENSE™ CM530: The RS232 data link is used to communicate with the INSITE™ electronic service tool. This data link is located on the engine wiring harness and is typically also in the vehicle cab.
>
> For CENSE™ CM2330: The J1939 data link is used to communicate with INSITE™ electronic service tool. This data link is located on the engine wiring harness.
>
> ### Maintenance Monitor
>
> The CENSE™ system has a maintenance monitor feature that monitors the change intervals for the fuel filter, the lubricating oil, the lubricating oil filters, the coolant, and the coolant filters. Reference the INSITE™ Electronic Service Tool User's Manual for more information.
>
> ### Real-Time Clock
>
> The CENSE™ ECM has a real-time clock that can be set to the local time of day. The ECM records the time of day when events occur. For example, the ECM will record the exact time of day that a fault code was logged.
>
> ### Monitor Capabilities
>
> INSITE™ electronic service tool can be used to monitor any of the CENSE™ sensors in real time while the engine is running.
