---
aliases:
  - "Неисправность сигнала температуры масла на входе (для LLOYD's)"
type: "Процедура"
doc: "116-t02-1126"
title_en: "Lubricating Oil Inlet Temperature Signal for LLOYD's Malfunction"
title_ru: "Неисправность сигнала температуры масла на входе (для LLOYD's)"
modified: "2008-05-22"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1126.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1126.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Lubricating Oil Inlet Temperature Signal for LLOYD's Malfunction
**Неисправность сигнала температуры масла на входе (для LLOYD's)**

> [!abstract] Процедура · `116-t02-1126`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1126.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1126.pdf)

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
|  | **ШАГ 1А.** Проверить входной температурный сигнал моторного масла, возврат и возврат 2 проводов на наличие открытого. |  |
|  | **STEP 1B.** Проверьте температурный сигнал впускного отверстия моторного масла, возврат и возврат 2 проводов для короткого провода к проводу. |  |
|  | **STEP 1C.** Проверить впускной температурный сигнал проволоки моторного масла на короткое время до заземления. |  |

### ШАГ 1. Проверьте жгут проводов изготовителя машины.

#### ШАГ 1A. Проверьте сигнал температуры входного отверстия моторного масла, верните и верните 2 провода для открытого.

| **Условия: ** Откройте окно интерфейса клиента. Отключите входной температурный сигнал моторного масла, возврат и возврат 2 проводов на удаленном разъёме ввода/вывода X7. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнал температуры входного отверстия моторного масла, верните и верните 2 провода для открытого. Поместите один испытательный щуп на контактный сигнал входного температурного сигнала моторного масла на разъеме X7. Поместите другой испытательный щуп на контактный сигнал входного температурного сигнала моторного масла на датчик температуры входного температурного сигнала моторного масла. Поместите один испытательный щуп на входной температурный контакт моторного масла на разъеме X7. Поместите другой испытательный щуп на входной температурный контакт моторного масла на датчик температуры входного отверстия моторного масла. Поместите один испытательный щуп на входной температурный отверток моторного масла 2 штифта на разъем X7. Поместите другой испытательный щуп на входной температурный отверток 2 моторного масла на датчик температуры входного отверстия моторного масла. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 1B. Проверьте температурный сигнал впуска моторного масла, верните и верните 2 провода для короткого провода к проводу.

| **Условия: ** Откройте окно интерфейса клиента. Отключите входной температурный сигнал моторного масла, возврат и возврат 2 проводов на удаленном разъёме ввода/вывода X7. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте температурный сигнал впуска моторного масла, верните и верните 2 провода для короткого провода к проводу. Поместите один испытательный щуп на контактный сигнал входного температурного сигнала моторного масла на разъеме X7. Поместите другой испытательный щуп на все другие штифты в разъем X7. Поместите один испытательный щуп на входной температурный контакт моторного масла на разъеме X7. Поместите другой испытательный щуп на все другие штифты в разъем X7. Поместите один испытательный щуп на входной температурный отверток моторного масла 2 штифта на разъем X7. Поместите другой испытательный щуп на все другие штифты в разъем X7. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (ящик пользовательского интерфейса) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте впускной сигнальный провод моторного масла для короткого заземления.

| **Условия: ** Откройте окно интерфейса клиента. Отсоедините провод входного температурного сигнала моторного масла на удаленном разъёме ввода/вывода X7. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте впускной сигнальный провод моторного масла для короткого заземления. Поместите один испытательный щуп на контактный сигнал входного температурного сигнала моторного масла на разъеме X7. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить датчик температуры впускного отверстия моторного масла. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |  |


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
> |  | **STEP 1A.** Check the lubricating oil inlet temperature signal, return, and return 2 wires for an open. |  |
> |  | **STEP 1B.** Check the lubricating oil inlet temperature signal, return, and return 2 wires for a wire-to-wire short. |  |
> |  | **STEP 1C.** Check the lubricating oil inlet temperature signal wire for a short to ground. |  |
>
> ### STEP 1. Check the OEM wiring harness.
>
> #### STEP 1A. Check the lubricating oil inlet temperature signal, return, and return 2 wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the lubricating oil inlet temperature signal, return, and return 2 wires at the remote input/output unit X7 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the lubricating oil inlet temperature signal, return, and return 2 wires for an open. Place one test lead on the lubricating oil inlet temperature signal pin at the X7 connector. Place the other test lead on the lubricating oil inlet temperature signal pin at the lubricating oil inlet temperature sensor. Place one test lead on the lubricating oil inlet temperature return pin at the X7 connector. Place the other test lead on the lubricating oil inlet temperature return pin at the lubricating oil inlet temperature sensor. Place one test lead on the lubricating oil inlet temperature return 2 pin at the X7 connector. Place the other test lead on the lubricating oil inlet temperature return 2 pin at the lubricating oil inlet temperature sensor. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 1B. Check the lubricating oil inlet temperature signal, return, and return 2 wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the lubricating oil inlet temperature signal, return, and return 2 wires at the remote input/output unit X7 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the lubricating oil inlet temperature signal, return, and return 2 wires for a wire-to-wire short. Place one test lead on the lubricating oil inlet temperature signal pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Place one test lead on the lubricating oil inlet temperature return pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Place one test lead on the lubricating oil inlet temperature return 2 pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check the lubricating oil inlet temperature signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the lubricating oil inlet temperature signal wire at the remote input/output unit X7 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the lubricating oil inlet temperature signal wire for a short to ground. Place one test lead on the lubricating oil inlet temperature signal pin at the X7 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the lubricating oil inlet temperature sensor. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |  |
