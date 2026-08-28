---
aliases:
  - "Код 245 — цепь управления вентилятором — напряжение ниже нормы или замыкание на массу"
type: "Процедура"
doc: "122-t05-245"
title_en: "FAULT CODE 245 - Fan Control Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Код 245 — цепь управления вентилятором — напряжение ниже нормы или замыкание на массу"
modified: "2017-09-07"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-245.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-245.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 245 - Fan Control Circuit - Voltage Below Normal or Shorted to Low Source
**Код 245 — цепь управления вентилятором — напряжение ниже нормы или замыкание на массу**

> [!abstract] Процедура · `122-t05-245`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-09-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-245.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-245.pdf)

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
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить наличие активного кода неисправности. | Код 245 неисправности активен или неактивен, более 1 счета за последние 25 часов работы двигателя? |
| ШАГ 2. | Проверьте управление вентилятором и схему. |  |
|  | **STEP 2A.** Проверить контакты вентилятора и разъема. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте внутреннюю короткометражку в вентиляторном управлении. | В рамках спецификации сопротивления оригинального производителя оборудования (OEM)? |
|  | **STEP 2B-1.** Проверьте короткое замыкание вентилятора. | Больше 100 тысяч ом? |
| ШАГ 3. | Проверьте электропроводку ECM и OEM. |  |
|  | **STEP 3A.** Проверить контакты разъёма электропроводки ECM и OEM. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте короткое замыкание в проводной упряжке OEM. | Больше 100 тысяч ом? |
|  | **STEP 3C.** Проверьте короткое замыкание в электропроводке OEM или электропроводке двигателя. | Больше 100 тысяч ом? |
|  | **STEP 3D.** Проверить неактивный код ошибки. | Код 245 неактивен? |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 245 неактивен? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 245 неисправности активен или неактивен, более 1 счета за последние 25 часов работы двигателя? *Да | 2А |
| Код 245 неисправности активен или неактивен, более 1 счета за последние 25 часов работы двигателя? **НЕТ** | Используйте следующую процедуру для неактивного или прерывистого кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |  |

### ШАГ 2. Проверьте управление вентилятором и схему.

#### ШАГ 2A. Проверьте контакты управления вентилятором и разъемом.

| **Условия:** Выключите замок зажигания. Отсоедините разъем управления вентилятором от разъема OEM-проводов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты OEM-проводов, жгута проводов двигателя и разъема ECM для следующего: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]]. | Грязные или поврежденные контакты? **YESRepair:** В разъеме управления вентилятором или проводной жгуте проводов обнаружено поврежденное соединение. Очистите разъем и булавки. Замените поврежденный участок проводов ремнем или вентилятором управления. Проверьте все проводов, подключенные последовательно. См. схему или схему проводов для всех соединений проводов. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. Ремонт цепи управления вентилятором. См. процедуру 019-045 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте внутреннюю короткую в вентиляторном контроле.

| **Условия:** Выключите замок зажигания. Отсоедините разъем управления вентилятором от разъема OEM или разъёма жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте низкое внутреннее сопротивление вентилятора. Используйте мультиметр для измерения сопротивления между SIGNAL управления вентилятором и RETURN управления вентилятором (датчик возврата датчика 1) штифта разъема управления вентилятором. См. схему или схему проводов для идентификации контакта с разъемом. См. руководство по обслуживанию OEM для спецификаций сопротивления. Используйте следующую процедуру для идентификации контакта с разъемом.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]]. | В спецификации OEM-сопротивления? *Да | 2В-1-1 |
| В спецификации OEM-сопротивления? **NORepair:** Заменить вентиляторный пульт управления. Ремонт цепи управления вентилятором. См. процедуру 019-045 в разделе 19. | 4А |  |

#### ШАГ 2B-1. Проверьте короткое замыкание от пин-до-земли в управлении вентилятором.

| **Условия:** Выключите замок зажигания. Отсоедините разъем управления вентилятором от разъема OEM или разъёма жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Короткое замыкание на одном разъёме контакт-к-земле проверки: Измерьте сопротивление и проверьте короткое замыкание между контактом разъема SIGNAL и землей: См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для идентификации контакта с разъемом.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 2C |
| Больше 100 тысяч ом? **NORepair:** Заменить вентиляторный пульт управления. Ремонт цепи управления вентилятором. См. процедуру 019-045 в разделе 19. | 4А |  |

### ШАГ 3. Проверьте ECM, упряжку для проводов двигателя и упряжку для проводов OEM.

#### ШАГ 3A. Проверьте все контакты разъёма OEM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отключите проводку двигателя и проводку OEM-соединения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты проводов OEM и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **YESRepair:** В разъеме управления вентилятором или проводной жгуте проводов обнаружено поврежденное соединение. Замените поврежденный участок проводов ремнем или вентилятором управления. См. схему или схему проводов для всех соединений проводов. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. Ремонт цепи управления вентилятором. См. процедуру 019-045 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте, есть ли пин-топ в электропроводке OEM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема ECM. Отсоедините разъем управления вентилятором от разъема OEM или разъёма жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Короткое замыкание на одном разъёме контакт-к-земле проверки: Измерьте сопротивление и проверьте короткое замыкание между контактом сигнала управления вентилятором проводов электропроводки разъема ECM и заземлением блока двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для идентификации контакта с разъемом.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3C |
| Больше 100 тысяч ом? **NORepair:** Устранение неполадок во всех проводных упряжках, соединенных последовательно, чтобы определить, какая из них содержит штифт-на-землю. См. схему или схему проводов для всех соединений проводов. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 4А |  |

#### ШАГ 3C. Проверьте короткое замыкание контакта с контактом в OEM-проводнике или упряжке для проводов двигателя.

| **Условия:** Замок зажигания отключите разъем электропроводки двигателя от разъема ECM Отключите разъем управления вентилятором от разъема OEM или разъема электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Короткое замыкание на одном разъёме контакт-к-контакту проверка: Измерьте сопротивление и проверьте короткое замыкание между контактом сигнала управления вентилятором проводов электромобиля разъема ECM и всеми другими штифтами в разъеме. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для идентификации контакта с разъемом.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3D |
| Больше 100 тысяч ом? **NORepair:** Устранение неполадок во всех проводных упряжках, соединенных последовательно, для определения того, какая из них содержит короткое контактное соединение. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 4А |  |

#### ШАГ 3D. Проверьте неактивный код ошибки.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 245 неактивен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | 4А |
| Код 245 неактивен? Заменить ЭКМ. См. процедуру 019-031 в разделе 19. | 4А |  |

### ШАГ 4. Сбросьте коды неисправностей.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Отключите соленоид управления вентилятором от OEM или жгута проводов двигателя. Выключите замок зажигания. Подключите соленоид управления вентилятором к OEM или жгуту проводов двигателя. Включите зажигание. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кодов неисправностей. | Код 245 неактивен? *Да | 4B |
| Код 245 неактивен? **NORepair: **Ссылка на Руководство по ремонту, Системы управления базовыми панелями Marine C CommandTM, Бюллетень [[4021587 — C Command Panel System Marine Master Repair Manual\|4021587]] или Руководство по ремонту Master, Панельная система Marine C Command EliteTM и C Command Elite PlusTM, Бюллетень [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual\|4021617]]. | Соответствующие шаги по устранению неполадок |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **Секретарь:**Проверить, что все шаги были выполнены. Если все шаги выполнены, то следуйте процессу технической эскалации. | Эскалация или призыв к помощи |  |


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
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for an active fault code. | Fault Code 245 active or inactive with more than 1 count in the last 25 engine hours? |
> | STEP 2. | Check the fan control and circuit. |  |
> |  | **STEP 2A.** Inspect the fan control and connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check for an internal short in the fan control. | Within the original equipment manufacturer (OEM) resistance specification? |
> |  | **STEP 2B-1.** Check for a pin-to-ground short circuit in the fan control. | Greater than 100k ohms? |
> | STEP 3. | Check the ECM and OEM harness. |  |
> |  | **STEP 3A.** Inspect the ECM and OEM harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check for a pin-to-ground short circuit in the OEM harness. | Greater than 100k ohms? |
> |  | **STEP 3C.** Check for a pin-to-pin short circuit in the OEM harness or engine harness. | Greater than 100k ohms? |
> |  | **STEP 3D.** Check for an inactive fault code. | Fault Code 245 inactive? |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 245 inactive? |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for an active fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 245 active or inactive with more than 1 count in the last 25 engine hours? **YES** | 2A |
> | Fault Code 245 active or inactive with more than 1 count in the last 25 engine hours? **NO** | Use the following procedure for inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |
>
> ### STEP 2. Check the fan control and circuit.
>
> #### STEP 2A. Inspect the fan control and connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the fan control connector from the OEM harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness, engine harness, and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the fan control or harness connector. Clean the connector and pins. Replace the damaged section of the harness or fan control. Check all harnesses connected in series. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Repair the fan control circuit. Refer to Procedure 019-045 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check for an internal short in the fan control.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the fan control connector from the OEM or engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for low internal resistance of the fan control. Use a multimeter to measure the resistance between the fan control SIGNAL and fan control RETURN (sensor return 1) pin of the fan control connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Refer to the OEM service manual for resistance specifications. Use the following procedure for connector pin identification. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19]]. | Within the OEM resistance specification? **YES** | 2B-1 |
> | Within the OEM resistance specification? **NORepair:** Replace the fan control. Repair the fan control circuit. Refer to Procedure 019-045 in Section 19. | 4A |  |
>
> #### STEP 2B-1. Check for a pin-to-ground short circuit in the fan control.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the fan control connector from the OEM or engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Short circuit on one connector pin-to-ground check: Measure the resistance and check for a short circuit between the fan control SIGNAL connector pin and ground: Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for connector pin identification. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 2C |
> | Greater than 100k ohms? **NORepair:** Replace the fan control. Repair the fan control circuit. Refer to Procedure 019-045 in Section 19. | 4A |  |
>
> ### STEP 3. Check the ECM, engine harness, and OEM harness.
>
> #### STEP 3A. Inspect all OEM and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness and OEM harness connections. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the fan control or harness connector. Replace the damaged section of the harness or fan control. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Repair the fan control circuit. Refer to Procedure 019-045 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check for a pin-to-ground in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM connector. Disconnect the fan control connector from the OEM or engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Short circuit on one connector pin-to-ground check: Measure the resistance and check for a short circuit between the fan control SIGNAL pin of the engine harness ECM connector and engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for connector pin identification. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3C |
> | Greater than 100k ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the pin-to-ground short. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |
>
> #### STEP 3C. Check for a pin-to-pin short circuit in the OEM harness or engine harness.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the engine harness connector from the ECM connector Disconnect the fan control connector from the OEM or engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Short circuit on one connector pin-to-pin check: Measure the resistance and check for a short circuit between the fan control SIGNAL pin of the engine harness ECM connector and all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for connector pin identification. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3D |
> | Greater than 100k ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the pin-to-pin short. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |
>
> #### STEP 3D. Check for an inactive fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 245 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
> | Fault Code 245 inactive? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |  |
>
> ### STEP 4. Clear the fault codes.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Disconnect the fan control solenoid from the OEM or engine harness. Turn the keyswitch OFF. Connect the fan control solenoid to the OEM or engine harness. Turn keyswitch ON. Use INSITE™ electronic service tool to verify that the fault codes are inactive. | Fault Code 245 inactive? **YES** | 4B |
> | Fault Code 245 inactive? **NORepair:** Reference the Master Repair Manual, Marine C Command™ Basic Panel Manual Systems, Bulletin [[4021587 — C Command Panel System Marine Master Repair Manual\|4021587]], or the Master Repair Manual, Marine C Command Elite™ and C Command Elite Plus™ Panel System, Bulletin [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual\|4021617]]. | Appropriate Troubleshooting Steps |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance |  |
