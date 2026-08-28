---
aliases:
  - "Требуется замена масла"
type: "Процедура"
doc: "96-fc649"
title_en: "Oil Change Required"
title_ru: "Требуется замена масла"
modified: "2004-03-03"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc649.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc649.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# Oil Change Required
**Требуется замена масла**

> [!abstract] Процедура · `96-fc649`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-03-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc649.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc649.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 649

### Требуется замена масла

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 649 PID(P): СПН: ФМИ: Лампа: Красная СТО: | Требуется замена масла. Модуль управления CentinelTM обнаружил сигнал от ECM, требуемый для изменения масла. | Система CentinelTM будет работать **не**. |

![[05800058.png]]

### Описание цепи

Модуль управления CentinelTM отслеживает динамику двигателя с помощью информации от электронного модуля управления (ECM). Если масло требует изменения, модуль управления CentinelTM покажет неисправность.

### Расположение компонента

Тяжелая работа: Модуль управления CentinelTM расположен на масляном баке системы CentinelTM.

Высокая мощность: Модуль управления CentinelTM расположен на кронштейне установки клапана управления маслом системы CentinelTM.

### Практические замечания

Замена масла устанавливается, если в течение некоторого времени существовала другая неисправность. Убедитесь, что все неисправности были устранены, и убедитесь, что масло и фильтр изменены до устранения неисправности.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Код ошибки 649 активен. |
| ШАГ 2. | Сбросьте коды неисправностей. |  |
|  | **STEP 2A.** Отключить код ошибки. | Код 649 неактивен. |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. Двигатель не работает |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Тяжелая и высокая мощность: Измените масло и фильтр. Высокая мощность: Проверьте использование масла против топлива. | Тяжелая сыпь: Измените масло и фильтр Высокое энергопотребление: изменение масла и фильтра Стандартное масло = 300 галлонов топлива до 1 галлона масла Продвинутое масло = 400 галлонов топлива до 1 галлона масла. | 2А |
| **Высоколошадные: Проверить использование масла по сравнению с использованием топлива** Перенастроить параметр рабочего цикла модуля управления CentinelTM с помощью INSITETM, повысив рабочий цикл на один уровень. Три уровня: легкий 45 процентов, средний 75 процентов и тяжелый 95 процентов. | Тяжелая работа: Полная мощность: 2А |  |

### ШАГ 2. Очистить коды неисправностей,

#### ШАГ 2A. Отключите коды неисправностей,

| **Условия:** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Чтобы устранить необходимость замены масла. См. 007-999. Подключите все компоненты. Запустите двигатель и отпустите на 1 минуту. Убедитесь, что код 649 неактивен. | Код 649 неактивен | Полный комплект |
| Вернитесь к этапу устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все этапы были завершены и проверены снова. | 1А |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 649
>
> ### Oil Change Required
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 649 PID(P): SPN: FMI: Lamp: Red SRT: | Oil Change Required. The Centinel™ control module detected an Oil Change Required signal from the ECM. | The Centinel™ system will **not** operate. |
>
> ### Circuit Description
>
> The Centinel™ control module monitors the engine dynamics via information from the electronic control module (ECM). If the oil requires changing, the Centinel™ control module will display a fault.
>
> ### Component Location
>
> Heavy-duty: The Centinel™ control module is located on the Centinel™ system make-up oil tank.
>
> High-horsepower: The Centinel™ control module is located on the Centinel™ system oil control valve mounting bracket.
>
> ### Shoptalk
>
> The oil change required is set if another fault existed for some time. Make certain all faults have been cleared and make certain the oil and filter are changed before clearing the fault.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Code 649 active. |
> | STEP 2. | Clear the fault codes. |  |
> |  | **STEP 2A.** Disable the fault code. | Fault Code 649 inactive. |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Turn the keyswitch ON. Engine is not running |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Heavy-duty and high-horsepower: Change the oil and filter. High-horsepower: Check oil versus fuel usage. | Heavy-Duty: change oil and filter High-Horsepower: change oil and filter Standard oil = 300 gallons of fuel to 1 gallon of oil Advanced oil = 400 gallons of fuel to 1 gallon of oil. | 2A |
> | **High-horsepower: Check oil usage versus fuel usage** Recalibrate the Centinel™ control module duty cycle parameter using INSITE™, raising the duty cycle up one level. Three levels, light 45 percent, medium 75 percent, and heavy 95 percent. | Heavy-duty: Complete High-horsepower: 2A |  |
>
> ### STEP 2. Clear the fault codes,
>
> #### STEP 2A. Disable the fault codes,
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the oil change required fault. Refer to 007-999. Connect all the components. Start the engine and let idle for 1 minute. Verify that Fault Code 649 is inactive. | Fault Code 649 inactive | Complete |
> | Return to the troubleshooting step or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
