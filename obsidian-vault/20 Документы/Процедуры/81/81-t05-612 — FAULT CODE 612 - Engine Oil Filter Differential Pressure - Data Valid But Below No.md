---
type: "Процедура"
doc: "81-t05-612"
title_en: "FAULT CODE 612 - Engine Oil Filter Differential Pressure - Data Valid But Below Normal Operating Range - Most Severe Level"
modified: "2015-07-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-t05-612.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-t05-612.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# FAULT CODE 612 - Engine Oil Filter Differential Pressure - Data Valid But Below Normal Operating Range - Most Severe Level

> [!abstract] Процедура · `81-t05-612`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-t05-612.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-t05-612.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Устранение неисправностей кода. |  |
|  | **СТЭП 1А.** Ссылка на соответствующую процедуру. |  |
| ШАГ 2. | Очистите код ошибки. |  |
|  | **STEP 2A.** Отключить код ошибки. |  |
|  | **STEP 2B.** Очистить коды неактивных ошибок |  |

### ШАГ 1. Устранение неисправностей кода.

#### ШАГ 1A. Ссылка на соответствующую процедуру.

| **Условия:** |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Ссылка на ограничение фильтра моторного масла - дерево высоких симптомов в разделе TS этого руководства. | Ограничение фильтрации моторного масла в пределах спецификаций. | 2А |
| Ссылка на дерево симптомов «Ограничение фильтра моторного масла является высоким» в разделе TS этого руководства. | 1А |  |

### ШАГ 2. Очистите код ошибки.

#### ШАГ 2A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода 612. | Код 612 неактивен | 2В |
| Вернитесь к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 2B. Неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки всех кодов неактивных ошибок. | Все коды ошибок очищены | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Troubleshoot the fault code. |  |
> |  | **STEP 1A.** Reference the appropriate procedure. |  |
> | STEP 2. | Clear the fault code. |  |
> |  | **STEP 2A.** Disable the fault code. |  |
> |  | **STEP 2B.** Clear the inactive fault codes |  |
>
> ### STEP 1. Troubleshoot the fault code.
>
> #### STEP 1A. Reference the appropriate procedure.
>
> | **Conditions:** |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Reference the Lubricating Oil Filter Restriction is High symptom tree in Section TS of this manual. | Lubricating Oil Filter restriction within specifications. | 2A |
> | Reference the "Lubricating Oil Filter Restriction is High" symptom tree in Section TS of this manual. | 1A |  |
>
> ### STEP 2. Clear the fault code.
>
> #### STEP 2A. Disable the fault code.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to verify Fault Code 612 is inactive. | Fault Code 612 inactive | 2B |
> | Return to the troubleshooting steps, or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 2B. Clear inactive fault codes.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear inactive fault codes. Use INSITE™ electronic service tool to clear all inactive fault codes. | All fault codes cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
