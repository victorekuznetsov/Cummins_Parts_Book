---
aliases:
  - "Цепь датчика давления масла (OPS)"
type: "Процедура"
doc: "94-fc141"
title_en: "Oil Pressure Sensor (OPS) Circuit"
title_ru: "Цепь датчика давления масла (OPS)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Oil Pressure Sensor (OPS) Circuit
**Цепь датчика давления масла (OPS)**

> [!abstract] Процедура · `94-fc141`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc141.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 141

### Цепь датчика давления масла (OPS)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 141 PID(P): СПН: ФМИ: Лампа: СТО: 00-353 | Низкое напряжение, обнаруженное при датчике давления масла двигателя, сигнализирует о контакте 12 электропроводки ремня электроники (ECM) Connector. | Никакого влияния на производительность. Общий предупредительный выход активизируется. |

![[19a00007.png]]

### Описание цепи

OPS контролирует давление масла и передает информацию в ECM через контакт 12 с ремнем электропроводки двигателя. ECM контролирует напряжение на контакте 12 и ожидает, что напряжение будет варьироваться от 0,5 до 4,5 ВДК во время нормальной работы двигателя. Напряжение ниже 0,35 VDC при контакте 12 будет сбивать Код 141 по умолчанию и может быть вызвано шортами в подаче, сигнале или обратном проводе, открытым в подаче или сигнальных проводах, низким напряжением питания от ECM или неисправным датчиком.

### Расположение компонента

OPS расположен на левом берегу блока двигателя над топливным насосом.

### Практические замечания

Если код 143 или 415 неисправности ** не присутствует**, проблема связана с базовым двигателем.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

** Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерения: Часть нет. 3822758 - пробный щуп типа пробки Deutsch/Cannon/Metri-Pack**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте датчик давления масла. |  |
|  | **STEP 1A.** Осмотрите датчик давления масла и контакты разъема для проводов двигателя. | Никаких поврежденных контактов |
|  | **STEP 1B.** Проверьте напряжение питания под давлением масла ECM. | 4,75-5,25 VDC |
|  | **STEP 1C** Проверьте напряжение сигнала давления масла ECM. | 0,42 - 0,58 VDC |
| ШАГ 2. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 2A.** Проверить кабель адаптера ремня электропитания двигателя и разъем ECM на наличие поврежденных контактов. | Никаких поврежденных контактов |
|  | **STEP 2A-1.** Осмотрите разъем (разъемы) жгутов проводов и удлинитель (расширительные кабели) жгутов проводов двигателя для поврежденных контактов. | Никаких поврежденных контактов |
|  | **ШАГ 2В.** Проверить наличие открытой цепи. | Менее 10 Ом |
|  | **STEP 2B-1.** Проверьте наличие открытого в двигателе провода, адаптера жгута и любых используемых удлинителей жгута жгута. | Менее 10 Ом |
|  | **ШАГ 2С.** Проверить короткое замыкание на землю. | Более 100 тыс. ом |
|  | **STEP 2C-1.** Проверьте электропроводку двигателя для короткого замыкания на землю. | Более 100 тыс. ом |
|  | **STEP 2D.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 2D-1.** Проверьте короткое замыкание от штифта до штифта в кабеле адаптера жгута двигателя и любом используемом кабеле расширения жгута двигателя. | Более 100 тыс. ом |
| ШАГ 3. | Очистите код ошибки. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код 141 неактивный |
|  | **STEP 3B.** Очистить коды неактивных ошибок. | Все ошибки устранены |

### ШАГ 1. Проверьте датчик давления масла.

#### ШАГ 1A. Проверьте датчик давления масла и контакты разъёма жгута двигателя.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от датчика давления масла. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты корродируют штифты влагой или разъемом отсутствует уплотнение разъема. | Никаких поврежденных контактов | 1В |
| ** Поврежденные контакты** Ремонт или замена ремня электропроводки двигателя или ОПС, в зависимости от того, какие контакты повреждены. Ремонт ремня электропроводки двигателя. См. процедуру 019-203 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Замените ОПС. См. процедуру 019-061 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. Замените уплотнение разъема. | 3А |  |

#### ШАГ 1B. Проверьте напряжение подачи масла ECM.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Установите датчик давления масла, выключите кабель, номер детали. 3824775, между датчиком и разъёмом проводов датчика. Измерьте напряжение питания, установив подачу кабеля (контакт A) и разъемы возврата (контакт B) в мультиметр. | 4,75-5,25 VDC | 1С |
|  | 2А |  |

#### ШАГ 1C. Проверьте напряжение сигнала давления масла ECM.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте напряжение сигнала, установив сигнал кабеля (контакт C) и разъемы возврата (контакт B) в мультиметр. | 0,42 - 0,58 VDC | 2А |
| **Заменить датчик давления масла** См. процедуру 019-066 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3А |  |

### ШАГ 2. Проверьте жгут проводов двигателя.

#### ШАГ 2A. Осмотрите кабель адаптера жгута двигателя и разъем ECM для поврежденных контактов.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2А-1-1 |
| ** Починить поврежденные контакты** Починить или заменить проводку двигателя на адаптерный кабель или ECM, в зависимости от того, какие контакты повреждены. Ремонт проводов двигателя с помощью адаптера кабеля. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Замените проводку двигателя адаптерным кабелем. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Заменить ECM. См. процедуры OEM. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. | 3А |  |

#### ШАГ 2A-1. Осмотрите разъём ремня электропроводки двигателя и кабель(ы) расширения ремня электропроводки двигателя для поврежденных контактов.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от проводов двигателя кабеля (расширяющих кабелей). |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2В |
| ** Починить поврежденные контакты** Починить или заменить упряжку для проводов двигателя или кабель расширения упряжки двигателя, в зависимости от того, какие контакты повреждены. Ремонт ремня электропроводки двигателя или кабеля расширения ремня электропроводки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Замените упряжку для проводов двигателя или кабель расширения упряжки двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. | 3А |  |

#### ШАГ 2B. Проверьте цепь на обрыв.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините жгут электропроводки двигателя от OPS. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить сопротивление от проводов двигателя адаптерного кабеля разъёма контакта 12 к сигналу давления масла, контакту С, от стороны проводов разъема OPS. Измерить сопротивление от проводов двигателя упряжки адаптера кабельного разъёма контакт 11 и +5 VDC питания, контакт А, от разъема проводов упряжки OPS стороны. | Менее 10 Ом | 2C |
|  | 2В-1-1 |  |

#### ШАГ 2B-1. Проверьте наличие открытого в двигателе провода, адаптерного кабеля и любых используемых удлинителей проводов двигателя.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините проводку двигателя от проводов двигателя кабеля (расширяющих кабелей). |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте непрерывность контакта 12 для адаптера ремня электропроводки двигателя и любого используемого кабеля расширения ремня электропроводки двигателя. Измерьте непрерывность контакта 11 для адаптера жгута проводов двигателя и любого используемого кабеля расширения жгута проводов двигателя. | Менее 10 Ом Ремонт или замена электропроводки двигателя Ремонт электропроводки двигателя ремня. См. процедуру 019-203 и 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3А |
| ** Починить или заменить кабель адаптера упряжки двигателя или кабель расширения упряжки двигателя, в зависимости от того, что неисправно** Починить адаптер упряжки двигателя или кабель расширения упряжки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Замените адаптерный кабель или кабель расширения ремня электропроводки двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3А |  |

#### ШАГ 2C. Проверьте короткое замыкание на землю.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините жгут электропроводки двигателя от OPS. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить сопротивление от проводов двигателя разъёма адаптера кабеля контакт 12 к блоку двигателя грунт измерить сопротивление от проводов двигателя адаптер разъёма кабеля контакт 13 к блоку двигателя грунт измерить сопротивление от проводов двигателя адаптера разъёма кабеля контакт 11 к блоку двигателя земля. | Более 100 тыс. ом | 2D |
|  | 2С-1 |  |

#### ШАГ 2C-1. Проверьте короткое замыкание на землю.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините жгут электропроводки двигателя от OPS. Отсоедините проводку двигателя от проводов двигателя удлиняющие кабели. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить сопротивление от контакта 12 разъёма жгута двигателя к заземлению блока двигателя измерить сопротивление от контакта 13 разъёма жгута двигателя к заземлению блока двигателя измерить сопротивление от контакта 11 разъёма жгута двигателя к заземлению блока двигателя. | Более 100 тыс. ом | 2D-1 |
| ** Ремонт или замена электропроводки двигателя ** Ремонт электропроводки двигателя ремня. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3А |  |

#### ШАГ 2D. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините жгут электропроводки двигателя от OPS. Отсоедините проводку двигателя от датчика температуры охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить сопротивление от проводов двигателя разъёма адаптера кабеля контакт 12 ко всем другим штифтам в разъеме измерить сопротивление от проводов двигателя адаптера кабеля контакт 13 ко всем другим штифтам в разъеме измерить сопротивление от проводов двигателя адаптера кабеля контакт 11 ко всем другим штифтам в разъеме. | Более 100 000 Ом заменяют ECM. См. процедуры OEM. | 3А |
|  | 2D-1 |  |

#### ШАГ 2D-1. Проверьте короткое замыкание от пин-кодов до пин-кодов в адаптерном кабеле с жгутом двигателя и любом используемом кабеле расширения с жгутом двигателя.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините проводку двигателя от проводов двигателя кабеля (расширяющих кабелей). |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить сопротивление от контакта 12 проводов двигателя адаптер кабеля и любой проводов двигателя упряжки расширения кабеля, используемого, для всех других контактов в проводах двигателя упряжки разъёма измеряют сопротивление от контакта 13 проводов двигателя упряжки адаптера кабеля и любого провода двигателя упряжки расширения кабеля, используемого, чтобы все другие контакты в проводах двигателя упряжки разъема, чтобы измерить сопротивление от контакта 11 проводов двигателя упряжки адаптера кабеля и любого провода двигателя упряжки расширения кабеля, используемого, для всех других контактов в разъёме упряжки двигателя. | Более 100k Ом Ремонт или замена электропроводки двигателя Ремонт электропроводки двигателя ремня. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3А |
| ** Починить или заменить кабель адаптера упряжки двигателя или кабель расширения упряжки двигателя, в зависимости от того, что неисправно** Починить адаптер упряжки двигателя или кабель расширения упряжки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Замените адаптерный кабель или кабель расширения ремня электропроводки двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3А |  |

### ШАГ 3. Очистите код ошибки.

#### ШАГ 3A. Отключите код неисправности.

| **Условия: ** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Подключите все компоненты, запустите двигатель и проведите одну минуту, чтобы убедиться, что код 141 неактивен. | Код 141 неактивный | 3B |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 3B. Сбросьте неактивные коды неисправностей.

| **Условия: ** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Стирать неактивные коды неисправностей с помощью INSITETM, номер детали. 3825145. **Примечание:** Разъем шины данных CAN расположен на правом берегу корпуса маховика. | Все ошибки устранены | Ремонт завершён |
| **Устранение неполадок с оставшимися активными кодами ошибок.** | Соответствующая диаграмма устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 141
>
> ### Oil Pressure Sensor (OPS) Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 141 PID(P): SPN: FMI: Lamp: SRT: 00-353 | Low voltage detected at engine oil pressure sensor signal pin 12 of the engine harness Electronic Control Module (ECM) Connector. | No effect on performance. Common Warning output is energized. |
>
> ### Circuit Description
>
> The OPS monitors oil pressure and passes information to the ECM through pin 12 of the engine harness. The ECM monitors the voltage on pin 12 and expects to see the voltage vary between 0.5 and 4.5 VDC during normal engine operation. Voltage below 0.35 VDC on pin 12 will trip Fault Code 141 and can be caused by shorts in the supply, signal, or return wires, an open in the supply or signal wires, low supply voltage from the ECM, or a failed sensor.
>
> ### Component Location
>
> The OPS is located on the left bank of the engine block above the fuel pump.
>
> ### Shoptalk
>
> If Fault Code 143 or 415 are **not** present, the problem is **not** base engine related.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To avoid pin and harness damage, use the following test leads when taking a measurement: Part No. 3822758 - male Deutsch/Cannon/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the oil pressure sensor. |  |
> |  | **STEP 1A.** Inspect the oil pressure sensor and engine harness connector pins. | No damaged pins |
> |  | **STEP 1B.** Check the ECM oil pressure supply voltage. | 4.75 to 5.25 VDC |
> |  | **STEP 1C.** Check the ECM oil pressure signal voltage. | 0.42 to 0.58 VDC |
> | STEP 2. | Check the engine harness. |  |
> |  | **STEP 2A.** Inspect the engine harness adaptor cable and the ECM connector for damaged pins. | No damaged pins |
> |  | **STEP 2A-1.** Inspect the engine harness connector and the engine harness extension cable(s) for damaged pins. | No damaged pins |
> |  | **STEP 2B.** Check for an open circuit. | Less than 10 ohms |
> |  | **STEP 2B-1.** Check for an open in the engine harness adaptor cable and any engine harness extension cables used. | Less than 10 ohms |
> |  | **STEP 2C.** Check for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 2C-1.** Check engine harness for short circuit to ground. | More than 100k ohms |
> |  | **STEP 2D.** Check for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 2D-1.** Check for a short circuit from pin to pin in the engine harness adaptor cable and any engine harness extension cable used. | More than 100k ohms |
> | STEP 3. | Clear the fault code. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 141 inactive |
> |  | **STEP 3B.** Clear any inactive fault codes. | All faults cleared |
>
> ### STEP 1. Check the oil pressure sensor.
>
> #### STEP 1A. Inspect the oil pressure sensor and engine harness connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the oil pressure sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or the connector missing connector seal. | No damaged pins | 1B |
> | **Repair damaged pins** Repair or replace the engine harness or the OPS, whichever has the damaged pins. Repair the engine harness. Refer to Procedure 019-203 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the OPS. Refer to Procedure 019-061 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Dry the connector by using electrical contact cleaner, Part No. 3824510. Replace the connector seal. | 3A |  |
>
> #### STEP 1B. Check the ECM oil pressure supply voltage.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Install the oil pressure sensor break out cable, Part No. 3824775, between the sensor and the sensor harness connector. Measure the supply voltage by installing the break out cable's supply (pin A) and return connectors (pin B) into the multimeter. | 4.75 to 5.25 VDC | 1C |
> |  | 2A |  |
>
> #### STEP 1C. Check the ECM oil pressure signal voltage.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the signal voltage by installing the break out cable's signal (pin C) and return connectors (pin B) into the multimeter. | 0.42 to 0.58 VDC | 2A |
> | **Replace the oil pressure sensor** Refer to Procedure 019-066 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |
>
> ### STEP 2. Check the engine harness.
>
> #### STEP 2A. Inspect the engine harness adaptor cable and the ECM connector for damaged pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-1 |
> | **Repair the damaged pins** Repair or replace the engine harness adaptor cable or the ECM, whichever has the damaged pins. Repair the engine harness adaptor cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness adaptor cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the ECM. Refer to OEM Procedures. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 3A |  |
>
> #### STEP 2A-1. Inspect the engine harness connector and the engine harness expansion cable(s) for damaged pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness expansion cable(s). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2B |
> | **Repair the damaged pins** Repair or replace the engine harness or the engine harness expansion cable, whichever has the damaged pins. Repair the engine harness or the engine harness expansion cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness or the engine harness expansion cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 3A |  |
>
> #### STEP 2B. Check for an open circuit.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the OPS. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from engine harness adaptor cable connector pin 12 to oil pressure signal, pin C, of the OPS connector harness side. Measure the resistance from engine harness adaptor cable connector pin 11 and +5 VDC supply, pin A, of the OPS connector harness side. | Less than 10 ohms | 2C |
> |  | 2B-1 |  |
>
> #### STEP 2B-1. Check for an open in the engine harness adaptor cable and any engine harness extension cables used.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the engine harness expansion cable(s). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the continuity of pin 12 for the engine harness adaptor cable and any engine harness expansion cable being used. Measure the continuity of pin 11 for the engine harness adaptor cable and any engine harness expansion cable being used. | Less than 10 ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-203 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |
> | **Repair or replace the engine harness adaptor cable or the engine harness expansion cable, whichever is faulty** Repair the engine harness adaptor cable or the engine harness expansion cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness adaptor cable or the engine harness expansion cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |
>
> #### STEP 2C. Check for a short circuit to ground.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the OPS. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | measure the resistance from engine harness adaptor cable connector pin 12 to engine block ground measure the resistance from engine harness adaptor cable connector pin 13 to engine block ground measure the resistance from engine harness adaptor cable connector pin 11 to engine block ground. | More than 100k ohms | 2D |
> |  | 2C-1 |  |
>
> #### STEP 2C-1. Check for a short circuit to ground.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the OPS. Disconnect the engine harness from the engine harness extension cables. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | measure the resistance from engine harness connector pin 12 to engine block ground measure the resistance from engine harness connector pin 13 to engine block ground measure the resistance from engine harness connector pin 11 to engine block ground. | More than 100k ohms | 2D-1 |
> | **Repair or replace the engine harness** Repair the engine harness. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |
>
> #### STEP 2D. Check for a short circuit from pin to pin.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the OPS. Disconnect the engine harness from the coolant temperature sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | measure the resistance from engine harness adaptor cable connector pin 12 to all other pins in the connector measure the resistance from engine harness adaptor cable connector pin 13 to all other pins in the connector measure the resistance from engine harness adaptor cable connector pin 11 to all other pins in the connector. | More than 100k ohms Replace the ECM. Refer to OEM Procedures. | 3A |
> |  | 2D-1 |  |
>
> #### STEP 2D-1. Check for a short circuit from pin to pin in the engine harness adaptor cable and any engine harness extension cable used.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the engine harness expansion cable(s). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | measure the resistance from pin 12 of the engine harness adaptor cable and any engine harness expansion cable used, to all other pins in the engine harness connector measure the resistance from pin 13 of the engine harness adaptor cable and any engine harness expansion cable used, to all other pins in the engine harness connector measure the resistance from pin 11 of the engine harness adaptor cable and any engine harness expansion cable used, to all other pins in the engine harness connector. | More than 100k ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |
> | **Repair or replace the engine harness adaptor cable or the engine harness expansion cable, whichever is faulty** Repair the engine harness adaptor cable or the engine harness expansion cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness adaptor cable or the engine harness expansion cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |
>
> ### STEP 3. Clear the fault code.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | connect all components start the engine and idle for one minute verify that Fault Code 141 is inactive. | Fault Code 141 inactive | 3B |
> | Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 3B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared | Repair complete |
> | **Troubleshoot any remaining active fault codes.** | Appropriate troubleshooting chart |  |
