---
aliases:
  - "Температура охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "94-fc146"
title_en: "Coolant Temperature - Engine Protection"
title_ru: "Температура охлаждающей жидкости — защита двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc146.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc146.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Coolant Temperature - Engine Protection
**Температура охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `94-fc146`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc146.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc146.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 146

### Температура охлаждающей жидкости — защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 146 PID(P): СПН: ФМИ: Лампа: СТО: | Температура охлаждающей жидкости двигателя превысила порог предупреждения о высокой температуре охлаждающей жидкости. | Никакого влияния на производительность. Общий предупредительный выход активизируется. Водитель реле с высокой температурой охлаждения заряжается энергией. |

![[19a00009.png]]

### Описание цепи

CTS используется электронным модулем управления (ECM) для мониторинга температуры охлаждающей жидкости двигателя. ECM контролирует напряжение на контакте сигнала и преобразует его в температурное значение. Температура охлаждающей жидкости используется ECM для системы защиты двигателя и управления заправкой.

### Расположение компонента

CTS расположен на стороне корпуса термостата.

### Практические замечания

- Убедитесь, что поток воздуха через радиатор не затрудняется.

- Сопротивление всех датчиков температуры изменяется в зависимости от температуры. Считывание, которое вы наблюдаете, должно быть сопоставимо со следующей таблицей, если датчик работает должным образом.

- Порог для предупреждения о температуре охлаждающей жидкости регулируется с помощью INSITETM, номер детали. 3825145. Убедитесь, что порог установлен на соответствующее значение.

| Температура (°С) | Температура \[°F\] | Сопротивление (Омс) |
|---|---|---|
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

## Предупреждения и меры предосторожности

> [!danger] ОПАСНО
>

**Подождите, пока температура охлаждающей жидкости не будет ниже 50°C \[120°F\], прежде чем удалять крышку радиатора системы охлаждающей жидкости или CTS. Неспособность сделать это может привести к травмам от нагреваемого спрея охлаждающей жидкости.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте точность датчика. |  |
|  | **STEP 1A.** Проверить точность датчика с помощью термопары или аналогичного датчика температуры. | Чтение датчиков правильное |
| ШАГ 2. | Очистите код ошибки. |  |
|  | **STEP 2A.** Отключить код ошибки. | Код 146 неактивен |
|  | **STEP 2B.** Очистить коды неактивных ошибок. | Все ошибки устранены |

### ШАГ 1. Проверьте точность датчика.

#### ШАГ 1A. Проверить точность датчика с помощью термопары или аналогичного датчика температуры.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подключите датчик температуры к двигателю рядом с CTS. Подключите Insite, номер детали. 3825145, к шине данных CAN. Сравните показания температуры охлаждающей жидкости на экране монитора рабочего инструмента с показаниями датчика температуры. **Примечание:** Если прибор для измерения температуры недоступен, то ответьте «ОК» на этот шаг. | Датчик показаний правильный. См. Руководство по устранению неполадок и ремонту базового двигателя для правильных спецификаций. | 2А |
| **Перейти к коду 145** | Код ошибки 145 |  |

### ШАГ 2. Очистите код ошибки.

#### ШАГ 2A. Отключите код неисправности.

| **Условия: **Соедините все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подключите все компоненты. Запустите двигатель и дайте ему прогреться до нормальной рабочей температуры, чтобы убедиться, что неисправность была исправлена. | Код 146 неактивен | 2В |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 2B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соедините все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Стирать неактивные коды неисправностей с помощью INSITETM, номер детали. 3825145. **Примечание:** Разъем шины данных CAN расположен на правом берегу корпуса маховика. | Все ошибки устранены. | Ремонт завершён |
| **Устранение неполадок с оставшимися активными кодами ошибок.** | Соответствующая диаграмма устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 146
>
> ### Coolant Temperature - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 146 PID(P): SPN: FMI: Lamp: SRT: | Engine coolant temperature has exceeded the warning threshold for high coolant temperature. | No effect on performance. Common Warning output is energized. Pre-High Coolant Temperature relay driver is energized. |
>
> ### Circuit Description
>
> The CTS is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The ECM monitors the voltage on the signal pin and converts this to a temperature value. The coolant temperature is used by the ECM for the engine protection system and fueling control.
>
> ### Component Location
>
> The CTS is located on the side of the thermostat housing.
>
> ### Shoptalk
>
> - Make sure the air flow through the radiator is **not** obstructed.
>
> - The resistance of all the temperature sensors varies with the temperature. The reading that you observe should compare to the following table if the sensor is functioning properly.
>
> - The threshold for the coolant temperature warning is adjustable with INSITE™, Part No. 3825145. Ensure the threshold is set to the appropriate value.
>
> | Temperature (° C) | Temperature \[° F\] | Resistance (ohms) |
> |---|---|---|
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
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the sensor accuracy. |  |
> |  | **STEP 1A.** Verify the sensor accuracy with a thermocouple or similar temperature probe. | Sensor reading is correct |
> | STEP 2. | Clear the fault code. |  |
> |  | **STEP 2A.** Disable the fault code. | Fault Code 146 inactive |
> |  | **STEP 2B.** Clear the inactive fault codes. | All faults cleared |
>
> ### STEP 1. Check the sensor accuracy.
>
> #### STEP 1A. Verify the sensor accuracy with a thermocouple or similar temperature probe.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect the temperature probe to the engine near the CTS. Connect INSITE™, Part No. 3825145, to the equipment data link. Compare the coolant temperature reading on the service tool monitor screen to the reading from the temperature probe. **NOTE:** If no temperature measuring device is available, then answer "OK" to this step. | Sensor reading is correct. Refer to the Base Engine Troubleshooting and Repair Manual for correct specifications. | 2A |
> | **Go to Fault code 145** | Fault code 145 |  |
>
> ### STEP 2. Clear the fault code.
>
> #### STEP 2A. Disable the fault code.
>
> | **Conditions:** Connect all the components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect all the components. Start the engine and let it warm up to normal operating temperature to verify that the fault has been fixed. | Fault Code 146 inactive | 2B |
> | Return to the troubleshooting steps or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
>
> #### STEP 2B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all the components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared. | Repair complete |
> | **Troubleshoot any remaining active fault codes.** | Appropriate troubleshooting chart |  |
