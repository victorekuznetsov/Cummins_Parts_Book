---
aliases:
  - "Неверная передача данных от выносного блока ввода-вывода к блоку управления дизелем"
type: "Процедура"
doc: "116-t02-1116"
title_en: "Incorrect Data Link Transmission from Remote Input/Output Unit to Diesel Control Unit"
title_ru: "Неверная передача данных от выносного блока ввода-вывода к блоку управления дизелем"
modified: "2008-05-22"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1116.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1116.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Incorrect Data Link Transmission from Remote Input/Output Unit to Diesel Control Unit
**Неверная передача данных от выносного блока ввода-вывода к блоку управления дизелем**

> [!abstract] Процедура · `116-t02-1116`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1116.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1116.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Нет связи между удаленным блоком ввода/вывода и блоком DCU410.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс коробки проводов. |  |
|  | **STEP 1A.** Проверьте наличие проводов для передачи и возврата на открытом устройстве ModiconTM. |  |
|  | **STEP 1B.** Проверить напряжение на проводе питания удаленного входа/выхода на удаленном блоке ввода/вывода. |  |

### ШАГ 1. Проверьте клиентский интерфейс коробки проводов.

#### ШАГ 1A. Проверьте удаленный блок ввода/вывода ModiconTM, обеспечивающий подачу коммуникационных шины, и провода возврата для открытого доступа.

| **Условия:** Откройте окно интерфейса клиента. Отключите удаленный блок ввода/вывода ModiconTM, обеспечивающий подачу и возврат проводов в удаленном блоке ввода/вывода и блоке DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить провода подачи и возврата для открытого испытательного щупа Place One на проводе питания коммуникационной шины ModiconTM на удаленном входе/выходе в блоке DCU410. Поместите другой испытательный щуп на провод подачи коммуникационной шины ModiconTM удаленного ввода/вывода. Поместите один испытательный щуп на провод возврата коммуникационной шины ModiconTM удаленного ввода/вывода в блоке DCU410. Поместите другой испытательный щуп на провод возврата шины связи ModiconTM удаленного ввода/вывода. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (ящик пользовательского интерфейса) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1B. Проверьте напряжение на проводе питания удаленного входа / вывода на удаленном блоке ввода / вывода.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на проводе питания коммуникационной шины ModiconTM удаленного ввода/вывода. Поместите один испытательный щуп на провод подачи коммуникационной шины ModiconTM удаленного ввода/вывода. Поместите другой испытательный щуп на провод возврата шины связи ModiconTM удаленного ввода/вывода. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? *** Ремонт:** Проверить или заменить батареи. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - No communication between the remote input/output unit and the DCU410 unit.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box wiring. |  |
> |  | **STEP 1A.** Check the remote input/output unit Modicon™ communication bus supply and return wires for an open. |  |
> |  | **STEP 1B.** Check the voltage at the remote input/output unit supply wire at the remote input/output unit. |  |
>
> ### STEP 1. Check the customer interface box wiring.
>
> #### STEP 1A. Check the remote input/output unit Modicon™ communication bus supply and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the remote input/output unit Modicon™ communication bus supply and return wires at the remote input/output unit and DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply and return wires for an open Place one test lead on the remote input/output Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on the remote input/output Modicon™ communication bus supply wire at the remote input/output unit. Place one test lead on the remote input/output Modicon™ communication bus return wire at the DCU410 unit. Place the other test lead on the remote input/output Modicon™ communication bus return wire at the remote input/output unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1B. Check the voltage at the remote input/output unit supply wire at the remote input/output unit.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the remote input/output Modicon™ communication bus supply wire. Place one test lead on the remote input/output Modicon™ communication bus supply wire at the remote input/output unit. Place the other test lead on the remote input/output Modicon™ communication bus return wire at the remote input/output unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check or replace the batteries. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than +24-VDC? **NO** | Repair complete |  |
