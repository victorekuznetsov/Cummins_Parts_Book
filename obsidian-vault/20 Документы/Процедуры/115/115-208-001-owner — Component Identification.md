---
aliases:
  - "Идентификация компонентов"
type: "Процедура"
doc: "115-208-001-owner"
title_en: "Component Identification"
title_ru: "Идентификация компонентов"
modified: "2008-10-09"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
  - "41353297"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
manuals:
  - "4021589"
figures: 11
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-208-001-owner.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-208-001-owner.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Component Identification
**Идентификация компонентов**

> [!abstract] Процедура · `115-208-001-owner`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Входит в руководства:** [[4021589 — Marine C Command Panel System Owners Manual|4021589]]
> **Секции:** Section E - Engine and System Identification
> **Даты:** изменён 2008-10-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-208-001-owner.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-208-001-owner.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

![[17800070.png]]

Клиентский интерфейс (Front View)

1. Кнопка остановки двигателя
2. Механизм запирания дверей.

![[17800071.png]]

Коробка интерфейса клиента (Inside View)

1. Выключатели
2. Логический блок интерфейса клиента
3. Кабельные лотки
4. Терминальные полосы.

![[17800072.png]]

Внутренняя панель (Inside of Door View)

1. Выключатель остановки двигателя
2. Механизм блокировки дверей
3. Земля.

![[17800073.png]]

Клиентский интерфейс (нижний вид)

1. Диспетчер машинного отделения с проводкой ремня разъема
2. ← Моторная проводка упряжка 31-контактный разъем
3. Моторная проводка жгута 16-контактного разъема.

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
11. Пропуск 85% номинальной лампы
12. лампа для бега
13. Белая (поддерживающая) лампа
14. лампа-жужжальщик
15. Янтарная лампа неисправности
16. Красная лампа неисправности
17. Локальная лампа
18. 2.1.2 Остановить двигатель
19. 2-х лампа для подачи
20. Поставка 1 лампы.

![[17800075.png]]

Панель машинного отделения (Front View)

1. Цифровой дисплей ED-3
2. Переключатель питания
3. Локальный запуск **** с кнопки
4. Кнопка тишины тревоги
5. Кнопка остановки двигателя
6. Локальный старт только переключается
7. Будильник
8. Кнопка запуска двигателя
9. Механизм запирания дверей.

![[17800076.png]]

Панель машинного отделения (Inside Door View)

1. Терминальная полоса
2. Цифровой дисплей ED-3
3. Механизм блокировки дверей
4. Панель управления
5. Разъемы панели управления.

![[17800078.png]]

Панель машинного отделения (нижний вид)

1. Клиентский интерфейс Box Wiring Usge Connector
2. SAE J1939 CAN дата-автобусный порт.

![[17800079.png]]

Дистанционная панель (Front View)

1. Цифровой дисплей ED-3
2. 4.2.1 Силовая лампа
3. Кнопка тишины тревоги
4. Кнопка остановки двигателя
5. Будильник
6. Кнопка запуска двигателя
7. Локальный старт **** лампа

![[17800080.png]]

Дистанционная панель (обратный вид)

1. Терминальная полоса
2. Цифровой дисплей ED-3
3. Панель управления
4. Разъемы панели управления.

> [!note] Примечание
> **Не** Показано: SAE J1939 CAN дата-автобусный порт. Порт обслуживания шины данных SAE J1939 CAN представляет собой свиной хвост и свободно висит в корпусе клиента.

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
> Customer Interface Box (Front View)
>
> 1. Engine stop button
> 2. Door locking mechanism.
>
> Customer Interface Box (Inside View)
>
> 1. Circuit breakers
> 2. Customer interface box logic unit
> 3. Cable trays
> 4. Terminal strips.
>
> Customer Interface Box (Inside of Door View)
>
> 1. Engine stop switch
> 2. Door locking mechanism
> 3. Ground.
>
> Customer Interface Box (Bottom View)
>
> 1. Engine room panel harness connector
> 2. Engine harness 31-pin connector
> 3. Engine harness 16-pin connector.
>
> Customer Interface Box (Logic Unit)
>
> 1. Terminal strip
> 2. Crank status lamp
> 3. Stop status lamp
> 4. Data save status lamp
> 5. Dip switches
> 6. Diagnostic ON lamp
> 7. Red diagnostic lamp
> 8. Amber diagnostic lamp
> 9. Fault increment/decrement switch
> 10. Diagnostic ON/OFF switch
> 11. Running 85 percent of rated lamp
> 12. Running lamp
> 13. White (maintenance) lamp
> 14. Buzzer lamp
> 15. Amber fault lamp
> 16. Red fault lamp
> 17. Local mode lamp
> 18. Engine stop lamp
> 19. Supply 2 lamp
> 20. Supply 1 lamp.
>
> Engine Room Panel (Front View)
>
> 1. ED-3 digital display
> 2. Power switch
> 3. Local start **only** off button
> 4. Alarm silence button
> 5. Engine stop button
> 6. Local start only switch
> 7. Alarm lamp
> 8. Engine start button
> 9. Door locking mechanism.
>
> Engine Room Panel (Inside Door View)
>
> 1. Terminal strip
> 2. ED-3 digital display
> 3. Door locking mechanism
> 4. Control panel
> 5. Control panel connectors.
>
> Engine Room Panel (Bottom View)
>
> 1. Customer interface box harness connector
> 2. SAE J1939 data link service port.
>
> Remote Panel (Front View)
>
> 1. ED-3 digital display
> 2. Power lamp
> 3. Alarm silence button
> 4. Engine stop button
> 5. Alarm lamp
> 6. Engine start button
> 7. Local start **only** lamp
>
> Remote Panel (Reverse View)
>
> 1. Terminal strip
> 2. ED-3 digital display
> 3. Control panel
> 4. Control panel connectors.
>
> **Note · Примечание**
> **Not** Shown: SAE J1939 data link service port. The SAE J1939 data link service port is a pig tail and hangs freely in the customer enclosure.
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
