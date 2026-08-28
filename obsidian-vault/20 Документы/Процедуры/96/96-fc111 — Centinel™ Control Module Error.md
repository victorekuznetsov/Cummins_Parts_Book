---
aliases:
  - "Ошибка блока управления Centinel™"
type: "Процедура"
doc: "96-fc111"
title_en: "Centinel™ Control Module Error"
title_ru: "Ошибка блока управления Centinel™"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# Centinel™ Control Module Error
**Ошибка блока управления Centinel™**

> [!abstract] Процедура · `96-fc111`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-03-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc111.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 111

### Ошибка блока управления Centinel™

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 111 PID(P): СПН: ФМИ: Лампа: Нет, не srt: | Ошибка блока управления Centinel™. Ошибка произошла во время диагностического испытания внутреннего аппаратного модуля управления CentinelTM. | Система CentinelTM будет работать некорректно. |

![[05800058.png]]

### Описание цепи

Модуль управления CentinelTM — это компьютер, который отвечает за управление системой CentinelTM и диагностику.

### Расположение компонента

Тяжелая работа: Модуль управления CentinelTM расположен на масляном баке системы CentinelTM.

Высокая мощность: Модуль управления CentinelTM расположен на кронштейне установки клапана управления маслом системы CentinelTM.

### Практические замечания

Этот код неисправности может быть вызван только *** внутренней проблемой модуля управления CentinelTM. **Только на высокой мощности, если вы попытаетесь очистить код ошибки с помощью вилки службы. Ремонт невозможен для модуля управления CentinelTM.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

Чтобы избежать повреждения нового модуля управления CentinelTM, необходимо изучить все другие коды активных неисправностей до замены модуля управления CentinelTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Код 111 неактивен |
|  | **СТЭП 1В.** Проверьте коды неисправностей. | Полный комплект |

### ШАГ 1. Проверьте коды неисправностей. (Этот шаг только для высокопроизводительных. Для тяжелых работ, продолжайте шаг 1B.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Высокомощные только Соединяют все компоненты. Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды неисправностей с помощью диагностической лампы. | Код 111 неактивен | Полный комплект |
| Высокомощные **только**: Очистите коды неисправностей с помощью вилки службы. См. процедуру[[96-209-001 — System Description\|209-001]]. | 1В |  |

#### ШАГ 1B. Проверьте коды неисправностей.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте код ошибки. | Код 111 неактивен | Полный комплект |
| Заменить модуль управления CentinelTM См. процедуру[[96-019-130-tr — Centinel™ Control Module\|019-130]]. | Полный комплект |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 111
>
> ### Centinel™ Control Module Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 111 PID(P): SPN: FMI: Lamp: None SRT: | Centinel™ Control Module Error. An error occurred during the diagnostic test of the Centinel™ control module internal hardware. | The Centinel™ system will **not** operate properly. |
>
> ### Circuit Description
>
> The Centinel™ control module is a computer that is responsible for Centinel™ system control and diagnostics.
>
> ### Component Location
>
> Heavy-duty: The Centinel™ control module is located on the Centinel™ system make-up oil tank.
>
> High-horsepower: The Centinel™ control module is located on the Centinel™ system oil control valve mounting bracket.
>
> ### Shoptalk
>
> This fault code can be caused **only** by an internal Centinel™ control module problem. **Only** on high-horsepower should you try to clear a fault code with use of the service plug. Repairs are **not** possible for the Centinel™ control module.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To avoid damaging a new Centinel™ control module, all other active fault codes must be investigated prior to replacing the Centinel™ control module.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Code 111 inactive |
> |  | **STEP 1B.** Check the fault codes. | Complete |
>
> ### STEP 1. Check the fault codes. (This step is for high-horsepower only. For heavy-duty, continue to Step 1B.)
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** High-horsepower only Connect all components. Turn the keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes using diagnostic lamp. | Fault Code 111 inactive | Complete |
> | High-horsepower **only**: Clear the fault codes with the service plug. Refer to Procedure [[96-209-001 — System Description\|209-001]]. | 1B |  |
>
> #### STEP 1B. Check the fault codes.
>
> | **Conditions:** Turn the keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault code. | Fault Code 111 inactive | Complete |
> | Replace the Centinel™ control module Refer to Procedure [[96-019-130-tr — Centinel™ Control Module\|019-130]]. | Complete |  |
