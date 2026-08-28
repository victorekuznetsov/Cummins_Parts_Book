---
aliases:
  - "Неисправность сигнала давления масла на входе фильтра (для LLOYD's)"
type: "Процедура"
doc: "116-t02-1131"
title_en: "Lubricating Oil Filter Inlet Pressure Signal for LLOYD's Malfunction"
title_ru: "Неисправность сигнала давления масла на входе фильтра (для LLOYD's)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1131.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1131.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Lubricating Oil Filter Inlet Pressure Signal for LLOYD's Malfunction
**Неисправность сигнала давления масла на входе фильтра (для LLOYD's)**

> [!abstract] Процедура · `116-t02-1131`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1131.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1131.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Сигнал OEM для датчика LLOYD вышел из строя.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Этот датчик LLOYD подключен к OEM-стороне (разъем X7) удаленного блока ввода/вывода. OEM отвечает за эту связь.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте жгут проводов изготовителя машины. |  |
|  | **STEP 1A.** Проверить впускной сигнал давления фильтра моторного масла и подачу датчика +24-VDC проводов на наличие открытого. |  |
|  | **STEP 1B.** Проверьте входной сигнал давления фильтра моторного масла и подачу датчика +24-VDC проводов для короткого провода к проводу. |  |
|  | **STEP 1C.** Проверить впускной сигнальный провод моторного масла на короткое время до заземления. |  |
|  | **STEP 1D.** Проверьте впускной датчик давления фильтра моторного масла +24-VDC на напряжение. |  |

### ШАГ 1. Проверьте жгут проводов изготовителя машины.

#### ШАГ 1A. Проверьте фильтр моторного масла на входной сигнал давления и подачу датчика +24-VDC проводов для открытого.

| **Условия: **Отключите электропроводку OEM-производителя на разъеме X7. Отсоедините фильтр моторного масла от входного датчика давления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте фильтр моторного масла на входной сигнал давления и подачу датчика +24-VDC проводов для открытого. Поместите один испытательный щуп на контактный входной сигнал давления фильтра моторного масла на разъеме X7. Поместите другой испытательный щуп на фильтр моторного масла, входящий сигнал давления, контактирующий с разъемом датчика. Поместите один испытательный щуп на фильтр моторного масла, впускной датчик давления подачи +24-VDC штифт на разъеме X7. Поместите другой испытательный щуп на фильтр моторного масла, впускной датчик давления подачи +24-VDC штифт на разъем датчика. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 2B. Проверьте фильтр моторного масла на входном сигнале давления и датчике питания проводов +24-VDC для короткого провода к проводу.

| **Условия: **Отключите электропроводку OEM-производителя на разъеме X7. Отсоедините фильтр моторного масла от входного датчика давления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте фильтр моторного масла на входном сигнале давления и датчике питания проводов +24-VDC для короткого провода к проводу. Поместите один испытательный щуп на контактный входной сигнал давления фильтра моторного масла на разъеме X7. Поместите другой испытательный щуп на все другие штифты в разъем X7. Поместите один испытательный щуп на фильтр моторного масла, впускной датчик давления подачи +24-VDC штифт на разъеме X7. Поместите другой испытательный щуп на все другие штифты в разъем X7. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте фильтр моторного масла на входном сигнале давления и датчике подачи проводов +24-VDC для короткого заземления.

| **Условия: **Отключите электропроводку OEM-производителя на разъеме X7. Отсоедините фильтр моторного масла от входного датчика давления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте фильтр моторного масла на входном сигнале давления и датчике подачи проводов +24-VDC для короткого заземления. Поместите один испытательный щуп на контактный входной сигнал давления фильтра моторного масла на разъеме X7. Поместите другой испытательный щуп на землю двигателя. Поместите один испытательный щуп на датчик питания +24-VDC штифта на разъем X7. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте фильтр моторного масла на входе датчика давления питания +24-VDC провода на напряжение.

| **Условия:** Отсоединить разъем датчика давления на входе фильтра моторного масла. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте фильтр моторного масла на входе датчика давления питания +24-VDC провода на напряжение. Поместите один испытательный щуп на фильтр моторного масла, впускной датчик давления подачи +24-VDC штифт на разъем датчика. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | +24-VDC? **Ремонт:** Заменить датчик давления на входе фильтра моторного масла. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |
| +24-VDC? **Батарные батареи:** Проверить. См. сервисное руководство изготовителя машины. Заменить удаленный блок ввода/вывода. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The OEM signal for LLOYD's sensor has malfunctioned.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> This LLOYD's sensor is connected to the OEM side (X7 connector) of the remote input/output unit. The OEM is responsible for this connection.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the OEM wiring harness. |  |
> |  | **STEP 1A.** Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for an open. |  |
> |  | **STEP 1B.** Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for a wire-to-wire short. |  |
> |  | **STEP 1C.** Check the lubricating oil filter inlet pressure signal wire for a short to ground. |  |
> |  | **STEP 1D.** Check the lubricating oil filter inlet pressure sensor supply +24-VDC for voltage. |  |
>
> ### STEP 1. Check the OEM wiring harness.
>
> #### STEP 1A. Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for an open.
>
> | **Conditions:** Disconnect the OEM harness at the X7 connector. Disconnect the lubricating oil filter inlet pressure sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for an open. Place one test lead on the lubricating oil filter inlet pressure signal pin at the X7 connector. Place the other test lead on the lubricating oil filter inlet pressure signal pin at the sensor connector. Place one test lead on the lubricating oil filter inlet pressure sensor supply +24-VDC pin at the X7 connector. Place the other test lead on the lubricating oil filter inlet pressure sensor supply +24-VDC pin at the sensor connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 2B. Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for a wire-to-wire short.
>
> | **Conditions:** Disconnect the OEM harness at the X7 connector. Disconnect the lubricating oil filter inlet pressure sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for a wire-to-wire short. Place one test lead on the lubricating oil filter inlet pressure signal pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Place one test lead on the lubricating oil filter inlet pressure sensor supply +24-VDC pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for a short to ground.
>
> | **Conditions:** Disconnect the OEM harness at the X7 connector. Disconnect the lubricating oil filter inlet pressure sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for a short to ground. Place one test lead on the lubricating oil filter inlet pressure signal pin at the X7 connector. Place the other test lead on engine ground. Place one test lead on the sensor supply +24-VDC pin at the X7 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2D |  |
>
> #### STEP 2D. Check the lubricating oil filter inlet pressure sensor supply +24-VDC wire for voltage.
>
> | **Conditions:** Disconnect the lubricating oil filter inlet pressure sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the lubricating oil filter inlet pressure sensor supply +24-VDC wire for voltage. Place one test lead on the lubricating oil filter inlet pressure sensor supply +24-VDC pin at the sensor connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | +24-VDC? **YESRepair:** Replace the lubricating oil filter inlet pressure sensor. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |
> | +24-VDC? **NORepair:** Check the batteries. Refer to the OEM service manual. Replace the remote input/output unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
