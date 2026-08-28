---
aliases:
  - "Неисправность сигнала давления забортной воды"
type: "Процедура"
doc: "300-t02-1123"
title_en: "Sea Water Pressure Signal Malfunction"
title_ru: "Неисправность сигнала давления забортной воды"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1123.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1123.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
  - "перевод/машинный"
---

# Sea Water Pressure Signal Malfunction
**Неисправность сигнала давления забортной воды**

> [!abstract] Процедура · `300-t02-1123`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2022-02-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1123.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1123.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Датчик давления морской воды (OEM) производителя оригинального оборудования вышел из строя.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Датчик давления морской воды подключен к разъему сигнализации и безопасности C2, расположенному на окне интерфейса клиента (C.I.B.).

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте C.I.B. проводка. |  |
|  | **ШАГ 1А.** Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для открытой цепи. | Больше 100 тысяч ом? |
|  | **ШАГ 1В.** Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC проводов для короткого замыкания провода к проводу. | Менее 10 Ом? |
|  | **ШАГ 1С.** Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания на землю. | Менее 10 Ом? |
| ШАГ 2. | Проверьте жгут проводов изготовителя машины. |  |
|  | **ШАГ 2А.** Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для открытой цепи. | Больше 100 тысяч ом? |
|  | **ШАГ 2В.** Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC проводов для провода к проводу короткое замыкание. | Менее 10 Ом? |
|  | **STEP 2C.** Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания на землю. | Менее 10 Ом? |
|  | **ШАГ 2D.** Проверьте давление морской воды SUPPLY +24-VDC провода на напряжение. | +24-VDC? |

### ШАГ 1. Проверьте C.I.B. проводка.

#### ШАГ 1A. Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для открытой цепи.

| **Условия: **Открыть ЦБ. Отключите провода давления морской воды SIGNAL и датчик SUPPLY +24-VDC на панели управления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для открытой цепи. Примечание: Сигнал тревоги будет звучать на удаленном блоке ввода/вывода при обнаружении открытой цепи. Поместите один испытательный щуп на провод SIGNAL давления морской воды на панели управления. Поместите другой испытательный щуп на контакт сигнала давления морской воды на разъем С2. Поместите один испытательный щуп на провод датчика SUPPLY +24-VDC на панели управления. Поместите другой испытательный щуп на штифт датчика SUPPLY +24-VDC на разъем C2. См. схему или схему проводов для идентификации контакта с разъемом. | Больше 100 тысяч ом? *Да | 1В |
| Больше 100 тысяч ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1B. Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания провода к проводу.

| **Условия: **Открыть ЦБ. Отключите провода давления морской воды SIGNAL и датчик SUPPLY +24-VDC на панели управления. Отключите разъем C2. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания провода к проводу. Поместите один испытательный щуп на провод SIGNAL давления морской воды на панели управления. Поместите другой испытательный щуп на все другие провода на панели управления. Поместите один испытательный щуп на провод датчика SUPPLY +24-VDC на панели управления. Поместите другой испытательный щуп на все другие провода на панели управления. См. схему или схему проводов для идентификации контакта с разъемом. | Менее 10 Ом? Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания на землю.

| **Условия: **Открыть ЦБ. Отключите провода давления морской воды SIGNAL и датчик SUPPLY +24-VDC на панели управления. Отключите разъем C2. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания на землю. Поместите один испытательный щуп на провод SIGNAL давления морской воды на панели управления. Поместите другой испытательный щуп на землю панели. Поместите один испытательный щуп на провод датчика SUPPLY +24-VDC на панели управления. Поместите другой испытательный щуп на землю панели. См. схему или схему проводов для идентификации контакта с разъемом. | Менее 10 Ом? Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов изготовителя машины.

#### ШАГ 2A. Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для открытой цепи.

| **Условия: **Отключите проводку OEM-производителя на разъемах C2 и C9. Отключите датчик давления морской воды. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для открытой цепи. Примечание: Сигнал тревоги будет звучать на удаленном блоке ввода/вывода, если произошла ложная тревога. Поместите один испытательный щуп на контакт сигнала давления морской воды на разъеме С2. Поместите другой испытательный щуп на контакт сигнала давления морской воды на разъем С9. Поместите один испытательный щуп на датчик давления морской воды SUPPLY +24-VDC на разъеме C2. Поместите другой испытательный щуп на датчик давления морской воды SUPPLY +24-VDC на разъем C9. Поместите один испытательный щуп на контакт сигнала давления морской воды на разъеме C9. Поместите другой испытательный щуп на контакт сигнала давления морской воды на разъем датчика. Поместите один испытательный щуп на датчик давления морской воды SUPPLY +24-VDC на разъеме C9. Поместите другой испытательный щуп на датчик давления морской воды SUPPLY +24-VDC на разъем датчика. См. схему или схему проводов для идентификации контакта с разъемом. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2B. Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания провода к проводу.

| **Условия: **Отключите проводку OEM-производителя на разъемах C2 и C9. Отключите датчик давления морской воды. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания провода к проводу. Поместите один испытательный щуп на контакт сигнала давления морской воды на разъеме С2. Поместите другой испытательный щуп на все другие штифты на разъеме C2. Поместите один испытательный щуп на датчик SUPPLY +24-VDC на разъеме C2. Поместите другой испытательный щуп на все другие штифты на разъеме C2. Поместите один испытательный щуп на контакт сигнала давления морской воды на разъеме C9. Поместите другой испытательный щуп на все другие штифты на разъеме C9. Поместите один испытательный щуп на датчик SUPPLY +24-VDC на разъеме C9. Поместите другой испытательный щуп на все другие штифты на разъеме C9. См. схему или схему проводов для идентификации контакта с разъемом. | Менее 10 Ом? Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания на землю.

| **Условия: **Отключите проводку OEM-производителя на разъемах C2 и C9. Отключите датчик давления морской воды. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление морской воды SIGNAL и датчик SUPPLY +24-VDC провода для короткого замыкания на землю. Поместите один испытательный щуп на контакт сигнала давления морской воды на разъеме С2. Поместите другой испытательный щуп на землю двигателя. Поместите один испытательный щуп на датчик SUPPLY +24-VDC на разъеме C9. Поместите другой испытательный щуп на землю двигателя. См. схему или схему проводов для идентификации контакта с разъемом. | Менее 10 Ом? Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте давление морской воды SUPPLY +24-VDC провода на напряжение.

| **Условия: **Отключите разъем датчика давления морской воды. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление морской воды SUPPLY +24-VDC провода на напряжение. Поместите один испытательный щуп на датчик давления морской воды SUPPLY +24-VDC на разъем датчика. Поместите другой испытательный щуп на землю двигателя. См. схему или схему проводов для идентификации контакта с разъемом. | +24-VDC? Заменить датчик давления морской воды. См. сервисное руководство изготовителя машины. См. процедуру 019-452 в разделе 19. | Ремонт завершён |
| +24-VDC? **NORepair:** Заменить удаленный блок ввода/вывода. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The original equipment manufacturer (OEM) sea water pressure sensor has malfunctioned.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The sea water pressure sensor is connected to the alarm and safety C2 connector located on the customer interface box (C.I.B.).
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the C.I.B. wiring. |  |
> |  | **STEP 1A.** Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit. | Greater than 100k ohms? |
> |  | **STEP 1B.** Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. | Less than 10 ohms? |
> |  | **STEP 1C.** Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground. | Less than 10 ohms? |
> | STEP 2. | Check the OEM wiring harness. |  |
> |  | **STEP 2A.** Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit. | Greater than 100k ohms? |
> |  | **STEP 2B.** Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. | Less than 10 ohms? |
> |  | **STEP 2C.** Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground. | Less than 10 ohms? |
> |  | **STEP 2D.** Check the sea water pressure SUPPLY +24-VDC wire for voltage. | +24-VDC? |
>
> ### STEP 1. Check the C.I.B. wiring.
>
> #### STEP 1A. Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit.
>
> | **Conditions:** Open the C.I.B. Disconnect the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires at the control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit. Note: An alarm will sound on the remote input/output unit when an open circuit is detected. Place one test lead on the sea water pressure SIGNAL wire at the control panel. Place the other test lead on the sea water pressure SIGNAL pin at the C2 connector. Place one test lead on the sensor SUPPLY +24-VDC wire at the control panel. Place the other test lead on the sensor SUPPLY +24-VDC pin at the C2 connector. Refer to the circuit diagram or wiring diagram for connector pin identification. | Greater than 100k ohms? **YES** | 1B |
> | Greater than 100k ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> #### STEP 1B. Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit.
>
> | **Conditions:** Open the C.I.B. Disconnect the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires at the control panel. Disconnect the C2 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. Place one test lead on the sea water pressure SIGNAL wire at the control panel. Place the other test lead on all other wires at the control panel. Place one test lead on the sensor SUPPLY +24-VDC wire at the control panel. Place the other test lead on all other wires at the control panel. Refer to the circuit diagram or wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground.
>
> | **Conditions:** Open the C.I.B. Disconnect the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires at the control panel. Disconnect the C2 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground. Place one test lead on the sea water pressure SIGNAL wire at the control panel. Place the other test lead on the panel ground. Place one test lead on the sensor SUPPLY +24-VDC wire at the control panel. Place the other test lead on the panel ground. Refer to the circuit diagram or wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM wiring harness.
>
> #### STEP 2A. Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit.
>
> | **Conditions:** Disconnect the OEM harness at the C2 and C9 connectors. Disconnect the sea water pressure sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit. Note: An alarm will sound on the remote input/output unit when if a false alarm has occurred. Place one test lead on the sea water pressure SIGNAL pin at the C2 connector. Place the other test lead on the sea water pressure SIGNAL pin at the C9 connector. Place one test lead on the sea water pressure sensor SUPPLY +24-VDC pin at the C2 connector. Place the other test lead on the sea water pressure sensor SUPPLY +24-VDC pin at the C9 connector. Place one test lead on the sea water pressure SIGNAL pin at the C9 connector. Place the other test lead on the sea water pressure SIGNAL pin at the sensor connector. Place one test lead on the sea water pressure sensor SUPPLY +24-VDC pin at the C9 connector. Place the other test lead on the sea water pressure sensor SUPPLY +24-VDC pin at the sensor connector. Refer to the circuit diagram or wiring diagram for connector pin identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> #### STEP 2B. Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit.
>
> | **Conditions:** Disconnect the OEM harness at the C2 and C9 connectors. Disconnect the sea water pressure sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. Place one test lead on the sea water pressure SIGNAL pin at the C2 connector. Place the other test lead on all other pins at the C2 connector. Place one test lead on the sensor SUPPLY +24-VDC pin at the C2 connector. Place the other test lead on all other pins at the C2 connector. Place one test lead on the sea water pressure SIGNAL pin at the C9 connector. Place the other test lead on all other pins at the C9 connector. Place one test lead on the sensor SUPPLY +24-VDC pin at the C9 connector. Place the other test lead on all other pins at the C9 connector. Refer to the circuit diagram or wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground.
>
> | **Conditions:** Disconnect the OEM harness at the C2 and C9 connectors. Disconnect the sea water pressure sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the sea water pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground. Place one test lead on the sea water pressure SIGNAL pin at the C2 connector. Place the other test lead on the engine ground. Place one test lead on the sensor SUPPLY +24-VDC pin at the C9 connector. Place the other test lead on the engine ground. Refer to the circuit diagram or wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2D |  |
>
> #### STEP 2D. Check the sea water pressure SUPPLY +24-VDC wire for voltage.
>
> | **Conditions:** Disconnect the sea water pressure sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the sea water pressure SUPPLY +24-VDC wire for voltage. Place one test lead on the sea water pressure sensor SUPPLY +24-VDC pin at the sensor connector. Place the other test lead on the engine ground. Refer to the circuit diagram or wiring diagram for connector pin identification. | +24-VDC? **YESRepair:** Replace the sea water pressure sensor. Refer to the OEM service manual. Refer to Procedure 019-452 in Section 19. | Repair complete |
> | +24-VDC? **NORepair:** Replace the remote input/output unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
