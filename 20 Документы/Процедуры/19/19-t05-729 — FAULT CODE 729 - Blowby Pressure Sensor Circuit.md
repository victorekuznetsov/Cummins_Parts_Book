---
type: "Процедура"
doc: "19-t05-729"
title_en: "FAULT CODE 729 - Blowby Pressure Sensor Circuit"
modified: "2013-04-15"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-729.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-729.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# FAULT CODE 729 - Blowby Pressure Sensor Circuit

> [!abstract] Процедура · `19-t05-729`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2013-04-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-729.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-729.pdf)

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
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 - пробный щуп типа вилки DeutschTM/AMPTM/Metri-PackTM, номер детали 3822917 - пробный щуп типа гнезда DeutschTM/AMPTM/Metri-PackTM, номер детали 3823994 - пробный щуп типа гнезда DeutschTM, номер детали 3824774 - проводной ветвь ремня.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте несколько кодов ошибок. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Коды 123, 141, 222, 232, 265 и 471 не активны? |
| ШАГ 2. | Проверьте датчик давления. |  |
|  | **STEP 2A.** Осмотрите датчик давления продувки и контакты разъема жгута двигателя. | Грязные или поврежденные контакты? |
|  | **ШАГ 2В.** Прочитайте коды неисправностей. | Код ошибки 729 активен? |
|  | **STEP 2C** Проверить напряжение подачи под давлением ECM. | 4,75-5,25-ВДЦ? |
|  | **STEP 2C-1.** Проверьте напряжение подачи под давлением ECM. | 4,75-5,25-VDC двигатель остановился? |
|  | **STEP 2D.** Проверьте напряжение сигнала обдува ECM. | Двигатель 0,42-0,58-VDC остановился? |
|  | **STEP 2D-1.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тысяч ом? |
|  | **STEP 2D-2.** Проверить непрерывность в ремне электропроводки двигателя. | Менее 10 Ом? |
|  | **STEP 2D-3.** Проверить сопротивление от контакта с сигналом до обратного контакта в порту ECM. | Более 35 тысяч ом? |
| ШАГ 3. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 3A.** Проверить контактные линзы для проводов двигателя и разъема ECM. | Грязные или поврежденные контакты? |
|  | **СТЭП 3В.** Прочитайте коды неисправностей. | Код ошибки 729 активен? |
|  | **STEP 3C.** Проверить наличие открытой цепи. | Менее 10 Ом? |
|  | **STEP 3D.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тысяч ом? |
|  | **ШАГ 3Е.** Проверьте короткое замыкание на блокировку двигателя. | Более 100 тысяч ом? |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 729 неактивен? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте несколько кодов ошибок.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Подключить электронный сервисный инструмент INSITETM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Коды 123, 141, 222, 232, 265 и 471 не активны? | 2А |
| Возможен открытый контур в датчике общего провода питания. | Несколько деревьев кода неисправностей |  |

### ШАГ 2. Проверьте датчик давления.

#### ШАГ 2A. Проверьте датчик давления продувки и контакты разъёма жгута двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините проводку двигателя от датчика давления продувки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите датчик давления продувки и контакты разъёма ремня электропроводки двигателя на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? | 2В |
| В разъеме двигателя ECM или разъеме ремней электропроводки двигателя было обнаружено поврежденное соединение. Ремонт поврежденных контактов. Ремонт или замена жгута проводов двигателя или замена датчика давления продувки, в зависимости от того, какие контакты повреждены. Смывать грязь, мусор или влагу с контактов разъема, использовать электронный контактный очиститель, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. См. процедуру 019-201 в разделе 19. См. процедуру 019-202 в разделе 19. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. Заменить датчик давления. См. процедуру 019-011 в разделе 19. | 4А |  |

#### ШАГ 2B. Считайте коды неисправностей.

| **Условия:** Подключить электронный сервисный инструмент INSITETM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 729 активен? | 2C |
| Ремонт завершён. | 4B |  |

#### ШАГ 2C. Проверьте напряжение подачи под давлением ECM.

| **Условия:** Отсоединить датчик давления продувки от электропроводки двигателя. Установите проводной кабель с датчиком давления продувки, номер детали 3824774, между датчиком и разъёмом с ремнем электропроводки двигателя. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение подачи под давлением ECM. Измерьте напряжение питания, установив подачу проводов ветвящегося кабеля (контакт A) и разъемы возврата (контакт B) в мультиметр. | 4,75-5,25-ВДЦ? | 2D |
|  | 2С-1 |  |

#### ШАГ 2C-1. Проверьте напряжение подачи под давлением ECM.

| **Условия:** Отсоедините проводку от ветки провода от датчика. (Оставить проводку жгута ветвь кабеля, подключенного к жгуту проводов двигателя.) Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение подачи под давлением ECM. Измерьте напряжение питания, установив разъёмы питания проводов ветвящегося кабеля (контакт A) и возврата (контакт B) в мультиметр. | 4,75-5,25-ВДЦ? Заменить датчик давления. См. процедуру 019-011 в разделе 19. | 4А |
|  | 3А |  |

#### ШАГ 2D. Проверьте напряжение сигнала давления ECM.

| **Условия:** Отсоединить датчик давления продувки от электропроводки двигателя. Установите проводной кабель с датчиком давления продувки, номер детали 3824774, между датчиком и разъёмом с ремнем электропроводки двигателя. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение сигнала давления ECM. Измерьте напряжение сигнала, установив сигнал проводов ветвящегося кабеля (контакт C) и разъемы возврата (контакт B) в мультиметр. | 0,42-0,58-VDC? | 3А |
| не соответствует спецификации. | 4А |  |

#### ШАГ 2D-1. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отсоедините датчик давления от электропроводки двигателя. Отсоедините датчик давления рельсов от электропроводки двигателя. Отсоедините датчик давления топливного насоса от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание от пин-кодов до пин-кодов. Измерьте сопротивление от контакта 6 проводов двигателя с помощью разъема ECM ко всем другим штифтам в разъеме. Измерьте сопротивление от контакта 25 проводов двигателя с помощью разъема ECM со всеми другими штифтами в разъеме. Измерьте сопротивление от контакта 17 проводов двигателя с помощью разъема ECM со всеми другими штифтами в разъеме. | Более 100 тысяч ом? | 2D-2 |
| Ремонт или замена ремня электропроводки двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 5а |  |

#### ШАГ 2D-2. Проверьте непрерывность в ремне электропроводки двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отсоедините датчик давления от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте непрерывность в ремне электропроводки двигателя. Измерить сопротивление от контакта 6 проводов двигателя с помощью разъема ECM к контакту A датчика давления продувки с помощью разъема с помощью ремня. Измерить сопротивление от контакта 25 проводов двигателя с помощью разъема ECM к контакту C датчика давления продувки с помощью разъема с жгутом проводов. Измерить сопротивление от контакта 17 проводов двигателя с помощью разъема ECM к контакту B датчика давления продувки с помощью разъема с помощью ремня. | Менее 10 Ом? | 2D-3 |
| Ремонт или замена ремня электропроводки двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-201 в разделе 19. См. процедуру 019-202 в разделе 19. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 5а |  |

#### ШАГ 2D-3. Проверьте сопротивление от контакта с сигналом до обратного контакта в порту ECM.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сопротивление от контакта с сигналом до обратного контакта в порту ECM. Измерьте сопротивление от контакта 25 (сигнал) до контакта 17 (возврат) в соединительном порту электропроводки двигателя ECM. | Более 35 тысяч ом? Заменить датчик давления. См. процедуру 019-011 в разделе 19. | 5а |
| Менее 35 тысяч ом? Заменить ECM. См. процедуру 019-031 в разделе 19. | 5а |  |

### ШАГ 3. Проверьте жгут проводов двигателя.

#### ШАГ 3A. Проверьте контакты разъёма электропроводки двигателя и разъема ECM.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты электропроводки двигателя и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? | 3B |
| В разъеме двигателя ECM или разъеме ремней электропроводки двигателя было обнаружено поврежденное соединение. Ремонт поврежденных контактов. Ремонт или замена ремня электропроводки двигателя, или замена ECM, в зависимости от того, какие контакты повреждены. Смывать грязь, мусор или влагу с контактов разъема, использовать электронный контактный очиститель, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. Заменить ECM. См. процедуру 019-031 в разделе 19. | 4А |  |

#### ШАГ 3B. Считайте коды неисправностей.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 729 активен? | 3C |
| Ремонт завершён. | 4B |  |

#### ШАГ 3C. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от ECM. Отсоедините проводку двигателя от датчика давления продувки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление от контакта 25 проводов двигателя с помощью разъема ECM к контакту C с разъемом датчика сжатия под давлением. Измерить сопротивление от контакта 6 проводов двигателя с помощью разъема ECM для контакта с A (+5-VDC питания) датчика давления продувки проводов разъема. | Менее 10 Ом? | 3D |
| Ремонт или замена ремня электропроводки двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-201 в разделе 19. См. процедуру 019-202 в разделе 19. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 4А |  |

#### ШАГ 3D. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Замок зажигания отключите от электропроводки двигателя электроузел от ECM. Отсоедините проводку двигателя от датчика давления продувки. Отсоедините проводку двигателя от датчика температуры воздуха впускного коллектора. Отсоедините проводку двигателя от датчика давления окружающего воздуха. Отсоедините жгут электропроводки двигателя от датчика давления впускного коллектора. Отсоедините проводку двигателя от датчика температуры топлива. Отсоедините проводку двигателя от датчика давления масла. Отсоедините проводку двигателя от датчика давления охлаждающей жидкости. Отсоедините проводку двигателя от датчика температуры охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание от пин-кодов до пин-кодов. Измерьте сопротивление от контакта 25 проводов двигателя с помощью разъема ECM со всеми другими штифтами в разъеме. Измерьте сопротивление от контакта 17 проводов двигателя с помощью разъема ECM со всеми другими штифтами в разъеме. Измерьте сопротивление от контакта 6 проводов двигателя с помощью разъема ECM ко всем другим штифтам в разъеме. | Более 100 тысяч ом? | 3E |
| Ремонт или замена ремня электропроводки двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 4А |  |

#### ШАГ 3E. Проверьте короткое замыкание на блокировку двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от ECM. Отсоедините проводку двигателя от датчика давления продувки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на блокировку двигателя. Измерьте сопротивление от контакта 25 проводов двигателя с помощью разъема ECM к заземлению блока двигателя. Измерьте сопротивление от контакта 17 проводов двигателя с помощью разъема ECM к заземлению блока двигателя. Измерьте сопротивление от контакта 6 проводов двигателя с помощью разъема ECM к заземлению блока двигателя. | Более 100 тысяч ом? Заменить ECM. См. процедуру 019-031 в разделе 19. | 4А |
| Ремонт или замена ремня электропроводки двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 4А |  |

### ШАГ 4. Сбросьте коды неисправностей.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте инструмент для проверки неактивности кода 729. | Код 729 неактивен? | 4B |
| Вернитесь к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды ошибок очищены | Ремонт завершён |
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
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3823994 - female Deutsch™ test lead, Part Number 3824774 - breakout cable.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check for multiple fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Codes 123, 141, 222, 232, 265, and 471 are not active? |
> | STEP 2. | Check the blowby pressure sensor. |  |
> |  | **STEP 2A.** Inspect the blowby pressure sensor and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Read the fault codes. | Fault Code 729 active? |
> |  | **STEP 2C.** Check ECM blowby pressure supply voltage. | 4.75 to 5.25-VDC? |
> |  | **STEP 2C-1.** Check ECM blowby pressure supply voltage. | 4.75 to 5.25-VDC engine stopped? |
> |  | **STEP 2D.** Check ECM blowby pressure signal voltage. | 0.42 to 0.58-VDC engine stopped? |
> |  | **STEP 2D-1.** Check for a short circuit from pin to pin. | More than 100k ohms? |
> |  | **STEP 2D-2.** Check for continuity in the engine harness. | Less than 10 ohms? |
> |  | **STEP 2D-3.** Check the resistance from SIGNAL pin to RETURN pin in the ECM port. | More than 35k ohms? |
> | STEP 3. | Check the engine harness. |  |
> |  | **STEP 3A.** Inspect the engine harness and ECM connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Read the fault codes. | Fault Code 729 active? |
> |  | **STEP 3C.** Check for an open circuit. | Less than 10 ohms? |
> |  | **STEP 3D.** Check for a short circuit from pin to pin. | More than 100k ohms? |
> |  | **STEP 3E.** Check for a short circuit to engine block ground. | More than 100k ohms? |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 729 inactive? |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check for multiple fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Codes 123, 141, 222, 232, 265, and 471 are not active? | 2A |
> | Possible open circuit in the sensor common supply wire. | Multiple fault code trees |  |
>
> ### STEP 2. Check the blowby pressure sensor.
>
> #### STEP 2A. Inspect the blowby pressure sensor and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the blowby pressure sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the blowby pressure sensor and engine harness connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? | 2B |
> | A damaged connection has been detected in the ECM engine connector or engine harness connector. Repair damaged pins. Repair or replace the engine harness, or replace the blowby pressure sensor, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins, use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-201 in Section 19. Refer to Procedure 019-202 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the blowby pressure sensor. Refer to Procedure 019-011 in Section 19. | 4A |  |
>
> #### STEP 2B. Read the fault codes.
>
> | **Conditions:** Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 729 active? | 2C |
> | Repair complete. | 4B |  |
>
> #### STEP 2C. Check ECM blowby pressure supply voltage.
>
> | **Conditions:** Disconnect the blowby pressure sensor from the engine harness. Install the blowby pressure sensor breakout cable, Part Number 3824774, between the sensor and the engine harness connector. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check ECM blowby pressure supply voltage. Measure the supply voltage by installing the breakout cable's supply (pin A) and return connectors (pin B) into the multimeter. | 4.75 to 5.25-VDC? | 2D |
> |  | 2C-1 |  |
>
> #### STEP 2C-1. Check ECM blowby pressure supply voltage.
>
> | **Conditions:** Disconnect the breakout cable from the sensor. (Leave breakout cable connected to the engine harness.) Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ECM blowby pressure supply voltage. Measure the supply voltage by installing the breakout cable's supply (pin A) and return (pin B) connectors into the multimeter. | 4.75 to 5.25-VDC? Replace the blowby pressure sensor. Refer to Procedure 019-011 in Section 19. | 4A |
> |  | 3A |  |
>
> #### STEP 2D. Check ECM blowby pressure signal voltage.
>
> | **Conditions:** Disconnect the blowby pressure sensor from the engine harness. Install the blowby pressure sensor breakout cable, Part Number 3824774, between the sensor and the engine harness connector. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ECM blowby pressure signal voltage. Measure the signal voltage by installing the breakout cable's signal (pin C) and return connectors (pin B) into the multimeter. | 0.42 to 0.58-VDC? | 3A |
> | Does **not** meet specification. | 4A |  |
>
> #### STEP 2D-1. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect blowby pressure sensor from the engine harness. Disconnect rail pressure sensor from the engine harness. Disconnect the fuel pump pressure sensor from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin to pin. Measure the resistance from pin 6 of the engine harness ECM connector to all other pins in the connector. Measure the resistance from pin 25 of the engine harness ECM connector to all other pins in the connector. Measure the resistance from pin 17 of the engine harness ECM connector to all other pins in the connector. | More than 100k ohms? | 2D-2 |
> | Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 5A |  |
>
> #### STEP 2D-2. Check for continuity in the engine harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the blowby pressure sensor from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for continuity in the engine harness. Measure the resistance from pin 6 of the engine harness ECM connector to pin A of the blowby pressure sensor harness connector. Measure the resistance from pin 25 of the engine harness ECM connector to pin C of the blowby pressure sensor harness connector. Measure the resistance from pin 17 of the engine harness ECM connector to pin B of the blowby pressure sensor harness connector. | Less than 10 ohms? | 2D-3 |
> | Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-201 in Section 19. Refer to Procedure 019-202 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 5A |  |
>
> #### STEP 2D-3. Check the resistance from signal pin to return pin in the ECM port.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the resistance from signal pin to return pin in the ECM port. Measure the resistance from pin 25 (signal) to pin 17 (return) in the ECM engine harness connector port. | More than 35k ohms? Replace the blowby pressure sensor. Refer to Procedure 019-011 in Section 19. | 5A |
> | Less than 35k ohms? Replace the ECM. Refer to Procedure 019-031 in Section 19. | 5A |  |
>
> ### STEP 3. Check the engine harness.
>
> #### STEP 3A. Inspect the engine harness and ECM connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? | 3B |
> | A damaged connection has been detected in the ECM engine connector or engine harness connector. Repair damaged pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins, use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |  |
>
> #### STEP 3B. Read the fault codes.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 729 active? | 3C |
> | Repair complete. | 4B |  |
>
> #### STEP 3C. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM. Disconnect the engine harness from the blowby pressure sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance from pin 25 of the engine harness ECM connector to pin C of the blowby pressure harness sensor connector. Measure the resistance from pin 6 of the engine harness ECM connector to pin A (+5-VDC supply) of the blowby pressure sensor harness connector. | Less than 10 ohms? | 3D |
> | Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-201 in Section 19. Refer to Procedure 019-202 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |
>
> #### STEP 3D. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the ECM. Disconnect the engine harness from the blowby pressure sensor. Disconnect the engine harness from the intake manifold air temperature sensor. Disconnect the engine harness from the ambient air pressure sensor. Disconnect the engine harness from the intake manifold pressure sensor. Disconnect the engine harness from the fuel temperature sensor. Disconnect the engine harness from the oil pressure sensor. Disconnect the engine harness from the coolant pressure sensor. Disconnect the engine harness from the coolant temperature sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin to pin. Measure the resistance from pin 25 of the engine harness ECM connector to all other pins in the connector. Measure the resistance from pin 17 of the engine harness ECM connector to all other pins in the connector. Measure the resistance from pin 6 of the engine harness ECM connector to all other pins in the connector. | More than 100k ohms? | 3E |
> | Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |
>
> #### STEP 3E. Check for a short circuit to engine block ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM. Disconnect the engine harness from the blowby pressure sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to engine block ground. Measure the resistance from pin 25 of the engine harness ECM connector to engine block ground. Measure the resistance from pin 17 of the engine harness ECM connector to engine block ground. Measure the resistance from pin 6 of the engine harness ECM connector to engine block ground. | More than 100k ohms? Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |
> | Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |
>
> ### STEP 4. Clear the fault codes.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to verify that Fault Code 729 is inactive. | Fault Code 729 inactive? | 4B |
> | Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
