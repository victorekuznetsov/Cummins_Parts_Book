---
aliases:
  - "Код 1543 — цепь вспомогательного датчика давления 1 — напряжение ниже нормы"
type: "Процедура"
doc: "122-t05-1543"
title_en: "FAULT CODE 1543 - Auxiliary Pressure Sensor Input 1 Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Код 1543 — цепь вспомогательного датчика давления 1 — напряжение ниже нормы"
modified: "2012-07-29"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1543.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1543.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 1543 - Auxiliary Pressure Sensor Input 1 Circuit - Voltage Below Normal or Shorted to Low Source
**Код 1543 — цепь вспомогательного датчика давления 1 — напряжение ниже нормы**

> [!abstract] Процедура · `122-t05-1543`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1543.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1543.pdf)

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
|  | **STEP 1A.** Проверить коды неисправностей датчиков. | Код 352 активен? |
| ШАГ 2. | Проверьте датчик давления OEM и схему. |  |
|  | **STEP 2A.** Для морских применений проверьте, установлен ли резистивный прыгун, когда датчик давления **не используется. | Резистивный прыгун, установленный в удлинении жгута проводов, когда датчик давления OEM **не используется|
|  | **STEP 2B.** Для морских применений проверьте резистивный прыгун. | Сопротивление в спецификациях по всем штифтам? |
|  | **STEP 2C** Проверить датчик давления OEM и контакты разъема. | Грязные или поврежденные контакты? |
|  | **STEP 2D.** Проверьте напряжение питания датчика и схему возврата. | Напряжение между 4,75 и 5,25-VDC? |
|  | **ШАГ 2Е.** Проверьте реакцию цепи. | Код 297 активен, а Код 298 неактивен? |
|  | **STEP 2F.** Проверьте коды неисправностей и состояние датчика. | Код ошибки 298 активен? |
| ШАГ 3. | Проверьте электропроводку ECM и OEM. |  |
|  | **STEP 3A.** Проверить контакты разъёма электропроводки ECM и OEM. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте наличие открытой цепи в электропроводке OEM. | Менее 10 Ом? |
|  | **STEP 3C.** Проверьте наличие открытой цепи в электропроводке OEM. | Менее 10 Ом? |
|  | **STEP 3D.** Проверьте короткое замыкание в проводной ремне OEM. | Больше 100 Км? |
|  | **ШАГ 3Е.** Проверьте короткое замыкание от пин-до земли. | Больше 100 Км? |
|  | **STEP 3F.** Проверить неактивный код ошибки. | Код ошибки 298 неактивен? |
| ШАГ 4. | Четкие коды ошибок. |  |
|  | **STEP 4A.** Отключить коды неисправностей. | Код 1543 неактивен? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте коды неисправностей датчика.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте коды неисправностей датчика. Используйте электронную службу INSITETM для считывания кодов неисправностей. | Код 352 активен? *Да | Код ошибки 352. |
| Код 352 активен? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте датчик давления OEM и схему.

#### ШАГ 2A. Для морских применений проверьте, установлен ли резистивный прыгун, когда датчик давления не используется.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, установлен ли датчик давления OEM. Если датчик давления OEM не установлен, проверьте, чтобы убедиться, что в удлинении проводов установлен резистивный прыгун. | Резистивный прыгун, установленный в удлинении жгута проводов, когда датчик давления OEM **не используется **Да | 2В |
| Резистивный прыгун, установленный в удлинении жгута проводов, когда датчик давления OEM **не используется **NORepair: Установите резистивный прыгун в удлинитель проводов. | 4А |  |

#### ШАГ 2B. Для морских применений проверьте резистивный прыгун.

| **Условия:** Выключите замок зажигания. Отсоедините проводку с удлинением проводов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сопротивление через штифты. Контакт 1 - Контакт 2: 1.2k Ом контакт 2 контакт 3: 1.5k Ом контакт 1 контакт 3: 270 Омс См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление в спецификациях по всем штифтам? *Да | 2C |
| Сопротивление в спецификациях по всем штифтам? **NORepair:** Заменить резистивный прыгун. | 4А |  |

#### ШАГ 2C. Проверьте датчик давления OEM и контакты разъема.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления OEM от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы разъёма OEM-проводов и датчика давления OEM для следующих целей: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте напряжение питания датчика и обратную цепь.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления OEM от электропроводки OEM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение питания и обратную цепь. Измерьте напряжение между контактом питания OEM + 5 вольт и обратным контактом давления OEM на разъеме датчика проводов OEM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов использования мультиметра.[[99-019-359 — Multimeter Usage\|См. процедуру 019-359 в разделе 19.]] | Напряжение между 4,75 и 5,25-VDC? *Да | 2Е |
| Напряжение между 4,75 и 5,25-VDC? **НЕТ** | 3А |  |

#### ШАГ 2E. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления OEM от электропроводки OEM. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Поместите провод перемычки между контактом подачи давления OEM и контактом сигнала давления OEM на разъеме датчика давления OEM проводов OEM. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 297 активен, а Код 298 неактивен? *Да | 2F |
| Код 297 активен, а Код 298 неактивен? **НЕТ** | 3А |  |

#### ШАГ 2F. Проверьте коды неисправностей и состояние датчика.

| **Условия:** Выключите замок зажигания. Подключите датчик давления OEM к электропроводке OEM. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 298 уязвимости активен? Поврежденный датчик был обнаружен. Замените датчик давления OEM. См. сервисное руководство изготовителя машины. | 4А |
| Код 298 уязвимости активен? **Норвегия: **Нет. Удаление и установка разъема исправили неисправность. | 4А |  |

### ШАГ 3. Проверьте электропроводку ECM и OEM.

#### ШАГ 3A. Проверить контакты разъёма ECM и OEM-проводов.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты проводов OEM и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъеме ECM или разъеме OEM-проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте наличие открытой цепи в OEM-проводах.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. Отсоедините датчик давления OEM от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление между OEM проводкой ремня разъема ECM OEM давления возвратного контакта и OEM проводов ремня OEM датчика давления разъёма обратного контакта. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 3C |
| Менее 10 Ом? **NORepair:** В электропроводке OEM обнаружена схема с открытым возвратом. Устранение неполадок в каждой проводах, соединенной последовательно, чтобы определить, которая содержит открытую обратную цепь. Ремонт или замена OEM проводов жгута. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 3C. Проверьте наличие открытой цепи в OEM-проводах.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. Отсоедините датчик давления OEM от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление между OEM проводкой жгута разъема ECM OEM сигнала контакта давления и OEM проводов жгута OEM датчика давления разъема контакта. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом** Да** | 3D |
| Менее 10 Ом? **NORepair:** В электропроводке OEM обнаружена схема открытого сигнала. Устранение неполадок в каждой проводах, соединенной последовательно, чтобы определить, какая из них содержит цепь открытого сигнала. Ремонт или замена OEM проводов жгута. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 3D. Проверьте короткое замыкание контакт-контакт в электропроводке OEM.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. Отсоедините датчик давления OEM от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое контактное соединение. Измерьте сопротивление между контактом сигнала давления OEM в разъеме ECM проводов OEM и всеми другими штифтами в разъеме OEM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3E |
| Больше 100 тысяч ом? **NORepair:** В электропроводке OEM обнаружено короткое замыкание на проводе сигнала. Устранение неполадок в каждой проводах, соединенной последовательно, чтобы определить, какая из них содержит короткое кольцо сигнала. Ремонт или замена OEM проводов жгута. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 3E. Проверьте короткое замыкание от булавки до земли.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. Отсоедините датчик давления OEM от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, не хватает липкой крошки. Измерьте сопротивление между контактом сигнала давления OEM в разъёме ECM и земле. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3F |
| Больше 100 тысяч ом? **NORepair:** В электропроводке OEM обнаружено короткое замыкание на сигнальном проводе. Устранение неполадок в каждой проводах, соединенной последовательно, чтобы определить, какая из них содержит короткое кольцо сигнала. Ремонт или замена OEM проводов жгута. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 3F. Проверьте неактивный код ошибки.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 298 неактивен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | 4А |
| Код ошибки 298 неактивен? Заменить ЭКМ. См. процедуру 019-031 в разделе 19. | 4А |  |

### ШАГ 4. Сбросьте коды неисправностей.

#### ШАГ 4A. Отключите коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код 1543 неактивен? *Да | 4B |
| Код 1543 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён. |
| Все коды неисправностей очищены? **NORepair:** Устранение неполадок с оставшимися кодами неисправностей. | Перейдите к соответствующим шагам устранения неполадок. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for sensor supply fault codes. | Fault Code 352 active? |
> | STEP 2. | Check the OEM pressure sensor and circuit. |  |
> |  | **STEP 2A.** For Marine applications, check if a a resistive jumper is installed when a pressure sensor is **not** being used. | Resistive jumper installed in wiring harness extension when OEM pressure sensor is **not** being used? |
> |  | **STEP 2B.** For Marine applications, check the resistive jumper. | Resistance within specifications across all pins? |
> |  | **STEP 2C.** Inspect the OEM pressure sensor and connector pins. | Dirty or damaged pins? |
> |  | **STEP 2D.** Check the sensor supply voltage and return circuit. | Voltage between 4.75 and 5.25-VDC? |
> |  | **STEP 2E.** Check the circuit response. | Fault Code 297 active and Fault Code 298 inactive? |
> |  | **STEP 2F.** Check the fault codes and verify sensor condition. | Fault Code 298 active? |
> | STEP 3. | Check the ECM and OEM harness. |  |
> |  | **STEP 3A.** Inspect ECM and OEM harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
> |  | **STEP 3C.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
> |  | **STEP 3D.** Check for a pin-to-pin short circuit in the OEM harness. | Greater than 100K ohms? |
> |  | **STEP 3E.** Check for a pin-to-ground short circuit. | Greater than 100K ohms? |
> |  | **STEP 3F.** Check for an inactive fault code. | Fault Code 298 inactive? |
> | STEP 4. | Clear fault codes. |  |
> |  | **STEP 4A.** Disable the fault codes. | Fault Code 1543 inactive? |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for sensor supply fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for sensor supply fault codes. Use INSITE™ electronic service to tool read the fault codes. | Fault Code 352 active? **YES** | Reference Fault Code 352. |
> | Fault Code 352 active? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM pressure sensor and circuit.
>
> #### STEP 2A. For Marine applications, check if a resistive jumper is installed when a pressure sensor is **not** being used.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check if an OEM pressure sensor is installed. If an OEM pressure sensor is not installed, check to make sure a resistive jumper is installed in the wiring harness extension. | Resistive jumper installed in wiring harness extension when OEM pressure sensor is **not** being used? **YES** | 2B |
> | Resistive jumper installed in wiring harness extension when OEM pressure sensor is **not** being used? **NORepair:** Install the resistive jumper in the wiring harness extension. | 4A |  |
>
> #### STEP 2B. For Marine applications, check the resistive jumper.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the wiring extension harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the resistance across the pins. Pin 1 to Pin 2: 1.2k Ohms Pin 2 to Pin 3: 1.5k Ohms Pin 1 to Pin 3: 270 Ohms Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Resistance within specifications across all pins? **YES** | 2C |
> | Resistance within specifications across all pins? **NORepair:** Replace the resistive jumper. | 4A |  |
>
> #### STEP 2C. Inspect the OEM pressure sensor and connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness and OEM pressure sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2D |  |
>
> #### STEP 2D. Check the sensor supply voltage and return circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM pressure sensor from the OEM harness. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply voltage and return circuit. Measure the voltage between the OEM pressure +5 volt SUPPLY pin and the OEM pressure RETURN pin at the sensor connector of the OEM harness. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Voltage between 4.75 and 5.25-VDC? **YES** | 2E |
> | Voltage between 4.75 and 5.25-VDC? **NO** | 3A |  |
>
> #### STEP 2E. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM pressure sensor from the OEM harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Place a jumper wire between the OEM pressure SUPPLY pin and the OEM pressure SIGNAL pin at the OEM pressure sensor connector of the OEM harness. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 297 active and Fault Code 298 inactive? **YES** | 2F |
> | Fault Code 297 active and Fault Code 298 inactive? **NO** | 3A |  |
>
> #### STEP 2F. Check the fault codes and verify sensor condition.
>
> | **Conditions:** Turn keyswitch OFF. Connect the OEM pressure sensor to the OEM harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 298 is active? **YESRepair:** A damaged sensor has been detected. Replace the OEM pressure sensor. Refer to the OEM service manual. | 4A |
> | Fault Code 298 is active? **NORepair:** None. The removal and installation of the connector corrected the fault. | 4A |  |
>
> ### STEP 3. Check the ECM and OEM harness.
>
> #### STEP 3A. Inspect ECM and OEM harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or OEM harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check for an open circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the OEM harness ECM connector OEM pressure RETURN pin and the OEM harness OEM pressure sensor connector RETURN pin. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3C |
> | Less than 10 ohms? **NORepair:** An open return circuit has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the open return circuit. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 3C. Check for an open circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the OEM harness ECM connector OEM pressure SIGNAL pin and the OEM harness OEM pressure sensor connector SIGNAL pin. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms **YES** | 3D |
> | Less than 10 ohms? **NORepair:** An open signal circuit has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the open signal circuit. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 3D. Check for a pin-to-pin short circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short. Measure the resistance between the OEM pressure SIGNAL pin in the OEM harness ECM connector and all other pins in the OEM connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3E |
> | Greater than 100k ohms? **NORepair:** A pin-to-pin short circuit on the signal wire has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the shorted signal circuit. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 3E. Check for a pin-to-ground short circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-ground short. Measure the resistance between the OEM pressure SIGNAL pin in the OEM harness ECM connector and ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3F |
> | Greater than 100k ohms? **NORepair:** A pin-to-ground short circuit on the signal wire has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the shorted signal circuit. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 3F. Check for an inactive fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 298 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
> | Fault Code 298 inactive? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |  |
>
> ### STEP 4. Clear the fault codes.
>
> #### STEP 4A. Disable the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 1543 inactive? **YES** | 4B |
> | Fault Code 1543 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Go to the appropriate troubleshooting steps. |  |
