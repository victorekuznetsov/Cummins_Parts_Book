---
aliases:
  - "Нет связи по SAE J1939 с дистанционным пультом"
type: "Процедура"
doc: "116-t02-1040"
title_en: "No SAE J1939 Communication Remote Panel"
title_ru: "Нет связи по SAE J1939 с дистанционным пультом"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1040.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1040.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# No SAE J1939 Communication Remote Panel
**Нет связи по SAE J1939 с дистанционным пультом**

> [!abstract] Процедура · `116-t02-1040`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1040.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1040.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- SAE J1939 Communication to DCU410 Unit (недоступная ссылка).

- Нет связи SAE J1939 с дистанционным дисплеем панели.

- Панель машинного отделения имеет связь SAE J1939.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Начните с проверки конечного резистора. Конечный резистор расположен на схемах проводов QSK19, QSK38, QSK50 и QSK60 CM850 на ремне электропроводки двигателя.

Шина данных SAE J1939 CAN предоставляет информацию на дисплей в удаленной панели.

Шина данных SAE J1939 CAN обеспечивает следующие параметры:

- Коды неисправностей двигателя

- Параметры двигателя, контролируемые ECM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс коробки проводов. |  |
|  | **STEP 1A.** Проверьте дисплей блока DCU410 на наличие неисправностей. |  |
|  | **STEP 1A-1.** Проверьте провод блока питания DCU410 на напряжение +24-VDC. |  |
| ШАГ 2. | Проверить сигнал шины данных SAE J1939 CAN. |  |
|  | **STEP 2A.** Проверить SAE J1939 CAN данные шины связи на двигателе. |  |
|  | **STEP 2B.** Проверьте связь шины данных SAE J1939 CAN на удаленной панели. |  |
| ШАГ 3. | Проверьте проводку удаленной панели. |  |
|  | **ШАГ 3А.** Проверить провода питания SAE J1939 на наличие открытого. |  |
|  | **ШАГ 3В.** Проверить обратный провод SAE J1939 на наличие открытого. |  |
|  | **STEP 3C.** Проверьте провод щита шины данных SAE J1939 на наличие открытого экрана. |  |
| ШАГ 4. | Проверьте проводку удаленной панели. |  |
|  | **STEP 4A.** Проверьте, может ли шина данных SAE J1939 обеспечивать подачу, возврат и экранные провода для короткого провода к проводу. |  |
|  | **STEP 4B.** Проверьте, может ли шина данных SAE J1939 обеспечивать подачу, возврат и экранные провода для короткого заземления. |  |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте дисплей блока DCU410 на наличие неисправностей.

| **Условия:** Найдите дисплей блока DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей блока DCU410 для указания неисправностей. | DCU410 указывает на неисправность (неисправности)? *Да | 2А |
| DCU410 указывает на неисправность (неисправности)? **НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте провод блока питания DCU410 на напряжение +24-VDC.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Поместите один тест на провод питания напряжения батареи 1 в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? **Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию OEM. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 2А |  |

### ШАГ 2. Проверить сигнал шины данных SAE J1939 CAN.

#### ШАГ 2A. Проверить SAE J1939 CAN данные шины связи на двигателе.

| **Условия:** Найдите электропроводку двигателя из ECM. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить SAE J1939 CAN данные шины связи на двигателе. Используйте инструмент электронного обслуживания INSITETM для установления связи. | Коммуникация установлена? *Да | 2В |
| Коммуникация установлена? **NORepair:** Для двигателей QSK19, обратитесь к Руководству по устранению неполадок и ремонту, Электронной системе управления, Модульной общей железнодорожной системе QSK19 CM850, Бюллетень 4021493. Для двигателей QSK38, QSK50 и QSK60, обратитесь к Руководству по устранению неполадок и ремонту, Электронной системе управления, QSK38, QSK50 и QSK60 (Модульная общая железнодорожная система CM850), Бюллетень 4021533. | Ремонт завершён |  |

#### ШАГ 2B. Проверьте связь шины данных SAE J1939 на удаленной панели.

| **Условия:** Откройте окно интерфейса клиента. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте связь шины данных SAE J1939 на удаленной панели. Используйте инструмент электронного обслуживания INSITETM для установления связи. | Коммуникация установлена? *Да | Ремонт завершён |
| Коммуникация установлена? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте проводку удаленной панели.

#### ШАГ 3A. Проверьте провод питания SAE J1939 на наличие открытого.

| **Условия:** Откройте окно интерфейса клиента. Найдите дисплей удаленной панели. Отсоедините провод питания SAE J1939 на блоке DCU410 и разъеме порта обслуживания. Отключите разъем C3. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания SAE J1939 на наличие открытого. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на провод подачи в разъем порта обслуживания шины данных SAE J1939 CAN. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на провод передачи данных шины SAE J1939 CAN на разъем C3. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 3B |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 3B. Проверьте обратный провод SAE J1939 на наличие открытого.

| **Условия:** Откройте окно интерфейса клиента. Найдите дисплей удаленной панели. Отсоедините провод возврата SAE J1939 на блоке DCU410 и разъеме порта обслуживания. Отключите разъем C3. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте обратный провод SAE J1939 на наличие открытого. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN в блок DCU410. Поместите другой измерительный щуп на обратный провод в разъем порта обслуживания шины данных SAE J1939 CAN. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN в блок DCU410. Поместите другой измерительный щуп на провод возврата шины данных SAE J1939 CAN на разъеме C3. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 3C |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 3C. Проверить SAE J1939 CAN данные шины экрана провода для открытого.

| **Условия:** Откройте окно интерфейса клиента. Найдите дисплей удаленной панели. Отсоедините провод щита шины данных SAE J1939 CAN на блоке DCU410 и разъеме порта обслуживания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить SAE J1939 CAN данные шины экрана провода для открытого. Поместите один измерительный щуп на провод шины данных SAE J1939 CAN в блок DCU410. Поместите другой измерительный щуп на обратный провод в разъем порта обслуживания шины данных SAE J1939 CAN. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 4А |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

### ШАГ 4. Проверьте проводку удаленной панели.

#### ШАГ 4A. Проверьте данные шины SAE J1939 CAN для подачи, возврата и экранных проводов для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. Найдите дисплей удаленной панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод передачи данных SAE J1939 CAN для короткого провода. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один измерительный щуп на провод шины данных SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 4B |  |

#### ШАГ 4B. Проверьте данные шины SAE J1939 CAN для подачи, возврата и экрана проводов для короткого приземления.

| **Условия:** Откройте окно интерфейса клиента. Найдите дисплей удаленной панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте данные шины SAE J1939 CAN для подачи, возврата и экрана проводов для короткого приземления. Поместите один измерительный щуп на провод передачи данных шины SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один измерительный щуп на провод возврата шины данных SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один измерительный щуп на провод шины данных SAE J1939 CAN в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | Обратитесь в авторизованный сервисный центр Cummins®. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - No SAE J1939 Communication to DCU410 unit.
>
> - No SAE J1939 communication with the remote panel display panel.
>
> - Engine room panel has SAE J1939 communication.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Start by checking the terminating resistor. The terminating resistor is located on the QSK19, QSK38, QSK50, and QSK60 CM850 wiring diagrams on the engine wiring harness.
>
> The SAE J1939 data link provides information to the display in the remote panel.
>
> The SAE J1939 data link provides the following parameters:
>
> - Engine fault codes
>
> - Engine parameters monitored by the ECM.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box wiring. |  |
> |  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
> |  | **STEP 1A-1.** Check the DCU410 unit power supply wire for voltage +24-VDC. |  |
> | STEP 2. | Check the SAE J1939 data link signal. |  |
> |  | **STEP 2A.** Check SAE J1939 data link communication on engine. |  |
> |  | **STEP 2B.** Check the SAE J1939 data link communication at remote panel. |  |
> | STEP 3. | Check the remote panel wiring. |  |
> |  | **STEP 3A.** Check SAE J1939 supply wire for an open. |  |
> |  | **STEP 3B.** Check SAE J1939 return wire for an open. |  |
> |  | **STEP 3C.** Check the SAE J1939 data link shield wire for an open. |  |
> | STEP 4. | Check the remote panel wiring. |  |
> |  | **STEP 4A.** Check the SAE J1939 data link supply, return, and shield wires for a wire-to-wire short. |  |
> |  | **STEP 4B.** Check the SAE J1939 data link supply, return, and shield wires for a short to ground. |  |
>
> ### STEP 1. Check the customer interface box.
>
> #### STEP 1A. Check the DCU410 unit display for faults.
>
> | **Conditions:** Locate the DCU410 unit display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 unit display for indication of faults. | DCU410 unit indicates fault(s)? **YES** | 2A |
> | DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |
>
> #### STEP 1A-1. Check the DCU410 unit power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 2A |  |
>
> ### STEP 2. Check the SAE J1939 data link signal.
>
> #### STEP 2A. Check SAE J1939 data link communication on engine.
>
> | **Conditions:** Locate the engine wiring harness from the ECM. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check SAE J1939 data link communication on engine. Use INSITE™ electronic service tool to establish communication. | Communication established? **YES** | 2B |
> | Communication established? **NORepair:** For QSK19 engines, refer to the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System, Bulletin 4021493. For QSK38, QSK50, and QSK60 engines, refer to Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60 (CM850 Modular Common Rail System), Bulletin 4021533. | Repair complete |  |
>
> #### STEP 2B. Check the SAE J1939 data link communication at the remote panel.
>
> | **Conditions:** Open the customer interface box. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link communication at the remote panel. Use INSITE™ electronic service tool to establish communication. | Communication established? **YES** | Repair complete |
> | Communication established? **NO** | 3A |  |
>
> ### STEP 3. Check the remote panel wiring.
>
> #### STEP 3A. Check SAE J1939 supply wire for an open.
>
> | **Conditions:** Open the customer interface box. Locate the remote panel display. Disconnect the SAE J1939 supply wire at the DCU410 unit and service port connector. Disconnect the C3 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check SAE J1939 supply wire for an open. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on the supply wire at the SAE J1939 data link service port connector. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link supply wire at the C3 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 3B. Check SAE J1939 return wire for an open.
>
> | **Conditions:** Open the customer interface box. Locate the remote panel display. Disconnect the SAE J1939 return wire at the DCU410 unit and service port connector. Disconnect the C3 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check SAE J1939 return wire for an open. Place one test lead on the SAE J1939 data link return wire at the DCU410 unit. Place the other test lead on the return wire at the SAE J1939 data link service port connector. Place one test lead on the SAE J1939 data link return wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link return wire at the C3 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3C |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 3C. Check SAE J1939 data link shield wire for an open.
>
> | **Conditions:** Open the customer interface box. Locate the remote panel display. Disconnect the SAE J1939 data link shield wire at the DCU410 unit and service port connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check SAE J1939 data link shield wire for an open. Place one test lead on the SAE J1939 data link shield wire at the DCU410 unit. Place the other test lead on the return wire at the SAE J1939 data link service port connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 4A |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> ### STEP 4. Check the remote panel wiring.
>
> #### STEP 4A. Check the SAE J1939 data link supply, return, and shield wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Locate the remote panel display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply wire for wire-to-wire short. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the SAE J1939 data link return wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the SAE J1939 data link shield wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 4B |  |
>
> #### STEP 4B. Check the SAE J1939 data link supply, return, and shield wires for a short to ground.
>
> | **Conditions:** Open the customer interface box. Locate the remote panel display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply, return, and shield wires for a short to ground. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the SAE J1939 data link return wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the SAE J1939 data link shield wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location. |  |
