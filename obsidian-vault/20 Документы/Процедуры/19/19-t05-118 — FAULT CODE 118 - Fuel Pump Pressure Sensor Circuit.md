---
type: "Процедура"
doc: "19-t05-118"
title_en: "FAULT CODE 118 - Fuel Pump Pressure Sensor Circuit"
modified: "2014-09-19"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-118.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-118.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# FAULT CODE 118 - Fuel Pump Pressure Sensor Circuit

> [!abstract] Процедура · `19-t05-118`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TS - Troubleshooting Symptoms
> **Даты:** изменён 2014-09-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-118.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-118.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
> Чтобы не повредить новый блок управления двигателем (ЭБУ), перед его заменой разберитесь со всеми остальными активными кодами неисправностей.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 - пробный щуп типа штепсельной вилки DeutschTM/AMPTM/Metri-PackTM, номер детали 3822917 - пробный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM, номер детали 3824774 - ветвь проводной ветки PackardTM, номер детали 3164752 - ветвь проводной ветки DIN.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте несколько кодов ошибок. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Коды 116 и 451 не активны? |
| ШАГ 2. | Проверьте датчик давления топливного насоса. |  |
|  | **STEP 2A.** Осмотрите датчик давления топливного насоса и контакты разъема для проводов двигателя. | Грязные или поврежденные контакты? |
|  | **ШАГ 2В.** Прочитайте коды неисправностей. | Код 118 активен? |
|  | **STEP 2C** Проверьте напряжение подачи топлива на топливный насос. | 4,75-5,25-ВДЦ? |
|  | **STEP 2C-1.** Проверьте напряжение подачи топлива на топливный насос. | 4,75-5,25-ВДЦ? |
|  | **STEP 2D.** Проверьте напряжение сигнала давления топливного насоса. | Двигатель 0,42-0,58-VDC остановился? |
|  | **STEP 2D-1.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. омов". |
|  | **STEP 2D-2.** Проверить непрерывность в ремне электропроводки двигателя. | Менее 10 Ом? |
|  | **STEP 2D-3.** Проверьте реакцию ECM. | Код 118 неактивен, код 119 активен. |
|  | **STEP 2D-4.** Проверить сопротивление от контакта с сигналом до контакта с подачей в порту ECM. | Более 35 тысяч ом? |
| ШАГ 3. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 3A.** Проверить контактные линзы для проводов двигателя и разъема ECM. | Грязные или поврежденные контакты? |
|  | **СТЭП 3В.** Прочитайте коды неисправностей. | Код 118 активен? |
|  | **STEP 3C.** Проверить наличие открытой цепи. | Менее 10 Ом? |
|  | **STEP 3D.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тысяч ом? |
| ШАГ 4. | Проверьте ответ на ECM. |  |
|  | **STEP 4A.** Проверить наличие соответствующего ответа на ECM. | Код 118 неактивен, код 119 активен. |
| ШАГ 5. | Сбросьте коды неисправностей. |  |
|  | **STEP 5A.** Отключить код ошибки. | Код 118 неактивен? |
|  | **STEP 5B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте несколько кодов ошибок.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Подключить электронный инструмент InsiteTM Turn ignition switch ON. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Коды 116 и 451 не активны? | 2А |
|  | Многократное дерево кода ошибки |  |

### ШАГ 2. Проверьте датчик давления топливного насоса.

#### ШАГ 2A. Проверьте датчик давления топливного насоса и контакты разъёма ремня электропроводки двигателя.

| **Условия:** Замок зажигания отключите проводку двигателя от датчика давления топливного насоса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить датчик давления топливного насоса и контакты разъёма ремня электропроводки двигателя на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? | 2В |
| В разъеме двигателя ECM или разъеме ремней электропроводки двигателя было обнаружено поврежденное соединение. Ремонт поврежденных контактов. Ремонт или замена жгута проводов двигателя или замена датчика давления топливного насоса, в зависимости от того, какие контакты повреждены. Смывать грязь, мусор или влагу с контактов разъема, использовать электронный контактный очиститель, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. См. процедуру 019-201 в разделе 19. См. процедуру 019-202 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. Замените датчик давления времени. См. процедуру 019-191 в разделе 19. Замените датчик давления топливного насоса. См. процедуру 019-118 в разделе 19. | 5а |  |

#### ШАГ 2B. Считайте коды неисправностей.

| **Условия:** Подключите все компоненты Подключите электронный сервисный инструмент INSITETM Включите переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 118 активен? | 2C |
| Ремонт завершён. | 5В |  |

#### ШАГ 2C. Проверьте напряжение подачи давления топливного насоса.

| **Условия:** Отсоедините датчик давления топливного насоса от электропроводки двигателя Установите соответствующий датчик давления топливного насоса, проводящий ветвь провода ремня между датчиком и разъемом ремня электропитания двигателя Включите переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение подачи давления топливного насоса. Измерьте напряжение питания, установив разъёмы питания проводов ветвящегося кабеля (контакт A) и возврата (контакт B) в мультиметр. | 4,75-5,25-ВДЦ? | 2D |
|  | 2С-1 |  |

#### ШАГ 2C-1. Проверьте напряжение подачи давления топливного насоса.

| **Условия:** Отсоедините проводку от ветки провода от датчика. (Оставить проводку жгута ветвь кабеля, подключенного к жгуту проводов двигателя.) Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение подачи давления топливного насоса. Измерьте напряжение питания, установив разъёмы питания проводов ветвящегося кабеля (контакт A) и возврата (контакт B) в мультиметр. | 4,75-5,25-ВДЦ? Замените датчик давления топливного насоса.[[00-019-118 — Fuel Pump Pressure Sensor\|См. процедуру 019-118 в разделе 19.]] | 5а |
|  | 3А |  |

#### ШАГ 2D. Проверьте напряжение сигнала давления топливного насоса.

| **Условия:** Отсоедините датчик давления топливного насоса от электропроводки двигателя Установите соответствующий датчик давления топливного насоса, проводящий ветвь провода ремня между датчиком и разъемом ремня электропроводки двигателя Включите переключатель зажигания ON Engine, не работающий. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение сигнала давления топливного насоса. Измерьте напряжение сигнала, установив сигнал проводов ветвящегося кабеля (контакт C) и разъемы возврата (контакт B) в мультиметр. | 0,42-0,58-VDC? | 3А |
| не соответствует спецификации. | 2D-1 |  |

#### ШАГ 2D-1. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия: **Отключите переключатель зажигания двигателя Отключите датчик давления топливного насоса от датчика давления двигателя Отключите датчик давления рельса от ремня электропитания Отключите датчик давления времени от ремня электропитания двигателя Отключите барометрический датчик давления от ремня электропитания двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание от пин-кодов до пин-кодов. Измерьте сопротивление от контакта 5 проводов двигателя с помощью разъема ECM ко всем другим штифтам в разъеме. Измерьте сопротивление от контакта 32 проводов двигателя с помощью разъема ECM со всеми другими штифтами в разъеме. Измерьте сопротивление от контакта 18 проводов двигателя с помощью разъема ECM со всеми другими штифтами в разъеме. | Более 100 тысяч ом? | 2D-2 |
| Ремонт или замена проводов двигателя ремень ремень проводов двигателя ремень. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 5а |  |

#### ШАГ 2D-2. Проверьте непрерывность в ремне электропроводки двигателя.

| **Условия:** Замок зажигания отключите от электропроводки двигателя ремень отключения от датчика давления топливного насоса от электропроводки двигателя ремень. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте непрерывность в ремне электропроводки двигателя. Измерить сопротивление от контакта 5 проводов двигателя с помощью разъема ECM для контакта A разъема датчика давления топливного насоса. Измерить сопротивление от контакта 32 проводов двигателя с помощью разъема ECM для контакта C разъема датчика давления топливного насоса. Измерить сопротивление от контакта 18 проводов двигателя с помощью разъема ECM для контакта B разъема датчика давления топливного насоса. | Менее 10 Ом? | 2D-3 |
| Ремонт или замена проводов двигателя ремень ремень проводов двигателя ремень. См. процедуру 019-201 в разделе 19. См. процедуру 019-202 в разделе 19. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 5а |  |

#### ШАГ 2D-3. Проверьте реакцию ECM.

| **Условия:** Отсоедините электропроводку двигателя от электронно-сервисного инструментария ECM Connect INSITETM Включите переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующий ответ ECM. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 118 неактивен, код 119 активен. | 2D-4 |
| Код 118 активен. Заменить ECM. См. процедуру 019-031 в разделе 19. | 5а |  |

#### ШАГ 2D-4. Проверьте сопротивление от контакта сигнала до контакта подачи в порту ECM.

| **Условия:** Замок зажигания отключите от разъема электропроводки жгута двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сопротивление от контакта сигнала до контакта подачи в порту ECM. Измерьте сопротивление от контакта 32 (сигнал) до контакта 5 (предложение) в соединительном порту электропроводки двигателя ECM. | Более 35 Ом? Замените датчик давления топливного насоса. См. процедуру 019-118 в разделе 19. | 5а |
| Менее 35 тысяч ом? Заменить ECM. См. процедуру 019-031 в разделе 19. | 5а |  |

### ШАГ 3. Проверьте жгут проводов двигателя.

#### ШАГ 3A. Проверьте контакты разъёма электропроводки двигателя и разъема ECM.

| **Условия:** Замок зажигания отключите от электропроводки двигателя ремень от ECM Отключите электропроводку двигателя от датчика давления топливного насоса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты электропроводки двигателя и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? | 3B |
| В разъеме двигателя ECM или разъеме ремней электропроводки двигателя было обнаружено поврежденное соединение. Ремонт поврежденных контактов. Ремонт или замена ремня электропроводки двигателя, или замена ECM, в зависимости от того, какие контакты повреждены. Смывать грязь, мусор или влагу с контактов разъема, использовать электронный контактный очиститель, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. Заменить ECM. См. процедуру 019-031 в разделе 19. | 5а |  |

#### ШАГ 3B. Считайте коды неисправностей.

| **Условия:** Подключите все компоненты Подключите электронный сервисный инструмент INSITETM Включите переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 118 активен? | 3C |
| Ремонт завершён. | 5В |  |

#### ШАГ 3C. Проверьте цепь на обрыв.

| **Условия:** Замок зажигания отключите от электропроводки двигателя ремень от ECM Отключите электропроводку двигателя от датчика давления топливного насоса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление от контакта 18 проводов двигателя с разъемом жгута проводов к контакту В датчика давления топливного насоса с разъемом жгута проводов, проводкой двигателя со стороны жгута проводов. | Менее 10 Ом? | 3D |
| Ремонт или замена электропроводки двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-201 в разделе 19. См. процедуру 019-202 в разделе 19. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 5а |  |

#### ШАГ 3D. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия: **Замок зажигания отключите от электропроводки двигателя ремень отключения электропроводки двигателя от датчика давления времени Отключите электропроводку двигателя от датчика давления рельса Отключите электропроводку двигателя от датчика давления топливного насоса Отключите барометрический датчик давления от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверка на замыкание между контактами. Измерьте сопротивление от контакта 5 разъёма ремня электропроводки двигателя со всеми другими штифтами в разъеме. Измерьте сопротивление от контакта 32 разъёма ремня электропроводки двигателя со всеми другими штифтами в разъеме. Измерьте сопротивление от контакта 18 разъёма ремня электропроводки двигателя со всеми другими штифтами в разъеме. Ищите короткие замыкания от напряжения батареи или датчика до контакта 5, 32 или 18. | Более 100 тысяч ом? | 4А |
| Ремонт или замена электропроводки двигателя ремень ремень электропроводки двигателя ремень. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 5а |  |

### ШАГ 4. Проверьте ответ на ECM.

#### ШАГ 4A. Проверьте соответствующий ответ ECM.

| **Условия:** Отсоедините электропроводку двигателя от электронно-сервисного инструментария ECM Connect INSITETM Включите переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующий ответ ECM. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 118 неактивен, код 119 активен. | 5а |
| Заменить ECM. См. процедуру 019-031 в разделе 19. | 5а |  |

### ШАГ 5. Сбросьте коды неисправностей.

#### ШАГ 5A. Отключите код неисправности.

| **Условия:** Подключить все компоненты Подключить электронный сервисный инструмент INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода 116. | Код 118 неактивен? | 5В |
| Вернитесь к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 5B. Сбросьте неактивные коды неисправностей.

| **Условия:** Подключите все компоненты Включите переключатель зажигания ON Connect INSITETM электронный сервисный инструмент. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3824774 - Packard™ breakout cable Part Number 3164752 - DIN breakout cable.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check for multiple fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Codes 116 and 451 are not active? |
> | STEP 2. | Check the fuel pump pressure sensor. |  |
> |  | **STEP 2A.** Inspect the fuel pump pressure sensor and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Read the fault codes. | Fault Code 118 active? |
> |  | **STEP 2C.** Check the fuel pump pressure supply voltage. | 4.75 to 5.25-VDC? |
> |  | **STEP 2C-1.** Check the fuel pump pressure supply voltage. | 4.75 to 5.25-VDC? |
> |  | **STEP 2D.** Check the fuel pump pressure signal voltage. | 0.42 to 0.58-VDC engine stopped? |
> |  | **STEP 2D-1.** Check for a short circuit from pin to pin. | More than 100k ohms” |
> |  | **STEP 2D-2.** Check for continuity in the engine harness. | Less than 10 ohms? |
> |  | **STEP 2D-3.** Check the ECM response. | Fault Code 118 inactive; Fault Code 119 active? |
> |  | **STEP 2D-4.** Check the resistance from signal pin to supply pin in the ECM port. | More than 35k ohms? |
> | STEP 3. | Check the engine harness. |  |
> |  | **STEP 3A.** Inspect the engine harness and ECM connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Read the fault codes. | Fault Code 118 active? |
> |  | **STEP 3C.** Check for an open circuit. | Less than 10 ohms? |
> |  | **STEP 3D.** Check for a short circuit from pin to pin. | More than 100k ohms? |
> | STEP 4. | Check for an ECM response. |  |
> |  | **STEP 4A.** Check for the appropriate ECM response. | Fault Code 118 inactive; Fault Code 119 active? |
> | STEP 5. | Clear the fault codes. |  |
> |  | **STEP 5A.** Disable the fault code. | Fault Code 118 inactive? |
> |  | **STEP 5B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check for multiple fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Connect INSITE™ electronic service tool Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Codes 116 and 451 are not active? | 2A |
> |  | Multiple fault code tree |  |
>
> ### STEP 2. Check the fuel pump pressure sensor.
>
> #### STEP 2A. Inspect the fuel pump pressure sensor and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the fuel pump pressure sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect fuel pump pressure sensor and engine harness connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? | 2B |
> | A damaged connection has been detected in the ECM engine connector or engine harness connector. Repair damaged pins. Repair or replace the engine harness, or replace the fuel pump pressure sensor, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins, use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-201 in Section 19. Refer to Procedure 019-202 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the timing pressure sensor. Refer to Procedure 019-191 in Section 19. Replace the fuel pump pressure sensor. Refer to Procedure 019-118 in Section 19. | 5A |  |
>
> #### STEP 2B. Read the fault codes.
>
> | **Conditions:** Connect all components Connect INSITE™ electronic service tool Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 118 active? | 2C |
> | Repair complete. | 5B |  |
>
> #### STEP 2C. Check the fuel pump pressure supply voltage.
>
> | **Conditions:** Disconnect the fuel pump pressure sensor from the engine harness Install the appropriate fuel pump pressure sensor breakout cable between the sensor and the engine harness connector Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel pump pressure supply voltage. Measure the supply voltage by installing the breakout cable's supply (pin A) and return (pin B) connectors into the multimeter. | 4.75 to 5.25-VDC? | 2D |
> |  | 2C-1 |  |
>
> #### STEP 2C-1. Check the fuel pump pressure supply voltage.
>
> | **Conditions:** Disconnect the breakout cable from the sensor. (Leave breakout cable connected to the engine harness.) Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel pump pressure supply voltage. Measure the supply voltage by installing the breakout cable's supply (pin A) and return (pin B) connectors into the multimeter. | 4.75 to 5.25-VDC? Replace the fuel pump pressure sensor. [[00-019-118 — Fuel Pump Pressure Sensor\|Refer to Procedure 019-118 in Section 19.]] | 5A |
> |  | 3A |  |
>
> #### STEP 2D. Check the fuel pump pressure signal voltage.
>
> | **Conditions:** Disconnect the fuel pump pressure sensor from the engine harness Install the appropriate fuel pump pressure sensor breakout cable between the sensor and the engine harness connector Turn keyswitch ON Engine not running. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel pump pressure signal voltage. Measure the signal voltage by installing the breakout cable's signal (pin C) and return (pin B) connectors into the multimeter. | 0.42 to 0.58-VDC? | 3A |
> | Does **not** meet specification. | 2D-1 |  |
>
> #### STEP 2D-1. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the ECM Disconnect fuel pump pressure sensor from the engine harness Disconnect rail pressure sensor from the engine harness Disconnect the timing pressure sensor from the engine harness Disconnect the barometric pressure sensor from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin to pin. Measure the resistance from pin 5 of the engine harness ECM connector to all other pins in the connector. Measure the resistance from pin 32 of the engine harness ECM connector to all other pins in the connector. Measure the resistance from pin 18 of the engine harness ECM connector to all other pins in the connector. | More than 100k ohms? | 2D-2 |
> | Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 5A |  |
>
> #### STEP 2D-2. Check for continuity in the engine harness.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the ECM Disconnect the fuel pump pressure sensor from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for continuity in the engine harness. Measure the resistance from pin 5 of the engine harness ECM connector to pin A of the fuel pump pressure sensor connector. Measure the resistance from pin 32 of the engine harness ECM connector to pin C of the fuel pump pressure sensor connector. Measure the resistance from pin 18 of the engine harness ECM connector to pin B of the fuel pump pressure sensor connector. | Less than 10 ohms? | 2D-3 |
> | Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-201 in Section 19. Refer to Procedure 019-202 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 5A |  |
>
> #### STEP 2D-3. Check the ECM response.
>
> | **Conditions:** Disconnect the engine harness from the ECM Connect INSITE™ electronic service tool Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 118 inactive; Fault Code 119 active? | 2D-4 |
> | Fault Code 118 active. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 5A |  |
>
> #### STEP 2D-4. Check the resistance from signal pin to supply pin in the ECM port.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the engine harness connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the resistance from signal pin to supply pin in the ECM port. Measure the resistance from pin 32 (signal) to pin 5 (supply) in the ECM engine harness connector port. | More than 35 ohms? Replace the fuel pump pressure sensor. Refer to Procedure 019-118 in Section 19. | 5A |
> | Less than 35k ohms? Replace the ECM. Refer to Procedure 019-031 in Section 19. | 5A |  |
>
> ### STEP 3. Check the engine harness.
>
> #### STEP 3A. Inspect the engine harness and ECM connector pins.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the ECM Disconnect the engine harness from the fuel pump pressure sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? | 3B |
> | A damaged connection has been detected in the ECM engine connector or engine harness connector. Repair damaged pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins, use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 5A |  |
>
> #### STEP 3B. Read the fault codes.
>
> | **Conditions:** Connect all components Connect INSITE™ electronic service tool Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 118 active? | 3C |
> | Repair complete. | 5B |  |
>
> #### STEP 3C. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the ECM Disconnect the engine harness from the fuel pump pressure sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance from pin 18 of the engine harness connector to pin B of the fuel pump pressure sensor harness connector, engine harness side. | Less than 10 ohms? | 3D |
> | Repair or replace engine harness. Repair the engine harness. Refer to Procedure 019-201 in Section 19. Refer to Procedure 019-202 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 5A |  |
>
> #### STEP 3D. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the ECM Disconnect the engine harness from the timing pressure sensor Disconnect the engine harness from the rail pressure sensor Disconnect the engine harness from the fuel pump pressure sensor Disconnect the barometric pressure sensor from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for short circuit from pin to pin. Measure the resistance from pin 5 of the engine harness connector to all other pins in the connector. Measure the resistance from pin 32 of the engine harness connector to all other pins in the connector. Measure the resistance from pin 18 of the engine harness connector to all other pins in the connector. Look for short circuits from battery or sensor voltage to pin 5, 32, or 18. | More than 100k ohms? | 4A |
> | Repair or replace engine harness Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 5A |  |
>
> ### STEP 4. Check for an ECM response.
>
> #### STEP 4A. Check for the appropriate ECM response.
>
> | **Conditions:** Disconnect the engine harness from the ECM Connect INSITE™ electronic service tool Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 118 inactive; Fault Code 119 active? | 5A |
> | Replace the ECM. Refer to Procedure 019-031 in Section 19. | 5A |  |
>
> ### STEP 5. Clear the fault codes.
>
> #### STEP 5A. Disable the fault code.
>
> | **Conditions:** Connect all components Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to verify that Fault Code 116 is inactive. | Fault Code 118 inactive? | 5B |
> | Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 5B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components Turn keyswitch ON Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
