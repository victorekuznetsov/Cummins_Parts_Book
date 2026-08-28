---
aliases:
  - "Цепь датчика температуры масла"
type: "Процедура"
doc: "87-fc213"
title_en: "Oil Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры масла"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc213.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc213.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Oil Temperature Sensor Circuit
**Цепь датчика температуры масла**

> [!abstract] Процедура · `87-fc213`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc213.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc213.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 213

### Цепь датчика температуры масла

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 213 P(P): P175 SPN: 175 ФМИ: 4 лампы: Желтая СТО: | Низкое напряжение, обнаруженное при температуре масла, сигнализирует контакт 35 проводов двигателя. | Электронный модуль управления (ECM) не выполняет никаких действий. |

![[19802862.png]]

Цепь датчика температуры масла

### Описание цепи

Датчик температуры масла контролирует температуру масла и передает информацию в ECM через электропроводку двигателя.

### Расположение компонента

Датчик температуры масла расположен в масляной панели на левой стороне двигателя. Датчик температуры масла * присутствует только на двигателях с CENSETM.

### Практические замечания

Сопротивление датчика изменяется в зависимости от температуры. Сравните показания, которые вы наблюдаете, со следующей таблицей, если датчик работает должным образом.

| Температура (°C) | Температура \[°F\] | Сопротивление (Омс) |
|---|---|---|
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

См. Код устранения неполадок t05-213


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 213
>
> ### Oil Temperature Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 213 PID(P): P175 SPN: 175 FMI: 4 Lamp: Yellow SRT: | Low voltage detected at the oil temperature signal pin 35 of the engine harness. | No action is taken by the electronic control module (ECM). |
>
> Oil Temperature Sensor Circuit
>
> ### Circuit Description
>
> The oil temperature sensor monitors oil temperature and passes information to the ECM through the engine harness.
>
> ### Component Location
>
> The oil temperature sensor is located in the oil pan on the left side of the engine. The oil temperature sensor is **only** present on engines with CENSE™.
>
> ### Shoptalk
>
> The resistance of the sensor varies with the temperature. Compare the reading you observe to the following table if the sensor is functioning properly.
>
> | Temperature (°C) | Temperature \[°F\] | Resistance (ohms) |
> |---|---|---|
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> Refer to Troubleshooting Fault Code t05-213
