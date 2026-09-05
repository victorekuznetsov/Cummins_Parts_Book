---
aliases:
  - "Цепь датчика температуры масла 1 — напряжение ниже нормы"
type: "Процедура"
doc: "81-fc213"
title_en: "Engine Oil Temperature Sensor 1 Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика температуры масла 1 — напряжение ниже нормы"
modified: "2015-07-07"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc213.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc213.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Engine Oil Temperature Sensor 1 Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика температуры масла 1 — напряжение ниже нормы**

> [!abstract] Процедура · `81-fc213`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc213.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc213.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 213

### Цепь датчика температуры масла 1 — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 213 P(P): 175 SPN: 175 ФМИ: 4 лампы: Желтая СТО: 00-502 | Цепь датчика температуры масла 1 — напряжение ниже нормы. Низкое напряжение, обнаруженное на контакте SIGNAL 35 основной проводов ремня разъема A ECM. | Код 214 неисправности отключен. |

![[19802518.png]]

Цепь датчика температуры масла

### Описание цепи

Схема датчика температуры масла обеспечивает сигнал температуры масла к ECM. Сопротивление датчика температуры масла изменяется с температурой. ECM обнаруживает изменение сопротивления датчика температуры масла, контролируя напряжение на внутреннем резисторе, который последовательно с датчиком температуры масла. Изменение напряжения на внутреннем резисторе переводится в изменение температуры.

### Расположение компонента

Датчик температуры масла расположен на правой стороне масляной панели.

### Практические замечания

- Сопротивление датчика изменяется в зависимости от температуры. Считывание, которое вы наблюдаете, должно быть сопоставимо со следующей таблицей, если датчик работает должным образом.

| температура | температура | Сопротивление |
|---|---|---|
| (°C) | (°F) | (Омс) |
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

См. Код устранения неполадок t05-213


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 213
>
> ### Engine Oil Temperature Sensor 1 Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 213 PID(P): 175 SPN: 175 FMI: 4 Lamp: Yellow SRT: 00-502 | Engine Oil Temperature Sensor 1 Circuit - Voltage Below Normal or Shorted to Low Source. Low voltage detected on SIGNAL pin 35 of the main harness A ECM connector. | Fault Code 214 is disabled. |
>
> Oil Temperature Sensor Circuit
>
> ### Circuit Description
>
> The oil temperature sensor circuit provides the oil temperature signal to the ECM. The resistance of the oil temperature sensor varies with temperature. The ECM detects the change in resistance of the oil temperature sensor by monitoring the voltage across an internal resistor that is in series with the oil temperature sensor. The change in voltage across the internal resistor is translated into a temperature change.
>
> ### Component Location
>
> The oil temperature sensor is located on the right side of the oil pan.
>
> ### Shoptalk
>
> - The resistance of the sensor varies with the temperature. The reading that you observe should compare to the following table if the sensor is functioning properly.
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
> Refer to Troubleshooting Fault Code t05-213
