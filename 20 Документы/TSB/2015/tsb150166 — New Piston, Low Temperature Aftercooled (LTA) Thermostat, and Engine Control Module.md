---
type: "TSB"
doc: "tsb150166"
title_en: "New Piston, Low Temperature Aftercooled (LTA) Thermostat, and Engine Control Module (ECM) Calibrations for Haul Trucks Operating at High Altitude."
modified: "2015-12-14"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
parts:
  - "3645958"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150166.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150166.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60"
  - "перевод/машинный"
---

# New Piston, Low Temperature Aftercooled (LTA) Thermostat, and Engine Control Module (ECM) Calibrations for Haul Trucks Operating at High Altitude.

> [!abstract] TSB · `tsb150166`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Даты:** изменён 2015-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150166.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150166.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Новый термостат с низким температурным охлаждением (LTA) и калибровка модуля управления двигателем (ECM) для грузовых автомобилей, работающих на большой высоте.

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- QSK60 CM500 (**Только** 2-ступенчатые грузовые автомобили, работающие на высоте около 2590 метров \[8500 футов \] или выше)

**Описание изменения**

В этом документе сообщается о выпуске:

- Пистон с высоким коэффициентом сжатия
- Новый термостат с низкой температурой после охлаждения (LTA)
- Новый модуль управления двигателем (ECM) калибровки с алгоритмом высокогорья (HATA)

Высокое сжатие поршня:

- Это существующая часть, которая в настоящее время структурирована в сборки для двигателей, работающих выше 2590 метров [8500 футов].
- Соотношение сжатия изменяется с 14,5:1 на стандартном поршне до 16,0:1 на поршне с высоким коэффициентом сжатия.
- Помогает контролировать горение на высоте и уменьшить аномальные события стрельбы и пики высокого давления цилиндров

Новый термостат с низкой температурой послеохладителя (LTA):

- Имеет более высокую полностью открытую температуру по сравнению с существующей частью.
- Полностью открытая температура увеличилась с 57 ° C \[134 ° F \] до 68 ° C \[154 ° F \]

Новый модуль управления двигателем (ECM) калибровки с алгоритмом высокогорья (HATA):

- Регулирует время заправки в зависимости от высоты
- Поддерживает давление в цилиндре на стабильном уровне, а также имеет небольшие преимущества в эффективности использования топлива.
- Изменения других таблиц заправки для уменьшения аномального сгорания

**Причина изменения**

Эти изменения были сделаны для уменьшения аномальных событий сгорания для 2-ступенчатых грузовых автомобилей, работающих на высоте около 2590 метров [8500 футов] или выше.

**Указания по обслуживанию**

Для 2-ступенчатых грузовых автомобилей, работающих на высоте около 2590 метров [8500 футов] или выше, Cummins Inc. рекомендует установить следующее:

- Новые поршни с высоким сжатием, номер детали 3640513

- Новые термостаты LTA, номер детали 4381506

- Соответствующая калибровка ECM с помощью алгоритма высокогорья (HATA)
- После того, как двигатель будет оснащен новыми поршнями высокого сжатия и калибровкой алгоритма высокого времени (HATA), двигатель будет работать с другим списком контрольных частей (CPL) и рейтингом FR, чем указано на табличке данных двигателя. Это означает, что новый табличный знак должен быть заказан и установлен на двигателе.

Подробное руководство по установке компонентов см. в таблице 1 ниже.

| Таблица 1, Руководство по установке компонентов |  |  |  |  |  |
|---|---|---|---|---|---|
| Сценарий установки | Пистон с высоким сжатием | LTA Thermostat | Калибровка ECM | высота | Заметки об установке |
| 1 | x | x | x | Выше 2590 метров[8500 футов] | **Всегда** Рекомендуемый |
| 2 | x |  | x | Выше 2590 метров[8500 футов] | Не рекомендуется, но разрешено |
| 3 |  |  | x | Выше 2590 метров[8500 футов] | Не допускается |
| 4 | x |  | x | Ниже 2590 метров[8500 футов] | Не допускается |
| 5 |  |  | x | Ниже 2590 метров[8500 футов] | Не допускается |
| 6 |  | x |  | Любой | Не рекомендуется, но разрешено |
| 7 | x |  |  | Ниже 2590 метров[8500 футов] | Не допускается |
| 8 | x | x |  | Выше 2590 метров[8500 футов] | Не рекомендуется, но разрешено |
| 9 | x | x |  | Ниже 2590 метров[8500 футов] | Не допускается |
| 10 | x |  |  | Выше 2590 метров[8500 футов] | Не рекомендуется, но разрешено |

Сценарий установки Примечание:

1. **Всегда** Рекомендуем: Cummins Inc. Рекомендует, чтобы все три компонента были установлены вместе, чтобы эффективно уменьшить аномальные события горения.

2. Не рекомендуется, но разрешено: Новый термостат LTA будет особенно эффективен в холодном климате и остановит распад температуры впускного коллектора. Низкий уровень

Многообразные температуры могут вызвать аномальное горение.

3. Не допускается: Калибровка ECM с помощью алгоритма высокогорья (HATA) может быть использована с двигателями, работающими на стандартных поршнях на высотах более 2590 метров [8500 футов ]. Однако эти двигатели не смогут контролировать горение, и все еще могут вызывать звон в поршневых кольцах.

> [!warning] ОСТОРОЖНО
> Новая калибровка ECM с помощью алгоритма высокого алгоритма определения времени (HATA) должна использоваться только в сочетании с новым высоким коэффициентом сжатия поршня или повреждением двигателя.

4. Не допускается: Если калибровка ECM с помощью алгоритма высокогорья (HATA) используется на двигателях, работающих ниже 2590 метров [8500 футов], двигатель войдет в состояние выбоя.

5. Не допускается: Если калибровка ECM с помощью алгоритма высокогорья (HATA) используется на двигателях, работающих ниже 2590 метров [8500 футов], двигатель войдет в состояние выбоя.

6. Не рекомендуется, но разрешено: Новый термостат LTA будет особенно эффективен в холодном климате и остановит распад температуры впускного коллектора. Низкий уровень

Многообразные температуры могут вызвать аномальное горение.

7. Не допускается: Если работать на высоте ниже 3658 метров[12 000 футов], двигатель с высоким коэффициентом сжатия поршней и невысотной калибровкой синхронизации (HATA) может превышать пределы давления цилиндра и может привести к повреждению двигателя.

8. Не рекомендуется, но разрешено: Cummins Inc. Настоятельно рекомендуется, чтобы калибровка ECM с помощью алгоритма высокого алгоритма синхронизации (HATA) не использовалась, если двигатель не имеет установленных поршней с высоким коэффициентом сжатия. Также меньше контроля над давлением цилиндров на всех рабочих высотах.

9. Не допускается:

> [!warning] ОСТОРОЖНО
> Новые поршни с высоким коэффициентом сжатия не должны использоваться на двигателях, работающих ниже 2590 метров [8500 футов], поскольку это будет означать, что двигатели будут превышать пределы давления цилиндра и могут привести к повреждению двигателя.

10. Не рекомендуется, но разрешено: Cummins Inc. Настоятельно рекомендуется, чтобы калибровка ECM с помощью алгоритма высокого алгоритма синхронизации (HATA) не использовалась, если двигатель не имеет установленных поршней с высоким коэффициентом сжатия. Также меньше контроля над давлением цилиндров на всех рабочих высотах. Новый термостат LTA может использоваться на двигателях, работающих на всех высотах. Новый термостат LTA будет особенно эффективен в холодном климате и остановит распад температуры впускного коллектора. Низкий уровень

Многообразные температуры могут вызвать аномальное горение

**Наличие сервисных деталей**

Сервисные детали доступны для заказа. См. таблицу 2 ниже.

| **Таблица 2, Части обслуживания** |  |  |  |
|---|---|---|---|
| **Часть описания** | **Предыдущее число частей** | **Новый номер** | **Количество** |
| Поршень | [[3645958]]или 3640474 | 3640513 (продается в комплекте 4955783) | 16 на двигатель |
| LTA Thermostat | 4065566 | 4381506 | 2 для двигателя |

Выпущено девять новых калибровок ECM с функцией алгоритма высокогорья (HATA) и изменениями таблицы времени. См. таблицу 3 ниже.

- Семь калибровок ECM сертифицированы на уровень выбросов Tier1.
- Две дополнительные калибровки ECM являются несертифицированными калибровками, оптимизированными для топлива. Эти новые калибровки потребовали выпуска новых вариантов DO, SC и FC для этих двигателей.
- Правильная калибровка ECM, которая соответствует уровню выбросов в стране, в которой работает установка, должна быть установлена.

| **Таблица 3, Модуль управления двигателем (ECM) Калибровки и опции** |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Существующие калибровки и варианты** | **Новые калибровки и опции** |  |  |  |  |  |  |  |  |  |  |
| **Предыдущий код ECM** | **Существующий вариант СК** | **Существующий вариант** | **Существующий вариант ФК** | **FR Вариант** | **Сертификация** | **Новый код ECM** | **Новый вариант СК** | **Новый вариант** | **Новый вариант ФК** | **FR Вариант** | **Сертификация** |
| D60559.02 | SC61622 | ДО 60786 | FCWD86 | FR60259 | Уровень 1 | D60693,00 | SC61738 | ДО60904 | FCWH05 | FR60259 | Уровень 1 |
| D60684.01 | SC61668 | ДО60831 | FCWF68 | FR60259 | D60694,00 | SC61739 | ДО 60905 | FCWH06 | FR60259 |  |  |
| D60685.01 | SC61689 | ДО60853 | FCWF77 | FR60259 | D60695,00 | SC61740 | ДО 60906 | FCWH07 | FR60259 |  |  |
| D60560.02 | SC61623 | ДО 60787 | FCWD87 | FR60260 | D60696,00 | SC61741 | ДО60907 | FCWH08 | FR60260 |  |  |
| D60676.01 | SC61660 | ДО 60823 | FCWF63 | FR60260 | D60697,00 | SC61742 | ДО60908 | FCWH09 | FR60260 |  |  |
| D60683.01 | SC61667 | ДО 60830 | FCWF67 | FR60260 | D60698,00 | SC61743 | ДО 60909 | FCWH10 | FR60260 |  |  |
| D60686.01 | SC61690 | ДО60854 | FCWF78 | FR60260 | D60699,00 | SC61744 | ДО 60910 | FCWH11 | FR60260 |  |  |
| D60561.02 | SC61624 | ДО 60789 | FCWD88 | FR60267 | Несертифицированное топливо оптимизировано | D60700,00 | SC61745 | ДО 60911 | FCWH12 | FR60267 | Несертифицированное топливо оптимизировано |
| D60562.02 | SC61625 | ДО 60790 | FCWD89 | FR60268 | Несертифицированное топливо оптимизировано | D60701,00 | SC61746 | 60912 | FCWH13 | FR60268 | Несертифицированное топливо оптимизировано |

**Совместимость частей**

Новый поршень с высоким сжатием и термостат LTA обратно совместимы.

**Идентификация детали**

Высокое сжатие поршня имеет более мелкую поршневую чашу по сравнению со стандартным поршнем.

### История изменений документа

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3645958]] | Engine Piston | Поршень двигателя |

> [!quote]- Original (English) · английский оригинал
> ## New Piston, Low Temperature Aftercooled (LTA) Thermostat, and Engine Control Module (ECM) Calibrations for Haul Trucks Operating at High Altitude.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - QSK60 CM500 (**Only** 2-Stage Haul Trucks Operating at Approximately 2590 Meters \[ 8500 Feet \] or Above)
>
> **Description of Change**
>
> This document announces the release of:
>
> - High compression ratio piston
> - New low temperature aftercooled (LTA) circuit thermostat
> - New engine control module (ECM) calibrations with high altitude timing algorithm (HATA)
>
> High compression ratio piston:
>
> - Is an existing part that is now being structured into builds for engines operating above 2590 meters \[ 8500 feet \]
> - The compression ratio changes from 14.5:1 on the standard piston to 16.0:1 on the high compression ratio piston
> - Helps to control combustion at altitude and reduce abnormal firing events and high cylinder pressure spikes
>
> New low temperature aftercooler (LTA) circuit thermostat:
>
> - Has a new higher fully open temperature as compared to the existing part
> - Fully open temperature has increased from 57°C \[ 134°F \] to 68°C \[ 154°F \]
>
> New engine control module (ECM) calibrations with high altitude timing algorithm (HATA):
>
> - Adjusts the fueling timing depending on the altitude
> - Keeps cylinder pressure at a consistent level and also has small fuel efficiency benefits
> - Changes other fueling tables to reduce abnormal combustion
>
> **Reason for Change**
>
> These changes have been made to reduce abnormal combustion events for 2-stage haul trucks operating at approximately 2590 meters \[ 8500 feet \] or above.
>
> **Service Instructions**
>
> For 2-stage haul trucks operating at approximately 2590 meters \[ 8500 feet \] or above, Cummins Inc. recommends the installation of the following:
>
> - New high compression pistons, Part Number 3640513
>
> - New LTA thermostats, Part Number 4381506
>
> - Corresponding ECM calibration with high altitude timing algorithm (HATA) feature
> - Once an engine has the new high compression pistons and high altitude timing algorithm (HATA) calibration installed, the engine will be operating with a different control parts list (CPL) and FR rating from that specified on the engine dataplate. This means that a new dataplate **must** be ordered and installed on the engine.
>
> For a detailed component installation recommendation guide, see Table 1 below.
>
> | Table 1, Component Installation Recommendation Guide |  |  |  |  |  |
> |---|---|---|---|---|---|
> | Installation Scenario | High Compression Piston | LTA Thermostat | ECM Calibration | Altitude | Installation Notes |
> | 1 | x | x | x | Above 2590 meters \[ 8500 feet \] | **Always** recommended |
> | 2 | x |  | x | Above 2590 meters \[ 8500 feet \] | **Not** recommended but allowed |
> | 3 |  |  | x | Above 2590 meters \[ 8500 feet \] | **Not** allowed |
> | 4 | x |  | x | Below 2590 meters \[ 8500 feet \] | **Not** allowed |
> | 5 |  |  | x | Below 2590 meters \[ 8500 feet \] | **Not** allowed |
> | 6 |  | x |  | Any | **Not** recommended but allowed |
> | 7 | x |  |  | Below 2590 meters \[ 8500 feet \] | **Not** allowed |
> | 8 | x | x |  | Above 2590 meters \[ 8500 feet \] | **Not** recommended but allowed |
> | 9 | x | x |  | Below 2590 meters \[ 8500 feet \] | **Not** allowed |
> | 10 | x |  |  | Above 2590 meters \[ 8500 feet \] | **Not** recommended but allowed |
>
> Installation Scenario Notes:
>
> 1. **Always** recommended: Cummins Inc. recommends that all three components are installed together to effectively reduce abnormal combustion events.
>
> 2. **Not** recommended but allowed: The new LTA circuit thermostat will be particularly effective in cold climates, and will stop the decay of intake manifold temperatures. Low intake
>
> manifold temperatures can cause abnormal combustion.
>
> 3. **Not** allowed: The ECM calibration with the high altitude timing algorithm (HATA) feature can be used with engines running standard pistons at altitudes over 2590 meters \[ 8500 feet \]. However, these engines will not be able to control combustion as well, and may still inducing ringing in the piston rings.
>
> **CAUTION · Осторожно**
> The new ECM calibration with the high altitude timing algorithm (HATA) should only be used in tandem with the new high compression ratio piston or engine damage can result.
>
> 4. **Not** allowed: If the ECM calibration with the high altitude timing algorithm (HATA) feature is used on engines operating below 2590 meters \[ 8500 feet \] the engine will enter a derate state.
>
> 5. **Not** allowed: If the ECM calibration with the high altitude timing algorithm (HATA) feature is used on engines operating below 2590 meters \[ 8500 feet \] the engine will enter a derate state.
>
> 6. **Not** recommended but allowed: The new LTA circuit thermostat will be particularly effective in cold climates, and will stop the decay of intake manifold temperatures. Low intake
>
> manifold temperatures can cause abnormal combustion.
>
> 7. **Not** allowed: If operating at an altitude lower than 3658 meters \[12,000 feet \], an engine with the high compression ratio pistons and non high altitude timing algorithm (HATA) calibration could exceed cylinder pressure limits and engine damage can result.
>
> 8. **Not** recommended but allowed: Cummins Inc. strongly recommends that the ECM calibration with the high altitude timing algorithm (HATA) feature is **not** used unless the engine has the high compression ratio pistons installed. There is also less control over cylinder pressure at all operating heights.
>
> 9. **Not** allowed:
>
> **CAUTION · Осторожно**
> The new high compression ratio pistons are not to be used on engines operating below 2590 meters \[8500 feet\] as this will mean the engines will exceed the cylinder pressure limits, and could cause damage to the engine.
>
> 10. **Not** recommended but allowed: Cummins Inc. strongly recommends that the ECM calibration with the high altitude timing algorithm (HATA) feature is **not** used unless the engine has the high compression ratio pistons installed. There is also less control over cylinder pressure at all operating heights. The new LTA circuit thermostat can be used on engines operating at all altitudes. The new LTA circuit thermostat will be particularly effective in cold climates, and will stop the decay of intake manifold temperatures. Low intake
>
> manifold temperatures can cause abnormal combustion
>
> **Service Parts Availability**
>
> Service parts are available. See Table 2 below.
>
> | **Table 2, Service Parts** |  |  |  |
> |---|---|---|---|
> | **Part Description** | **Previous Part Number** | **New Part Number** | **Quantity** |
> | Piston | [[3645958]] or 3640474 | 3640513 (Sold in Service Kit 4955783) | 16 per engine |
> | LTA Thermostat | 4065566 | 4381506 | 2 per engine |
>
> Nine new ECM calibrations have been released with the high altitude timing algorithm (HATA) feature and timing table changes. See Table 3 below.
>
> - Seven of the ECM calibrations are certified for the Tier1 emissions level.
> - The additional two ECM calibrations are non-certified fuel optimized calibrations. These new calibrations necessitated the release new DO, SC, and FC options for these engines.
> - The correct ECM calibration, that meets the emissions level of the country the unit is operating in, **must** be installed.
>
> | **Table 3, Engine Control Module (ECM) Calibrations and Options** |  |  |  |  |  |  |  |  |  |  |  |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> | **Existing Calibrations and Options** | **New Calibrations and Options** |  |  |  |  |  |  |  |  |  |  |
> | **Previous ECM Code** | **Existing SC Option** | **Existing DO Option** | **Existing FC Option** | **FR Option** | **Certification** | **New ECM Code** | **New SC Option** | **New DO Option** | **New FC Option** | **FR Option** | **Certification** |
> | D60559.02 | SC61622 | DO60786 | FCWD86 | FR60259 | Tier 1 | D60693.00 | SC61738 | DO60904 | FCWH05 | FR60259 | Tier 1 |
> | D60684.01 | SC61668 | DO60831 | FCWF68 | FR60259 | D60694.00 | SC61739 | DO60905 | FCWH06 | FR60259 |  |  |
> | D60685.01 | SC61689 | DO60853 | FCWF77 | FR60259 | D60695.00 | SC61740 | DO60906 | FCWH07 | FR60259 |  |  |
> | D60560.02 | SC61623 | DO60787 | FCWD87 | FR60260 | D60696.00 | SC61741 | DO60907 | FCWH08 | FR60260 |  |  |
> | D60676.01 | SC61660 | DO60823 | FCWF63 | FR60260 | D60697.00 | SC61742 | DO60908 | FCWH09 | FR60260 |  |  |
> | D60683.01 | SC61667 | DO60830 | FCWF67 | FR60260 | D60698.00 | SC61743 | DO60909 | FCWH10 | FR60260 |  |  |
> | D60686.01 | SC61690 | DO60854 | FCWF78 | FR60260 | D60699.00 | SC61744 | DO60910 | FCWH11 | FR60260 |  |  |
> | D60561.02 | SC61624 | DO60789 | FCWD88 | FR60267 | Non Certified Fuel Optimised | D60700.00 | SC61745 | DO60911 | FCWH12 | FR60267 | Non Certified Fuel Optimised |
> | D60562.02 | SC61625 | DO60790 | FCWD89 | FR60268 | Non Certified Fuel Optimised | D60701.00 | SC61746 | DO60912 | FCWH13 | FR60268 | Non Certified Fuel Optimised |
>
> **Part Compatibility**
>
> The new high compression piston and LTA thermostat are backwards compatible.
>
> **Part Identification**
>
> The high compression ratio piston has a shallower piston bowl when compared to the standard piston.
>
> ### Document History
