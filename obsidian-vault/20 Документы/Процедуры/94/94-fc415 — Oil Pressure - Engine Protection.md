---
aliases:
  - "Давление масла — защита двигателя"
type: "Процедура"
doc: "94-fc415"
title_en: "Oil Pressure - Engine Protection"
title_ru: "Давление масла — защита двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc415.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc415.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Oil Pressure - Engine Protection
**Давление масла — защита двигателя**

> [!abstract] Процедура · `94-fc415`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc415.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc415.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 415

### Давление масла — защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 415 PID(P): СПН: ФМИ: Лампа: СТО: 00-367 | Давление масла в двигателе упало ниже порога тревоги (затормоза) для низкого давления масла. | Двигатель отключится. Общий выход сигнализации активизирован. Водитель реле низкого давления (LOP) заряжается энергией. |

![[19a00007.png]]

### Описание цепи

OPS используется электронным модулем управления (ECM) для мониторинга давления моторного масла. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления. Значение давления масла используется ECM для системы защиты двигателя.

### Расположение компонента

OPS расположен на левом берегу блока двигателя над топливным насосом.

### Практические замечания

- Подтвердите, что напряжение питания OPS находится между 4,75 и 5,25 ВДК на датчике. См. Код 141.

- Давление масла является функцией скорости двигателя, уровня масла и функции регулятора. Работа двигателя на низкой скорости при нагрузке не приведет к низкому давлению масла, если масло не нагревается, на низком уровне регулятор неисправен или где-то в системе происходит потеря.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте точность датчика. |  |
|  | **STEP 1A.** Проверить точность датчика с помощью механического калибра. | Чтение датчиков правильное |
| ШАГ 2. | Очистите код ошибки. |  |
|  | **STEP 2A.** Отключить код ошибки. | Код 415 неактивный |
|  | **STEP 2B.** Очистить коды неактивных ошибок. | Все неисправности устранены |

### ШАГ 1. Проверьте точность датчика.

#### ШАГ 1A. Проверить точность датчика с помощью механического калибра.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подключите механический измеритель давления масла известного качества и калибровку к двигателю на одной из вилок поверх головки масляного фильтра. Подключите Insite, номер детали. 3825145, на шину данных CAN. Запустите двигатель и сравните показания давления масла на экране монитора с показаниями на механическом датчике измерения давления масла. **Примечание: **Скорость двигателя должна быть увеличена, чтобы было легче увидеть различия в показаниях. | Датчик показаний правильный. | 2А |
| **Перейти к коду 141** | Код ошибки 141 |  |

### ШАГ 2. Очистите код ошибки.

#### ШАГ 2A. Отключите код неисправности.

| **Условия: **Соедините все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подключите все компоненты. Запустите двигатель и запускайте его на холостом ходу в течение одной минуты. **Примечание:** Если неисправность была на определенной скорости, то для проверки исправления проблемы используется двигатель с такой скоростью. | Код 415 неактивный | 2В |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 2B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соедините все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Стирать неактивные коды неисправностей с помощью INSITETM, номер детали. 3825145. **Примечание:** Разъем шины данных CAN расположен на правом берегу корпуса маховика. | Все неисправности устранены | Ремонт завершён |
| **Устранение неисправностей с оставшимися активными кодами** | Соответствующая диаграмма устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 415
>
> ### Oil Pressure - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 415 PID(P): SPN: FMI: Lamp: SRT: 00-367 | Engine oil pressure has dropped below the alarm (shutdown) threshold for low oil pressure. | Engine will shutdown. Common Alarm output is energized. Low Oil Pressure (LOP) relay driver is energized. |
>
> ### Circuit Description
>
> The OPS is used by the electronic control module (ECM) to monitor the lubricating oil pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The oil pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> The OPS is located on the left bank of the engine block above the fuel pump.
>
> ### Shoptalk
>
> - Confirm that the OPS supply voltage is between 4.75 and 5.25 VDC at the sensor. See Fault Code 141.
>
> - Oil pressure is a function of the engine speed, oil level and regulator function. Operating the engine at a low speed under load will **not** cause the oil pressure to be low unless the oil is hot, at a low level, regulator has malfunctioned or a loss is occurring somewhere in the system.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the sensor accuracy. |  |
> |  | **STEP 1A.** Verify the sensor accuracy with a mechanical gauge. | Sensor reading is correct |
> | STEP 2. | Clear the fault code. |  |
> |  | **STEP 2A.** Disable the fault code. | Fault Code 415 inactive |
> |  | **STEP 2B.** Clear the inactive fault codes. | All the faults cleared |
>
> ### STEP 1. Check the sensor accuracy.
>
> #### STEP 1A. Verify the sensor accuracy with a mechanical gauge.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect a mechanical oil pressure gauge of known quality and calibration to the engine at one of the plugs on top of the oil filter head. Connect INSITE™, Part No. 3825145, to the data link. Start the engine and compare the oil pressure reading on the monitor screen to the reading on the mechanical oil pressure gauge. **NOTE:** The engine speed will have to be increased to make it easier to see the differences in the readings. | Sensor reading is correct. | 2A |
> | **Go To Fault Code 141** | Fault Code 141 |  |
>
> ### STEP 2. Clear the fault code.
>
> #### STEP 2A. Disable the fault code.
>
> | **Conditions:** Connect all the components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect all the components. Start the engine and let it idle for one minute. **NOTE:** If fault was at a particular speed, run engine at that speed to verify problem is corrected. | Fault Code 415 inactive | 2B |
> | Return to the troubleshooting steps or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
>
> #### STEP 2B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all the components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All the faults cleared | Repair complete |
> | **Troubleshoot any remaining active fault codes** | Appropriate troubleshooting chart |  |
