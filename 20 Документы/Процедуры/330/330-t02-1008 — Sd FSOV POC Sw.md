---
aliases:
  - "Останов: выключатель контроля клапана отсечки топлива"
type: "Процедура"
doc: "330-t02-1008"
title_en: "Sd FSOV POC Sw"
title_ru: "Останов: выключатель контроля клапана отсечки топлива"
modified: "2024-08-13"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4358403"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1008.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1008.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/330"
  - "перевод/машинный"
---

# Sd FSOV POC Sw
**Останов: выключатель контроля клапана отсечки топлива**

> [!abstract] Процедура · `330-t02-1008`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4358403 — Dual Fuel Technology DF101 Master Repair Manual|4358403]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2024-08-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1008.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1008.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

Предотвращается двойная эксплуатация топлива. Весь поток газа остановится, если система работает в режиме двойного топлива.

### Как пользоваться этим деревом

Это дерево можно использовать для устранения неисправности. На шаге 1 описывается вариант панели управления насосом. Этот шаг определит, на каком этапе начать диагностику.

**Описание:**

Условие отключения указывает на командное положение двойного затвора соленоида, а фактические положения доказательства переключателя закрытия **не** в требуемых положениях.

**Условия для проведения диагностики:**

В любое время модуль управления включен.

**Условия активации сообщения об ошибке:**

Включается модуль управления двойным топливом и сигнал подтверждения переключателя закрытия (обратной связи) находится **не** в правильном положении, система укажет это сообщение и защиту.

**Условия автоматической очистки кодов по умолчанию:**

Нет.

**Условия для очистки кодов ошибок вручную:**

Сброс неисправностей осуществляется локально или с помощью программного обеспечения.

Для NewCtrl (см. ниже), если сообщение об ошибке неактивно, это означает, что проблема была решена. Система остановит газ, и состояние BI4 и BOUT14 будет в правильном порядке (см. таблицу BOUT/BIN), но как только вы попытаетесь запустить сообщение об ошибке газа, появится снова.

### Практические замечания

| **Стол для комбинации BOUT/BIN** |  |  |
|---|---|---|
| **ОКРУГ 14** | **BIN4** | **Ошибочное сообщение** |
| 0 | 0 | FSOV POC Sw |
| 0 | 1 | Нет сообщения |
| 1 | 0 | Нет сообщения |
| 1 | 1 | FSOV POC Sw |

Состояние неисправности указывает на то, что двухзатворный соленоид не открывался или закрывался, когда им командовал модуль управления двойным топливом.

Если разъём ремня электропроводки газового поезда отключен, управление всегда будет в состоянии неисправности (также, если провод разрезается, переключатель сломан, или клапан механически застрял, заморожен или связывается).

Поскольку время и ответ оцениваются, когда клапану приказано открыться, неисправность может быть трудно отследить без использования программного обеспечения для регистрации данных WinScope.

Если шаги исчерпаны и неисправность не определена, полезно использовать инструмент WinScope для регистрации ответов данных во время обычных операций.

Возможные причины:

- Неисправность доказательства закрытия выключателя

- Неисправность двойного отключения соленоида

- Незащищенный разъем, плохая проводка, поврежденные контакты разъема

- Неисправное реле (реле) управления в двойной панели управления топливом

- Свободные провода в корпусе реле управления (CR2 и CR4: которые работают с клапанами 1 и 2) или на двоичном входе 6 на модуле

- Поврежденные контакты на выключателе отключения газа

- Поврежденные или неисправные предохранители в панели управления двойным топливом.

| Модуль двойного контроля топлива |  |  |
|---|---|---|
| Коды или сообщения | Причина | Последствия |
| Останов: выключатель контроля клапана отсечки топлива | Командируемая позиция FSOV и сигнал обратной связи не совпадают. | Двойной модуль управления топливом не позволит работать с газом. Двойной модуль управления топливом остановит поток газа. |

![[05m00181.png]]

Рисунок 1, контроллер Legacy (LegCtrl, показан слева) и новый контроллер (NewCtrl, показан справа)

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Определить конфигурацию ComAp. |  |
|  | **СТЭП 1А.** Определить конфигурацию. | Подразделение, оснащенное LegCtrl? |
| ШАГ 2. | Проверить сообщение о вине. |  |
|  | **Сообщение об ошибке 2А.** Активно. | Активный? |
| ШАГ 3. | Проверьте FSOV POC выключатель и схему. |  |
|  | **STEP 3A.** Проверить наличие контактов переключателя и разъема. | Грязные или поврежденные контакты? |
|  | **СТЭП 3В.** Проверьте выключатель. | Бинарный вход 6 отображает 1 с помощью InteliMonitor? |
|  | **STEP 3C.** Проверьте электропроводку. | Бинарный вход 6 отображает 1 с помощью InteliMonitor? |
|  | **STEP 3D.** Тестирование бинарного входного ответа. | Бинарный вход 6 отображает 1 с помощью InteliMonitor? |
| ШАГ 4. | Проверьте работу клапана 2 отключения топлива. |  |
|  | **STEP 4A.** Проверьте цепь 2 запорного клапана. | Напряжение системы считывается с обеих сторон предохранителя F3? |
|  | **STEP 4B.** Проверьте цепь 2 запорного клапана. | 2,7 ампера (±0,2 ампера) втягиваются и 0,9 ампера (±0,2 ампера) удерживаются в токе, наблюдаемом во время испытания на утечку? |
|  | **STEP 4C** Проверьте цепь 2 запорного клапана. | Напряжение системы считывается на разъёме жгута проводов к запорному клапану топлива? |
|  | **STEP 4D.** Проверьте цепь 2 запорного клапана. | Система напряжения рад на разъеме С3? |
|  | **STEP 4E.** Проверьте цепь 2 запорного клапана. | Напряжение системы считывается при контакте 11 реле 2 запорного клапана топлива? |
|  | **STEP 4F.** Проверьте цепь 2 запорного клапана. | Напряжение системы считывается при контакте 14 реле 2 запорного клапана топлива? |
| ШАГ 5. | Снимите вину. |  |
|  | **СТАП 5А.** Сбросьте вину. | Вернулись? |
| ШАГ 6. | Проверьте на наличие неисправностей. |  |
|  | **STEP 6A.** Просмотрите сообщение(ы) об ошибке. | Sd FSOV POC Sw - код сигнализации? |
| ШАГ 7. | Проверьте FSOV POC выключатель и схему. |  |
|  | **STEP 7A.** Проверить наличие контактов переключателя и разъема. | Грязные или поврежденные контакты? |
|  | **7B.** Проверьте выключатель. | FSOV POC Sw отображает 1 с помощью InteliMonitor? |
|  | **STEP 7C.** Проверьте электропроводку. | FSOV POC Sw отображает 1 с помощью InteliMonitor? |
|  | **STEP 7D.** Проверить ответ двоичного ввода. | FSOV POC Sw отображает 1 с помощью InteliMonitor? |
| ШАГ 8. | Проверить реакцию FSOV POC. |  |
|  | **STEP 8A.** Проверить реакцию переключателя FSOV POC. | Статус FSOV POC Sw соответствует команде FSOV 2 в InteliMonitor? |
| ШАГ 9. | Проверьте работу клапана отключения топлива. |  |
|  | **STEP 9A.** Проверить разъем и контакты FSOV. | Грязные или поврежденные контакты? |
|  | **СТЭП 9В** Проверить цепь запорного клапана топлива. | Напряжение системы при контакте питания FSOV 2 в разъеме FSOV? |
|  | **STEP 9C** Проверьте цепь запорного клапана. | Системное напряжение на контакте питания FSOV 2 в разъеме панели C4? |
|  | **STEP 9D.** Проверьте цепь запорного клапана. | Системное напряжение на разъеме модуля FSOV 2 питания Inteli Bi-Fuel? |
| ШАГ 10. | Проверьте работу клапана отключения топлива. |  |
|  | **STEP 10A.** Проверить FSOV POC ответ. | Статус FSOV POC Sw соответствует команде FSOV 2 в InteliMonitor? |

### ШАГ 1. Определить конфигурацию ComAp.

#### ШАГ 1A. Определить конфигурацию ComAp.

| **Условия:** Проверить конфигурацию панели управления ComAp. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Определите, какая панель управления ComAp установлена на устройстве. См. идентификационные изображения панели в обзоре кода тревоги. | Подразделение, оснащенное LegCtrl? *Да | 2А |
| Подразделение, оснащенное LegCtrl? **НЕТ** | 6А |  |

### ШАГ 2. Проверить сообщение о вине.

#### ШАГ 2A. Сообщение об ошибке является активным.

| **Условия:** Модуль управления питанием на двухтопливном топливе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить наличие Sd FSOV POC. Используйте InteliMonitor. | Активный? *Да | 5а |
| Активный? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте FSOV POC выключатель и схему.

#### ШАГ 3A. Проверьте доказательство контактов переключателя и разъема.

| **Условия:** Выключите замок зажигания. Отсоедините доказательство закрытия коммутатора от двойного топливного разъёма жгута. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите двойную топливную проводку и доказательство контактов разъёма переключателя закрытия для следующего: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В доказательстве наличия переключателя или разъёма жгута проводов обнаружено поврежденное соединение. Проверьте все проводов, подключенные последовательно. Очистите разъем и булавки. Заменить поврежденный участок проводов ремнем поврежденного доказательства закрытия переключателя. Ремонт проводов жгута. См. процедуру 019-564 в разделе 19. Замените выключатель. См. процедуру 019-581 в разделе 19. | 5а |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте выключатель.

| **Условия:** Двигатель не работает. Power ON двойной панели управления топливом. Отсоедините доказательство закрытия переключателя от разъема жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Поместите провод прыгуна между проводом SIGNAL и RETURN на разъёме жгута проводов. | Бинарный вход 6 отображает 1 с помощью InteliMonitor? *Да | 4А |
| Бинарный вход 6 отображает 1 с помощью InteliMonitor? **НЕТ** | 3C |  |

#### ШАГ 3C. Проверьте проводку.

| **Условия:** Двигатель не работает. Power ON двойной панели управления топливом. Отсоедините проводную упряжку от разъема C3. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Поместите провод прыгуна между проводом SIGNAL и RETURN на разъёме проводов C3. | Бинарный вход 6 отображает 1 с помощью InteliMontor? **Ремонт:** Установка проводов неисправна. Ремонт или замена проводов жгута. См. процедуру 019-564 в разделе 19. | 5а |
| Бинарный вход 6 отображает 1 с помощью InteliMontor? **НЕТ** | 3D |  |

#### ШАГ 3D. Тестирование бинарного входного ответа.

| **Условия:** Двигатель не работает. Включение модуля управления двойным топливом. Двойной модуль управления топливом |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сделайте временное соединение от наземного шпилька панели до двоичного входного терминала BI-6. Используйте одобренный прыгун. Наблюдайте, когда соединение сделано, состояние ввода становится 1. | Бинарный вход 6 отображает 1 с помощью InteliMontor? **Ремонт:** Ремонт или замена проводов от C3-A до модуля управления BI-6 (проводка 2001). См. руководство по обслуживанию панели управления. | 5а |
| Бинарный вход 6 отображает 1 с помощью InteliMontor? **NORepair:** Обнаружен неисправный модуль Inteli Bi-Fuel. См. руководство по обслуживанию панели управления. | 5а |  |

### ШАГ 4. Проверьте работу клапана 2 отключения топлива.

#### ШАГ 4A. Проверьте цепь 2 запорного клапана топлива.

| **Условия:** Двигатель не работает. Включение модуля управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение с обеих сторон предохранителя F3 для запорного клапана 2. | Напряжение системы считывается с обеих сторон предохранителя F3? *Да | 4B |
| Напряжение системы считывается с обеих сторон предохранителя F3? **NORepair:** Проверить предохранитель. См. процедуру 019-051 в разделе 19. Убедитесь, что батарея полностью заряжена и работает должным образом. См. сервисную документацию изготовителя оборудования. Проверьте проводку к батарее. См. процедуру 019-564 в разделе 19. | 5а |  |

#### ШАГ 4B. Проверьте цепь 2 запорного клапана топлива.

| **Условия:** Двигатель не работает. Модуль управления двойным топливом Power ON. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Установите амперметр (10 ампер диапазон) вместо предохранителя. Инициировать испытание внутреннего клапана клапана отключения топлива. См. процедуру 005-236 в разделе 5. | 2,7 ампера (±0,2 ампера) втягиваются и 0,9 ампера (±0,2 ампера) удерживаются в токе, наблюдаемом во время испытания на утечку? **Ремонт:** Обнаружен неисправный переключатель проверки закрытия. Калибровка выключателя проверки закрытия. См. процедуру 019-581 в разделе 19. Если калибровка не приводит систему в спецификацию, то переключатель проверки закрытия должен быть заменен. | 5а |
| 2,7 ампера (±0,2 ампера) втягиваются и 0,9 ампера (±0,2 ампера) удерживаются в токе, наблюдаемом во время испытания на утечку? **НЕТ** | 4C |  |

#### ШАГ 4C. Проверьте цепь 2 запорного клапана топлива.

| **Условия:** Двигатель не работает. Установите предохранитель F3. Модуль управления двойным топливом Power ON. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отсоедините разъем от клапана отключения топлива. Инициировать испытание внутреннего клапана клапана отключения топлива. См. процедуру 005-236 в разделе 5. | Напряжение системы считывается на разъёме жгута проводов к запорному клапану топлива? **Ремонт:** Неисправный клапан отключения топлива был найден. См. процедуру 005-044 в разделе 5. | 5а |
| Напряжение системы считывается на разъёме жгута проводов к запорному клапану топлива? **НЕТ** | 4D |  |

#### ШАГ 4D. Проверьте цепь 2 запорного клапана топлива.

| **Условия:** Двигатель не работает. Модуль управления двойным топливом Power ON. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отсоедините проводную упряжку от разъема C3. Инициировать испытание внутреннего клапана клапана отключения топлива. См. процедуру 005-236 в разделе 5. Измерить напряжение для запорного клапана 2 топлива при контакте подачи разъёма С3. | Напряжение системы считывается на разъеме C3? **Ремонт:** Выявлена неисправная электропроводка. Ремонт или замена проводной упряжки от разъема С3 на запорный клапан. См. процедуру 019-564 в разделе 19. | 5а |
| Напряжение системы считывается на разъеме C3? **НЕТ** | 4Е |  |

#### ШАГ 4E. Проверьте цепь 2 запорного клапана топлива.

| **Условия:** Двигатель не работает. Модуль управления двойным топливом Power ON. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить напряжение для запорного клапана 2 топлива при контакте 11 запорного клапана 2 реле SUPPLY. | Напряжение системы считывается при контакте 11 реле 2 запорного клапана топлива? **Ремонт:** Выявлена неисправность проводов в панели управления. Ремонт или замена неисправной проводов в панели управления. См. руководство по обслуживанию панели управления. | 5а |
| Напряжение системы считывается при контакте 11 реле 2 запорного клапана топлива? **НЕТ** | 4F |  |

#### ШАГ 4F. Проверьте цепь 2 запорного клапана топлива.

| **Условия:** Двигатель не работает. Модуль управления двойным топливом Power ON. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отсоедините разъем к клапану отключения топлива. Инициировать испытание внутреннего клапана клапана отключения топлива. См. процедуру 005-236 в разделе 5. Измерить напряжение для запорного клапана 2 топлива при контакте подачи (контакте 14) реле запорного клапана 2 топлива. | Напряжение системы считывается при контакте 14 реле 2 запорного клапана топлива? **Ремонт:** Выявлена неисправность проводов в панели управления. Ремонт или замена неисправной проводов в панели управления. См. руководство по обслуживанию панели управления. | 5а |
| Напряжение системы считывается при контакте 14 реле 2 запорного клапана топлива? **NORepair:** Проверить, что реле функционирует должным образом, наблюдая светодиодный индикатор на корпусе реле. Если светодиод не освещается, проверьте реле. См. процедуру 019-589 в разделе 19. Если реле работает правильно, то обнаружена неисправность в проводах панели управления между реле и предохранителем. См. руководство по обслуживанию панели управления. | 5а |  |

### ШАГ 5. Снимите вину.

#### ШАГ 5A. Снимите вину.

| **Условия:** Двигатель не работает. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сброс неисправности на панели управления или через InteliMonitor. Работайте с двигателем в условиях, позволяющих замену газа. | Вернулись? Возвращение к шагам устранения неполадок или обращение в авторизованное место ремонта Cummins®, если все шаги были завершены и проверены повторно. | 2А |
| Вернулись? **НЕТ** | Ремонт завершён |  |

### ШАГ 6. Проверьте на наличие неисправностей.

#### ШАГ 6A. Просмотреть сообщение (сообщения) о неисправности.

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте локальную панель отображения сообщений о неисправностях в списке тревоги и истории. | Sd FSOV POC Sw - код сигнализации? *Да | 7А |
| Sd FSOV POC Sw - код сигнализации? **НЕТ** | Верните насос в эксплуатацию и на монитор. |  |

### ШАГ 7. Проверьте FSOV POC выключатель и схему.

#### ШАГ 7A. Проверьте доказательство контактов переключателя и разъема.

| **Условия:** Выключите замок зажигания. Отсоедините доказательство закрытия коммутатора от двойного топливного разъёма жгута. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите двойную топливную проводку и доказательство контактов разъёма переключателя закрытия для следующего: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В доказательстве наличия переключателя или разъёма жгута проводов обнаружено поврежденное соединение. Ремонт или замена поврежденного участка электропроводки ремня или поврежденного доказательства закрытия/закрытия валидационного переключателя. Ремонт проводов жгута. См. процедуру 019-564 в разделе 19. Заменить переключатель проверки закрытия. См. процедуру 019-581 в разделе 19. | 8а |
| Грязные или поврежденные контакты? **НЕТ** | 7B |  |

#### ШАГ 7B. Проверьте выключатель.

| **Условия:** Двигатель не работает. Power ON двойной панели управления топливом. Отсоедините доказательство закрытия разъёма переключателя от двойной топливной проводов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Поместите провод прыгуна между проводом SIGNAL и RETURN на разъёме жгута проводов. | FSOV POC Sw отображает 1 с помощью InteliMonitor? **Ремонт:** Регулировать или заменить переключатель проверки закрытия. См. процедуру 019-581 в разделе 19. | 8а |
| FSOV POC Sw отображает 1 с помощью InteliMonitor? **НЕТ** | 7C |  |

#### ШАГ 7C. Проверьте проводку.

| **Условия:** Двигатель не работает. Модуль управления двойным топливом Power ON. Подключите InteliMonitor к панели управления двойным топливом. Отсоедините двойную топливную проводку от разъема C3. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Поместите провод прыгуна между проводом SIGNAL и RETURN на разъёме проводов C3. | FSOV POC Sw отображает 1 с помощью InteliMonitor? **Ремонт:** Установка проводов неисправна. Ремонт или замена проводов жгута. См. процедуру 019-564 в разделе 19. | 8а |
| FSOV POC Sw отображает 1 с помощью InteliMonitor? **НЕТ** | 7D |  |

#### ШАГ 7D. Тестирование бинарного входного ответа.

| **Условия:** Двигатель не работает. Модуль управления двойным топливом Power ON. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сделайте временное соединение от поверхности панели до контакта сигнала POC на разъеме модуля IBF. Используйте одобренный прыгун. Наблюдайте, когда соединение сделано, состояние ввода становится 1. | FSOV POC Sw отображает 1 с помощью InteliMonitor? **Ремонт:** Ремонт или замена внутренней проводов панели ремня. | 8а |
| FSOV POC Sw отображает 1 с помощью InteliMonitor? **NORepair:** Обнаружен неисправный модуль Inteli Bi-Fuel. См. руководство по обслуживанию панели управления. | 9а |  |

### ШАГ 8. Проверить реакцию FSOV POC.

#### ШАГ 8A. Проверить реакцию FSOV POC.

| **Условия:** Двигатель не работает. Модуль управления двойным топливом Power ON. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Ручное управление FSOV 2 в ручном режиме: IMON - Дистанционные переключатели - «FSOV 2 ON» (требуется пароль уровня 2). Проверьте статус POC Switch, чтобы сопоставить команду клапана с InteliMonitor. При ручной работе с FSOV с помощью InteliMonitor и с выключенным двигателем вы должны быть в состоянии слышать и чувствовать движение клапана. | Статус FSOV POC Sw соответствует команде FSOV 2 в InteliMonitor? *Да | Верните насос в эксплуатацию и на монитор. |
| Статус FSOV POC Sw соответствует команде FSOV 2 в InteliMonitor? **НЕТ** | 9а |  |

### ШАГ 9. Проверьте работу клапана отключения топлива.

#### ШАГ 9A. Проверьте разъем и контакты FSOV.

| **Условия:** Выключите замок зажигания. Отсоедините двойную проводку от FSOV. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъёма двойной топливной проводов и разъёма FSOV на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** Ремонт или замена двухтопливной электропроводки ремня или поврежденного FSOV. Ремонт проводов жгута. См. процедуру 019-564 в разделе 19. Заменить ФСОВ. См. процедуру 005-044 в разделе 5. | 10А |
| Грязные или поврежденные контакты? **НЕТ** | 9В |  |

#### ШАГ 9B. Проверьте цепь клапана отключения топлива.

| **Условия:** Двигатель не работает. Отсоедините двойную проводку от FSOV. Модуль управления двойным топливом Power ON. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Ручное управление FSOV 2 в ручном режиме: IMON - Дистанционные переключатели - «FSOV 2 ON» (требуется пароль уровня 2). Измерение напряжения батареи FSOV 2 питающих штифтов. | Напряжение системы при контакте питания FSOV 2 в разъеме FSOV? *Да | 10А |
| Напряжение системы при контакте питания FSOV 2 в разъеме FSOV? **НЕТ** | 9С |  |

#### ШАГ 9C. Проверьте цепь клапана отключения топлива.

| **Условия:** Двигатель не работает. Отсоедините двухтопливную проводку ремня разъема С4 от панели. Модуль управления двойным топливом Power ON. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Ручное управление FSOV 2 в ручном режиме: IMON - Дистанционные переключатели - «FSOV 2 ON» (требуется пароль уровня 2). Измерение напряжения батареи FSOV 2 контакта питания в двойной панели управления топливом C4 Connector. | Системное напряжение на контакте питания FSOV 2 в разъеме панели C4? **Ремонт:** Ремонт или замена поврежденной двухтопливной электропроводки ремня. См. процедуру 019-564 в разделе 19. | 10А |
| Системное напряжение на контакте питания FSOV 2 в разъеме панели C4? **НЕТ** | 9D |  |

#### ШАГ 9D. Проверьте цепь клапана отключения топлива.

| **Условия:** Двигатель не работает. Модуль управления двойным топливом Power ON. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Ручное управление FSOV 2 в ручном режиме: IMON - Дистанционные переключатели - «FSOV 2 ON» (требуется пароль уровня 2). Измерение напряжения батареи на разъеме модуля питания FSOV 2 Inteli Bi-Fuel. См. схему проводов для идентификации контакта с разъемом. | Системное напряжение на разъеме модуля FSOV 2 питания Inteli Bi-Fuel? **Ремонт:** Ремонт или замена поврежденной двойной панели управления топливом внутренней электропроводки ремня. | 10А |
| Системное напряжение на разъеме модуля FSOV 2 питания Inteli Bi-Fuel? **NORepair:** Обнаружен неисправный модуль Inteli Bi-Fuel. Заменить модуль IBF. См. процедуру 019-568 в разделе 19. | 10А |  |

### ШАГ 10. Проверить FSOV и POC коммутационный ответ.

#### ШАГ 10A. Проверить FSOV POC ответ.

| **Условия:** Двигатель не работает. Модуль управления двойным топливом Power ON. Подключите InteliMonitor к панели управления двойным топливом |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Ручное управление FSOV 2 в ручном режиме: IMON - Дистанционные переключатели - «FSOV 2 ON» (требуется пароль уровня 2). Проверьте статус POC Switch, чтобы сопоставить команду клапана с InteliMonitor. При ручной работе с FSOV с помощью InteliMonitor и с выключенным двигателем вы должны быть в состоянии слышать и чувствовать движение клапана. Если не перейти непосредственно к шагу 9А. | Статус FSOV POC Sw соответствует команде FSOV 2 в InteliMonitor? *Да | Верните насос в эксплуатацию и на монитор. |
| Статус FSOV POC Sw соответствует команде FSOV 2 в InteliMonitor? **НЕТ** | Вернитесь к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> Dual fuel operation will be prevented. All gas flow will stop if system is operating in dual fuel mode.
>
> ### How To Use This Tree
>
> This tree can be used to troubleshoot a malfunction. Step 1 describes the variant of pump control panel. This step will determine which step to start diagnostics.
>
> **Circuit Description:**
>
> Shutdown condition indicates the commanded position of the dual shutoff solenoid and actual positions of the proof of closure switch are **not** in the required positions.
>
> **Conditions for Running the Diagnostics:**
>
> Anytime the control module is powered ON.
>
> **Conditions for Activating the Fault Message:**
>
> Dual fuel control module is powered on and the proof of closure switch (feedback) signal is **not** in the correct position, the system will indicate this message and protection.
>
> **Conditions for Clearing the Fault Codes Automatically:**
>
> None.
>
> **Conditions for Clearing the Fault Codes Manually:**
>
> Fault reset is operated locally or via software.
>
> For NewCtrl (see below), if the error message is inactive, it does **not** mean problem was solved. System will stop gas and state of BI4 and BOUT14 are in correct order (see table BOUT/BIN combination), but once you will try to run on gas error message will appear again.
>
> ### Shoptalk
>
> | **Table of BOUT/BIN combination** |  |  |
> |---|---|---|
> | **BOUT14** | **BIN4** | **Error message** |
> | 0 | 0 | FSOV POC Sw |
> | 0 | 1 | No message |
> | 1 | 0 | No message |
> | 1 | 1 | FSOV POC Sw |
>
> The fault condition indicates the dual shutoff solenoid failed to open or close when commanded by the dual fuel control module.
>
> If the gas train harness connector is unplugged, the control will always be in the fault condition (also if the wire is cut, switch is broken, or the valve is mechanically stuck, frozen, or binding).
>
> Because the timing and response are evaluated when the valve is commanded to open, the fault can be difficult to track without the use of WinScope data-logging software.
>
> If steps are exhausted and failure is **not** identified, it is useful to use the WinScope PC tool to data log the responses during normal operations.
>
> Possible causes:
>
> - Malfunctioning proof of closure switch
>
> - Malfunctioning dual shutoff solenoid
>
> - Unplugged connector, bad wiring, damaged connector pins
>
> - Malfunctioning control relay(s) in the dual fuel control panel
>
> - Loose wires at the control relay housing (CR2 and CR4: that operate valves 1 and 2) or at the binary input 6 on the module
>
> - Damaged contacts on the gas shutdown switch
>
> - Damaged or malfunctioning fuses in the dual fuel control panel.
>
> | Dual Fuel Control Module |  |  |
> |---|---|---|
> | Codes or Messages | Reason | Effect |
> | Sd FSOV POC Sw | Commanded FSOV position and feedback signal disagree. | Dual fuel control module will **not** allow gas operations. Dual fuel control module will stop gas flow. |
>
> Figure 1, Legacy controller (LegCtrl , shown left) and new controller (NewCtrl, shown right)
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Determine ComAp configuration. |  |
> |  | **STEP 1A.** Determine configuration. | Unit equipped with LegCtrl? |
> | STEP 2. | Validate the fault message. |  |
> |  | **STEP 2A.** Fault message is active. | Fault active? |
> | STEP 3. | Check the FSOV POC switch and circuit. |  |
> |  | **STEP 3A.** Inspect the proof of closure switch and connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the switch. | Binary Input 6 displays a 1 using InteliMonitor? |
> |  | **STEP 3C.** Check the wiring harness. | Binary Input 6 displays a 1 using InteliMonitor? |
> |  | **STEP 3D.** Test the binary input response. | Binary Input 6 displays a 1 using InteliMonitor? |
> | STEP 4. | Check the fuel shutoff valve 2 operation. |  |
> |  | **STEP 4A.** Check the fuel shutoff valve 2 circuit. | System voltage read on both side of fuse F3? |
> |  | **STEP 4B.** Check the fuel shutoff valve 2 circuit. | 2.7 amps (±0.2 amps) pull in and 0.9 amps (±0.2 amps) hold in current observed during the leak test? |
> |  | **STEP 4C.** Check the fuel shutoff valve 2 circuit. | System voltage read at the harness connector to the fuel shutoff valve? |
> |  | **STEP 4D.** Check the fuel shutoff valve 2 circuit. | System voltage rad at the C3 connector? |
> |  | **STEP 4E.** Check the fuel shutoff valve 2 circuit. | System voltage read at pin 11 of the fuel shutoff valve 2 relay? |
> |  | **STEP 4F.** Check the fuel shutoff valve 2 circuit. | System voltage read at pin 14 of the fuel shutoff valve 2 relay? |
> | STEP 5. | Reset the fault. |  |
> |  | **STEP 5A.** Reset the fault. | Fault returns? |
> | STEP 6. | Check for faults. |  |
> |  | **STEP 6A.** Review the fault message(s). | Sd FSOV POC Sw alarm code is present? |
> | STEP 7. | Check the FSOV POC switch and circuit. |  |
> |  | **STEP 7A.** Inspect the proof of closure switch and connector pins. | Dirty or damaged pins? |
> |  | **STEP 7B.** Check the switch. | FSOV POC Sw displays a 1 using InteliMonitor? |
> |  | **STEP 7C.** Check the wiring harness. | FSOV POC Sw displays a 1 using InteliMonitor? |
> |  | **STEP 7D.** Test the binary input response. | FSOV POC Sw displays a 1 using InteliMonitor? |
> | STEP 8. | Verify FSOV POC switch response. |  |
> |  | **STEP 8A.** Verify FSOV POC switch response. | FSOV POC Sw status matches FSOV 2 command in InteliMonitor? |
> | STEP 9. | Check the fuel shutoff valve operation. |  |
> |  | **STEP 9A.** Inspect the FSOV connector and pins. | Dirty or damaged pins? |
> |  | **STEP 9B.** Check the fuel shutoff valve circuit. | System voltage at FSOV 2 supply pin in FSOV connector? |
> |  | **STEP 9C.** Check the fuel shutoff valve circuit. | System voltage at FSOV 2 supply pin in panel C4 connector? |
> |  | **STEP 9D.** Check the fuel shutoff valve circuit. | System voltage at FSOV 2 supply pin Inteli Bi-Fuel module connector? |
> | STEP 10. | Check the fuel shutoff valve operation. |  |
> |  | **STEP 10A.** Verify FSOV POC response. | FSOV POC Sw status matches FSOV 2 command in InteliMonitor? |
>
> ### STEP 1. Determine ComAp configuration.
>
> #### STEP 1A. Determine ComAp configuration.
>
> | **Conditions:** Verify ComAp control panel configuration. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Determine which ComAp control panel is installed on the unit. Refer to panel identification images in alarm code overview. | Unit equipped with LegCtrl? **YES** | 2A |
> | Unit equipped with LegCtrl? **NO** | 6A |  |
>
> ### STEP 2. Validate the fault message.
>
> #### STEP 2A. Fault message is active.
>
> | **Conditions:** Power ON dual fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for occurrences of Sd FSOV POC. Use InteliMonitor. | Fault active? **YES** | 5A |
> | Fault active? **NO** | 3A |  |
>
> ### STEP 3. Check the FSOV POC switch and circuit.
>
> #### STEP 3A. Inspect the proof of closure switch and connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the proof of closure switch connector from the dual fuel harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the dual fuel harness and proof of closure switch connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the proof of closure switch or harness connector. Check all harnesses connected in series. Clean the connector and pins. Replace the damaged section of harness of damaged proof of closure switch. Repair the harness. Refer to Procedure 019-564 in Section 19. Replace the switch. Refer to Procedure 019-581 in Section 19. | 5A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the switch.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the proof of closure switch connector from the engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Place a jumper wire between the SIGNAL and RETURN wire on the wiring harness connector. | Binary Input 6 displays a 1 using InteliMonitor? **YES** | 4A |
> | Binary Input 6 displays a 1 using InteliMonitor? **NO** | 3C |  |
>
> #### STEP 3C. Check the wiring harness.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the wiring harness from the C3 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Place a jumper wire between the SIGNAL and RETURN wire on the C3 wiring harness connector. | Binary Input 6 displays a 1 using InteliMontor? **YESRepair:** The wiring harness has malfunctioned. Repair or replace the wiring harness. Refer to Procedure 019-564 in Section 19. | 5A |
> | Binary Input 6 displays a 1 using InteliMontor? **NO** | 3D |  |
>
> #### STEP 3D. Test the binary input response.
>
> | **Conditions:** Engine not operating. Power ON the dual fuel control module. Place dual fuel control module |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Make a temporary connection from the panel ground stud to the binary input terminal BI-6. Use an approved jumper wire. Observe when the connection is made, the input status becomes 1. | Binary Input 6 displays a 1 using InteliMontor? **YESRepair:** Repair or replace the wiring from C3-A to the control module BI-6 (wire 2001). See control panel service manual. | 5A |
> | Binary Input 6 displays a 1 using InteliMontor? **NORepair:** A malfunctioning Inteli Bi-Fuel module has been detected. See control panel service manual. | 5A |  |
>
> ### STEP 4. Check the fuel shutoff valve 2 operation.
>
> #### STEP 4A. Check the fuel shutoff valve 2 circuit.
>
> | **Conditions:** Engine not operating. Power ON the dual fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage on both side of fuse F3 for fuel shutoff valve 2. | System voltage read on both sides of fuse F3? **YES** | 4B |
> | System voltage read on both sides of fuse F3? **NORepair:** Inspect the fuse. Refer to Procedure 019-051 in Section 19. Verify the battery is fully charged and working properly. See equipment manufacturer service information. Inspect the wiring to the battery. Refer to Procedure 019-564 in Section 19. | 5A |  |
>
> #### STEP 4B. Check the fuel shutoff valve 2 circuit.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Install an ammeter (10 amp range) in place of the fuse. Initiate the Fuel Shutoff Valve Internal Valve Leak Test. Refer to Procedure 005-236 in Section 5. | 2.7 amps (±0.2 amps) pull in and 0.9 amps (±0.2 amps) hold in current observed during the leak test? **YESRepair:** A malfunctioning closure validation switch has been found. Calibrate the closure validation switch. Refer to Procedure 019-581 in Section 19. If calibration does **not** bring the system into specification, the closure validation switch **must** be replace. | 5A |
> | 2.7 amps (±0.2 amps) pull in and 0.9 amps (±0.2 amps) hold in current observed during the leak test? **NO** | 4C |  |
>
> #### STEP 4C. Check the fuel shutoff valve 2 circuit.
>
> | **Conditions:** Engine not operating. Install fuse F3. Power ON dual fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disconnect the connector from the fuel shutoff valve. Initiate the Fuel Shutoff Valve Internal Valve Leak Test. Refer to Procedure 005-236 in Section 5. | System voltage read at the harness connector to the fuel shutoff valve? **YESRepair:** A malfunctioning fuel shutoff valve has been found. Refer to Procedure 005-044 in Section 5. | 5A |
> | System voltage read at the harness connector to the fuel shutoff valve? **NO** | 4D |  |
>
> #### STEP 4D. Check the fuel shutoff valve 2 circuit.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disconnect the wiring harness from the C3 connector. Initiate the Fuel Shutoff Valve Internal Valve Leak Test. Refer to Procedure 005-236 in Section 5. Measure the voltage for fuel shutoff valve 2 at the SUPPLY pin of the C3 connector. | System voltage read at the C3 connector? **YESRepair:** A malfunctioning wiring harness has been identified. Repair or replace the wiring harness from the C3 connector to the shutoff valve. Refer to Procedure 019-564 in Section 19. | 5A |
> | System voltage read at the C3 connector? **NO** | 4E |  |
>
> #### STEP 4E. Check the fuel shutoff valve 2 circuit.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage for fuel shutoff valve 2 at the SUPPLY pin 11 of the fuel shutoff valve 2 relay. | System voltage read at pin 11 of the fuel shutoff valve 2 relay? **YESRepair:** A malfunction in the wiring in the control panel has been identified. Repair or replace the malfunctioning wiring in the control panel. See control panel service manual. | 5A |
> | System voltage read at pin 11 of the fuel shutoff valve 2 relay? **NO** | 4F |  |
>
> #### STEP 4F. Check the fuel shutoff valve 2 circuit.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disconnect the connector to the fuel shutoff valve. Initiate the Fuel Shutoff Valve Internal Valve Leak Test. Refer to Procedure 005-236 in Section 5. Measure the voltage for fuel shutoff valve 2 at the SUPPLY pin (pin 14) of the fuel shutoff valve 2 relay. | System voltage read at pin 14 of the fuel shutoff valve 2 relay? **YESRepair:** A malfunction in the wiring in the control panel has been identified. Repair or replace the malfunctioning wiring in the control panel. See control panel service manual. | 5A |
> | System voltage read at pin 14 of the fuel shutoff valve 2 relay? **NORepair:** Verify the relay is functioning properly by observing the LED indicator on the body of the relay. If the LED is not lighting, inspect the relay. Refer to Procedure 019-589 in Section 19. If the relay is operating correctly, a malfunction in the control panel wiring between the relay and fuse has bee detected. See control panel service manual. | 5A |  |
>
> ### STEP 5. Reset the fault.
>
> #### STEP 5A. Reset the fault.
>
> | **Conditions:** Engine not operating. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Reset the fault on the control panel or through InteliMonitor. Operate the engine under conditions to allow gas substitution. | Fault returns? **YESRepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 2A |
> | Fault returns? **NO** | Repair complete |  |
>
> ### STEP 6. Check for faults.
>
> #### STEP 6A. Review the fault message(s).
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check local display panel for fault messages in alarm list and history. | Sd FSOV POC Sw alarm code is present? **YES** | 7A |
> | Sd FSOV POC Sw alarm code is present? **NO** | Return the pump to service and monitor. |  |
>
> ### STEP 7. Check the FSOV POC switch and circuit.
>
> #### STEP 7A. Inspect the proof of closure switch and connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the proof of closure switch connector from the dual fuel harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the dual fuel harness and proof of closure switch connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the proof of closure switch or harness connector. Repair or replace the damaged section of harness or damaged proof of closure / closure validation switch. Repair the harness. Refer to Procedure 019-564 in Section 19. Replace the closure validation switch. Refer to Procedure 019-581 in Section 19. | 8A |
> | Dirty or damaged pins? **NO** | 7B |  |
>
> #### STEP 7B. Check the switch.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the proof of closure switch connector from the dual fuel harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Place a jumper wire between the SIGNAL and RETURN wire on the wiring harness connector. | FSOV POC Sw displays a 1 using InteliMonitor? **YESRepair:** Readjust or replace the closure validation switch. Refer to Procedure 019-581 in Section 19. | 8A |
> | FSOV POC Sw displays a 1 using InteliMonitor? **NO** | 7C |  |
>
> #### STEP 7C. Check the wiring harness.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Disconnect the dual fuel wiring harness from the C3 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Place a jumper wire between the SIGNAL and RETURN wire on the C3 wiring harness connector. | FSOV POC Sw displays a 1 using InteliMonitor? **YESRepair:** The wiring harness has malfunctioned. Repair or replace the wiring harness. Refer to Procedure 019-564 in Section 19. | 8A |
> | FSOV POC Sw displays a 1 using InteliMonitor? **NO** | 7D |  |
>
> #### STEP 7D. Test the binary input response.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Make a temporary connection from the panel ground to the POC Signal pin on IBF Module connector. Use an approved jumper wire. Observe when the connection is made, the input status becomes 1. | FSOV POC Sw displays a 1 using InteliMonitor? **YESRepair:** Repair or replace the panel internal wiring harness. | 8A |
> | FSOV POC Sw displays a 1 using InteliMonitor? **NORepair:** A malfunctioning Inteli Bi-Fuel module has been detected. See control panel service manual. | 9A |  |
>
> ### STEP 8. Verify FSOV POC switch response.
>
> #### STEP 8A. Verify FSOV POC switch response.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Manually Operate FSOV 2 in manual mode: IMON - Remote switches – “FSOV 2 ON” (Level 2 password required). Verify POC Switch status matches valve command with InteliMonitor. While manually operating the FSOV using InteliMonitor and with the engine off you should be able to hear and feel the valve move. | FSOV POC Sw status matches FSOV 2 command in InteliMonitor? **YES** | Return the pump to service and monitor. |
> | FSOV POC Sw status matches FSOV 2 command in InteliMonitor? **NO** | 9A |  |
>
> ### STEP 9. Check the fuel shutoff valve operation.
>
> #### STEP 9A. Inspect the FSOV connector and pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the dual fuel harness from the FSOV. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the dual fuel harness and FSOV connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair or replace the dual fuel harness or damaged FSOV. Repair the harness. Refer to Procedure 019-564 in Section 19. Replace the FSOV. Refer to Procedure 005-044 in Section 5. | 10A |
> | Dirty or damaged pins? **NO** | 9B |  |
>
> #### STEP 9B. Check the fuel shutoff valve circuit.
>
> | **Conditions:** Engine not operating. Disconnect the dual fuel harness from the FSOV. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Manually Operate FSOV 2 in manual mode: IMON - Remote switches – “FSOV 2 ON” (Level 2 password required). Measure for battery voltage FSOV 2 supply pins. | System voltage at FSOV 2 supply pin in FSOV connector? **YES** | 10A |
> | System voltage at FSOV 2 supply pin in FSOV connector? **NO** | 9C |  |
>
> #### STEP 9C. Check the fuel shutoff valve circuit.
>
> | **Conditions:** Engine not operating. Disconnect the dual fuel harness C4 connector from panel. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Manually Operate FSOV 2 in manual mode: IMON - Remote switches – “FSOV 2 ON” (Level 2 password required). Measure for battery voltage FSOV 2 supply pin in Dual Fuel Control Panel C4 Connector. | System voltage at FSOV 2 supply pin in panel C4 connector? **YESRepair:** Repair or replace damaged dual fuel wiring harness. Refer to Procedure 019-564 in Section 19. | 10A |
> | System voltage at FSOV 2 supply pin in panel C4 connector? **NO** | 9D |  |
>
> #### STEP 9D. Check the fuel shutoff valve circuit.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Manually Operate FSOV 2 in manual mode: IMON - Remote switches – “FSOV 2 ON” (Level 2 password required). Measure for battery voltage at FSOV 2 supply pin Inteli Bi-Fuel module connector. Refer to wiring diagram for connector pin identification. | System voltage at FSOV 2 supply pin Inteli Bi-Fuel module connector? **YESRepair:** Repair or replace damaged dual fuel control panel internal wiring harness. | 10A |
> | System voltage at FSOV 2 supply pin Inteli Bi-Fuel module connector? **NORepair:** A malfunctioning Inteli Bi-Fuel module has been detected. Replace IBF module. Refer to Procedure 019-568 in Section 19. | 10A |  |
>
> ### STEP 10. Verify FSOV and POC switch response.
>
> #### STEP 10A. Verify FSOV POC response.
>
> | **Conditions:** Engine not operating. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Manually Operate FSOV 2 in manual mode: IMON - Remote switches – “FSOV 2 ON” (Level 2 password required). Verify POC Switch status matches valve command with InteliMonitor. While manually operating the FSOV using InteliMonitor and with the engine off you should be able to hear and feel the valve move. If not proceed directly to Step 9A. | FSOV POC Sw status matches FSOV 2 command in InteliMonitor? **YES** | Return the pump to service and monitor. |
> | FSOV POC Sw status matches FSOV 2 command in InteliMonitor? **NO** | Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. |  |
