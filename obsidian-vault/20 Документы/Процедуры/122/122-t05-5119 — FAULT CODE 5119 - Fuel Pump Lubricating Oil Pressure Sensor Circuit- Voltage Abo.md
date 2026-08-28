---
aliases:
  - "Код 5119 — цепь датчика давления масла топливного насоса — напряжение выше нормы"
type: "Процедура"
doc: "122-t05-5119"
title_en: "FAULT CODE 5119 - Fuel Pump Lubricating Oil Pressure Sensor Circuit- Voltage Above Normal or Shorted to High Source"
title_ru: "Код 5119 — цепь датчика давления масла топливного насоса — напряжение выше нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-5119.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-5119.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 5119 - Fuel Pump Lubricating Oil Pressure Sensor Circuit- Voltage Above Normal or Shorted to High Source
**Код 5119 — цепь датчика давления масла топливного насоса — напряжение выше нормы**

> [!abstract] Процедура · `122-t05-5119`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2020-05-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-5119.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-5119.pdf)

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
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3164596 — штыревой пробный щуп FramatomeTM и номер детали 3822917 — пробный щуп типа сокет DeutschTM/AmpTM/Metri-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить коды неисправностей датчиков. | Код ошибки 2185 активен? |
| ШАГ 2. | Проверьте датчик давления моторного масла и схему топливного насоса. |  |
|  | **ШАГ 2А.** Осмотрите штифты и разъемы на предмет повреждения. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте напряжение питания датчика и схему возврата. | 4.75-5.25 VDC? |
|  | **STEP 2C.** Проверьте реакцию цепи. Контроль схемы датчика давления моторного масла. | Код 5121 активен? |
| ШАГ 3. | Контроль схемы датчика давления моторного масла. |  |
|  | **STEP 3A.** Датчик давления моторного масла на топливных насосах с открытым контуром. | Сопротивление менее 10 Ом? |
|  | **STEP 3B.** Топливный насос моторного масла датчик давления цепь зажима для проверки зажима. | Сопротивление менее 100k ом? |
| ШАГ 4. | Проверьте калибровку ECM и четкие коды ошибок. |  |
|  | **STEP 4A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 4B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте коды неисправностей датчика.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте коды неисправностей датчика. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 2185 активен? *Да | Перейдите к соответствующему дереву устранения неисправностей кода ошибки. |
| Код ошибки 2185 активен? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте датчик давления моторного масла и схему топливного насоса.

#### ШАГ 2A. Осмотрите датчик давления моторного масла топливного насоса и контакты разъема для проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика давления моторного масла топливного насоса от разъема ремня электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите штифты и разъемы на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем или разбитые штифты Отталкивание или разъем разъема Разъема разъема или разъема или разъема или разъема оболочки Разбитая Запирающаяся вкладка Разъема разъема. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361]]В разделе 19. | Грязные или поврежденные контакты? *** Ремонт:** Ремонт или замена только тех компонентов, которые были обнаружены за пределами указанных пределов. Замените датчик давления моторного масла топливного насоса. См. процедуру 019-679 в разделе 19. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте напряжение питания датчика и обратную цепь.

| **Условия:** Выключите замок зажигания. Отсоедините разъем датчика давления моторного масла топливного насоса от разъема ремня электропроводки двигателя. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение питания и обратную цепь. Измерьте напряжение от давления масла топливного насоса, 5-вольтового контакта подачи к обратному контакту давления топливного насоса на разъеме датчика проводов двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов использования мультиметра.[[99-019-359 — Multimeter Usage\|См. процедуру 019-359 в разделе 19.]] | 4,75-5,25-ВДЦ? *Да | 2C |
| 4,75-5,52-ВДЦ? **НЕТ** | 3А |  |

#### ШАГ 2C. Проверьте отклик цепи.

| **Условия:** Замок зажигания отключите разъем датчика давления моторного масла топливного насоса от разъема жгутов проводов двигателя. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте правильность ответа на цепь через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 5121 активен? **Ремонт:** Поврежденный датчик давления моторного масла топливного насоса обнаружен. Замените датчик давления моторного масла топливного насоса. См. процедуру 019-679 в разделе 19. | 4А |
| Код 5121 активен? **НЕТ** | 3А |  |

### ШАГ 3. Контроль схемы датчика давления моторного масла.

#### ШАГ 3A. Датчик давления моторного масла на топливных насосах с открытым контуром.

| **Условия:** Замок зажигания отключите датчик давления моторного масла топливного насоса от электропроводки двигателя. Отсоедините разъем жгута проводов двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление между датчиком давления моторного масла топливного насоса, контактирующим с сигналом на разъеме датчика давления моторного масла топливного насоса и датчиком давления моторного масла топливного насоса, контактирующим с сигналом на разъеме ECM электропроводки двигателя. Измерить сопротивление между датчиком давления моторного масла топливного насоса обратного контакта на разъёме датчика давления моторного масла топливного насоса и датчиком давления моторного масла топливного насоса обратного контакта на разъёме электропроводки двигателя ECM. | Сопротивление менее 10 Ом? *Да | 3B |
| Сопротивление менее 10 Ом? **NORepair:** Обнаружена неисправная проводка двигателя. Ремонт или замена ремня электропроводки двигателя.[[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043]]В разделе 19. | 4А |  |

#### ШАГ 3B. Топливный насос моторного масла датчик давления цепь пин-код для проверки пин-код.

| **Условия:** Замок зажигания отключите датчик давления моторного масла топливного насоса от электропроводки двигателя. Отсоедините разъем жгута проводов двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление между датчиком давления моторного масла топливного насоса, контактирующим с сигналом на разъеме ECM электропроводки двигателя и всеми другими штифтами на разъеме ECM электропроводки двигателя. | Сопротивление менее 100k ом? **Ремонт:** Неисправная проводка двигателя была обнаружена.[[122-019-043 — Engine Wiring Harness\|См. процедуру 019-043]]В разделе 19. | 4А |
| Сопротивление менее 100k ом? **НЕТ** | 4А |  |

### ШАГ 4. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 4A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и его пересмотр с калибровочным пересмотром, перечисленным в истории калибровочных изменений ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички данных в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту ревизию или выше? *Да | 4B |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту редакцию или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032]]В разделе 19. | 4B |  |

#### ШАГ 4B. Отключите код неисправности.

| **Условия:** Подключить все компоненты Подключить электронный сервисный инструмент INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да | Ремонт завершён. |
| Код неактивен? **Секретарь:**Проверить, что все шаги были выполнены. Если все шаги выполнены, то следуйте процессу технической эскалации. | Эскалация или призыв к помощи. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3164596 - male Framatome™ test lead and Part Number 3822917 - female Deutsch™/Amp™/Metri-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for sensor supply fault codes. | Fault Code 2185 active? |
> | STEP 2. | Check the fuel pump lubricating oil pressure sensor and circuit. |  |
> |  | **STEP 2A.** Inspect the pins and connectors for damage. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the sensor supply voltage and return circuit. | 4.75 to 5.25 VDC? |
> |  | **STEP 2C.** Check the circuit response. Fuel pump lubricating oil pressure sensor circuit check. | Fault Code 5121 active? |
> | STEP 3. | Fuel pump lubricating oil pressure sensor circuit check. |  |
> |  | **STEP 3A.** Fuel pump lubricating oil pressure sensor open circuit check. | Resistance less than 10 ohms? |
> |  | **STEP 3B.** Fuel pump lubricating oil pressure sensor circuit pin to pin check. | Resistance less than 100k ohms? |
> | STEP 4. | Check ECM calibraion and clear fault codes. |  |
> |  | **STEP 4A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 4B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for sensor supply fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for sensor supply fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2185 active? **YES** | Go to appropriate fault code troubleshooting tree. |
> | Fault Code 2185 active? **NO** | 2A |  |
>
> ### STEP 2. Check the fuel pump lubricating oil pressure sensor and circuit.
>
> #### STEP 2A. Inspect the fuel pump lubricating oil pressure sensor and engine wiring harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the fuel pump lubricating oil pressure sensor connector from the engine wiring harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the pins and connectors for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Dirt or debris in or on the connector pins Wire insulation damage Missing or damaged connector seals Connector or shell broken Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361]] in Section 19. | Dirty or damaged pins? **YESRepair:** Repair or replace only the components that were found to be out of specification. Replace the fuel pump lubricating oil pressure sensor. Refer to Procedure 019-679 in Section 19. Repair or replace the engine wiring harness. Refer to Procedure 019-043 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the sensor supply voltage and return circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the fuel pump lubricating oil pressure sensor connector from the engine wiring harness connector. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply voltage and return circuit. Measure the voltage from the fuel pump oil pressure, 5-volt SUPPLY pin to the fuel pump pressure RETURN pin at the sensor connector of the engine wiring harness. See the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | 4.75 to 5.25-VDC? **YES** | 2C |
> | 4.75 to 5.52-VDC? **NO** | 3A |  |
>
> #### STEP 2C. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the fuel pump lubricating oil pressure sensor connector from the engine wiring harness connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 5121 active? **YESRepair:** A damaged fuel pump lubricating oil pressure sensor has been detected. Replace the fuel pump lubricating oil pressure sensor. Refer to Procedure 019-679 in Section 19. | 4A |
> | Fault Code 5121 active? **NO** | 3A |  |
>
> ### STEP 3. Fuel pump lubricating oil pressure sensor circuit check.
>
> #### STEP 3A. Fuel pump lubricating oil pressure sensor open circuit check.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the fuel pump lubricating oil pressure sensor from the engine wiring harness. Disconnect the engine wiring harness connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between the fuel pump lubricating oil pressure sensor SIGNAL pin at the fuel pump lubricating oil pressure sensor wiring harness connector and the fuel pump lubricating oil pressure sensor SIGNAL pin at the engine wiring harness ECM connector. Measure the resistance between the fuel pump lubricating oil pressure sensor RETURN pin at the fuel pump lubricating oil pressure sensor wiring harness connector and the fuel pump lubricating oil pressure sensor RETURN pin at the engine wiring harness ECM connector. | Resistance less than 10 ohms? **YES** | 3B |
> | Resistance less than 10 ohms? **NORepair:** A malfunctioning engine wiring harness has been detected. Repair or replace the engine wiring harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043]] in Section 19. | 4A |  |
>
> #### STEP 3B. Fuel pump lubricating oil pressure sensor circuit pin to pin check.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the fuel pump lubricating oil pressure sensor from the engine wiring harness. Disconnect the engine wiring harness connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between the fuel pump lubricating oil pressure sensor SIGNAL pin at the engine wiring harness ECM connector and all other pins at the engine wiring harness ECM connector. | Resistance less than 100k ohms? **YESRepair:** A malfunctioning engine wiring harness has been detected. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043]] in Section 19. | 4A |
> | Resistance less than 100k ohms? **NO** | 4A |  |
>
> ### STEP 4. Check the ECM calibration and clear fault codes.
>
> #### STEP 4A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision in the ECM to the calibration revision listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 4B |
> | If a calibrtion update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032]] in Section 19. | 4B |  |
>
> #### STEP 4B. Disable the fault code.
>
> | **Conditions:** Connect all components Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
> | Fault code inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance. |  |
