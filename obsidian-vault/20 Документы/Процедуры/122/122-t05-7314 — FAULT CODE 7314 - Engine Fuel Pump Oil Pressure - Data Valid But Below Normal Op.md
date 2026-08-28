---
aliases:
  - "Код 7314 — давление масла топливного насоса ниже нормы — наивысший уровень"
type: "Процедура"
doc: "122-t05-7314"
title_en: "FAULT CODE 7314 - Engine Fuel Pump Oil Pressure - Data Valid But Below Normal Operating Range- Most Severe Level"
title_ru: "Код 7314 — давление масла топливного насоса ниже нормы — наивысший уровень"
modified: "2020-05-21"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-7314.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-7314.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 7314 - Engine Fuel Pump Oil Pressure - Data Valid But Below Normal Operating Range- Most Severe Level
**Код 7314 — давление масла топливного насоса ниже нормы — наивысший уровень**

> [!abstract] Процедура · `122-t05-7314`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2020-05-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-7314.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-7314.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **ШАГ 1А.** Проверить первичные коды неисправностей. | Код 143, 415, 1362 активен или неактивен с более чем одним счетчиком за последние 25 часов работы двигателя? |
| ШАГ 2. | Датчик давления моторного масла топливного насоса застрял в диапазоне. |  |
|  | **STEP 2A.** Визуально осмотрите датчик на предмет повреждения. | Повреждения, обнаруженные на датчике давления моторного масла топливного насоса, разъемах или упряжке для проводов двигателя? |
|  | **STEP 2B** Проверить точность датчика давления моторного масла в топливном насосе. | Считывание датчика между рекомендованной электронной сервисной оснасткой Cummins® или эквивалентной ей и механическим калибром находится в пределах спецификации? |
| ШАГ 3. | Проверьте топливный насос привода моторного масла фильтра на предмет повреждения. |  |
|  | **ШАГ 3А.** Проверить наличие повреждений на топливном насосе привода смазочного масляного фильтра. | Поврежденный или заглушенный топливный насос приводной фильтр моторного масла? |
| ШАГ 4. | Проверьте давление масла топливного насоса. |  |
|  | **STEP 4A.** Проверить давление масла на выходе топливного насоса на головке фильтра моторного масла. | Давление масла в топливном насосе выше минимального давления масла? |
|  | **STEP 4B.** Проверить давление масла на выходе топливного насоса на головке фильтра моторного масла с установленным новым масляным фильтром. | Давление масла в топливном насосе выше минимального давления масла? |
| ШАГ 5. | Проверьте калибровку ECM и очистите коды ошибок. |  |
|  | **STEP 5A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 5B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте первичные коды неисправностей.

| **Условия:** Включите переключатель зажигания на электронном сервисном оборудовании Connect INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие активных кодов неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 143, 415, 1362 активен или неактивен с более чем одним счетчиком за последние 25 часов работы двигателя? *Да | Устранение неполадок с соответствующими кодами неисправностей. |
| Код 143 или 415 активных или неактивных с более чем одним счетчиком за последние 25 часов работы двигателя? **НЕТ** | 2А |  |

### ШАГ 2. Датчик давления моторного масла топливного насоса застрял в диапазоне.

#### ШАГ 2A. Визуально осмотрите контактные линзы датчика и разъема.

| **Условия:** Замок зажигания отключите датчик давления моторного масла топливного насоса от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите разъём проводов и разъём датчика давления моторного масла топливного насоса. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема изоляции Поврежденная блокировка разъема поврежденная закладка. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361]]В разделе 19. | Повреждения, обнаруженные на датчике давления моторного масла топливного насоса, разъемах или упряжке для проводов двигателя? **Ремонт:** Ремонт или замена только тех компонентов, которые были обнаружены за пределами указанных пределов. Замените датчик давления моторного масла топливного насоса.[[56-019-679 — Fuel Pump Lubricating Oil Supply Pressure Sensor\|См. процедуру 019-679]]В разделе 19. Ремонт или замена ремня электропроводки двигателя или разъемов.[[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043]]В разделе 19. | 5а |
| Повреждения, обнаруженные на датчике давления моторного масла топливного насоса, разъемах или упряжке для проводов двигателя? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте точность датчика давления моторного масла топливного насоса.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление масла топливного насоса на выходе головки фильтра масла топливного насоса. См. процедуру 019-679 в разделе 19. | Считывание датчика между рекомендованной электронной сервисной оснасткой Cummins® или эквивалентной ей и механическим калибром находится в пределах спецификации? *Да | 3А |
| Считывание датчика между рекомендованной электронной сервисной оснасткой Cummins® или эквивалентной ей и механическим калибром находится в пределах спецификации? **NORepair:** Заменить датчик давления моторного масла топливного насоса.[[56-019-679 — Fuel Pump Lubricating Oil Supply Pressure Sensor\|См. процедуру 019-679]]В разделе 19. | 5а |  |

### ШАГ 3. Проверьте топливный насос привода моторного масла фильтра на предмет повреждения.

#### ШАГ 3A. Проверьте наличие повреждений на топливном насосе привода смазочного масляного фильтра.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте топливный насос привода моторного масла фильтр. См. процедуру 007-110 в Таблице ассоциированных процедур. | Повреждение, обнаруженное на топливном насосе привода фильтра моторного масла? **Ремонт:** Заменить топливный насос приводным фильтром моторного масла. См. процедуру 007-110 в Таблице ассоциированных процедур. | 5а |
| Повреждение, обнаруженное на топливном насосе привода фильтра моторного масла? **НЕТ** | 4А |  |

### ШАГ 4. Проверьте давление масла топливного насоса.

#### ШАГ 4A. Проверить давление масла на выходе топливного насоса приводом моторного масла фильтрующей головки.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить давление масла на выходе из головки масляного фильтра топливного насоса. См. процедуру 007-110 в Таблице ассоциированных процедур. | Давление масла в топливном насосе выше минимального давления масла? *Да | 5а |
| Давление масла в топливном насосе выше минимального давления масла? **NORepair:** Заменить топливный насос приводным фильтром моторного масла. См. процедуру 007-110 в Таблице ассоциированных процедур. | 4B |  |

#### ШАГ 4B. Проверьте давление масла на выходе топливного насоса привода моторного масла с фильтром головки с новым масляным фильтром установлен.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить давление масла на выходе из головки масляного фильтра топливного насоса. См. процедуру 007-110 в Таблице ассоциированных процедур. | Давление масла в топливном насосе выше минимального давления масла? *Да | 5а |
| Давление масла в топливном насосе выше минимального давления масла? **НЕТ** | 5а |  |

### ШАГ 5. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 5A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички данных в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 5В |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032]]В разделе 19. | 5В |  |

#### ШАГ 5B. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да | Ремонт завершён. |
| Код неактивен? **Секретарь:**Проверить, что все шаги были выполнены. Если все шаги были выполнены, то следуйте своему техническому процессу эскалации. | Эскалация или призыв к помощи. |  |

## Связанные процедуры

| Связанные процедуры |  |  |  |
|---|---|---|---|
| Название процедуры | Процедурный номер | Модель двигателя | Номер бюллетеня |
| Фильтр для моторного масла Fuel Pump Drive | См. процедуру 007-110 | QSK45 и QSK60 | [[4021530 — QSK45 and QSK60 Service Manual\|4021530]] |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for primary fault codes. | Fault Code 143, 415, 1362 active or inactive with more than one count in the last 25 engine hours? |
> | STEP 2. | Fuel pump lubricating oil pressure sensor stuck in-range. |  |
> |  | **STEP 2A.** Visually inspect the sensor for damage. | Damage found on the fuel pump lubricating oil pressure sensor, connectors, or engine wiring harness? |
> |  | **STEP 2B.** Verify fuel pump lubricating oil pressure sensor's accuracy. | Sensor reading between the recommended Cummins® electronic service tool or equivalent and the mechanical gauge is within specification? |
> | STEP 3. | Check the fuel pump drive lubricating oil filter for damage. |  |
> |  | **STEP 3A.** Check for damage on the fuel pump drive lubricating oil filter. | Damaged or plugged fuel pump drive lubricating oil filter? |
> | STEP 4. | Check Fuel Pump Oil Pressure. |  |
> |  | **STEP 4A.** Verify oil pressure at the outlet of the fuel pump drive lubricating oil filter head. | Fuel pump oil pressure is above the minimum oil pressure? |
> |  | **STEP 4B.** Verify oil pressure at the outlet of the fuel pump drive lubricating oil filter head with the new oil filter installed. | Fuel pump oil pressure is above the minimum oil pressure? |
> | STEP 5. | Check ECM calibration and clear the fault codes. |  |
> |  | **STEP 5A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 5B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for primary fault codes.
>
> | **Conditions:** Turn keyswitch ON Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for active fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 143, 415, 1362 active or inactive with more than one count in the last 25 engine hours? **YES** | Troubleshoot the appropriate fault codes. |
> | Fault Code 143 or 415 active or inactive with more than one count in the last 25 engine hours? **NO** | 2A |  |
>
> ### STEP 2. Fuel pump lubricating oil pressure sensor stuck in-range.
>
> #### STEP 2A. Visually inspect the sensor and connector pins.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the fuel pump lubricating oil pressure sensor from the engine wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the harness connector and fuel pump lubricating oil pressure sensor connector. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damaged Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361]] in Section 19. | Damage found on the fuel pump lubricating oil pressure sensor, connectors or engine wiring harness? **YESRepair:** Repair or replace only the components that were found to be out of specification. Replace the fuel pump lubricating oil pressure sensor. [[56-019-679 — Fuel Pump Lubricating Oil Supply Pressure Sensor\|Refer to Procedure 019-679]] in Section 19. Repair or replace the engine wiring harness or connectors. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043]] in Section 19. | 5A |
> | Damage found on the fuel pump lubricating oil pressure sensor, connectors, or engine wiring harness? **NO** | 2B |  |
>
> #### STEP 2B. Verify fuel pump lubricating oil pressure sensor's accuracy.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel pump oil pressure at the outlet of the fuel pump oil filter head. Refer to Procedure 019-679 in Section 19. | Sensor reading between the recommended Cummins® electronic service tool or equivalent and the mechanical gauge is within specification? **YES** | 3A |
> | Sensor reading between the recommended Cummins® electronic service tool or equivalent and the mechanical gauge is within specification? **NORepair:** Replace the fuel pump lubricating oil pressure sensor. [[56-019-679 — Fuel Pump Lubricating Oil Supply Pressure Sensor\|Refer to Procedure 019-679]] in Section 19. | 5A |  |
>
> ### STEP 3. Check the fuel pump drive lubricating oil filter for damage.
>
> #### STEP 3A. Check for damage on the fuel pump drive lubricating oil filter.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel pump drive lubricating oil filter. Refer to Procedure 007-110 in the Associated Procedures Table. | Damage found on the fuel pump drive lubricating oil filter? **YESRepair:** Replace the fuel pump drive lubricating oil filter. Refer to Procedure 007-110 in the Associated Procedures Table. | 5A |
> | Damage found on the fuel pump drive lubricating oil filter? **NO** | 4A |  |
>
> ### STEP 4. Check Fuel Pump Oil Pressure.
>
> #### STEP 4A. Verify oil pressure at the outlet of the fuel pump drive lubricating oil filter head.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify oil pressure at the outlet of the fuel pump oil filter head. Refer to Procedure 007-110 in the Associated Procedures Table. | Fuel pump oil pressure is above the minimum oil pressure? **YES** | 5A |
> | Fuel pump oil pressure is above the minimum oil pressure? **NORepair:** Replace the fuel pump drive lubricating oil filter. Refer to Procedure 007-110 in the Associated Procedures Table. | 4B |  |
>
> #### STEP 4B. Verify oil pressure at the outlet of the fuel pump drive lubricating oil filter head with new oil filter installed.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify oil pressure at the outlet of the fuel pump oil filter head. Refer to Procedure 007-110 in the Associated Procedures Table. | Fuel pump oil pressure is above the minimum oil pressure? **YES** | 5A |
> | Fuel pump oil pressure is above the minimum oil pressure? **NO** | 5A |  |
>
> ### STEP 5. Check ECM calibration and clear fault codes.
>
> #### STEP 5A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 5B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032]] in Section 19. | 5B |  |
>
> #### STEP 5B. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable and clear the fault code. Operate the engine within the “Conditions for Clearing the Fault Code” found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
> | Fault code inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow your technical escalation process. | Escalate or Call for assistance. |  |
>
> ## Associated Procedures
>
> | Associated Procedures |  |  |  |
> |---|---|---|---|
> | Procedure Title | Procedure Number | Engine Model | Bulletin Number |
> | Fuel Pump Drive Lubricating Oil Filter | [[56-007-110-tr — Fuel Pump Drive Lubricating Oil Filter\|Refer to Procedure 007-110]] | QSK45 and QSK60 | [[4021530 — QSK45 and QSK60 Service Manual\|4021530]] |
