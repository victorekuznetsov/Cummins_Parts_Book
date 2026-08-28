---
aliases:
  - "Описание системы"
type: "Процедура"
doc: "115-209-001-mrm-marpanel"
title_en: "System Description"
title_ru: "Описание системы"
modified: "2008-10-09"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-209-001-mrm-marpanel.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-209-001-mrm-marpanel.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# System Description
**Описание системы**

> [!abstract] Процедура · `115-209-001-mrm-marpanel`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section F — Familiarization
> **Даты:** изменён 2008-10-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-209-001-mrm-marpanel.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-209-001-mrm-marpanel.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Панельная система Marine C Command используется для мониторинга основных рабочих характеристик двигателя и управления локальными и удаленными функциями запуска и остановки.

Эта система получает информацию о данных двигателя и имеет возможность получать информацию о шине данных SAE J1939 CAN от ECM. Панельная система командования морской пехоты C состоит из следующих панелей:

- Интерфейсная коробка заказчика
- Пульт машинного отделения
- Дистанционный пульт.

Панельная система командования морской пехоты C может иметь перечисленные конфигурации:

- Интерфейс клиента **только**
- Клиентский интерфейс коробки и панели машинного отделения
- Коробка интерфейса клиента, панель машинного отделения и одна или несколько удаленных панелей (определяется общей длиной кабеля и общим током)
- Коробка интерфейса клиента и одна или несколько удаленных панелей (определяется общей длиной кабеля и общим током).

> [!note] Примечание
> Если панель машинного отделения **не используется, крышка перемычки **должна использоваться на разъеме C7 на окне интерфейса клиента.

Интерфейсная коробка заказчика

Коробка интерфейса клиента расположена в машинном отделении и принимает данные о двигателе от ECM через 16-контактные и 31-контактные разъемы. Двигатель получает команды запуска, остановки и остановки двигателя через окно интерфейса клиента.

Коробка интерфейса клиента содержит следующие компоненты:

- Логический блок интерфейса клиента
- Выключатели
- Терминальные полосы
- Кнопка остановки двигателя.

Логический блок клиентского интерфейса — обработка сигналов для панельной системы.

Выключатель цепи - предотвращает перегрузку системы.

Терминальные полосы - Обеспечивают точки подключения для проводов.

Кнопка остановки двигателя - позволяет прямому остановке двигателя от окна интерфейса клиента.

![[17800169.png]]

Конфигурация бокса интерфейса клиента, когда панель машинного отделения не используется

Если конфигурация панели **не** включает в себя панель машинного отделения, то на разъеме C7 окна интерфейса клиента должен быть установлен шортинг-разъем (1) *.

Интерфейсная коробка заказчика

Коробка интерфейса клиента имеет логический блок с пометкой CLU. Логический блок клиентского интерфейса расположен внутри клиентского интерфейса и управляет функциями панели управления Marine C Command. В этом блоке есть перечисленные лампы. Все лампы имеют соответствующие реле, которые позволяют подключить внешние компоненты, как определено OEM.

- 2.1.1.1 Предоставление 1 лампы (К1)
- 2-я лампа (К2) для подачи
- Огни остановки двигателя (K3)
- Локальная лампа (K4)
- Красная лампа (К5)
- Янтарная лампа (К6)
- Buzzer (K7)
- Белая лампа (K8)
- Бегущая лампа (K9)
- 85% номинальной лампы (K10).

1 лампа питания (K1) - Указывает напряжение, присутствующее для цепи питания 1.

2 лампа питания (K2) - Указывает напряжение, присутствующее для цепи питания 2.

Огни остановки двигателя (K3) - Указывает, что была начата функция прямой остановки двигателя.

Локальный режим лампы (K4) - Указывает, что панельная система находится в локальном режиме.

Красная лампа (K5) - указывает на выключение двигателя или ECM, который генерирует код сбоя.

Янтарная лампа (K6) - указывает, когда ECM генерирует код неисправности, который **не** выключает двигатель.

Buzzer (K7) - Указывает на наличие состояния зуммера. Может использоваться для активации сигнализации судна.

Белая лампа (K8) - указывает на наличие кода ошибки технического обслуживания.

Бегущая лампа (K9) - указывает на то, что двигатель работает.

85 процентов номинальной лампы (K10) - указывает, что двигатель работает на 85 процентах номинальной оборотной массы.

Логический блок клиентского интерфейса имеет статусную область, в которой есть лампы, перечисленные ниже:

- лампа с коленчатым вентилятором
- Стоп-сигнал
- Лампа для сохранения данных.

Лампа с коленчатым механизмом - указывает, что стартовая команда отправляется на стартер.

Стоп-лампа - указывает на то, что команда стоп отправляется в ECM.

Лампа сохранения данных - указывает, что команда сохранения данных отправляется в ECM.

Логический блок клиентского интерфейса имеет диагностическую область с перечисленными лампами и переключателями.

- Диагностический переключатель ON/OFF
- Диагностика лампы (зеленая)
- Переключатель накачки/декремента
- Красная лампа
- Янтарная лампа.

Диагностический переключатель ON/OFF - используется для размещения блока логики окна интерфейса клиента и ECM в диагностическом режиме. Диагностический режим может быть введен только при остановке двигателя.

Диагностическая лампа ON (зеленая) - Solid ON указывает, что логический блок окна интерфейса клиента находится в диагностическом режиме (диагностический переключатель ON / OFF включен и двигатель остановлен). Флешинговая лампа указывает, что Диагностический переключатель ON/OFF включен, но двигатель **не** остановлен; поэтому логический блок окна клиентского интерфейса может **не** входить в диагностический режим.

Переключатель нарастания/декремента - используется для выбора следующего кода неисправности для вспышки блока.

Красная лампа - выдает коды неисправностей ECM.

Янтарная лампа - вспышки, указывающие на начало нового кода неисправности ECM.

Логический блок клиентского интерфейса имеет набор DIP-коммутаторов, которые используются для установки обозначений двигателя на многомоторных приложениях. Они предназначены для одноразового ввода в эксплуатацию и расположены под крышкой на передней панели клиентского интерфейса. В настоящее время DIP-коммутаторы не используются в системе командной панели C.

Ручной отказ от защиты двигателя

Панельная система Marine C Command оснащена возможностью отменять команду отключения защиты двигателя от ECM. Если требуется функция переопределения защиты двигателя, OEM отвечает за установку переключателя.

Терминал защиты от переопределения двигателя расположен на терминальной полосе X4 в поле интерфейса клиента.

Когда переключатель оверрайда защиты двигателя активируется, сигнал отправляется в ECM через 31-контактный разъем, что позволяет ECM игнорировать выключение защиты двигателя.

Пульт машинного отделения

Панель машинного отделения расположена в машинном отделении и используется для мониторинга и контроля работы двигателя. Эта панель оснащена цифровым дисплеем ED3. Кроме того, панель машинного отделения оснащена кнопками и лампами.

- Выключатель питания/лампа (белый)
- Локальная кнопка «Пуск» **только**
- Огни сигнализации двигателя (красный)
- жужжание
- Кнопка запуска
- Локальный старт **только** лампа (желтый)
- Кнопка остановки
- Кнопка молчания.

Выключатель питания / лампа (белый) - включает ECM, панель машинного отделения и удаленную панель.

Локальный запуск **только** кнопка - когда кнопка находится в депрессии, позволяет запустить функцию **ТОЛЬКО** с панели машинного отделения.

Сигнальная лампа двигателя (красная) - при освещении указывает на наличие неисправности.

Buzzer - Поставляет звуковое указание на неисправность.

Пуск кнопки - Запуск двигателя.

Локальный пуск только лампы (желтый) - при освещении указывает, что двигатель может **только** быть запущен с панели машинного отделения.

Кнопка остановки - остановка двигателя.

Кнопка тишины - заглушает зуммер, когда сгенерировано состояние тревоги.

ED3 соединен с ECM через шину данных SAE J1939 CAN. ED3 будет указывать параметры работы двигателя и коды неисправностей.

Удалённая панель расположена в соответствии со спецификациями OEM и используется для мониторинга и управления работой двигателя. Эта панель может быть оснащена калибром или цифровым дисплеем ED3. Он также оснащен кнопками и лампами.

- Силовая лампа (белая)
- Локальный старт только лампа (янтарь)
- Огни сигнализации двигателя (красный)
- жужжание
- Кнопка запуска
- Кнопка остановки
- Кнопка молчания.

Силовая лампа (белая) - при освещении указывает, что удаленная панель имеет подачу питания.

Локальный пуск только лампы (янтаря) - при освещении указывается, что двигатель может **не** быть запущен с удаленной панели.

Сигнальная лампа двигателя (красная) - при освещении указывает на наличие неисправности.

Buzzer - Поставляет звуковое указание на неисправность.

Кнопка запуска - позволяет двигателю запускать, когда локальный запуск **только** лампа **не** освещена.

Кнопка остановки - остановка двигателя.

Кнопка тишины - заглушает зуммер, когда сгенерировано состояние тревоги.

ECM подает сигналы

Панельная система Marine C Command снабжается сигналами от двигателя ECM.

- Уровень масла в двигателе дистанционного резервуара сигнала
- Сигнал уровня охлаждения 1 (киль или теплообменник охлажден)
- Удаленный педаль акселератора или сигнал положения рычага
- 4.2.1.1 Педаль акселератора или сигнал положения рычага
- Педаль акселератора или рычаг холостого валидирования выключают сигнал
- Педаль акселератора или рычаг холостого валидационного переключателя на сигнал
- сигнал переключения
- 5.2.1.1 Защита двигателя от огня
- Предупреждающий сигнал лампы
- Сигнал лампы технического обслуживания
- Запасной пропорционметрический входной сигнал 1
- Сигнал тахометра
- Сигнал режима диагностического испытания
- Промежуточный сигнал управления скоростью/прироста холостого хода
- Промежуточный сигнал управления скоростью/уменьшения скорости
- Промежуточное управление скоростью 1/ удаленный сигнал PTO
- Промежуточная скорость/контроль 3/ валидационный сигнал переключателя
- Сигнал опровержения защиты двигателя
- SAE J1939: сигнал передачи данных шины
- SAE J1939 CAN Data Bus Return Сигнал возврата шины данных.

- Уровень масла в двигателе дистанционного резервуара сигнала
- Сигнал уровня охлаждения 1 (киль или теплообменник охлажден)
- Сигнал потенциометра с регулировкой петли
- Скорость генератора / нагрузка, управляющая сигналом смещения
- Сигнал переключения / Stop Switch
- Сигнал обнаружения неисправностей
- Общий сигнал выключения лампы
- Общий сигнал о сигнале сигнала сигнала
- Сигнал лампы замедления
- Сигнал режима диагностического испытания
- Диагностический сигнал приращения
- Диагностический сигнал декремента
- Сигнал переключателя переменной частоты
- 5.2.1.1 Сигнал переключателя с номинальным значением
- Сигнал тахометра
- Сигнал опровержения защиты двигателя
- SAE J1939: сигнал передачи данных шины
- SAE J1939: сигнал возврата шины данных
- Генератор выходной частоты регулирует потенциометрический сигнал.

Шина передачи данных Connectors

Cummins Inc. Сегодня производится много двигателей, которые управляются электронным способом. Эти двигатели имеют особые диагностические требования из-за ECM в системе. Для взаимодействия с этими ECM были разработаны инструменты электронного обслуживания, такие как инструмент электронного обслуживания INSITETM. INSITETM - это инструментальная система для электронных сервисов, которая взаимодействует с электронными двигателями с помощью шины данных CAN. Шина данных CAN обеспечивает физическое средство для передачи и сортировки электронных сигналов. Шина данных CAN состоит из специальной электронной схемы и электропроводки. Точки подключения для электронных сервисных инструментов также являются частью шины данных CAN. Ссылки на данные определяются стандартами, написанными Обществом автомобильных инженеров (SAE). Cummins Inc. Использует два таких стандарта для электронных средств обслуживания. Один из них представляет собой комбинацию SAE J1587/SAE J1708, а другой - SAE J1939. Двигатели могут поддерживать один или оба из этих стандартов шины данных CAN.

Рекомендуемый разъем шины данных CAN для двигателей Cummins® представляет собой 9-контактный разъем DeutschTM. Этот разъем может обеспечивать связь SAE J1587/SAE J1708 и SAE J1939 и напряжение батареи. Ниже приведены вырезы для 9-контактного разъема:

| Пин | сигнал |
|---|---|
| А. | Напряжение батареи 1 Возвращение |
| B | Напряжение батареи 1 Поставка |
| C | SAE J1939 CAN Data Bus Поставка данных |
| D | SAE J1939 Возвращение данных |
| Е | SAE J1939 CAN шина данных Shield |
| F | Не используется* |
| GGG | Не используется* |
| Hе | Не используется* |
| Джей | Не используется* |

![[19400739.png]]

Панель коммутации

![[15400069.png]]

Факультативная панель переключателей (Front View)

1. Переключение переключения
2. Альтернативный выключатель холостого хода
3. Выключатель промежуточной частоты вращения
4. RPM-переключатель / RPM-переключатель.

> [!note] Примечание
> Коммутационная панель является дополнительной панелью управления, которая обеспечивает легкую активацию определенных функций управления двигателем. Включает в себя вышеперечисленные переключатели.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The Marine C Command panel system is used to monitor basic engine operating characteristics and to control local and remote start and stop functions.
>
> This system receives engine data information and has the ability to receive SAE J1939 data link information from the ECM. The Marine C Command panel system is comprised of the following panels:
>
> - Customer interface box
> - Engine room panel
> - Remote panel.
>
> The Marine C Command panel system can have the listed configurations:
>
> - Customer interface box **only**
> - Customer interface box and engine room panel
> - Customer interface box, engine room panel, and one or more remote panels (determined by total cable length and total current draw)
> - Customer interface box and one or more remote panels (determined by total cable length and total current draw).
>
> **Note · Примечание**
> If the engine room panel is **not** used, a jumper cap **must** be used at connector C7 on the customer interface box.
>
> Customer Interface Box
>
> The customer interface box is located in the engine room and receives engine data from the ECM through 16-pin and 31-pin connectors. The engine receives start, stop, and engine stop commands through the customer interface box.
>
> The customer interface box contains the following components:
>
> - Customer interface box logic unit
> - Circuit breakers
> - Terminal strips
> - Engine stop button.
>
> Customer interface box logic unit - Signal processing for the panel system.
>
> Circuit breaker - Prevents system overcurrent draw.
>
> Terminal strips - Provide connection points for wires.
>
> Engine stop button- Allows direct engine stop from the customer interface box.
>
> Customer Interface Box Configuration When Engine Room Panel is Not Used
>
> If the panel configuration does **not** include an engine room panel, a shorting connector (1) **must** be installed at the C7 connector of the customer interface box.
>
> Customer Interface Box
>
> The customer interface box has a logic unit labeled CLU. The customer interface box logic unit is located inside the customer interface box and controls the functions of the Marine C Command panel system. This unit has the listed lamps. All lamps have associated relays that allow the connection of the external components, as determined by the OEM.
>
> - Supply 1 lamp (K1)
> - Supply 2 lamp (K2)
> - Engine stop lamp (K3)
> - Local mode lamp (K4)
> - Red lamp (K5)
> - Amber lamp (K6)
> - Buzzer (K7)
> - White lamp (K8)
> - Running lamp (K9)
> - 85 percent of rated lamp (K10).
>
> Supply 1 lamp (K1) - Indicates voltage is present for supply 1 circuit.
>
> Supply 2 lamp (K2) - Indicates voltage is present for supply 2 circuit.
>
> Engine stop lamp (K3) - Indicates that the direct engine stop function has been initiated.
>
> Local mode lamp (K4) - Indicates the panel system is in local mode.
>
> Red lamp (K5) - Indicates engine shutdown or ECM has generated a severe fault code.
>
> Amber lamp (K6) - Indicates when the ECM has generated a fault code that will **not** shut down the engine.
>
> Buzzer (K7) - Indicates a buzzer condition is present. Can be used to activate vessel alarm horn.
>
> White lamp (K8) - Indicates a maintenance fault code is present.
>
> Running lamp (K9) - Indicates the engine is running.
>
> 85 percent of rated lamp (K10) - Indicates the engine is running at 85 percent of rated rpm.
>
> The customer interface box logic unit has a status area that has lamps that are listed below:
>
> - Crank lamp
> - Stop lamp
> - Data save lamp.
>
> Crank lamp - Indicates a start command is being sent to the starter.
>
> Stop lamp - Indicates a stop command is being sent to the ECM.
>
> Data save lamp - Indicates a data save command is being sent to the ECM.
>
> The customer interface box logic unit has a diagnostic area with the listed lamps and switches.
>
> - Diagnostic ON/OFF switch
> - Diagnostic ON lamp (green)
> - Increment/Decrement switch
> - Red lamp
> - Amber lamp.
>
> Diagnostic ON/OFF switch - Used to place the customer interface box logic unit and the ECM in the diagnostic mode. Diagnostic mode can **only** be entered when the engine is stopped.
>
> Diagnostic ON lamp (green) - Solid ON indicates the customer interface box logic unit is in diagnostic mode (Diagnostic ON/OFF switch is ON and engine is stopped). Flashing lamp indicates the Diagnostic ON/OFF switch is ON, but the engine is **not** stopped; so the customer interface box logic unit can **not** enter diagnostic mode.
>
> Increment/Decrement switch - Used to select next fault code for unit to flash out. **Only** operational in diagnostic mode.
>
> Red lamp - Flashes out ECM fault codes. **Only** operational in diagnostic mode.
>
> Amber lamp - Flashes to indicate the start of a new ECM fault code. **Only** operational in diagnostic mode.
>
> The customer interface box logic unit has a set of DIP switches that are used to set engine designations on multi-engine applications. These are intended to be one-time set at commissioning and are located under a cover on the front of the customer interface box logic unit. The DIP switches are **not** used on the C Command panel system at this time.
>
> Engine Protection Shutdown Manual Override
>
> The Marine C Command panel system is equipped with the ability to override an engine protection shutdown command from the ECM. If the engine protection override function is desired, the OEM is responsible for the installation of the switch.
>
> The engine protection override terminal is located on the X4 terminal strip in the customer interface box.
>
> When the engine protection override switch is activated, a signal is sent to the ECM through the 31-pin connector, which allows the ECM to disregard the engine protection shutdown.
>
> Engine Room Panel
>
> The engine room panel is located in the engine room and is used to monitor and control the operation of the engine. This panel is equipped with an ED3 digital display. In addition, the engine room panel is equipped with buttons and lamps.
>
> - Power switch/lamp (white)
> - Local start **only** button
> - Engine alarm lamp (red)
> - Buzzer
> - Start button
> - Local start **only** lamp (yellow)
> - Stop button
> - Silence button.
>
> Power switch/lamp (white) - Turns on ECM, engine room panel, and remote panel.
>
> Local start **only** button - When button is depressed, allows start function **ONLY** from engine room panel.
>
> Engine alarm lamp (red) - When illuminated, indicates a fault condition is present.
>
> Buzzer - Supplies an audible fault indication.
>
> Start button - Starts the engine.
>
> Local start only lamp (yellow) - When illuminated, indicates the engine can **only** be started from the engine room panel.
>
> Stop button - Stops the engine.
>
> Silence button - Silences the buzzer when an alarm condition has been generated.
>
> The ED3 is connected with the ECM through a SAE J1939 data link. The ED3 will indicate engine operating parameters and fault codes.
>
> The remote panel is located per OEM specifications and is used to monitor and control the operation of the engine. This panel can be equipped with a gauge set or ED3 digital display. It is also equipped with buttons and lamps.
>
> - Power lamp (white)
> - Local start only lamp (amber)
> - Engine alarm lamp (red)
> - Buzzer
> - Start button
> - Stop button
> - Silence button.
>
> Power lamp (white) - When illuminated, indicates the remote panel has power supplied.
>
> Local start only lamp (amber) - When illuminated, indicates the engine can **not** be started from the remote panel.
>
> Engine alarm lamp (red) - When illuminated, indicates a fault condition is present.
>
> Buzzer - Supplies an audible fault indication.
>
> Start button - Allows engine start when the local start **only** lamp is **not** illuminated.
>
> Stop button - Stops the engine.
>
> Silence button - Silences the buzzer when an alarm condition has been generated.
>
> ECM Supplied Signals
>
> The Marine C Command panel system is supplied signals from the engine ECM.
>
> - Engine oil level remote reservoir signal
> - Coolant level 1 signal (keel or heat exchanger cooled)
> - Remote accelerator pedal or lever position signal
> - Accelerator pedal or lever position signal
> - Accelerator pedal or lever idle validation switch off signal
> - Accelerator pedal or lever idle validation switch on signal
> - OEM switch signal
> - Engine protection stop lamp signal
> - Warning lamp signal
> - Maintenance lamp signal
> - Spare ratiometric input 1 signal
> - Tachometer signal
> - Diagnostic test mode signal
> - Intermediate speed control/idle increment signal
> - Intermediate speed control/idle decrement signal
> - Intermediate speed control 1/remote PTO signal
> - Intermediate speed/control 3/validate switch signal
> - Engine protection override signal
> - SAE J1939 data link supply signal
> - SAE J1939 data link return signal.
>
> - Engine oil level remote reservoir signal
> - Coolant level 1 signal (keel or heat exchanger cooled)
> - Droop adjust potentiometer signal
> - Generator speed/load governing bias signal
> - Run/stop switch signal
> - Fault acknowledge signal
> - Common shutdown lamp signal
> - Common warning lamp signal
> - Over speed shutdown lamp signal
> - Diagnostic test mode signal
> - Diagnostic increment signal
> - Diagnostic decrement signal
> - Alternate frequency switch signal
> - Idle/rated switch signal
> - Tachometer signal
> - Engine protection override signal
> - SAE J1939 data link supply signal
> - SAE J1939 data link return signal
> - Generator output frequency adjust potentiometer signal.
>
> Datalink Connectors
>
> Cummins Inc. produces many engines today that are electronically controlled. These engines have special diagnostic requirements because of the ECM in the system. To interface with these ECMs, electronic service tools have been developed, such as INSITE™ electronic service tool. INSITE™ electronic service tool interfaces with the electronic engines by means of a data link. A data link provides a physical means for transmitting and sorting electronic signals. A data link consists of special electronic circuitry and electrical harnesses. Connection points for electronic service tools are also part of the data link. Data links are defined by standards written by the Society of Automotive Engineers (SAE). Cummins Inc. uses two such standards for electronic service tools. One is a combination of SAE J1587/SAE J1708 and the other is SAE J1939. Engines can support one or both of these data link standards.
>
> The recommended data link connector for Cummins® engines is a 9-pin Deutsch™ connector. This connector can supply SAE J1587/SAE J1708 and SAE J1939 communications and battery voltage. The following are pin-outs for the 9-pin connector:
>
> | Pin | Signal |
> |---|---|
> | A | Battery Voltage 1 Return |
> | B | Battery Voltage 1 Supply |
> | C | SAE J1939 Data Link Supply |
> | D | SAE J1939 Data Link Return |
> | E | SAE J1939 Data Link Shield |
> | F | **Not** Used |
> | G | **Not** Used |
> | H | **Not** Used |
> | J | **Not** Used |
>
> Switch Panel
>
> Optional Switch Panel (Front View)
>
> 1. Shutdown override switch
> 2. Alternate idle switch
> 3. Intermediate speed control switch
> 4. RPM increment/decrement switch.
>
> **Note · Примечание**
> The switch panel is an optional control panel that provides easy activation of certain engine control features. It includes the above switches.
