---
aliases:
  - "Введение термопарного датчика температуры ОГ (EGTS)"
type: "TSB"
doc: "tsb210001"
title_en: "New Thermocouple Exhaust Gas Temperature Sensor (EGTS) Introduction"
title_ru: "Введение термопарного датчика температуры ОГ (EGTS)"
released: "2024-02-19"
modified: "2024-02-19"
group: "19 - Electronic Engine Controls"
engines:
  - "33224404"
  - "33239746"
  - "33239899"
  - "41340468"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK50"
parts:
  - "3015283"
  - "3609817"
  - "3641274"
  - "4326918"
  - "4924291"
  - "5372025"
  - "5372029"
  - "5372878"
  - "5376160"
  - "5376161"
  - "5462023"
  - "5462024"
  - "5462025"
  - "5462026"
  - "5538108"
  - "5538144"
  - "5538145"
  - "5538146"
  - "5538148"
  - "5538926"
  - "5538937"
  - "5538957"
  - "5539796"
  - "5572259"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210001.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK50"
  - "год/2024"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# New Thermocouple Exhaust Gas Temperature Sensor (EGTS) Introduction
**Введение термопарного датчика температуры ОГ (EGTS)**

> [!abstract] TSB · `tsb210001`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK50
> **Даты:** выпущен 2024-02-19 · изменён 2024-02-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210001.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Введение термопарного датчика температуры ОГ (EGTS)

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- QSK50 CM2150 MCRS
- QSK50 CM2150 K107

**Проблема**

Симптом:

- Датчик температуры выхлопного газа (EGTS) Коды ошибок: FC671, FC672, FC673, FC674, FC676, FC677, FC678, FC722, FC723, FC724, FC725, FC726, FC728, FC1521, FC1522, FC1523, FC1524, FC1525, FC1526, FC1527, FC1529, FC1532, FC1533, FC1534, FC1535, FC1536, FC1618, FC1619, FC2735, FC2736.
- Отсутствие считывания или некорректного сигнала EGTS на модуль управления двигателем (ECM).

Первопричина:

- Прочность кабеля на растяжение при температуре выхлопных газов (EGTS) была превышена из-за того, что кабель датчика подвергается воздействию высокой температуры, что приводит к разрыву кабеля.
- Близость EGTS к выпускным коллекторам, которые имеют лучистую температуру более 400°C \[752°F \], приводит к перегреву и неисправности точки перехода EGTS (от твердого тела к косе).

![[19r99706.png]]

Рисунок 1 Примеры повреждений ЭГТС.

**Проверка**

- Визуальный осмотр кабеля EGTS покажет тепловое повреждение кабеля EGTS. Обнаженные голые провода, ерзающие.
- Использование мультиметра для измерения через терминалы датчиков приводит к чрезвычайно высокому сопротивлению или открытой цепи.
- Использование электронного инструментария обслуживания Cummins® или эквивалентного ему средства для подтверждения наличия любого из кодов неисправностей, перечисленных выше.

**Решение**

- Выпущена новая более длинная термопара кузова EGTS, которая имеет более высокую рабочую температуру вокруг области выхлопного коллектора. Раздел Доступность Сервисных Частей ниже для номеров частей.
- Существующие терморезисторы EGTS не совместимы с термопарой EGTS. См. раздел Совместимость частей ниже.

**Описание изменения**

Существующие терморезисторные датчики температуры выхлопных газов

![[19r99734.png]]

2, Существующие ЭГТС без расширенного тела.

Новые термопары выхлопных газовых датчиков температуры

Четыре новые термопары EGTS необходимы для правильного маршрутизации датчиков от выхлопного коллектора и предотвращения вмешательства в работу других компонентов, таких как водяные и выхлопные коллекторы, турбокомпрессоры и т.д. На вершине двигателей. Инконель термопары EGTS имеет более высокую температурную оценку, намного более длинную, чем терморезистор EGTS. Термопары EGTS имеют темно-оранжевые кабели.

![[19r99708.png]]

Рисунок 3, Новая маршрутизация EGTS.

См. таблицу 1 ниже, чтобы определить, какой номер детали EGTS совместим с расположением цилиндра.

| Таблица 1 Цилиндровый локатор EGTS |  |
|---|---|
| Часть EGTS Номер | Цилиндровые номера Места |
| [[5462023]] | 1 |
| [[5462024]] | 2, 3, 4, 5, 6, 7, 10, 11, 12, 13 |
| [[5462025]] | 8, 9 |
| [[5462026]] | 14, 15, 16 |

![[19r99709.png]]

Рисунок 4, EGTS Part Number Locations by Cylinder.

Совместимые левобережье и правобережье основные провода двигателя

Основные жгуты для проводов двигателя теперь имеют дополнительную ветку разъёма коробки конвертера. Это можно найти как на левом берегу (LB), так и на правом берегу (RB) основных проводных ремнях двигателя.

![[19r99710.png]]

Рисунок 5, Конвертерная коробка EGTS.

Совместимые топливные форсунки левого и правого берега / EGTS Wiring Harnesss

Внутренние провода топливных форсунок/проводников EGTS были изменены на провода, поддерживающие новые термопары. Разъемы жгута проводов были объединены с одним более крупным разъемом, который соединяется с основными жгутами проводов двигателя.

![[19r99711.png]]

Рисунок 6, Новые точки подключения проводов.

![[19r99712.png]]

Рисунок 7, Новые точки подключения проводов.

Левый и правый банковские конвертеры и монтажные скобки

Для размещения и защиты внутренних модулей преобразования сигналов требуются две коробки преобразователя. Модули преобразования внутренних сигналов обрабатывают сигналы термопары EGTS для ECM двигателя. Оба конвертера LB и RB установлены на воздухозаборнике двигателя.

![[19r99713.png]]

Рисунок 8, Конвертерная коробка EGTS.

Электронный модуль управления (ECM)

Для распознавания, передачи и интерпретации сигналов датчиков термопар необходима пересмотренная калибровка ECM. Подробный обзор новой калибровки ECM будет представлен в отдельном TSB. См. Технический бюллетень службы, Типы датчиков выхлопных газов (EGT) и Стратегия отбора, [[tsb210137 — Exhaust Gas Temperature (EGT) Sensor Types and Selection Strategy\|TSB210137]], для получения более подробной информации о новых калибровках ECM.

**Указания по обслуживанию**

Для двигателей, использующих термопару EGTS, требуется следующее оборудование:

- Совместимы ремни левобережья и правобережья основной проводов двигателя.
- Совместимые форсунки для электропроводки EGTS левого и правого берега.
- Левый берег и правый берег конвертерные коробки и крепежные скобки.
- Совместимые электронные калибровки модуля управления (ECM).

**Наличие сервисных деталей**

Сервисные детали доступны для заказа. См. таблицу 2 для номеров частей.

| Таблица 2, Части обслуживания |  |  |  |  |  |
|---|---|---|---|---|---|
| Часть описание | Существующий номер детали | устарелый | Заменённый | Новый номер детали | Количество на двигатель |
| Температура, датчик | 4326918 | Нет | Нет | [[5462023]] | 1 |
| [[5462024]] | 10 |  |  |  |  |
| [[5462025]] | 2 |  |  |  |  |
| [[5462026]] | 3 |  |  |  |  |
| Болт с неотделяемой шайбой | - | - | - | [[3609817]] | 16 |
| Болт с неотделяемой шайбой | - | - | - | [[3015283]] | 33 |
| Ремонтная втулка (износостойкая) | - | - | - | [[5539796]] | 16 |
| Скоба | - | - | - | [[4924291]] | 16 |
| Кронштейн датчика | - | - | - | [[5376160]] | 16 |
| Опора кронштейна | - | - | - | [[5376161]] | 16 |
| Кронштейн водяной трубки | - | - | - | [[5372025]] | 4 |
| LB Main Wiring Sweet - Промышленный | 3649114 | Нет | Нет | [[5538144]] | 1 |
| LB Main Wiring Grundage - Промышленный (LIEBHERR) | 3649235 | Нет | Нет | 5538740 | 1 |
| RB Main Wiring Sweet - Промышленный | 3645547 | Нет | Нет | [[5538145]] | 1 |
| LB форсунка/проводной упряжь EGTS | 5538957 | Нет | Нет | [[5538148]] | 2 |
| РБ форсунка/проводной упряжь EGTS | 5372878 | Нет | Нет | [[5538146]] | 2 |
| LB Главная / форсунка / электропроводка EGTS (AGGREKO) | 3650849 | Нет | Нет | 6416926 | 1 |
| RB Главная / форсунка / электропроводка EGTS (AGGREKO) | 2880749 | Нет | Нет | 6416933 | 1 |
| Схема электропроводки топливного фильтра (Off Engine) | 3643872 | Нет | Нет | 5538926 | 1 |
| Схема электропроводки топливного фильтра (на двигателе) | 3641274 | Нет | Нет | [[5538937]] | 1 |
| Квадрантная проводка упряжка Защитная кронштейн | - | - | - | [[5372029]] | 4 |
| Конвертерный ящик Mounting Bracket | - | - | - | [[5538108]] | 2 |
| Кронштейн датчика | - | - | - | [[5376160]] | 16 |
| Опора кронштейна | - | - | - | [[5376161]] | 16 |
| Аналоговые конверторные коробки | - | - | - | [[5572259]] | 2 |

**Совместимость частей**

Термопары EGTS **не** совместимы с обратной связью и  не могут быть смешаны с терморезистором EGTS на одном двигателе.

**Статус в производстве**

Внедрено в производство. См. таблицу 3.

| Таблица 3, Информация о производстве |  |  |
|---|---|---|
| ESN First | Постройте дату 1 | растение |
| 33222656 | 1 сентября 2020 года | Давентрийский моторный завод |
| 1 Дата сборки двигателя можно найти на табличке с данными двигателя. |  |  |

**Публикации затронуты**

| Таблица 4, Затронутые публикации |  |  |  |  |  |
|---|---|---|---|---|---|
| Тип ручного | Двигатель | Номер бюллетеня | Название процедуры | Процедура | Раздел |
| Руководство по обслуживанию | QSK50 CM2150 MCRS | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] | Преобразователь датчика температуры ОГ | [[122-019-450 — Exhaust Gas Temperature Sensor Converter\|См. процедуру 019-450]] | 19 |
| Руководство по обслуживанию | QSK50 CM2150 MCRS | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] | Датчик температуры отработавших газов | [[122-019-013 — Exhaust Temperature Sensor\|См. процедуру 019-013]] | 19 |

### История изменений документа

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3015283]] | CAPTIVE WASHER CAP SCREW | Болт с неотделяемой шайбой |
| [[3609817]] | CAPTIVE WASHER CAP SCREW | Болт с неотделяемой шайбой |
| [[3641274]] | ELECTRONIC CONTROL MODULE WIRING HARNESS | Жгут проводов блока управления |
| [[4326918]] | TEMPERATURE SENSOR | Датчик температуры |
| [[4924291]] | CLIP | Скоба |
| [[5372025]] | WATER TUBE BRACKET | Кронштейн водяной трубки |
| [[5372029]] | CABLE BRACKET | Кронштейн кабеля |
| [[5372878]] | ELECTRONIC CONTROL MODULE WIRING HARNESS | Жгут проводов блока управления |
| [[5376160]] | SENSOR BRACKET | Кронштейн датчика |
| [[5376161]] | BRACKET SUPPORT | Опора кронштейна |
| [[5462023]] | TEMPERATURE SENSOR | Датчик температуры |
| [[5462024]] | TEMPERATURE SENSOR | Датчик температуры |
| [[5462025]] | TEMPERATURE SENSOR | Датчик температуры |
| [[5462026]] | TEMPERATURE SENSOR | Датчик температуры |
| [[5538108]] | MODULE BRACKET | Кронштейн модуля |
| [[5538144]] | ELECTRONIC CONTROL MODULE WIRING HARNESS | Жгут проводов блока управления |
| [[5538145]] | ELECTRONIC CONTROL MODULE WIRING HARNESS | Жгут проводов блока управления |
| [[5538146]] | ELECTRONIC CONTROL MODULE WIRING HARNESS | Жгут проводов блока управления |
| [[5538148]] | ELECTRONIC CONTROL MODULE WIRING HARNESS | Жгут проводов блока управления |
| [[5538926]] | ELECTRONIC CONTROL MODULE WIRING HARNESS | Жгут проводов блока управления |
| [[5538937]] | ELECTRONIC CONTROL MODULE WIRING HARNESS | Жгут проводов блока управления |
| [[5538957]] | ELECTRONIC CONTROL MODULE WIRING HARNESS | Жгут проводов блока управления |
| [[5539796]] | WEAR SLEEVE | Ремонтная втулка (износостойкая) |
| [[5572259]] | ELECTRONIC INTERFACE MODULE | Электронный интерфейсный модуль |

> [!quote]- Original (English) · английский оригинал
> ## New Thermocouple Exhaust Gas Temperature Sensor (EGTS) Introduction
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - QSK50 CM2150 MCRS
> - QSK50 CM2150 K107
>
> **Issue**
>
> Symptom:
>
> - Exhaust gas temperature sensor (EGTS) Fault Codes: FC671, FC672, FC673, FC674, FC675, FC676, FC677, FC678, FC722, FC723, FC724, FC725, FC726, FC727, FC728, FC1521, FC1522, FC1523, FC1524, FC1525, FC1526, FC1527, FC1529, FC1532, FC1533, FC1534, FC1535, FC1536, FC1618, FC1619, FC2735, FC2736.
> - No reading or incorrect EGTS signal to engine control module (ECM).
>
> Root Cause:
>
> - The exhaust gas temperature sensor (EGTS) cable tensile strength capability has been exceeded due to the sensor cabling being exposed to high heat causing cable fracture.
> - Proximity of the EGTS to exhaust manifolds which have radiant temperature of greater than 400°C \[ 752°F \] causes the EGTS transition point (from the solid to the braid) to overheat and malfunction.
>
> Figure 1, EGTS Damage Examples.
>
> **Verification**
>
> - Visual inspection of the EGTS cable will show thermal damage to the EGTS's cable i.e. exposed bare wires, chaffing.
> - Use of a multimeter to measure across the terminals of the sensors results in extremely high resistance or open circuit.
> - Use of Cummins® electronic service tool or equivalent to confirm presence of any of the fault codes listed above.
>
> **Resolution**
>
> - New longer body thermocouple EGTS, which have higher working temperature capability around the exhaust manifold area, have been released. Service Parts Availability section below for part numbers.
> - Existing thermistor EGTS are **not** compatible with thermocouple EGTS. See Part Compatibility section below.
>
> **Description of Change**
>
> Existing Thermistor Exhaust Gas Temperature Sensors
>
> Figure 2, Existing EGTS Without Extended Body.
>
> New Thermocouple Exhaust Gas Temperature Sensors
>
> Four new thermocouple EGTS are required to properly route the sensors from the exhaust manifold and avoid interfering with other components such as water and exhaust manifolds, turbochargers, etc. at the top of engines. The inconel of the thermocouple EGTS has a higher temperature rating is much longer than the thermistor EGTS. The thermocouple EGTS have dark orange cables.
>
> Figure 3, New EGTS Routing.
>
> See Table 1 below to identify what EGTS part number is compatible with a cylinder location.
>
> | Table 1, EGTS Cylinder Locator |  |
> |---|---|
> | EGTS Part Number | Cylinder Number Locations |
> | [[5462023]] | 1 |
> | [[5462024]] | 2, 3, 4, 5, 6, 7, 10, 11, 12, 13 |
> | [[5462025]] | 8, 9 |
> | [[5462026]] | 14, 15, 16 |
>
> Figure 4, EGTS Part Number Locations by Cylinder.
>
> Compatible Left Bank and Right Bank Main Engine Wiring Harnesses
>
> The main engine wiring harnesses now have an additional converter box connector breakout. This can be found on both the Left Bank (LB) and Right Bank (RB) main engine wiring harnesses.
>
> Figure 5, EGTS Converter Box.
>
> Compatible Left Bank and Right Bank Injector/ EGTS Wiring Harnesses
>
> The internal wires of the injector/ EGTS harnesses have been changed to wires which support the new thermocouples. The wiring harness connectors have been combined to one single bigger connector which connects to the main engine wiring harnesses.
>
> Figure 6, New Wiring Harness Connections Points.
>
> Figure 7, New Wiring Harness Connections Points.
>
> Left Bank and Right Bank Converter Boxes and Mounting Brackets
>
> Two converter boxes are required to house and protect the internal signal conversion modules. The internal signal conversion modules process the thermocouple EGTS's signals for the engine's ECMs. Both LB and RB converter boxes are mounted on the air intake manifold of the engine.
>
> Figure 8, EGTS Converter Box.
>
> Electronic Control Module (ECM) Calibrations
>
> A revised ECM calibration is needed to recognize, transmit, and interpret the signals of the thermocouple sensors. A detail overview of the new ECM calibration will be covered in a separate TSB. See Technical Service Bulletin, Exhaust Gas Temperature (EGT) Sensor Types and Selection Strategy, [[tsb210137 — Exhaust Gas Temperature (EGT) Sensor Types and Selection Strategy\|TSB210137]], for more details on the new ECM calibrations.
>
> **Service Instructions**
>
> For engines to use the thermocouple EGTS, the following hardware is required:
>
> - Compatible left bank and right bank main engine harnesses.
> - Compatible left bank and right bank injector/ EGTS harnesses.
> - Left bank and right bank converter boxes and mounting brackets.
> - Compatible electronic control module (ECM) calibrations.
>
> **Service Parts Availability**
>
> Service parts are available. See Table 2 for part numbers.
>
> | Table 2, Service Parts |  |  |  |  |  |
> |---|---|---|---|---|---|
> | Part Description | Existing Part Number | Obsolete | Superseded | New Part Number | Quantity Per Engine |
> | Temperature, Sensor | [[4326918]] | No | No | [[5462023]] | 1 |
> | [[5462024]] | 10 |  |  |  |  |
> | [[5462025]] | 2 |  |  |  |  |
> | [[5462026]] | 3 |  |  |  |  |
> | Captive Washer Cap Screw | - | - | - | [[3609817]] | 16 |
> | Captive Washer Cap Screw | - | - | - | [[3015283]] | 33 |
> | Wear Sleeve | - | - | - | [[5539796]] | 16 |
> | Clip | - | - | - | [[4924291]] | 16 |
> | Sensor Bracket | - | - | - | [[5376160]] | 16 |
> | Bracket Support | - | - | - | [[5376161]] | 16 |
> | Water Tube Bracket | - | - | - | [[5372025]] | 4 |
> | LB Main Harness- Industrial | 3649114 | No | No | [[5538144]] | 1 |
> | LB Main Harness – Industrial (LIEBHERR) | 3649235 | No | No | 5538740 | 1 |
> | RB Main Harness - Industrial | 3645547 | No | No | [[5538145]] | 1 |
> | LB Injector/ EGTS Harness | [[5538957]] | No | No | [[5538148]] | 2 |
> | RB Injector/ EGTS Harness | [[5372878]] | No | No | [[5538146]] | 2 |
> | LB Main / Injector / EGTS Harness (AGGREKO) | 3650849 | No | No | 6416926 | 1 |
> | RB Main / Injector / EGTS Harness (AGGREKO) | 2880749 | No | No | 6416933 | 1 |
> | Fuel Filter Harness (Off Engine) | 3643872 | No | No | [[5538926]] | 1 |
> | Fuel Filter Harness (On Engine) | [[3641274]] | No | No | [[5538937]] | 1 |
> | Quadrant Harness Protection Bracket | - | - | - | [[5372029]] | 4 |
> | Convertor Box Mounting Bracket | - | - | - | [[5538108]] | 2 |
> | Sensor Bracket | - | - | - | [[5376160]] | 16 |
> | Bracket Support | - | - | - | [[5376161]] | 16 |
> | Analog Convertor Box | - | - | - | [[5572259]] | 2 |
>
> **Part Compatibility**
>
> Thermocouple EGTS are **not** backwards compatible and are **not** able to be mixed with the thermistor EGTS on the same engine.
>
> **Production Status**
>
> Implemented for production. See Table 3.
>
> | Table 3, Production Information |  |  |
> |---|---|---|
> | ESN First | Build Date 1 | Plant |
> | 33222656 | 1 September 2020 | Daventry Engine Plant |
> | 1 Engine build date can be found on engine dataplate. |  |  |
>
> **Publications Affected**
>
> | Table 4, Publications Affected |  |  |  |  |  |
> |---|---|---|---|---|---|
> | Manual Type | Engine | Bulletin Number | Procedure Title | Procedure | Section |
> | Service Manual | QSK50 CM2150 MCRS | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] | Exhaust Gas Temperature Sensor Converter | [[122-019-450 — Exhaust Gas Temperature Sensor Converter\|Refer to Procedure 019-450]] | 19 |
> | Service Manual | QSK50 CM2150 MCRS | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] | Exhaust Temperature Sensor | [[122-019-013 — Exhaust Temperature Sensor\|Refer to Procedure 019-013]] | 19 |
>
> ### Document History
