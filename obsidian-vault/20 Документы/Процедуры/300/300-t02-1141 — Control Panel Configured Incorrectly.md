---
type: "Процедура"
doc: "300-t02-1141"
title_en: "Control Panel Configured Incorrectly"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
  - "перевод/машинный"
---

# Control Panel Configured Incorrectly

> [!abstract] Процедура · `300-t02-1141`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1141.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Панель управления неправильно настроена для применения двигателя.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Этот код неисправности не имеет внешней проводов от панели управления, за исключением блока питания панели управления +24 VDC.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс (C.I.B.) проводов. |  |
|  | **STEP 1A.** Проверьте дисплеи панели управления на наличие неисправностей. | Панель управления указывает на неисправность (неисправности)? |
|  | **ШАГ 1А-1.** Проверьте питание панели управления Проводом SUPPLY на напряжение +24 ВДК. | Меньше +24 VDC? |

### ШАГ 1. Проверьте клиентский интерфейс (C.I.B.) проводов.

#### ШАГ 1A. Проверьте дисплей панели управления на наличие неисправностей.

| **Условия: **Найдите дисплей панели управления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей панели управления на наличие неисправностей. | Панель управления указывает на неисправность (неисправности)? **Ремонт: **Устранение неисправностей с помощью соответствующего кода ошибки. Ссылка на Руководство по устранению неполадок в коде QSB7-DM CM850, Бюллетень 4325972, Раздел TF; или Руководство по устранению и ремонту неполадок в электронной системе управления ISM и QSM 11, Бюллетень [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Раздел TF; или Руководство по устранению неполадок в коде X15 CM2350 X125M, Бюллетень 5504346, Раздел TF. | Ремонт завершён |
| Панель управления указывает на неисправность (неисправности)? **НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте питание панели управления SUPPLY провода на напряжение +24 VDC.

| **Условия: **Открыть ЦБ. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжение (переключенная мощность) провода на панели управления. Поместите один испытательный щуп на напряжение батареи 1 (переключенная мощность) Провода SUPPLY на панели управления. Поместите другой испытательный щуп на землю панели. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24 VDC? **Ремонт:** Проверить аккумуляторы. См. сервисную документацию изготовителя оборудования. | Ремонт завершён |
| Меньше +24 VDC? **НЕТ** | Обратитесь в авторизованный сервисный центр Cummins®. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The control panel is configured incorrectly for the engine application.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> This fault code has no external wiring from the control panel except the +24 VDC control panel power supply.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box (C.I.B.) wiring. |  |
> |  | **STEP 1A.** Check the control panel display for faults. | Control panel indicates fault(s)? |
> |  | **STEP 1A-1.** Check the control panel power SUPPLY wire for voltage +24 VDC. | Less than +24 VDC? |
>
> ### STEP 1. Check the customer interface box (C.I.B.) wiring.
>
> #### STEP 1A. Check the control panel display for faults.
>
> | **Conditions:** Locate the control panel display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the control panel display for faults. | Control panel indicates fault(s)? **YESRepair:** Troubleshoot the appropriate fault code. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF; or ISM and QSM 11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF; or X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346, Section TF. | Repair complete |
> | Control panel indicates fault(s)? **NO** | 1A-1 |  |
>
> #### STEP 1A-1. Check the control panel power SUPPLY wire for voltage +24 VDC.
>
> | **Conditions:** Open the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the battery 1 voltage (switched power) wire at the control panel. Place one test lead at the battery 1 voltage (switched power) SUPPLY wire at the control panel. Place the other test lead on the panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24 VDC? **YESRepair:** Check the batteries. See equipment manufacturer service information. | Repair complete |
> | Less than +24 VDC? **NO** | Contact a Cummins® Authorized Repair Location. |  |
