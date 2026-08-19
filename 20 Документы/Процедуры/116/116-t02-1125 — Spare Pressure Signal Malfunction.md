---
aliases:
  - "Неисправность резервного сигнала давления"
type: "Процедура"
doc: "116-t02-1125"
title_en: "Spare Pressure Signal Malfunction"
title_ru: "Неисправность резервного сигнала давления"
modified: "2008-05-22"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1125.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1125.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Spare Pressure Signal Malfunction
**Неисправность резервного сигнала давления**

> [!abstract] Процедура · `116-t02-1125`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1125.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1125.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Датчик давления OEM неисправен.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Запасной датчик давления подключен к разъему сигнализации и безопасности C4, расположенному на окне интерфейса клиента.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс коробки проводов. |  |
|  | **STEP 1A.** Проверить запасной сигнал давления и подачу датчика +24-VDC проводов на наличие открытого. |  |
|  | **STEP 1B.** Проверьте запасной сигнал давления и датчик питания +24-VDC проводов для провода к проводу короткой. |  |
|  | **STEP 1C** Проверить запасной сигнал давления на короткое время до земли. |  |
| ШАГ 2. | Проверьте жгут проводов изготовителя машины. |  |
|  | **STEP 2A.** Проверьте запасной сигнал давления и подачу датчика +24-VDC провода на наличие открытого сигнала. |  |
|  | **STEP 2B.** Проверьте запасной сигнал давления и датчик питания +24-VDC проводов для провода к проводу короткой. |  |
|  | **STEP 2C** Проверить запасной сигнал давления на короткое время до земли. |  |
|  | **STEP 2D.** Проверьте запасной датчик давления на подачу провода +24-VDC на напряжение. |  |

### ШАГ 1. Проверьте клиентский интерфейс коробки проводов.

#### ШАГ 1A. Проверьте запасной сигнал давления и датчик питания проводов +24-VDC на наличие открытого.

| **Условия: ** Откройте окно интерфейса клиента. Отключите запасной сигнал давления и датчик питания проводов +24-VDC на удаленном блоке ввода/вывода. Отключите разъем C4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте запасной сигнал давления и датчик питания проводов +24-VDC на наличие открытого. Примечание: Сигнал тревоги будет звучать на удаленном блоке ввода/вывода при обнаружении открытого устройства. Поместите один испытательный щуп на запасной провод сигнала давления на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на контакт с запасным сигналом давления на разъеме С4. Поместите один испытательный щуп на провод датчика питания +24-VDC на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на датчик питания +24-VDC штифта на разъем С4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1B. Проверьте запасной сигнал давления и датчик питания +24-VDC проводов для провода к проводу коротко.

| **Условия: ** Откройте окно интерфейса клиента. Отключите запасной сигнал давления и датчик питания проводов +24-VDC на удаленном блоке ввода/вывода. Отключите разъем C4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте запасной сигнал давления и датчик питания +24-VDC проводов для провода к проводу коротко. Поместите один испытательный щуп на запасной провод сигнала давления на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на все другие провода в удаленном блоке ввода/вывода. Поместите один испытательный щуп на провод датчика питания +24-VDC на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на все другие провода в удаленном блоке ввода/вывода. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте запасной сигнал давления и датчик питания проводов +24-VDC для короткого наземного.

| **Условия: ** Откройте окно интерфейса клиента. Отключите запасной сигнал давления и датчик питания проводов +24-VDC на удаленном блоке ввода/вывода. Отключите разъем C4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте запасной сигнал давления и датчик питания проводов +24-VDC для короткого наземного. Поместите один испытательный щуп на запасной провод сигнала давления на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на провод датчика питания +24-VDC на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов изготовителя машины.

#### ШАГ 2A. Проверьте запасной сигнал давления и датчик питания проводов +24-VDC на наличие открытого.

| **Условия: ** Отключите проводку OEM-производителя на разъемах C4 и C11. Отключите запасной разъем датчика давления. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте запасной сигнал давления и датчик питания проводов +24-VDC на наличие открытого. Примечание: Открытое устройство было обнаружено удаленным устройством ввода/вывода, если произошла ложная тревога. Поместите один испытательный щуп на контакт с запасным сигналом давления на разъеме С4. Поместите другой испытательный щуп на контакт с запасным сигналом давления на разъеме C11. Поместите один испытательный щуп на запасной датчик давления питания +24-VDC штифт на разъеме С4. Поместите другой испытательный щуп на запасной датчик давления +24-VDC на разъеме C11. Поместите один испытательный щуп на контакт с запасным сигналом давления на разъеме C11. Поместите другой испытательный щуп на контакт с запасным сигналом давления на разъем датчика. Поместите один испытательный щуп на запасной датчик давления питания +24-VDC штифт на разъеме C11. Поместите другой испытательный щуп на запасной датчик давления +24-VDC на разъем датчика. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 2B. Проверьте запасной сигнал давления и датчик питания +24-VDC проводов для провода к проводу коротко.

| **Условия: ** Отключите проводку OEM-производителя на разъемах C4 и C11. Отключите запасной разъем датчика давления. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте запасной сигнал давления и датчик питания +24-VDC проводов для провода к проводу коротко. Поместите один испытательный щуп на контакт с запасным сигналом давления на разъеме С4. Поместите другой испытательный щуп на все другие штифты на разъеме C4. Поместите один испытательный щуп на запасной датчик давления питания +24-VDC штифт на разъеме С4. Поместите другой испытательный щуп на все другие штифты на разъеме C4. Поместите один испытательный щуп на контакт с запасным сигналом давления на разъеме C11. Поместите другой испытательный щуп на все другие штифты на разъеме C11. Поместите один испытательный щуп на запасной датчик давления питания +24-VDC штифт на разъеме C11. Поместите другой испытательный щуп на все другие штифты на разъеме C11. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте запасной сигнал давления и датчик питания проводов +24-VDC для короткого наземного.

| **Условия: ** Отключите проводку OEM-производителя на разъемах C4 и C11. Отключите запасной разъем датчика давления. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте запасной сигнал давления и датчик питания проводов +24-VDC для короткого наземного. Поместите один испытательный щуп на контакт с запасным сигналом давления на разъеме С4. Поместите другой испытательный щуп на землю двигателя. Поместите один испытательный щуп на датчик питания +24-VDC штифта на разъеме C11. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте запасной датчик давления подачу +24-VDC провода на напряжение.

| **Условия:** Отключите запасной разъем датчика давления. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте запасной датчик давления подачу +24-VDC провода на напряжение. Поместите один испытательный щуп на запасной датчик давления питания +24-VDC штифт на разъем датчика. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | +24-VDC? *** Заменить запасной датчик давления. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |
| +24-VDC? **Батарные батареи:** Проверить. См. сервисное руководство изготовителя машины. Заменить удаленный блок ввода/вывода. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The OEM spare pressure sensor has malfunctioned.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The spare pressure sensor is connected to the Alarm and Safety C4 connector located on the customer interface box.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box wiring. |  |
> |  | **STEP 1A.** Check the spare pressure signal and sensor supply +24-VDC wires for an open. |  |
> |  | **STEP 1B.** Check the spare pressure signal and sensor supply +24-VDC wires for a wire-to-wire short. |  |
> |  | **STEP 1C.** Check the spare pressure signal wire for a short to ground. |  |
> | STEP 2. | Check the OEM wiring harness. |  |
> |  | **STEP 2A.** Check the spare pressure signal and sensor supply +24-VDC wires for an open. |  |
> |  | **STEP 2B.** Check the spare pressure signal and sensor supply +24-VDC wires for a wire-to-wire short. |  |
> |  | **STEP 2C.** Check the spare pressure signal wire for a short to ground. |  |
> |  | **STEP 2D.** Check the spare pressure sensor supply +24-VDC wire for voltage. |  |
>
> ### STEP 1. Check the customer interface box wiring.
>
> #### STEP 1A. Check the spare pressure signal and sensor supply +24-VDC wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the spare pressure signal and sensor supply +24-VDC wires at the remote input/output unit. Disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the spare pressure signal and sensor supply +24-VDC wires for an open. NOTE: An alarm will sound on the remote input/output unit when an open is detected. Place one test lead on the spare pressure signal wire at the remote input/output unit. Place the other test lead on the spare pressure signal pin at the C4 connector. Place one test lead on the sensor supply +24-VDC wire at the remote input/output unit. Place the other test lead on the sensor supply +24-VDC pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1B. Check the spare pressure signal and sensor supply +24-VDC wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the spare pressure signal and sensor supply +24-VDC wires at the remote input/output unit. Disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the spare pressure signal and sensor supply +24-VDC wires for a wire-to-wire short. Place one test lead on the spare pressure signal wire at the remote input/output unit. Place the other test lead on all other wires at the remote input/output unit. Place one test lead on the sensor supply +24-VDC wire at the remote input/output unit. Place the other test lead on all other wires at the remote input/output unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check the spare pressure signal and sensor supply +24-VDC wires for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the spare pressure signal and sensor supply +24-VDC wires at the remote input/output unit. Disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the spare pressure signal and sensor supply +24-VDC wires for a short to ground. Place one test lead on the spare pressure signal wire at the remote input/output unit. Place the other test lead on panel ground. Place one test lead on the sensor supply +24-VDC wire at the remote input/output unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM wiring harness.
>
> #### STEP 2A. Check the spare pressure signal and sensor supply +24-VDC wires for an open.
>
> | **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the spare pressure sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the spare pressure signal and sensor supply +24-VDC wires for an open. NOTE: An open has been detected by the remote input/output unit if a false alarm has occurred. Place one test lead on the spare pressure signal pin at the C4 connector. Place the other test lead on the spare pressure signal pin at the C11 connector. Place one test lead on the spare pressure sensor supply +24-VDC pin at the C4 connector. Place the other test lead on the spare pressure sensor supply +24-VDC pin at the C11 connector. Place one test lead on the spare pressure signal pin at the C11 connector. Place the other test lead on the spare pressure signal pin at the sensor connector. Place one test lead on the spare pressure sensor supply +24-VDC pin at the C11 connector. Place the other test lead on the spare pressure sensor supply +24-VDC pin at the sensor connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 2B. Check the spare pressure signal and sensor supply +24-VDC wires for a wire-to-wire short.
>
> | **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the spare pressure sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the spare pressure signal and sensor supply +24-VDC wires for a wire-to-wire short. Place one test lead on the spare pressure signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the spare pressure sensor supply +24-VDC pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the spare pressure signal pin at the C11 connector. Place the other test lead on all other pins at the C11 connector. Place one test lead on the spare pressure sensor supply +24-VDC pin at the C11 connector. Place the other test lead on all other pins at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the spare pressure signal and sensor supply +24-VDC wires for a short to ground.
>
> | **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the spare pressure sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the spare pressure signal and sensor supply +24-VDC wires for a short to ground. Place one test lead on the spare pressure signal pin at the C4 connector. Place the other test lead on engine ground. Place one test lead on the sensor supply +24-VDC pin at the C11 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2D |  |
>
> #### STEP 2D. Check the spare pressure sensor supply +24-VDC wire for voltage.
>
> | **Conditions:** Disconnect the spare pressure sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the spare pressure sensor supply +24-VDC wire for voltage. Place one test lead on the spare pressure sensor supply +24-VDC pin at the sensor connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | +24-VDC? **YESRepair:** Replace the spare pressure sensor. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |
> | +24-VDC? **NORepair:** Check the batteries. Refer to the OEM service manual. Replace the remote input/output unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
