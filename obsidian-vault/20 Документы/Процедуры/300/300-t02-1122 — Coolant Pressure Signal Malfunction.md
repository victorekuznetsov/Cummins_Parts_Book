---
aliases:
  - "Неисправность сигнала давления ОЖ"
type: "Процедура"
doc: "300-t02-1122"
title_en: "Coolant Pressure Signal Malfunction"
title_ru: "Неисправность сигнала давления ОЖ"
modified: "2022-02-04"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1122.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1122.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
  - "перевод/машинный"
---

# Coolant Pressure Signal Malfunction
**Неисправность сигнала давления ОЖ**

> [!abstract] Процедура · `300-t02-1122`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2022-02-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1122.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1122.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Датчик давления охлаждающей жидкости оригинального производителя оборудования (OEM) вышел из строя.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Датчик давления охлаждающей жидкости подключен к разъему сигнализации и безопасности C2, расположенному на окне интерфейса клиента (C.I.B.).

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте C.I.B. проводка. |  |
|  | **ШАГ 1А.** Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC провода для открытой цепи. | Больше 100 тысяч ом? |
|  | **ШАГ 1В.** Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC проводов для короткого замыкания провода к проводу. | Менее 10 Ом? |
|  | **STEP 1C.** Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC проводов для короткого замыкания провода к проводу. | Менее 10 Ом? |
| ШАГ 2. | Проверьте жгут проводов изготовителя машины. |  |
|  | **ШАГ 2А.** Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC провода для открытой цепи. | Больше 100 тысяч ом? |
|  | **ШАГ 2В.** Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC проводов для короткого замыкания провода к проводу. | Менее 10 Ом? |
|  | **STEP 2C.** Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC проводов для короткого замыкания провода к проводу. | Менее 10 Ом? |
|  | **STEP 2D.** Проверьте датчик давления охлаждающей жидкости SUPPLY +24-VDC провода на напряжение. | +24-VDC? |

### ШАГ 1. Проверьте C.I.B. проводка.

#### ШАГ 1A. Проверьте давление охлаждающей жидкости SIGNAL и провода датчика SUPPLY +24-VDC для открытой цепи.

| **Условия: **Открыть ЦБ. Отсоедините провода давления охлаждающей жидкости SIGNAL и датчика SUPPLY +24-VDC на панели управления. Отключите разъем C2. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление охлаждающей жидкости SIGNAL и провода датчика SUPPLY +24-VDC для открытой цепи. Примечание: Сигнал тревоги будет звучать на удаленном блоке ввода/вывода при обнаружении открытой цепи. Поместите один испытательный щуп на провод SIGNAL давления охлаждающей жидкости на панели управления. Поместите другой испытательный щуп на контакт сигнала давления охлаждающей жидкости на разъем С2. Поместите один испытательный щуп на провод датчика SUPPLY +24-VDC на панели управления. Поместите другой испытательный щуп на штифт датчика SUPPLY +24-VDC на разъем C2. См. схему или схему проводов для идентификации контакта с разъемом. | Больше 100 тысяч ом? *Да | 1В |
| Больше 100 тысяч ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1B. Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC для короткого замыкания провода к проводу.

| **Условия: **Открыть ЦБ. Отсоедините провода давления охлаждающей жидкости SIGNAL и датчика SUPPLY +24-VDC на панели управления. Отключите разъем C2. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC для короткого замыкания провода к проводу. Поместите один испытательный щуп на провод SIGNAL давления охлаждающей жидкости на панели управления. Поместите другой испытательный щуп на все другие провода на панели управления. Поместите один испытательный щуп на провод датчика SUPPLY +24-VDC на панели управления. Поместите другой испытательный щуп на все другие провода на панели управления. См. схему или схему проводов для идентификации контакта с разъемом. | Менее 10 Ом? Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания на землю.

| **Условия: **Открыть ЦБ. Отсоедините провода давления охлаждающей жидкости SIGNAL и датчика SUPPLY +24-VDC на панели управления. Отключите разъем C2. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания на землю. Поместите один испытательный щуп на провод SIGNAL давления охлаждающей жидкости на панели управления. Поместите другой испытательный щуп на землю панели. Поместите один испытательный щуп на провод датчика SUPPLY +24-VDC на панели управления. Поместите другой испытательный щуп на землю панели. См. схему или схему проводов для идентификации контакта с разъемом. | Менее 10 Ом? Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов изготовителя машины.

#### ШАГ 2A. Проверьте давление охлаждающей жидкости SIGNAL и провода датчика SUPPLY +24-VDC для открытой цепи.

| **Условия: **Отключите проводку OEM-производителя на разъемах C2 и C9. Отключите разъем датчика давления охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление охлаждающей жидкости SIGNAL и провода датчика SUPPLY +24-VDC для открытой цепи. Примечание: На удаленном блоке ввода/вывода будет звучать сигнализация, если произошла ложная тревога. Поместите один испытательный щуп на контакт сигнала давления охлаждающей жидкости на разъеме C2. Поместите другой испытательный щуп на контакт сигнала давления охлаждающей жидкости на разъем С9. Поместите один испытательный щуп на датчик давления охлаждающей жидкости SUPPLY +24-VDC на разъеме C2. Поместите другой испытательный щуп на датчик давления охлаждающей жидкости SUPPLY +24-VDC на разъем C9. Поместите один испытательный щуп на контакт сигнала давления охлаждающей жидкости на разъеме C9. Поместите другой испытательный щуп на контакт сигнала давления охлаждающей жидкости на разъем датчика. Поместите один испытательный щуп на датчик давления охлаждающей жидкости SUPPLY +24-VDC на разъеме C9. Поместите другой испытательный щуп на датчик давления охлаждающей жидкости SUPPLY +24-VDC на разъем датчика. См. схему или схему проводов для идентификации контакта с разъемом. | Больше 100 тысяч ом? *Да | 2В |
| Больше 100 тысяч ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2B. Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC для короткого замыкания провода к проводу.

| **Условия: **Отключите проводку OEM-производителя на разъемах C2 и C9. Отключите разъем датчика давления охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC для короткого замыкания провода к проводу. Поместите один испытательный щуп на контакт сигнала давления охлаждающей жидкости на разъеме C2. Поместите другой испытательный щуп на все другие штифты на разъеме C2. Поместите один испытательный щуп на датчик давления охлаждающей жидкости SUPPLY +24-VDC на разъеме C2. Поместите другой испытательный щуп на все другие штифты на разъеме C2. Поместите один испытательный щуп на контакт сигнала давления охлаждающей жидкости на разъеме C9. Поместите другой испытательный щуп на все другие штифты на разъеме C9. Поместите один испытательный щуп на датчик давления охлаждающей жидкости SUPPLY +24-VDC на разъеме C9. Поместите другой испытательный щуп на все другие штифты на разъеме C9. См. схему или схему проводов для идентификации контакта с разъемом. | Менее 10 Ом? Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания на землю.

| **Условия: **Отключите проводку OEM-производителя на разъемах C2 и C9. Отключите разъем датчика давления охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление охлаждающей жидкости SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания на землю. Поместите один испытательный щуп на контакт сигнала давления охлаждающей жидкости на разъеме C2. Поместите другой испытательный щуп на землю двигателя. Поместите один испытательный щуп на датчик SUPPLY +24-VDC на разъеме C9. Поместите другой испытательный щуп на землю двигателя. См. схему или схему проводов для идентификации контакта с разъемом. | Менее 10 Ом? Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте датчик давления охлаждающей жидкости SUPPLY +24-VDC провода на напряжение.

| **Условия:** Отключить разъем датчика давления охлаждающей жидкости. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте датчик давления охлаждающей жидкости SUPPLY +24-VDC провода на напряжение. Поместите один испытательный щуп на датчик давления охлаждающей жидкости SUPPLY +24-VDC на разъем датчика. Поместите другой испытательный щуп на землю двигателя. См. схему или схему проводов для идентификации контакта с разъемом. | +24-VDC? **Ремонт: **Заменить датчик давления охлаждающей жидкости. См. сервисное руководство изготовителя машины. См. процедуру 019-016 в разделе 19. | Ремонт завершён |
| +24-VDC? **NORepair:** Заменить удаленный блок ввода/вывода. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The original equipment manufacturer (OEM) coolant pressure sensor has malfunctioned.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The coolant pressure sensor is connected to the alarm and safety C2 connector located on the customer interface box (C.I.B.).
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the C.I.B. wiring. |  |
> |  | **STEP 1A.** Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit. | Greater than 100k ohms? |
> |  | **STEP 1B.** Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. | Less than 10 ohms? |
> |  | **STEP 1C.** Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. | Less than 10 ohms? |
> | STEP 2. | Check the OEM wiring harness. |  |
> |  | **STEP 2A.** Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit. | Greater than 100k ohms? |
> |  | **STEP 2B.** Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. | Less than 10 ohms? |
> |  | **STEP 2C.** Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. | Less than 10 ohms? |
> |  | **STEP 2D.** Check the coolant pressure sensor SUPPLY +24-VDC wire for voltage. | +24-VDC? |
>
> ### STEP 1. Check the C.I.B. wiring.
>
> #### STEP 1A. Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit.
>
> | **Conditions:** Open the C.I.B. Disconnect the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires at the control panel. Disconnect the C2 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit. Note: An alarm will sound on the remote input/output unit when an open circuit is detected. Place one test lead on the coolant pressure SIGNAL wire at the control panel. Place the other test lead on the coolant pressure SIGNAL pin at the C2 connector. Place one test lead on the sensor SUPPLY +24-VDC wire at the control panel. Place the other test lead on the sensor SUPPLY +24-VDC pin at the C2 connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Greater than 100k ohms? **YES** | 1B |
> | Greater than 100k ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> #### STEP 1B. Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit.
>
> | **Conditions:** Open the C.I.B. Disconnect the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires at the control panel. Disconnect the C2 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. Place one test lead on the coolant pressure SIGNAL wire at the control panel. Place the other test lead on all other wires at the control panel. Place one test lead on the sensor SUPPLY +24-VDC wire at the control panel. Place the other test lead on all other wires at the control panel. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground.
>
> | **Conditions:** Open the C.I.B. Disconnect the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires at the control panel. Disconnect the C2 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground. Place one test lead on the coolant pressure SIGNAL wire at the control panel. Place the other test lead on the panel ground. Place one test lead on the sensor SUPPLY +24-VDC wire at the control panel. Place the other test lead on the panel ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM wiring harness.
>
> #### STEP 2A. Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit.
>
> | **Conditions:** Disconnect the OEM harness at the C2 and C9 connectors. Disconnect the coolant pressure sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit. Note: An alarm will sound on the remote input/output unit if a false alarm has occurred. Place one test lead on the coolant pressure SIGNAL pin at the C2 connector. Place the other test lead on the coolant pressure SIGNAL pin at the C9 connector. Place one test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the C2 connector. Place the other test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the C9 connector. Place one test lead on the coolant pressure SIGNAL pin at the C9 connector. Place the other test lead on the coolant pressure SIGNAL pin at the sensor connector. Place one test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the C9 connector. Place the other test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the sensor connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Greater than 100k ohms? **YES** | 2B |
> | Greater than 100k ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> #### STEP 2B. Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit.
>
> | **Conditions:** Disconnect the OEM harness at the C2 and C9 connectors. Disconnect the coolant pressure sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. Place one test lead on the coolant pressure SIGNAL pin at the C2 connector. Place the other test lead on all other pins at the C2 connector. Place one test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the C2 connector. Place the other test lead on all other pins at the C2 connector. Place one test lead on the coolant pressure SIGNAL pin at the C9 connector. Place the other test lead on all other pins at the C9 connector. Place one test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the C9 connector. Place the other test lead on all other pins at the C9 connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground.
>
> | **Conditions:** Disconnect the OEM harness at the C2 and C9 connectors. Disconnect the coolant pressure sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground. Place one test lead on the coolant pressure SIGNAL pin at the C2 connector. Place the other test lead on the engine ground. Place one test lead on the sensor SUPPLY +24-VDC pin at the C9 connector. Place the other test lead on the engine ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2D |  |
>
> #### STEP 2D. Check the coolant pressure sensor SUPPLY +24-VDC wire for voltage.
>
> | **Conditions:** Disconnect the coolant pressure sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant pressure sensor SUPPLY +24-VDC wire for voltage. Place one test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the sensor connector. Place the other test lead on the engine ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. | +24-VDC? **YESRepair:** Replace the coolant pressure sensor. Refer to the OEM service manual. Refer to Procedure 019-016 in Section 19. | Repair complete |
> | +24-VDC? **NORepair:** Replace the remote input/output unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
