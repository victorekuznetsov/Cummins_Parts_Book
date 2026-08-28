---
aliases:
  - "Неисправность сигнала впускного коллектора 2"
type: "Процедура"
doc: "116-t02-1119"
title_en: "Intake Manifold 2 Signal Malfunction"
title_ru: "Неисправность сигнала впускного коллектора 2"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1119.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1119.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Intake Manifold 2 Signal Malfunction
**Неисправность сигнала впускного коллектора 2**

> [!abstract] Процедура · `116-t02-1119`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1119.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1119.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Датчик температуры воздуха (правый задний бок) OEM-заряда вышел из строя.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Датчик температуры воздуха в правом боковом углу подключен к разъему сигнализации и безопасности C4, расположенному на окне интерфейса клиента.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс коробки проводов. |  |
|  | **ШАГ 1А.** Проверьте сигнал температуры воздуха (правый борт задней части), возврат и возврат 2 проводов для открытого. |  |
|  | **STEP 1B.** Проверьте сигнал температуры воздуха (правый берег задней части), возврат и возврат 2 проводов для короткого провода к проводу. |  |
|  | **STEP 1C** Проверьте температуру воздуха (правый задний) сигнального провода на короткое время до земли. |  |
| ШАГ 2. | Проверьте жгут проводов изготовителя машины. |  |
|  | **STEP 2A.** Проверьте сигнал температуры воздуха (правый берег задней части), возврат и возврат 2 проводов для открытого. |  |
|  | **STEP 2B.** Проверьте сигнал температуры воздуха (правый берег задней части), возврат и возврат 2 проводов для короткого провода к проводу. |  |
|  | **STEP 2C.** Проверьте сигнальный провод с заряженным воздухом (сзади справа) на короткое время до земли. |  |

### ШАГ 1. Проверьте клиентский интерфейс коробки проводов.

#### ШАГ 1A. Проверьте сигнал температуры воздуха (правый берег задней части), возврат и возврат 2 проводов для открытого.

| **Условия:** Откройте окно интерфейса клиента. Отключите сигнал температуры воздуха (задняя правая сторона) заряда, возврат и возврат 2 проводов на удаленном блоке ввода/вывода. Отключите разъем C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал температуры воздуха (правый берег задней части), возврат и возврат 2 проводов для открытого. Примечание: Сигнал тревоги будет звучать на удаленном блоке ввода/вывода при обнаружении открытого устройства. Поместите один испытательный щуп на провод сигнала температуры воздуха заряда (правый берег сзади) на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на контакт сигнала температуры воздуха заряда (правый берег задней части) на разъеме C4. Поместите один испытательный щуп на обратный провод с температурой воздуха заряда (правый берег сзади) на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на обратный контакт с температурой воздуха заряда (правый берег задней части) на разъеме C4. Поместите один испытательный щуп на заряд температуры воздуха (правый берег задней) 2 провода на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на заряд температуры воздуха (правый берег задней) 2-х штифт на разъеме C4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1B. Проверьте сигнал температуры воздуха (правый задний бок), возврат и возврат 2 проводов для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. Отключите сигнал температуры воздуха (задняя правая сторона) заряда, возврат и возврат 2 проводов на удаленном блоке ввода/вывода. Отключите разъем C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал температуры воздуха (правый задний бок), возврат и возврат 2 проводов для короткого провода к проводу. Поместите один испытательный щуп на провод сигнала температуры воздуха заряда (правый берег сзади) на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на все другие провода в удаленном блоке ввода/вывода. Поместите один испытательный щуп на обратный провод с температурой воздуха заряда (правый берег сзади) на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на все другие провода в удаленном блоке ввода/вывода. Поместите один испытательный щуп на заряд температуры воздуха (правый берег задней) 2 провода на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на все другие провода в удаленном блоке ввода/вывода. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте температуру воздуха заряда (правый задний) сигнального провода для короткого на землю.

| **Условия:** Откройте окно интерфейса клиента. Отключите сигнальный провод с температурой воздуха (правый берег сзади) на удаленном блоке ввода/вывода. Отключите разъем C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте температуру воздуха заряда (правый задний) сигнального провода для короткого на землю. Поместите один испытательный щуп на провод сигнала температуры воздуха заряда (правый берег сзади) на удаленном блоке ввода/вывода. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов изготовителя машины.

#### ШАГ 2A. Проверьте сигнал температуры воздуха (правый берег задней части), возврат и возврат 2 проводов для открытого.

| **Условия:** Отключите проводку OEM-производителя на разъемах C4 и C11. Отключите разъем датчика температуры воздуха (правый берег задней части). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал температуры воздуха (правый берег задней части), возврат и возврат 2 проводов для открытого. Примечание: Открытое устройство было обнаружено удаленным устройством ввода/вывода, если произошла ложная тревога. Поместите один испытательный щуп на контакт сигнала температуры воздуха заряда (правый берег задней части) на разъеме C4. Поместите другой испытательный щуп на контакт сигнала температуры воздуха заряда (правый берег задней части) на разъеме C11. Поместите один испытательный щуп на обратный контакт с температурой воздуха заряда (правый берег задней части) на разъеме C4. Поместите другой испытательный щуп на контакт обратной температуры воздуха (правый берег задней части) на разъеме C11. Поместите один испытательный щуп на заряд температуры воздуха (правый берег задней) 2 штифта на разъеме C4. Поместите другой испытательный щуп на заряд температуры воздуха (правый берег задней) 2-х штифта на разъеме C11. Поместите один испытательный щуп на контакт сигнала температуры воздуха заряда (правый берег задней части) на разъеме C11. Поместите другой испытательный щуп на контакт сигнала температуры воздуха заряда (задняя правая сторона) на датчик температуры воздуха заряда (задняя сторона правой стороны). Поместите один испытательный щуп на контакт обратной связи с температурой воздуха заряда (правый берег задней части) на разъеме C11. Поместите другой испытательный щуп на датчик температуры воздуха заряда (задняя правая сторона) обратного контакта на датчике температуры воздуха заряда (задняя сторона правой стороны). Поместите один испытательный щуп на заряд температуры воздуха (правый берег задней) 2 штифта на разъеме C11. Поместите другой испытательный щуп на датчик температуры воздуха заряда (задняя правая сторона) возврата 2 штифта на датчике температуры воздуха заряда (задняя сторона правой стороны). См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 2B. Проверьте сигнал температуры воздуха (правый задний бок), возврат и возврат 2 проводов для короткого провода к проводу.

| **Условия:** Отключите проводку OEM-производителя на разъемах C4 и C11. Отключите разъем датчика температуры воздуха (правый берег задней части). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал температуры воздуха (правый задний бок), верните и верните 2 провода для короткого провода. Поместите один испытательный щуп на контакт сигнала температуры воздуха заряда (правый берег задней части) на разъеме C4. Поместите другой испытательный щуп на все другие штифты в разъеме. Поместите один испытательный щуп на обратный контакт с температурой воздуха заряда (правый берег задней части) на разъеме C4. Поместите другой испытательный щуп на все другие штифты в разъеме. Поместите один испытательный щуп на заряд температуры воздуха (правый берег задней) 2 штифта на разъеме C4. Поместите другой испытательный щуп на все другие штифты в разъеме. Поместите один испытательный щуп на контакт сигнала температуры воздуха заряда (правый берег задней части) на разъеме C11. Поместите другой испытательный щуп на все другие штифты в разъеме. Поместите один испытательный щуп на контакт обратной связи с температурой воздуха заряда (правый берег задней части) на разъеме C11. Поместите другой испытательный щуп на все другие штифты в разъеме. Поместите один испытательный щуп на заряд температуры воздуха (правый берег задней) 2 штифта на разъеме C11. Поместите другой испытательный щуп на все другие штифты в разъеме. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте температуру воздуха заряда (правый задний) сигнального провода для короткого на землю.

| **Условия:** Отключите проводку OEM-производителя на разъемах C4 и C11. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте температуру воздуха заряда (правый задний) сигнального провода для короткого на землю. Поместите один испытательный щуп на контакт сигнала температуры воздуха заряда (правый берег задней части) на разъеме C4. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на контакт сигнала температуры воздуха заряда (правый берег задней части) на разъеме C11. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить датчик температуры воздуха (правый бортовой задний) заряда. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The OEM charge air temperature (right bank rear) sensor has malfunctioned.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The charge air temperature (right bank rear) sensor is connected to the Alarm and Safety C4 connector located on the customer interface box.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box wiring. |  |
> |  | **STEP 1A.** Check the charge air temperature (right bank rear) signal, return, and return 2 wires for an open. |  |
> |  | **STEP 1B.** Check the charge air temperature (right bank rear) signal, return, and return 2 wires for a wire-to-wire short. |  |
> |  | **STEP 1C.** Check the charge air temperature (right bank rear) signal wire for a short to ground. |  |
> | STEP 2. | Check the OEM wiring harness. |  |
> |  | **STEP 2A.** Check the charge air temperature (right bank rear) signal, return, and return 2 wires for an open. |  |
> |  | **STEP 2B.** Check the charge air temperature (right bank rear) signal, return, and return 2 wires for a wire-to-wire short. |  |
> |  | **STEP 2C.** Check the charge air temperature (right bank rear) signal wire for a short to ground. |  |
>
> ### STEP 1. Check the customer interface box wiring.
>
> #### STEP 1A. Check the charge air temperature (right bank rear) signal, return, and return 2 wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the charge air temperature (right bank rear) signal, return, and return 2 wires at the remote input/output unit. Disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the charge air temperature (right bank rear) signal, return, and return 2 wires for an open. NOTE: An alarm will sound on the remote input/output unit when an open is detected. Place one test lead on the charge air temperature (right bank rear) signal wire at the remote input/output unit. Place the other test lead on the charge air temperature (right bank rear) signal pin at the C4 connector. Place one test lead on the charge air temperature (right bank rear) return wire at the remote input/output unit. Place the other test lead on the charge air temperature (right bank rear) return pin at the C4 connector. Place one test lead on the charge air temperature (right bank rear) return 2 wire at the remote input/output unit. Place the other test lead on the charge air temperature (right bank rear) return 2 pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1B. Check the charge air temperature (right bank rear) signal, return, and return 2 wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the charge air temperature (right bank rear) signal, return, and return 2 wires at the remote input/output unit. Disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the charge air temperature (right bank rear) signal, return, and return 2 wires for a wire-to-wire short. Place one test lead on the charge air temperature (right bank rear) signal wire at the remote input/output unit. Place the other test lead on all other wires at the remote input/output unit. Place one test lead on the charge air temperature (right bank rear) return wire at the remote input/output unit. Place the other test lead on all other wires at the remote input/output unit. Place one test lead on the charge air temperature (right bank rear) return 2 wire at the remote input/output unit. Place the other test lead on all other wires at the remote input/output unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check the charge air temperature (right bank rear) signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the charge air temperature (right bank rear) signal wire at the remote input/output unit. Disconnect the C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the charge air temperature (right bank rear) signal wire for a short to ground. Place one test lead on the charge air temperature (right bank rear) signal wire at the remote input/output unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM wiring harness.
>
> #### STEP 2A. Check the charge air temperature (right bank rear) signal, return, and return 2 wires for an open.
>
> | **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the charge air temperature (right bank rear) sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the charge air temperature (right bank rear) signal, return, and return 2 wires for an open. NOTE: An open has been detected by the remote input/output unit if a false alarm has occurred. Place one test lead on the charge air temperature (right bank rear) signal pin at the C4 connector. Place the other test lead on the charge air temperature (right bank rear) signal pin at the C11 connector. Place one test lead on the charge air temperature (right bank rear) return pin at the C4 connector. Place the other test lead on the charge air temperature (right bank rear) return pin at the C11 connector. Place one test lead on the charge air temperature (right bank rear) return 2 pin at the C4 connector. Place the other test lead on the charge air temperature (right bank rear) return 2 pin at the C11 connector. Place one test lead on the charge air temperature (right bank rear) signal pin at the C11 connector. Place the other test lead on the charge air temperature (right bank rear) signal pin at the charge air temperature (right bank rear) sensor. Place one test lead on the charge air temperature (right bank rear) return pin at the C11 connector. Place the other test lead on the charge air temperature (right bank rear) return pin at the charge air temperature (right bank rear) sensor. Place one test lead on the charge air temperature (right bank rear) return 2 pin at the C11 connector. Place the other test lead on the charge air temperature (right bank rear) return 2 pin at the charge air temperature (right bank rear) sensor. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 2B. Check the charge air temperature (right bank rear) signal, return, and return 2 wires for a wire-to-wire short.
>
> | **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the charge air temperature (right bank rear) sensor connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the charge air temperature (right bank rear) signal, return and return 2 wires for a wire-to-wire short. Place one test lead on the charge air temperature (right bank rear) signal pin at the C4 connector. Place the other test lead on all other pins in the connector. Place one test lead on the charge air temperature (right bank rear) return pin at the C4 connector. Place the other test lead on all other pins in the connector. Place one test lead on the charge air temperature (right bank rear) return 2 pin at the C4 connector. Place the other test lead on all other pins in the connector. Place one test lead on the charge air temperature (right bank rear) signal pin at the C11 connector. Place the other test lead on all other pins in the connector. Place one test lead on the charge air temperature (right bank rear) return pin at the C11 connector. Place the other test lead on all other pins in the connector. Place one test lead on the charge air temperature (right bank rear) return 2 pin at the C11 connector. Place the other test lead on all other pins in the connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the charge air temperature (right bank rear) signal wire for a short to ground.
>
> | **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the charge air temperature (right bank rear) signal wire for a short to ground. Place one test lead on the charge air temperature (right bank rear) signal pin at the C4 connector. Place the other test lead on panel ground. Place one test lead on the charge air temperature (right bank rear) signal pin at the C11 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the charge air temperature (right bank rear) sensor. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
