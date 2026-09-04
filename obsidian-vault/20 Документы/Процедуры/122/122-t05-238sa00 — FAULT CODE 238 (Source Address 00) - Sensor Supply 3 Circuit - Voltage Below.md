---
aliases:
  - "Код 238 (адрес 00) — цепь питания датчиков 3 — напряжение ниже нормы"
type: "Процедура"
doc: "122-t05-238sa00"
title_en: "FAULT CODE 238 (Source Address 00) - Sensor Supply 3 Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Код 238 (адрес 00) — цепь питания датчиков 3 — напряжение ниже нормы"
modified: "2018-06-27"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-238sa00.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-238sa00.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 238 (Source Address 00) - Sensor Supply 3 Circuit - Voltage Below Normal or Shorted to Low Source
**Код 238 (адрес 00) — цепь питания датчиков 3 — напряжение ниже нормы**

> [!abstract] Процедура · `122-t05-238sa00`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-06-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-238sa00.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-238sa00.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения новой ECM, все другие активные коды неисправностей должны быть исследованы до замены ECM.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 — пробный щуп типа штепсельной заглушки DeutschTM/AMPTM/Metri-PackTM, номер детали 3822917 — пробный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM, номер детали 3164596 — штыревой пробный щуп FramatomeTM, а номер детали 3164597 — гнездовой пробный щуп FramatomeTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить наличие активного кода неисправности. | Код ошибки 238 активный или неактивный с количеством более 1 за последние 25 часов работы двигателя? |
| ШАГ 2. | Проверьте датчики и схемы, подключенные к датчику питания 3 и возвращайтесь. |  |
|  | **STEP 2A.** Осмотрите датчик скорости/положения коленчатого вала двигателя и схему, подключенную к датчику питания 3 и возврата | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте реакцию цепи. | Код ошибки 238 активен? |
| ШАГ 3. | Проверьте ECM. |  |
|  | **STEP 3A.** Проверить контакты разъема ECM и проводов двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте реакцию модуля управления двигателем (ECM). | Код ошибки 238 активен? |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 4B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте активный код ошибки.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 238 активный или неактивный с количеством более 1 за последние 25 часов работы двигателя? *Да | 2А |
| Код ошибки 238 активный или неактивный с количеством более 1 за последние 25 часов работы двигателя? **НЕТ** | Ремонт завершён |  |

### ШАГ 2. Проверьте датчики и схемы, подключенные к датчику питания 3 и возвращайтесь.

#### ШАГ 2A. Осмотрите разъем датчика скорости/положения коленчатого вала двигателя и схему, подключенную к источнику 3 питания датчика и возврату.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика скорости/положения коленчатого вала двигателя от разъема ремня электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъёма датчика скорости/положения коленчатого вала двигателя для следующих элементов: Разъем разъема разъединенного типа разъединенного типа разъема разъединенного типа или разъединенного типа разъема или разъема поврежденной оболочки разъема поврежденной разъемной запирающей вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В датчике скорости/положения коленчатого вала двигателя или разъёме ремня электропроводки было обнаружено поврежденное соединение. Очистите разъем и булавки. Ремонт или замена поврежденного участка проводов двигателя жгутом. См. процедуру 019-043 в Таблице ассоциированных процедур. Ремонт или замена поврежденного датчика скорости коленчатого вала двигателя. См. процедуру 019-042 в Таблице ассоциированных процедур. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика скорости/положения коленчатого вала двигателя от разъема ремня электропроводки двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующий ответ на ECM через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 238 активен? *Да | 3А |
| Код ошибки 238 активен? **NORepair:** Заменить поврежденный датчик скорости/положения коленчатого вала двигателя. См. процедуру 019-042 в Таблице ассоциированных процедур. | 4А |  |

### ШАГ 3. Проверьте ECM.

#### ШАГ 3A. Проверьте контакты разъема ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините разъем электропроводки ремня от разъема ECM 60-pin. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактную проводку двигателя и соединительный контакт ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъеме ECM или в ремне электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. См. схему или схему проводов для всех соединений проводов. Ремонт или замена только компонентов и/или поврежденных секций электропроводки двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. См. процедуру 019-031 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте реакцию ECM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема 60-контактных разъемов ECM. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактную проводку двигателя и соединительный контакт ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Код ошибки 238 активен? Заменить ЭКМ. См. процедуру 019-031 в разделе 19. | 4А |
| Код ошибки 238 активен? **NORepair: **Устранение неполадок в каждой части проводных ремней, соединенных последовательно, для определения того, какая из них содержит короткое замыкание на землю или короткое замыкание контакт-контакт. См. схему или схему проводов для всех соединений проводов. Ремонт или замена поврежденного участка проводов двигателя жгутом. См. процедуру 019-043 в Таблице ассоциированных процедур. | 4А |  |

### ШАГ 4. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 4A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 4B |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM. См. процедуру 019-032 в разделе 19. | 4B |  |

#### ШАГ 4B. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да | Ремонт завершён |
| Код неактивен? **Секретарь:**Проверить, что все шаги были выполнены. Если все шаги были выполнены, то следуйте своему техническому процессу эскалации. | Эскалация или призыв к помощи |  |

## Связанные процедуры

| Связанные процедуры |  |  |  |
|---|---|---|---|
| Название процедуры | Процедурный номер | Модельный сервис | Номер бюллетеня |
| Датчик частоты вращения двигателя (ESS) | [[122-019-042 — Engine Speed Sensor (ESS)\|См. процедуру 019-042]] | QSK50 CM2150 MCRS | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
| Жгут проводов двигателя | [[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043]] | QSK50 CM2150 MCRS | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3164596 - male Framatome™ test lead, and Part Number 3164597 - female Framatome™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for an active fault code. | Fault Code 238 active or inactive with more than 1 count in the last 25 engine hours? |
> | STEP 2. | Check the sensors and circuits connected to the sensor supply 3 and return. |  |
> |  | **STEP 2A.** Inspect the engine crankshaft speed/position sensor and circuit connected to the sensor supply 3 and return | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the circuit response. | Fault Code 238 active? |
> | STEP 3. | Check the ECM. |  |
> |  | **STEP 3A.** Inspect the ECM and engine wiring harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the engine control module (ECM) response. | Fault Code 238 active? |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 4B.** Disable the fault code. | Fault Code inactive? |
>
> ### STEP 1. Check for an active fault code.
>
> #### STEP 1A. Check for an active fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 238 active or inactive with more than 1 count in the last 25 engine hours? **YES** | 2A |
> | Fault Code 238 active or inactive with more than 1 count in the last 25 engine hours? **NO** | Repair Complete |  |
>
> ### STEP 2. Check the sensors and circuits connected to the sensor supply 3 and return.
>
> #### STEP 2A. Inspect the engine crankshaft speed/position sensor connector and circuit connected to the sensor supply 3 and return.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine crankshaft speed/position sensor connector from the engine wiring harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine wiring harness and engine crankshaft speed/position sensor connector pins for the following: Loose connector corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection had been detected in the engine crankshaft speed/position sensor or wiring harness connector. Clean the connector and pins. Repair or replace the damaged section of the engine wiring harness. Refer to Procedure 019-043 in the Associated Procedures Table. Repair or replace the damaged engine crankshaft speed/position sensor. Refer to Procedure 019-042 in the Associated Procedure Table. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine crankshaft speed/position sensor connector from the engine wiring harness connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 238 active? **YES** | 3A |
> | Fault Code 238 active? **NORepair:** Replace the damaged engine crankshaft speed/position sensor. Refer to Procedure 019-042 in the Associated Procedure Table. | 4A |  |
>
> ### STEP 3. Check the ECM.
>
> #### STEP 3A. Inspect the ECM and engine wiring harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine wiring harness connector from the ECM 60-pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine wiring harness and ECM connector pin for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or the engine wiring harness. Clean the connector and pins. Refer to the circuit diagram or wiring diagram for all wiring harness interconnections. Repair or replace only the components and/or damaged section the engine wiring harness. Refer to Procedure 019-043 in the Associated Procedures Table. Refer to Procedure 019-031 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the ECM response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine wiring harness connector from the ECM 60-pins connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine wiring harness and ECM connector pin for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Fault Code 238 active? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |
> | Fault Code 238 active? **NORepair:** Troubleshoot each section of the wiring harnesses connected in series to determine which contains the short circuit to ground or pin-to-pin short circuit. Refer to the circuit diagram or wiring diagram for all wiring harness interconnections. Repair or replace the damaged section of the engine wiring harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |  |
>
> ### STEP 4. Check ECM calibration and clear fault codes.
>
> #### STEP 4A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 4B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. Refer to Procedure 019-032 in Section 19. | 4B |  |
>
> #### STEP 4B. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault Code inactive? **YES** | Repair complete |
> | Fault Code inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow your technical escalation process. | Escalate or call for assistance |  |
>
> ## Associated Procedures
>
> | Associated Procedures |  |  |  |
> |---|---|---|---|
> | Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
> | Engine Speed Sensor (ESS) | [[122-019-042 — Engine Speed Sensor (ESS)\|Refer to Procedure 019-042]] | QSK50 CM2150 MCRS | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
> | Engine Wiring Harness | [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043]] | QSK50 CM2150 MCRS | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
