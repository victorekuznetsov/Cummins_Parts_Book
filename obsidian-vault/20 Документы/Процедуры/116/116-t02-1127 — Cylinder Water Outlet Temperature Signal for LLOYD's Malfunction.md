---
aliases:
  - "Неисправность сигнала температуры воды на выходе цилиндра (для LLOYD's)"
type: "Процедура"
doc: "116-t02-1127"
title_en: "Cylinder Water Outlet Temperature Signal for LLOYD's Malfunction"
title_ru: "Неисправность сигнала температуры воды на выходе цилиндра (для LLOYD's)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1127.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1127.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Cylinder Water Outlet Temperature Signal for LLOYD's Malfunction
**Неисправность сигнала температуры воды на выходе цилиндра (для LLOYD's)**

> [!abstract] Процедура · `116-t02-1127`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1127.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1127.pdf)

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
|  | **ШАГ 1А.** Проверьте температурный сигнал розетки цилиндра, верните и верните 2 провода для открытого. |  |
|  | **STEP 1B.** Проверьте температурный сигнал розетки цилиндра, возврат и возврат 2 проводов для короткого провода к проводу. |  |
|  | **STEP 1C** Проверить температурный сигнал розетки цилиндра на короткое время до земли. |  |

### ШАГ 1. Проверьте жгут проводов изготовителя машины.

#### ШАГ 1A. Проверьте температурный сигнал розетки цилиндра, верните и верните 2 провода для открытого.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините сигнал температуры выходной воды цилиндра, возврат и возврат 2 проводов на удаленном разъёме ввода/вывода X7. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте температурный сигнал розетки цилиндра, верните и верните 2 провода для открытого. Поместите один испытательный щуп на контактный сигнал температуры розетки цилиндра в разъем X7. Поместите другой испытательный щуп на контактный сигнал температуры розетки цилиндра с температурным датчиком розетки цилиндра. Поместите один испытательный щуп на контакт обратной температуры розетки цилиндра на разъеме X7. Поместите другой испытательный щуп на контакт обратной температуры розетки цилиндра с датчиком температуры розетки цилиндра. Поместите один испытательный щуп на выходной температурный отверток 2 баллона на разъеме X7. Поместите другой испытательный щуп на температуру возврата 2 штифта розетки цилиндра на датчик температуры розетки цилиндра. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 1B. Проверьте температурный сигнал розетки воды в цилиндре, верните и верните 2 провода для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините сигнал температуры выходной воды цилиндра, возврат и возврат 2 проводов на удаленном разъёме ввода/вывода X7. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте температурный сигнал розетки воды в цилиндре, верните и верните 2 провода для короткого провода к проводу. Поместите один испытательный щуп на контактный сигнал температуры розетки цилиндра в разъем X7. Поместите другой испытательный щуп на все другие штифты в разъем X7. Поместите один испытательный щуп на контакт обратной температуры розетки цилиндра на разъеме X7. Поместите другой испытательный щуп на все другие штифты в разъем X7. Поместите один испытательный щуп на выходной температурный отверток 2 баллона на разъеме X7. Поместите другой испытательный щуп на все другие штифты в разъем X7. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте провод температурного сигнала розетки цилиндра для короткого заземления.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините провод температурного сигнала розетки цилиндра на удаленном блоке ввода/вывода X7. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод температурного сигнала розетки цилиндра для короткого заземления. Поместите один испытательный щуп на контактный сигнал температуры розетки цилиндра в разъем X7. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить датчик температуры розетки воды в цилиндре. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |  |


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
> |  | **STEP 1A.** Check the cylinder water outlet temperature signal, return, and return 2 wires for an open. |  |
> |  | **STEP 1B.** Check the cylinder water outlet temperature signal, return, and return 2 wires for a wire-to-wire short. |  |
> |  | **STEP 1C.** Check the cylinder water outlet temperature signal wire for a short to ground. |  |
>
> ### STEP 1. Check the OEM wiring harness.
>
> #### STEP 1A. Check the cylinder water outlet temperature signal, return, and return 2 wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the cylinder water outlet temperature signal, return, and return 2 wires at the remote input/output unit X7 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the cylinder water outlet temperature signal, return, and return 2 wires for an open. Place one test lead on the cylinder water outlet temperature signal pin at the X7 connector. Place the other test lead on the cylinder water outlet temperature signal pin at the cylinder water outlet temperature sensor. Place one test lead on the cylinder water outlet temperature return pin at the X7 connector. Place the other test lead on the cylinder water outlet temperature return pin at the cylinder water outlet temperature sensor. Place one test lead on the cylinder water outlet temperature return 2 pin at the X7 connector. Place the other test lead on the cylinder water outlet temperature return 2 pin at the cylinder water outlet temperature sensor. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 1B. Check the cylinder water outlet temperature signal, return, and return 2 wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the cylinder water outlet temperature signal, return, and return 2 wires at the remote input/output unit X7 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the cylinder water outlet temperature signal, return, and return 2 wires for a wire-to-wire short. Place one test lead on the cylinder water outlet temperature signal pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Place one test lead on the cylinder water outlet temperature return pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Place one test lead on the cylinder water outlet temperature return 2 pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check the cylinder water outlet temperature signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the cylinder water outlet temperature signal wire at the remote input/output unit X7 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the cylinder water outlet temperature signal wire for a short to ground. Place one test lead on the cylinder water outlet temperature signal pin at the X7 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the cylinder water outlet temperature sensor. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |  |
