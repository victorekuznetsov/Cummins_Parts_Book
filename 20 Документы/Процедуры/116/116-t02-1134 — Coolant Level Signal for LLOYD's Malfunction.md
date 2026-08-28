---
aliases:
  - "Неисправность сигнала уровня ОЖ (для LLOYD's)"
type: "Процедура"
doc: "116-t02-1134"
title_en: "Coolant Level Signal for LLOYD's Malfunction"
title_ru: "Неисправность сигнала уровня ОЖ (для LLOYD's)"
modified: "2008-07-11"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1134.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1134.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Coolant Level Signal for LLOYD's Malfunction
**Неисправность сигнала уровня ОЖ (для LLOYD's)**

> [!abstract] Процедура · `116-t02-1134`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-07-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1134.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1134.pdf)

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
|  | **STEP 1A.** Проверить уровень охлаждающей жидкости и подачу датчика +24-VDC проводов на наличие открытого источника. |  |
|  | **STEP 1B.** Проверьте уровень охлаждающей жидкости и датчик питания +24-VDC проводов для провода к проводу короткой. |  |
|  | **STEP 1C** Проверить уровень охлаждающей жидкости на короткое время до заземления. |  |
|  | **STEP 1D.** Проверьте подачу датчика уровня охлаждающей жидкости +24-VDC на напряжение. |  |

### ШАГ 1. Проверьте жгут проводов изготовителя машины.

#### ШАГ 1A. Проверьте уровень охлаждающей жидкости сигнала и датчика питания +24-VDC проводов для открытого.

| **Условия:** Отключите электропроводку OEM-производителя на разъеме X7. Отключите разъем датчика уровня охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте уровень охлаждающей жидкости сигнала и датчика питания +24-VDC проводов для открытого. Поместите один испытательный щуп на контакт сигнала уровня охлаждающей жидкости на разъеме X7. Поместите другой испытательный щуп на контакт сигнала уровня охлаждающей жидкости на разъем датчика. Поместите один испытательный щуп на датчик уровня охлаждающей жидкости, подаваемый +24-VDC на разъем X7. Поместите другой испытательный щуп на датчик уровня охлаждающей жидкости, подаваемый +24-VDC, на разъем датчика. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 2B. Проверьте уровень охлаждающей жидкости сигнала и датчика питания +24-VDC проводов для провода к проводу короткой.

| **Условия:** Отключите электропроводку OEM-производителя на разъеме X7. Отключите разъем датчика уровня охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте уровень охлаждающей жидкости сигнала и датчика питания +24-VDC проводов для провода к проводу короткой. Поместите один испытательный щуп на контакт сигнала уровня охлаждающей жидкости на разъеме X7. Поместите другой испытательный щуп на все другие штифты в разъем X7. Поместите один испытательный щуп на датчик уровня охлаждающей жидкости, подаваемый +24-VDC на разъем X7. Поместите другой испытательный щуп на все другие штифты в разъем X7. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте уровень охлаждающей жидкости сигнала и датчика питания +24-VDC проводов для короткого наземного.

| **Условия:** Отключите электропроводку OEM-производителя на разъеме X7. Отключите разъем датчика уровня охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте уровень охлаждающей жидкости сигнала и датчика питания +24-VDC проводов для короткого наземного. Поместите один испытательный щуп на контакт сигнала уровня охлаждающей жидкости на разъеме X7. Поместите другой испытательный щуп на землю двигателя. Поместите один испытательный щуп на датчик питания +24-VDC штифта на разъем X7. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте уровень охлаждающей жидкости датчика питания +24-VDC провода для напряжения.

| **Условия:** Отключить разъем датчика уровня охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте уровень охлаждающей жидкости датчика питания +24-VDC провода для напряжения. Поместите один испытательный щуп на датчик уровня охлаждающей жидкости +24-VDC на разъем датчика. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | +24-VDC?  Заменить датчик уровня охлаждающей жидкости. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |
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
> |  | **STEP 1A.** Check the coolant level signal and sensor supply +24-VDC wires for an open. |  |
> |  | **STEP 1B.** Check the coolant level signal and sensor supply +24-VDC wires for a wire-to-wire short. |  |
> |  | **STEP 1C.** Check the coolant level signal wire for a short to ground. |  |
> |  | **STEP 1D.** Check the coolant level sensor supply +24-VDC for voltage. |  |
>
> ### STEP 1. Check the OEM wiring harness.
>
> #### STEP 1A. Check the coolant level signal and sensor supply +24-VDC wires for an open.
>
> | **Conditions:** Disconnect the OEM harness at the X7 connector. Disconnect the coolant level sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant level signal and sensor supply +24-VDC wires for an open. Place one test lead on the coolant level signal pin at the X7 connector. Place the other test lead on the coolant level signal pin at the sensor connector. Place one test lead on the coolant level sensor supply +24-VDC pin at the X7 connector. Place the other test lead on the coolant level sensor supply +24-VDC pin at the sensor connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 2B. Check the coolant level signal and sensor supply +24-VDC wires for a wire-to-wire short.
>
> | **Conditions:** Disconnect the OEM harness at the X7 connector. Disconnect the coolant level sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant level signal and sensor supply +24-VDC wires for a wire-to-wire short. Place one test lead on the coolant level signal pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Place one test lead on the coolant level sensor supply +24-VDC pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the coolant level signal and sensor supply +24-VDC wires for a short to ground.
>
> | **Conditions:** Disconnect the OEM harness at the X7 connector. Disconnect the coolant level sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant level signal and sensor supply +24-VDC wires for a short to ground. Place one test lead on the coolant level signal pin at the X7 connector. Place the other test lead on engine ground. Place one test lead on the sensor supply +24-VDC pin at the X7 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2D |  |
>
> #### STEP 2D. Check the coolant level sensor supply +24-VDC wire for voltage.
>
> | **Conditions:** Disconnect the coolant level sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant level sensor supply +24-VDC wire for voltage. Place one test lead on the coolant level sensor supply +24-VDC pin at the sensor connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | +24-VDC? **YESRepair:** Replace the coolant level sensor. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |
> | +24-VDC? **NORepair:** Check the batteries. Refer to the OEM service manual. Replace the remote input/output unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
