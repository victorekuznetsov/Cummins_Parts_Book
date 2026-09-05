---
type: "Процедура"
doc: "300-t02-1109"
title_en: "Shutdown Unit Buzzer Does Not Activate With Fault"
modified: "2019-05-22"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4332828"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1109.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1109.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
  - "перевод/машинный"
---

# Shutdown Unit Buzzer Does Not Activate With Fault

> [!abstract] Процедура · `300-t02-1109`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1109.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1109.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Код неисправности зарегистрирован без активации зуммера блока отключения.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Входные сигналы блока отключения являются переключателями. Эти переключатели обычно открыты. Они закрываются при активации. Зуммер является внутренним для блока отключения и не имеет внешней проводов.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверка активных кодов неисправностей. | Активные коды неисправностей? |
| ШАГ 2. | Проверьте блок отключения. |  |
|  | **STEP 2A.** Проверьте функцию зуммера в блоке отключения. | Функционирует ли Buzzer? |
| ШАГ 3. | Сбросьте коды неисправностей. |  |
|  | **STEP 3A.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте наличие активных кодов неисправностей.

| **Условия:** Включить переключатель зажигания. Проверьте панель управления на наличие активных кодов неисправностей. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие активных кодов неисправностей. | Активные коды неисправностей? **Ремонт: **Устранение неисправностей с помощью соответствующего кода ошибки. См. Руководство по устранению неполадок в коде CM850 морского вспомогательного QSB7-DM, Бюллетень 4325972, Раздел TF; или Руководство по устранению и ремонту неполадок в электронной системе управления ISM и QSM 11, Бюллетень [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Раздел TF; или Руководство по устранению неполадок в коде X15 CM2350 X125M, Бюллетень 5504346, Раздел TF; или информация об услугах производителя оборудования. | Ремонт завершён |
| Активные коды неисправностей? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте блок отключения.

#### ШАГ 2A. Проверьте функцию зуммера в блоке отключения.

| **Условия: **Код неисправности не зарегистрирован в блоке отключения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте функцию зуммера в блоке отключения. | Функционирует ли Buzzer? *Да | 3А |
| Функционирует ли Buzzer? **NORepair:** Заменить блок отключения. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

### ШАГ 3. Сбросьте коды неисправностей.

#### ШАГ 3A. Сбросьте неактивные коды неисправностей.

| **Условия:** Включить переключатель зажигания. Проверьте панель управления на наличие неактивных кодов неисправностей. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Проверьте неактивные коды неисправностей. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair:** Устранение неполадок с оставшимися кодами неисправностей. | Свяжитесь с авторизованным местом ремонта Cummins® |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Fault code registered with no activation of shutdown unit buzzer.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The shutdown unit input signals are switches. These switches are normally open. They are closed when activated. The buzzer is internal to the shutdown unit and has no external wiring.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for active fault codes. | Active fault codes? |
> | STEP 2. | Check the shutdown unit. |  |
> |  | **STEP 2A.** Check for buzzer function at the shutdown unit. | Does buzzer function? |
> | STEP 3. | Clear the fault codes. |  |
> |  | **STEP 3A.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for active fault codes.
>
> | **Conditions:** Turn keyswitch ON. Check the control panel for active fault codes. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for active fault codes. | Active fault codes? **YESRepair:** Troubleshoot the appropriate fault code. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF; or ISM and QSM 11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF; or X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346, Section TF; or the equipment manufacturer service information. | Repair complete |
> | Active fault codes? **NO** | 2A |  |
>
> ### STEP 2. Check the shutdown unit.
>
> #### STEP 2A. Check for buzzer function at the shutdown unit.
>
> | **Conditions:** No fault code registered at the shutdown unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for buzzer function at the shutdown unit. | Does buzzer function? **YES** | 3A |
> | Does buzzer function? **NORepair:** Replace the shutdown unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> ### STEP 3. Clear the fault codes.
>
> #### STEP 3A. Clear the inactive fault codes.
>
> | **Conditions:** Turn keyswitch ON. Check the control panel for inactive fault codes. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Check the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Contact a Cummins® Authorized Repair Location |  |
