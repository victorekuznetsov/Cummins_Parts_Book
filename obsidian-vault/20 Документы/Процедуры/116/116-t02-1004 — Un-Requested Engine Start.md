---
aliases:
  - "Самопроизвольный пуск двигателя"
type: "Процедура"
doc: "116-t02-1004"
title_en: "Un-Requested Engine Start"
title_ru: "Самопроизвольный пуск двигателя"
modified: "2008-05-29"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1004.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1004.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Un-Requested Engine Start
**Самопроизвольный пуск двигателя**

> [!abstract] Процедура · `116-t02-1004`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1004.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1004.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель работает без нажатия оператором кнопки запуска на блоке DCU410 или удаленной панели.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента. |  |
|  | **STEP 1A.** Проверьте логическую блокировку светодиодного освещения в интерфейсе клиента. |  |
|  | **STEP 1B.** Проверьте провод питания DCU410 на напряжение +24-VDC. |  |
|  | **STEP 1C.** Проверьте провод дистанционного пускового питания на наличие открытого. |  |
|  | **STEP 1D.** Проверьте провод сигнала реле-ретранслятора стартера на наличие открытого. |  |
|  | **ШАГ 1Е.** Проверить провода питания и возврата SAE J1939 на наличие открытого источника. |  |
|  | **STEP 1F.** Проверьте, может ли шина передачи данных SAE J1939 подавать и возвращать провода для короткого провода к проводу. |  |
|  | **STEP 1G.** Проверьте провод передачи данных шины SAE J1939 на короткое время до земли. |  |
| ШАГ 2. | Проверьте жгут проводов изготовителя машины. |  |
|  | **STEP 2A.** Проверьте сигнал переключателя реле стартера и провода возврата для открытого. |  |
|  | **STEP 2B.** Проверьте сигнал переключателя реле стартера и провода возврата для короткого провода к проводу. |  |
|  | **STEP 2C.** Проверить сигнальный провод стартового реле-переключателя на короткое время до заземления. |  |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте логическое устройство клиентского интерфейса LED подсветка.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте лампу с коленчатым приводом на блоке DCU 410 или удаленной панели для освещения. | Светильник с кривошипом? *Да | 1В |
| Светильник с кривошипом? **НЕТ** | Свяжитесь с авторизованным местом ремонта Cummins® |  |

#### ШАГ 1B. Проверьте провод питания DCU410 на напряжение +24-VDC.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Проведите один тест на питающем проводе с напряжением батареи 1 (переключенной мощностью) в блоке DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? **Ремонт:** Проверить аккумуляторы. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте провод дистанционного запуска для открытия.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод дистанционного пускового питания от блока DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод дистанционного запуска для открытия. Поместите один испытательный щуп на провод дистанционного пускового питания в блок DCU410. Поместите другой испытательный щуп дистанционного пуска провода питания на соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1D |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1D. Проверьте провод сигнала реле-ретранслятора стартера на блоке DCU410 и разъеме C1 для открытого.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод сигнала реле-ретранслятора стартера на блоке DCU410 и разъеме C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод сигнала реле-ретранслятора стартера на блоке DCU410 и разъеме C1 для открытого. Поместите один испытательный щуп на провод сигнала реле стартера в блок DCU410. Поместите другой испытательный щуп на провод сигнала стартового реле переключателя в разъем С1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1Е |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1E. Проверьте данные шины SAE J1939 CAN для подачи и возврата проводов для открытого доступа.

| **Условия:** Откройте окно интерфейса клиента. Отключите шину передачи данных SAE J1939 CAN от блока DCU410, разъема C3 и соединения X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провода передачи и возврата данных SAE J1939 CAN на блоке DCU410, разъеме C3 и соединении X4 для открытого доступа. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на провод передачи данных шины SAE J1939 CAN на разъем C3. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на провод передачи данных шины SAE J1939 CAN на разъем X4. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN в блок DCU410. Поместите другой измерительный щуп на провод возврата шины данных SAE J1939 CAN на разъеме C3. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN в блок DCU410. Поместите другой измерительный щуп на провод возврата шины данных SAE J1939 CAN на разъем X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1F |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1F. Проверьте данные шины SAE J1939 CAN для подачи и возврата проводов для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. Отключите шину передачи данных SAE J1939 CAN от блока DCU410, разъема C3 и соединения X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте данные шины SAE J1939 CAN на блоке DCU410 для короткого провода. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1G |  |

#### ШАГ 1G. Проверьте провод передачи данных SAE J1939 CAN для короткого заземления.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод передачи данных шины SAE J1939 в блоке DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод передачи данных шины SAE J1939 CAN на блоке DCU410 для короткого заземления. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов изготовителя машины.

#### ШАГ 2A. Проверьте сигнал переключателя реле стартера и верните провода для открытого.

| **Условия:** Откройте окно интерфейса клиента. Отключите сигнал переключателя реле стартера и возвращайте провода на разъеме C1 и запустите терминал кольца двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал переключателя реле стартера и провода возврата на разъеме C1 для открытого. Поместите один испытательный щуп на провод сигнала стартового реле переключателя в разъем С1. Поместите другой испытательный щуп на провод сигнала переключателя стартового реле в пусковой двигательный кольцевой терминал. Поместите один испытательный щуп на провод возврата реле стартера в разъеме C1. Поместите другой испытательный щуп на провод возврата реле стартера в пусковой кольцевой терминал. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 2B. Проверьте сигнал переключателя реле стартера и возвращайте провода для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал переключателя реле стартера и возвращайте провода на разъеме C1 для короткого провода к проводу. Поместите один испытательный щуп на провод сигнала стартового реле переключателя в разъем С1. Поместите другой испытательный щуп на все другие провода в разъем С1. Поместите один испытательный щуп на провод возврата реле стартера в разъеме C1. Поместите другой испытательный щуп на все другие провода в разъем С1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте стартовый реле переключатель сигнала провода для короткого на землю.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте стартовый релейный сигнальный провод на разъеме C1 для короткого заземления. Поместите один испытательный щуп на провод сигнала стартового реле переключателя в разъем С1. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить разъем. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine cranks without the operator pushing the start button on the DCU410 unit or remote panel.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box. |  |
> |  | **STEP 1A.** Check the customer interface box logic unit LED illumination. |  |
> |  | **STEP 1B.** Check the DCU410 power supply wire for voltage +24-VDC. |  |
> |  | **STEP 1C.** Check the remote start supply wire for an open. |  |
> |  | **STEP 1D.** Check the starter relay switch signal wire for an open. |  |
> |  | **STEP 1E.** Check the SAE J1939 supply and return wires for an open. |  |
> |  | **STEP 1F.** Check the SAE J1939 data link supply and return wires for a wire-to-wire short. |  |
> |  | **STEP 1G.** Check the SAE J1939 data link supply wire for a short to ground. |  |
> | STEP 2. | Check the OEM wiring harness. |  |
> |  | **STEP 2A.** Check the starter relay switch signal and return wires for an open. |  |
> |  | **STEP 2B.** Check the starter relay switch signal and return wires for a wire-to-wire short. |  |
> |  | **STEP 2C.** Check the starter relay switch signal wire for a short to ground. |  |
>
> ### STEP 1. Check the customer interface box.
>
> #### STEP 1A. Check the customer interface box logic unit LED illumination.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the crank lamp LED on the DCU 410 unit or remote panel for illumination. | Crank lamp illuminated? **YES** | 1B |
> | Crank lamp illuminated? **NO** | Contact a Cummins® Authorized Repair Location |  |
>
> #### STEP 1B. Check the DCU410 power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 1C |  |
>
> #### STEP 1C. Check the remote start supply wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the remote start supply wire from the DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote start supply wire for an open. Place one test lead on the remote start supply wire at the DCU410 unit. Place the other test lead remote start supply wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1D. Check the starter relay switch signal wire at the DCU410 unit and C1 connector for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the starter relay switch signal wire at the DCU410 unit and C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter relay switch signal wire at the DCU410 unit and C1 connector for an open. Place one test lead on the starter relay switch signal wire at the DCU410 unit. Place the other test lead on the starter relay switch signal wire at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1E |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1E. Check the SAE J1939 data link supply and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link supply and return wires from the DCU410 unit, C3 connector, and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply and return wires at the DCU410 unit, C3 connector, and X4 connection for an open. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link supply wire at the C3 connector. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link supply wire at the X4 connector. Place one test lead on the SAE J1939 data link return wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link return wire at the C3 connector. Place one test lead on the SAE J1939 data link return wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link return wire at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1F |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1F. Check the SAE J1939 data link supply and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link supply and return wires from the DCU410 unit, C3 connector, and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply and return wires at the DCU410 unit for a wire-to-wire short. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the SAE J1939 data link return wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 1G |  |
>
> #### STEP 1G. Check the SAE J1939 data link supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the SAE J1939 data link supply wire at the DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply wire at the DCU410 unit for a short to ground. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM wiring harness.
>
> #### STEP 2A. Check the starter relay switch signal and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the starter relay switch signal and return wires at the C1 connector and start motor ring terminal. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter relay switch signal and return wires at the C1 connector for an open. Place one test lead on the starter relay switch signal wire at the C1 connector. Place the other test lead on the starter relay switch signal wire at the starting motor ring terminal. Place one test lead on the starter relay switch return wire at the C1 connector. Place the other test lead on the starter relay switch return wire at the starting motor ring terminal. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 2B. Check the starter relay switch signal and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter relay switch signal and return wires at the C1 connector for a wire-to-wire short. Place one test lead on the starter relay switch signal wire at the C1 connector. Place the other test lead on all other wires at the C1 connector. Place one test lead on the starter relay switch return wire at the C1 connector. Place the other test lead on all other wires at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the starter relay switch signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter relay switch signal wire at the C1 connector for a short to ground. Place one test lead on the starter relay switch signal wire at the C1 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the connector. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |  |
