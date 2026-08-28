---
aliases:
  - "Останов: низкое давление газа на входе"
type: "Процедура"
doc: "330-t02-1004"
title_en: "Sd LowGasPressIn"
title_ru: "Останов: низкое давление газа на входе"
modified: "2017-03-02"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4358403"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1004.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1004.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/330"
  - "перевод/машинный"
---

# Sd LowGasPressIn
**Останов: низкое давление газа на входе**

> [!abstract] Процедура · `330-t02-1004`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4358403 — Dual Fuel Technology DF101 Master Repair Manual|4358403]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2017-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1004.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1004.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

Весь поток газа будет остановлен, и модуль управления двойным топливом будет заблокирован для входа в режим двойного топлива.

### Как пользоваться этим деревом

**Описание:**

Газовый поезд оборудован выключателем низкого давления. Если переключатель указывает на состояние подачи под низким давлением, вводная активация останавливает или препятствует нормальной работе двойной топливной системы.

**Условия для проведения диагностики:**

Каждый раз, когда переключатель указывает на более низкое, чем принято, давление подачи и двойной модуль управления топливом включается, система будет указывать это сообщение и утверждать защиту.

**Условия активации сообщения об ошибке:**

Двойной модуль управления топливом включен, а двоичный вход с маркировкой BI-2 открыт для отрицательного заряда батареи.

**Действия, предпринимаемые при активной неисправности:**

Предотвращается двойная эксплуатация топлива.

Весь поток газа остановится, если система работает в режиме двойного топлива.

**Условия автоматической очистки кодов по умолчанию:**

Нет условий для автоматического устранения неисправности.

**Условия для очистки кодов ошибок вручную:**

Давление газа восстанавливается выше заданного предела точки переключателя, и сброс неисправности снижается локально или через программное обеспечение.

### Практические замечания

Защитный элемент предназначен для ограничения подачи газа в условиях низкого давления подачи топлива.

Когда модуль управления двойным топливом имеет открытую схему для BI-2, он утверждает защиту.

Возможные причины включают:

- Давление газа ниже заданной точки переключения

- Неисправный переключатель давления газа

- Поврежденные контакты в газовом выключателе давления

- Поврежденные или рыхлые проводные соединения в двухмодулях управления топливом для отрицательной батареи или BI-2

- Поврежденные или рыхлые проводные соединения при контактах переключателя давления газа

- Неисправный модуль двойного управления топливом

- Объем подачи газа недостаточно велик для поддержания достаточного давления при высокой нагрузке.

| Таблица 1: Модуль двойного управления топливом - состояние открытой цепи |  |  |
|---|---|---|
| Коды или сообщения | Причина | Последствия |
| **SD LowGasPressIn** | BI-2 открыт в отношении отрицательной батареи. Для нормальной работы цепи требуется заземленный вход. | Двойной модуль управления топливом не позволит работать с газом. Двойной модуль управления топливом остановит поток газа. |

| Таблица 2 |  |
|---|---|
| Виноваты случаи, когда: | Возможная причина(ы): |
| Изменения входа во время запуска/низкого напряжения батареи в управляющем модуле | Проверка падения напряжения, свободных проводных соединений с двойным модулем управления топливом при положительных и отрицательных соединениях батареи |
| Ввод изменяется периодически или случайным образом при низком холостом или высоком состоянии нагрузки - вибрация | Свободная проводка, поврежденные разъемы или поврежденные контакты |
| Ввод изменяется при нарушении проводов или разъемов | Свободная проводка, поврежденные разъемы или поврежденные контакты |
| Несколько бинарных входных ошибок | Заземление системы, свободные отрицательные соединения батареи, неисправные батареи или неправильные соединения проводов. |
| Виноваты только в условиях умеренной и большой нагрузки. | Подозреваемое фактическое давление газа падает ниже уровня защиты переключателя. Испытание с фактической записью давления газа с использованием преобразователя или калибра (измерительных приборов) по мере необходимости для изоляции. |

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверить сообщение о вине. |  |
|  | **ШАГ 1А.** Проверить наличие сообщения об ошибке. | Активный? |
|  | **ШАГ 1В.** Положите вину на себя. | Сообщение о вине удалено? |
|  | **STEP 1C.** Проверить сообщение об ошибке «Не активен». | Модуль управления имеет вхождения для SD LowGasPressIn? |
| ШАГ 2. | Проверьте правильное давление топлива. |  |
|  | **STEP 2A.** Проверьте показания датчика давления. | Топливное давление в спецификациях? |
| ШАГ 3. | Проверьте выключатель и цепь низкого давления топлива. |  |
|  | **STEP 3A** Проверить контакты переключателя и разъема низкого давления топлива. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте выключатель на правильность работы. | Двоичный вход 2 отображает 1 с помощью InteliMonitor? |
|  | **STEP 3C.** Проверьте электропроводку. | Двоичный вход 2 отображает 1 с помощью InteliMonitor? |
| ШАГ 4. | Проверьте бинарные входы. |  |
|  | **STEP 4A.** Проверить ответ двоичного ввода. | Двоичный вход 2 отображает 1 с помощью InteliMonitor? |
| ШАГ 5. | Тестирование системы с помощью WinScope PC. |  |
|  | **STEP 5A.** Измерительные вводы с использованием WinScope. | Есть ли случаи, когда BI-2 становится нулевым с использованием собранных данных и InteliMonitor? |
| ШАГ 6. | Перезагрузите панель управления. |  |
|  | **STEP 6A.** Перезагрузить контроллер. | Двойной модуль управления топливом в состоянии отключения для SD LowGasPressIn? |

### ШАГ 1. Проверить сообщение о вине.

#### ШАГ 1A. Проверьте «активное» сообщение о вине.

| **Условия:** Модуль управления питанием на двухтопливном топливе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте локальную панель дисплея для активного сообщения об ошибке. Навигация на экран дисплея с ошибкой. | Активный? *Да | 2А |
| Активный? **НЕТ** | 1В |  |

#### ШАГ 1B. Снимите вину.

| **Условия:** Модуль управления питанием на двухтопливном топливе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подключайтесь к двойной топливной панели. Используйте InteliMonitor. Сохраните копию файла конфигурации (архивного файла) на локальном ПК. Сброс неисправности с модуля управления или с программного обеспечения InteliMonitor. | Сообщение о вине удалено? *Да | 1С |
| Сообщение о вине удалено? **НЕТ** | Свяжитесь с авторизованным местом ремонта Cummins® для помощи в ремонте. |  |

#### ШАГ 1C. Проверить сообщение «Не активен».

| **Условия:** Модуль управления питанием на двухтопливном топливе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подключайтесь к панели управления двойным топливом. Используйте InteliMonitor. Сохраните копию файла конфигурации модуля управления (архивного файла) на локальном ПК. Доступ к короткому пути истории. Проверьте наличие сообщений SD LowGasPressIn. Проверьте другие сообщения о выключении, происходящие во время или около времени SD LowGasPressIn. Проверьте другие сообщения о выключении, происходящие во время или около времени SD LowGasPressIn. Если другие сообщения о выключении для бинарных входов происходят одновременно, см. процедуру для наземных и наземных измерительн. | Модуль управления имеет вхождения для SD LowGasPressIn? *Да | 5а |
| Модуль управления имеет вхождения для SD LowGasPressIn? **НЕТ** | Нет ремонта. |  |

### ШАГ 2. Проверьте правильное давление топлива.

#### ШАГ 2A. Проверьте показания датчика давления.

| **Условия:** Модуль управления питанием на двухтопливном топливе. Убедитесь, что модуль управления двойным топливом находится в режиме AUTO. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте показания на датчике измерения давления, установленном после топливного фильтра. Если давление газа меньше, чем настройка переключателя низкого давления 13,78 кПа \[2 psi\], разъем переключателя низкого давления отключается или переключатель поврежден, неисправность будет активной и не будет сбрасываться. | Топливное давление в спецификациях? *Да | 3А |
| Топливное давление в спецификациях? **NORepair:** Проверить причину низкого давления топлива. Проверьте топливный фильтр в газовом поезде. См. процедуру 005-246 в разделе 5. Если топливный фильтр функционирует должным образом, проверьте компоненты топливной системы. См. сервисную документацию изготовителя оборудования. | 6А |  |

### ШАГ 3. Проверьте выключатель и цепь низкого давления топлива.

#### ШАГ 3A. Проверьте контакты переключателя низкого давления топлива и разъема.

| **Условия:** Выключите замок зажигания. Отсоедините разъем переключателя низкого давления топлива от разъема с двойной топливной проводкой. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы двухтопливной проводов и разъема переключателя низкого давления топлива на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В разъеме с низким давлением топлива или проводной упряжке обнаружено поврежденное соединение. Проверьте все проводов, подключенные последовательно. Очистите разъем и булавки. Замените поврежденный участок проводов ремня поврежденного датчика. Ремонт проводов жгута. См. процедуру 019-564 в разделе 19. Замените датчик. См. процедуру 019-579 в разделе 19. | 6А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте выключатель для правильной работы.

| **Условия:** Двигатель не работает. Power ON двойной панели управления топливом. Отсоедините разъем переключателя низкого давления топлива от разъема жгутов проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Поместите провод прыгуна между проводом SIGNAL и RETURN на разъёме жгута проводов. | Двоичный вход 2 отображает 1 с помощью InteliMonitor? **Ремонт:** Проверьте настройку циферблата на выключателе. Проверьте, установлен ли переключатель на 55 in-H 2 O. Если выключатель установлен на уровне 55 in-H 2 O, выключатель низкого давления неисправен. Замените выключатель низкого давления. См. процедуру 019-579 в разделе 19. | 6А |
| Двоичный вход 2 отображает 1 с помощью InteliMonitor? **НЕТ** | 3C |  |

#### ШАГ 3C. Проверьте проводку.

| **Условия:** Двигатель не работает. Power ON двойной панели управления топливом. Отсоедините проводную упряжку от разъема C3. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Поместите провод прыгуна между проводом SIGNAL и RETURN на разъёме проводов C3. | Двоичный вход 2 отображает 1 с помощью InteliMonitor? **Ремонт:** Установка проводов неисправна. Ремонт или замена проводов жгута. См. процедуру 019-564 в разделе 19. | 6А |
| Двоичный вход 2 отображает 1 с помощью InteliMonitor? **НЕТ** | 4А |  |

### ШАГ 4. Проверьте бинарные входы.

#### ШАГ 4A. Тестирование бинарного входного ответа.

| **Условия:** Двигатель не работает. Модуль управления двойным топливом Power ON. Поместите модуль управления двойным топливом в режим выключения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сделайте временное соединение от наземного шпилька панели до двоичного входного терминала BI-2. Используйте одобренный прыгун. Наблюдайте, когда соединение сделано, состояние ввода становится 1. | Двоичный вход 2 отображает 1 с помощью InteliMonitor? **Ремонт:** Ремонт или замена проводов от C3-A до модуля управления BI-2 (провода 4002). | 6А |
| Двоичный вход 2 отображает 1 с помощью InteliMonitor? **NORepair:** Обнаружен неисправный модуль Inteli Bi-Fuel. | 6А |  |

### ШАГ 5. Тестирование системы с помощью WinScope PC.

#### ШАГ 5A. Измерительные вводы с использованием WinScope.

| **Условия:** Двигатель не работает. Подключите ПК с помощью WinScope к контроллеру с двойным топливом. Включите питание панели управления. Поместите модуль управления двойным топливом в режим выключения. Загрузка может быть применена до 85 процентов номинально, шагами от 10 до 15 процентов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Выберите элемент для мониторинга в выборе каналов, в частности, в этом случае монитор BI-2, аналоговый блок управления напряжением батареи, значение регулирования газа «Engine Power» и «G/S Ratio». Установите период времени охвата для захвата на 150 мС и начинайте лесозаготовку. 1. Доступ к разъёму жгута проводов для впускного газового переключателя давления (C18-1) на газовом поезде. Отключите и переподключите разъем, чтобы проверить, что управление реагирует на изменения, и WinScope указывает, что изменение произошло. 2. Запустите двигатель и обратите внимание, что вход для BI-2 остается на уровне 1 во время коленчатого, пускового и ходового состояния. Это делается для обнаружения неисправностей, вызванных вибрацией или необоснованными падениями напряжения батареи, подводимого к управлению во время нормальной работы. 3. Продолжайте запись двоичных данных и попробуйте создать неисправность, мягко перемещая провода и проводную упряжку внутри панели и у разъемов, внешних по отношению к панели, чтобы найти прерывистые неисправности или свободные соединения. 4. Если на Шагах 1-3 происходят неисправности, медленно добавляйте нагрузку на двигатель шагами. Разрешить двигателю и нагрузке стабилизироваться на каждом шаге в течение **no** менее 5 минут. Продолжайте регистрировать данные под нагрузкой до тех пор, пока не будет улавливаться неисправность или не будет применена мощность двигателя с номинальной мощностью 85%. | Есть ли случаи, когда BI-2 становится нулевым с использованием собранных данных и InteliMonitor? **Ремонт:** Используйте результаты указанных шагов для определения причины или разумных шагов и ремонта по мере необходимости. Справочная таблица 2 в разделе Shoptalk. | 6А |
| Есть ли случаи, когда BI-2 становится нулевым с использованием собранных данных и InteliMonitor? **НЕТ** | 6А |  |

### ШАГ 6. Перезагрузите панель управления.

#### ШАГ 6A. Перезагрузите контроллер.

| **Условия:** Двигатель не работает. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите питание от панели управления. Подожди 30 секунд. Восстановить подключение DC. Подтвердите, что ошибка SD LowGasPressIn отсутствует или активна. | Двойной модуль управления топливом в состоянии отключения для SD LowGasPressIn? Возвращение к шагам устранения неполадок или обращение в авторизованное место ремонта Cummins®, если все шаги были завершены и проверены повторно. | 1А |
| Двойной модуль управления топливом в состоянии отключения для SD LowGasPressIn? **НЕТ** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> All gas flow will stop and the dual fuel control module will be prevented from entering dual fuel mode.
>
> ### How To Use This Tree
>
> **Circuit Description:**
>
> The gas train is equipped with a low inlet pressure switch. If the switch indicates a low-pressure supply condition, the input activation stops or prevents the normal operation of the dual fuel system.
>
> **Conditions for Running the Diagnostics:**
>
> Any time the switch indicates a lower than accepted supply pressure and the dual fuel control module is powered ON, the system will indicate this message and assert protection.
>
> **Conditions for Activating the Fault Message:**
>
> Dual fuel control module is powered on and the binary input labeled BI-2 is open to battery negative.
>
> **Actions Taken When the Fault is Active:**
>
> Dual fuel operation will be prevented.
>
> All gas flow will stop if system is operating in dual fuel mode.
>
> **Conditions for Clearing the Fault Codes Automatically:**
>
> No conditions for clearing fault automatically.
>
> **Conditions for Clearing the Fault Codes Manually:**
>
> The gas pressure is restored above the set point limit of the switch and the fault reset is depressed locally or via the software.
>
> ### Shoptalk
>
> The protection element is intended to restrict gas delivery for low fuel supply pressure conditions.
>
> When the control dual fuel module has an open circuit for BI-2, it asserts the protection.
>
> Possible causes include:
>
> - Gas pressure below switch set point
>
> - Malfunctioned gas pressure switch
>
> - Damaged contacts on gas pressure switch
>
> - Damaged or loose wiring connections at dual fuel control module for battery negative or BI-2
>
> - Damaged or loose wiring connections at gas pressure switch contacts
>
> - Malfunctioned dual fuel control module
>
> - Gas supply volume is not great enough to maintain sufficient pressures at high load.
>
> | Table 1: Dual Fuel Control Module - Open Circuit Condition Exists |  |  |
> |---|---|---|
> | Codes or Messages | Reason | Effect |
> | **SD LowGasPressIn** | BI-2 is open in reference to battery negative. Circuit requires a grounded input for normal operation. | Dual fuel control module will **not** allow gas operations. Dual fuel control module will stop gas flow. |
>
> | Table 2 |  |
> |---|---|
> | Fault occurs when: | Possible cause(s): |
> | Input changes during starting/low battery voltage to control module | Check voltage drop, loose wiring connections to dual fuel control module at battery positive and negative connections |
> | Input changes intermittently or randomly at low idle or high load condition - vibration | Loose wiring, damaged connectors, or damaged pins |
> | Input changes when disturbing wires or connectors | Loose wiring, damaged connectors, or damaged pins |
> | Multiple binary input faults | System grounding, loose battery negative connections, malfunctioned batteries, or improper wiring connections. |
> | Fault occurs **only** under moderate to heavy load conditions | Suspect actual gas pressure is dropping below switch protection level. Test with actual gas pressure recording using transducer or gauge(s) as needed to isolate. |
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Validate the fault message. |  |
> |  | **STEP 1A.** Check for 'Active' fault message. | Fault active? |
> |  | **STEP 1B.** Rest the fault. | Fault message cleared? |
> |  | **STEP 1C.** Check for 'Not Active' fault message. | Control module has occurrences for SD LowGasPressIn? |
> | STEP 2. | Verify correct fuel pressure. |  |
> |  | **STEP 2A.** Check the pressure gauge reading. | Fuel pressure within specifications? |
> | STEP 3. | Check the low fuel pressure switch and circuit. |  |
> |  | **STEP 3A.** Inspect the low fuel pressure switch and connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the switch for correct operation. | Binary Input 2 displays a 1 using InteliMonitor? |
> |  | **STEP 3C.** Check the wiring harness. | Binary Input 2 displays a 1 using InteliMonitor? |
> | STEP 4. | Check the binary inputs. |  |
> |  | **STEP 4A.** Test the binary input response. | Binary Input 2 displays a 1 using InteliMonitor? |
> | STEP 5. | Test the system using WinScope PC tool. |  |
> |  | **STEP 5A.** Test inputs using WinScope. | Any occurrences of BI-2 becoming zero using data collected and InteliMonitor? |
> | STEP 6. | Restart the control panel. |  |
> |  | **STEP 6A.** Restart the controller. | Dual fuel control module in shutdown condition for SD LowGasPressIn? |
>
> ### STEP 1. Validate the fault message.
>
> #### STEP 1A. Check for 'Active' fault message.
>
> | **Conditions:** Power ON dual fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check local display panel for an active fault message. Navigate to fault display screen. | Fault active? **YES** | 2A |
> | Fault active? **NO** | 1B |  |
>
> #### STEP 1B. Reset the fault.
>
> | **Conditions:** Power ON dual fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect to the dual fuel panel. Use InteliMonitor. Save a copy of the configuration file (archive file) on the local PC. Reset the fault from the control module or from the software InteliMonitor. | Fault message cleared? **YES** | 1C |
> | Fault message cleared? **NO** | Contact a Cummins® Authorized Repair Location for repair assistance. |  |
>
> #### STEP 1C. Check for 'Not Active' fault message.
>
> | **Conditions:** Power ON dual fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect to the dual fuel control panel. Use InteliMonitor. Save a copy of the control module configuration file (archive file) on the local PC. Access the history shortcut. Check for occurrences of the message SD LowGasPressIn. Check for other shutdown messages occurring at or near the time of the SD LowGasPressIn. Check for other shutdown messages occurring at or near the time of the SD LowGasPressIn. If other shutdown messages for binary inputs occur at the same time, see the procedure for ground and ground loop tests. | Control module has occurrences for SD LowGasPressIn? **YES** | 5A |
> | Control module has occurrences for SD LowGasPressIn? **NO** | No repair. |  |
>
> ### STEP 2. Verify correct fuel pressure.
>
> #### STEP 2A. Check the pressure gauge reading.
>
> | **Conditions:** Power ON dual fuel control module. Make sure the dual fuel control module is in AUTO mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the reading on the pressure gauge mounted after the fuel filter. If gas pressure is less than the low pressure switch setting of 13.78 kPa \[2 psi\], the low gas pressure switch connector is unplugged, or the switch is damaged, the fault will be active and will not reset. | Fuel pressure within specifications? **YES** | 3A |
> | Fuel pressure within specifications? **NORepair:** Verify the cause of the low fuel pressure. Inspect the fuel filter on the gas train. Refer to Procedure 005-246 in Section 5. If the fuel filter is functioning properly, inspect the upstream fuel system components. See equipment manufacturer service information. | 6A |  |
>
> ### STEP 3. Check the low fuel pressure switch and circuit.
>
> #### STEP 3A. Inspect the low fuel pressure switch and connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the low fuel pressure switch connector from the dual fuel harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the dual fuel harness and low fuel pressure switch connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the low fuel pressure switch or harness connector. Check all harnesses connected in series. Clean the connector and pins. Replace the damage section of harness of damaged sensor. Repair the harness. Refer to Procedure 019-564 in Section 19. Replace the sensor. Refer to Procedure 019-579 in Section 19. | 6A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the switch for correct operation.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the low fuel pressure switch connector from the engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Place a jumper wire between the SIGNAL and RETURN wire on the wiring harness connector. | Binary Input 2 displays a 1 using InteliMonitor? **YESRepair:** Check the dial setting on the switch. Verify the switch is set to 55 in-H 2 O. If the switch is set at 55 in-H 2 O, the low pressure switch has malfunctioned. Replace the low pressure switch. Refer to Procedure 019-579 in Section 19. | 6A |
> | Binary Input 2 displays a 1 using InteliMonitor? **NO** | 3C |  |
>
> #### STEP 3C. Check the wiring harness.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the wiring harness from the C3 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Place a jumper wire between the SIGNAL and RETURN wire on the C3 wiring harness connector. | Binary Input 2 displays a 1 using InteliMonitor? **YESRepair:** The wiring harness has malfunctioned. Repair or replace the wiring harness. Refer to Procedure 019-564 in Section 19. | 6A |
> | Binary Input 2 displays a 1 using InteliMonitor? **NO** | 4A |  |
>
> ### STEP 4. Check the binary inputs.
>
> #### STEP 4A. Test the binary input response.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control module. Place dual fuel control module in OFF mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Make a temporary connection from the panel ground stud to the binary input terminal BI-2. Use an approved jumper wire. Observe when the connection is made, the input status becomes 1. | Binary Input 2 displays a 1 using InteliMonitor? **YESRepair:** Repair or replace the wiring from C3-A to the control module BI-2 (wire 4002). | 6A |
> | Binary Input 2 displays a 1 using InteliMonitor? **NORepair:** A malfunctioning Inteli Bi-Fuel module has been detected. | 6A |  |
>
> ### STEP 5. Test the system using WinScope PC tool.
>
> #### STEP 5A. Test inputs using WinScope.
>
> | **Conditions:** Engine not operating. Connect PC using WinScope to dual fuel controller. Switch control panel power ON. Place dual fuel control module in OFF mode. Load is available to be applied up to 85 percent nominal, in steps of 10 to 15 percent. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Select the item to monitor in the channel selections, specifically in this case monitor BI-2, analog control unit battery voltage, gas regulation value 'Engine Power' and 'G/S Ratio'. Set the scope time period to capture at 150 mS and begin logging. 1. Access the harness connector for the inlet gas pressure switch (C18-1) on the gas train. Disconnect and reconnect the connector to verify the control responds to the changes, and WinScope indicates the change occurred. 2. Start the engine and observe that the input for BI-2 remains at 1 during the crank, start, and run condition. This is to locate faults caused by vibration or unreasonable drops in battery voltage supply to the control during normal operation. 3. Continue recording the binary data and attempt to create the fault by gently moving wires and the wiring harness inside the panel and at the connectors, external to the panel, to locate intermittent faults or loose connections. 4. If **no** faults occur in Steps 1-3, slowly add load to the engine in steps. Allow the engine and load to stabilize at each step for **no** less than 5 minutes. Continue logging data under load until either the fault is captured or 85 percent rated engine power has been applied. | Any occurrences of BI-2 becoming zero using data collected and InteliMonitor? **YESRepair:** Use results from the specified steps to determine the cause or reasonable steps and repair as needed. Reference Table 2 in the Shoptalk section. | 6A |
> | Any occurrences of BI-2 becoming zero using data collected and InteliMonitor? **NO** | 6A |  |
>
> ### STEP 6. Restart the control panel.
>
> #### STEP 6A. Restart the controller.
>
> | **Conditions:** Engine not operating. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disconnect power from the control panel. Wait 30 seconds. Restore DC power connection. Confirm the fault for SD LowGasPressIn is not present or active. | Dual fuel control module in shutdown condition for SD LowGasPressIn? **YESRepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |
> | Dual fuel control module in shutdown condition for SD LowGasPressIn? **NO** | Repair complete. |  |
