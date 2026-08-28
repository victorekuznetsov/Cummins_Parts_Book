---
aliases:
  - "Зуммер блока останова не срабатывает при неисправности"
type: "Процедура"
doc: "116-t02-1109"
title_en: "Shutdown Unit Buzzer Does Not Activate with Fault"
title_ru: "Зуммер блока останова не срабатывает при неисправности"
modified: "2008-04-15"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1109.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1109.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Shutdown Unit Buzzer Does Not Activate with Fault
**Зуммер блока останова не срабатывает при неисправности**

> [!abstract] Процедура · `116-t02-1109`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1109.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1109.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Код ошибки, зарегистрированный без активации блока SDU410.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Входные сигналы SDU410 являются переключателями. Эти переключатели обычно открыты и закрыты при активации.

Зубец является внутренним для блока SDU410 и не имеет внешней проводов.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверка активных кодов неисправностей. | Какие-нибудь коды ошибок активны? |
| ШАГ 2. | Проверьте SDU410. |  |
|  | **STEP 2A.** Проверьте функцию зуммера в блоке SDU410. | Функционирует ли Buzzer? |
| ШАГ 3. | Сбросьте коды неисправностей. |  |
|  | **STEP 3A.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте наличие активных кодов неисправностей.

| **Условия:** Включить переключатель зажигания. Проверьте DCU410 на наличие активных кодов неисправностей. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие активных кодов неисправностей. | Есть ли активные коды неисправностей? **Ремонт:** Устранение неисправностей с помощью соответствующего кода ошибки. Для двигателей QSK19, обратитесь к Руководству по устранению неполадок и ремонту, Электронной системе управления, Модульные двигатели серии Common Rail System QSK19 CM850, Бюллетень 4021490. Для двигателей QSK38, QSK50 и QSK60, обратитесь к Руководству по устранению неполадок и ремонту, Электронной системе управления, QSK38, QSK50 и модульной общей железнодорожной системе QSK60 CM850, Бюллетень 4021533. | Ремонт завершён |
| Есть ли активные коды неисправностей? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте SDU410.

#### ШАГ 2A. Проверьте функцию зуммера в блоке SDU410.

| **Условия:** Код неисправности не зарегистрирован в блоке SDU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте функцию зуммера в блоке SDU410. | Функционирует ли Buzzer? *Да | 3А |
| Функционирует ли Buzzer? **NORepair:** Заменить модуль SDU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

### ШАГ 3. Сбросьте коды неисправностей.

#### ШАГ 3A. Сбросьте неактивные коды неисправностей.

| **Условия:** Включить переключатель зажигания. Проверьте блок DCU410 на наличие неактивных кодов неисправностей. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Проверьте неактивные коды неисправностей. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair:** Устранение неполадок с оставшимися кодами неисправностей. | Обратитесь в авторизованный сервисный центр Cummins®. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Fault code registered with no activation of SDU410 unit buzzer.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The SDU410 input signals are switches. These switches are normally open and closed when activated.
>
> The buzzer is internal to SDU410 unit and has no external wiring.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for active fault codes. | Any fault codes active? |
> | STEP 2. | Check the SDU410 unit. |  |
> |  | **STEP 2A.** Check for buzzer function at the SDU410 unit. | Does buzzer function? |
> | STEP 3. | Clear the fault codes. |  |
> |  | **STEP 3A.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for active fault codes.
>
> | **Conditions:** Turn keyswitch ON. Check the DCU410 for active fault codes. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for active fault codes. | Any active fault codes? **YESRepair:** Troubleshoot the appropriate fault code. For QSK19 engines, refer to the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021490. For QSK38, QSK50 and QSK60 engines, refer to the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60 CM850 Modular Common Rail System, Bulletin 4021533. | Repair complete |
> | Any active fault codes? **NO** | 2A |  |
>
> ### STEP 2. Check the SDU410 unit.
>
> #### STEP 2A. Check for buzzer function at the SDU410 unit.
>
> | **Conditions:** No fault code registered at the SDU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for buzzer function at the SDU410 unit. | Does buzzer function? **YES** | 3A |
> | Does buzzer function? **NORepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> ### STEP 3. Clear the fault codes.
>
> #### STEP 3A. Clear the inactive fault codes.
>
> | **Conditions:** Turn keyswitch ON. Check the DCU410 unit for inactive fault codes. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Check the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Contact a Cummins® Authorized Repair Location. |  |
