---
aliases:
  - "Нет связи по SAE J1939 с дистанционным пультом"
type: "Процедура"
doc: "300-t02-1040"
title_en: "No SAE J1939 Communication Remote Panel"
title_ru: "Нет связи по SAE J1939 с дистанционным пультом"
modified: "2019-05-22"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1040.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1040.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
  - "перевод/машинный"
---

# No SAE J1939 Communication Remote Panel
**Нет связи по SAE J1939 с дистанционным пультом**

> [!abstract] Процедура · `300-t02-1040`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1040.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1040.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- No Society of Automotive Engineers (SAE) J1939 (недоступная ссылка)

- Нет связи SAE J1939 с дистанционным дисплеем панели

- Панель машинного отделения имеет связь SAE J1939.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Шаг 1 Устранение неполадок. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Начните с проверки конечного резистора. Конечный резистор расположен на схемах проводов QSM11 и QSB7-DM CM850 на ремне электропроводки двигателя.

Шина данных SAE J1939 CAN предоставляет информацию на дисплей в удаленной панели.

Шина данных SAE J1939 CAN обеспечивает следующие параметры:

- Коды неисправностей двигателя

- Параметры двигателя, контролируемые модулем управления двигателем (ECM).

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента (C.I.B.). |  |
|  | **STEP 1A.** Проверьте дисплеи панели управления на наличие неисправностей. | Панель управления указывает на неисправность (неисправности)? |
|  | **ШАГ 1А-1.** Проверьте питание панели управления Проводом SUPPLY на напряжение +24 ВДК. | Меньше +24 VDC? |
| ШАГ 2. | Проверить сигнал шины данных SAE J1939 CAN. |  |
|  | **STEP 2A.** Проверьте связь шины данных SAE J1939 с двигателем. | Коммуникация установлена? |
|  | **STEP 2B.** Проверьте связь шины данных SAE J1939 на удаленной панели. | Коммуникация установлена? |
| ШАГ 3. | Проверьте проводку удаленной панели. |  |
|  | **ШАГ 3А.** Проверьте провод SAE J1939 для открытой цепи. | Менее 10 Ом? |
|  | **ШАГ 3В.** Проверить провод SAE J1939 RETURN на наличие открытой цепи. | Менее 10 Ом? |
|  | **STEP 3C.** Проверьте провод щита шины данных SAE J1939 для открытой цепи. | Менее 10 Ом? |
| ШАГ 4. | Проверьте проводку удаленной панели. |  |
|  | **STEP 4A.** Проверьте шину данных SAE J1939 CAN SUPPY, RETURN, щитовые провода для короткого замыкания провода к проводу. | Менее 10 Ом? |
|  | **STEP 4B.** Проверьте шину данных SAE J1939 CAN SUPPY, RETURN, провода экрана для короткого замыкания на землю. | Менее 10 Ом? |

### ШАГ 1. Проверьте окно интерфейса клиента (C.I.B.).

#### ШАГ 1A. Проверьте дисплей панели управления на наличие неисправностей.

| **Условия: **Найдите дисплей панели управления. Подключите рекомендуемую электронную сервисную оснастку Cummins®. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей панели управления для указания неисправностей. | Панель управления указывает на неисправность (неисправности)? *Да | 2А |
| Панель управления указывает на неисправность (неисправности)? **НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте питание панели управления SUPPLY провода на напряжение +24 VDC.

| **Условия: **Открыть ЦБ. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжение (переключенная мощность) на панели управления. Поместите один тест на аккумулятор 1 напряжения SUPPLY провода на панели управления. Поместите другой испытательный щуп на землю панели. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24 VDC? **Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию производителя оригинального оборудования (OEM). | Ремонт завершён |
| Меньше +24 VDC? **НЕТ** | 2А |  |

### ШАГ 2. Проверить сигнал шины данных SAE J1939 CAN.

#### ШАГ 2A. Проверьте связь передачи данных на шинах SAE J1939 CAN на двигателе.

| **Условия: **Найдите электропроводку двигателя из ECM. Подключите рекомендуемую электронную сервисную оснастку Cummins®. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте связь передачи данных на шинах SAE J1939 CAN на двигателе. Используйте рекомендованный инструмент электронного обслуживания Cummins® для установления связи. | Коммуникация установлена? *Да | 2В |
| Коммуникация установлена? **NORepair:** Устранение неисправностей с помощью соответствующего кода ошибки. Справочное руководство по устранению неполадок в коде QSB7-DM CM850, Бюллетень 4325972, Раздел TF; или Руководство по устранению и ремонту неполадок в электронной системе управления ISM и QSM 11, Бюллетень [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Раздел TF; или Руководство по устранению неполадок в коде X15 CM2350 X125M, Бюллетень 5504346, Раздел TF. | Ремонт завершён |  |

#### ШАГ 2B. Проверьте связь шины данных SAE J1939 на удаленной панели.

| **Условия: **Открыть ЦБ. Подключите рекомендуемую электронную сервисную оснастку Cummins®. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте связь шины данных SAE J1939 на удаленной панели. Используйте рекомендованный инструмент электронного обслуживания Cummins® для установления связи. | Коммуникация установлена? *Да | Ремонт завершён |
| Коммуникация установлена? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте проводку удаленной панели.

#### ШАГ 3A. Проверить провод SAE J1939 для открытой цепи.

| **Условия: **Открыть ЦБ. Найдите дисплей удаленной панели. Отсоедините провод SAE J1939 SUPPLY на панели управления и разъеме порта обслуживания. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить провод SAE J1939 для открытой цепи. Поместите один измерительный щуп на шину данных SAE J1939 CAN SUPPLY провода на панели управления. Поместите другой измерительный щуп на провод SUPPLY в разъем порта обслуживания шины данных SAE J1939 CAN. Поместите один измерительный щуп на шину данных SAE J1939 CAN SUPPLY провода на панели управления. Поместите другой испытательный щуп на шину данных SAE J1939 CAN SUPPLY провода на разъеме C1. | Менее 10 Ом? *Да | 3B |
| Менее 10 Ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 3B. Проверить провод SAE J1939 RETURN на наличие открытой цепи.

| **Условия: **Открыть ЦБ. Найдите дисплей удаленной панели. Отсоедините провод SAE J1939 RETURN на панели управления и разъеме порта обслуживания. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить провод SAE J1939 RETURN на наличие открытой цепи. Поместите один измерительный щуп на провод КАН САЕ J1939 КАН ВПЕРЕДЕНЬ на панели управления. Поместите другой измерительный щуп на провод RETURN в разъем порта обслуживания шины данных SAE J1939 CAN. Поместите один измерительный щуп на провод КАН САЕ J1939 КАН ВПЕРЕДЕНЬ на панели управления. Поместите другой измерительный щуп на провод шины данных SAE J1939 CAN RETURN на разъеме C1. | Менее 10 Ом? *Да | 3C |
| Менее 10 Ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 3C. Проверьте щитовой провод SAE J1939 на наличие открытой цепи.

| **Условия: **Открыть ЦБ. Найдите дисплей удаленной панели. Отсоедините защитный провод SAE J1939 на панели управления и разъеме порта обслуживания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте щитовой провод SAE J1939 на наличие открытой цепи. Поместите один испытательный щуп на провод щита шины данных SAE J1939 CAN на панели управления. Поместите другой измерительный щуп на экранный провод в разъем порта обслуживания шины данных SAE J1939 CAN. | Менее 10 Ом? *Да | 4А |
| Менее 10 Ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

### ШАГ 4. Проверьте проводку удаленной панели.

#### ШАГ 4A. Проверьте шину данных SAE J1939 CAN SUPPY, RETURN, щитовые провода для короткого замыкания провода к проводу.

| **Условия: **Открыть ЦБ. Найдите дисплей удаленной панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте шину данных SAE J1939 CAN SUPPY, RETURN, щитовые провода для короткого замыкания провода к проводу. Поместите один измерительный щуп на шину данных SAE J1939 CAN SUPPLY провода на панели управления. Поместите другой испытательный щуп на все другие провода на панели управления. Поместите один измерительный щуп на провод КАН САЕ J1939 КАН ВПЕРЕДЕНЬ на панели управления. Поместите другой испытательный щуп на все другие провода на панели управления. Поместите один испытательный щуп на провод щита шины данных SAE J1939 CAN на панели управления. Поместите другой испытательный щуп на все другие провода на панели управления. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить панель управления. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 4А |  |

#### ШАГ 4B. Проверьте шину данных SAE J1939 CAN SUPPY, RETURN, провода экрана для короткого замыкания на землю.

| **Условия: **Открыть ЦБ. Найдите дисплей удаленной панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте шину данных SAE J1939 CAN SUPPY, RETURN, провода экрана для короткого замыкания на землю. Поместите один измерительный щуп на шину данных SAE J1939 CAN SUPPLY провода на панели управления. Поместите другой испытательный щуп на все другие провода на панели управления. Поместите один измерительный щуп на провод КАН САЕ J1939 КАН ВПЕРЕДЕНЬ на панели управления. Поместите другой испытательный щуп на все другие провода на панели управления. Поместите один испытательный щуп на провод щита шины данных SAE J1939 CAN на панели управления. Поместите другой испытательный щуп на все другие провода на панели управления. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить панель управления. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | Обратитесь в авторизованный сервисный центр Cummins®. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - No Society of Automotive Engineers (SAE) J1939 communication to the control panel
>
> - No SAE J1939 communication with the remote panel display panel
>
> - Engine room panel has SAE J1939 communication.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Start by checking the terminating resistor. The terminating resistor is located on the QSM11 and QSB7-DM CM850 wiring diagrams on the engine wiring harness.
>
> The SAE J1939 data link provides information to the display in the remote panel.
>
> The SAE J1939 data link provides the following parameters:
>
> - Engine fault codes
>
> - Engine parameters monitored by the engine control module (ECM).
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box (C.I.B.). |  |
> |  | **STEP 1A.** Check the control panel display for faults. | Control panel indicates fault(s)? |
> |  | **STEP 1A-1.** Check the control panel power SUPPLY wire for voltage +24 VDC. | Less than +24 VDC? |
> | STEP 2. | Check the SAE J1939 data link signal. |  |
> |  | **STEP 2A.** Check the SAE J1939 data link communication on the engine. | Communication established? |
> |  | **STEP 2B.** Check the SAE J1939 data link communication at the remote panel. | Communication established? |
> | STEP 3. | Check the remote panel wiring. |  |
> |  | **STEP 3A.** Check the SAE J1939 SUPPLY wire for an open circuit. | Less than 10 ohms? |
> |  | **STEP 3B.** Check the SAE J1939 RETURN wire for an open circuit. | Less than 10 ohms? |
> |  | **STEP 3C.** Check the SAE J1939 data link shield wire for an open circuit. | Less than 10 ohms? |
> | STEP 4. | Check the remote panel wiring. |  |
> |  | **STEP 4A.** Check the SAE J1939 data link SUPPY, RETURN, ans shield wires for a wire-to-wire short circuit. | Less than 10 ohms? |
> |  | **STEP 4B.** Check the SAE J1939 data link SUPPY, RETURN, ans shield wires for a short circuit to ground. | Less than 10 ohms? |
>
> ### STEP 1. Check the customer interface box (C.I.B.).
>
> #### STEP 1A. Check the control panel display for faults.
>
> | **Conditions:** Locate the control panel display. Connect the recommended Cummins® electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the control panel display for indication of faults. | Control panel indicated fault(s)? **YES** | 2A |
> | Control panel indicated fault(s)? **NO** | 1A-1 |  |
>
> #### STEP 1A-1. Check the control panel power SUPPLY wire for voltage +24 VDC.
>
> | **Conditions:** Open the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the battery 1 voltage (switched power) at the control panel. Place one test on the battery 1 voltage SUPPLY wire at the control panel. Place the other test lead on the panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24 VDC? **YESRepair:** Check the batteries. Refer to the original equipment manufacturer (OEM) service manual. | Repair complete |
> | Less than +24 VDC? **NO** | 2A |  |
>
> ### STEP 2. Check the SAE J1939 data link signal.
>
> #### STEP 2A. Check the SAE J1939 data link supply communication on the engine.
>
> | **Conditions:** Locate the engine wiring harness from the ECM. Connect the recommended Cummins® electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link supply communication on the engine. Use the recommended Cummins® electronic service tool to establish communication. | Communication established? **YES** | 2B |
> | Communication established? **NORepair:** Troubleshoot the appropriate fault code. Reference Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF; or ISM and QSM 11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF; or X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346, Section TF. | Repair complete |  |
>
> #### STEP 2B. Check the SAE J1939 data link communication at the remote panel.
>
> | **Conditions:** Open the C.I.B. Connect the recommended Cummins® electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link communication at the remote panel. Use the recommended Cummins® electronic service tool to establish communication. | Communication established? **YES** | Repair complete |
> | Communication established? **NO** | 3A |  |
>
> ### STEP 3. Check the remote panel wiring.
>
> #### STEP 3A. Check the SAE J1939 SUPPLY wire for an open circuit.
>
> | **Conditions:** Open the C.I.B. Locate the remote panel display. Disconnect the SAE J1939 SUPPLY wire at the control panel and service port connector. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 SUPPLY wire for an open circuit. Place one test lead on the SAE J1939 data link SUPPLY wire at the control panel. Place the other test lead on the SUPPLY wire at the SAE J1939 data link service port connector. Place one test lead on the SAE J1939 data link SUPPLY wire at the control panel. Place the other test lead on the SAE J1939 data link SUPPLY wire at the C1 connector. | Less than 10 ohms? **YES** | 3B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> #### STEP 3B. Check the SAE J1939 RETURN wire for an open circuit.
>
> | **Conditions:** Open the C.I.B. Locate the remote panel display. Disconnect the SAE J1939 RETURN wire at the control panel and service port connector. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 RETURN wire for an open circuit. Place one test lead on the SAE J1939 data link RETURN wire at the control panel. Place the other test lead on the RETURN wire at the SAE J1939 data link service port connector. Place one test lead on the SAE J1939 data link RETURN wire at the control panel. Place the other test lead on the SAE J1939 data link RETURN wire at the C1 connector. | Less than 10 ohms? **YES** | 3C |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> #### STEP 3C. Check the SAE J1939 shield wire for an open circuit.
>
> | **Conditions:** Open the C.I.B. Locate the remote panel display. Disconnect the SAE J1939 shield wire at the control panel and service port connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 shield wire for an open circuit. Place one test lead on the SAE J1939 data link shield wire at the control panel. Place the other test lead on the shield wire at the SAE J1939 data link service port connector. | Less than 10 ohms? **YES** | 4A |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> ### STEP 4. Check the remote panel wiring.
>
> #### STEP 4A. Check the SAE J1939 data link SUPPY, RETURN, ans shield wires for a wire-to-wire short circuit.
>
> | **Conditions:** Open the C.I.B. Locate the remote panel display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link SUPPY, RETURN, ans shield wires for a wire-to-wire short circuit. Place one test lead on the SAE J1939 data link SUPPLY wire at the control panel. Place the other test lead on all other wires at the control panel. Place one test lead on the SAE J1939 data link RETURN wire at the control panel. Place the other test lead on all other wires at the control panel. Place one test lead on the SAE J1939 data link shield wire at the control panel. Place the other test lead on all other wires at the control panel. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the control panel. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 4A |  |
>
> #### STEP 4B. Check the SAE J1939 data link SUPPY, RETURN, ans shield wires for a short circuit to ground.
>
> | **Conditions:** Open the C.I.B. Locate the remote panel display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 data link SUPPY, RETURN, ans shield wires for a short circuit to ground. Place one test lead on the SAE J1939 data link SUPPLY wire at the control panel. Place the other test lead on all other wires at the control panel. Place one test lead on the SAE J1939 data link RETURN wire at the control panel. Place the other test lead on all other wires at the control panel. Place one test lead on the SAE J1939 data link shield wire at the control panel. Place the other test lead on all other wires at the control panel. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the control panel. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location. |  |
