---
aliases:
  - "Цепь датчика температуры охлаждающей жидкости (CTS)"
type: "Процедура"
doc: "94-fc145"
title_en: "Coolant Temperature Sensor (CTS) Circuit"
title_ru: "Цепь датчика температуры охлаждающей жидкости (CTS)"
modified: "2003-03-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc145.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc145.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Coolant Temperature Sensor (CTS) Circuit
**Цепь датчика температуры охлаждающей жидкости (CTS)**

> [!abstract] Процедура · `94-fc145`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc145.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc145.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 145

### Цепь датчика температуры охлаждающей жидкости (CTS)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 145 PID (P): СПН: ФМИ: Лампа: СТО: 00-356 | Низкое напряжение, обнаруженное при температуре охлаждающей жидкости двигателя, сигнального контакта 14 проводов двигателя с жгутом электронного модуля управления (ECM) Connector. | Никакого влияния на производительность. Общий предупредительный выход активизируется. |

![[19a00009.png]]

### Описание цепи

CTS используется ECM для мониторинга температуры охлаждающей жидкости двигателя. Температура охлаждающей жидкости используется ECM для системы защиты двигателя и управления заправкой. ECM контролирует напряжение на контакте 14. ECM ожидает, что напряжение будет варьироваться между 32 и 4,69 ВДК. Если напряжение ниже 24 ВДК более 2 секунд, то ECM регистрирует код 145 по умолчанию. Напряжение ниже 24 VDC на контакте 14 может быть вызвано шортами, которые заземляются на проводах подачи или возврата или на внутренне заземленном датчике отказа.

### Расположение компонента

CTS расположен на стороне корпуса термостата.

### Практические замечания

Все датчики температуры

- Сопротивление датчика изменяется в зависимости от температуры. Считывание, которое вы наблюдаете, будет сравниваться со следующей таблицей, если датчик работает должным образом.

**Примечание: ** Высокие напряжения соответствуют низким температурам, а низкие напряжения соответствуют высоким температурам.

| температура | температура | Сопротивление |
|---|---|---|
| (°С) | (° F) | (Омс) |
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

## Предупреждения и меры предосторожности

> [!danger] ОПАСНО
>

** Подождите, пока температура охлаждающей жидкости не будет ниже 50°C \[120°F\], прежде чем удалять крышку радиатора системы охлаждающей жидкости или CTS. Неспособность сделать это может привести к травмам от нагреваемого спрея охлаждающей жидкости. **

> [!warning] ОСТОРОЖНО
>

** Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерения: Часть нет. 3822758 - пробный щуп типа пробки Deutsch/Cannon/Metri-Pack Номер детали. 3823256 - Испытательный щуп с разъемом Metri-Pack 2.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте CTS. |  |
|  | **STEP 1A.** Проверить проводку жгута и контакты разъема датчика. | Никаких поврежденных контактов |
|  | **ШАГ 1В.** Проверить сопротивление СТС. | 600 Ом до 36к Ом См. таблицу температуры/сопротивления в практическом примечании для правильного значения. |
|  | **STEP 1C** Проверьте короткое замыкание на земле в датчике. | Более 100 тыс. ом |
| ШАГ 2. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 2A.** Проверить кабель адаптера ремня электропитания двигателя и контакты разъема ECM. | Никаких поврежденных контактов |
|  | **STEP 2A-1.** Осмотрите упряжку для проводов двигателя и удлинительный кабель (кабели) удлинителя проводов двигателя. | Никаких поврежденных контактов |
|  | **ШАГ 2В.** Проверьте короткое замыкание сигнала и верните штифты во все остальные штифты. | Более 100 тыс. ом |
|  | **STEP 2B-1.** Проверьте короткое замыкание сигнала и верните штифты во все остальные штифты. | Более 100 тыс. ом |
|  | **STEP 2C.** Проверьте короткое замыкание на землю в подаче и сигнальном проводе. | Более 100 тыс. ом |
|  | **STEP 2C-1.** Проверьте короткое замыкание на землю в подаче и сигнальном проводе. | Более 100 тыс. ом |
|  | **STEP 2D.** Проверьте наличие открытого сигнала и провода обратного сигнала. | Менее 10 Ом |
|  | **STEP 2D-1.** Проверьте наличие открытого в двигателе провода, адаптера жгута и любого используемого удлинителя жгута жгута. | Менее 10 Ом |
| ШАГ 3. | Очистите код ошибки. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код 145 неактивен |
|  | **STEP 3B.** Очистить коды неактивных ошибок. | Все ошибки устранены |

### ШАГ 1. Проверьте CTS.

#### ШАГ 1A. Проверьте проводку и контакты разъёма датчика.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините жгут электропроводки двигателя от CTS. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты корродируют штифты влагой в или на разъеме отсутствует уплотнение разъема. | Никаких поврежденных контактов | 1В |
| ** Починить поврежденные контакты** Починить или заменить ремень электропроводки двигателя или CTS, в зависимости от того, какие контакты повреждены. Ремонт ремня электропроводки двигателя. См. процедуру 019-202 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить CTS. См. процедуру 019-019 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. Замените уплотнение разъема. | 3А |  |

#### ШАГ 1B. Проверьте сопротивление CTS.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините жгут электропроводки двигателя от CTS. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте сопротивление между двумя штифтами на стороне датчика разъема CTS. | 600 Ом до 36k Ом См. таблицу температуры/сопротивления в практическом примечании для правильного значения. | 1С |
| **Заменить CTS** См. процедуру 019-019 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

#### ШАГ 1C. Проверьте короткое замыкание, чтобы приземлиться в датчике.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините жгут электропроводки двигателя от CTS. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте сопротивление одного из штифтов на стороне датчика разъема CTS к заземлению блока двигателя. | Более 100 тыс. ом | 2А |
| **Заменить CTS** См. процедуру 019-019 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

### ШАГ 2. Проверьте жгут проводов двигателя.

#### ШАГ 2A. Проверьте кабель адаптера жгута двигателя и контакты разъема ECM.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2А-1-1 |
| ** Починить поврежденные контакты** Починить или заменить проводку двигателя на адаптерный кабель или ECM, в зависимости от того, какие контакты повреждены. Ремонт ремня электропроводки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить ECM. См. процедуры OEM. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. | 3А |  |

#### ШАГ 2A-1. Осмотрите контактные линзы удлинителя (расширителей) кабеля (коннекторов) уплотнительной проводов двигателя и упряжки двигателя.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от проводов двигателя удлинитель (ы) удлинителя (ов) упряжки. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2В |
| ** Починить поврежденные контакты** Починить или заменить упряжку для проводов двигателя или упряжку для расширительного кабеля (расширительных кабелей) упряжки двигателя, в зависимости от того, какие контакты повреждены. Ремонт ремня электропроводки двигателя или кабеля (расширяющих кабелей) ремня электропроводки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить ремень (или провода) расширительного кабеля (расширений) ремня (расширений) электропроводки двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. | 3А |  |

#### ШАГ 2B. Проверьте короткое замыкание сигнала и верните штифты ко всем другим штифтам.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините жгут электропроводки двигателя от CTS. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте сопротивление от контакта 14 проводов двигателя с помощью адаптера разъёма кабеля со всеми другими штифтами в разъеме. Измерьте сопротивление от контакта 15 проводов двигателя с адаптером разъёма кабеля к другим штифтам в разъеме. | Более 100 тыс. ом | 2C |
|  | 2В-1-1 |  |

#### ШАГ 2B-1. Проверьте короткое замыкание сигнала и верните штифты ко всем другим штифтам.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините проводку двигателя от проводов двигателя удлиняющие кабели. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте сопротивление контакта 14 проводов двигателя с помощью адаптера кабеля разъёма и любой проводов двигателя с помощью удлинителя кабеля, используемого для всех других контактов в разъеме. Измерьте сопротивление контакта 15 проводов двигателя с адаптерным кабелем разъёма и любой используемой проводов двигателя с удлинительным кабелем, ко всем другим штифтам в разъеме. | Более 100k Ом Ремонт или замена электропроводки двигателя Ремонт электропроводки двигателя ремня. См. процедуры 019-199 и 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |
| ** Починить или заменить кабель адаптера упряжки двигателя или кабель расширения упряжки двигателя, в зависимости от того, что признано неисправным** Починить адаптер упряжки двигателя или кабель расширения упряжки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените адаптерный кабель или кабель расширения (расширяющие кабели) ремня электропроводки двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

#### ШАГ 2C. Проверьте короткое замыкание, чтобы заземлиться в подаче и сигнальном проводе.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отключите электропроводку двигателя от CTS. Отсоедините проводку двигателя от адаптерного кабеля ECM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте сопротивление от контакта 14 проводов двигателя с адаптерным кабелем разъёма к заземлению блока двигателя. Измерьте сопротивление от контакта 15 проводов двигателя с адаптерным кабелем разъёма к заземлению блока двигателя. | Более 100 000 Ом заменяют CTS. См. процедуру 019-019 в Руководстве по устранению неполадок и ремонту QST System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |
|  | 2С-1 |  |

#### ШАГ 2C-1. Проверьте короткое замыкание, чтобы заземлиться в подаче и сигнальном проводе.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отключите электропроводку двигателя от CTS. Отсоедините проводку двигателя от проводов двигателя кабеля расширения. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте сопротивление от контакта 14 разъёма ремня электропроводки двигателя с заземлением блока двигателя. Измерьте сопротивление от контакта 15 разъёма ремня электропроводки двигателя с заземлением блока двигателя. | Более 100 000 Ом заменяют CTS. См. процедуру 019-019 в Руководстве по устранению неполадок и ремонту QST System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 2D |
| ** Ремонт или замена электропроводки двигателя ** Ремонт электропроводки двигателя ремня. См. процедуры 019-199 и 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

#### ШАГ 2D. Проверьте наличие открытого сигнала и обратных проводов.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отключите проводку двигателя от адаптера кабеля от ECM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте сопротивление от контакта 14 проводов двигателя с помощью адаптера ремня для контакта 15 разъема. | Менее 10 Ом | 3А |
|  | 2D-1 |  |

#### ШАГ 2D-1. Проверьте наличие открытого в двигателе провода, адаптерного кабеля и любого используемого удлинителя провода.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отключите проводку двигателя от адаптера кабеля от ECM. Отсоедините проводку двигателя от проводов двигателя кабеля расширения. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте непрерывность контакта 14 проводов двигателя с адаптерным кабелем и любым используемым удлинительным кабелем. Измерьте непрерывность контакта 15 проводов двигателя с адаптерным кабелем и любым используемым удлинительным кабелем. | Менее 10 Ом Ремонт или замена электропроводки двигателя Ремонт электропроводки двигателя ремня. См. Процедуры 019-202 и 019-240 в Руководстве по устранению неполадок и ремонту топливной системы QST серии QST30 G-Drive Engine, Бюллетень No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |
| ** Починить или заменить кабель адаптера упряжки двигателя или кабель расширения упряжки двигателя, в зависимости от того, что признано неисправным** Починить адаптер упряжки двигателя или кабель расширения упряжки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените адаптерный кабель или кабель расширения (расширяющие кабели) ремня электропроводки двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

### ШАГ 3. Очистите код ошибки.

#### ШАГ 3A. Отключите код неисправности.

| **Условия: ** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Соедините все компоненты. Запуск двигателя и холостость в течение одной минуты. | Код 145 неактивен | 3B |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 3B. Сбросьте неактивные коды неисправностей.

| **Условия: ** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Стирать неактивные коды неисправностей с помощью INSITETM, номер детали. 3825145. **Примечание:** Разъем шины данных CAN расположен на правом берегу корпуса маховика. | Все ошибки устранены | Ремонт завершён |
| **Устранение неполадок с оставшимися активными кодами ошибок.** | Соответствующая диаграмма устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 145
>
> ### Coolant Temperature Sensor (CTS) Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 145 PID(P): SPN: FMI: Lamp: SRT: 00-356 | Low voltage detected at engine coolant temperature sensor signal pin 14 of the engine harness Electronic Control Module (ECM) Connector. | No effect on performance. Common Warning output is energized. |
>
> ### Circuit Description
>
> The CTS is used by the ECM to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system and fueling control. The ECM monitors the voltage on pin 14. The ECM expects to see the voltage vary between.32 and 4.69 VDC. If the voltage is below.24 VDC for more than 2 seconds, then the ECM will log Fault Code 145. Voltage below.24 VDC on pin 14 can be caused by shorts to ground on the supply or return wires or an internally grounded failed sensor.
>
> ### Component Location
>
> The CTS is located on the side of the thermostat housing.
>
> ### Shoptalk
>
> All Temperature Sensors
>
> - The resistance of the sensor varies with the temperature. The reading that you observe will compare to the following table if the sensor is functioning properly.
>
> **NOTE:** High voltages correspond to low temperatures and low voltages correspond to high temperatures.
>
> | Temperature | Temperature | Resistance |
> |---|---|---|
> | (° C) | (° F) | (ohms) |
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> ## Warnings and Cautions
>
> **WARNING · Опасно**
>
> **Wait until the coolant temperature is below 50° C \[120° F\] before removing the coolant system pressure cap or the CTS. Failure to do so can cause personal injury from heated coolant spray.**
>
> **CAUTION · Осторожно**
>
> **To avoid pin and harness damage, use the following test leads when taking a measurement: Part No. 3822758 - male Deutsch/Cannon/Metri-Pack test lead Part No. 3823256 - Metri-Pack 2-way connector test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the CTS. |  |
> |  | **STEP 1A.** Inspect harness and sensor connector pins. | No damaged pins |
> |  | **STEP 1B.** Check the resistance of the CTS. | 600 ohms to 36k ohms See temperature/resistance table under shop talk for correct value. |
> |  | **STEP 1C.** Check for a short circuit to ground in the sensor. | More than 100k ohms |
> | STEP 2. | Check the engine harness. |  |
> |  | **STEP 2A.** Inspect the engine harness adaptor cable and the ECM connector pins. | No damaged pins |
> |  | **STEP 2A-1.** Inspect the engine harness and the engine harness extension cable(s). | No damaged pins |
> |  | **STEP 2B.** Check for a short circuit from the signal and return pins to all other pins. | More than 100k ohms |
> |  | **STEP 2B-1.** Check for a short circuit from the signal and return pins to all other pins. | More than 100k ohms |
> |  | **STEP 2C.** Check for a short circuit to ground in the supply and signal wire. | More than 100k ohms |
> |  | **STEP 2C-1.** Check for a short circuit to ground in the supply and signal wire. | More than 100k ohms |
> |  | **STEP 2D.** Check for an open in the signal and return wires. | Less than 10 ohms |
> |  | **STEP 2D-1.** Check for an open in the engine harness adaptor cable and any engine harness extension cable used. | Less than 10 ohms |
> | STEP 3. | Clear the fault code. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 145 inactive |
> |  | **STEP 3B.** Clear the inactive fault codes. | All faults cleared |
>
> ### STEP 1. Check the CTS.
>
> #### STEP 1A. Inspect the harness and the sensor connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the CTS. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector missing connector seal. | No damaged pins | 1B |
> | **Repair the damaged pins** Repair or replace the engine harness or the CTS, whichever has the damaged pins. Repair the engine harness. Refer to Procedure 019-202 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the CTS. Refer to Procedure 019-019 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Dry the connector by using electrical contact cleaner, Part No. 3824510. Replace the connector seal. | 3A |  |
>
> #### STEP 1B. Check the resistance of the CTS.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the CTS. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between the two pins on the sensor side of the CTS connector. | 600 ohms to 36k ohms See Temperature/Resistance Table under Shop Talk for correct value. | 1C |
> | **Replace the CTS** Refer to Procedure 019-019 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> #### STEP 1C. Check for a short circuit to ground in the sensor.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the CTS. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from one of the pins on the sensor side of the CTS connector to the engine block ground. | More than 100k ohms | 2A |
> | **Replace the CTS** Refer to Procedure 019-019 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> ### STEP 2. Check the engine harness.
>
> #### STEP 2A. Inspect the engine harness adaptor cable and the ECM connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-1 |
> | **Repair the damaged pins** Repair or replace the engine harness adaptor cable or the ECM, whichever has the damaged pins. Repair the engine harness. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the ECM. Refer to OEM procedures. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 3A |  |
>
> #### STEP 2A-1. Inspect the engine harness and the engine harness extension cable(s) connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cable(s). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2B |
> | **Repair the damaged pins** Repair or replace the engine harness or the engine harness expansion cable(s), whichever has the damaged pins. Repair the engine harness or the engine harness expansion cable(s). Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness or the engine harness expansion cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 3A |  |
>
> #### STEP 2B. Check for a short circuit from the signal and return pins to all other pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the CTS. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 14 of the engine harness adaptor cable connector to all other pins in the connector. Measure the resistance from pin 15 of the engine harness adaptor cable connector to all other pins in the connector. | More than 100k ohms | 2C |
> |  | 2B-1 |  |
>
> #### STEP 2B-1. Check for a short circuit from the signal and return pins to all other pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the engine harness extension cables. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance of pin 14 of the engine harness adaptor cable connector and any engine harness extension cable used, to all other pins in the connector. Measure the resistance of pin 15 of the engine harness adaptor cable connector and any engine harness extension cable used, to all other pins in the connector. | More than 100k ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-199 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |
> | **Repair or replace the engine harness adaptor cable or the engine harness expansion cable(s), whichever is found faulty** Repair the engine harness adaptor cable or the engine harness expansion cable(s). Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or the engine harness expansion cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> #### STEP 2C. Check for a short circuit to ground in the supply and signal wire.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect engine harness from CTS. Disconnect engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 14 of the engine harness adaptor cable connector to engine block ground. Measure the resistance from pin 15 of the engine harness adaptor cable connector to engine block ground. | More than 100k ohms Replace the CTS. Refer to Procedure 019-019 in the Troubleshooting and Repair Manual QST System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |
> |  | 2C-1 |  |
>
> #### STEP 2C-1. Check for a short circuit to ground in the supply and signal wire.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect engine harness from CTS. Disconnect engine harness from the engine harness expansion cable. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 14 of the engine harness connector to engine block ground. Measure the resistance from pin 15 of the engine harness connector to engine block ground. | More than 100k ohms Replace the CTS. Refer to Procedure 019-019 in the Troubleshooting and Repair Manual QST System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 2D |
> | **Repair or replace the engine harness** Repair the engine harness. Refer to Procedure 019-199 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> #### STEP 2D. Check for an open in the signal and return wires.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect engine harness adaptor cable from ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 14 of the engine harness adaptor cable to pin 15 of the connector. | Less than 10 ohms | 3A |
> |  | 2D-1 |  |
>
> #### STEP 2D-1. Check for an open in the engine harness adaptor cable and any engine harness extension cable used.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect engine harness adaptor cable from ECM. Disconnect engine harness from the engine harness expansion cable. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the continuity for pin 14 of the engine harness adaptor cable and any engine harness extension cable used. Measure the continuity for pin 15 of the engine harness adaptor cable and any engine harness extension cable used. | Less than 10 ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedures 019-202 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |
> | **Repair or replace the engine harness adaptor cable or the engine harness expansion cable(s), whichever is found faulty** Repair the engine harness adaptor cable or the engine harness expansion cable(s). Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or the engine harness expansion cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> ### STEP 3. Clear the fault code.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect all components. Start the engine and idle for one minute. | Fault Code 145 inactive | 3B |
> | Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 3B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared | Repair complete |
> | **Troubleshoot any remaining active fault codes.** | Appropriate troubleshooting chart |  |
