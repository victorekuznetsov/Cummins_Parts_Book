---
aliases:
  - "Цепь датчика температуры во впускном коллекторе"
type: "Процедура"
doc: "82-fc153"
title_en: "Intake Manifold Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры во впускном коллекторе"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc153.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc153.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Intake Manifold Temperature Sensor Circuit
**Цепь датчика температуры во впускном коллекторе**

> [!abstract] Процедура · `82-fc153`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc153.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc153.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 153

### Цепь датчика температуры во впускном коллекторе

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 153 P(P): P105 SPN: 105 FMI: 3/3 лампы: Желтая СТО: | Высокое напряжение, обнаруженное на цепи датчика температуры впускного коллектора. | Возможен белый дым. Вентилятор будет оставаться включенным, если он контролируется электронным модулем управления (ECM). Отсутствие защиты двигателя от температуры впускного коллектора. |

![[19200139.png]]

Цепь датчика температуры во впускном коллекторе

### Описание цепи

Датчик температуры впускного коллектора используется ECM для мониторинга температуры воздуха впускного отверстия двигателя. Впускной сигнал температуры коллектора используется ECM для системы защиты двигателя, управления временем и заправкой.

### Расположение компонента

Датчик температуры впускного коллектора расположен на верхней передней половине впускного коллектора.

### Практические замечания

Сопротивление датчика изменяется в зависимости от температуры. Сравните свои показания с этой таблицей:

| Температура (°C) | Температура \[°F\] | Сопротивление (Омс) |
|---|---|---|
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

Устранение неполадок код t05-153


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 153
>
> ### Intake Manifold Temperature Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 153 PID(P): P105 SPN: 105 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at the intake manifold temperature sensor circuit. | Possible white smoke. Fan will stay on if controlled by the electronic control module (ECM). No engine protection for intake manifold temperature. |
>
> Intake Manifold Temperature Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold temperature sensor is used by the ECM to monitor the temperature of the engine intake air. The intake manifold temperature signal is used by the ECM for the engine protection system, timing, and fueling control.
>
> ### Component Location
>
> The intake manifold temperature sensor is located on the top front half of the intake manifold.
>
> ### Shoptalk
>
> The resistance of the sensor varies with the temperature. Compare your reading to this table:
>
> | Temperature (°C) | Temperature \[°F\] | Resistance (ohms) |
> |---|---|---|
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> Refer to Troubleshooting Fault Code t05-153
