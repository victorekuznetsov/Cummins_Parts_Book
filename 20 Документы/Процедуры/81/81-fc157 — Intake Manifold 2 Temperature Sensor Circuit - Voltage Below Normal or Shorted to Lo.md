---
aliases:
  - "Цепь датчика температуры коллектора 2 — напряжение ниже нормы"
type: "Процедура"
doc: "81-fc157"
title_en: "Intake Manifold 2 Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика температуры коллектора 2 — напряжение ниже нормы"
modified: "2018-10-15"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc157.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc157.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Intake Manifold 2 Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика температуры коллектора 2 — напряжение ниже нормы**

> [!abstract] Процедура · `81-fc157`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc157.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc157.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 157

### Цепь датчика температуры коллектора 2 — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 157 PID (P): 105 SPN: 1131 FMI: 4 лампы: Желтая СТО: 00-697 | Цепь датчика температуры коллектора 2 — напряжение ниже нормы. Низкое напряжение, обнаруженное на сигнальном контакте-06 основной проводов ремня управления двигателем (ECM) разъема. | Код 158 неисправности отключен. |

![[19800776.png]]

Схема датчика температуры Manifold 2

### Описание цепи

Датчик температуры впускного коллектора 2 обеспечивает сигнал температуры воздуха в левом заднем коллекторе впуска для CENSETM ECM.

### Расположение компонента

Датчик температуры впускного коллектора 2 расположен на левобережном заднем впускном коллекторе. Датчик расположен ниже по течению от послеохладителя.

### Практические замечания

Сопротивление датчика варьируется в зависимости от температуры. Считывание, которое вы наблюдаете, должно быть сопоставимо со следующей таблицей, если датчик работает должным образом.

| температура | температура | Сопротивление |
|---|---|---|
| (°C) | (°F) | (Омс) |
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

См. Код устранения неполадок t05-157.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 157
>
> ### Intake Manifold 2 Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 157 PID(P): 105 SPN: 1131 FMI: 4 Lamp: Yellow SRT: 00-697 | Intake Manifold 2 Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source. Low voltage detected on SIGNAL pin-06 of the main harness A engine control module (ECM) connector. | Fault Code 158 is disabled. |
>
> Intake Manifold 2 Temperature Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold 2 temperature sensor provides the left bank rear intake manifold air temperature signal to the CENSE™ ECM.
>
> ### Component Location
>
> The intake manifold 2 temperature sensor is located on the left bank rear intake manifold. The sensor is located downstream of the aftercooler.
>
> ### Shoptalk
>
> The resistance of the sensor varies with temperature. The reading that you observe should compare to the following table if the sensor is functioning properly.
>
> | Temperature | Temperature | Resistance |
> |---|---|---|
> | (°C) | (°F) | (ohms) |
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> Refer to Troubleshooting Fault Code t05-157.
