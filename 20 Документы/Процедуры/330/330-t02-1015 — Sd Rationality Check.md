---
aliases:
  - "Останов: проверка достоверности"
type: "Процедура"
doc: "330-t02-1015"
title_en: "Sd Rationality Check"
title_ru: "Останов: проверка достоверности"
modified: "2024-08-13"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4358403"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1015.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1015.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/330"
  - "перевод/машинный"
---

# Sd Rationality Check
**Останов: проверка достоверности**

> [!abstract] Процедура · `330-t02-1015`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4358403 — Dual Fuel Technology DF101 Master Repair Manual|4358403]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2024-08-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1015.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1015.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

Двухтопливная эксплуатация остановится. Двигатель будет продолжать работать в дизельном режиме **только**.

### Как пользоваться этим деревом

**Описание:**

Сигнализация активируется, если разница между мощностью двигателя на основе потребления дизельного топлива и мощностью двигателя на основе значения, передаваемого от OEM / ECM, превышает 25 процентов номинальной мощности двигателя при заданной оборотной мощности и высоте по меньшей мере 4s до начала замены газа.

**Условия для проведения диагностики:**

Только активные в MAN и AUT перед переходом на работу с двойным топливом, когда выполнены все условия для работы с двойным топливом**.Условия для активации сообщения об отказе:**

Сигнализация активируется, если разница между мощностью двигателя на основе потребления дизельного топлива и мощностью двигателя на основе значения, передаваемого от OEM / ECM, превышает 25 процентов номинальной мощности двигателя при заданной оборотной мощности и высоте по меньшей мере 4s до начала замены газа.

**Условия автоматической очистки кода ошибки:**

Нет.

**Условия для ручной очистки кода ошибки:**

Неисправность защелкивания, сброс требуется. После активации Sd-сообщения контроллер переключается только на Diesel, и сообщение становится неактивным. При решении проблемы ее можно очистить от IMON или IV5, нажав сброс неисправностей.

### Практические замечания

Возможные причины включают:

- Неправильное чтение мощности

- Неправильное показание расхода топлива из-за дрейфа форсунки

- Отказ топливной системы двигателя.

| **Вводное сообщение FLS DetonationAnalog 4-20 мА сигнал отсутствует от IBF CU Input на аналоговом канале ввода** |  |  |
|---|---|---|
| **Код или сообщение** | **Разум** | **Эффект** |
| Останов: проверка достоверности | Проверка рациональности показывает, что расчетная мощность дизельного топлива (кВт) не соответствует терпимости. | Система двойного контроля топлива не позволит работать газу. Двойной топливный контроллер остановит поток газа. |

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте на ошибки. |  |
|  | **STEP 1A.** Проверьте ECM двигателя на наличие кодов неисправностей двигателя. | Двигатель ECM указывает коды неисправностей? |
|  | **STEP 1B.** Проверить сообщение(ы) об ошибке. | Код сигнализации Sd RationalCheck? |
|  | **STEP 1C.** Проверить сообщение(ы) об ошибке. | Коды сигнализации, кроме Sd RationalCheck, присутствуют? |
| ШАГ 2. | Загрузка двигателя **не** в пределах установленного предела. |  |
|  | **STEP 2A.** Проверить источник мощности двигателя. | Pump использует сообщение Real Power, показанное в J1939? |
|  | **STEP 2B.** Проверить значение передаваемой реальной мощности (J1939). | Соответствуют ли ограничения мощности, передаваемые J1939, номинальной мощности насоса? |
|  | **STEP 2C** Проверить ограничения нагрузки двигателя (Перевернуто). | Соответствуют ли ограничения мощности рейтингу мощности насоса? |
| ШАГ 3. | Проверьте сообщения о неисправности. |  |
|  | **СТАП 3А.** Сбросить вину. | Вернулись? |

### ШАГ 1. Проверьте на ошибки.

#### ШАГ 1A. Проверьте ECM двигателя на наличие кодов неисправностей двигателя.

| **Условия:** Включить переключатель зажигания. Подключите рекомендуемый электронный сервисный инструмент Cummins® или его эквивалент. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте рекомендованную электронную сервисную инструментальную программу Cummins® или эквивалентную для считывания кода ошибки. | Двигатель ECM указывает коды неисправностей? *Да | Устранение неисправностей двигателя перед устранением неисправностей кодов сигнализации. |
| Двигатель ECM указывает коды неисправностей? **НЕТ** | 1В |  |

#### ШАГ 1B. Просмотреть сообщение (сообщения) о неисправности.

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте локальную панель дисплея или IntelliMonitor на наличие сообщений о неисправности в списке тревоги и истории. | Код сигнализации Sd RationalCheck? *Да | 1С |
| Код сигнализации Sd RationalCheck? **НЕТ** | Верните насос в эксплуатацию и на монитор. |  |

#### ШАГ 1C. Просмотреть сообщение (сообщения) о неисправности.

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте локальную панель дисплея или IntelliMonitor на наличие сообщений о неисправности в списке тревоги и истории. | Коды сигнализации, кроме Sd RationalCheck, присутствуют? *Да | Устранение неполадок во всех других кодах ошибок до устранения неполадок Sd RationalCheck. |
| Коды сигнализации, кроме Sd RationalCheck, присутствуют? **НЕТ** | 2А |  |

### ШАГ 2. Загрузка двигателя **не** в пределах установленного предела.

#### ШАГ 2A. Проверьте источник мощности двигателя.

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте источник питания в PLC Monitor. (Переведено в J1939). | Pump использует сообщение Real Power, показанное в J1939? *Да | 2В |
| Pump использует сообщение Real Power, показанное в J1939? **НЕТ** | 2C |  |

#### ШАГ 2B. Проверка реального значения передаваемой мощности (J1939)

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. Подключите рекомендуемую электронную сервисную оснастку Cummins® или эквивалентную |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Значение монитора для Real Power, передаваемого через J1939 на экране IV5 7 OR IMON – ECU – Pwr-Real R. Проверка двигателя работает в пределах мощности. (двигатель мощностью 2250 л.с. 373-1578 кВт) (2500 л.с.: 373-1748 кВт) Если присутствует как вход 4-20ma, так и сообщение J1939, сообщение J1939 принимает приоритет и управление игнорирует преобразованный сигнал. Все ограничения должны быть в одном диапазоне. | Соответствуют ли ограничения мощности, передаваемые J1939, номинальной мощности насоса? *Да | 3А |
| Соответствуют ли ограничения мощности, передаваемые J1939, номинальной мощности насоса? **NORepair:** Для насоса с реальной мощностью J1939: Подключите рекомендованный инструмент электронного обслуживания Cummins® или эквивалент и убедитесь, что рейтинг мощности, передаваемый через ECM, является правильным. Если значение не соответствует OEM, то OEM или клиент должен исправить это значение. | Обратитесь в авторизованный сервисный центр Cummins®. |  |

#### ШАГ 2C. Проверьте ограничения нагрузки двигателя (конвертированный).

| **Условия:** Модуль управления питанием на двухтопливном топливе. Подключите InteliMonitor к панели управления двойным топливом. Подключите рекомендуемый электронный сервисный инструмент Cummins® или его эквивалент. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните значение, которое OEM передает для соответствия значениям Engine HP, считанным в IMON -Analog CU - FracPumpHP OEM посылает линейный сигнал в 4-20 мА, соответствующий 0-2500 л.с. (на основе рейтинга двигателя). | Соответствуют ли ограничения мощности рейтингу мощности насоса? *Да | 3А |
| Соответствуют ли ограничения мощности рейтингу мощности насоса? **NORepair: Для насосов с переоборудованными ограничениями мощности:** Использование DMM гарантирует, что сигнал оценки мощности на BF1-A2 является правильным. Если значение не соответствует OEM, то OEM или клиент должен исправить это значение. Если значение от OEM правильно и ошибка сохраняется, замените модуль IBF. | Ремонт завершён |  |

### ШАГ 3. Проверьте сообщения о неисправности.

#### ШАГ 3A. Снимите вину.

| **Условия:** Двигатель не работает. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сброс неисправности на панели управления или через InteliMonitor. Работайте с двигателем в условиях, позволяющих замену газа. | Вернулись? Исправьте любые неисправности двигателя. Попытка сбросить вину. Вернитесь к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |
| Вернулись? **НЕТ** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> Dual Fuel operation will stop. Engine will continue to operate in diesel **only** mode.
>
> ### How To Use This Tree
>
> **Circuit Description:**
>
> Alarm is activated if difference between engine power based on diesel consumption and engine power based on value transmitted from OEM/ECM is greater than 25 percent of engine rated power at given rpm and altitude for at least 4s prior to start of the gas substitution.
>
> **Conditions for Running the Diagnostics:**
>
> Only active in MAN and AUT before transition to Dual Fuel operation, when all condition for running in Dual fuel are met **.Conditions for Activating the Fault Message:**
>
> Alarm is activated if difference between engine power based on diesel consumption and engine power based on value transmitted from OEM/ECM is greater than 25 percent of engine rated power at given rpm and altitude for at least 4s prior to start of the gas substitution.
>
> **Conditions for Clearing the Fault Code Automatically:**
>
> None.
>
> **Conditions for Clearing the Fault Code Manually:**
>
> Latching fault, reset is required. Once Sd message is activated controller switches to Diesel only state, and the message will become inactive. When problem is solved it can be cleared from IMON or IV5 by pressing fault reset.
>
> ### Shoptalk
>
> Possible causes include:
>
> - Incorrect power reading
>
> - Incorrect fuel consumption reading due to injector drift
>
> - Engine fuel system failure.
>
> | **Fault Message FLS DetonationAnalog 4-20 mA Signal is Missing from IBF CU Input at Analog Input Channel** |  |  |
> |---|---|---|
> | **Code or Message** | **Reason** | **Effect** |
> | Sd Rationality Check | Rationality Check indicates the calculated diesel power (kW) is out of tolerance. | Dual fuel control system will **not** allow gas operations. Dual fuel controller will stop gas flow. |
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check for errors. |  |
> |  | **STEP 1A.** Check the engine ECM for engine fault codes. | Engine ECM indicates fault codes? |
> |  | **STEP 1B.** Review the fault message(s). | Sd RationalCheck alarm code present? |
> |  | **STEP 1C.** Review the fault message(s). | Alarm Codes other than Sd RationalCheck present? |
> | STEP 2. | Engine load **not** within set limit. |  |
> |  | **STEP 2A.** Verify source for engine power value. | Pump using Real Power message shown in J1939? |
> |  | **STEP 2B.** Verify Real Power transmitted value (J1939). | Do J1939 transmitted power limits correspond with pump power rating? |
> |  | **STEP 2C.** Verify engine load limits (Converted). | Do power limits correspond with pump power rating? |
> | STEP 3. | Check for fault messages. |  |
> |  | **STEP 3A.** Reset the fault. | Fault returns? |
>
> ### STEP 1. Check for errors.
>
> #### STEP 1A. Check the engine ECM for engine fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect the recommended Cummins® electronic service tool or equivalent. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use the recommended Cummins® electronic service tool or equivalent to read the fault code. | Engine ECM indicates fault codes? **YES** | Troubleshoot engine fault codes prior to Troubleshooting Alarm Codes. |
> | Engine ECM indicates fault codes? **NO** | 1B |  |
>
> #### STEP 1B. Review the fault message(s).
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check local display panel or IntelliMonitor for fault messages in alarm list and history. | Sd RationalCheck alarm code present? **YES** | 1C |
> | Sd RationalCheck alarm code present? **NO** | Return the pump to service and monitor. |  |
>
> #### STEP 1C. Review the fault message(s).
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check local display panel or IntelliMonitor for fault messages in alarm list and history. | Alarm Codes other than Sd RationalCheck present? **YES** | Troubleshoot all other error codes prior to troubleshooting Sd RationalCheck. |
> | Alarm Codes other than Sd RationalCheck present? **NO** | 2A |  |
>
> ### STEP 2. Engine load **not** within set limit.
>
> #### STEP 2A. Verify source for engine power value.
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify power source in PLC Monitor. (Converted or J1939). | Pump using Real Power message shown in J1939? **YES** | 2B |
> | Pump using Real Power message shown in J1939? **NO** | 2C |  |
>
> #### STEP 2B. Verify Real Power transmitted value (J1939).
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Monitor value for Real Power transmitted via J1939 on IV5 screen 7 OR IMON – ECU – Pwr-Real R. Verify engine is operating within power limits. (2250 HP engine 373-1578 kW) (2500 HP engine: 373-1748 kW) If both 4-20ma input and J1939 message are present, the J1939 message takes priority and control ignores the converted signal. All limits should still be in the same range. | Do J1939 transmitted power limits correspond with pump power rating? **YES** | 3A |
> | Do J1939 transmitted power limits correspond with pump power rating? **NORepair:** For pump with J1939 Real Power Value: Connect the recommended Cummins® electronic service tool or equivalent and verify that power rating transmitted through the ECM is correct. If value is incorrect from the OEM, then the OEM or customer needs to correct this value. | Contact a Cummins® Authorized Repair Location. |  |
>
> #### STEP 2C. Verify engine load limits (Converted).
>
> | **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the value the OEM is transmitting for Engine HP matches value read in IMON -Analog CU - FracPumpHP OEM sends linear signal as 4-20 mA corresponding to 0-2500 HP (based on engine rating). | Do power limits correspond with pump power rating? **YES** | 3A |
> | Do power limits correspond with pump power rating? **NORepair:For pumps with converted power limits:** Using a DMM ensure that power rating signal on BF1-A2 is correct. If value is incorrect from the OEM, then the OEM or customer needs to correct this value. If value from OEM is correct and error persists replace IBF Module. | Repair complete |  |
>
> ### STEP 3. Check for fault messages.
>
> #### STEP 3A. Reset the fault.
>
> | **Conditions:** Engine not operating. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Reset the fault on the control panel or through InteliMonitor. Operate the engine under conditions to allow gas substitution. | Fault returns? **YESRepair:** Verify all engine systems are working correctly. Correct any malfunctions on the engine. Attempt to reset the fault. Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |
> | Fault returns? **NO** | Repair complete. |  |
