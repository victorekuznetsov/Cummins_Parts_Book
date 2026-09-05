---
aliases:
  - "Цепь датчика температуры масла"
type: "Процедура"
doc: "82-fc212"
title_en: "Oil Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры масла"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc212.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc212.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Oil Temperature Sensor Circuit
**Цепь датчика температуры масла**

> [!abstract] Процедура · `82-fc212`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc212.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc212.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 212

### Цепь датчика температуры масла

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 212 P(P): P175 SPN: 175 ФМИ: 3/3 лампы: Желтая СТО: | Высокое напряжение, обнаруженное в цепи температуры масла. | Отсутствие защиты двигателя от температуры масла. |

![[19c00506.png]]

Цепь датчика температуры масла

### Описание цепи

Датчик давления/температуры масла используется электронным модулем управления (ECM) для контроля температуры моторного масла. Если температура масла становится слишком высокой и включена защита двигателя, может возникнуть ухудшение состояния, что может привести к отключению.

### Расположение компонента

Датчик давления/температуры масла расположен на блоке двигателя слева от топливного фильтра, позади воздушного компрессора.

### Практические замечания

Сопротивление датчика варьируется в зависимости от температуры. Сравните свои показания с этой таблицей:

| Температура (°C) | Температура \[°F\] | Сопротивление (Омс) |
|---|---|---|
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

См. Код устранения неполадок t05-212


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 212
>
> ### Oil Temperature Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 212 PID(P): P175 SPN: 175 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at the oil temperature circuit. | No engine protection for oil temperature. |
>
> Oil Temperature Sensor Circuit
>
> ### Circuit Description
>
> The oil pressure/temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine oil. If the oil temperature becomes too high and the engine protection is enabled, a derate condition can be incurred, possibly leading to shutdown.
>
> ### Component Location
>
> The oil pressure/temperature sensor is located on the engine block to the left of the fuel filter, behind the air compressor.
>
> ### Shoptalk
>
> Sensor resistance varies with temperature. Compare your reading to this table:
>
> | Temperature (°C) | Temperature \[°F\] | Resistance (ohms) |
> |---|---|---|
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> Refer to Troubleshooting Fault Code t05-212
