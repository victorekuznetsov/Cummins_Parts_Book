---
aliases:
  - "Множественные коды неисправностей на жгуте двигателя"
type: "Процедура"
doc: "87-fcmulti"
title_en: "Multiple Fault Codes on the Engine Harness"
title_ru: "Множественные коды неисправностей на жгуте двигателя"
modified: "2003-10-23"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fcmulti.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fcmulti.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Multiple Fault Codes on the Engine Harness
**Множественные коды неисправностей на жгуте двигателя**

> [!abstract] Процедура · `87-fcmulti`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-10-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fcmulti.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fcmulti.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: многократно

### Множественные коды неисправностей на жгуте двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: Многократный PID(P): СПН: ФМИ: Лампа: СТО: | Несколько кодов неисправностей, генерируемых из-за общего источника питания или отказа обратного провода в ремне электропроводки двигателя. | Несколько кодов ошибок. |

![[19900397.png]]

### Описание цепи

Электронный модуль управления (ECM) поставляет все датчики давления двигателя на ремне электропроводки двигателя с +5 VDC от контакта 10. ECM имеет общую отдачу для всех датчиков давления двигателя и датчиков температуры при контакте 19. Неисправность на любом из этих проводов вызовет несколько кодов неисправностей.

### Расположение компонента

Проконсультируйтесь с диаграммами двигателя.

### Практические замечания

Ищите открытую цепь в общих проводах питания и возврата и коротких замыканиях от батареи или земли до проводов питания и возврата или дефектного источника питания ECM.

Неисправный датчик давления может вызвать несколько кодов неисправностей.

Неисправный датчик давления может привести к тому, что несколько активных кодов неисправностей будут неактивны после запуска двигателя.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения новой ЭКО необходимо изучить все другие активные коды неисправностей до замены ЭКО.**

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822758 - пробный щуп типа пробоотвода Deutsch/AMP/Metri-Pack**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Определите набор нескольких кодов ошибок. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Коды 122, 135, 144, 153, 221 и 719 неактивны. |
|  | **СТЭП 1В.** Прочитайте коды неисправностей. | Коды 122, 135, 221, 231 и 719 неактивны. |
|  | **СТЭП 1С.** Прочитайте коды неисправностей. | Коды 123, 141, 145, 154, 213, 222, 232 и 729 неактивны. |
|  | **СТЭП 1D.** Прочитайте коды неисправностей. | Коды 123, 141, 222, 232 и 729 не активны. |
| ШАГ 2. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 2A.** Проверить разъемы электропроводки и электропроводки двигателя. | Никаких поврежденных контактов |
|  | **ШАГ 2В.** Проверить наличие открытой цепи. | Менее 10 Ом |
|  | **STEP 2C.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
| ШАГ 3. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 3A.** Проверить разъемы электропроводки и электропроводки двигателя. | Никаких поврежденных контактов |
|  | **STEP 3B.** Проверьте наличие открытой цепи. | Более 100 тыс. ом |
| ШАГ 4. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 4A.** Проверить разъемы электропроводки и электропроводки двигателя. | Никаких поврежденных контактов |
|  | **STEP 4B.** Проверьте наличие открытой цепи. | Менее 10 Ом |
|  | **STEP 4C.** Проверьте короткое замыкание на землю. | Более 100 тыс. ом |
|  | **STEP 4D.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 4E.** Проверьте напряжение питания аккумулятора. | 17.0 до 35.0 VDC |
| ШАГ 5. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 5A.** Проверить разъемы электропроводки и электропроводки двигателя. | Никаких поврежденных контактов |
|  | **STEP 5B.** Проверьте наличие открытой цепи. | Менее 10 Ом |
|  | **STEP 5C** Проверьте короткое замыкание на землю. | Более 100 тыс. ом |
|  | **STEP 5D.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 5E.** Проверьте напряжение питания аккумулятора. | 17.0 до 35.0 VDC |
| ШАГ 6. | Сбросьте коды неисправностей. |  |
|  | **STEP 6A.** Отключить код ошибки. | Несколько кодов неактивных ошибок |
|  | **STEP 6B.** Очистить коды неактивных ошибок. | Все коды ошибок очищены |

### ШАГ 1. Определите набор нескольких кодов ошибок.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды ошибок с помощью INSITETM. | Коды 122, 135, 144, 153, 221 и 719 неактивны. | 1В |
| Код 122, 135, 144, 153, 221 или 719 уязвимостей активен | 2А |  |

#### ШАГ 1B. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды ошибок с помощью INSITETM. | Коды 122, 135, 221 и 719 неактивны | 1С |
| Код 122, 135, 221 или 719 уязвимостей активен | 3А |  |

#### ШАГ 1C. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды ошибок с помощью INSITETM. | Коды 123, 141, 145, 154, 222, 232 и 729 неактивны | 1D |
| Код 123, 141, 145, 154, 222, 232 или 729 уязвимостей активен | 4А |  |

#### ШАГ 1D. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды ошибок с помощью INSITETM. | Коды 123, 141, 222, 232 и 729 неактивны | 2А |
| Код 123, 141, 222, 232 или 729 уязвимостей активен | 5а |  |

### ШАГ 2. Проверьте жгут проводов двигателя.

#### ШАГ 2A. Проверьте разъемы ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Сгибаемые или сломанные штифты Отталкивающиеся или расширенные штифты Влажность в или на разъеме Пропавшие или поврежденные соединительные штифты Грязь или мусор в или на контактах разъема. | Никаких поврежденных контактов | 2В |
| Ремонт поврежденных контактов Смой грязь, мусор или влагу из контактов разъема. Ремонт или замена ремня электропроводки двигателя, или замена ECM, в зависимости от того, какие контакты повреждены. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. См. процедуру 019-204. Замените жгут проводов двигателя. См. процедуру 019-043. Заменить ECM. См. процедуру 019-031. Высушить разъем с помощью электрического контактного очистителя, номер детали 3824510. | 6А |  |

#### ШАГ 2B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отсоедините проводку двигателя в цепи с множественным кодом неисправности от датчика. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 19 в разъёме ремня электропроводки двигателя до контакта В на стороне ремня электропроводки двигателя всех датчиков с активными кодами неисправностей. | Менее 10 Ом | 2C |
| Ремонт или замена проводов двигателя ремень ремень проводов двигателя ремень. См. процедуру 019-202 или 019-204. Замените жгут проводов двигателя. См. процедуру 019-043. | 6А |  |

#### ШАГ 2C. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отсоедините проводку OEM от ECM. Отключите проводку двигателя в цепи с множественным кодом неисправности от всех датчиков. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 19 разъёма ремня электропроводки двигателя со всеми другими штифтами в разъеме и со всеми штифтами в разъеме OEM-проводов. | Более 100 тыс. ом | 6А |
| Ремонт или замена проводов двигателя ремень ремень проводов двигателя ремень. См. процедуру 019-204. Замените жгут проводов двигателя. См. процедуру 019-043. | 6А |  |

### ШАГ 3. Проверьте жгут проводов двигателя.

#### ШАГ 3A. Проверьте разъемы ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Сгибаемые или сломанные штифты Отталкивающиеся или расширенные штифты Влажность в или на разъеме Пропавшие или поврежденные соединительные штифты Грязь или мусор в или на контактах разъема. | Никаких поврежденных контактов | 3B |
| Ремонт поврежденных контактов Смой грязь, мусор или влагу из контактов разъема. Ремонт или замена ремня электропроводки двигателя, или замена ECM, в зависимости от того, какие контакты повреждены. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. 019-204. Замените жгут проводов двигателя. См. процедуру 019-043. Заменить ECM. См. процедуру 019-031. | 6А |  |

#### ШАГ 3B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отключите проводку двигателя в цепи с множественным кодом неисправности от всех датчиков. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 19 разъёма ремней электропроводки двигателя к контакту В стороны ремней электропроводки всех датчиков с активными кодами неисправностей. | Более 100 тыс. ом | 6А |
| Ремонт или замена проводов двигателя ремень ремень проводов двигателя ремень. См. процедуру 019-204. Замените жгут проводов двигателя. См. процедуру 019-043. | 6А |  |

### ШАГ 4. Проверьте жгут проводов двигателя.

#### ШАГ 4A. Проверьте разъемы ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Сгибаемые или сломанные штифты Отталкивающиеся или расширенные штифты Влажность в или на разъеме Пропавшие или поврежденные соединительные штифты Грязь или мусор в или на контактах разъема. | Никаких поврежденных контактов | 4B |
| Ремонт поврежденных контактов Смой грязь, мусор или влагу из контактов разъема. Ремонт или замена ремня электропроводки двигателя, или замена ECM, в зависимости от того, какие контакты повреждены. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. См. процедуру 019-204. Замените жгут проводов двигателя. См. процедуру 019-043. Заменить ECM. См. процедуру 019-031. | 6А |  |

#### ШАГ 4B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отключите проводку двигателя в цепи с множественным кодом неисправности от всех датчиков давления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 10 в разъёме ремня электропроводки двигателя до контакта А на стороне ремня электропроводки двигателя разъёма датчика давления. | Менее 10 Ом | 4C |
| Ремонт или замена проводов двигателя ремень ремень проводов двигателя ремень. См. процедуру 019-204. Замените жгут проводов двигателя. См. процедуру 019-043. | 6А |  |

#### ШАГ 4C. Проверьте короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отключите проводку двигателя в цепи с множественным кодом неисправности от всех датчиков. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 10 разъёма ремня электропроводки двигателя с заземлением блока двигателя. Измерьте сопротивление от контакта 23 разъёма ремня электропроводки двигателя с заземлением блока двигателя. Измерьте сопротивление от контакта 34 разъёма ремня электропроводки двигателя с заземлением блока двигателя. | Более 100 тыс. ом | 4D |
| Ремонт или замена проводов двигателя ремень ремень проводов двигателя ремень. См. процедуру 019-204. Замените жгут проводов двигателя. См. процедуру 019-043. | 6А |  |

#### ШАГ 4D. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отсоедините проводку OEM от ECM. Отключите проводку двигателя в цепи с множественным кодом неисправности от всех датчиков. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 10 разъёма ремня электропроводки двигателя ко всем другим штифтам в разъеме и ко всем штифтам в разъёме ремня электропроводки OEM. | Более 100 тыс. ом | 4Е |
| Ремонт или замена проводов двигателя ремень ремень проводов двигателя ремень. См. процедуру 019-204. Замените жгут проводов двигателя. См. процедуру 019-043. | 6А |  |

#### ШАГ 4E. Проверьте напряжение питания батареи.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отключите проводку двигателя в цепи с множественным кодом неисправности от всех датчиков. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта 50 разъёма проводов двигателя с заземлением блока двигателя. | 17.0 до 35.0 VDC | 5а |
| Правильная проблема с напряжением питания батареи. | 6А |  |

### ШАГ 5. Проверьте жгут проводов двигателя.

#### ШАГ 5A. Проверьте разъемы ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Сгибаемые или сломанные штифты Отталкивающиеся или расширенные штифты Влажность в или на разъеме Пропавшие или поврежденные соединительные штифты Грязь или мусор в или на контактах разъема. | Никаких поврежденных контактов | 5В |
| Ремонт поврежденных контактов Смой грязь, мусор или влагу из контактов разъема. Ремонт или замена ремня электропроводки двигателя, или замена ECM, в зависимости от того, какие контакты повреждены. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. См. процедуру 019-204. Замените жгут проводов двигателя. См. процедуру 019-043. Заменить ECM. См. процедуру 019-031. | 6А |  |

#### ШАГ 5B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отключите проводку двигателя в цепи с множественным кодом неисправности от всех датчиков давления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 10 в разъёме ремня электропроводки двигателя до контакта А на стороне ремня электропроводки двигателя всех датчиков давления с активными кодами неисправностей. | Менее 10 Ом | 5С |
| Ремонт или замена проводов двигателя ремень ремень проводов двигателя ремень. См. процедуру 019-204. Замените жгут проводов двигателя. См. процедуру 019-043. | 6А |  |

#### ШАГ 5C. Проверьте короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отключите проводку двигателя в цепи с множественным кодом неисправности от всех датчиков. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 10 разъёма ремня электропроводки двигателя с заземлением блока двигателя. Измерьте сопротивление от контакта 23 разъёма ремня электропроводки двигателя с заземлением блока двигателя. Измерьте сопротивление от контакта 34 разъёма ремня электропроводки двигателя с заземлением блока двигателя. | Более 100 тыс. ом | 5D |
| Ремонт или замена проводов двигателя ремень ремень проводов двигателя ремень. См. процедуру 019-204. Замените жгут проводов двигателя. См. процедуру 019-043. | 6А |  |

#### ШАГ 5D. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отсоедините проводку OEM от ECM. Отключите проводку двигателя в цепи с множественным кодом неисправности от всех датчиков. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 10 разъёма ремня электропроводки двигателя ко всем другим штифтам в разъеме и ко всем штифтам в разъёме ремня электропроводки OEM. | Более 100 тыс. ом | 5Е |
| Ремонт или замена проводов двигателя ремень ремень проводов двигателя ремень. См. процедуру 019-204. Замените жгут проводов двигателя. См. процедуру 019-043. | 6А |  |

#### ШАГ 5E. Проверьте напряжение питания батареи.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отключите проводку двигателя в цепи с множественным кодом неисправности от всех датчиков. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта 50 разъёма проводов двигателя с заземлением блока двигателя. | 17.0 до 35.0 VDC | 6А |
| Правильная проблема с напряжением питания батареи. | 6А |  |

### ШАГ 6. Сбросьте коды неисправностей.

#### ШАГ 6A. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Убедитесь, что несколько кодов неактивны. | Несколько кодов неактивных ошибок | 6B |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 6B. Сбросьте неактивные коды неисправностей.

| **Условия:** Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Стирать неактивные коды неисправностей с помощью INSITETM. | Все коды ошибок очищены | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: Multiple
>
> ### Multiple Fault Codes on the Engine Harness
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: Multiple PID(P): SPN: FMI: Lamp: SRT: | Multiple fault codes generated due to a common supply or a return wire failure in the engine harness. | Multiple fault codes. |
>
> ### Circuit Description
>
> The electronic control module (ECM) supplies all of the engine pressure sensors on the engine harness with +5 VDC from pin 10. The ECM has common returns for all of the engine pressure sensors and temperature sensors on pin 19. A failure on either of these wires will cause multiple fault codes.
>
> ### Component Location
>
> Consult the engine diagrams.
>
> ### Shoptalk
>
> Look for an open circuit in the common supply and return wires and short circuits from battery or ground to the supply and return wires or defective ECM power supply.
>
> A failed pressure sensor can cause multiple fault codes.
>
> A failed pressure sensor can cause multiple active fault codes to go inactive once the engine has been started.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.**
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Determine the set of multiple fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Codes 122, 135, 144, 153, 221, and 719 are not active |
> |  | **STEP 1B.** Read the fault codes. | Fault Codes 122, 135, 221, 231, and 719 are not active |
> |  | **STEP 1C.** Read the fault codes. | Fault Codes 123, 141, 145, 154, 213, 222, 232, and 729 are not active |
> |  | **STEP 1D.** Read the fault codes. | Fault Codes 123, 141, 222, 232, and 729 are not active |
> | STEP 2. | Check the engine harness. |  |
> |  | **STEP 2A.** Inspect the ECM and engine harness connectors. | No damaged pins |
> |  | **STEP 2B.** Check for an open circuit. | Less than 10 ohms |
> |  | **STEP 2C.** Check for a short circuit from pin to pin. | More than 100k ohms |
> | STEP 3. | Check the engine harness. |  |
> |  | **STEP 3A.** Inspect the ECM and engine harness connectors. | No damaged pins |
> |  | **STEP 3B.** Check for an open circuit. | More than 100k ohms |
> | STEP 4. | Check the engine harness. |  |
> |  | **STEP 4A.** Inspect the ECM and engine harness connectors. | No damaged pins |
> |  | **STEP 4B.** Check for an open circuit. | Less than 10 ohms |
> |  | **STEP 4C.** Check for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 4D.** Check for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 4E.** Check the battery supply voltage. | 17.0 to 35.0 VDC |
> | STEP 5. | Check the engine harness. |  |
> |  | **STEP 5A.** Inspect the ECM and engine harness connectors. | No damaged pins |
> |  | **STEP 5B.** Check for an open circuit. | Less than 10 ohms |
> |  | **STEP 5C.** Check for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 5D.** Check for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 5E.** Check the battery supply voltage. | 17.0 to 35.0 VDC |
> | STEP 6. | Clear the fault codes. |  |
> |  | **STEP 6A.** Disable the fault code. | Multiple fault codes inactive |
> |  | **STEP 6B.** Clear the inactive fault codes. | All fault codes cleared |
>
> ### STEP 1. Determine the set of multiple fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes using INSITE™. | Fault Codes 122, 135, 144, 153, 221, and 719 are not active | 1B |
> | Fault Code 122, 135, 144, 153, 221, or 719 is active | 2A |  |
>
> #### STEP 1B. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes using INSITE™. | Fault Codes 122, 135, 221, and 719 not active | 1C |
> | Fault Code 122, 135, 221, or 719 is active | 3A |  |
>
> #### STEP 1C. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes using INSITE™. | Fault Codes 123, 141, 145, 154, 222, 232, and 729 not active | 1D |
> | Fault Code 123, 141, 145, 154, 222, 232, or 729 is active | 4A |  |
>
> #### STEP 1D. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes using INSITE™. | Fault Codes 123, 141, 222, 232, and 729 not active | 2A |
> | Fault Code 123, 141, 222, 232, or 729 is active | 5A |  |
>
> ### STEP 2. Check the engine harness.
>
> #### STEP 2A. Inspect the ECM and engine harness connectors.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 2B |
> | Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. Replace the ECM. Refer to Procedure 019-031. Dry the connector by using an electrical contact cleaner, Part Number 3824510. | 6A |  |
>
> #### STEP 2B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from the sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 19 in the engine harness connector to pin B on the engine wiring harness side of all sensors with active fault codes. | Less than 10 ohms | 2C |
> | Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-202 or 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |
>
> #### STEP 2C. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the OEM harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 19 of the engine harness connector to all other pins in the connector, and to all pins in the OEM harness connector. | More than 100k ohms | 6A |
> | Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |
>
> ### STEP 3. Check the engine harness.
>
> #### STEP 3A. Inspect the ECM and engine harness connectors.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 3B |
> | Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. 019-204. Replace the engine harness. Refer to Procedure 019-043. Replace the ECM. Refer to Procedure 019-031. | 6A |  |
>
> #### STEP 3B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 19 of the engine harness connector to pin B of the harness side of all sensors with active fault codes. | More than 100k ohms | 6A |
> | Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |
>
> ### STEP 4. Check the engine harness.
>
> #### STEP 4A. Inspect the ECM and engine harness connectors.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 4B |
> | Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. Replace the ECM. Refer to Procedure 019-031. | 6A |  |
>
> #### STEP 4B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the pressure sensors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 10 in the engine harness connector to pin A on the engine wiring harness side of a pressure sensor connector. | Less than 10 ohms | 4C |
> | Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |
>
> #### STEP 4C. Check for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 10 of the engine harness connector to the engine block ground. Measure the resistance from pin 23 of the engine harness connector to the engine block ground. Measure the resistance from pin 34 of the engine harness connector to the engine block ground. | More than 100k ohms | 4D |
> | Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |
>
> #### STEP 4D. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the OEM harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 10 of the engine harness connector to all other pins in the connector, and to all pins in the OEM harness connector. | More than 100k ohms | 4E |
> | Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |
>
> #### STEP 4E. Check the battery supply voltage.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin 50 of the engine harness connector to engine block ground. | 17.0 to 35.0 VDC | 5A |
> | Correct battery supply voltage problem. | 6A |  |
>
> ### STEP 5. Check the engine harness.
>
> #### STEP 5A. Inspect the ECM and engine harness connectors.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 5B |
> | Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. Replace the ECM. Refer to Procedure 019-031. | 6A |  |
>
> #### STEP 5B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the pressure sensors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 10 in the engine harness connector to pin A on the engine wiring harness side of all pressure sensors with active fault codes. | Less than 10 ohms | 5C |
> | Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |
>
> #### STEP 5C. Check for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 10 of the engine harness connector to the engine block ground. Measure the resistance from pin 23 of the engine harness connector to the engine block ground. Measure the resistance from pin 34 of the engine harness connector to the engine block ground. | More than 100k ohms | 5D |
> | Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |
>
> #### STEP 5D. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the OEM harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 10 of the engine harness connector to all other pins in the connector, and to all pins in the OEM harness connector. | More than 100k ohms | 5E |
> | Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |
>
> #### STEP 5E. Check the battery supply voltage.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin 50 of the engine harness connector to engine block ground. | 17.0 to 35.0 VDC | 6A |
> | Correct battery supply voltage problem. | 6A |  |
>
> ### STEP 6. Clear the fault codes.
>
> #### STEP 6A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Start the engine and let it idle for 1 minute. Verify that multiple fault codes are inactive. | Multiple fault codes inactive | 6B |
> | Return to the troubleshooting steps or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
>
> #### STEP 6B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Erase the inactive fault codes using INSITE™. | All fault codes cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
