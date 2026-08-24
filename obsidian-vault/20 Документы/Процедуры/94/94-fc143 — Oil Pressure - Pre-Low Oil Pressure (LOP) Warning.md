---
aliases:
  - "Давление масла — предупреждение о приближении к низкому (LOP)"
type: "Процедура"
doc: "94-fc143"
title_en: "Oil Pressure - Pre-Low Oil Pressure (LOP) Warning"
title_ru: "Давление масла — предупреждение о приближении к низкому (LOP)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc143.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc143.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Oil Pressure - Pre-Low Oil Pressure (LOP) Warning
**Давление масла — предупреждение о приближении к низкому (LOP)**

> [!abstract] Процедура · `94-fc143`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc143.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc143.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 143

### Давление масла — предупреждение о приближении к низкому (LOP)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 143 PID(P): СПН: ФМИ: Лампа: СТО: 00-354 | Давление моторного масла упало ниже порога предупреждения низкого давления масла. | Никакого влияния на производительность. Общий предупредительный выход активизируется. Водитель реле пре-низкого давления масла (LOP) заряжается энергией. |

![[19a00007.png]]

### Описание цепи

Датчик давления масла используется электронным модулем управления (ECM) для контроля давления моторного масла. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления. Значение давления масла используется ECM для системы защиты двигателя.

### Расположение компонента

Датчик давления масла (OPS) расположен на левом берегу блока двигателя над топливным насосом.

### Практические замечания

- Подтвердите, что напряжение питания датчика давления масла составляет от 4,75 до 5,25 ВДК на датчике. См. Код 141.

- Давление масла является функцией скорости двигателя, уровня масла и функции регулятора. Работа двигателя на низкой скорости под нагрузкой будет ** не ** заставлять давление масла быть низким, если масло не нагревается, масло на низком уровне, регулятор неисправен или потери происходят где-то в системе.

- Порог для предупреждения о преднизком давлении масла регулируется с помощью INSITETM, номер детали. 3825145.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте точность датчика. |  |
|  | **STEP 1A.** Проверить точность датчика с помощью механического калибра. | Чтение датчиков правильное |
| ШАГ 2. | Очистите код ошибки. |  |
|  | **STEP 2A.** Отключить код ошибки. | Код 143 неактивен |
|  | **STEP 2B.** Очистить коды неактивных ошибок. | Все ошибки устранены |

### ШАГ 1. Проверьте точность датчика.

#### ШАГ 1A. Проверить точность датчика с помощью механического калибра.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Подключите механический измеритель давления масла известного качества и калибровку к двигателю на одной из вилок поверх головки масляного фильтра. Подключите Insite, номер детали. 3825145, на шину данных CAN. Запустите двигатель и сравните показания давления масла на INSITETM, номер детали. 3825145, экран монитора для считывания на механическом масляном измерителе давления. **Примечание:** Оборудование двигателя необходимо увеличить, чтобы было легче видеть различия в показаниях. | Считывание датчика правильно См. Руководство по устранению неполадок и ремонту базового двигателя для правильных спецификаций. | 2А |
|  | Перейти к коду 141 |  |

### ШАГ 2. Очистите код ошибки.

#### ШАГ 2A. Отключите код неисправности.

| **Условия: ** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Подключите все компоненты. Запустите двигатель и запускайте его на холостом ходу в течение одной минуты. **Примечание:** Если ошибка была на определенном обороте, запустите двигатель на этом обороте, чтобы проверить, что проблема исправлена. | Код 143 неактивен | 2В |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и перепроверены. | 1А |  |

#### ШАГ 2B. Очистите неактивные коды ошибок.

| **Условия: ** Соедините все компоненты. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Стирать неактивные коды неисправностей с помощью INSITETM, номер детали. 3825145. **Примечание:** Разъем шины данных CAN расположен на правом берегу корпуса маховика. | Все ошибки устранены | Ремонт завершён |
| **Устранение неполадок с оставшимися активными кодами ошибок.** | Соответствующая диаграмма устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 143
>
> ### Oil Pressure - Pre-Low Oil Pressure (LOP) Warning
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 143 PID(P): SPN: FMI: Lamp: SRT: 00-354 | Engine oil pressure has dropped below the warning threshold for low oil pressure. | No effect on performance. Common Warning output is energized. Pre-Low Oil Pressure (LOP) relay driver is energized. |
>
> ### Circuit Description
>
> The oil pressure sensor is used by the Electronic Control Module (ECM) to monitor the lubricating oil pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The oil pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> The oil pressure sensor (OPS) is located on the left bank of the engine block above the fuel pump.
>
> ### Shoptalk
>
> - Confirm that the oil pressure sensor supply voltage is between 4.75 and 5.25 VDC at the sensor. See Fault Code 141.
>
> - Oil pressure is a function of engine speed, oil level, and regulator function. Operating the engine at a low speed under load will **not** cause the oil pressure to be low unless oil is hot, oil at a low level, regulator has malfunctioned, or a loss is occurring somewhere in the system.
>
> - The threshold for the pre-low oil pressure warning is adjustable with INSITE™, Part No. 3825145.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the sensor accuracy. |  |
> |  | **STEP 1A.** Verify sensor accuracy with a mechanical gauge. | Sensor reading is correct |
> | STEP 2. | Clear the fault code. |  |
> |  | **STEP 2A.** Disable the fault code. | Fault Code 143 inactive |
> |  | **STEP 2B.** Clear any inactive fault codes. | All faults cleared |
>
> ### STEP 1. Check the sensor accuracy.
>
> #### STEP 1A. Verify sensor accuracy with a mechanical gauge.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect a mechanical oil pressure gauge of known quality and calibration to the engine at one of the plugs on top of the oil filter head. Connect INSITE™, Part No. 3825145, to the data link. Start engine and compare the oil pressure reading on the INSITE™, Part No. 3825145, monitor screen to the reading on mechanical oil pressure gauge. **NOTE:** The engine rpm will need to be increased to make it easier to see differences in the readings. | Sensor reading is correct Refer to the Base Engine Troubleshooting and Repair Manual for correct specifications. | 2A |
> |  | Go to Fault Code 141 |  |
>
> ### STEP 2. Clear the fault code.
>
> #### STEP 2A. Disable the fault code.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect all of the components. Start engine and let it idle for one minute. **NOTE:** If the fault was at a particular rpm, run engine at that rpm to verify the problem is corrected. | Fault Code 143 inactive | 2B |
> | Return to the troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and rechecked. | 1A |  |
>
> #### STEP 2B. Clear any inactive fault codes.
>
> | **Conditions:** Connect all of the components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Erase any inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared | Repair complete |
> | **Troubleshoot any remaining active fault codes.** | Appropriate troubleshooting chart |  |
