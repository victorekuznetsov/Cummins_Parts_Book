---
aliases:
  - "Неисправность аналогового сигнала судна 4"
type: "Процедура"
doc: "116-t02-1140"
title_en: "Vessel Analog Signal 4 Malfunction"
title_ru: "Неисправность аналогового сигнала судна 4"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1140.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1140.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Vessel Analog Signal 4 Malfunction
**Неисправность аналогового сигнала судна 4**

> [!abstract] Процедура · `116-t02-1140`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-07-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1140.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1140.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Датчик судна на OEM-приложении **не** связывается с блоком DCU410.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Входные данные датчика судна на клиентском интерфейсе (CIB) используются OEM. Ввод в DCU410 измеряет эти значения от датчиков.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс коробки проводов. |  |
|  | **STEP 1A.** Проверьте дисплей блока DCU410 на наличие неисправностей. |  |
|  | **STEP 1B.** Проверить источник подачи аналогового входного сигнала датчика судна и провода аналогового сигнала 4 датчика судна на наличие открытого сигнала. |  |
|  | **STEP 1C.** Проверить источник подачи аналогового входного сигнала датчика судна и аналоговый сигнал 4 датчика судна на короткое расстояние от провода к проводу. |  |
|  | **STEP 1D.** Проверьте датчик температуры судна 1 сигнальной проволокой на короткое время до заземления. |  |
| ШАГ 2. | Проверьте жгут проводов изготовителя машины. |  |
|  | **STEP 2A.** Проверить источник подачи аналогового входного сигнала датчика судна и провода аналогового сигнала 4 датчика судна на наличие открытого сигнала. |  |
|  | **STEP 2B.** Проверьте источник подачи аналогового входа датчика судна и аналоговый сигнал 4 датчика судна на короткое расстояние от провода к проводу. |  |
|  | **STEP 2C.** Проверить источник подачи аналогового сигнала датчика судна и провода аналогового сигнала 4 датчика судна на короткое время до заземления. |  |

### ШАГ 1. Проверьте клиентский интерфейс коробки проводов.

#### ШАГ 1A. Проверьте дисплей блока DCU410 на наличие неисправностей.

| **Условия:** Найдите дисплей блока DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей блока DCU410 на наличие неисправностей. | DCU410 указывает на неисправность (неисправности)? *Да | 1В |
| DCU410 указывает на неисправность (неисправности)? **НЕТ** | 2А |  |

#### ШАГ 1B. Проверьте датчик судна аналоговый входной источник и датчик судна аналоговый сигнал 4 провода для открытого.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините аналоговый входной сигнал датчика судна и аналоговый сигнал датчика судна 4 провода от блока DCU410 и соединения X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте датчик судна аналоговый входной источник и провода аналогового сигнала судна 4 для открытого. Поместите один испытательный щуп на аналоговый входной провод датчика судна в блок DCU410. Поместите другой испытательный щуп на датчик судна аналоговый входной провод питания на соединение X4. Поместите один испытательный щуп на провод аналогового сигнала 4 датчика судна в блок DCU410. Поместите другой испытательный щуп на датчик судна аналогового сигнала 4 провода в соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1С |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1C. Проверьте датчик судна аналоговый входной источник и датчик судна аналоговый сигнал 4 провода для провода к проводу короткий.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте датчик судна аналоговый входной источник и аналоговый сигнал судна 4 провода для провода к проводу короткой. Поместите один испытательный щуп на аналоговый входной провод датчика судна в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на провод аналогового сигнала 4 датчика судна в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1D |  |

#### ШАГ 1D. Проверьте датчик судна аналоговый сигнал 4 провода на короткое время до земли.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте датчик судна аналоговый сигнал 4 провода на короткое время до земли. Поместите один испытательный щуп на провод аналогового сигнала 4 датчика судна в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов изготовителя машины.

#### ШАГ 2A. Проверьте датчик судна аналоговый входной источник и датчик судна аналоговый сигнал 4 провода для открытого.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините аналоговый входной источник датчика судна и аналоговый сигнал датчика судна 4 провода в соединениях X4. Отсоедините аналоговый входной источник датчика судна и аналоговый сигнал 4 датчика судна на разъёме датчика судна. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте датчик судна аналоговый входной источник и датчик судна аналоговый сигнал 4 провода для открытого. Поместите один испытательный щуп на датчик судна аналоговый входной провод питания на соединение X4. Поместите другой испытательный щуп на аналоговый входной провод датчика судна на разъёме датчика судна. Поместите один испытательный щуп на датчик судна аналогового сигнала 4 провода при соединении X4. Поместите другой испытательный щуп на провод аналогового сигнала 4 датчика судна на разъёме датчика судна. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 2B. Проверьте датчик судна аналоговый входной источник и датчик судна аналоговый сигнал 4 провода для провода к проводу короткий.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините аналоговый входной источник датчика судна и аналоговый сигнал 4 датчика судна при соединении X4. Отсоедините аналоговый входной источник датчика судна и аналоговый сигнал 4 датчика судна на разъёме датчика судна. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте датчик судна аналоговый входной источник и аналоговый сигнал судна 4 провода для провода к проводу короткой. Поместите один испытательный щуп на датчик судна аналоговый входной провод питания на соединение X4. Поместите другой испытательный щуп на все другие провода в соединение X4. Поместите один испытательный щуп на датчик судна аналогового сигнала 4 провода при соединении X4. Поместите другой испытательный щуп на все другие провода в соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте датчик судна аналоговый входной источник и датчик судна аналоговый сигнал 4 провода для короткого наземного.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините аналоговый входной источник датчика судна и аналоговый сигнал 4 датчика судна при соединении X4. Отсоедините аналоговый входной источник датчика судна и аналоговый сигнал 4 датчика судна на разъёме датчика судна. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте датчик судна аналоговый входной источник и датчик судна аналоговый сигнал 4 провода для короткого наземного. Поместите один испытательный щуп на аналоговый входной провод питания в соединение X4. Поместите другой испытательный щуп на землю двигателя. Поместите один испытательный щуп на датчик судна аналогового сигнала 4 провода при соединении X4. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить датчик судна. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The vessel sensor on the OEM application is **not** communicating with DCU410 unit.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The vessel sensor inputs on the customer interface box (CIB) are used by the OEM. The input to the DCU410 measures these values from the sensors.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box wiring. |  |
> |  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
> |  | **STEP 1B.** Check the vessel sensor analog input supply and vessel sensor analog signal 4 wires for an open. |  |
> |  | **STEP 1C.** Check the vessel sensor analog input supply and vessel sensor analog signal 4 wires for a wire-to-wire short. |  |
> |  | **STEP 1D.** Check the vessel temperature sensor 1 signal wire for a short to ground. |  |
> | STEP 2. | Check the OEM wiring harness. |  |
> |  | **STEP 2A.** Check the vessel sensor analog input supply and vessel sensor analog signal 4 wires for an open. |  |
> |  | **STEP 2B.** Check the vessel sensor analog input supply and vessel sensor analog signal 4 wires for a wire-to-wire short. |  |
> |  | **STEP 2C.** Check the vessel sensor analog input supply and vessel sensor analog signal 4 wires for a short to ground. |  |
>
> ### STEP 1. Check the customer interface box wiring.
>
> #### STEP 1A. Check the DCU410 unit display for faults.
>
> | **Conditions:** Locate the DCU410 unit display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 unit display for faults. | DCU410 unit indicates fault(s)? **YES** | 1B |
> | DCU410 unit indicates fault(s)? **NO** | 2A |  |
>
> #### STEP 1B. Check the vessel sensor analog input supply and vessel sensor analog signal 4 wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 4 wires from the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the vessel sensor analog input supply and vessel analog signal 4 wires for an open. Place one test lead on the vessel sensor analog input supply wire at the DCU410 unit. Place the other test lead on the vessel sensor analog input supply wire at the X4 connection. Place one test lead on the vessel sensor analog signal 4 wire at the DCU410 unit. Place the other test lead on the vessel sensor analog signal 4 wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1C. Check the vessel sensor analog input supply and vessel sensor analog signal 4 wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the vessel sensor analog input supply and vessel analog signal 4 wires for a wire-to-wire short. Place one test lead on the vessel sensor analog input supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the vessel sensor analog signal 4 wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1D |  |
>
> #### STEP 1D. Check the vessel sensor analog signal 4 wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the vessel sensor analog signal 4 wire for a short to ground. Place one test lead on the vessel sensor analog signal 4 wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM wiring harness.
>
> #### STEP 2A. Check the vessel sensor analog input supply and vessel sensor analog signal 4 wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 4 wires at the X4 connections. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 4 wires at the vessel sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the vessel sensor analog input supply and vessel sensor analog signal 4 wires for an open. Place one test lead on the vessel sensor analog input supply wire at the X4 connection. Place the other test lead on the vessel sensor analog input supply wire at the vessel sensor connector. Place one test lead on the vessel sensor analog signal 4 wire at the X4 connection. Place the other test lead on the vessel sensor analog signal 4 wire at the vessel sensor connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 2B. Check the vessel sensor analog input supply and vessel sensor analog signal 4 wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 4 wires at the X4 connection. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 4 wires at the vessel sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the vessel sensor analog input supply and vessel analog signal 4 wires for a wire-to-wire short. Place one test lead on the vessel sensor analog input supply wire at the X4 connection. Place the other test lead on all other wires at the X4 connection. Place one test lead on the vessel sensor analog signal 4 wire at the X4 connection. Place the other test lead on all other wires at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the vessel sensor analog input supply and vessel sensor analog signal 4 wires for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 4 wires at the X4 connection. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 4 wires at the vessel sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the vessel sensor analog input supply and vessel sensor analog signal 4 wires for a short to ground. Place one test lead on the analog input supply wire at the X4 connection. Place the other test lead on engine ground. Place one test lead on the vessel sensor analog signal 4 wire at the X4 connection. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the vessel sensor. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |  |
