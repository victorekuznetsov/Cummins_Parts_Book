---
aliases:
  - "Код 1521 (термистор) — цепь датчика температуры ОГ цилиндра 3 — напряжение выше нормы"
type: "Процедура"
doc: "122-t05-1521thermistor"
title_en: "Fault Code 1521 (Thermistor) - Exhaust Gas Temperature Sensor Circuit Cylinder 3 - Voltage Above Normal or Shorted to High Source"
title_ru: "Код 1521 (термистор) — цепь датчика температуры ОГ цилиндра 3 — напряжение выше нормы"
modified: "2014-05-15"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1521thermistor.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1521thermistor.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Fault Code 1521 (Thermistor) - Exhaust Gas Temperature Sensor Circuit Cylinder 3 - Voltage Above Normal or Shorted to High Source
**Код 1521 (термистор) — цепь датчика температуры ОГ цилиндра 3 — напряжение выше нормы**

> [!abstract] Процедура · `122-t05-1521thermistor`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2014-05-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1521thermistor.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1521thermistor.pdf)

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
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3824811 - пробный щуп типа вилки DeutschTM Номер детали 3824812 - пробная утечка типа гнезда DeutschTM Номер детали 3822758 - пробный щуп типа вилки DeutschTM/AMPTM/Metri-PackTM Номер детали 3822917 - пробный щуп типа гнезда DeutschTM/AMPTM/Metri-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить неактивный код ошибки. | Код 1521 неактивен? |
| ШАГ 2. | Проверьте датчик температуры выхлопных газов цилиндр 3 схемы и соединительные контакты. |  |
|  | **STEP 2A.** Осмотрите упряжку для проводов двигателя и датчик температуры выхлопных газов цилиндр 3 и схему. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте реакцию цепи. | Код ошибки 672 активен? |
|  | **STEP 2C** Проверить коды неисправностей и состояние датчика. | Код 1521 активен? |
| ШАГ 3. | Проверьте ECM и проверьте электропроводку двигателя. |  |
|  | **STEP 3A.** Проверить контакты разъема ECM и проводов двигателя. | Грязные или поврежденные контакты? |
|  | **ШАГ 3В.** Проверьте наличие открытой цепи ВПЕРЕД в ремне электропроводки двигателя. | Менее 10 Ом? |
|  | **STEP 3C.** Проверьте наличие открытой схемы SIGNAL в ремне электропроводки двигателя. | Менее 10 Ом? |
|  | **STEP 3D.** Проверьте короткое замыкание в проводной ремне. | Больше 100 тысяч ом? |
|  | **STEP 3E.** Проверить неактивный код ошибки. | Код 1521 неактивен? |
|  | **STEP 3F.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 1521 неактивен? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте неактивный код ошибки.

| **Условия: **Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте неактивный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 1521 неактивен? *Да | [[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |
| Код 1521 неактивен? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте датчик температуры выхлопных газов цилиндр 3 и схему.

#### ШАГ 2A. Проверьте датчик температуры выхлопных газов цилиндр 3 схемы и соединительные контакты.

| **Условия:** Замок зажигания. Отсоедините датчик температуры выхлопных газов цилиндр 3 от разъема жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите разъём ремня электропроводки двигателя и датчик температуры выхлопных газов цилиндр 3 соединительного контакта для следующих целей: Свободный разъем. Корродированные булавки. Сдвинутые или сломанные булавки. Откинутые назад или расширенные булавки. Влажность внутри или на разъеме. Пропавшие или поврежденные соединительные уплотнения. Грязь или мусор в или на контактах разъема. Скорлупа разбита. Повреждение изоляции провода. Поврежденная блокировка разъема.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]]для общих методов проверки. | Грязные или поврежденные контакты? **Ремонт:** В разъеме баллона 3 датчика температуры выхлопных газов или разъеме ремней электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Заменить поврежденный участок проводов двигателя ремнем или поврежденный датчик температуры выхлопных газов цилиндром 3 разъема, если ремонт невозможен. Проверьте все проводов, подключенные последовательно. См. схему или схему проводов для всех соединений проводов. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте отклик цепи.

| **Условия:** Замок зажигания. Отсоедините датчик температуры выхлопных газов цилиндр 3 от проводов двигателя. Поместите провод перемычки между датчиком температуры выхлопных газов 3 SIGNAL и обратного контакта на разъем датчика проводов двигателя. Включай зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие соответствующего ECM-ответа через 2 минуты холостого хода двигателя выше 600 об/мин. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. После пропоказаний кодов неисправностей выключите двигатель. Удалите провод перемычки между датчиком температуры выхлопных газов 3 SIGNAL и верните контакт на разъем датчика проводов двигателя. | Код ошибки 672 активен? *Да | 2C |
| Код ошибки 672 активен? **НЕТ** | 3А |  |

#### ШАГ 2C. Проверьте коды неисправностей и состояние датчика.

| **Условия:** Замок зажигания. Подключите датчик температуры выхлопных газов 3 к электропроводке двигателя. Включай зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие соответствующего ECM-ответа через 2 минуты холостого хода двигателя выше 600 об/мин. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 1521 активен? Заменить датчик температуры выхлопных газов. См. процедуру 019-013 в разделе 19. | 4А |
| Код 1521 активен? **Норвегия: **Нет. Удаление и установка разъема исправили неисправность. | 4А |  |

### ШАГ 3. Проверьте ECM и проверьте электропроводку двигателя.

#### ШАГ 3A. Проверьте контакты разъема ECM и проводов двигателя.

| **Условия:** Замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты электропроводки двигателя и разъема ECM на предмет: Свободный разъем. Корродированные булавки. Сдвинутые или сломанные булавки. Откинутые назад или расширенные булавки. Влажность внутри или на разъеме. Пропавшие или поврежденные соединительные уплотнения. Грязь или мусор в или на контактах разъема. Скорлупа разбита. Повреждение изоляции провода. Поврежденная блокировка разъема.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]]для общих методов проверки. | Грязные или поврежденные контакты? **В разъеме ECM или разъеме ремня электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Заменить поврежденный участок проводов жгутом, если ремонт **не возможен. Проверьте все проводов, подключенные последовательно. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. Замените ECM, если разъем ECM поврежден. См. процедуру 019-031 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте наличие открытой схемы RETURN в ремне электропроводки двигателя.

| **Условия:** Замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. Отсоедините датчик температуры выхлопных газов цилиндр 3 от проводной упряжки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление между датчиком температуры выхлопных газов цилиндром 3 обратного контакта в проводах двигателя с помощью разъема ECM 60 pin и датчиком температуры выхлопных газов цилиндром 3 обратного контакта в разъеме датчика температуры выхлопных газов. См. схему или схему проводов для идентификации контакта с разъемом.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]]Общие методы измерения сопротивления. | Менее 10 Ом? *Да | 3C |
| Менее 10 Ом? **NORepair:** В ремне электропроводки двигателя обнаружена открытая схема RETURN. Ремонт или замена ремня электропроводки двигателя. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 4А |  |

#### ШАГ 3C. Проверьте наличие открытой схемы SIGNAL в ремне электропроводки двигателя.

| **Условия:** Замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. Отсоедините датчик температуры выхлопных газов цилиндр 3 от проводной упряжки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление между датчиком температуры выхлопных газов цилиндром 3 сигнального контакта в разъеме ECM 60 и датчиком температуры выхлопных газов цилиндром 3 сигнального контакта в разъеме датчика температуры выхлопных газов. См. схему или схему проводов для идентификации контакта с разъемом.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]]Общие методы измерения сопротивления. | Менее 10 Ом? *Да | 3D |
| Менее 10 Ом? **NORepair:** В ремне электропроводки двигателя обнаружена открытая схема SIGNAL. Ремонт или замена ремня электропроводки двигателя. Замените жгут проводов двигателя. См. процедуру 019-043 в разделе 19. | 4А |  |

#### ШАГ 3D. Проверьте короткое замыкание контакт-контакт.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема цоколя ECM 60. Отсоедините датчик температуры выхлопных газов цилиндр 3 от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание контакт-контакт. Измерьте сопротивление между датчиком температуры выхлопных газов 3 сигнального контакта в проводах двигателя с помощью разъема ECM 60 pin и всех других разъемов в разъеме. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3E |
| Больше 100 тысяч ом? **NORepair:** В ремне электропроводки двигателя обнаружено короткое замыкание на проводе SIGNAL. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. | 4А |  |

#### ШАГ 3E. Проверьте неактивный код ошибки.

| **Условия:** Выключите замок зажигания. Соедините все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте на подходящую схему ответа. Управляйте двигателем с праздной скоростью более 600 об/мин в течение 2 минут. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 1521 неактивен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | 4А |
| Код 1521 неактивен? **NORepair:** Проверьте наличие обновлений калибровки ECM. | 3F |  |

#### ШАГ 3F. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **Ремонт:** Заменить неисправную ЭХМ. См. процедуру 019-031 в разделе 19. | 4А |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM. См. процедуру 019-032 в разделе 19. | 4А |  |

### ШАГ 4. Сбросьте коды неисправностей.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включай зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код 1521 неактивен? *Да | 4B |
| Код 1521 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. Включай зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair: **Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие шаги по устранению неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3824811 - male Deutsch™ test lead Part Number 3824812 - female Deutsch™ test leak Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for an inactive fault code. | Fault Code 1521 inactive? |
> | STEP 2. | Check the exhaust gas temperature sensor cylinder 3 circuit and connector pins. |  |
> |  | **STEP 2A.** Inspect the engine harness and exhaust gas temperature sensor cylinder 3 and circuit. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the circuit response. | Fault Code 672 active? |
> |  | **STEP 2C.** Check the fault codes and verify sensor condition. | Fault Code 1521 active? |
> | STEP 3. | Inspect the ECM and check the engine harness. |  |
> |  | **STEP 3A.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check for an open RETURN circuit in the engine wiring harness. | Less than 10 ohms? |
> |  | **STEP 3C.** Check for an open SIGNAL circuit in the engine wiring harness. | Less than 10 ohms? |
> |  | **STEP 3D.** Check for a pin-to-pin short circuit in the wiring harness. | Greater than 100k ohms? |
> |  | **STEP 3E.** Check for an inactive fault code. | Fault Code 1521 inactive? |
> |  | **STEP 3F.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 1521 inactive? |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for an inactive fault code.
>
> | **Conditions:** Keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an inactive fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1521 inactive? **YES** | [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |
> | Fault Code 1521 inactive? **NO** | 2A |  |
>
> ### STEP 2. Check the exhaust gas temperature sensor cylinder 3 and circuit.
>
> #### STEP 2A. Check the exhaust gas temperature sensor cylinder 3 circuit and connector pins.
>
> | **Conditions:** Keyswitch OFF. Disconnect the exhaust gas temperature sensor cylinder 3 connector from the engine harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness connector and exhaust gas temperature sensor cylinder 3 connector pins for the following: Loose connector. Corroded pins. Bent or broken pins. Pushed back or expanded pins. Moisture in or on the connector. Missing or damaged connector seals. Dirt or debris in or on the connector pins. Connector shell broken. Wire insulation damage. Damaged connector locking tab. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]] for general inspection techniques. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the exhaust gas temperature sensor cylinder 3 connector or engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Replace the damaged section of the engine harness or damaged exhaust gas temperature sensor cylinder 3 connector, if repair is **not** possible. Check all harnesses connected in series. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the circuit response.
>
> | **Conditions:** Keyswitch OFF. Disconnect the exhaust gas temperature sensor cylinder 3 connector from the engine harness. Place a jumper wire between the exhaust gas temperature sensor 3 SIGNAL and RETURN pin at the sensor connector of the engine harness. Keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 2 minutes idling the engine above 600 rpm. Use INSITE™ electronic service tool to read the fault codes. After reading the fault codes, switch OFF the engine. Remove the jumper wire between the exhaust gas temperature sensor 3 SIGNAL and RETURN pin at the sensor connector of the engine harness. | Fault Code 672 active? **YES** | 2C |
> | Fault Code 672 active? **NO** | 3A |  |
>
> #### STEP 2C. Check the fault codes and verify sensor condition.
>
> | **Conditions:** Keyswitch OFF. Connect the exhaust gas temperature sensor 3 to the engine harness. Keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 2 minutes idling the engine above 600 rpm. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1521 active? **YESRepair:** Replace the exhaust gas temperature sensor. Refer to Procedure 019-013 in Section 19. | 4A |
> | Fault Code 1521 active? **NORepair:** None. The removal and installation of the connector corrected the fault. | 4A |  |
>
> ### STEP 3. Inspect the ECM and check the engine harness.
>
> #### STEP 3A. Inspect the ECM and engine harness connector pins.
>
> | **Conditions:** Keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connector pins for the following: Loose connector. Corroded pins. Bent or broken pins. Pushed back or expanded pins. Moisture in or on the connector. Missing or damaged connector seals. Dirt or debris in or on the connector pins. Connector shell broken. Wire insulation damage. Damaged connector locking tab. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]] for general inspection techniques. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or the engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Replace the damaged section of harness, if repair is **not** possible. Check all harnesses connected in series. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the ECM if the ECM connector is damaged. Refer to Procedure 019-031 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check for an open RETURN circuit in the engine wiring harness.
>
> | **Conditions:** Keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the exhaust gas temperature sensor cylinder 3 from the wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the exhaust gas temperature sensor cylinder 3 RETURN pin in the engine harness ECM 60 pin connector and the exhaust gas temperature sensor cylinder 3 RETURN pin in the engine harness exhaust gas temperature sensor connector. Refer to the circuit diagram or wiring diagram for connector pin identification. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19]] for general resistance measurement techniques. | Less than 10 ohms? **YES** | 3C |
> | Less than 10 ohms? **NORepair:** An open RETURN circuit has been detected in the engine harness. Repair or replace the engine harness. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |
>
> #### STEP 3C. Check for an open SIGNAL circuit in the engine wiring harness.
>
> | **Conditions:** Keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the exhaust gas temperature sensor cylinder 3 from the wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the exhaust gas temperature sensor cylinder 3 SIGNAL pin in the ECM 60 pin connector and the exhaust gas temperature sensor cylinder 3 SIGNAL pin in the engine harness exhaust gas temperature sensor connector. Refer to the circuit diagram or wiring diagram for connector pin identification. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19]] for general resistance measurement techniques. | Less than 10 ohms? **YES** | 3D |
> | Less than 10 ohms? **NORepair:** An open SIGNAL circuit has been detected in the engine wiring harness. Repair or replace the engine harness. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |
>
> #### STEP 3D. Check for a pin-to-pin short circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the exhaust gas temperature sensor cylinder 3 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short circuit. Measure the resistance between the exhaust gas temperature sensor 3 SIGNAL pin in the engine harness ECM 60 pin connector and all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3E |
> | Greater than 100k ohms? **NORepair:** A pin-to-pin short circuit on the SIGNAL wire has been detected in the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |
>
> #### STEP 3E. Check for an inactive fault code.
>
> | **Conditions:** Turn keyswitch OFF. Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response. Operate the engine with an idle speed greater than 600 rpm for 2 minutes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1521 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
> | Fault Code 1521 inactive? **NORepair:** Check if an ECM calibration update is available. | 3F |  |
>
> #### STEP 3F. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YESRepair:** Replace the malfunctioning ECM. Refer to Procedure 019-031 in Section 19. | 4A |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. Refer to Procedure 019-032 in Section 19. | 4A |  |
>
> ### STEP 4. Clear the fault codes.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 1521 inactive? **YES** | 4B |
> | Fault Code 1521 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting steps |  |
