---
aliases:
  - "Цепь датчика температуры воздуха коллектора — напряжение ниже нормы"
type: "Процедура"
doc: "07-fc154"
title_en: "Intake Manifold Air Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика температуры воздуха коллектора — напряжение ниже нормы"
modified: "2012-12-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc154.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc154.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Intake Manifold Air Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика температуры воздуха коллектора — напряжение ниже нормы**

> [!abstract] Процедура · `07-fc154`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc154.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc154.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 154

### Цепь датчика температуры воздуха коллектора — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 154 PID(P): P105 SPN: 105 FMI: 4 лампы: Янтарная СРТ: | Цепь датчика температуры воздуха коллектора — напряжение ниже нормы. | Отсутствие защиты двигателя от сбоев цепи или датчика. |

![[19900359.png]]

Схема датчика температуры воздуха Manifold Air Temperature Sensor Circuit

### Описание цепи

Датчик температуры впускного коллектора используется электронным модулем управления (ECM) для мониторинга температуры воздуха в впускном коллекторе после охладителя. Датчик температуры впускного коллектора используется ECM для системы защиты двигателя, управления временем и заправкой.

### Расположение компонента

Справочный раздел E для подробного описания местоположения компонента. Датчик температуры впускного коллектора расположен в впускном коллекторе в задней части двигателя.

### Практические замечания

Сопротивление всех датчиков температуры изменяется в зависимости от температуры. Наблюдаемое считывание должно быть сопоставимо со следующей таблицей, если датчик работает должным образом.

| Температура (°F) | Температура (°C) | Сопротивление (Омс) |
|---|---|---|
| 32 | 0 | 30k до 36k |
| 77 | 25 | 9k до 11k |
| 122 | 50 | 3k - 4k |
| 167 | 75 | 1350—1500 |
| 212 | 100 | 600-675 |

Устранение неполадок код t05-154


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 154
>
> ### Intake Manifold Air Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 154 PID(P): P105 SPN: 105 FMI: 4 Lamp: Amber SRT: | Intake manifold air temperature sensor circuit - voltage below normal or shorted to low source. | No engine protection for circuit or sensor failure. |
>
> Intake Manifold Air Temperature Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the air in the intake manifold after the aftercooler. The intake manifold temperature sensor is used by the ECM for the engine protection system, timing, and fueling control.
>
> ### Component Location
>
> Reference Section E for a detailed component location view. The intake manifold temperature sensor is located in the intake manifold at the rear of the engine.
>
> ### Shoptalk
>
> The resistance of all the temperature sensors varies with the temperature. The reading observed should compare to the following table if the sensor is functioning properly.
>
> | Temperature (°F) | Temperature (°C) | Resistance (ohms) |
> |---|---|---|
> | 32 | 0 | 30k to 36k |
> | 77 | 25 | 9k to 11k |
> | 122 | 50 | 3k to 4k |
> | 167 | 75 | 1350 to 1500 |
> | 212 | 100 | 600 to 675 |
>
> Refer to Troubleshooting Fault Code t05-154
