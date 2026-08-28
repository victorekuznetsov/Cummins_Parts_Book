---
aliases:
  - "Идентификация компонентов"
type: "Процедура"
doc: "116-208-001"
title_en: "Component Identification"
title_ru: "Идентификация компонентов"
modified: "2008-11-21"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
  - "4021618"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-208-001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-208-001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Component Identification
**Идентификация компонентов**

> [!abstract] Процедура · `116-208-001`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]], [[4021618 — C Command Elite and C Command Elite Plus Panel System Marine Owners Manual|4021618]]
> **Секции:** Section E - Engine and System Identification
> **Даты:** изменён 2008-11-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-208-001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-208-001.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

![[17800172.png]]

Интерфейсная коробка заказчика

1. Интерфейсная коробка заказчика
2. Дизельный блок 410 управления
3. Выключатель остановки двигателя
4. Механизм блокировки
5. Переключатель питания.

![[17800173.png]]

Вид спереди: Дизельный блок 410 управления

1. Дисплейный блок
2. Кнопка запуска
3. Кнопка остановки
4. Мягкие кнопки
5. Вниз по стрелке
6. Кнопка меню
7. Кнопка стрелка вверх
8. Кнопка сигнализации
9. Диод, излучающий свет.

![[00400366.png]]

Задний обзор - Дизельный блок 410 управления

1. Настраиваемые выходные сигналы для реле и сигнализации
2. Ком 1, 2, 3, 4 и 5 входов сигналов ModbusTM
3. Входные сигналы датчика
4. 1-8 коммутаторов входов
5. Электропитание блока управления дизельным топливом
6. Критические сигналы, поступающие в блок управления дизельным двигателем.

![[17800174.png]]

Front View - удаленная панель

1. Диод с излучающим светом
2. Дисплейная панель
3. Кнопка сигнализации
4. Кнопка меню
5. Кнопка запуска
6. Кнопка остановки
7. Кнопка "Домой".

![[00400367.png]]

Задний вид - удаленная панель

1. Электропитание для удаленной панели
2. Переключите входной сигнал на сигнал тревоги
3. 1 выход сигнала реле для активной станции
4. Выход сигнала реле 2 для подтверждения удаленной панели
5. 2 выход сигнала для подтверждения жужжащего
6. Выход сигнала реле 2 для резервного общего
7. Com 1 сигнал для модема
8. 2 сигнал для приемника.

![[17800175.png]]

Внутренняя часть окна - Customer Interface Box

1. Проводные лотки
2. 5.2.1.1 Реле защиты двигателя
3. Выключатели
4. Логический блок интерфейса клиента
5. Ethernet коммутатор
6. Терминальная полоса.

![[00400368.png]]

Front View - блок отключения

1. Ethernet соединение
2. Подключение USB Com 4
3. Связь с блоком управления дизельным топливом
4. Запуск эстафеты
5. Неисправность реле
6. Эстафета с зуммером
7. Кран двигателя выключен
8. Эстафета остановки
9. Входные сигналы скорости двигателя
10. Электроснабжение блока отключения
11. Выключатель отказов Shutdown
12. Входные сигналы канала для датчиков.

![[00400369.png]]

Front View - удаленный входной/выходной блок

1. Входные сигналы для соединений датчиков Lloyd
2. Номер 1 и 2 конфигурационные ретрансляционные соединения
3. Датчики давления и температуры сигнализируют в блок управления дизельным двигателем
4. Переключай входные данные
5. Подключение электропитания к удаленному блоку ввода/вывода
6. Подключение ModbusTM к блоку управления дизельным двигателем

![[17800074.png]]

Коробка интерфейса клиента (Logic Unit)

1. Терминальная полоса
2. Лампа с коленчатым состоянием
3. Остановить лампу
4. Данные о состоянии лампы
5. Дип-переключатели
6. Диагностика на лампе
7. Красная диагностическая лампа
8. Янтарная диагностическая лампа
9. Переключатель сгиба/прироста
10. Диагностический переключатель ON/OFF
11. Пропуск 85% лампы Rated
12. лампа для бега
13. Белая (поддерживающая) лампа
14. лампа-жужжальщик
15. Янтарная (неисправная) лампа
16. Красная (неисправная) лампа
17. Локальная лампа режима
18. 2.1.2.2 Остановить двигатель
19. 2-х лампа для подачи
20. Поставка 1 лампы.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Customer Interface Box
>
> 1. Customer interface box
> 2. Diesel Control Unit 410
> 3. Engine stop switch
> 4. Locking mechanism
> 5. Power switch.
>
> Front View - Diesel Control Unit 410
>
> 1. Display unit
> 2. Start button
> 3. Stop button
> 4. Soft buttons
> 5. Down arrow button
> 6. Menu button
> 7. Up arrow button
> 8. Alarm button
> 9. Power light emitting diode.
>
> Rear View - Diesel Control Unit 410
>
> 1. Configurable output signals for relays and alarms
> 2. Com 1, 2, 3, 4, and 5 Modbus™ signal inputs
> 3. Sensor input signals
> 4. 1 through 8 switch inputs
> 5. Power supply to diesel control unit
> 6. Critical signal inputs to the diesel control unit.
>
> Front View - Remote Panel
>
> 1. Power light emitting diode
> 2. Display panel
> 3. Alarm button
> 4. Menu button
> 5. Start button
> 6. Stop button
> 7. Home button.
>
> Rear View - Remote Panel
>
> 1. Power supply for remote panel
> 2. Switch input signal for alarm
> 3. Relay 1 signal output for active station
> 4. Relay 2 signal output for acknowledgement of remote panel
> 5. Relay 2 signal output for buzzer acknowledgement
> 6. Relay 2 signal output for reserve common
> 7. Com 1 signal for modem
> 8. Com 2 signal for receiver.
>
> Inside View - Customer Interface Box
>
> 1. Wire trays
> 2. Engine protection override relay
> 3. Circuit breakers
> 4. Customer interface box logic unit
> 5. Ethernet switch
> 6. Terminal strip.
>
> Front View - Shutdown Unit
>
> 1. Ethernet connection
> 2. Com 4 USB connection
> 3. Communication link to diesel control unit
> 4. Running relay
> 5. Fault relay
> 6. Buzzer relay
> 7. Engine crank shut off
> 8. Shutdown relay
> 9. Engine speed input signals
> 10. Power supply for shutdown unit
> 11. Shutdown fault switches
> 12. Channel input signals for sensors.
>
> Front View - Remote Input/Output Unit
>
> 1. Input signals for Lloyd sensor connections
> 2. Number 1 and 2 configuration relay connections
> 3. Pressure and temperature sensor signals to diesel control unit
> 4. Switch inputs
> 5. Power supply connections for remote input/output unit
> 6. Communication Modbus™ connection to diesel control unit
>
> Customer Interface Box (Logic Unit)
>
> 1. Terminal strip
> 2. Crank status lamp
> 3. Stop status lamp
> 4. Data Save status lamp
> 5. Dip switches
> 6. Diagnostic ON lamp
> 7. Red diagnostic lamp
> 8. Amber diagnostic lamp
> 9. Fault increment/decrement switch
> 10. Diagnostic ON/OFF switch
> 11. Running 85% of Rated lamp
> 12. Running lamp
> 13. White (maintenance) lamp
> 14. Buzzer lamp
> 15. Amber (fault) lamp
> 16. Red (fault) lamp
> 17. Local Mode lamp
> 18. Engine Stop lamp
> 19. Supply 2 lamp
> 20. Supply 1 lamp.
