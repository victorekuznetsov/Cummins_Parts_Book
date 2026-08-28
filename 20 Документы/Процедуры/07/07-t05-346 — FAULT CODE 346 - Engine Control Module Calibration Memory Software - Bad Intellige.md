---
aliases:
  - "Код 346 — ПО калибровочной памяти ЭБУ — неисправное устройство"
type: "Процедура"
doc: "07-t05-346"
title_en: "FAULT CODE 346 - Engine Control Module Calibration Memory Software - Bad Intelligent Device or Component"
title_ru: "Код 346 — ПО калибровочной памяти ЭБУ — неисправное устройство"
modified: "2016-10-07"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-t05-346.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-t05-346.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# FAULT CODE 346 - Engine Control Module Calibration Memory Software - Bad Intelligent Device or Component
**Код 346 — ПО калибровочной памяти ЭБУ — неисправное устройство**

> [!abstract] Процедура · `07-t05-346`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-10-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-t05-346.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-t05-346.pdf)

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

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Код 346 сбоя активен или неактивен, с более чем одним счетчиком, зарегистрированным за последние 25 часов работы двигателя? |
| ШАГ 2. | Проверьте ECM и электропроводку двигателя. |  |
|  | **STEP 2A.** Проверить упряжку электропроводки двигателя и разъемы ECM. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте наличие открытой цепи в непереключенных цепях питания аккумулятора. | По крайней мере (+) 10 VDC \[(+) 20 VDC для 24-вольтовой системы\]? |
|  | **STEP 2C.** Проверьте наличие открытой цепи в непереключенных цепях питания аккумулятора. | По крайней мере (+) 10 VDC \[(+) 20 VDC для 24-вольтовой системы\]? |
| ШАГ 3. | Проверьте батареи и предохранители. |  |
|  | **СТЭП 3А.** Проверить аккумуляторы. | Соединения плотные и без коррозии? |
|  | **ШАГ 3В.** Проверьте напряжение батареи. | Напряжение батареи приемлемо в нормальных и кривошипных условиях? |
|  | **STEP 3B-1.** Убедитесь, что предохранители производителя оригинального оборудования установлены правильно. | Правильно установлен предохранитель? |
|  | **ШАГ 3В-2.** Проверьте, не взорваны ли предохранители. | Взорван предохранитель? |
| ШАГ 4. | Проверьте OEM-систему электропроводки и 4-контактный разъем интерфейса питания ECM. |  |
|  | **STEP 4A.** Проверить электропроводку жгута и 4 контактов разъема силового интерфейса ECM. | Грязные или поврежденные контакты? |
|  | **STEP 4B.** Проверьте наличие открытой цепи в цепях питания аккумулятора. | По крайней мере (+) 10 VDC \[(+) 20 VDC для 24-вольтовой системы\]? |
|  | **STEP 4C.** Проверьте наличие открытой цепи в цепях питания аккумулятора. | По крайней мере (+) 10 VDC \[(+) 20 VDC для 24-вольтовой системы\]? |
| ШАГ 5. | Проверьте калибровку ECM и четкие коды неисправностей. |  |
|  | **STEP 5A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 5B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 346 сбоя активен или неактивен, с более чем одним счетчиком, зарегистрированным за последние 25 часов работы двигателя? *Да | 2А |
| Код 346 сбоя активен или неактивен, с более чем одним счетчиком, зарегистрированным за последние 25 часов работы двигателя? **НЕТ** | Используйте следующую процедуру для неактивного или прерывистого кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]]. |  |

### ШАГ 2. Проверьте ECM и электропроводку двигателя.

#### ШАГ 2A. Проверьте разъемы ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отсоедините жгут проводов двигателя от 4-контактного разъема интерфейса питания ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты электропроводки двигателя и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или разъема изоляции Поврежденный разъем блокировки вкладки. Используйте следующие методы для общего осмотра.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? В разъеме ECM или разъеме ремня электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. Заменить поврежденный участок проводов жгутом. Ссылка на схему или схему проводов для всех соединений проводов жгута. Замените проводку упряжкой. См. 019-043 в Таблице ассоциированных процедур. | 5а |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте наличие открытой цепи в непереключенных цепях питания батареи.

| **Условия:** Замок зажигания отключите от электропроводки двигателя электроузел от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение между непереключенными контактами напряжения батареи SUPPLY и контактами RETURN на разъеме 50-контактной электропроводки двигателя ECM. Ссылка на схему схемы или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов использования мультиметра. См. процедуру 019-359 в разделе 19. | По крайней мере (+) 10 VDC \[(+) 20 VDC для 24-вольтовой системы\]?  Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 5а |
| По крайней мере (+) 10 VDC \[(+) 20 VDC для 24-вольтовой системы\]? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте наличие открытой цепи в непереключенных цепях питания батареи.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку двигателя от ECM. Отсоедините электропроводку двигателя от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение между непереключенными контактами напряжения батареи SUPPLY на разъёме 50-контактной проводов двигателя и блоке двигателя. Ссылка на схему схемы или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов использования мультиметра. См. процедуру 019-359 в разделе 19. | По крайней мере (+) 10 VDC \[(+) 20 VDC для 24-вольтовой системы\]? **Ремонт:** В цепи возврата напряжения батареи обнаружена открытая или высоковольтная цепь. Устранение неполадок в проводах двигателя и всех межсоединений для неисправности. По мере необходимости ремонтировать или заменять поврежденный компонент. | 5а |
| По крайней мере (+) 10 VDC \[(+) 20 VDC для 24-вольтовой системы\]? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте батареи и предохранители.

#### ШАГ 3A. Проверьте батареи и предохранители.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соединения терминала батареи. | Соединения плотные и без коррозии? *Да | 3B |
| Соединения плотные и без коррозии? **NORepair:** Затянуть свободные соединения и очистить терминалы. См. информацию об услугах производителя оборудования. | 5а |  |

#### ШАГ 3B. Проверьте напряжение батареи.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Поместите положительный (+) щуп мультиметра на положительный вывод батареи и прикоснитесь к отрицательному (-) датчику к отрицательному выводу батареи при попытке запустить двигатель. | Напряжение батареи приемлемо в нормальных и кривошипных условиях? *Да | 3В-1-1 |
| Напряжение батареи приемлемо в нормальных и кривошипных условиях? **NORepair:** Зарядить или заменить аккумулятор. См. информацию об услугах производителя оборудования. | 5а |  |

#### ШАГ 3B-1. Убедитесь, что предохранители OEM установлены правильно.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что предохранители OEM 10A между аккумулятором и 4-контактным интерфейсом питания ECM установлены правильно. Ссылка на схему схемы или схему проводов для идентификации контакта с разъемом. | Правильно установленные предохранители? *Да | 3В-2-2 |
| Правильно установленные предохранители? **NORepair:** Установите предохранители правильно.[[99-019-198 — Fuse, Harness In-Line\|См. процедуру 019-198 в разделе 19.]]. | 5а |  |

#### ШАГ 3B-2. Проверьте, не взорваны ли предохранители.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что предохранители OEM 10A между аккумулятором и 4-контактным интерфейсом питания ECM не взорваны. Ссылка на схему схемы или схему проводов для идентификации контакта с разъемом. | Сдувают предохранители? **Ремонт:** Найдите короткое замыкание. Заменить выдувной предохранитель(ы).[[99-019-198 — Fuse, Harness In-Line\|См. процедуру 019-198 в разделе 19.]]. | 5а |
| Сдувают предохранители? **НЕТ** | 4А |  |

### ШАГ 4. Проверьте силовую проводку и 4-контактный разъем интерфейса питания ECM.

#### ШАГ 4A. Проверьте электропроводку и 4-контактные контакты разъёма интерфейса питания ECM.

| **Условия:** Выключите выключатель питания Отключите электропроводку от 4-контактного разъема интерфейса ECM Power. Отключите электропроводку от батарей. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы разъёма электропроводки и 4-контактного интерфейса ECM Power для следующего: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или разъема изоляции Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]]. | Грязные или поврежденные контакты? **Ремонт:** В электропроводке или 4-контактном интерфейсе питания ECM обнаружено поврежденное соединение. Очистите разъем и булавки. Ссылка на схему или схему проводов для всех соединений проводов жгута. Замените проводку ремня или интерфейсный разъем. | 5а |
| Грязные или поврежденные контакты? **НЕТ** | 4B |  |

#### ШАГ 4B. Проверьте наличие открытой цепи в цепях питания батареи.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку от 4-контактного разъема интерфейса питания ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение между штифтами питания SUPPLY и штифтами питания RETURN на разъеме интерфейса питания 4 штифта. Ссылка на схему схемы или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов использования мультиметра. См. процедуру 019-359 в разделе 19. | По крайней мере (+) 10 VDC \[(+) 20 VDC для 24-вольтовой системы\]? **YESRepair:** Устранение неполадок в проводах двигателя и межсоединении при неисправности. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в Таблице ассоциированных процедур. | 5а |
| По крайней мере (+) 10 VDC \[(+) 20 VDC для 24-вольтовой системы\]? **НЕТ** | 4C |  |

#### ШАГ 4C. Проверьте наличие открытой цепи в цепях питания батареи.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку от 4-контактного разъема интерфейса питания ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение между штифтами силовой проводов SUPPLY на штифте силовой проводов 4 штифта ECM силового интерфейса разъема и блок-земли двигателя. Ссылка на схему схемы или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов использования мультиметра. См. процедуру 019-359 в разделе 19. | По крайней мере (+) 10 VDC \[(+) 20 VDC для 24-вольтовой системы\]? **Ремонт:** В цепи возврата напряжения батареи обнаружена открытая или высоковольтная цепь. Устранение неполадок в электропроводке и всех межсоединений для неисправности. По мере необходимости ремонтировать или заменять поврежденный компонент. | 5а |
| По крайней мере (+) 10 VDC \[(+) 20 VDC для 24-вольтовой системы\]? **NORepair:** В цепи возврата напряжения батареи обнаружена цепь с открытым или высоким сопротивлением. Устранение неполадок в электропроводке и всех межсоединений для неисправности. По мере необходимости ремонтировать или заменять поврежденный компонент. | 5а |  |

### ШАГ 5. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 5A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички данных в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 5В |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM. См. процедуру 019-032 в разделе 19 таблицы ассоциированных процедур. | 5В |  |

#### ШАГ 5B. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да | Ремонт завершён |
| Код неактивен? **Секретарь:**Проверить, что все шаги были выполнены. Если все шаги были выполнены, то следуйте своему техническому процессу эскалации. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Code 346 active or inactive with more than one count logged in the last 25 engine hours? |
> | STEP 2. | Check the ECM and engine harness. |  |
> |  | **STEP 2A.** Inspect the engine harness and ECM connectors. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check for an open circuit in the unswitched battery power circuits. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? |
> |  | **STEP 2C.** Check for an open circuit in the unswitched battery power circuits. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? |
> | STEP 3. | Check the batteries and fuses. |  |
> |  | **STEP 3A.** Check the batteries. | Connections tight and corrosion-free? |
> |  | **STEP 3B.** Check the battery voltage. | Battery voltage acceptable in normal and cranking conditions? |
> |  | **STEP 3B-1.** Verify that the original equipment manufacturer (OEM) fuses are installed correctly. | Fuse installed correctly? |
> |  | **STEP 3B-2.** Check if the OEM fuses are blown. | Fuse blown? |
> | STEP 4. | Check the OEM power harness and 4 pin ECM power interface connector. |  |
> |  | **STEP 4A.** Inspect the power harness and 4 pin ECM power interface connector pins. | Dirty or damaged pins? |
> |  | **STEP 4B.** Check for an open circuit in the battery power circuits. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? |
> |  | **STEP 4C.** Check for an open circuit in the battery power circuits. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? |
> | STEP 5. | Check ECM calibration and clear fault codes. |  |
> |  | **STEP 5A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 5B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use INSITE™ electronic service tool to read the fault codes. | Fault Code 346 active or inactive with more than one count logged in the last 25 engine hours? **YES** | 2A |
> | Fault Code 346 active or inactive with more than one count logged in the last 25 engine hours? **NO** | Use the following procedure for an inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19]]. |  |
>
> ### STEP 2. Check the ECM and engine harness.
>
> #### STEP 2A. Inspect the ECM and engine harness connectors.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness from the 4 pin ECM power interface connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or the engine harness connector. Clean the connector and pins. Replace the damaged section of the harness. Reference the circuit diagram or wiring diagram for all harness interconnections. Replace the harness. Refer to 019-043 in the Associated Procedures Table. | 5A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check for an open circuit in the unswitched battery power circuits.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage between the unswitched battery voltage SUPPLY pins and RETURN pins at the 50 pin ECM engine harness connector. Reference the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. Refer to Procedure 019-359 in Section 19. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 5A |
> | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **NO** | 2C |  |
>
> #### STEP 2C. Check for an open circuit in the unswitched battery power circuits.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage between the unswitched battery voltage SUPPLY pins at the 50 pin engine harness connector and engine block ground. Reference the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. Refer to Procedure 019-359 in Section 19. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **YESRepair:** An open or high resistance circuit has been detected in the battery voltage return circuit. Troubleshoot the engine harness and all interconnects for the malfunction. Repair or replace the damaged component as necessary. | 5A |
> | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **NO** | 3A |  |
>
> ### STEP 3. Check the batteries and fuses.
>
> #### STEP 3A. Check the batteries and fuses.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery terminal connections. | Connections tight and corrosion-free? **YES** | 3B |
> | Connections tight and corrosion-free? **NORepair:** Tighten the loose connections and clean the terminals. See the equipment manufacturer service information. | 5A |  |
>
> #### STEP 3B. Check the battery voltage.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Place the positive (+) probe of the multimeter on the positive battery terminal and touch the negative (-) probe to the negative battery terminal while trying to start the engine. | Battery voltage acceptable in normal and cranking conditions? **YES** | 3B-1 |
> | Battery voltage acceptable in normal and cranking conditions? **NORepair:** Charge or replace the battery. See the equipment manufacturer service information. | 5A |  |
>
> #### STEP 3B-1. Verify that the OEM fuses are installed correctly.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify that the OEM 10A fuses between the battery and 4 pin ECM power interface are installed correctly. Reference the circuit diagram or the wiring diagram for connector pin identification. | Fuses installed correctly? **YES** | 3B-2 |
> | Fuses installed correctly? **NORepair:** Install the fuses correctly. [[99-019-198 — Fuse, Harness In-Line\|Refer to Procedure 019-198 in Section 19]]. | 5A |  |
>
> #### STEP 3B-2. Check if the OEM fuses are blown.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify that the OEM 10A fuses between the battery and 4 pin ECM power interface are **not** blown. Reference the circuit diagram or the wiring diagram for connector pin identification. | Fuses blown? **YESRepair:** Locate the short circuit. Replace the blown fuse(s). [[99-019-198 — Fuse, Harness In-Line\|Refer to Procedure 019-198 in Section 19]]. | 5A |
> | Fuses blown? **NO** | 4A |  |
>
> ### STEP 4. Check the power harness and 4 pin ECM power interface connector.
>
> #### STEP 4A. Inspect the power harness and the 4 pin ECM power interface connector pins.
>
> | **Conditions:** Turn keyswitch OFF Disconnect power harness from the 4 pin ECM Power interface connector. Disconnect the power harness from the batteries. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the power harness and 4 pin ECM Power interface connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the power harness or 4 pin ECM power interface connection. Clean the connector and pins. Reference the circuit diagram or wiring diagram for all harness interconnections. Replace the harness or interface connector. | 5A |
> | Dirty or damaged pins? **NO** | 4B |  |
>
> #### STEP 4B. Check for an open circuit in the battery power circuits.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the power harness from the 4 pin ECM power interface connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage between the power harness SUPPLY pins and the power harness RETURN pins at the power harness 4 pin power interface connector. Reference the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. Refer to Procedure 019-359 in Section 19. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **YESRepair:** Troubleshoot the engine harness and the interconnect for the malfunction. Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 5A |
> | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **NO** | 4C |  |
>
> #### STEP 4C. Check for an open circuit in the battery power circuits.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the power harness from the 4 pin ECM power interface connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage between the power harness SUPPLY pins on the power harness 4 pin ECM power interface connector and engine block ground. Reference the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. Refer to Procedure 019-359 in Section 19. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **YESRepair:** An open or high resistance circuit has been detected in the battery voltage return circuit. Troubleshoot the power harness and all interconnects for the malfunction. Repair or replace the damaged component as necessary. | 5A |
> | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **NORepair:** An open or high resistance circuit has been detected in the battery voltage return circuit. Troubleshoot the power harness and all interconnects for the malfunction. Repair or replace the damaged component as necessary. | 5A |  |
>
> ### STEP 5. Check ECM calibration and clear fault codes.
>
> #### STEP 5A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 5B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. Refer to Procedure 019-032 in Section 19 in the Associated Procedure Table. | 5B |  |
>
> #### STEP 5B. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete |
> | Fault code inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow your technical escalation process. | Repair complete |  |
