---
aliases:
  - "Код 422 — цепь датчика уровня охлаждающей жидкости"
type: "Процедура"
doc: "82-t05-422"
title_en: "FAULT CODE 422 - Coolant Level Sensor Circuit"
title_ru: "Код 422 — цепь датчика уровня охлаждающей жидкости"
modified: "2019-01-22"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-422.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-422.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# FAULT CODE 422 - Coolant Level Sensor Circuit
**Код 422 — цепь датчика уровня охлаждающей жидкости**

> [!abstract] Процедура · `82-t05-422`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-01-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-422.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-422.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!danger] ОПАСНО
> Не снимайте пробку радиатора с горячего двигателя. Подождите, пока температура охлаждающей жидкости не будет ниже 50°C \[122°F\], прежде чем снимать крышку радиатора. Струя горячей охлаждающей жидкости или пар могут привести к травме.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 — пробный щуп типа штепсельной заглушки DeutschTM/AMPTM/Metri-PackTM, номер детали 3822917 — пробный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM, а номер детали 3823995 — штыревой пробный щуп Weather-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте наличие нескольких кодов неисправностей и наличие датчика уровня охлаждающей жидкости. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Код 187 неисправности активен или неактивен, включив более одного номера за последние 25 часов работы двигателя? |
|  | **STEP 1B.** Проверьте, имеет ли транспортное средство датчик уровня охлаждающей жидкости. | Датчик уровня охлаждения? |
|  | **STEP 1B-1.** Проверьте, используется ли в приложении датчик уровня охлаждающей жидкости или установлена шорт-розетка в соединении с проводкой датчика уровня охлаждающей жидкости. | Шортинг вилка установлена? |
| ШАГ 2. | Проверьте датчик уровня охлаждающей жидкости. |  |
|  | **STEP 2A.** Осмотрите жгут электропроводки двигателя и разъемы датчиков уровня охлаждающей жидкости. | Грязные или поврежденные контакты? |
|  | **STEP 2B** Проверить упряжку электропроводки двигателя и разъемы модуля управления двигателем (ECM). | Грязные или поврежденные контакты? |
|  | **STEP 2C.** Проверьте наличие открытой цепи в цепи датчика уровня охлаждающей жидкости. | Менее 10 Ом? |
|  | **STEP 2C-1.** Проверить оригинальную проводку производителя оборудования (OEM) с помощью датчика и 31 контактного штифта OEM-разъема. | Грязные или поврежденные контакты? |
|  | **STEP 2C-2.** Проверьте наличие открытой цепи в ремне электропроводки двигателя. | Менее 10 Ом? |
|  | **STEP 2C-3.** Проверьте наличие открытой цепи в электропроводке OEM. | Менее 10 Ом? |
| ШАГ 3. | Проверьте короткое замыкание на землю в проводах SIGNAL. |  |
|  | **STEP 3A.** Проверьте короткое замыкание на землю в проводах SIGNAL датчика уровня охлаждающей жидкости. | Больше 100 тысяч ом? |
|  | **STEP 3A-1.** Проверьте короткое замыкание в ремне электропроводки двигателя. | Больше 100 тысяч ом? |
|  | **ШАГ 3А-2.** Проверьте короткое замыкание в электропроводке OEM. | Больше 100 тысяч ом? |
| ШАГ 4. | Проверьте короткое замыкание между проводами SIGNAL и любыми другими проводами в ремне электропроводки двигателя или OEM-проводах. |  |
|  | **STEP 4A.** Проверьте короткое замыкание между проводами SIGNAL и любыми другими проводами в ремне электропроводки двигателя или ремне электропроводки OEM. | Больше 100 тысяч ом? |
|  | **STEP 4A-1.** Проверьте короткое замыкание в ремне электропроводки двигателя. | Больше 100 тысяч ом? |
|  | **STEP 4A-2.** Проверьте короткое замыкание в электропроводке OEM. | Больше 100 тысяч ом? |
| ШАГ 5. | Проверьте короткое замыкание, чтобы заземлиться в проводе SUPPLY. |  |
|  | **ШАГ 5А.** Проверьте короткое замыкание на землю в проводе SUPPLY. | Больше 100 тысяч ом? |
|  | **STEP 5A-1.** Проверьте короткое замыкание в ремне электропроводки двигателя. | Больше 100 тысяч ом? |
|  | **STEP 5A-2.** Проверьте короткое замыкание в электропроводке OEM. | Больше 100 тысяч ом? |
| ШАГ 6. | Сбросьте коды неисправностей. |  |
|  | **STEP 6A.** Отключить код ошибки. | Код 422 неактивен? |
|  | **STEP 6B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте наличие нескольких кодов неисправностей и наличие датчика уровня охлаждающей жидкости.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Запуск двигателя и холостость в течение одной минуты. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 187 неисправности активен или неактивен, включив более одного номера за последние 25 часов работы двигателя? *Да | Код ошибки 187, дерево устранения неполадок |
| Код 187 неисправности активен или неактивен, включив более одного номера за последние 25 часов работы двигателя? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте, есть ли у автомобиля датчик уровня охлаждающей жидкости.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, есть ли у автомобиля датчик уровня охлаждающей жидкости. | Датчик уровня охлаждения? *Да | 2А |
| Датчик уровня охлаждения? **НЕТ** | 1В-1-1 |  |

#### ШАГ 1B-1. Проверьте, используется ли в приложении датчик уровня охлаждающей жидкости или установлена шорт-розетка в соединении с датчиком уровня охлаждающей жидкости.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, установлена ли шортинговая вилка в подключении датчика уровня охлаждающей жидкости. Примечание: Проверьте OEM-проводку от шортинга до подключения жгута к двигателю для проблем. Ссылка на OEM и схемы проводов жгута двигателя. | Если в приложении используется шортинг-плаг, присутствует ли он и правильно ли установлен? *Да | 2А |
| Если в приложении используется шортинг-плаг, присутствует ли он и правильно ли установлен? **NORepair:** Установите шортинг. | 6А |  |

### ШАГ 2. Проверьте датчик уровня охлаждающей жидкости.

#### ШАГ 2A. Проверьте проводку и разъёмы датчика уровня охлаждающей жидкости.

| **Условия:** Замок зажигания включить Отключить разъем проводов датчика от ECM Отключить проводку OEM от датчика уровня охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы разъёма проводов и датчика уровня охлаждающей жидкости на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]]. | Грязные или поврежденные контакты? **Ремонт: **Ремонт поврежденных контактов. Ремонт или замена OEM проводов жгута, или заменить датчик уровня охлаждающей жидкости, в зависимости от того, что имеет поврежденные контакты. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт проводной упряжки OEM. См. процедуру 019-204 в разделе 19. См. процедуру 019-208 в разделе 19. Замените проводку OEM. См. процедуру 019-071 в разделе 19. Замените датчик уровня охлаждающей жидкости. См. процедуру 019-017 в разделе 19. | 6А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте жгут электропроводки двигателя и разъемы ECM.

| **Условия:** Замок зажигания отключите от разъема электропроводки датчика от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите жгут электропроводки двигателя и контакты разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]]. | Грязные или поврежденные контакты? **Ремонт: **Ремонт поврежденных контактов. Ремонт или замена ремня электропроводки двигателя, или замена ECM, в зависимости от того, какие контакты повреждены. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19 Таблицы ассоциированных процедур. Заменить ECM. См. процедуру 019-031 в разделе 19. | 6А |
| Грязные или поврежденные контакты? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте наличие открытой цепи в цепи датчика уровня охлаждающей жидкости.

| **Условия:** Замок зажигания включить Отключить разъем проводов датчика от ECM Отключить проводку OEM от датчика уровня охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие открытой цепи в цепи датчика уровня охлаждающей жидкости. Измерьте сопротивление от контакта 25 в разъёме жгута проводов датчика к контакту C (или 3) на стороне ремня электропроводки разъёма датчика уровня охлаждающей жидкости. Измерьте сопротивление контакта 23 в разъёме проводов датчика для контакта с B (или 2) на стороне проводов жгута проводов разъёма датчика уровня охлаждающей жидкости. Измерьте сопротивление от контакта 24 в разъёме проводов датчика для контакта D (или 4) на стороне проводов жгута проводов разъёма датчика уровня охлаждающей жидкости. Измерьте сопротивление от контакта 22 в разъёме жгута датчика для контакта с A (или 1) на стороне жгута проводов разъёма датчика уровня охлаждающей жидкости. | Менее 10 Ом? *Да | 3А |
| Менее 10 Ом? **NORepair:** Ремонт или замена ремня электропроводки двигателя или ремня электропроводки OEM. Ремонт ремня электропроводки двигателя. См. процедуру 019-208 в разделе 19. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19 Таблицы ассоциированных процедур. Замените проводку OEM. См. сервисное руководство изготовителя машины. | 2С-1 |  |

#### ШАГ 2C-1. Осмотрите датчик подключения OEM-проводов и контакты 31-контактного OEM-разъема.

| **Условия: **Замок зажигания поворота Отключите разъем проводов датчика от ECM Отключите проводку OEM от датчика уровня охлаждающей жидкости Отключите проводку двигателя от ремня проводов OEM на разъеме OEM 31 пин. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите датчик подключения OEM-проводов и 31 контакт OEM-разъема на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]]. | Грязные или поврежденные контакты? **Ремонт: **Ремонт поврежденных контактов. Ремонт или замена ремня электропроводки двигателя или ремня электропроводки OEM, в зависимости от того, какие контакты повреждены. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. См. процедуру 019-208 в разделе 19. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19 таблиц ассоциированных процедур. Ремонт проводной упряжки OEM. См. процедуру 019-204 в разделе 19. См. процедуру 019-208 в разделе 19. Замените проводку OEM. См. процедуру 019-071 в разделе 19. | 6А |
| Грязные или поврежденные контакты? **НЕТ** | 2С-2 |  |

#### ШАГ 2C-2. Проверьте наличие открытой цепи в ремне электропроводки двигателя.

| **Условия: **Замок зажигания поворота Отключите разъем проводов датчика от ECM Отключите проводку OEM от датчика уровня охлаждающей жидкости Отключите проводку двигателя от ремня проводов OEM на разъеме OEM 31 пин. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие открытой цепи в ремне электропроводки двигателя. Измерьте сопротивление от контакта 22 в разъёме датчика проводов жгута проводов к контакту 6 на стороне ремня электропроводки двигателя 31-контактного OEM-разъема. Измерьте сопротивление от контакта 23 в разъёме датчика проводов жгута проводов к контакту 19 на стороне ремня электропроводки двигателя 31-контактного OEM-разъема. Измерьте сопротивление от контакта 24 в разъёме датчика проводов жгута проводов к контакту 5 на стороне ремня электропроводки двигателя 31-контактного OEM-разъема. Измерьте сопротивление от контакта 25 в разъёме датчика проводов жгута проводов к контакту 7 на стороне ремня электропроводки двигателя 31-контактного OEM-разъема. | Менее 10 Ом? *Да | 2С-3 |
| Менее 10 Ом? **NORepair:** Ремонт или замена ремня электропроводки двигателя или ремня электропроводки OEM. Ремонт ремня электропроводки двигателя. 019-208 в разделе 19. 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19 Таблицы ассоциированных процедур. Замените проводку OEM. См. процедуру 019-071 в разделе 19. | 6А |  |

#### ШАГ 2C-3. Проверьте наличие открытой цепи в OEM-проводах.

| **Условия: **Замок зажигания поворота Отключите электропроводку двигателя от электропроводки OEM на 31-контактном OEM-разъеме Отключите электропроводку OEM-разъема на четырехстороннем разъеме Weather-PackTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие открытой цепи в OEM-проводах. Измерьте сопротивление от контакта 6 на стороне OEM проводов жгута проводов 31 пин OEM разъема для контакта A (или 1) на стороне OEM проводов жгута проводов 4 пин разъема. Измерить сопротивление от контакта 19 на стороне OEM проводов жгута проводов 31 пин OEM разъема для контакта B (или 2) на стороне OEM проводов жгута проводов 4 пин разъема. Измерьте сопротивление от контакта 7 на стороне OEM проводов жгута проводов 31 пин OEM разъема для контакта C (или 3) на стороне OEM проводов жгута проводов 4 пин разъема. Измерьте сопротивление от контакта 5 на стороне OEM-проводов OEM-разъема 31-контактного разъема OEM для контакта D (или 4) на стороне OEM-проводов 4-контактного разъема. | Менее 10 Ом? *Да | 3А |
| Менее 10 Ом? **NORepair:** Ремонтировать или заменить проводку OEM. Ремонт проводной упряжки OEM. См. процедуру 019-204 в разделе 19. См. процедуру 019-208 в разделе 19. Замените проводку OEM. См. процедуру 019-071 в разделе 19. | 6А |  |

### ШАГ 3. Проверьте короткое замыкание на землю в проводах SIGNAL.

#### ШАГ 3A. Проверьте короткое замыкание для заземления в проводах датчика уровня охлаждающей жидкости SIGNAL.

| **Условия:** Замок зажигания включить Отключить разъем проводов датчика от ECM Отключить проводку OEM от датчика уровня охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание, чтобы заземлиться в сигнальных проводах датчика уровня охлаждающей жидкости. Измерьте сопротивление от контакта 22 датчика проводов ремня разъема к блоку двигателя земли. Измерьте сопротивление от контакта 24 датчика проводов ремня разъема к блоку двигателя земли. Измерьте сопротивление от контакта 25 датчика проводов ремня разъема к блоку двигателя земли. | Больше 100 тысяч ом? *Да | 4А |
| Больше 100 тысяч ом? **NORepair: **Не соответствует спецификациям. | 3А-1-1 |  |

#### ШАГ 3A-1. Проверьте короткое замыкание, чтобы заземлиться в ремне электропроводки двигателя.

| **Условия: **Замок зажигания поворота Отключите разъем проводов датчика от ECM Отключите проводку OEM от датчика уровня охлаждающей жидкости Отключите проводку двигателя от ремня проводов OEM на разъеме OEM 31 пин. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание, чтобы заземлиться в ремне электропроводки двигателя. Измерьте сопротивление от контакта 22 датчика проводов ремня разъема к блоку двигателя земли. Измерьте сопротивление от контакта 24 датчика проводов ремня разъема к блоку двигателя земли. | Больше 100 тысяч ом? *Да | 3А-2 |
| Больше 100 тысяч ом? **NORepair:** Ремонтировать или заменить электропроводку двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19 таблицы ассоциированных процедур. | 6А |  |

#### ШАГ 3A-2. Проверьте короткое замыкание, чтобы приземлиться в OEM-проводах.

| **Условия: **Замок зажигания поворота Отключите проводку OEM от датчика уровня охлаждающей жидкости Отключите проводку двигателя от электропроводки OEM на 31-контактном OEM-разъеме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на землю в OEM-проводах. Измерьте сопротивление от контакта А (или 1) на стороне проводов OEM-проводов 4-контактного разъема к заземлению блока двигателя. Измерьте сопротивление от контакта C (или 3) на стороне проводов OEM-проводов 4-контактного разъема к заземлению блока двигателя. Измерьте сопротивление от контакта D (или 4) на стороне проводов OEM-проводов 4-контактного разъема к заземлению блока двигателя. | Больше 100 тысяч ом? *Да | 4А |
| Больше 100 тысяч ом? **NORepair:** Ремонтировать или заменить проводку OEM. Ремонт проводной упряжки OEM. См. процедуру 019-204 в разделе 19. Замените проводку OEM. См. процедуру 019-071 в разделе 19. | 6А |  |

### ШАГ 4. Проверьте короткое замыкание между проводами SIGNAL и любыми другими проводами в ремне электропроводки двигателя или OEM-проводах.

#### ШАГ 4A. Проверьте короткое замыкание между проводами SIGNAL и любыми другими проводами в ремне электропроводки двигателя или OEM-проводах.

| **Условия:** Замок зажигания включить Отключить разъём проводов датчика от разъема ECM Отключить разъем OEM от датчика уровня охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание между проводами SIGNAL и любыми другими проводами в упряжке OEM-проводов или упряжке для проводов двигателя. Измерьте сопротивление от контакта 22 разъёма проводов датчика со всеми другими штифтами в разъеме. Измерьте сопротивление от контакта 24 разъёма проводов датчика со всеми другими штифтами в разъеме. | Больше 100 тысяч ом? Заменить датчик уровня охлаждающей жидкости. См. процедуру 019-017 в таблице ассоциированных процедур. | 4А-1-1 |
| Больше 100 тысяч ом? **НЕТ** | 6А |  |

#### ШАГ 4A-1. Проверьте короткое замыкание в ремне электропроводки двигателя.

| **Условия: **Замок зажигания поворота Отключите разъем электропроводки датчика от разъема ECM Отключите разъем OEM от датчика уровня охлаждающей жидкости Отключите ремень электропроводки двигателя от ремня электропроводки OEM на разъеме OEM 31 pin. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание в ремне электропроводки двигателя. Измерьте сопротивление от контакта 22 разъёма проводов датчика к контактам 24, 23 и 25 разъёма. Измерьте сопротивление от контакта 24 разъёма проводов датчика к контактам 22, 23 и 25 разъёма. | Больше 100 тысяч ом? *Да | 4А-2 |
| Больше 100 тысяч ом? **NORepair:** Ремонтировать или заменить электропроводку двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 6А |  |

#### ШАГ 4A-2. Проверьте короткое замыкание в OEM-проводах.

| **Условия: **Замок зажигания поворота Отключите проводку OEM от датчика уровня охлаждающей жидкости Отключите проводку OEM на стороне OEM разъема OEM с 31 выводом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание в OEM-проводах. Измерьте сопротивление от контакта А (или 1) в разъёме проводов OEM-системы к штифтам B (или 2), C (или 3) и D (или 4). Измерьте сопротивление от контакта D (или 4) в разъёме проводов OEM-системы к штифтам A (или 1), B (или 2) и C (или 3). | Больше 100 тысяч ом? *Да | 5а |
| Больше 100 тысяч ом? **NORepair:** Ремонтировать или заменить проводку OEM. Ремонт проводной упряжки OEM. См. процедуру 019-204 в разделе 19. Замените проводку OEM. См. процедуру 019-071 в разделе 19. | 6А |  |

### ШАГ 5. Проверьте короткое замыкание, чтобы заземлиться в проводе SUPPLY.

#### ШАГ 5A. Проверьте короткое замыкание, чтобы заземлиться в проводе SUPPLY.

| **Условия:** Замок зажигания включить Отключить разъем проводов датчика от ECM Отключить проводку OEM от датчика уровня охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание, чтобы заземлиться в проводе SUPPLY. Измерьте сопротивление от контакта 25 в разъёме соединительной проводов датчика к блоку двигателя. | Больше 100 тысяч ом? *Да | 5А-1-1 |
| Больше 100 тысяч ом? **NORepair:** Ремонтировать или заменить электропроводку двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 6А |  |

#### ШАГ 5A-1. Проверьте короткое замыкание в проводах датчика.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика проводов ремня от ECM. Отсоедините проводку OEM от датчика уровня охлаждающей жидкости. Отсоедините датчик проводов жгута от OEM проводов жгута на 31 пин OEM разъем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание в проводах датчика. Измерьте сопротивление от контакта 25 разъёма проводов датчика к контакту 22 разъёма. Измерьте сопротивление от контакта 25 разъёма проводов датчика к контакту 23 разъёма. Измерьте сопротивление от контакта 25 разъёма проводов датчика к контакту 24 разъёма. | Больше 100 тысяч ом? *Да | 5А-2 |
| Больше 100 тысяч ом? **NORepair:** Ремонтировать или заменить двигатель. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 6А |  |

#### ШАГ 5A-2. Проверьте короткое замыкание в OEM-проводах.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика проводов ремня от ECM. Отсоедините проводку OEM от датчика уровня охлаждающей жидкости. Отсоедините датчик проводов жгута от OEM проводов жгута на 31 пин OEM разъем. Отключите проводку OEM-производителя на четырехстороннем разъеме Weather-PackTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание в OEM-проводах. Измерьте сопротивление от контакта C (или 3) в разъёме OEM-проводов с штифтами A (или 1), B (или 2) и D (или 4). | Больше 100 тысяч ом? *Да | 6А |
| Больше 100 тысяч ом? **NORepair:** Ремонтировать или заменить проводку OEM. Ремонт проводной упряжки OEM. См. процедуру 019-204 в разделе 19. Замените проводку OEM. См. процедуру 019-071 в разделе 19. | 6А |  |

### ШАГ 6. Сбросьте коды неисправностей.

#### ШАГ 6A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Запуск двигателя и холостость в течение одной минуты. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода 422. | Код 422 неактивен? *Да | 6B |
| Код 422 неактивен? **Секретарь:**Проверить, что все шаги были выполнены. Если все шаги выполнены, то следуйте процессу технической эскалации. | Эскалация или призыв к помощи. |  |

#### ШАГ 6B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair: **Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **WARNING · Опасно**
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[122°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, and Part Number 3823995 - male Weather-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check for multiple fault codes and the presence of the coolant level sensor. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Code 187 active or inactive with more than one count logged in the last 25 engine hours? |
> |  | **STEP 1B.** Check if vehicle has a coolant level sensor. | Coolant level sensor present? |
> |  | **STEP 1B-1.** Check if a coolant level sensor is used in the application, or if a shorting plug is installed in the coolant level sensor harness connection. | Shorting plug installed? |
> | STEP 2. | Check the coolant level sensor. |  |
> |  | **STEP 2A.** Inspect the engine harness and coolant level sensor connectors. | Dirty or damaged pins? |
> |  | **STEP 2B.** Inspect the engine harness and the engine control module (ECM) connectors. | Dirty or damaged pins? |
> |  | **STEP 2C.** Check for an open circuit in the coolant level sensor circuit. | Less than 10 ohms? |
> |  | **STEP 2C-1.** Inspect the original equipment manufacturer (OEM) harness sensor connector and 31 pin OEM connector pins. | Dirty or damaged pins? |
> |  | **STEP 2C-2.** Check for an open circuit in the engine harness. | Less than 10 ohms? |
> |  | **STEP 2C-3.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
> | STEP 3. | Check for a short circuit to ground in the SIGNAL wires. |  |
> |  | **STEP 3A.** Check for a short circuit to ground in the coolant level sensor SIGNAL wires. | Greater than 100k ohms? |
> |  | **STEP 3A-1.** Check for a short circuit to ground in the engine harness. | Greater than 100k ohms? |
> |  | **STEP 3A-2.** Check for a short circuit to ground in the OEM harness. | Greater than 100k ohms? |
> | STEP 4. | Check for a short circuit between the SIGNAL wires and any other wires in the engine harness or OEM harness. |  |
> |  | **STEP 4A.** Check for a short circuit between the SIGNAL wires and any other wires in the engine harness or OEM harness. | Greater than 100k ohms? |
> |  | **STEP 4A-1.** Check for a short circuit in the engine harness. | Greater than 100k ohms? |
> |  | **STEP 4A-2.** Check for a short circuit in the OEM harness. | Greater than 100k ohms? |
> | STEP 5. | Check for a short circuit to ground in the SUPPLY wire. |  |
> |  | **STEP 5A.** Check for a short circuit to ground in the SUPPLY wire. | Greater than 100k ohms? |
> |  | **STEP 5A-1.** Check for a short circuit in the engine harness. | Greater than 100k ohms? |
> |  | **STEP 5A-2.** Check for a short circuit in the OEM harness. | Greater than 100k ohms? |
> | STEP 6. | Clear the fault codes. |  |
> |  | **STEP 6A.** Disable the fault code. | Fault Code 422 inactive? |
> |  | **STEP 6B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check for multiple fault codes and the presence of the coolant level sensor.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Start the engine and idle for one minute. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 187 active or inactive with more than one count logged in the last 25 engine hours? **YES** | Go to Fault Code 187 troubleshooting tree |
> | Fault Code 187 active or inactive with more than one count logged in the last 25 engine hours? **NO** | 1B |  |
>
> #### STEP 1B. Check if vehicle has a coolant level sensor.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check to see if the vehicle has a coolant level sensor. | Coolant level sensor present? **YES** | 2A |
> | Coolant level sensor present? **NO** | 1B-1 |  |
>
> #### STEP 1B-1. Check if a coolant level sensor is used in the application, or if a shorting plug is installed in the coolant level sensor harness connection.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check if a shorting plug is installed in the coolant level sensor harness connection. Note: Check the OEM wiring from the shorting plug to the engine harness connection for problems. Reference the OEM and the engine harness wiring diagrams. | If a Shorting plug is used in the application, is it present and properly installed? **YES** | 2A |
> | If a Shorting plug is used in the application, is it present and properly installed? **NORepair:** Install the shorting plug. | 6A |  |
>
> ### STEP 2. Check the coolant level sensor.
>
> #### STEP 2A. Inspect the harness and the coolant level sensor connectors.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the harness and the coolant level sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Repair or replace the OEM harness, or replace the coolant level sensor, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Refer to Procedure 019-208 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. Replace the coolant level sensor. Refer to Procedure 019-017 in Section 19. | 6A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Inspect the engine harness and the ECM connectors.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and the ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19 in the Associated Procedures Table. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 6A |
> | Dirty or damaged pins? **NO** | 2C |  |
>
> #### STEP 2C. Check for an open circuit in the coolant level sensor circuit.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit in the coolant level sensor circuit. Measure the resistance from pin 25 in the sensor harness connector to pin C (or 3) on the harness side of the coolant level sensor connector. Measure the resistance from pin 23 in the sensor harness connector to pin B (or 2) on the harness side of the coolant level sensor connector. Measure the resistance from pin 24 in the sensor harness connector to pin D (or 4) on the harness side of the coolant level sensor connector. Measure the resistance from pin 22 in the sensor harness connector to pin A (or 1) on the harness side of the coolant level sensor connector. | Less than 10 ohms? **YES** | 3A |
> | Less than 10 ohms? **NORepair:** Repair or replace the engine harness or OEM harness. Repair the engine harness. Refer to Procedure 019-208 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19 in the Associated Procedures Table. Replace the OEM harness. Refer to the OEM service manual. | 2C-1 |  |
>
> #### STEP 2C-1. Inspect the OEM harness sensor connector and 31 pin OEM connector pins.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor Disconnect the engine harness from the OEM harness at the 31 pin OEM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness sensor connector and 31 pin OEM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Repair or replace the engine harness or the OEM harness, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-208 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19 in the Associated Procedure Tables. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Refer to Procedure 019-208 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 6A |
> | Dirty or damaged pins? **NO** | 2C-2 |  |
>
> #### STEP 2C-2. Check for an open circuit in the engine harness.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor Disconnect the engine harness from the OEM harness at the 31 pin OEM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit in the engine harness. Measure the resistance from pin 22 in the sensor harness connector to pin 6 on the engine harness side of the 31 pin OEM connector. Measure the resistance from pin 23 in the sensor harness connector to pin 19 on the engine harness side of the 31 pin OEM connector. Measure the resistance from pin 24 in the sensor harness connector to pin 5 on the engine harness side of the 31 pin OEM connector. Measure the resistance from pin 25 in the sensor harness connector to pin 7 on the engine harness side of the 31 pin OEM connector. | Less than 10 ohms? **YES** | 2C-3 |
> | Less than 10 ohms? **NORepair:** Repair or replace the engine harness or OEM harness. Repair the engine harness. 019-208 in Section 19. 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19 in the Associated Procedures Table. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 6A |  |
>
> #### STEP 2C-3. Check for an open circuit in OEM harness.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the OEM harness at the 31 pin OEM connector Disconnect the OEM harness at the Weather-Pack™ four-way connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit in the OEM harness. Measure the resistance from pin 6 on the OEM harness side of the 31 pin OEM connector to pin A (or 1) on the OEM harness side of the 4 pin connector. Measure the resistance from pin 19 on the OEM harness side of the 31 pin OEM connector to pin B (or 2) on the OEM harness side of the 4 pin connector. Measure the resistance from pin 7 on the OEM harness side of the 31 pin OEM connector to pin C (or 3) on the OEM harness side of the 4 pin connector. Measure the resistance from pin 5 on the OEM harness side of the 31 pin OEM connector to pin D (or 4) on the OEM harness side of the 4 pin connector. | Less than 10 ohms? **YES** | 3A |
> | Less than 10 ohms? **NORepair:** Repair or replace the OEM harness. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Refer to Procedure 019-208 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 6A |  |
>
> ### STEP 3. Check for a short circuit to ground in the SIGNAL wires.
>
> #### STEP 3A. Check for a short circuit to ground in the coolant level sensor SIGNAL wires.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground in the coolant level sensor signal wires. Measure the resistance from pin 22 of the sensor harness connector to engine block ground. Measure the resistance from pin 24 of the sensor harness connector to engine block ground. Measure the resistance from pin 25 of the sensor harness connector to engine block ground. | Greater than 100k ohms? **YES** | 4A |
> | Greater than 100k ohms? **NORepair:** Does **not** meet specifications. | 3A-1 |  |
>
> #### STEP 3A-1. Check for a short circuit to ground in the engine harness.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor Disconnect the engine harness from the OEM harness at the 31 pin OEM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground in the engine harness. Measure the resistance from pin 22 of the sensor harness connector to engine block ground. Measure the resistance from pin 24 of the sensor harness connector to engine block ground. | Greater than 100k ohms? **YES** | 3A-2 |
> | Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section. Replace the engine harness. Refer to Procedure 019-043 in Section 19 in the Associated Procedure Table. | 6A |  |
>
> #### STEP 3A-2. Check for a short circuit to ground in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the OEM harness from the coolant level sensor Disconnect the engine harness from the OEM harness at the 31 pin OEM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground in OEM harness. Measure the resistance from pin A (or 1) on the OEM harness side of the 4 pin connector to engine block ground. Measure the resistance from pin C (or 3) on the OEM harness side of the 4 pin connector to engine block ground. Measure the resistance from pin D (or 4) on the OEM harness side of the 4 pin connector to engine block ground. | Greater than 100k ohms? **YES** | 4A |
> | Greater than 100k ohms? **NORepair:** Repair or replace the OEM harness. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 6A |  |
>
> ### STEP 4. Check for a short circuit between the SIGNAL wires and any other wires in the engine harness or OEM harness.
>
> #### STEP 4A. Check for a short circuit between the SIGNAL wires and any other wires in the engine harness or OEM harness.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM connector from the coolant level sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit between the SIGNAL wires and any other wires in the OEM harness or engine harness. Measure the resistance from pin 22 of the sensor harness connector to all other pins in the connector. Measure the resistance from pin 24 of the sensor harness connector to all other pins in the connector. | Greater than 100k ohms? **YESRepair:** Replace the coolant level sensor. Refer to Procedure 019-017 in the Associated Procedure Table. | 4A-1 |
> | Greater than 100k ohms? **NO** | 6A |  |
>
> #### STEP 4A-1. Check for a short circuit in the engine harness.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM connector from the coolant level sensor Disconnect the engine harness from the OEM harness at the 31 pin OEM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit in the engine harness. Measure the resistance from pin 22 of the sensor harness connector to pins 24, 23, and 25 of the connector. Measure the resistance from pin 24 of the sensor harness connector to pins 22, 23, and 25 of the connector. | Greater than 100k ohms? **YES** | 4A-2 |
> | Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associate Procedures Table. | 6A |  |
>
> #### STEP 4A-2. Check for a short circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the OEM harness from the coolant level sensor Disconnect the OEM harness at the OEM side of the 31 pin OEM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit in the OEM harness. Measure the resistance from pin A (or 1) in the OEM harness connector to pins B (or 2), C (or 3), and D (or 4). Measure the resistance from pin D (or 4) in the OEM harness connector to pins A (or 1), B (or 2), and C (or 3). | Greater than 100k ohms? **YES** | 5A |
> | Greater than 100k ohms? **NORepair:** Repair or replace the OEM harness. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 6A |  |
>
> ### STEP 5. Check for a short circuit to ground in the SUPPLY wire.
>
> #### STEP 5A. Check for a short circuit to ground in the SUPPLY wire.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground in the SUPPLY wire. Measure the resistance from pin 25 in the sensor harness connector to engine block ground. | Greater than 100k ohms? **YES** | 5A-1 |
> | Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associated Procedure Table. | 6A |  |
>
> #### STEP 5A-1. Check for a short circuit in the sensor harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the sensor harness connector from the ECM. Disconnect the OEM harness from the coolant level sensor. Disconnect the sensor harness from the OEM harness at the 31 pin OEM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit in the sensor harness. Measure the resistance from pin 25 of the sensor harness connector to pin 22 of the connector. Measure the resistance from pin 25 of the sensor harness connector to pin 23 of the connector. Measure the resistance from pin 25 of the sensor harness connector to pin 24 of the connector. | Greater than 100k ohms? **YES** | 5A-2 |
> | Greater than 100k ohms? **NORepair:** Repair or replace the engine. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 6A |  |
>
> #### STEP 5A-2. Check for a short circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the sensor harness connector from the ECM. Disconnect the OEM harness from the coolant level sensor. Disconnect the sensor harness from the OEM harness at the 31 pin OEM connector. Disconnect the OEM harness at the Weather-Pack™ four-way connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit in the OEM harness. Measure the resistance from pin C (or 3) in the OEM harness connector to pins A (or 1), B (or 2), and D (or 4). | Greater than 100k ohms? **YES** | 6A |
> | Greater than 100k ohms? **NORepair:** Repair or replace the OEM harness. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 6A |  |
>
> ### STEP 6. Clear the fault codes.
>
> #### STEP 6A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Start the engine and idle for one minute. Use INSITE™ electronic service tool to verify that Fault Code 422 is inactive. | Fault Code 422 inactive? **YES** | 6B |
> | Fault Code 422 inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance. |  |
>
> #### STEP 6B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
