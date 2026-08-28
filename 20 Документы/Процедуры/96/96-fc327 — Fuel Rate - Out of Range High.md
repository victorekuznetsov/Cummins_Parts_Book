---
aliases:
  - "Расход топлива выше диапазона"
type: "Процедура"
doc: "96-fc327"
title_en: "Fuel Rate - Out of Range High"
title_ru: "Расход топлива выше диапазона"
modified: "2004-02-25"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc327.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc327.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# Fuel Rate - Out of Range High
**Расход топлива выше диапазона**

> [!abstract] Процедура · `96-fc327`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc327.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc327.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 327

### Расход топлива выше диапазона

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 327 P(P): СПН: ФМИ: Лампа: Красная СТО: | Расход топлива выше диапазона. Модуль управления CentinelTM обнаружил высокую скорость подачи топлива из диапазона высокого сигнала от электронного модуля управления (ECM). | Система CentinelTM будет работать некорректно. |

![[05800058.png]]

### Описание цепи

Модуль управления CentinelTM отслеживает динамику двигателя с помощью информации от электронного модуля управления (ECM). Если расход топлива не в диапазоне, модуль управления CentinelTM покажет неисправность.

### Расположение компонента

Тяжелая сыпь: Модуль управления CentinelTM расположен на масляном баке системы CentinelTM.

Высоколошадные: Модуль управления CentinelTM расположен на кронштейне установки клапана управления маслом системы CentinelTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Данные по расходу топлива ОК |
| ШАГ 2. | Очистите код ошибки. |  |
|  | **STEP 2A.** Отключить код ошибки. | Код 327 неактивен |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте наличие активных кодов неисправностей.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверять данные о расходе топлива ECM с помощью инструментария электронного обслуживания INSITETM. | **Данные о скорости топлива ОК** | 2А |
| **Перепрограммировать ECM** См. процедуру[[105-019-032 — Engine Control Module Calibration Code\|019-032]]и руководство пользователя INSITETM. | 2А |  |

### ШАГ 2. Очистите код ошибки.

#### ШАГ 2A. Отключите код неисправности.

| **Условия:** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подключите все компоненты. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Проверить код 327 неактивен. | **Код ошибки 327 неактивен** | Полный комплект |
| Вернитесь к этапу устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все этапы были завершены и проверены снова. | 1А |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 327
>
> ### Fuel Rate - Out of Range High
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 327 PID(P): SPN: FMI: Lamp: Red SRT: | Fuel Rate - Out of Range High. The Centinel™ control module detected a fuel rate out of range high signal from the electronic control module (ECM). | The Centinel™ system will **not** operate properly. |
>
> ### Circuit Description
>
> The Centinel™ control module monitors the engine dynamics via information from the electronic control module (ECM). If the fuel rate is out of range, the Centinel™ control module will display a fault.
>
> ### Component Location
>
> Heavy-Duty: The Centinel™ control module is located on the Centinel™ system make-up oil tank.
>
> High-Horsepower: The Centinel™ control module is located on the Centinel™ system oil control valve mounting bracket.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fuel rate data OK |
> | STEP 2. | Clear the fault code. |  |
> |  | **STEP 2A.** Disable the fault code. | Fault Code 327 inactive |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for active fault codes.
>
> | **Conditions:** Turn the keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify ECM fuel rate data using INSITE™ electronic service tool. | **Fuel rate data OK** | 2A |
> | **Reprogram the ECM** Refer to Procedure [[105-019-032 — Engine Control Module Calibration Code\|019-032]] and the INSITE™ user manual. | 2A |  |
>
> ### STEP 2. Clear the fault code.
>
> #### STEP 2A. Disable the fault code.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect all the components. Start the engine and let it idle for 1 minute. Verify Fault Code 327 is inactive. | **Fault Code 327 inactive** | Complete |
> | Return to the troubleshooting step or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
