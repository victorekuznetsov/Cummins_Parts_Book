---
aliases:
  - "Цепь датчика температуры охлаждающей жидкости (CTS)"
type: "Процедура"
doc: "94-fc144"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc144.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc144.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Coolant Temperature Sensor (CTS) Circuit
**Цепь датчика температуры охлаждающей жидкости (CTS)**

> [!abstract] Процедура · `94-fc144`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc144.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc144.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 144

### Цепь датчика температуры охлаждающей жидкости (CTS)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 144 PID(P): СПН: ФМИ: Лампа: СТО: 00-355 | Высокое напряжение, обнаруженное при контакте датчика температуры охлаждающей жидкости двигателя 14 с электропроводкой жгута электронный модуль управления (ECM) разъема. | Ни одного на выступление. Общий предупредительный выход активизируется. |

![[19a00009.png]]

### Описание цепи

CTS используется ECM для мониторинга температуры охлаждающей жидкости двигателя. Температура охлаждающей жидкости используется ECM для системы защиты двигателя и управления заправкой. ECM контролирует напряжение на контакте 14. ECM ожидает, что напряжение будет варьироваться от 0,32 до 4,69 ВДК. Если напряжение выше 4,60 ВДК, то ECM регистрирует код 144 ошибки. Напряжение выше 4,60 VDC на контакте 14 может быть вызвано, открывается в сигнале или обратной провода, напряжения шорты на сигнал или обратной провода, или неисправный открытый датчик.

### Расположение компонента

CTS расположен на стороне корпуса термостата.

### Практические замечания

Если температура охлаждающей жидкости ниже -18°C \[0°F\], двигатель должен быть прогрет и проверен, чтобы увидеть, если неисправность неактивна.

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
|  | **STEP 1A.** Проверить проводку и контакты разъёма датчика. | Никаких поврежденных контактов |
|  | **ШАГ 1В.** Проверить сопротивление СТС. | 600 Ом до 36к Ом См. таблицу температуры/сопротивления в практическом примечании для правильного значения. |
| ШАГ 2. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 2A.** Проверить контакты разъёма адаптера и разъёма кабеля электропроводки двигателя. | Никаких поврежденных контактов |
|  | **STEP 2A-1.** Осмотрите контакты разъема (контактов) удлинителя (расширителей) кабеля (расширителей) упряжки двигателя и проводов двигателя. | Никаких поврежденных контактов |
|  | **STEP 2B.** Проверьте наличие открытого сигнала и провода обратной связи. | Менее 10 Ом |
|  | **STEP 2B-1.** Проверьте наличие открытого в двигателе провода, адаптера жгута и любого используемого удлинителя жгута жгута. | Менее 10 Ом |
|  | **STEP 2C.** Проверьте короткое замыкание сигнала и верните штифты во все остальные штифты. | Более 100 тыс. ом |
|  | **STEP 2C-1.** Проверьте короткое замыкание от штифта до всех других штифтов в адаптерном кабеле с жгутом двигателя и любом используемом кабеле с удлинением жгута двигателя. | Более 100 тыс. ом |
| ШАГ 3. | Очистите код ошибки. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код 144 неактивен |
|  | **STEP 3B.** Очистить код неактивного отказа. | Все ошибки устранены |

### ШАГ 1. Проверьте CTS.

#### ШАГ 1A. Проверьте проводку и контакты разъёма датчика.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините жгут электропроводки двигателя от CTS. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты корродируют штифты влагой в или на разъеме отсутствует уплотнение разъема. | Никаких поврежденных контактов | 1В |
| ** Починить поврежденные контакты** Починить или заменить ремень электропроводки двигателя или CTS, в зависимости от того, какие контакты повреждены. Ремонт ремня электропроводки двигателя. См. процедуру 019-202 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Заменить CTS. См. процедуру 019-019 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Сухой разъем с использованием электрического контактного очистителя, номер детали. 3824510. Замените уплотнение разъема. | 3А |  |

#### ШАГ 1B. Проверить сопротивление CTS.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините жгут электропроводки двигателя от CTS. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте сопротивление между двумя штифтами на стороне датчика соединения CTS. | 600 Ом до 36k Ом | 2А |
| **Заменить CTS** См. процедуру 019-019 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3А |  |

### ШАГ 2. Проверьте жгут проводов двигателя.

#### ШАГ 2A. Проверьте контакты разъёма ECM и проводов.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2А-1-1 |
| ** Починить поврежденные контакты** Починить или заменить ремень электропроводки двигателя или ECM, в зависимости от того, какие контакты повреждены. Ремонт ремня электропроводки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Заменить ECM. См. процедуры OEM. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. | 3А |  |

#### ШАГ 2A. Проверьте контакты разъёма ECM и проводов.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2А-1-1 |
| ** Починить поврежденные контакты** Починить или заменить проводку двигателя на адаптерный кабель или ECM, в зависимости от того, какие контакты повреждены. Ремонт проводов двигателя с помощью адаптера кабеля. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Замените проводку двигателя адаптерным кабелем. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Заменить ECM. См. процедуры OEM. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. | 3А |  |

#### ШАГ 2B. Проверьте наличие открытого сигнала и обратных проводов.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините жгут электропроводки двигателя от CTS. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте сопротивление от контакта 14 проводов двигателя с адаптерным кабелем разъёма для контакта А на стороне проводов ремня разъема CTS. Измерьте сопротивление от контакта 15 проводов двигателя с адаптерным кабелем разъёма к контакту B на стороне проводов ремня разъема CTS. | Менее 10 Ом | 2C |
|  | 2В-1-1 |  |

#### ШАГ 2B-1. Проверьте наличие открытого в двигателе провода, адаптерного кабеля и любого используемого удлинителя провода.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините жгут электропроводки двигателя от CTS. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте непрерывность контакта 14 с адаптерным кабелем адаптера и любым используемым кабелем расширения ремня электропроводки двигателя. Измерьте непрерывность контакта 15 с адаптерным кабелем адаптера и любым используемым кабелем расширения ремня электропроводки двигателя. | Менее 10 Ом Ремонт или замена электропроводки двигателя Ремонт электропроводки двигателя ремня. См. Процедуры 019-199, 019-202 и 019-240 в Руководстве по устранению неполадок и ремонту топливной системы QST серии QST30 G-Drive Engine, Бюллетень No. 3666184. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3А |
| ** Починить или заменить кабель адаптера или удлинитель (расширители) упряжки упряжки двигателя или проводку двигателя, в зависимости от того, что признано неисправным** Починить адаптер упряжки двигателя или удлинитель (расширители) упряжки двигателя. См. Процедуры 019-199, 019-202 и 019-240 в Руководстве по устранению неполадок и ремонту топливной системы QST серии QST30 G-Drive Engine, Бюллетень No. 3666184. Заменить проводку двигателя адаптерным кабелем или проводкой двигателя удлинительным кабелем (расширительными кабелями). См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3А |  |

#### ШАГ 2C. Проверьте короткое замыкание сигнала и верните штифты ко всем другим штифтам.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините жгут электропроводки двигателя от CTS. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить сопротивление от контакта 14 в проводах двигателя, соединить адаптерный кабель жгута проводов со всеми другими штифтами в разъеме, измерить сопротивление от контакта 15 в проводах двигателя, соединить адаптерный кабель жгута проводов со всеми другими штифтами в разъеме. | Более 100 тыс. ом | 3А |
|  | 2С-1 |  |

#### ШАГ 2C-1. Проверьте короткое замыкание от штифта до всех других штифтов в адаптерном кабеле жгута двигателя и любом используемом удлинительном кабеле жгута двигателя.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините проводку двигателя от проводов двигателя удлинитель (ы) удлинителя (ов) упряжки. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить сопротивление от контакта 14 в разъёме адаптера жгута проводов двигателя и любых проводов жгута проводов двигателя, используемых удлинителями кабелей, ко всем другим штифтам в разъеме измерить сопротивление от контакта 15 в разъёме адаптера жгута проводов двигателя и любой проводах двигателя, используемой удлинителями жгута проводов, ко всем другим штифтам в разъеме. | Более 100k Ом Ремонт или замена электропроводки двигателя Ремонт электропроводки двигателя ремня. См. процедуры 019-199 и 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3А |
| ** Починить или заменить кабель адаптера или удлинитель (расширители) упряжки упряжки двигателя или проводку двигателя, в зависимости от того, что признано неисправным** Починить адаптер упряжки двигателя или удлинитель (расширители) упряжки двигателя. См. Процедуры 019-199, 019-202 и 019-240 в Руководстве по устранению неполадок и ремонту топливной системы QST серии QST30 G-Drive Engine, Бюллетень No. 3666184. Заменить проводку двигателя адаптерным кабелем или проводкой двигателя удлинительным кабелем (расширительными кабелями). См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3А |  |

### ШАГ 3. Очистите код ошибки.

#### ШАГ 3A. Отключите код неисправности.

| **Условия: ** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Соедините все компоненты. Запустите двигатель и отпустите на минуту. Проверить, что код 144 неактивен. | Код 144 неактивен | 3B |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 3B. Сбросьте неактивные коды неисправностей.

| **Условия: ** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Стирать неактивные коды неисправностей с помощью INSITETM, номер детали. 3825145. **Примечание:** Разъем шины данных CAN расположен на правом берегу корпуса маховика. | Все ошибки устранены | Ремонт завершён |
| **Устранение неполадок с оставшимися активными кодами ошибок.** | Соответствующая диаграмма устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 144
>
> ### Coolant Temperature Sensor (CTS) Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 144 PID(P): SPN: FMI: Lamp: SRT: 00-355 | High voltage detected at engine coolant temperature sensor signal pin 14 of the engine harness Electronic Control Module (ECM) Connector. | None on performance. Common Warning output is energized. |
>
> ### Circuit Description
>
> The CTS is used by the ECM to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system and fueling control. The ECM monitors the voltage on pin 14. The ECM expects to see the voltage vary between 0.32 and 4.69 VDC. If the voltage is above 4.60 VDC, then the ECM will log Fault Code 144. Voltage above 4.60 VDC on pin 14 can be caused by, opens in the signal or return wires, voltage shorts to the signal or return wires, or a failed open sensor.
>
> ### Component Location
>
> The CTS is located on the side of the thermostat housing.
>
> ### Shoptalk
>
> If the coolant temperature is below -18° C \[0° F\] the engine should be warmed and checked to see if fault goes inactive.
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
> |  | **STEP 1A.** Inspect the harness and the sensor connector pins. | No damaged pins |
> |  | **STEP 1B.** Check the resistance of the CTS. | 600 ohms to 36k ohms See temperature/resistance table under shop talk for correct value. |
> | STEP 2. | Check the engine harness. |  |
> |  | **STEP 2A.** Inspect the ECM and the engine harness adaptor cable connector pins. | No damaged pins |
> |  | **STEP 2A-1.** Inspect the engine harness and the engine harness extension cable(s) connector pins. | No damaged pins |
> |  | **STEP 2B.** Check for an open in the signal and return wires. | Less than 10 ohms |
> |  | **STEP 2B-1.** Check for an open in the engine harness adaptor cable and any engine harness extension cable used. | Less than 10 ohms |
> |  | **STEP 2C.** Check for a short circuit from the signal and return pins to all other pins. | More than 100k ohms |
> |  | **STEP 2C-1.** Check for a short circuit from pin to all other pins in the engine harness adaptor cable and any engine harness extension cable used. | More than 100k ohms |
> | STEP 3. | Clear the fault code. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 144 inactive |
> |  | **STEP 3B.** Clear the inactive fault code. | All faults cleared |
>
> ### STEP 1. Check the CTS.
>
> #### STEP 1A. Inspect the harness and the sensor connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the CTS. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector missing connector seal. | No damaged pins | 1B |
> | **Repair the damaged pins** Repair or replace the engine harness or the CTS, whichever has the damaged pins. Repair the engine harness. Refer to Procedure 019-202 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the CTS. Refer to Procedure 019-019 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Dry connector by using electrical contact cleaner, Part No. 3824510. Replace the connector seal. | 3A |  |
>
> #### STEP 1B. Check resistance of CTS.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the CTS. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between the two pins on the sensor side of the CTS connection. | 600 ohms to 36k ohms | 2A |
> | **Replace the CTS** Refer to Procedure 019-019 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |
>
> ### STEP 2. Check the engine harness.
>
> #### STEP 2A. Inspect the ECM and the harness connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-1 |
> | **Repair the damaged pins** Repair or replace the engine harness or the ECM, whichever has the damaged pins. Repair the engine harness. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the ECM. Refer to OEM Procedures. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 3A |  |
>
> #### STEP 2A. Inspect the ECM and the harness connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-1 |
> | **Repair the damaged pins** Repair or replace the engine harness adaptor cable or the ECM, whichever has the damaged pins. Repair the engine harness adaptor cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness adaptor cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the ECM. Refer to OEM Procedures. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 3A |  |
>
> #### STEP 2B. Check for an open in the signal and return wires.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the CTS. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 14 of the engine harness adaptor cable connector to pin A on the harness side of the CTS connector. Measure the resistance from pin 15 of the engine harness adaptor cable connector to pin B on the harness side of the CTS connector. | Less than 10 ohms | 2C |
> |  | 2B-1 |  |
>
> #### STEP 2B-1. Check for an open in the engine harness adaptor cable and any engine harness extension cable used.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the CTS. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the continuity for pin 14 of the engine harness adaptor cable connector and any engine harness expansion cable used. Measure the continuity for pin 15 of the engine harness adaptor cable connector and any engine harness expansion cable used. | Less than 10 ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedures 019-199, 019-202 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |
> | **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedures 019-199, 019-202 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |
>
> #### STEP 2C. Check for a short circuit from the signal and return pins to all other pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the CTS. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | measure the resistance from pin 14 in the engine harness adaptor cable connector to all other pins in the connector measure the resistance from pin 15 in the engine harness adaptor cable connector to all other pins in the connector. | More than 100k ohms | 3A |
> |  | 2C-1 |  |
>
> #### STEP 2C-1. Check for a short circuit from pin to all other pins in the engine harness adaptor cable and any engine harness extension cable used.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the engine harness extension cable(s). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | measure the resistance from pin 14 in the engine harness adaptor cable connector and any engine harness extension cables used, to all other pins in the connector measure the resistance from pin 15 in the engine harness adaptor cable connector and any engine harness extension cables used, to all other pins in the connector | More than 100k ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-199 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |
> | **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedures 019-199, 019-202 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |
>
> ### STEP 3. Clear the fault code.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect all components. Start the engine and let idle for one minute. Verify Fault Code 144 is inactive. | Fault Code 144 inactive | 3B |
> | Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 3B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared | Repair complete |
> | **Troubleshoot any remaining active fault codes.** | Appropriate troubleshooting chart |  |
