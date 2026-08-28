---
aliases:
  - "Газодизельный режим не готов"
type: "Процедура"
doc: "330-t02-1111"
title_en: "DF Not Ready"
title_ru: "Газодизельный режим не готов"
modified: "2024-08-06"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/330"
  - "перевод/машинный"
---

# DF Not Ready
**Газодизельный режим не готов**

> [!abstract] Процедура · `330-t02-1111`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4358403 — Dual Fuel Technology DF101 Master Repair Manual|4358403]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2024-08-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1111.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

Блок **не** перейдет в режим двойного топлива.

### Как пользоваться этим деревом

Это дерево можно использовать для устранения неисправности. Начните с шага 1 поиска неисправностей. Шаг 2 задаст ряд вопросов и предоставит список шагов по устранению неполадок, в зависимости от симптома.

Легктрль

**Описание схемы**

DF **Not** Ready - сообщение STATUS, указывающее на то, что одно из условий, необходимых для работы с двойным топливом, не было выполнено. В этом состоянии панель **не** позволит работать газу.

**Условия для проведения диагностики**

В любое время модуль управления включен.

**Условия для активации сообщения о статусе:**

О возможных причинах см. в разделе практического примечания.

**Условия автоматической очистки сообщения о статусе:**

Удовлетворить все условия для начала работы на двух видах топлива.

**Условия для ручного снятия сообщения о статусе:**

Нет.

Нью-Ктрл

**Описание схемы**

DF **Not** Готовое сообщение отображается в списке тревог Newctr и InteliMonitor.

**Условия для проведения диагностики**

В любое время модуль управления включен.

**Условия для активации сообщения о статусе:**

О возможных причинах см. в разделе практического примечания.

**Условия автоматической очистки сообщения о статусе:**

Удовлетворить все условия для начала работы на двух видах топлива.

**Условия для ручного снятия сообщения о статусе:**

### Практические замечания

Сигнализация сигнализирует о том, что система не готова к двойному использованию топлива из-за нескольких условий (описанных в возможных причинах). После выполнения всех условий, двойная работа топлива будет включена автоматически.

Если любой другой сигнал тревоги/s активен одновременно с DF **Not** Ready, устраните неполадки, которые сигнализируют/s в первую очередь.

Если NewCtrl: Информация в InteliMonitor Tool - PLC Monitor - Sheet 5 может использоваться вместе с деревом устранения неполадок.

Если вход на определенном блоке ошибок имеет белую точку на входе, а линия на входе черная, вам нужно перейти к этапу устранения неполадок, связанному с этим входом. Если на входе есть только черная точка, а входная линия синяя, перейдите на этап устранения неполадок, связанный с этим входом.

Возможные причины LegCtrl включают:

- Положение в области передачи

- Неправильная скорость двигателя

- Мощность гидравлического насоса вне рабочего диапазона

- Температура охлаждающей жидкости ниже минимальной установленной точки для работы

- Удаленная остановка занята

- Оператор Shutdown занимается

- Дистанционный оператор Shutdown запускается

- Температура впускного коллектора дизельного двигателя за пределами калибровочного диапазона

- Неправильное отключение панели.

Возможные причины NewCtrl включают:

- Скорость двигателя **не** в пределах 1570-1980 об/мин

- Передача в нейтральном режиме (при оснащении электронной передачей)

- PLC Setpoint UseTransGear неправильно установлен

- Низкое давление впускного газа

- LowGasPressIn Alarm сработала более 10 раз

- Температура охлаждения < 71°C

- Скорость двигателя более 2100 об/мин

- Загрузка двигателя слишком высока для работы с двойным топливом (более 94% от номинальной мощности)

- Загрузка двигателя **не** в пределах установленного предела (2250 л.с.): 373-1578 кВт, 2500 л.с.: 373-1748 кВт

- Любые сигналы тревоги (Sensor Fail)

- IMT (температура впуска коллектора) **не** в пределах установленного предела (43°C - 82°C)

- Оператор или удаленный SD

- Количество стукательных событий превысило установленный предел (100 раз в день / цикл питания)

| Код сообщения | Причина | Последствия |
|---|---|---|
| DF Не готов | Существуют условия, препятствующие двойному использованию топлива. | Панель управления не позволит блоку работать в режиме двойного топлива. |

![[05m00181.png]]

Рисунок 1, контроллер Legacy (LegCtrl, показан слева) и новый контроллер (NewCtrl, показан справа)

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Определить конфигурацию ComAp. |  |
|  | **ШАГ 1А.** Определить конфигурацию | Насос оснащен LegCtrl? |
| ШАГ 2. | Проверить сообщение о вине. |  |
|  | **Сообщение об ошибке 2А.** Активно. | Модуль управления в состоянии неисправности с DF Не готов? |
|  | **STEP 2B.** Перезагрузить панель управления. | DF **Не** Готовы к отображению на дисплее панели управления после перезапуска? |
| ШАГ 3. | Проверьте мощность гидравлического насоса. |  |
|  | **STEP 3A.** Проверить мощность гидравлического насоса. | Мощность гидравлического насоса более 373 кВт, но менее 1578 кВт для двигателей мощностью 2250 л.с. или 1748 кВт для двигателей мощностью 2500 л.с. |
| ШАГ 4. | Проверить температуру коллектора. |  |
|  | **STEP 4A.** Проверить температуру коллектора впуска. | Температура коллектора при впуске между 43°C \[110°F \] и 82°C \[180°F \]? |
| ШАГ 5. | Проверьте скорость двигателя. |  |
|  | **STEP 5A.** Проверить скорость двигателя. | Скорость двигателя между 1400 и 2000 об/мин более 60 секунд? |
| ШАГ 6. | Проверить температуру охлаждающей жидкости. |  |
|  | **STEP 6A.** Проверить температуру охлаждающей жидкости. | Температура охлаждающей жидкости более 71 ° C \[160°F \] в течение более 3 секунд? |
| ШАГ 7. | Проверяйте аварийные остановки и удаленные остановки. |  |
|  | **STEP 7A.** Закрытая работа. | Закрытие оператора включено? |
|  | **STEP 7B.** Закрытое удаленное управление. | Занята отключение удаленного оператора? |
|  | **STEP 7C.** Удаленная остановка включена. | Удалённо прекратить помолвку? |
| ШАГ 8. | Проверьте выбор передач. |  |
|  | **STEP 8A.** Проверить выбор передач. | Передача на передаче более 60 секунд? |
| ШАГ 9. | Проверьте на ошибки. |  |
|  | **STEP 9A.** Проверить коды ошибок Cummins® ECM. | Двигатель ECM указывает коды неисправностей? |
|  | **СТЭП 9В.** Проверка сообщений о неисправностях. | DF **Не** Готовый код сигнализации? |
|  | **STEP 9C.** Проверка сообщений о неисправностях. | Коды сигнализации, кроме DF **Не** Готовы? |
| ШАГ 10. | Проверьте скорость двигателя. |  |
|  | **STEP 10A.** Проверить скорость двигателя. | Скорость двигателя между 1570-1980 оборотами в минуту более 60 секунд? |
| ШАГ 11. | Проверьте выбор передач. |  |
|  | **STEP 11A.** Проверить выбор передач. | TransReqGear больше 0 дольше 60 секунд |
| ШАГ 12. | Неправильная настройка регулируемых параметров. |  |
|  | **STEP 12A.** Проверить тип передачи. | Используете трансмиссионный тип трансмиссии TransGear? |
| ШАГ 13. | Проверить температуру коллектора. |  |
|  | **STEP 13A.** Проверить температуру коллектора впуска. | Температура коллектора при впуске между 43°C \[110°F \] и 82°C \[180°F \]? |
| ШАГ 14. | Проверьте температуру охлаждающей жидкости двигателя. |  |
|  | **STEP 14A.** Проверить температуру охлаждающей жидкости двигателя. | Температура охлаждающей жидкости более 71 ° C \[160°F \] в течение более 3 секунд? |
| ШАГ 15. | Загрузка двигателя **не** в пределах установленного предела. |  |
|  | **STEP 15A.** Проверить тип ограничения нагрузки двигателя. | Pump использует сообщение Real Power на J1939 |
|  | 15B. Проверить значение передаваемой реальной мощности (J1939). | Соответствуют ли ограничения мощности, передаваемые J1939, номинальной мощности насоса? |
|  | **STEP 15C** Проверить ограничения нагрузки двигателя (Перевернуто). | Соответствуют ли ограничения мощности рейтингу мощности двигателя? |

### ШАГ 1. Определить конфигурацию ComAp.

#### ШАГ 1A. Определить конфигурацию ComAp.

| **Условия:** Проверить конфигурацию панели управления ComAp. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Определите, какая панель управления ComAp установлена на насосе. См. идентификационные изображения панели в обзоре кода тревоги. | Насос оснащен LegCtrl? *Да | 2А |
| Насос оснащен LegCtrl? **НЕТ** | 9а |  |

### ШАГ 2. Проверить сообщение о вине.

#### ШАГ 2A. Сообщение об ошибке является активным.

| **Условия:** Включить модуль управления двойным топливом. Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте локальную панель дисплея на наличие сообщения о неисправности. Навигация по неисправности с экрана дисплея. | Модуль управления в состоянии неисправности с DF **Не готов? *Да** | 2В |
| Модуль управления в состоянии неисправности с DF **Не готов? **Норэпэр: Не требуется устранение неполадок. | Ремонт завершён |  |

#### ШАГ 2B. Перезагрузите панель управления.

| **Условия:** Выключите панель управления на выключателе питания на передней панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подождите 30 секунд, включите панель управления. | DF **Не** Готовы к отображению на дисплее панели управления после перезапуска? *Да | 3А |
| DF **Не** Готовы к отображению на дисплее панели управления после перезапуска? **Норвегия:** Нет. Перезапуск панели управления устранил любые неактивные неисправности, не допускающие потока газа. | Ремонт завершён |  |

### ШАГ 3. Проверьте мощность гидравлического насоса.

#### ШАГ 3A. Проверьте мощность гидравлического насоса.

| **Условия:** Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте мощность гидравлического насоса на дисплее панели управления. | Гидравлический насос мощностью более 373 кВт, но менее 1578 кВт для двигателей мощностью 2250 л.с. или 1748 кВт для двигателей мощностью 2500 л.с. *Да | 4А |
| Мощность гидравлического насоса более 373 кВт, но менее 1578 кВт для двигателей мощностью 2250 л.с. или 1748 кВт для двигателей мощностью 2500 л.с. **NORepair:** Позволяет гидравлическому насосу достигать рабочего диапазона. | Ремонт завершён |  |

### ШАГ 4. Проверить температуру коллектора.

#### ШАГ 4A. Проверить температуру коллектора.

| **Условия:** Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить температуру впускного коллектора на дисплее панели управления. | Температура коллектора впуска между 43 ° C \[110 ° F \] и 82 ° C \[180 ° F \]? *Да | 5а |
| Температура коллектора впуска между 43 ° C \[110 ° F \] и 82 ° C \[180 ° F \]? **NORepair:** Позволяет температуре впускного коллектора достигать температурных пределов. | Ремонт завершён |  |

### ШАГ 5. Проверьте скорость двигателя.

#### ШАГ 5A. Проверьте скорость двигателя.

| **Условия:** Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте скорость двигателя на дисплее панели управления. | Скорость двигателя между 1400 и 2000 об/мин более 60 секунд? *Да | 6А |
| Скорость двигателя между 1400 и 2000 об/мин более 60 секунд? **NORepair:** Позволяет двигателю работать от 1400 до 2000 об/мин в течение более 60 секунд. | Ремонт завершён |  |

### ШАГ 6. Проверить температуру охлаждающей жидкости.

#### ШАГ 6A. Проверить температуру охлаждающей жидкости.

| **Условия:** Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте температуру охлаждающей жидкости двигателя на дисплее панели управления. | Температура охлаждающей жидкости более 71 ° C \[160 ° F \] в течение более 3 секунд? *Да | 7А |
| Температура охлаждающей жидкости более 71 ° C \[160 ° F \] в течение более 3 секунд? **NORepair:** Позволяет температуре охлаждающей жидкости достичь минимального предела. | Ремонт завершён |  |

### ШАГ 7. Проверяйте аварийные остановки и удаленные остановки.

#### ШАГ 7A. Оператор отключен.

| **Условия:** Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте состояние отключения оператора на дисплее панели управления. | Закрытие оператора включено? **Ремонт:** Перезагрузка. | Ремонт завершён |
| Закрытие оператора включено? **НЕТ** | 7B |  |

#### ШАГ 7B. Дистанционный оператор Shutdown.

| **Условия:** Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте состояние отключения оператора на дисплее панели управления. | Занята отключение удаленного оператора? **Ремонт:** Перезагрузка. | Ремонт завершён |
| Занята отключение удаленного оператора? **НЕТ** | 7C |  |

#### ШАГ 7C. Дистанционная остановка включена.

| **Условия:** Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте состояние удаленной остановки на дисплее панели управления. | Удалённо прекратить помолвку? **Ремонт:** Сброс удаленной остановки. | Ремонт завершён |
| Удалённо прекратить помолвку? **НЕТ** | 8а |  |

### ШАГ 8. Проверьте выбор передач.

#### ШАГ 8A. Проверьте выбор передач.

| **Условия:** Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить состояние передачи. | Передача на передаче более 60 секунд? *Да | Свяжитесь с авторизованным местом ремонта Cummins® |
| Передача на передаче более 60 секунд? **NORepair:** Запуск передачи на передаче более 60 секунд. | Ремонт завершён |  |

### ШАГ 9. Проверьте на ошибки.

#### ШАГ 9A. Проверьте ECM двигателя на наличие кодов неисправностей двигателя.

| **Условия:** Включить переключатель зажигания. Подключите рекомендуемый электронный сервисный инструмент Cummins® или его эквивалент. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте рекомендованную электронную сервисную инструментальную программу Cummins® или эквивалентную для считывания кода ошибки. | Двигатель ECM указывает коды неисправностей? *Да | Устранение неисправностей двигателя перед устранением неисправностей кодов сигнализации. |
| Двигатель ECM указывает коды неисправностей? **НЕТ** | 9В |  |

#### ШАГ 9B. Просмотреть сообщение (сообщения) о неисправности.

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте локальную панель дисплея или InteliMonitor на наличие сообщений о неисправности в списке тревоги и истории. | DF **Not** Готовый код тревоги присутствует? *Да | 9С |
| DF **Not** Готовый код тревоги присутствует? **НЕТ** | Верните насос в эксплуатацию и на монитор. |  |

#### ШАГ 9C. Просмотреть сообщение (сообщения) о неисправности.

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте локальную панель дисплея или InteliMonitor на наличие сообщений о неисправности в списке тревоги и истории. | Коды сигнализации, кроме DF **Не** Готовы? *Да** | Устранение неполадок во всех других кодах ошибок до устранения неполадок DF **Not Ready. |
| Коды сигнализации, кроме DF **Не** Готовы? **НЕТ** | 10А |  |

### ШАГ 10. Проверьте скорость двигателя.

#### ШАГ 10A. Проверьте скорость двигателя.

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. Подключите рекомендуемый электронный сервисный инструмент Cummins® или его эквивалент. Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте рекомендованную электронную сервисную инструментальную установку Cummins® или эквивалентную для проверки скорости двигателя по значению соответствия двигателя, отображаемому в InteliMonitor. | Скорость двигателя между 1570-1980 оборотами в обоих модулях более 60 секунд? *Да | 11А |
| Скорость двигателя между 1570-1980 оборотами в обоих модулях более 60 секунд? **NORepair:** Позволяет двигателю работать в диапазоне 1570-1980 оборотов в минуту в течение более 60 секунд и проверяет работу DF. | Ремонт завершён |  |

### ШАГ 11. Проверьте выбор передач.

#### ШАГ 11A. Проверьте выбор передач.

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Монитор TransReqGear в программном обеспечении Intellimonitor или на локальной панели дисплея. Если значение-ECU-TransReqGear = \#, то заданная точка в 12A (UseTransGear) должна быть 0. | TransReqGear больше 0 дольше 60 секунд *Да | 12А |
| TransReqGear больше 0 дольше 60 секунд **NORepair:** Запускайте передачу на передаче более 60 секунд и проверяйте работу DF. | Ремонт завершён |  |

### ШАГ 12. Неправильная настройка регулируемых параметров.

#### ШАГ 12A. Проверьте тип передачи.

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствие типа передачи UseTransGear на насосе. Для механической коробки передач оборудованный насос UseTransGear **должен** быть 0. Для электронной передачи использования TransGear **должен** быть 1. Если значение-ECU-TransReqGear = \#, то заданная точка в 12A (UseTransGear) должна быть 0. | Используете трансмиссионный тип трансмиссии TransGear? *Да | 13А |
| Используете трансмиссионный тип трансмиссии TransGear? **NORepair:** Настройте UseTransGear на соответствующую стоимость и проверьте работу DF. Для этого требуется пароль уровня 2. | Ремонт завершён |  |

### ШАГ 13. Проверить температуру коллектора.

#### ШАГ 13A. Проверить температуру (температурные) коллектора впуска.

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. Подключите рекомендуемый электронный сервисный инструмент Cummins® или его эквивалент. Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте рекомендованную электронную сервисную оснастку Cummins® или эквивалентную для проверки температуры впускного коллектора по значениям соответствия двигателя, отображаемым в InteliMonitor. После того, как температура коллектора (-ов) потребления превысила 82 ° C \[ 180° F \], они **должны **опуститься ниже 79 ° C \[ 174 ° F \] для того, чтобы DF был восстановлен. | Температура коллектора (температуры) впуска между 43°C \[110°F \] и 82°C \[180°F \] в обоих модулях? *Да | 14А |
| Температура коллектора впуска между 43 ° C \[110°F \] и 82 ° C \[180°F \] в обоих модулях? **NORepair:** Работайте с двигателем с температурой впускного коллектора в безопасном диапазоне и проверяйте работу DF. | Ремонт завершён |  |

### ШАГ 14. Проверьте температуру охлаждающей жидкости двигателя.

#### ШАГ 14A. Проверьте температуру охлаждающей жидкости двигателя.

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. Подключите рекомендуемый электронный сервисный инструмент Cummins® или его эквивалент. Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте рекомендованную электронную сервисную оснастку Cummins® или эквивалент для проверки значения температуры охлаждающей жидкости на основе значений соответствия двигателя, отображаемых в InteliMonitor. | Температура охлаждающей жидкости двигателя более 71 ° C \[160°F \] в течение более 3 секунд в обоих модулях? *Да | 15А |
| Температура охлаждающей жидкости двигателя более 71 ° C \[160°F \] в течение более 3 секунд в обоих модулях? **NORepair:** Управляйте двигателем, позволяйте температуре охлаждающей жидкости достигать минимального предела и проверяйте работу DF. | Ремонт завершён |  |

### ШАГ 15. Загрузка двигателя **не** в пределах установленного предела.

#### ШАГ 15A. Проверьте источник мощности двигателя.

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте источник питания в PLC Monitor. (Переведено в J1939). | Pump использует сообщение Real Power на J1939 *Да | 15В |
| Pump использует сообщение Real Power на J1939 **НЕТ** | 15С |  |

#### ШАГ 15B. Проверка реального значения передаваемой мощности (J1939)

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. Подключите рекомендуемый электронный сервисный инструмент Cummins® или его эквивалент. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Значение монитора для Real Power, передаваемого через J1939 на экране IV5 7 OR IMON – ECU – Pwr-Real R. Проверка двигателя работает в пределах мощности. (двигатель мощностью 2250 л.с. 373-1578 кВт) (2500 л.с.: 373-1748 кВт) Если присутствует как вход 4-20ma, так и сообщение J1939, сообщение J1939 принимает приоритет и управление игнорирует преобразованный сигнал. Все ограничения должны быть в одном диапазоне. | Соответствуют ли ограничения мощности, передаваемые J1939, номинальной мощности насоса? *Да | Верните насос в эксплуатацию и на монитор. |
| Соответствуют ли ограничения мощности, передаваемые J1939, номинальной мощности насоса? **NORepair:** Для насоса с реальной мощностью J1939: Подключите рекомендованный инструмент электронного обслуживания Cummins® или эквивалент и убедитесь, что рейтинг мощности, передаваемый через ECM, является правильным. Если значение не соответствует OEM, то OEM или клиент должен исправить это значение. | Устранение неполадок OEM. |  |

#### ШАГ 15C. Проверьте ограничения нагрузки двигателя (конвертированный).

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. Подключите рекомендуемый электронный сервисный инструмент Cummins® или его эквивалент. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните значение, которое OEM передает для соответствия машинному HP значениям, указанным в IMON -Analog CU - FracPumpHP. OEM посылает линейный сигнал в 4-20 мА, соответствующий 0-2500 л.с. (на основе рейтинга двигателя). | Соответствуют ли ограничения мощности рейтингу мощности насоса? *Да | Проверьте работу DF, верните насос в эксплуатацию и проверьте. |
| Соответствуют ли ограничения мощности рейтингу мощности насоса? **NORepair:** Для насосов с переоборудованными ограничениями мощности: Используя DMM, убедитесь, что сигнал оценки мощности на BF1-A2 правильный. Если значение не соответствует OEM, то OEM или клиент должен исправить это значение. Если значение от OEM правильно и ошибка сохраняется, замените модуль IBF. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> Unit will **not** go into dual fuel mode.
>
> ### How To Use This Tree
>
> This tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending up the symptom.
>
> LegCtrl-
>
> **Circuit Description**
>
> DF **Not** Ready is a STATUS message to indicate one of the conditions necessary for Dual Fuel operation has **not** been satisfied. In this state, the panel will **not** allow Gas operation.
>
> **Conditions for Running the Diagnostics**
>
> Anytime the control module is powered ON.
>
> **Conditions for Activating the Status Message:**
>
> See possible causes in the Shop Talk section.
>
> **Conditions for Clearing the Status Message Automatically:**
>
> Satisfy all conditions to start dual fuel operation.
>
> **Conditions for Clearing the Status Message Manually:**
>
> None.
>
> NewCtrl-
>
> **Circuit Description**
>
> DF **Not** Ready message is displayed on the Newctr and InteliMonitor alarm list.
>
> **Conditions for Running the Diagnostics**
>
> Anytime the control module is powered ON.
>
> **Conditions for Activating the Status Message:**
>
> See possible causes in the Shop Talk section.
>
> **Conditions for Clearing the Status Message Automatically:**
>
> Satisfy all conditions to start dual fuel operation.
>
> **Conditions for Clearing the Status Message Manually:**
>
> ### Shoptalk
>
> Alarm is indicated when system is **not** ready for dual fuel operation due to several conditions (described in possible causes). Once all conditions are met, dual fuel operation will be enabled automatically.
>
> In case any other alarm/s is active at the same time as DF **Not** Ready, troubleshoot that alarm/s first.
>
> If NewCtrl: Information in InteliMonitor Tool - PLC Monitor - Sheet 5 can be used along with the troubleshooting tree.
>
> If the input on a particular error block has a white dot on the input and the line to the input is black you need to go to the troubleshooting step associated with that input. If there is **only** a black dot on the input and the input line is blue then go to the troubleshooting step associated with that input.
>
> LegCtrl possible causes include:
>
> - Transmission position
>
> - Incorrect engine speed
>
> - Hydraulic pump power outside of the operating range
>
> - Coolant temperature is below the minimum set point for operation
>
> - Remote Stop is engaged
>
> - Operator Shutdown is engaged
>
> - Remote Operator Shutdown is engaged
>
> - Diesel engine intake manifold temperature outside of the calibration range
>
> - Incorrect panel shutdown.
>
> NewCtrl possible causes include:
>
> - Engine speed **not** within 1570-1980 rpm
>
> - Transmission in neutral (if equipped with electronic transmission)
>
> - PLC Setpoint UseTransGear incorrectly set
>
> - Low inlet gas pressure
>
> - LowGasPressIn Alarm has occurred greater than 10 times
>
> - Coolant temperature \< 71°C
>
> - Engine overspeed greater than 2100 rpm
>
> - Engine load too high for Dual fuel operation (greater than 94% of Rated power)
>
> - Engine load **not** within set limit (2250 hp: 373-1578 kW, 2500 hp: 373-1748 kW)
>
> - Any Fls (Sensor Fail) Alarms
>
> - IMT (Intake Manifold Temperatures) **not** within set limit (43°C to 82°C)
>
> - Any Operator or Remote SD
>
> - Number of Knocking events exceeded set limit (100 times per day/power cycle)
>
> | Code of Message | Reason | Effect |
> |---|---|---|
> | DF **Not** Ready | Conditions exist preventing dual fuel operation. | The control panel will prevent the unit from running in dual fuel mode. |
>
> Figure 1, Legacy controller (LegCtrl, shown left) and new controller (NewCtrl, shown right)
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Determine ComAp configuration. |  |
> |  | **STEP 1A.** Determine configuration | Pump equipped with LegCtrl? |
> | STEP 2. | Validate the fault message. |  |
> |  | **STEP 2A.** Fault message is active. | Control module in fault condition with DF **Not** Ready? |
> |  | **STEP 2B.** Restart the control panel. | DF **Not** Ready displayed on the control panel display after restart? |
> | STEP 3. | Verify hydraulic pump power. |  |
> |  | **STEP 3A.** Verify hydraulic pump power. | Hydraulic pump power greater than 373 kW but less than 1578 kW for 2250 HP engines or 1748 kW for 2500 HP engines? |
> | STEP 4. | Verify intake manifold temperature. |  |
> |  | **STEP 4A.** Verify intake manifold temperature. | Intake manifold temperature between 43°C \[ 110°F \] and 82°C \[ 180°F \]? |
> | STEP 5. | Verify engine speed. |  |
> |  | **STEP 5A.** Verify engine speed. | Engine speed between 1400 and 2000 rpm for longer than 60 seconds? |
> | STEP 6. | Verify coolant temperature. |  |
> |  | **STEP 6A.** Verify coolant temperature. | Coolant temperature greater than 71°C \[ 160°F \] for longer than 3 seconds? |
> | STEP 7. | Check emergency stops and remote stops. |  |
> |  | **STEP 7A.** Operate shutdown engaged. | Operator shutdown engaged? |
> |  | **STEP 7B.** Remote Operator Shutdown is engaged. | Remote operator shutdown engaged? |
> |  | **STEP 7C.** Remote Stop is engaged. | Remote stop engaged? |
> | STEP 8. | Check transmission gear selection. |  |
> |  | **STEP 8A.** Check transmission gear selection. | Transmission in gear for longer than 60 seconds? |
> | STEP 9. | Check for errors. |  |
> |  | **STEP 9A.** Check for Cummins® ECM Fault Codes. | Engine ECM indicates fault codes? |
> |  | **STEP 9B.** Check for fault messages. | DF **Not** Ready alarm code present? |
> |  | **STEP 9C.** Check for fault messages. | Alarm codes other than DF **Not** Ready present? |
> | STEP 10. | Verify engine speed. |  |
> |  | **STEP 10A.** Verify engine speed. | Engine speed between 1570-1980 rpm for longer than 60 seconds? |
> | STEP 11. | Check transmission gear selection. |  |
> |  | **STEP 11A.** Check transmission gear selection. | TransReqGear greater than 0 for longer than 60 seconds? |
> | STEP 12. | Incorrect adjustable parameter setting. |  |
> |  | **STEP 12A.** Check transmission type selection. | UseTransGear matches transmission type? |
> | STEP 13. | Verify intake manifold temperature. |  |
> |  | **STEP 13A.** Verify intake manifold temperature. | Intake manifold temperature between 43°C \[ 110°F \] and 82°C \[ 180°F \]? |
> | STEP 14. | Verify engine coolant temperature. |  |
> |  | **STEP 14A.** Verify engine coolant temperature. | Coolant temperature greater than 71°C \[ 160°F \] for longer than 3 seconds? |
> | STEP 15. | Engine load **not** within set limit. |  |
> |  | **STEP 15A.** Verify engine load limit type. | Pump using Real Power message via J1939? |
> |  | **STEP 15B.** Verify Real Power transmitted value (J1939). | Do J1939 transmitted power limits correspond with pump power rating? |
> |  | **STEP 15C.** Verify engine load limits (Converted). | Do Power Limits correspond with engine power rating? |
>
> ### STEP 1. Determine ComAp configuration.
>
> #### STEP 1A. Determine ComAp configuration.
>
> | **Conditions:** Verify ComAp control panel configuration. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Determine which ComAp control panel is installed on the pump. Refer to panel identification images in alarm code overview. | Pump equipped with LegCtrl? **YES** | 2A |
> | Pump equipped with LegCtrl? **NO** | 9A |  |
>
> ### STEP 2. Validate the fault message.
>
> #### STEP 2A. Fault message is active.
>
> | **Conditions:** Turn dual fuel control module ON. Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the local display panel for a fault message. Navigate to the fault from the display screen. | Control module in fault condition with DF **Not** Ready? **YES** | 2B |
> | Control module in fault condition with DF **Not** Ready? **NORepair:** No troubleshooting needed. | Repair complete |  |
>
> #### STEP 2B. Restart the control panel.
>
> | **Conditions:** Turn control panel off at the power switch on the front panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Wait 30 seconds Turn the control panel ON. | DF **Not** Ready displayed on the control panel display after restart? **YES** | 3A |
> | DF **Not** Ready displayed on the control panel display after restart? **NORepair:** None. Restarting the control panel removed any inactive faults **not** allowing gas flow. | Repair complete |  |
>
> ### STEP 3. Verify hydraulic pump power.
>
> #### STEP 3A. Verify hydraulic pump power.
>
> | **Conditions:** Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify hydraulic pump power on the control panel display. | Hydraulic pump power greater than 373kW but less than 1578 kW for 2250 HP engines or 1748 kW for 2500 HP engines? **YES** | 4A |
> | Hydraulic pump power greater than 373 kW but less than 1578 kW for 2250 HP engines or 1748 kW for 2500 HP engines? **NORepair:** Allow hydraulic pump power to reach operation range. | Repair complete |  |
>
> ### STEP 4. Verify intake manifold temperature.
>
> #### STEP 4A. Verify intake manifold temperature.
>
> | **Conditions:** Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify intake manifold temperature on the control panel display. | Intake manifold temperature between 43°C \[110 °F\] and 82°C \[180 °F\]? **YES** | 5A |
> | Intake manifold temperature between 43°C \[110 °F\] and 82°C \[180 °F\]? **NORepair:** Allow the intake manifold temperature reach the temperature limits. | Repair complete |  |
>
> ### STEP 5. Verify engine speed.
>
> #### STEP 5A. Verify engine speed.
>
> | **Conditions:** Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify engine speed on the control panel display. | Engine speed between 1400 and 2000 rpm for longer than 60 seconds? **YES** | 6A |
> | Engine speed between 1400 and 2000 rpm for longer than 60 seconds? **NORepair:** Allow engine to operate between 1400 and 2000 rpm for longer than 60 seconds. | Repair complete |  |
>
> ### STEP 6. Verify coolant temperature.
>
> #### STEP 6A. Verify coolant temperature.
>
> | **Conditions:** Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify engine coolant temperature on the control panel display. | Coolant temperature greater than 71°C \[160 °F\] for longer than 3 seconds? **YES** | 7A |
> | Coolant temperature greater than 71°C \[160 °F\] for longer than 3 seconds? **NORepair:** Allow the coolant temperature to reach the minimum limit. | Repair complete |  |
>
> ### STEP 7. Check emergency stops and remote stops.
>
> #### STEP 7A. Operator shutdown engaged.
>
> | **Conditions:** Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the operator shutdown status on the control panel display. | Operator shutdown engaged? **YESRepair:** Reset the shutdown. | Repair complete |
> | Operator shutdown engaged? **NO** | 7B |  |
>
> #### STEP 7B. Remote Operator Shutdown is engaged.
>
> | **Conditions:** Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the operator shutdown status on the control panel display. | Remote operator shutdown engaged? **YESRepair:** Reset the shutdown. | Repair complete |
> | Remote operator shutdown engaged? **NO** | 7C |  |
>
> #### STEP 7C. Remote Stop is engaged.
>
> | **Conditions:** Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote stop status on the control panel display. | Remote stop engaged? **YESRepair:** Reset the remote stop. | Repair complete |
> | Remote stop engaged? **NO** | 8A |  |
>
> ### STEP 8. Check transmission gear selection.
>
> #### STEP 8A. Check transmission gear selection.
>
> | **Conditions:** Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify the transmission status. | Transmission in gear for longer than 60 seconds? **YES** | Contact a Cummins® Authorized Repair Location |
> | Transmission in gear for longer than 60 seconds? **NORepair:** Run the transmission in gear for more than 60 seconds. | Repair complete |  |
>
> ### STEP 9. Check for errors.
>
> #### STEP 9A. Check the engine ECM for engine fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect the recommended Cummins® electronic service tool or equivalent. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use the recommended Cummins® electronic service tool or equivalent to read the fault code. | Engine ECM indicates fault codes? **YES** | Troubleshoot engine fault codes prior to Troubleshooting Alarm Codes. |
> | Engine ECM indicates fault codes? **NO** | 9B |  |
>
> #### STEP 9B. Review the fault message(s).
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check local display panel or InteliMonitor for fault messages in alarm list and history. | DF **Not** Ready alarm code is present? **YES** | 9C |
> | DF **Not** Ready alarm code is present? **NO** | Return the pump to service and monitor. |  |
>
> #### STEP 9C. Review the fault message(s).
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check local display panel or InteliMonitor for fault messages in alarm list and history. | Alarm codes other than DF **Not** Ready present? **YES** | Troubleshoot all other error codes prior to troubleshooting DF **Not** Ready. |
> | Alarm codes other than DF **Not** Ready present? **NO** | 10A |  |
>
> ### STEP 10. Verify engine speed.
>
> #### STEP 10A. Verify engine speed.
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent. Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use the recommended Cummins® electronic service tool or equivalent to verify engine speed from engine matches value displayed in InteliMonitor. | Engine speed between 1570-1980 rpm in both modules for longer than 60 seconds? **YES** | 11A |
> | Engine speed between 1570-1980 rpm in both modules for longer than 60 seconds? **NORepair:** Allow engine to operate between 1570-1980 rpm for longer than 60 seconds and verify DF operation. | Repair complete |  |
>
> ### STEP 11. Check transmission gear selection.
>
> #### STEP 11A. Check transmission gear selection.
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Monitor TransReqGear in Intellimonitor Software or on local display panel. If Value-ECU-TransReqGear = \#, the setpoint in 12A (UseTransGear) needs to be 0. | TransReqGear greater than 0 for longer than 60 seconds? **YES** | 12A |
> | TransReqGear greater than 0 for longer than 60 seconds? **NORepair:** Run the transmission in gear for more than 60 seconds and verify DF operation. | Repair complete |  |
>
> ### STEP 12. Incorrect adjustable parameter setting.
>
> #### STEP 12A. Check transmission type selection.
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify UseTransGear matches transmission type on pump. For a manual transmission equipped pump UseTransGear **must** be 0. For electronic Transmission UseTransGear **must** be 1. If Value-ECU-TransReqGear = \#, the setpoint in 12A (UseTransGear) needs to be 0. | UseTransGear matches transmission type? **YES** | 13A |
> | UseTransGear matches transmission type? **NORepair:** Set UseTransGear to appropriate value and verify DF operation. This requires a level 2 password. | Repair complete |  |
>
> ### STEP 13. Verify intake manifold temperature.
>
> #### STEP 13A. Verify intake manifold temperature(s).
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent. Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use the recommended Cummins® electronic service tool or equivalent to verify intake manifold temperatures from engine match values displayed in InteliMonitor. Once intake manifold temperature(s) have exceeded 82°C \[ 180°F \] they **must** drop below 79°C \[ 174°F \] in order for DF to be reenabled. | Intake manifold temperature(s) between 43°C \[ 110°F \] and 82°C \[ 180°F \] in both modules? **YES** | 14A |
> | Intake manifold temperature between 43°C \[ 110°F \] and 82°C \[ 180°F \] in both modules? **NORepair:** Operate engine with intake manifold temperatures within safe range and verify DF operation. | Repair complete |  |
>
> ### STEP 14. Verify engine coolant temperature.
>
> #### STEP 14A. Verify engine coolant temperature.
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent. Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use the recommended Cummins® electronic service tool or equivalent to verify coolant temperature value from engine match values displayed in InteliMonitor. | Engine coolant temperature greater than 71°C \[ 160°F \] for longer than 3 seconds in both modules? **YES** | 15A |
> | Engine coolant temperature greater than 71°C \[ 160°F \] for longer than 3 seconds in both modules? **NORepair:** Operate engine, allow the coolant temperature to reach the minimum limit and verify DF operation. | Repair complete |  |
>
> ### STEP 15. Engine load **not** within set limit.
>
> #### STEP 15A. Verify source for engine power value.
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify power source in PLC Monitor. (Converted or J1939). | Pump using Real Power message via J1939? **YES** | 15B |
> | Pump using Real Power message via J1939? **NO** | 15C |  |
>
> #### STEP 15B. Verify Real Power transmitted value (J1939).
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Monitor value for Real Power transmitted via J1939 on IV5 screen 7 OR IMON – ECU – Pwr-Real R. Verify engine is operating within power limits. (2250 HP engine 373-1578 kW) (2500 HP engine: 373-1748 kW) If both 4-20ma input and J1939 message are present, the J1939 message takes priority and control ignores the converted signal. All limits should still be in the same range. | Do J1939 transmitted power limits correspond with pump power rating? **YES** | Return the pump to service and monitor. |
> | Do J1939 transmitted power limits correspond with pump power rating? **NORepair:** For pump with J1939 Real Power Value: Connect the recommended Cummins® electronic service tool or equivalent and verify that power rating transmitted through the ECM is correct. If value is incorrect from the OEM, then the OEM or customer needs to correct this value. | Refer to OEM troubleshooting. |  |
>
> #### STEP 15C. Verify engine load limits (Converted).
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the value the OEM is transmitting for Engine HP matches value read in IMON -Analog CU - FracPumpHP. OEM sends linear signal as 4-20 mA corresponding to 0-2500 HP (based on engine rating). | Do power limits correspond with pump power rating? **YES** | Verify DF Operation, return pump to service and monitor. |
> | Do power limits correspond with pump power rating? **NORepair:** For pumps with converted power limits: Using a DMM, verify that power rating signal on BF1-A2 is correct. If value is incorrect from the OEM, then the OEM or customer needs to correct this value. If value from OEM is correct and error persists replace IBF Module. | Repair complete |  |
