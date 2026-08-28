---
aliases:
  - "Идентификация компонентов"
type: "Процедура"
doc: "97-208-001"
title_en: "Component Identification"
title_ru: "Идентификация компонентов"
modified: "2007-01-29"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
  - "3666422"
figures: 19
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-208-001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-208-001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Component Identification
**Идентификация компонентов**

> [!abstract] Процедура · `97-208-001`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]], [[3666422 — ICON™ Idle Control System|3666422]]
> **Секции:** Section E - Component Identification · Section E - System Identification
> **Даты:** изменён 2007-01-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-208-001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-208-001.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система ICONTM

Система контроля холостого хода ICONTM является необязательным или послепродажным продуктом, который предназначен для сокращения чрезмерного времени простоя при выполнении следующих задач:

- Сохранение температуры моторного масла выше 16 ° C \[60 ° F \] в холодных погодных условиях
- Держать батареи полностью заряженными в любое время
- Поддержание желаемой температуры внутри кабины. (Этой функцией требуется установка термостата кабины.)

Вся система ICONTM состоит из следующих компонентов:

1. Кабина термостата
2. Датчик температуры окружающего воздуха
3. Лампа ICON™
4. Dash Relay (необязательно)
5. Нейтральный переключатель положения
6. Переключатель тормозов
7. Реле 1 и 2 шины зажигания
8. ICONTM cab Wiring Grund
9. Узлы для проводов двигателя ICONTM
10. Снаряд термостата кабины
11. Сенсор температуры проводка жгут
12. Модуль управления ICONTM
13. Начать эстафету
14. Тревога двигателя
15. Переключатель наклона копыт (не ртуть)

### Cab Thermostat

Термостат кабины - это устройство, которое позволяет пользователю устанавливать температуру внутри кабины. Когда температура превышает либо высокий, либо низкий температурный порог, термостат кабины направляет систему ICONTM на запуск и запуск двигателя до тех пор, пока желаемая температура внутри кабины не будет восстановлена. Термостат кабины обычно устанавливается внутри зоны кабины кабины.

При первоначальном включении термостата кабины термостат будет отображать уровень доработки программного обеспечения, загруженного в термостат, то есть «01», «02», «03» и т.д.

| Идентификация компонентов |  |
|---|---|
| компонент | Уровень пересмотра |
| ICONTM Idle Control модуль | 11, 14, 15, 16, 18 или 19 |
| Термостат | 01, 02, 03, 04, 05 или 06 |

Любая модификация модуля управления ICONTM совместима с любой модификацией термостата ICONTM, хотя может потребоваться изменение проводов.

![[15800001.png]]

### Датчик температуры окружающего воздуха

Датчик температуры окружающего воздуха - это датчик, установленный снаружи кабины под пятым колесом. Датчик подключен к термостату кабины. Датчик позволяет системе ICONTM использовать температуру окружающего воздуха в качестве фактора при определении времени работы двигателя.

![[15800014.png]]

### Лампа ICON™

Лампа ICONTM обеспечивает визуальный дисплей, который показывает состояние системы ICONTM. В зависимости от состояния системы ICONTM лампа либо будет светиться стабильно, либо будет мигать определенными узорами, либо останется выключенной. Лампа ICONTM установлена на приборной панели.

> [!note] Примечание
> Светодиод может **только **использоваться с ICONTM бездействия модуль управления ревизия 18.

![[15800003.png]]

### Dash Relay

Реле приборной панели позволяет системе ICONTM и двигателю ECM быть изолированными от электронного приборного панели, в то время как система ICONTM активна, но шина зажигания не работает.

Реле тире устанавливается, когда электронные тире мешают работе системы ICONTM. Установка реле приборов **не** влияет на нормальную работу приборов, когда система ICONTM **не** активна.

![[15800013.png]]

### Нейтральный переключатель позиции

Переключатель нейтрального положения — это устройство, которое устанавливается на трансмиссию транспортного средства. Переключатель нейтрального положения позволяет системе ICONTM знать, находится ли трансмиссия автомобиля в передаче или в нейтральной. Переключатель закрывается, когда передача находится в нейтральной зоне, и открыт, когда передача находится в передаче. Система ICONTM будет **не** запускать двигатель или становиться активной, если трансмиссия не находится в положении NEUTRAL.

![[15800006.png]]

### Переключатель тормозов

Переключатель стояночного тормоза - это устройство, которое устанавливается в линии стояночного тормоза транспортного средства под тире за ручным клапаном. Переключатель стояночного тормоза позволяет системе ICONTM знать, установлен или выпущен стояночный тормоз транспортного средства. Переключатель закрывается, когда парковочные тормоза включены, и переключатель открывается, когда парковочные тормоза выключены. Система ICONTM будет **не** запускать двигатель или становиться активной, если не установлен стояночный тормоз.

![[15800011.png]]

### шинный реле 1 и 2

Реле 1 и 2 шины зажигания представляют собой реле, которые позволяют системе ICONTM автоматически управлять цепью зажигания OEM. В обычных условиях оператор передает питание цепям транспортного средства, включив переключатель зажигания. Система ICONTM, будучи активной, управляет этими цепями с помощью реле шины зажигания. Хотя набор ICONTM включает в себя **только** одно реле (реле 1 шины зажигания), второе реле (реле 2 шины зажигания) может быть установлено для управления несколькими пакетами аксессуаров. Реле 1 и 2 зажигания монтируются под приборной панелью.

![[15800002.png]]

### ICONTM Cab Wiring Grund

Послепродажный рынок

Связь проводов ICONTM соединяет все компоненты системы ICONTM внутри кабины. Кабина проводов жгута подключена к ICONTM двигатель проводов жгута с проходным разъемом на брандмауэр автомобиля.

![[15800009.png]]

### Узлы для проводов двигателя ICONTM

Послепродажный рынок

Связь с проводкой двигателя ICONTM соединяет все компоненты системы ICONTM в отсеке двигателя. Снаряд для проводов двигателя ICONTM также обеспечивает первичную мощность и заземление системы ICONTM.

![[15800010.png]]

### Cab Thermostat Jumper - электропроводка

Послепродажный рынок

Кабина термостата проводка ремень соединяет кабину проводка ремень кабины термостат.

![[15800073.png]]

### Сенсор температуры проводка жгут

Послепродажный рынок

Связь с датчиком температуры соединяет термостат кабины с датчиком температуры окружающего воздуха.

![[15800072.png]]

### ICONTM Idle Control модуль

Послепродажный рынок

Модуль управления ICONTM представляет собой небольшой мощный компьютер, который управляет системой ICONTM. Модуль управления ICONTM idle взаимодействует со всеми переключателями системы ICONTM и двигателем ECM на шине данных J1587 CAN для сбора данных и отправки команд. Модуль управления ICONTM idle управляет скоростью холостого хода, временем холостого хода, запуском и остановкой двигателя, мощностью шины зажигания и общим управлением системы ICONTM. Модуль управления ICONTM холостого хода установлен на брандмауэре автомобиля.

Диаграмма модуля управления ICONTM расположена на передней части модуля управления и в верхнем левом углу. В нем содержится следующее:

1. P/N - номер модуля управления холостым режимом ICONTM
2. S/N - ICONTM модуль управления холостым ходом серийный номер

![[19803433.png]]

### Стартовая ретрансляция

Реле стартера используется системой ICONTM для активации стартера двигателя. Поскольку запуск двигателя является автоматическим, модуль управления холостым ходом использует реле стартера для включения стартера без необходимости оператора нажимать кнопку запуска или поворачивать ключ. Стартерная реле установлена на брандмауэре автомобиля.

![[15800004.png]]

### Тревога запустения двигателя

Перед автоматическим запуском двигателя система ICONTM вызывает сигнал тревоги (если включен). Эта тревога предупреждает любого, кто находится рядом с двигателем, что двигатель вот-вот запустится. Система ICONTM позволяет сотрудникам во время сигнализации удаляться от мест, которые могут привести к травмам при запуске двигателя. Тревога запуска двигателя установлена на брандмауэре автомобиля.

![[15800007.png]]

### Hood Tilt коммутатор

> [!danger] ОПАСНО
> Некоторые переключатели наклона капота содержат ртуть, химическое вещество, известное некоторым государственным и федеральным агентствам, которое вызывает врожденные дефекты или другой репродуктивный вред. Не утилизируйте. Переработка в соответствии с государственными правилами.

Переключатель наклона капота - это предохранительное устройство, которое установлено на капоте автомобиля. Переключатель наклона капота позволяет системе ICONTM знать, открыт ли капот автомобиля или закрыт. Система ICONTM будет **не** запускать двигатель или быть активной, если капот не закрыт.

> [!note] Примечание
> Некоторые нертутные выключатели наклона капота могут поставляться без скобки.

![[15800005.png]]

### Тормозная проводка двигателя

интегрированный

Требуется установка тормозной проводов двигателя ICONTM для двигателей Signature и ISX Series **только**. Тормозная проводка двигателя уменьшает количество возможных уровней тормозов двигателя с шести до трех. Это позволяет использовать драйверы приращения и сужения для систем ICONTM на двигателях Signature и ISX Series.

1. 2.1.1 Разъемы тормозов двигателя
2. Разъем для проводов ремня электропитания

![[19c01037.png]]

### Список компонентов

Послепродажный рынок

![[19802979.png]]

ICONTM Cab Wiring Grund и Mating Components and Connections

1. Кабина термостата \*
2. Схема электропроводки термостата
3. Коннектор электропроводки ремня термостата
4. Датчик температуры окружающего воздуха
5. Сенсор температуры проводка жгут
6. 14-контактная переборка проезда
7. Шина передачи данных CAN сплайс проводная
8. Лампа ICONTM и разъем
9. Переключатель и разъем тормозов
10. Зажимная коробка с зажимом
11. Щелкание проводов переключателя зажигания
12. 3.3.1.1 Узел переключателя зажигания
13. Реле и разъем шины зажигания
14. Узлы для проводов двигателя ICONTM
15. Шина зажигания для электрических цепей OEM.

\* Требуется Cummins Inc. поставленная часть

![[19803843.png]]

ICONTM - электропроводка двигателя, компоненты и соединения для сопряжения

1. ICONTM модуль управления холостым ходом*
2. ICONTM модуль управления холостым ходом и разъёмы жгута проводов
3. Тревога двигателя
4. Разъем аварийной сигнализации двигателя
5. Нейтральный переключатель положения и разъем
6. Двигатель ECM и модуль управления ICONTM холостого хода сплайс-проволока (провод переключателя зажигания)
7. Стартовый реле и разъем
8. ICONTM Engine Wiring Wang Fuse Holder (Флакон-схема)
9. Переключатель наклона копыт
10. Разъем переключателя наклона крючка
11. 14-контактный переборочный переборочный разъем
12. Разъемы терминалов аккумуляторов
13. Упряжка для проводов кабины.

\* Требуется Cummins Inc. поставленная часть

интегрированный

![[19803460.png]]

ICONTM OEM Поставленная электропроводка и поставляемые детали Cummins в соответствии с требованиями

1. Двигатель OEM Wiring Silge
2. Ремень привода двигателя
3. Двигатель датчика проводов жгута
4. 31-контактный OEM-разъем
5. Эстафета старта
6. Переключатель и разъем тормозов
7. Запуск сигнализации и разъема*
8. Нейтральный переключатель положения и разъем
9. Переключатель наклона копыт
10. Лампа ICONTM и разъем
11. Тормозная проводка ICONTM
12. Ретранслятор шины зажигания
13. Датчик температуры окружающего воздуха и электропроводка \*
14. Кабина термостата*
15. Разъем Bulkhead

\* Требуется Cummins Inc. поставленная часть


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> ICON™ System
>
> ICON™ idle control system is an optional or aftermarket product that is designed to reduce excessive idle time when accomplishing the following tasks:
>
> - Keeping the engine oil temperature above 16°C \[60°F\] in cold weather environments
> - Keeping the batteries fully charged at all times
> - Maintaining a desired temperature inside the cab. (This feature requires the cab thermostat to be installed.)
>
> The complete ICON™ system consists of the following components:
>
> 1. Cab thermostat
> 2. Ambient air temperature sensor
> 3. ICON™ lamp
> 4. Dash relay (optional)
> 5. Neutral position switch
> 6. Parking brake switch
> 7. Ignition bus relay 1 and 2
> 8. ICON™ cab harness
> 9. ICON™ engine harness
> 10. Cab thermostat harness
> 11. Temperature sensor harness
> 12. ICON™ idle control module
> 13. Start relay
> 14. Engine start alarm
> 15. Hood tilt switch (non-mercury)
>
> ### Cab Thermostat
>
> The cab thermostat is a device that allows the user to set the temperature inside the cab. When the temperature exceeds either the high or low temperature threshold, the cab thermostat directs the ICON™ system to start and run the engine until the desired temperature inside the cab has been reestablished. The cab thermostat is typically mounted inside the bunk area of the cab.
>
> At initial turn-on of the cab thermostat, the thermostat will display the revision level of the software loaded in the thermostat, that is “01”, “02”, “03”, and so forth.
>
> | Component Identification |  |
> |---|---|
> | Component | Revision Level |
> | ICON™ Idle Control Module | 11, 14, 15, 16, 18, or 19 |
> | Thermostat | 01, 02, 03, 04, 05, or 06 |
>
> Any revision of the ICON™ control module is compatible with any revision of the ICON™ thermostat, although a wiring change can possibly be required.
>
> ### Ambient Air Temperature Sensor
>
> The ambient air temperature sensor is a sensor mounted outside the cab, under the fifth wheel. The sensor is connected to the cab thermostat. The sensor allows the ICON™ system to use the ambient air temperature as a factor in determining when to operate the engine.
>
> ### ICON™ Lamp
>
> The ICON™ lamp provides a visual display that shows the status of the ICON™ system. Depending on the status of the ICON™ system, the lamp either will illuminate steadily, will flash in certain patterns, or will remain off. The ICON™ lamp is mounted on the dash.
>
> **Note · Примечание**
> A LED can **only** be used with ICON™ idle control module revision 18.
>
> ### Dash Relay
>
> The dash relay allows the ICON™ system and engine ECM to be isolated from the electronic dash while the ICON™ system is active but the ignition bus is unpowered.
>
> The dash relay is installed when electronic dashes interfere with the ICON™ system operation. The installation of the dash relay does **not** affect normal dash operation when the ICON™ system is **not** active.
>
> ### Neutral Position Switch
>
> The neutral position switch is a device that is installed on the vehicle's transmission. The neutral position switch lets the ICON™ system know whether the vehicle's transmission is in gear or in neutral. The switch is closed when the transmission is in neutral, and is open when the transmission is in gear. The ICON™ system will **not** start the engine or become active unless the transmission is in the NEUTRAL position.
>
> ### Parking Brake Switch
>
> The parking brake switch is a device that is installed in the vehicle's parking brake line under the dash behind the hand valve. The parking brake switch lets the ICON™ system know whether the vehicle's parking brake is set or released. The switch closes when the parking brakes are on and the switch opens when the parking brakes are off. The ICON™ system will **not** start the engine or become active unless the parking brake is set.
>
> ### Ignition Bus Relay 1 and 2
>
> The ignition bus relay 1 and 2 are relays that allow the ICON™ system to control the OEM ignition circuit automatically. Under normal conditions, the operator sends power to the vehicle's circuits by turning the keyswitch on. The ICON™ system, while active, controls these circuits with the ignition bus relays. Though the ICON™ kit includes **only** one relay (ignition bus relay 1), a second relay (ignition bus relay 2) can be installed to control multiple accessory packages. The ignition bus relay 1 and 2 are mounted under the dash.
>
> ### ICON™ Cab Harness
>
> Aftermarket
>
> The ICON™ cab harness connects all of the ICON™ system components inside the cab. The cab harness is connected to the ICON™ engine harness with a pass-through connector at the vehicle firewall.
>
> ### ICON™ Engine Harness
>
> Aftermarket
>
> The ICON™ engine harness connects all of the ICON™ system components in the engine bay. The ICON™ engine harness also provides primary power and grounding for the ICON™ system.
>
> ### Cab Thermostat Jumper Harness
>
> Aftermarket
>
> The cab thermostat harness connects the cab harness to the cab thermostat.
>
> ### Temperature Sensor Harness
>
> Aftermarket
>
> The temperature sensor harness connects the cab thermostat to the ambient air temperature sensor.
>
> ### ICON™ Idle Control Module
>
> Aftermarket
>
> The ICON™ idle control module is a small, powerful computer that controls the ICON™ system. The ICON™ idle control module communicates with all the ICON™ system switches and the engine ECM on the J1587 datalink to gather data and send commands. The ICON™ idle control module controls idle speed, idle time, engine starting and stopping, ignition bus power, and overall ICON™ system control. The ICON™ idle control module is mounted on the firewall of the vehicle.
>
> The ICON™ idle control module's dataplate is located on the front of the idle control module and in the upper left corner. It contains the following:
>
> 1. P/N - ICON™ idle control module part number
> 2. S/N - ICON™ idle control module serial number
>
> ### Starter Relay
>
> The starter relay is used by the ICON™ system to engage the engine starter. Since the engine start is automatic, the idle control module uses the starter relay to engage the starter without the necessity of an operator to push the start button or turn the key. The starter relay is mounted on the firewall of the vehicle.
>
> ### Engine Start Alarm
>
> Prior to automatic engine starting, the ICON™ system sounds the engine start alarm (if enabled). This alarm warns anyone near the engine that the engine is about to start. The ICON™ system allows time during this alarm for personnel to move away from places that could cause personal injury when the engine starts. The engine start alarm is mounted on the firewall of the vehicle.
>
> ### Hood Tilt Switch
>
> **WARNING · Опасно**
> Some hood tilt switches contain Mercury, a chemical known to some state and federal agencies to cause birth defects or other reproductive harm. Do not dispose. Recycle in accordance with state regulations.
>
> The hood tilt switch is a safety device that is installed on the vehicle's hood. The hood tilt switch lets the ICON™ system know whether the vehicle's hood is open or closed. The ICON™ system will **not** start the engine or be active unless the hood is closed.
>
> **Note · Примечание**
> Some non-mercury hood tilt switches can be supplied without a bracket.
>
> ### Engine Brake Harness
>
> Integrated
>
> The ICON™ engine brake harness is required for Signature and ISX Series engines **only**. The engine brake harness reduces the number of possible engine brake levels from six to three. This allows increment and decrement drivers for ICON™ system use on Signature and ISX Series engines.
>
> 1. Engine brake connectors
> 2. Engine Brake harness connector
>
> ### Component List
>
> Aftermarket
>
> ICON™ Cab Harness and Mating Components and Connections
>
> 1. Cab thermostat \*
> 2. Thermostat jumper harness
> 3. Thermostat jumper harness connector
> 4. Ambient air temperature sensor
> 5. Temperature sensor harness
> 6. 14-pin bulkhead pass-through
> 7. Datalink splice wired
> 8. ICON™ lamp and connector
> 9. Parking brake switch and connector
> 10. Cab harness fuse holder
> 11. Keyswitch splice wires
> 12. Keyswitch assembly
> 13. Ignition bus relays and connector
> 14. ICON™ engine harness
> 15. Ignition bus for OEM electrical circuits.
>
> \* Required Cummins Inc. supplied part
>
> ICON™ Engine Harness, Mating Components and Connections
>
> 1. ICON™ idle control module \*
> 2. ICON™ idle control module and harness connectors
> 3. Engine start alarm
> 4. Engine start alarm connector
> 5. Neutral position switch and connector
> 6. Engine ECM and ICON™ idle control module splice wire (keyswitch input wire)
> 7. Starter relay and connector
> 8. ICON™ engine harness fuse holder
> 9. Hood tilt switch
> 10. Hood tilt switch connector
> 11. 14-pin bulkhead pass-through connector
> 12. Battery terminal connectors
> 13. Cab harness.
>
> \* Required Cummins Inc. supplied part
>
> Integrated
>
> ICON™ OEM Supplied Harness and Cummins Supplied Parts As Required
>
> 1. Engine OEM harness
> 2. Engine actuator harness
> 3. Engine sensor harness
> 4. 31-pin OEM connector
> 5. Starter relay
> 6. Parking brake switch and connector
> 7. Start alarm and connector\*
> 8. Neutral position switch and connector
> 9. Hood tilt switch
> 10. ICON™ lamp and connector
> 11. ICON™ engine brake harness
> 12. Ignition bus relay
> 13. Ambient air temperature sensor and harness\*
> 14. Cab thermostat\*
> 15. Bulkhead connector
>
> \* Required Cummins Inc. supplied part
