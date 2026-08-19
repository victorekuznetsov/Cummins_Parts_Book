---
aliases:
  - "Код 254 — цепь драйвера клапана отсечки топлива — напряжение ниже нормы"
type: "Процедура"
doc: "82-t05-254"
title_en: "FAULT CODE 254 - Engine Fuel Shutoff Valve Driver Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Код 254 — цепь драйвера клапана отсечки топлива — напряжение ниже нормы"
modified: "2019-05-31"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-254.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-t05-254.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# FAULT CODE 254 - Engine Fuel Shutoff Valve Driver Circuit - Voltage Below Normal or Shorted to Low Source
**Код 254 — цепь драйвера клапана отсечки топлива — напряжение ниже нормы**

> [!abstract] Процедура · `82-t05-254`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-05-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-254.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-t05-254.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
> Чтобы не повредить новый блок управления двигателем (ЭБУ), перед его заменой разберитесь со всеми остальными активными кодами неисправностей.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 - пробный щуп типа вилки DeutschTM/AMPTM/Metri-PackTM и номер детали 3822917 - пробный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте, не работает ли соленоид. |  |
|  | **ШАГ 1А.** Проверьте наличие дополнительных проводов на затворе соленоидного поста. | Дополнительные провода? |
|  | **ШАГ 1В.** Проверка на коррозию на соленоидном посту. | Коррозия найдена? |
|  | **STEP 1C** Проверить напряжение питания на соленоиде отключения топлива. | Больше, чем положительный +6 VDC? |
|  | **STEP 1C-1.** Проверьте электропроводку привода и контакты разъема ECM. | Грязные или поврежденные контакты? |
|  | **STEP 1C-2.** Проверьте наличие открытой цепи. | Менее 10 Ом? |
|  | **STEP 1C-3.** Проверить короткое замыкание от контакта к контакту. | Больше 100 тысяч ом? |
|  | **STEP 1C-4.** Измерить напряжение от ECM. | Больше, чем положительный +6 VDC? |
|  | **STEP 1D.** Проверьте сопротивление соленоидов отключения топлива. | От 1 до 5 Ом для соленоидов 6-VDC, от 6 до 15 Ом для соленоидов 12-VDC, от 24 до 50 Ом для соленоидов 24-VDC, от 42 до 80 Ом для соленоидов 32-VDC, от 46 до 87 Ом для соленоидов 36-VDC, от 92 до 145 Ом для соленоидов 48-VDC, от 315 до 375 Ом для соленоидов 74-VDC, от 645 до 735 Ом для соленоидов 115-VAC? |
| ШАГ 2. | Проверьте калибровку ECM и четкие коды неисправностей. |  |
|  | **STEP 2A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 2B.** Выключите код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте, не работает ли соленоид.

#### ШАГ 1A. Проверьте наличие дополнительных проводов на затворе топлива.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте дополнительные провода. Проверьте наличие дополнительных проводов на топливе, выключенном соленоидным столбом. | Дополнительные провода? *Да** | 1В |
| Дополнительные провода? **NORepair:** Удалите дополнительные провода и подключитесь к положительному источнику питания +12 VDC. | 2А |  |

#### ШАГ 1B. Проверьте на коррозию на соленоидном столбе.

| **Условия:** Выключите замок зажигания. Отсоедините провод управления отключением топлива от соленоида отключения топлива. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте на коррозию. Проверьте на коррозию на соленоидном столбе. | Коррозия найдена? *Да** | 1С |
| Коррозия найдена? **NORepair:** Очистить соленоидный пост и проводной терминал. См. процедуру 019-050 в Таблице ассоциированных процедур. | 2А |  |

#### ШАГ 1C. Проверьте напряжение питания на соленоиде отключения топлива.

| **Условия:** Отсоединить электропроводку привода от затвора соленоида. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте напряжение питания на соленоиде отключения топлива. Измерьте напряжение от разъемов проводов управления отключения топлива на стороне проводов жгута проводов до заземления блока двигателя. | Больше, чем положительный +6-VDC? *Да** | 1D |
| Больше, чем положительный +6-VDC? ** НЕТ** | 1С-1-1 |  |

#### ШАГ 1C-1. Проверьте электропроводку привода и контакты разъема ECM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем электропроводки привода от ECM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Осмотрите контактные линзы электропроводки привода и разъёма ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? *Да** | 1С-2 |
| Грязные или поврежденные контакты? **NORepair:** Ремонтировать или заменить поврежденные контакты. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. Заменить ECM. См. процедуру 019-031 в Таблице ассоциированных процедур. | 1D |  |

#### ШАГ 1C-2. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку привода от затвора топлива соленоида. Отсоедините разъем электропроводки привода от ECM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте наличие открытой цепи на контакте 33. Измерить сопротивление от контакта 33 привода провода жгута к топливу выключателя управляющего провода. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да** | 1С-3 |
| Менее 10 Ом? **NORepair:** Ремонтировать или заменить электропроводку двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 2А |  |

#### ШАГ 1C-3. Проверьте короткий сиркуит от контакта к контакту.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку привода от затвора топлива соленоида. Отсоедините разъем электропроводки привода от ECM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте короткое замыкание от контакта к контакту. Измерьте сопротивление от контакта 33 проводов привода разъёма ремня со всеми другими штифтами в разъёме. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да** | 1С-4 |
| Больше 100 тысяч ом? **NORepair:** Ремонтировать или заменить электропроводку двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 2А |  |

#### ШАГ 1C-4. Измерьте напряжение от ECM.

| **Условия:** Отсоединить от ECM разъем электропроводки привода. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте напряжение из ECM. Измерьте напряжение на ECM от контакта 33 порта разъёма ремня привода к заземлению блока двигателя. | Больше, чем положительный +6-VDC? *** Ремонт:** Ремонт или замена ремня электропроводки двигателя. Ремонт ремня электропроводки двигателя. См. процедуру 019-204 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 2А |
| Больше, чем положительный +6-VDC? **Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 2А |  |

#### ШАГ 1D. Проверьте сопротивление соленоидов отключения топлива.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку привода от затвора топлива соленоида. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сопротивление соленоидов отключения топлива. Измерьте сопротивление от отключения топлива соленоида к заземлению блока двигателя. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | От 1 до 5 Ом для соленоидов 6-VDC, от 6 до 15 Ом для соленоидов 12-VDC, от 24 до 50 Ом для соленоидов 24-VDC, от 42 до 80 Ом для соленоидов 32-VDC, от 46 до 87 Ом для соленоидов 36-VDC, от 92 до 145 Ом для соленоидов 48-VDC, от 315 до 375 Ом для соленоидов 74-VDC, от 645 до 735 Ом для соленоидов 115-VAC? *Да** | 2А |
| От 1 до 5 Ом для соленоидов 6-VDC, от 6 до 15 Ом для соленоидов 12-VDC, от 24 до 50 Ом для соленоидов 24-VDC, от 42 до 80 Ом для соленоидов 32-VDC, от 46 до 87 Ом для соленоидов 36-VDC, от 92 до 145 Ом для соленоидов 48-VDC, от 315 до 375 Ом для соленоидов 74-VDC, от 645 до 735 Ом для соленоидов 115-VAC? **NORepair:** Заменить выключаемый соленоид топливом. См. процедуру 019-050 в Таблице ассоциированных процедур. | 2А |  |

### ШАГ 2. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 2A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: ** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички данных в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да** | 2В |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]] | 2В |  |

#### ШАГ 2B. Отключите код неисправности.

| **Условия: ** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да** | Ремонт завершён. |
| Код неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

## Связанные процедуры

| Связанные процедуры |  |  |  |
|---|---|---|---|
| Название процедуры | Процедурный номер | Модельный сервис | Номер бюллетеня |
| Электронный блок управления двигателем | [[82-019-031 — Engine Control Module\|См. процедуру 019-031]] | Двигатели ISM и QSM11 | 3666266 |
| Жгут проводов двигателя | [[82-019-043-tr — Engine Wiring Harness\|См. процедуру 019-043]] | Двигатели ISM и QSM11 | 3666266 |
| Клапан отсечки топлива | [[82-019-050 — Fuel Shutoff Valve\|См. процедуру 019-050]] | Двигатели ISM и QSM11 | 3666266 |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fuel shutoff solenoid. |  |
> |  | **STEP 1A.** Check for extra wires on the fuel shutoff solenoid post. | Extra wires? |
> |  | **STEP 1B.** Check for corrosion on the solenoid post. | Corrosion found? |
> |  | **STEP 1C.** Check the supply voltage at the fuel shutoff solenoid. | Greater than positive +6 VDC? |
> |  | **STEP 1C-1.** Check the actuator harness and the ECM connector pins. | Dirty or damaged pins? |
> |  | **STEP 1C-2.** Check for an open circuit. | Less than 10 ohms? |
> |  | **STEP 1C-3.** Check for a short circuit from pin-to-pin. | Greater than 100k ohms? |
> |  | **STEP 1C-4.** Measure the voltage from the ECM. | Greater than positive +6 VDC? |
> |  | **STEP 1D.** Check the fuel shutoff solenoid resistance. | 1 to 5 ohms for 6-VDC solenoids, 6 to 15 ohms for 12-VDC solenoids, 24 to 50 ohms for 24-VDC solenoids, 42 to 80 ohms for 32-VDC solenoids, 46 to 87 ohms for 36-VDC solenoids, 92 to 145 ohms for 48-VDC solenoids, 315 to 375 ohms for 74-VDC solenoids, 645 to 735 ohms for 115-VAC solenoids? |
> | STEP 2. | Check the ECM calibration and clear fault codes. |  |
> |  | **STEP 2A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 2B.** Diable the fault code. | Fault code inactive? |
>
> ### STEP 1. Check the fuel shutoff solenoid.
>
> #### STEP 1A. Check for extra wires on the fuel shutoff solenoid post.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for extra wires. Check for extra wires on the fuel shut off solenoid post. | Extra wires? **YES** | 1B |
> | Extra wires? **NORepair:** Remove extra wires and connect to positive +12 VDC supply. | 2A |  |
>
> #### STEP 1B. Check for corrosion on the solenoid post.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the fuel shutoff control wire from the fuel shutoff solenoid. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for corrosion. Check for corrosion on the solenoid post. | Corrosion found? **YES** | 1C |
> | Corrosion found? **NORepair:** Clean the solenoid post and wiring terminal. Refer to Procedure 019-050 in the Associated Procedures Table. | 2A |  |
>
> #### STEP 1C. Check the supply voltage at the fuel shutoff solenoid.
>
> | **Conditions:** Disconnect the actuator harness from the fuel shutoff solenoid. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply voltage at the fuel shutoff solenoid. Measure the voltage from the fuel shutoff control wire connectors on the harness side to engine block ground. | Greater than positive +6-VDC? **YES** | 1D |
> | Greater than positive +6-VDC? **NO** | 1C-1 |  |
>
> #### STEP 1C-1. Check the actuator harness and the ECM connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the actuator harness connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the actuator harness and the ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YES** | 1C-2 |
> | Dirty or damaged pins? **NORepair:** Repair or replace the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 1D |  |
>
> #### STEP 1C-2. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the actuator harness from the fuel shutoff solenoid. Disconnect the actuator harness connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit at pin 33. Measure the resistance from pin 33 of the actuator harness to the fuel shutoff control wire. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 1C-3 |
> | Less than 10 ohms? **NORepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 2A |  |
>
> #### STEP 1C-3. Check for a short sircuit from pin-to-pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the actuator harness from the fuel shutoff solenoid. Disconnect the actuator harness connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin-to-pin. Measure the resistance from pin 33 of the actuator harness connector to all other pins in the connector. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 1C-4 |
> | Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 2A |  |
>
> #### STEP 1C-4. Measure the voltage from the ECM.
>
> | **Conditions:** Disconnect the actuator harness connector from the ECM. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage out of the ECM. Measure the voltage at the ECM from pin 33 of the actuator harness connector port to engine block ground. | Greater than positive +6-VDC? **YESRepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 2A |
> | Greater than positive +6-VDC? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 2A |  |
>
> #### STEP 1D. Check the fuel shutoff solenoid resistance.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the actuator harness from the fuel shutoff solenoid. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel shutoff solenoid resistance. Measure the resistance from the fuel shutoff solenoid to engine block ground. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | 1 to 5 ohms for 6-VDC solenoids, 6 to 15 ohms for 12-VDC solenoids, 24 to 50 ohms for 24-VDC solenoids, 42 to 80 ohms for 32-VDC solenoids, 46 to 87 ohms for 36-VDC solenoids, 92 to 145 ohms for 48-VDC solenoids, 315 to 375 ohms for 74-VDC solenoids, 645 to 735 ohms for 115-VAC solenoids? **YES** | 2A |
> | 1 to 5 ohms for 6-VDC solenoids, 6 to 15 ohms for 12-VDC solenoids, 24 to 50 ohms for 24-VDC solenoids, 42 to 80 ohms for 32-VDC solenoids, 46 to 87 ohms for 36-VDC solenoids, 92 to 145 ohms for 48-VDC solenoids, 315 to 375 ohms for 74-VDC solenoids, 645 to 735 ohms for 115-VAC solenoids? **NORepair:** Replace the fuel shutoff solenoid. Refer to Procedure 019-050 in the Associated Procedures Table. | 2A |  |
>
> ### STEP 2. Check ECM calibration and clear fault codes.
>
> #### STEP 2A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 2B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 2B |  |
>
> #### STEP 2B. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
> | Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> ## Associated Procedures
>
> | Associated Procedures |  |  |  |
> |---|---|---|---|
> | Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
> | Engine Control Module | [[82-019-031 — Engine Control Module\|Refer to Procedure 019-031]] | ISM and QSM11 Engines | 3666266 |
> | Engine Wiring Harness | [[82-019-043-tr — Engine Wiring Harness\|Refer to Procedure 019-043]] | ISM and QSM11 Engines | 3666266 |
> | Fuel Shutoff Valve | [[82-019-050 — Fuel Shutoff Valve\|Refer to Procedure 019-050]] | ISM and QSM11 Engines | 3666266 |
