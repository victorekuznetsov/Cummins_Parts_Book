---
aliases:
  - "Цепь датчика давления масла (OPS)"
type: "Процедура"
doc: "94-fc135"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc135.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc135.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Oil Pressure Sensor (OPS) Circuit
**Цепь датчика давления масла (OPS)**

> [!abstract] Процедура · `94-fc135`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc135.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc135.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 135

### Цепь датчика давления масла (OPS)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 135 PID (P): СПН: ФМИ: Лампа: СТО: 00-352 | Высокое напряжение, обнаруженное при контакте 12 сигнала датчика давления масла двигателя с электропроводкой упряжки электронного модуля управления (ECM) Коннектора. | Никакого влияния на производительность. Общий предупредительный выход активизируется. |

![[19a00007.png]]

### Описание цепи

OPS контролирует давление масла и передает информацию в ECM через контакт 12 с ремнем электропроводки двигателя. ECM контролирует напряжение на контакте 12 и ожидает, что напряжение будет варьироваться от 0,5 до 4,5 ВДК во время нормальной работы двигателя. Напряжение выше 4,89 VDC при контакте 12 будет сбивать Код 135 по умолчанию и может быть вызвано шортами в проводах подачи, сигнала или возврата, открытым в обратном проводе или неисправным датчиком.

### Расположение компонента

OPS расположен на левом берегу блока двигателя над топливным насосом.

### Практические замечания

Происходит ли ошибка только в холодную погоду? Если это так, то дайте маслу разогреться и посмотрите, не активируется ли разлом.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерения: Часть нет. 3822758 - пробный щуп типа пробки Deutsch/Cannon/Metri-Pack**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте датчик давления масла. |  |
|  | **STEP 1A.** Осмотрите датчик давления масла и контакты разъема для проводов двигателя. | Никаких поврежденных контактов |
|  | **STEP 1B.** Проверьте напряжение питания под давлением масла ECM. | 4,75-5,25 VDC |
|  | **STEP 1C** Проверьте напряжение сигнала давления масла ECM. | 0,42 - 0,58 VDC |
| ШАГ 2. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 2A.** Проверить кабель адаптера ремня электропитания двигателя и контакты разъема ECM. | Никаких поврежденных контактов |
|  | **STEP 2A-1.** Осмотрите контакты разъема (контактов) удлинителя (расширителей) кабеля (расширителей) упряжки двигателя и проводов двигателя. | Никаких поврежденных контактов |
|  | **ШАГ 2В.** Проверить короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 2B-1.** Проверьте короткое замыкание от штифта до штифта в проводах двигателя, адаптерном кабеле и удлинительном кабеле (-ах). | Больше 100k Ом |
|  | **STEP 2C.** Проверьте наличие открытой цепи в обратном проводе. | Менее 10 Ом |
|  | **STEP 2C-1.** Проверьте наличие открытой цепи от штифта до штифта в проводах двигателя, адаптерном кабеле и удлинительном кабеле (-ах). | Менее 10 Ом |
| ШАГ 3. | Очистите код ошибки. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код 135 неактивен |
|  | **STEP 3B.** Очистить коды неактивных ошибок. | Все ошибки устранены |

### ШАГ 1. Проверьте датчик давления масла.

#### ШАГ 1A. Проверьте датчик давления масла и контакты разъёма жгута двигателя.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините разъем жгута проводов двигателя от датчика давления масла. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты корродируют штифты влагой в или на разъеме отсутствует уплотнение разъема. | Никаких поврежденных контактов | 1В |
| **Починить поврежденные контакты** Починить или заменить ремень электропроводки двигателя или датчик давления масла, в зависимости от того, какие контакты повреждены. Ремонт ремня электропроводки двигателя. См. процедуру 019-203 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 19-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените датчик давления масла. См. процедуру 019-066 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. Замените уплотнение разъема. | 3А |  |

#### ШАГ 1B. Проверьте напряжение подачи масла ECM.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Установите датчик давления масла проводку ремня ветвления кабеля, номер детали. 3824775, между датчиком и разъёмом проводов датчика. Измерьте напряжение питания, установив разъёмы питания проводов ветвящегося кабеля (контакт A) и возврата (контакт B) в мультиметр. | 4,75-5,25 VDC | 1С |
|  | 2А |  |

#### ШАГ 1C. Проверьте напряжение сигнала давления масла ECM.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение сигнала, установив сигнал проводов ветвящегося кабеля (контакт C) и разъемы возврата (контакт B) в мультиметр. | 0,42 - 0,58 VDC | 2А |
| **Заменить датчик давления масла** См. процедуру 019-066 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

### ШАГ 2. Проверьте жгут проводов двигателя.

#### ШАГ 2A. Проверьте кабель адаптера жгута двигателя и контакты разъема ECM.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2А-1-1 |
| **Поврежденные контакты** Починить или заменить проводку двигателя на адаптерный кабель или ECM, в зависимости от того, какие контакты повреждены. Ремонт проводов двигателя с помощью адаптера кабеля. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените проводку двигателя адаптерным кабелем. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить ECM. См. процедуры OEM. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. | 3А |  |

#### ШАГ 2A-1. Осмотрите контакты разъема (контактов) удлинителя (расширителей) кабеля (расширителей) упряжки двигателя и проводов двигателя.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от проводов двигателя удлинитель (ы) удлинителя (ов) упряжки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2В |
| **Починить поврежденные контакты** Починить или заменить упряжку для проводов двигателя или удлинитель (расширительные кабели) упряжки двигателя, в зависимости от того, какие контакты повреждены. Ремонт ремня проводов двигателя или проводов двигателя удлинитель (ы) провода удлинителя (ов). См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить упряжку или удлинитель (расширительные кабели) упряжки двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. | 3А |  |

#### ШАГ 2B. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините жгут электропроводки двигателя от OPS. Отсоедините проводку двигателя от датчика температуры охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от проводов двигателя кабельного разъёма адаптера ремня 12 ко всем другим штифтам в кабельном разъёме адаптера ремня управления двигателем. Измерьте сопротивление от проводов двигателя кабельного разъёма адаптера ремня 13 ко всем другим штифтам в кабельном разъёме адаптера ремня управления двигателем. Измерьте сопротивление от проводов двигателя кабельного разъёма адаптера контакт 11 ко всем другим штифтам в проводах двигателя кабельного разъёма ремня. | Более 100 тыс. ом | 2C |
|  | 2В-1-1 |  |

#### ШАГ 2B-1. Проверьте короткое замыкание от пин-кодов до пин-кодов в кабеле адаптера для проводов двигателя и удлинительном кабеле (-ах).

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините проводку двигателя от проводов двигателя удлинитель (ы) удлинителя (ов) упряжки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от проводов двигателя адаптерного кабеля и проводов двигателя удлинителя (расширителей) разъёма разъёма 12 ко всем другим штифтам в разъёме. Измерьте сопротивление от проводов двигателя адаптерного кабеля и проводов двигателя удлинителя (расширителей) разъёма контактного 13 со всеми другими штифтами в разъеме. Измерьте сопротивление от проводов двигателя адаптерного кабеля и проводов двигателя удлинителя (расширителей) разъёма разъёма 11 ко всем другим штифтам в разъёме. | Более 100 тыс. омов Ремонт или замена электропроводки двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |
| **Починить или заменить кабель адаптера или удлинитель (расширители) упряжки упряжки двигателя или проводку двигателя, в зависимости от того, что признано неисправным** Починить адаптер упряжки двигателя или удлинитель (расширители) упряжки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить проводку двигателя адаптерным кабелем или проводкой двигателя удлинительным кабелем (расширительными кабелями). См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

#### ШАГ 2C. Проверьте наличие открытой цепи в обратном проводе.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините жгут электропроводки двигателя от OPS. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от проводов двигателя с помощью адаптера разъёма кабеля контакт 13 для контакта В разъема OPS на стороне проводов ремня. | Менее 10 Ом | 3А |
|  | 2С-1 |  |

#### ШАГ 2C-1. Проверьте наличие открытой цепи от пин-кодов до пин-кодов в кабеле адаптера и удлинительном кабеле (-ах).

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от проводов двигателя удлинитель (ы) удлинителя (ов) упряжки. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте непрерывность контакта 13 проводов двигателя с адаптерным кабелем разъёма и любой проводов двигателя с удлинителями кабелей. | Менее 10 Ом Ремонт или замена электропроводки двигателя жгута. Ремонт ремня электропроводки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |
| **Починить или заменить кабель адаптера или удлинитель (расширители) упряжки упряжки двигателя или проводку двигателя, в зависимости от того, что признано неисправным** Починить адаптер упряжки двигателя или удлинитель (расширители) упряжки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить проводку двигателя адаптерным кабелем или проводкой двигателя удлинительным кабелем (расширительными кабелями). См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

### ШАГ 3. Очистите код ошибки.

#### ШАГ 3A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подключите все компоненты, запустите двигатель и проведите одну минуту, чтобы убедиться, что код 135 неактивен. | Код 135 неактивен | 3B |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 3B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Стирать неактивные коды неисправностей с помощью INSITETM, номер детали. 3825145. **Примечание:** Разъем шины данных CAN расположен на правом берегу корпуса маховика. | Все ошибки устранены | Ремонт завершён |
| **Устранение неполадок с оставшимися активными кодами ошибок.** | Соответствующая диаграмма устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 135
>
> ### Oil Pressure Sensor (OPS) Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 135 PID(P): SPN: FMI: Lamp: SRT: 00-352 | High voltage detected at engine oil pressure sensor signal pin 12 of the engine harness Electronic Control Module (ECM) Connector. | No effect on performance. Common Warning output is energized. |
>
> ### Circuit Description
>
> The OPS monitors oil pressure and passes information to the ECM through pin 12 of the engine harness. The ECM monitors the voltage on pin 12 and expects to see the voltage vary between 0.5 and 4.5 VDC during normal engine operation. Voltage above 4.89 VDC on pin 12 will trip Fault Code 135 and can be caused by shorts in the supply, signal, or return wires, an open in the return wire or a failed sensor.
>
> ### Component Location
>
> The OPS is located on the left bank of the engine block above the fuel pump.
>
> ### Shoptalk
>
> Does the fault occur only in cold weather? If so, allow the oil to warm up and see if the fault goes inactive.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To avoid pin and harness damage use the following test leads when taking a measurement: Part No. 3822758 - male Deutsch/Cannon/Metri-Pack test lead.**
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
> |  | **STEP 2A.** Inspect the engine harness adaptor cable and the ECM connector pins. | No damaged pins |
> |  | **STEP 2A-1.** Inspect the engine harness and engine harness extension cable(s) connector pins. | No damaged pins |
> |  | **STEP 2B.** Check for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 2B-1.** Check for a short circuit from pin to pin in the engine harness adaptor cable and extension cable(s). | More the 100k ohms |
> |  | **STEP 2C.** Check for an open circuit in the return wire. | Less than 10 ohms |
> |  | **STEP 2C-1.** Check for an open circuit from pin to pin in the engine harness adaptor cable and extension cable(s). | Less than 10 ohms |
> | STEP 3. | Clear the fault code. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 135 inactive |
> |  | **STEP 3B.** Clear the inactive fault codes. | All faults cleared |
>
> ### STEP 1. Check the oil pressure sensor.
>
> #### STEP 1A. Inspect the oil pressure sensor and engine harness connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the oil pressure sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector missing connector seal. | No damaged pins | 1B |
> | **Repair the damaged pins** Repair or replace the engine harness or the oil pressure sensor, whichever has the damaged pins. Repair the engine harness. Refer to Procedure 019-203 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 19-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the oil pressure sensor. Refer to Procedure 019-066 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Dry the connector by using an electrical contact cleaner, Part No. 3824510. Replace the connector seal. | 3A |  |
>
> #### STEP 1B. Check the ECM oil pressure supply voltage.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Install the oil pressure sensor breakout cable, Part No. 3824775, between the sensor and the sensor harness connector. Measure the supply voltage by installing the breakout cable's supply (pin A) and return (pin B) connectors into the multimeter. | 4.75 to 5.25 VDC | 1C |
> |  | 2A |  |
>
> #### STEP 1C. Check the ECM oil pressure signal voltage.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the signal voltage by installing the breakout cable's signal (pin C) and return (pin B) connectors into the multimeter. | 0.42 to 0.58 VDC | 2A |
> | **Replace oil pressure sensor** Refer to Procedure 019-066 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> ### STEP 2. Check the engine harness.
>
> #### STEP 2A. Inspect the engine harness adaptor cable and the ECM connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-1 |
> | **Repair the damaged pins** Repair or replace the engine harness adaptor cable or ECM, whichever has the damaged pins. Repair the engine harness adaptor cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the ECM. Refer to OEM Procedures. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 3A |  |
>
> #### STEP 2A-1. Inspect the engine harness and engine harness extension cable(s) connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cable(s). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2B |
> | **Repair the damaged pins** Repair or replace the engine harness or the engine harness extension cable(s), whichever has the damaged pins. Repair the engine harness or the engine harness extension cable(s). Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness or the engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 3A |  |
>
> #### STEP 2B. Check for a short circuit from pin to pin.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the OPS. Disconnect the engine harness from the coolant temperature sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from the engine harness adaptor cable connector pin 12 to all other pins in the engine harness adaptor cable connector. Measure the resistance from the engine harness adaptor cable connector pin 13 to all other pins in the engine harness adaptor cable connector. Measure the resistance from the engine harness adaptor cable connector pin 11 to all other pins in the engine harness cable connector. | More than 100k ohms | 2C |
> |  | 2B-1 |  |
>
> #### STEP 2B-1. Check for a short circuit from pin to pin in the engine harness adaptor cable and extension cable(s).
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the engine harness extension cable(s). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from the engine harness adaptor cable and engine harness extension cable(s) connector pin 12 to all other pins in the connector. Measure the resistance from the engine harness adaptor cable and engine harness extension cable(s) connector pin 13 to all other pins in the connector. Measure the resistance from the engine harness adaptor cable and engine harness extension cable(s) connector pin 11 to all other pins in the connector. | More than 100k ohms Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |
> | **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> #### STEP 2C. Check for an open circuit in the return wire.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the OPS. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from engine harness adaptor cable connector pin 13 to pin B of the OPS connector on the harness side. | Less than 10 ohms | 3A |
> |  | 2C-1 |  |
>
> #### STEP 2C-1. Check for an open circuit from pin to pin in the engine harness adaptor cable and extension cable(s).
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cable(s). Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the continuity of pin 13 of the engine harness adaptor cable connector and any engine harness extension cables. | Less than 10 ohms Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |
> | **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> ### STEP 3. Clear the fault code.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | connect all components start the engine and idle for one minute verify that Fault Code 135 is inactive. | Fault Code 135 inactive | 3B |
> | Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 3B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared | Repair complete |
> | **Troubleshoot any remaining active fault codes.** | Appropriate troubleshooting chart |  |
