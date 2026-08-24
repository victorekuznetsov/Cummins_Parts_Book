---
aliases:
  - "Превышение частоты вращения — защита двигателя"
type: "Процедура"
doc: "94-fc234"
title_en: "Engine Overspeed - Engine Protection"
title_ru: "Превышение частоты вращения — защита двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc234.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc234.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Engine Overspeed - Engine Protection
**Превышение частоты вращения — защита двигателя**

> [!abstract] Процедура · `94-fc234`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc234.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc234.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 234

### Превышение частоты вращения — защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 234 PID(P): СПН: ФМИ: Лампа: СТО: | Сигнал датчика скорости двигателя (ESS) на контактах 21 и 22 разъёма электронного модуля управления (ECM) указывает на скорость двигателя, превышающую пороговое значение сигнализации (затвора). | Запорные клапаны отключения топлива обесточены (клапаны закрыты). Общий выход сигнализации активизирован. Водитель реле сверхскоростной передачи заряжается энергией. |

![[19a00001.png]]

### Описание цепи

Схема ESS обеспечивает сигнал скорости двигателя к ECM через электропроводку двигателя.

### Расположение компонента

ESS расположен в корпусе маховика.

### Практические замечания

Этот код неисправности указывает на то, что скорость двигателя была выше максимально допустимой скорости двигателя. Перегрузка двигателя может быть вызвана либо проблемой топливной системы, либо двигателем, приводимым в движение или приводимым в движение задним ходом, превышающим его максимально допустимую скорость.

Порог для отключения скорости двигателя регулируется с помощью INSITETM, номер детали. 3825145. Убедитесь, что порог установлен на соответствующее значение.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Определите причину превышения скорости. |  |
|  | **ШАГ 1А.** Проверить код ошибки 171. | Код 171 не указан |
|  | **ШАГ 1В.** Проверка на двигательную мощность (обратная мощность). | Двигатель не имеет обратного привода |
|  | **STEP 1C** Проверка альтернативного источника топлива. | Альтернативный источник топлива |
|  | **STEP 1D.** Проверьте обороты двигателя с помощью монитора. | Правильное чтение rpm |
| ШАГ 2. | Четкие коды ошибок. |  |
|  | **STEP 2A.** Отключить код ошибки. | Код 234 неактивен |
|  | **STEP 2B.** Очистить коды неактивных ошибок. | Все ошибки устранены |

### ШАГ 1. Определите причину превышения скорости.

#### ШАГ 1A. Проверить код ошибки 171.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Прочитайте коды неисправностей с помощью INSITETM, номер детали. 3825145. | Код 171 не указан | 1В |
|  | Перейти к коду 171 |  |

#### ШАГ 1B. Проверьте двигатель (обратная мощность).

| ** Условия:** |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте данные снимка для указания обратной мощности. | Двигатель не имеет обратного привода | 1С |
| ** Проверьте двигатель на предмет повреждений, вызванных превышением скорости.** | 2А |  |

#### ШАГ 1C. Проверьте альтернативный источник топлива.

| **Условия: ** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
|  | Альтернативный источник топлива | 1D |
| ** Найдите альтернативный источник топлива и удалите любой альтернативный источник топлива. | 2А |  |

#### ШАГ 1D. Проверьте обороты двигателя с помощью монитора инструмента.

| **Условия: ** Переключатель стоп/бега в положении «РУН». |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Мониторинг оборотов двигателя с помощью INSITETM, номер детали. 3825145. | Правильное чтение rpm | 2А |
| ** Осмотрите датчик скорости двигателя** См. процедуру 019-042. | 2А |  |

### ШАГ 2. Четкие коды ошибок.

#### ШАГ 2A. Отключите код неисправности.

| **Условия: ** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Соедините все компоненты. Запуск двигателя и холостость в течение одной минуты. Проверить, что код 234 неактивен. | Код 234 неактивен. | 2В |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 2B. Неактивные коды неисправностей.

| **Условия: ** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Стирать неактивные коды неисправностей с помощью INSITETM, номер детали. 3825145. **Примечание:** Разъем шины данных CAN расположен на правом берегу корпуса маховика. | Все ошибки устранены | Ремонт завершён |
| **Устранение любых оставшихся активных недостатков.** | Соответствующая диаграмма устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 234
>
> ### Engine Overspeed - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 234 PID(P): SPN: FMI: Lamp: SRT: | Engine Speed Sensor (ESS) signal on pins 21 and 22 of the engine harness electronic control module (ECM) connector indicates engine speed greater than alarm (shutdown) threshold. | Fuel shutoff valves are de-energized (valves closed). Common Alarm output is energized. Overspeed relay driver is energized. |
>
> ### Circuit Description
>
> The ESS circuit provides the engine speed signal to the ECM through the engine harness.
>
> ### Component Location
>
> The ESS is located in the flywheel housing.
>
> ### Shoptalk
>
> This fault code indicates that the engine speed was above the maximum allowable engine speed. An engine overspeed can be caused by either a fuel system problem or the engine being driven or reverse powered past its maximum allowable speed.
>
> The threshold for the engine overspeed shutdown is adjustable with INSITE™, Part No. 3825145. Ensure the threshold is set to the appropriate value.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Identify the reason for the overspeed. |  |
> |  | **STEP 1A.** Check for Fault Code 171. | Fault Code 171 not present |
> |  | **STEP 1B.** Check for motoring of engine (reverse power). | Engine not reverse powered |
> |  | **STEP 1C.** Check for alternate fuel source. | No alternate fuel source |
> |  | **STEP 1D.** Check engine rpm with service tool monitor. | Correct rpm reading |
> | STEP 2. | Clear fault codes. |  |
> |  | **STEP 2A.** Disable the fault code. | Fault Code 234 inactive |
> |  | **STEP 2B.** Clear the inactive fault codes. | All faults cleared |
>
> ### STEP 1. Identify the reason for the overspeed.
>
> #### STEP 1A. Check for Fault Code 171.
>
> | **Conditions:** Stop/Run switch in the “STOP” position. Controller in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes using INSITE™, Part No. 3825145. | Fault Code 171 not present | 1B |
> |  | Go to Fault Code 171 |  |
>
> #### STEP 1B. Check for motoring of engine (reverse power).
>
> | **Conditions:** |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check snapshot data for indications of reverse power. | Engine not reverse powered | 1C |
> | **Check engine for damage caused by overspeed condition.** | 2A |  |
>
> #### STEP 1C. Check for alternate fuel source.
>
> | **Conditions:** Stop/Run switch in the “STOP” position. Controller not in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> |  | No alternate fuel source | 1D |
> | **Locate the alternate fuel source.** Locate and remove any alternate fuel source. | 2A |  |
>
> #### STEP 1D. Check engine rpm with service tool monitor.
>
> | **Conditions:** Stop/Run switch in the “RUN” position. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Monitor the engine rpm using INSITE™, Part No. 3825145. | Correct rpm reading | 2A |
> | **Inspect engine speed sensor** Refer to Procedure 019-042. | 2A |  |
>
> ### STEP 2. Clear fault codes.
>
> #### STEP 2A. Disable the fault code.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect all components. Start the engine and idle for one minute. Verify Fault Code 234 is inactive. | Fault Code 234 inactive. | 2B |
> | Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 2B. Clear inactive fault codes.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared | Repair complete |
> | **Troubleshoot any remaining active fault Faults.** | Appropriate troubleshooting chart |  |
