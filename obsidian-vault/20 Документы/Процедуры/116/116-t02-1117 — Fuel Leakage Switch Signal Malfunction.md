---
aliases:
  - "Неисправность сигнала датчика утечки топлива"
type: "Процедура"
doc: "116-t02-1117"
title_en: "Fuel Leakage Switch Signal Malfunction"
title_ru: "Неисправность сигнала датчика утечки топлива"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1117.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1117.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Fuel Leakage Switch Signal Malfunction
**Неисправность сигнала датчика утечки топлива**

> [!abstract] Процедура · `116-t02-1117`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1117.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1117.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Выключатель утечки топлива OEM вышел из строя.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Переключатель утечки топлива является обычно закрытым переключателем. Тревога звучит, когда в цепи открыта.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс коробки проводов. |  |
|  | **ШАГ 1А.** Проверить сигнал утечки топлива и возвратные провода на наличие открытого. |  |
|  | **STEP 1B.** Проверьте сигнал утечки топлива и провода возврата для короткого провода к проводу. |  |
|  | **STEP 1C** Проверить сигнальный провод утечки топлива на короткое время до заземления. |  |
| ШАГ 2. | Проверьте жгут проводов изготовителя машины. |  |
|  | **ШАГ 2А.** Проверить сигнал утечки топлива и возвратные провода на наличие открытого. |  |
|  | **STEP 2B.** Проверьте сигнал утечки топлива и провода возврата для короткого провода к проводу. |  |
|  | **STEP 2C** Проверить сигнал утечки топлива на короткое время до заземления. |  |

### ШАГ 1. Проверьте клиентский интерфейс коробки проводов.

#### ШАГ 1A. Проверьте сигнал утечки топлива и возвратные провода для открытого.

| **Условия: **Откройте окно интерфейса клиента. Отключите сигнал утечки топлива и провода возврата на удаленном блоке ввода/вывода. Отключите разъем C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал утечки топлива и возвратные провода для открытого. Примечание: Сигнал тревоги будет звучать на удаленном блоке ввода/вывода при обнаружении открытого устройства. Поместите один испытательный щуп на провод сигнала утечки топлива на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на контакт сигнала утечки топлива на разъеме C4. Поместите один испытательный щуп на провод возврата утечки топлива на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на обратный контакт утечки топлива на разъеме C4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (ящик пользовательского интерфейса) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1B. Проверьте сигнал утечки топлива и возвратные провода для короткого провода к проводу.

| **Условия: **Откройте окно интерфейса клиента. Отключите сигнал утечки топлива и провода возврата на удаленном блоке ввода/вывода. Отключите разъем C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал утечки топлива и возвратные провода для короткого провода к проводу. Поместите один испытательный щуп на контакт сигнала утечки топлива на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на все другие штифты на удаленном блоке ввода/вывода. Поместите один испытательный щуп на обратный контакт утечки топлива на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на все другие штифты на удаленном блоке ввода/вывода. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (ящик пользовательского интерфейса) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте сигнал утечки топлива на короткий срок до земли.

| **Условия: **Откройте окно интерфейса клиента. Отключите сигнальный провод утечки топлива на удаленном блоке ввода/вывода. Отключите разъем C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал утечки топлива на короткий срок до земли. Поместите один испытательный щуп на провод сигнала утечки топлива на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (ящик пользовательского интерфейса) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов изготовителя машины.

#### ШАГ 2A. Проверьте сигнал утечки топлива и возвратные провода для открытого.

| **Условия: **Отключите проводку OEM-производителя на разъемах C4 и C11. Отключите разъем датчика утечки топлива. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал утечки топлива и возвратные провода для открытого. Примечание: Сигнал тревоги будет звучать на удаленном блоке ввода/вывода при обнаружении открытого устройства. Поместите один испытательный щуп на контакт сигнала утечки топлива на разъеме С4. Поместите другой испытательный щуп на контакт сигнала утечки топлива на разъеме C11. Поместите один испытательный щуп на обратный контакт утечки топлива на разъеме C4. Поместите другой испытательный щуп на обратный контакт утечки топлива на разъеме C11. Поместите один испытательный щуп на контакт сигнала утечки топлива на разъеме C11. Поместите другой испытательный щуп на контакт сигнала утечки топлива на разъем датчика. Поместите один испытательный щуп на обратный контакт утечки топлива на разъеме C11. Поместите другой испытательный щуп на обратный контакт утечки топлива на разъем датчика. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 2B. Проверьте сигнал утечки топлива и возвратные провода для короткого провода к проводу.

| **Условия: **Отключите проводку OEM-производителя на разъемах C4 и C11. Отключите разъем датчика утечки топлива. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал утечки топлива и возвратные провода для короткого провода к проводу. Поместите один испытательный щуп на контакт сигнала утечки топлива на разъеме С4. Поместите другой испытательный щуп на все другие штифты на разъеме C4. Поместите один испытательный щуп на контакт сигнала утечки топлива на разъеме C11. Поместите другой испытательный щуп на все другие штифты на разъеме C11. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте сигнал утечки топлива на короткий срок до земли.

| **Условия: **Отключите проводку OEM-производителя на разъемах C4 и C11. Отключите разъем датчика утечки топлива. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал утечки топлива на короткий срок до земли. Поместите один испытательный щуп на контакт сигнала утечки топлива на разъеме С4. Поместите другой испытательный щуп на землю двигателя. Поместите один испытательный щуп на контакт сигнала утечки топлива на разъеме C11. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить выключатель утечки топлива. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - OEM fuel leakage switch has malfunctioned.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The fuel leakage switch is a normally closed switch. The alarm sounds when there is an open in the circuit.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box wiring. |  |
> |  | **STEP 1A.** Check the fuel leakage signal and return wires for an open. |  |
> |  | **STEP 1B.** Check the fuel leakage signal and return wires for a wire-to-wire short. |  |
> |  | **STEP 1C.** Check the fuel leakage signal wire for a short to ground. |  |
> | STEP 2. | Check the OEM wiring harness. |  |
> |  | **STEP 2A.** Check the fuel leakage signal and return wires for an open. |  |
> |  | **STEP 2B.** Check the fuel leakage signal and return wires for a wire-to-wire short. |  |
> |  | **STEP 2C.** Check the fuel leakage signal wire for a short to ground. |  |
>
> ### STEP 1. Check the customer interface box wiring.
>
> #### STEP 1A. Check the fuel leakage signal and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the fuel leakage signal and return wires at remote input/output unit. Disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel leakage signal and return wires for an open. NOTE: An alarm will sound on the remote input/output unit when an open is detected. Place one test lead on the fuel leakage signal wire at the remote input/output unit. Place the other test lead on the fuel leakage signal pin at the C4 connector. Place one test lead on the fuel leakage return wire at the remote input/output unit. Place the other test lead on the fuel leakage return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1B. Check the fuel leakage signal and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the fuel leakage signal and return wires at the remote input/output unit. Disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel leakage signal and return wires for a wire-to-wire short. Place one test lead on the fuel leakage signal pin at the remote input/output unit. Place the other test lead on all other pins at the remote input/output unit. Place one test lead on the fuel leakage return pin at the remote input/output unit. Place the other test lead on all other pins at the remote input/output unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check the fuel leakage signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the fuel leakage signal wire at the remote input/output unit. Disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel leakage signal wire for a short to ground. Place one test lead on the fuel leakage signal wire at the remote input/output unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM wiring harness.
>
> #### STEP 2A. Check the fuel leakage signal and return wires for an open.
>
> | **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the fuel leakage sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel leakage signal and return wires for an open. NOTE: An alarm will sound on the remote input/output unit when an open is detected. Place one test lead on the fuel leakage signal pin at the C4 connector. Place the other test lead on the fuel leakage signal pin at the C11 connector. Place one test lead on the fuel leakage return pin at the C4 connector. Place the other test lead on the fuel leakage return pin at the C11 connector. Place one test lead on the fuel leakage signal pin at the C11 connector. Place the other test lead on the fuel leakage signal pin at the sensor connector. Place one test lead on the fuel leakage return pin at the C11 connector. Place the other test lead on the fuel leakage return pin at the sensor connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 2B. Check the fuel leakage signal and return wires for a wire-to-wire short.
>
> | **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the fuel leakage sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel leakage signal and return wires for a wire-to-wire short. Place one test lead on the fuel leakage signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the fuel leakage signal pin at the C11 connector. Place the other test lead on all other pins at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the fuel leakage signal wire for a short to ground.
>
> | **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the fuel leakage sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel leakage signal wire for a short to ground. Place one test lead on the fuel leakage signal pin at the C4 connector. Place the other test lead on engine ground. Place one test lead on the fuel leakage signal pin at the C11 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the fuel leakage switch. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
