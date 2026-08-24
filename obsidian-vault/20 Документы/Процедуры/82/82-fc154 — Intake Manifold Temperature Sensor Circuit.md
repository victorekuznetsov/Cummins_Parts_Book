---
aliases:
  - "Цепь датчика температуры во впускном коллекторе"
type: "Процедура"
doc: "82-fc154"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc154.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc154.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Intake Manifold Temperature Sensor Circuit
**Цепь датчика температуры во впускном коллекторе**

> [!abstract] Процедура · `82-fc154`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc154.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc154.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 154

### Цепь датчика температуры во впускном коллекторе

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 154 PID(P): P105 SPN: 105 FMI: 4/4 лампы: Желтая СТО: | Низкое напряжение, обнаруженное на цепи датчика температуры впускного коллектора. | Возможен белый дым. Вентилятор будет оставаться включенным, если он контролируется электронным модулем управления (ECM). Отсутствие защиты двигателя от температуры впускного коллектора. |

![[19200139.png]]

Цепь датчика температуры во впускном коллекторе

### Описание цепи

Датчик температуры впускного коллектора контролирует температуру воздуха впускного воздуха двигателя для ECM. ECM использует температурный сигнал впускного коллектора для системы защиты двигателя, управления временем и заправкой.

### Расположение компонента

Датчик температуры впускного коллектора расположен на верхней половине впускного коллектора, спереди.

### Практические замечания

Сопротивление датчика изменяется в зависимости от температуры. Сравните свои показания с этой таблицей:

| Температура (°C) | Температура \[°F\] | Сопротивление (Омс) |
|---|---|---|
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

Устранение неполадок код t05-154


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 154
>
> ### Intake Manifold Temperature Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 154 PID(P): P105 SPN: 105 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected at the intake manifold temperature sensor circuit. | Possible white smoke. Fan will stay on if controlled by the electronic control module (ECM). No engine protection for intake manifold temperature. |
>
> Intake Manifold Temperature Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold temperature sensor monitors the temperature of the engine intake air for the ECM. The ECM uses the intake manifold temperature signal for the engine protection system, timing, and fueling control.
>
> ### Component Location
>
> The intake manifold temperature sensor is located on the top half of the intake manifold, at the front.
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
> Refer to Troubleshooting Fault Code t05-154
