---
aliases:
  - "Блок управления дизелем сконфигурирован неверно"
type: "Процедура"
doc: "116-t02-1141"
title_en: "Diesel Control Unit Configured Incorrectly"
title_ru: "Блок управления дизелем сконфигурирован неверно"
modified: "2008-07-30"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Diesel Control Unit Configured Incorrectly
**Блок управления дизелем сконфигурирован неверно**

> [!abstract] Процедура · `116-t02-1141`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-07-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1141.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Блок DCU410 неправильно настроен для применения в двигателе.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Этот код неисправности не имеет внешней проводов от блока DCU410, за исключением блока питания +24-VDC DCU410.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс коробки проводов. |  |
|  | **STEP 1A.** Проверьте дисплей блока DCU410 на наличие неисправностей. | DCU410 указывает на неисправность (неисправности)? |
|  | **STEP 1A-1.** Проверьте источник питания DCU410 на напряжение +24-VDC. | Меньше +24-VDC? |

### ШАГ 1. Проверьте клиентский интерфейс коробки проводов.

#### ШАГ 1A. Проверьте дисплей блока DCU410 на наличие неисправностей.

| **Условия: ** Найдите дисплей блока DCU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте дисплей блока DCU410 на наличие неисправностей. | DCU410 указывает на неисправность (неисправности)? ** Ремонт системы электронного управления см. Руководство по устранению неполадок и ремонту, модульный двигатель серии Common Rail System QSK19 CM850, бюллетень 4021493 или руководство по устранению и ремонту системы электронного управления, QSK38, QSK50 и модульный двигатель серии Common Rail System QSK60 CM850, бюллетень 4021533. | Ремонт завершён |
| DCU410 указывает на неисправность (неисправности)? ** НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте провод питания DCU410 на напряжение +24-VDC.

| **Условия: ** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте напряжение на проводе напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? *** Ремонт:** Проверить аккумуляторы. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Меньше +24-VDC? ** НЕТ** | Обратитесь в авторизованный сервисный центр Cummins®. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The DCU410 unit is configured incorrectly for the engine application.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> This fault code has no external wiring from the DCU410 unit except the +24-VDC DCU410 unit power supply.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box wiring. |  |
> |  | **STEP 1A.** Check the DCU410 unit display for faults. | DCU410 unit indicates fault(s)? |
> |  | **STEP 1A-1.** Check the DCU410 power supply for voltage +24-VDC. | Less than +24-VDC? |
>
> ### STEP 1. Check the customer interface box wiring.
>
> #### STEP 1A. Check the DCU410 unit display for faults.
>
> | **Conditions:** Locate the DCU410 unit display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 unit display for faults. | DCU410 unit indicates fault(s)? **YESRepair:** Refer to the Electronic Control System Troubleshooting and Repair Manual, QSK19 CM850 Modular Common Rail System Series Engine, Bulletin 4021493 or the Electronic Control System Troubleshooting and Repair Manual, QSK38, QSK50, and QSK60 CM850 Modular Common Rail System Series Engine, Bulletin 4021533. | Repair complete |
> | DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |
>
> #### STEP 1A-1. Check the DCU410 power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the battery 1 voltage (switched power) wire at the DCU410 unit. Place one test lead at the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | Contact a Cummins® Authorized Repair Location. |  |
