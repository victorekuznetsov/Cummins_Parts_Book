---
aliases:
  - "Останов: давление газа регулятора"
type: "Процедура"
doc: "330-t02-1007"
title_en: "Sd RegGasPress"
title_ru: "Останов: давление газа регулятора"
modified: "2017-03-02"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "4358403"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/330"
  - "перевод/машинный"
---

# Sd RegGasPress
**Останов: давление газа регулятора**

> [!abstract] Процедура · `330-t02-1007`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[4358403 — Dual Fuel Technology DF101 Master Repair Manual|4358403]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2017-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1007.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Весь поток газа прекратится или модуль управления двойным топливом будет заблокирован при переходе в режим двойного топлива.

### Как пользоваться этим деревом

Это дерево можно использовать для устранения неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

**Описание:**

Газовый поезд оборудован выключателем высокого давления. Если переключатель указывает на состояние высокого давления после регулятора Cummins®, вводная активация останавливает или препятствует нормальной работе двойной топливной системы. Переключатель представляет собой поддерживаемое или защелкивающее устройство, то есть, если условие возникает, устройство должно быть вручную сброшено до того, как сигнал будет восстановлен на входе модуля управления двойным топливом.

**Условия для проведения диагностики:**

В любое время, когда система работает и заменяет газ, а переключатель давления указывает большее, чем принятое давление, на более длительный период времени, чем фиксированная задержка, система будет указывать это сообщение и утверждать защиту.

**Условия активации сообщения об ошибке:**

Двоичный вход 3 (BI-3) открыт для отрицательной зарядки аккумулятора при работе в режиме двойного топлива дольше, чем задержка (60 секунд).

Двоичный вход 3 (BI-3) открыт для отрицательной батареи, когда **не** в режиме двойного топлива дольше 0,5 секунды.

**Условия автоматического устранения неисправности:**

Нет.

**Условия для очистки кодов ошибок вручную:**

Давление газа восстанавливается ниже заданного предела переключателя. Механический переключатель был сброшен, и сброс неисправностей подавлен локально или через программное обеспечение.

### Практические замечания

Элемент защиты - защита от чрезмерного давления подачи газа в двигатель.

Когда модуль управления утверждает защиту, наиболее вероятной причиной является давление газа, подавшего газ, перепрыгнуло через предел. Контроллер не реагирует на неисправность в течение 60 секунд. Это может привести к тому, что оператор поверит, что неисправность произошла позже, чем фактически, или что условие не возникло, если мониторинг давления осуществляется только в качестве механического переключателя защелкивающего типа. Проверьте переключатель, чтобы увидеть, «подстригся» ли он перед детальным устранением неполадок в цепи. Сиюминутный всплеск все равно приведет к отключению. Если вход открыт, когда контроллер включен или открывается, когда он находится только в дизельном режиме, это приведет к неисправности.

Возможные причины включают:

- Чрезмерное давление газа выше предела давления переключателя

- Неисправный переключатель давления газа

- Неисправные контакты на газовом выключателе давления

- Неисправность или рыхлая проводка в модуле управления двойным топливом для отрицательного или двоичного входа батареи (BI-3)

- Неисправность или рыхлая проводка соединений при контактах переключателя давления газа

- Неисправный модуль двойного управления топливом

- Неправильно установлен или нет отверстия на переключателе.

| Код сообщения | Причина | Последствия |
|---|---|---|
| Останов: давление газа регулятора | BI-3 открыт в отношении отрицательной батареи. Для нормальной работы цепи требуется заземленный вход. | Двойной модуль управления топливом не позволит работать газу. Двойной модуль управления топливом остановит поток газа. |

В следующей таблице приведена справочная информация по этому дереву разломов.

| Таблица 1 |  |
|---|---|
| Виноваты, когда | Подозреваемый в каше |
| Изменения входа во время запуска - низкое напряжение батареи для модуля управления | Проверяйте падение напряжения, свободные проводные соединения с двойным модулем управления топливом при положительных и отрицательных соединениях батареи. |
| Ввод изменяется периодически или случайным образом при низкой холостой или очень высокой нагрузке - вибрация | Неисправные разъёмы, поврежденные контакты |
| Ввод изменяется при нарушении проводов или разъемов | Неисправные разъёмы, поврежденные контакты |
| Несколько бинарных входных ошибок | Заземление системы, свободные отрицательные соединения батареи, неисправные батареи, неправильные соединения проводов |
| Виноваты сразу после активации BO-1 и 7. | Подозрительный фактический всплеск давления газа происходит из-за неисправности газового регулятора или чрезмерного давления доставки. |
| Неисправность возникает при перепадах нагрузки примерно на 25% мощности | Регулятор газа переходный (сменный) ответ, вопросы стабильности доставки газа при смене нагрузки. Неисправный регулятор или устройство ограничения давления |
| Sd-неисправность для «LowGasPressIn» возникает при тестировании Sd RegGasPress | Регулятор газа переходный (сменный) ответ, вопросы стабильности доставки газа при смене нагрузки. Неисправный регулятор или устройство ограничения давления |

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверить сообщение о вине. |  |
|  | **ШАГ 1А.** Проверить наличие сообщения об ошибке. | Модуль управления в неисправном состоянии? |
|  | **STEP 1B.** Проверить сообщение об ошибке «Не активен». | Модуль управления имеет вхождения для Sd RegGasPres? |
|  | **СТЭП 1С** Сбросить вину. | Сообщение о вине удалено? |
| ШАГ 2. | Сбросьте выключатель высокого давления. |  |
|  | **STEP 2A.** Сбросить переключатель высокого давления. | Выше действий очищена вина? |
| ШАГ 3. | Проверьте выключатель и цепь высокого давления топлива. |  |
|  | **STEP 3A** Проверить контакты переключателя высокого давления топлива и разъема. | Грязные или поврежденные контакты? |
|  | **СТЭП 3В.** Проверьте выключатель. | Двоичный вход 3 отображает 1 с помощью InteliMonitor? |
|  | **STEP 3C.** Проверьте электропроводку. | Двоичный вход 3 отображает 1 с помощью InteliMonitor? |
|  | **STEP 3D.** Тестирование бинарного входного ответа. | Двоичный вход 3 отображает 1 с помощью InteliMonitor? |
| ШАГ 4. | Проверьте топливную систему высокого давления. |  |
|  | **ШАГ 4А.** Проверьте на скачок высокого давления. | Выявлены признаки всплеска высокого давления? |
|  | **STEP 4B.** Проверьте выключатель высокого давления. | Выберите правильный размер и без повреждений? |
|  | **STEP 4C** Проверьте регулятор давления топлива. | Регулятор давления топлива в соответствии со спецификациями? |
| ШАГ 5. | Тестирование системы с помощью WinScope PC. |  |
|  | **STEP 5A.** Измерительные вводы с использованием WinScope. | Есть ли случаи, когда BI-3 становится нулевым с использованием собранных данных и InteliMonitor? |
| ШАГ 6. | Снимите тревогу. |  |
|  | **СТЭП 6А.** Сбросьте будильник. | Двойной модуль управления топливом в состоянии отключения для Sd RegGasPress |

### ШАГ 1. Проверить сообщение о вине.

#### ШАГ 1A. Проверьте «активное» сообщение о вине.

| **Условия:** Модуль управления топливом в дуэли. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте локальную панель дисплея на наличие сообщения о неисправности. Навигация на экран дисплея неисправности. | Модуль управления в неисправном состоянии? *Да | 1С |
| Модуль управления в неисправном состоянии? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверить сообщение «Не активен».

| **Условия: **Модуль управления питанием на двухтопливном топливе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подключайтесь к панели управления двойным топливом. Используйте InteliMonitor. Сохраните копию файла конфигурации модуля управления (архивного файла) на локальном ПК. Доступ к короткому пути истории. Проверьте наличие сообщений Sd RegGasPress. Проверьте другие сообщения о выключении, происходящие во время или около времени Sd RegGasPress. Проверьте другие сообщения о выключении, происходящие во время или около времени Sd RegGasPress. Если другие сообщения о выключении для бинарных входов происходят одновременно, см. процедуру для наземных и наземных измерительн. | Модуль управления имеет вхождения для Sd RegGasPress? *Да | 1С |
| Модуль управления имеет вхождения для Sd RegGasPress? **НЕТ** | Нет ремонта. |  |

#### ШАГ 1C. Снимите вину.

| **Условия:** Модуль управления топливом в дуэли. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подключайтесь к двойной топливной панели. Используйте InteliMonitor. Сохраните копию файла конфигурации (архивного файла) на локальном ПК. Сброс неисправности с модуля управления или с программного обеспечения InteliMonitor. | Сообщение о вине удалено? *Да | 5а |
| Сообщение о вине удалено? **НЕТ** | 2А |  |

### ШАГ 2. Сбросьте выключатель высокого давления.

#### ШАГ 2A. Сбросьте выключатель высокого давления.

| **Условия: **Модуль управления питанием на двухтопливном топливе. Убедитесь, что модуль управления двойным топливом находится в режиме AUTO. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Нажмите кнопку отдыха на выключателе высокого давления. После нажатия кнопки сброса на переключателе перейдите на панель и сбросьте неисправность. | Выше действий очищена вина? *Да | 4А |
| Выше действий очищена вина? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте выключатель и цепь высокого давления топлива.

#### ШАГ 3A. Проверьте контакты переключателя высокого давления топлива и разъема.

| **Условия:** Выключите замок зажигания. Отсоедините разъем переключателя высокого давления топлива от разъема с двойной топливной проводкой. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы двойной топливной проводов и разъёма переключателя высокого давления топлива на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В переключателе высокого давления топлива или разъёме жгута проводов обнаружено поврежденное соединение. Проверьте все проводов, подключенные последовательно. Очистите разъем и булавки. Замените поврежденный участок проводов ремня или поврежденный переключатель. Ремонт проводов жгута. См. процедуру 019-564 в разделе 19. Замените выключатель. См. процедуру 019-580 в разделе 19. | 5а |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте выключатель.

| **Условия: **Двигатель не работает. Power ON двойной панели управления топливом. Отсоедините разъем переключателя высокого давления топлива от разъема жгутов проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Поместите провод прыгуна между проводом SIGNAL и RETURN на разъёме жгута проводов. | Двоичный вход 3 отображает 1 с помощью InteliMonitor? **Ремонт: **Выключатель высокого давления вышел из строя. Замените выключатель высокого давления. См. процедуру 019-580 в разделе 19. | 5а |
| Двоичный вход 3 отображает 1 с помощью InteliMonitor? **НЕТ** | 3C |  |

#### ШАГ 3C. Проверьте проводку.

| **Условия: **Двигатель не работает. Power ON двойной панели управления топливом. Отсоедините проводную упряжку от разъема C3. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Поместите провод прыгуна между проводом SIGNAL и RETURN на разъёме проводов C3. | Двоичный вход 3 отображает 1 с помощью InteliMonitor? **Ремонт: **Установка проводов неисправна. Ремонт или замена проводов жгута. См. процедуру 019-564 в разделе 19. | 5а |
| Двоичный вход 3 отображает 1 с помощью InteliMonitor? **НЕТ** | 3D |  |

#### ШАГ 3D. Тестирование бинарного входного ответа.

| **Условия: **Двигатель не работает. Модуль управления двойным топливом Power ON. Поместите модуль управления двойным топливом в режим выключения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сделайте временное соединение от наземного шпилька панели до двоичного входного терминала BI-3. Используйте одобренный прыгун. Наблюдайте, когда соединение сделано, состояние ввода становится 1. | Двоичный вход 3 отображает 1 с помощью InteliMonitor? **Ремонт:** Ремонт или замена проводов от C3-C до модуля управления BI-3 (провод 4003). | 6А |
| Двоичный вход 3 отображает 1 с помощью InteliMonitor? **NORepair: **Обнаружен неисправный модуль Inteli Bi-Fuel. | 6А |  |

### ШАГ 4. Проверьте топливную систему высокого давления.

#### ШАГ 4A. Проверьте на скачок высокого давления.

| **Условия: **Двигатель не работает. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте правильность работы исходной стороны топливной системы производителя оборудования (OEM). См. сервисную документацию изготовителя оборудования. Просмотрите историю неисправностей в InteliMonitor, чтобы определить, есть ли какие-либо неисправности, которые могут вызвать всплеск высокого давления. | Выявлены признаки всплеска высокого давления? **Ремонт:** Исправить источник всплеска высокого давления. См. сервисную документацию изготовителя оборудования. | 6А |
| Выявлены признаки всплеска высокого давления? **НЕТ** | 4B |  |

#### ШАГ 4B. Проверьте выключатель высокого давления.

| **Условия: **Двигатель не работает. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Удалите выключатель высокого давления. См. процедуру 019-580 в разделе 19. Удалите шестерочную установку из порта давления на фланце газоотвода. | Выберите правильный размер и без повреждений? *Да | 4C |
| Выберите правильный размер и без повреждений? **NORepair:** Установите правильное шестиугольное отверстие. См. процедуру 019-580 в разделе 19. | 6А |  |

#### ШАГ 4C. Проверьте регулятор давления топлива.

| **Условия: **Двигатель, работающий в режиме двойного топлива. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, чтобы регулятор давления топлива был отрегулирован и работал правильно. См. процедуру 005-245 в разделе 5. | Топливное давление в спецификациях? *Да | 5а |
| Топливное давление в спецификациях? **NORepair:** Регулятор давления регулируется таким образом, чтобы давление было в пределах спецификаций. См. процедуру 005-245 в разделе 5. Если давление не может быть включено в технические характеристики, то был обнаружен неисправный регулятор давления топлива. Заменить регулятор давления топлива. См. процедуру 005-042 в разделе 5. | 6А |  |

### ШАГ 5. Тестирование системы с помощью WinScope PC.

#### ШАГ 5A. Измерительные вводы с использованием WinScope.

| **Условия: **Двигатель не работает. Подключите ПК с помощью WinScope к контроллеру с двойным топливом. Включите питание панели управления. Поместите модуль управления двойным топливом в режим выключения. Загрузка может быть применена до 85 процентов номинально, шагами от 10 до 15 процентов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Выберите элемент для мониторинга в выборе каналов, в частности, в этом случае монитор BI-3, аналоговый блок управления напряжением батареи, значение регулирования газа «Engine Power» и «G/D Ratio». Установите период времени охвата для захвата на 150 мС и начинайте лесозаготовку. 1. Запустите двигатель и обратите внимание, что вход для BI-3 остается на уровне 1 во время коленчатого, пускового и ходового состояния. Это делается для обнаружения неисправностей, вызванных вибрацией или необоснованными падениями напряжения батареи, подводимого к управлению во время нормальной работы. 2. Продолжайте запись двоичных данных и попробуйте создать неисправность, мягко перемещая провода и проводную упряжку внутри панели и у разъемов, внешних по отношению к панели, чтобы найти прерывистые неисправности или свободные соединения. 3. Если на шагах 1 или 2 происходят неисправности, медленно добавляйте нагрузку на двигатель шагами. Разрешить двигателю и нагрузке стабилизироваться на каждом шаге в течение **no** менее 5 минут. Продолжайте регистрировать данные под нагрузкой до тех пор, пока не будет улавливаться неисправность или не будет применена мощность двигателя с номинальной мощностью 85%. | Есть ли случаи, когда BI-3 становится нулевым с использованием собранных данных и InteliMonitor? **Ремонт: **Используйте результаты указанных шагов для определения причины или разумных шагов и ремонта по мере необходимости. Справочная таблица 2 в разделе Shoptalk. | 6А |
| Есть ли случаи, когда BI-3 становится нулевым с использованием собранных данных и InteliMonitor? **НЕТ** | 6А |  |

### ШАГ 6. Снимите тревогу.

#### ШАГ 6A. Снимите тревогу.

| **Условия: **Двигатель не работает. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите питание от панели управления. Подожди 30 секунд. Восстановить подключение DC. Подтвердите, что вина Sd RegGasPress отсутствует или активна. | Двойной модуль управления топливом в состоянии отключения для Sd RegGasPress Возвращение к шагам устранения неполадок или обращение в авторизованное место ремонта Cummins®, если все шаги были завершены и проверены повторно. | 1А |
| Двойной модуль управления топливом в состоянии отключения для Sd RegGasPress **НЕТ** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - All gas flow will stop or the dual fuel control module will be prevented from entering dual fuel mode.
>
> ### How To Use This Tree
>
> This tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> **Circuit Description:**
>
> The gas train is equipped with a high-pressure switch. If the switch indicates a high-pressure condition after the Cummins® regulator, the input activation stops or prevents normal operation of the dual fuel system. The switch is a maintained or latching device, meaning if the condition occurs, the device **must** be manually reset before the signal will be restored to the dual fuel control module input.
>
> **Conditions for Running the Diagnostics:**
>
> Any time the system is operating and is substituting gas and the pressure switch indicates greater than accepted pressure for longer than a fixed delay, the system will indicate this message and assert protection.
>
> **Conditions for Activating the Fault Message:**
>
> Binary input 3 (BI-3) is open to battery negative when running in dual fuel mode for longer than the delay (60 seconds).
>
> Binary input 3 (BI-3) is open to battery negative when **not** in dual fuel mode for longer than 0.5 second.
>
> **Conditions for Clearing the Fault Automatically:**
>
> None.
>
> **Conditions for Clearing the Fault Codes Manually:**
>
> The gas pressure is restored below the set-point limit of the switch. The mechanical switch has been reset and the fault reset is depressed locally or via the software.
>
> ### Shoptalk
>
> The protection element is to protect against excessive gas delivery pressure to the engine.
>
> When the control module asserts the protection, the most probable cause is delivery gas pressure has spiked over the limit. The controller will not respond to the fault for 60 seconds. This can cause the operator to believe the fault occurred later than actual or the condition did not occur if monitoring pressure only as the mechanical switch is of a latching type. Inspect the switch to see if it 'tripped' before detailed troubleshooting of the circuit. A momentary spike will still cause the shutdown. If the input is open when the controller is powered ON or opens when in diesel only mode, it will cause the fault.
>
> Possible causes include:
>
> - Excessive gas pressure above the switch pressure limit
>
> - Malfunctioning gas pressure switch
>
> - Malfunctioning contacts on the gas pressure switch
>
> - Malfunctioning or loose wiring connections at the dual fuel control module for battery negative or binary input (BI-3)
>
> - Malfunctioning or loose wiring connections at gas pressure switch contacts
>
> - Malfunctioning dual fuel control module
>
> - Incorrectly installed or no orifice at switch.
>
> | Code of Message | Reason | Effect |
> |---|---|---|
> | Sd RegGasPress | BI-3 open in reference to battery negative. Circuit requires a grounded input for normal operation. | Dual fuel control module will not allow gas operations. Dual fuel control module will stop gas flow. |
>
> The following table provides reference information for this fault tree.
>
> | Table 1 |  |
> |---|---|
> | Fault Occurs When | Suspected Casue |
> | Input changes during starting - low battery voltage to control module | Check voltage drop, loose wiring connections to dual fuel control module at battery positive and negative connections. |
> | Input changes intermittently or randomly at low idle or very high load - vibration | Loose wiring, malfunctioning connectors, damaged pins |
> | Input changes when disturbing wires or connectors | Loose wiring, malfunctioning connectors, damaged pins |
> | Multiple binary input faults | System grounding, loose battery negative connections, malfunctioning batteries, improper wiring connections |
> | Fault occurs as soon as BO-1 and 7 activate | Suspect actual gas pressure spike occurs due to gas regulator malfunction or excessive delivery pressure |
> | Fault occurs during load shifts of approximately 25% power | Gas regulator transient (shift) response, gas delivery stability issues under load shift. Malfunctioning regulator or pressure limiting device |
> | Sd fault for 'LowGasPressIn' occurs while testing for Sd RegGasPress | Gas regulator transient (shift) response, gas delivery stability issues under load shift. Malfunctioning regulator or pressure limiting device |
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Validate the fault message. |  |
> |  | **STEP 1A.** Check for 'Active' fault message. | Control module in fault condition? |
> |  | **STEP 1B.** Check for 'Not Active' fault message. | Control module has occurrences for Sd RegGasPres? |
> |  | **STEP 1C.** Reset the fault. | Fault message cleared? |
> | STEP 2. | Reset the high-pressure switch. |  |
> |  | **STEP 2A.** Reset the high-pressure switch. | Above actions cleared fault? |
> | STEP 3. | Check the high fuel pressure switch and circuit. |  |
> |  | **STEP 3A.** Inspect the high fuel pressure switch and connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the switch. | Binary Input 3 displays a 1 using InteliMonitor? |
> |  | **STEP 3C.** Check the wiring harness. | Binary Input 3 displays a 1 using InteliMonitor? |
> |  | **STEP 3D.** Test the binary input response. | Binary Input 3 displays a 1 using InteliMonitor? |
> | STEP 4. | Check the high-pressure fuel system. |  |
> |  | **STEP 4A.** Check for a high-pressure spike. | Signs of a high-pressure spike identified? |
> |  | **STEP 4B.** Check the high-pressure switch orifice. | Orifice the correct size and free of damage? |
> |  | **STEP 4C.** Check the fuel pressure regulator. | Fuel pressure regulator within specifications? |
> | STEP 5. | Test the system using WinScope PC tool. |  |
> |  | **STEP 5A.** Test inputs using WinScope. | Any occurrences of BI-3 becoming zero using data collected and InteliMonitor? |
> | STEP 6. | Reset the alarm. |  |
> |  | **STEP 6A.** Reset the alarm. | Dual fuel control module in shutdown condition for Sd RegGasPress? |
>
> ### STEP 1. Validate the fault message.
>
> #### STEP 1A. Check for 'Active' fault message.
>
> | **Conditions:** Power ON duel fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the local display panel for a fault message. Navigate to the fault display screen. | Control module in fault condition? **YES** | 1C |
> | Control module in fault condition? **NO** | 1B |  |
>
> #### STEP 1B. Check for 'Not Active' fault message.
>
> | **Conditions:** Power ON dual fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect to the dual fuel control panel. Use InteliMonitor. Save a copy of the control module configuration file (archive file) on the local PC. Access the history shortcut. Check for occurrences of the message Sd RegGasPress. Check for other shutdown messages occurring at or near the time of the Sd RegGasPress. Check for other shutdown messages occurring at or near the time of the Sd RegGasPress. If other shutdown messages for binary inputs occur at the same time, see the procedure for ground and ground loop tests. | Control module has occurrences for Sd RegGasPress? **YES** | 1C |
> | Control module has occurrences for Sd RegGasPress? **NO** | No repair. |  |
>
> #### STEP 1C. Reset the fault.
>
> | **Conditions:** Power ON duel fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect to the dual fuel panel. Use InteliMonitor. Save a copy of the configuration file (archive file) on the local PC. Reset the fault from the control module or from the software InteliMonitor. | Fault message cleared? **YES** | 5A |
> | Fault message cleared? **NO** | 2A |  |
>
> ### STEP 2. Reset the high-pressure switch.
>
> #### STEP 2A. Reset the high-pressure switch.
>
> | **Conditions:** Power ON dual fuel control module. Make sure the dual fuel control module is in AUTO mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Press the rest button on the high-pressure switch. After pressing the reset button on switch, go to the panel and reset the fault. | Above actions cleared fault? **YES** | 4A |
> | Above actions cleared fault? **NO** | 3A |  |
>
> ### STEP 3. Check the high fuel pressure switch and circuit.
>
> #### STEP 3A. Inspect the high fuel pressure switch and connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the high fuel pressure switch connector from the dual fuel harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the dual fuel harness and high fuel pressure switch connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the high fuel pressure switch or harness connector. Check all harnesses connected in series. Clean the connector and pins. Replace the damaged section of harness or damaged switch. Repair the harness. Refer to Procedure 019-564 in Section 19. Replace the switch. Refer to Procedure 019-580 in Section 19. | 5A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the switch.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the high fuel pressure switch connector from the engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Place a jumper wire between the SIGNAL and RETURN wire on the wiring harness connector. | Binary Input 3 displays a 1 using InteliMonitor? **YESRepair:** The high-pressure switch has malfunctioned. Replace the high pressure switch. Refer to Procedure 019-580 in Section 19. | 5A |
> | Binary Input 3 displays a 1 using InteliMonitor? **NO** | 3C |  |
>
> #### STEP 3C. Check the wiring harness.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the wiring harness from the C3 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Place a jumper wire between the SIGNAL and RETURN wire on the C3 wiring harness connector. | Binary Input 3 displays a 1 using InteliMonitor? **YESRepair:** The wiring harness has malfunctioned. Repair or replace the wiring harness. Refer to Procedure 019-564 in Section 19. | 5A |
> | Binary Input 3 displays a 1 using InteliMonitor? **NO** | 3D |  |
>
> #### STEP 3D. Test the binary input response.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control module. Place dual fuel control module in OFF mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Make a temporary connection from the panel ground stud to the binary input terminal BI-3. Use an approved jumper wire. Observe when the connection is made, the input status becomes 1. | Binary Input 3 displays a 1 using InteliMonitor? **YESRepair:** Repair or replace the wiring from C3-C to the control module BI-3 (wire 4003). | 6A |
> | Binary Input 3 displays a 1 using InteliMonitor? **NORepair:** A malfunctioning Inteli Bi-Fuel module has been detected. | 6A |  |
>
> ### STEP 4. Check the high-pressure fuel system.
>
> #### STEP 4A. Check for a high-pressure spike.
>
> | **Conditions:** Engine not operating. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify the original equipment manufacturer (OEM) side of the fuel system is operating correctly. See equipment manufacturer service information. Review the fault history in InteliMonitor to determine if there are any faults that would cause a high-pressure spike. | Signs of a high-pressure spike identified? **YESRepair:** Correct the source of the high-pressure spike. See equipment manufacturer service information. | 6A |
> | Signs of a high-pressure spike identified? **NO** | 4B |  |
>
> #### STEP 4B. Check the high-pressure switch orifice.
>
> | **Conditions:** Engine not operating. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Remove the high-pressure switch. Refer to Procedure 019-580 in Section 19. Remove the hex orifice fitting from the pressure port on the gas outlet flange. | Orifice the correct size and free of damage? **YES** | 4C |
> | Orifice the correct size and free of damage? **NORepair:** Install the correct hex orifice. Refer to Procedure 019-580 in Section 19. | 6A |  |
>
> #### STEP 4C. Check the fuel pressure regulator.
>
> | **Conditions:** Engine operating in dual fuel mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify the fuel pressure regulator is adjusted and operating correctly. Refer to Procedure 005-245 in Section 5. | Fuel pressure within specifications? **YES** | 5A |
> | Fuel pressure within specifications? **NORepair:** Adjust the pressure regulator to bring the pressure within specifications. Refer to Procedure 005-245 in Section 5. If the pressure cannot be brought into specifications, a malfunctioning fuel pressure regulator has been detected. Replace the fuel pressure regulator. Refer to Procedure 005-042 in Section 5. | 6A |  |
>
> ### STEP 5. Test the system using WinScope PC tool.
>
> #### STEP 5A. Test inputs using WinScope.
>
> | **Conditions:** Engine not operating. Connect PC using WinScope to dual fuel controller. Switch control panel power ON. Place dual fuel control module in OFF mode. Load is available to be applied up to 85 percent nominal, in steps of 10 to 15 percent. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Select the item to monitor in the channel selections, specifically in this case monitor BI-3, analog control unit battery voltage, gas regulation value 'Engine Power' and 'G/D Ratio'. Set the scope time period to capture at 150 mS and begin logging. 1. Start the engine and observe that the input for BI-3 remains at 1 during the crank, start, and run condition. This is to locate faults caused by vibration or unreasonable drops in battery voltage supply to the control during normal operation. 2. Continue recording the binary data and attempt to create the fault by gently moving wires and the wiring harness inside the panel and at the connectors, external to the panel, to locate intermittent faults or loose connections. 3. If **no** faults occur in Steps 1 or 2, slowly add load to the engine in steps. Allow the engine and load to stabilize at each step for **no** less than 5 minutes. Continue logging data under load until either the fault is captured or 85 percent rated engine power has been applied. | Any occurrences of BI-3 becoming zero using data collected and InteliMonitor? **YESRepair:** Use results from the specified steps to determine the cause or reasonable steps and repair as needed. Reference Table 2 in the Shoptalk section. | 6A |
> | Any occurrences of BI-3 becoming zero using data collected and InteliMonitor? **NO** | 6A |  |
>
> ### STEP 6. Reset the alarm.
>
> #### STEP 6A. Reset the alarm.
>
> | **Conditions:** Engine not operating. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disconnect power from the control panel. Wait 30 seconds. Restore DC power connection. Confirm the fault for Sd RegGasPress is not present or active. | Dual fuel control module in shutdown condition for Sd RegGasPress? **YESRepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |
> | Dual fuel control module in shutdown condition for Sd RegGasPress? **NO** | Repair complete. |  |
