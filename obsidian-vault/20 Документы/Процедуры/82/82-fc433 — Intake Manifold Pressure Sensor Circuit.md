---
aliases:
  - "Цепь датчика давления во впускном коллекторе"
type: "Процедура"
doc: "82-fc433"
title_en: "Intake Manifold Pressure Sensor Circuit"
title_ru: "Цепь датчика давления во впускном коллекторе"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc433.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc433.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Intake Manifold Pressure Sensor Circuit
**Цепь датчика давления во впускном коллекторе**

> [!abstract] Процедура · `82-fc433`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc433.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc433.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 433

### Цепь датчика давления во впускном коллекторе

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 433 PID(P): P102 SPN: 102 FMI: 2/2 лампы: Желтая СТО: | Сигнал напряжения в цепи давления впускного коллектора указывает на высокое давление впускного коллектора, но другие характеристики двигателя указывают, что давление впускного коллектора должно быть низким. | Склоняйтесь к безвоздушной обстановке. |

![[19200329.png]]

Цепь датчика давления во впускном коллекторе

### Описание цепи

Датчик давления впускного коллектора контролирует давление впускного коллектора и передает информацию в электронный модуль управления (ECM) через проводку датчика. Если давление впускного коллектора превышает 127 мм рт.ст. \[5 рт.ст. \] более чем на 20 секунд, в то время как двигатель находится под 5%-ной нагрузкой, это вызовет ухудшение состояния.

### Расположение компонента

Датчик давления впускного коллектора расположен в верхней части впускного коллектора по направлению к передней части двигателя.[[82-100-002 — Engine Diagrams|См. процедуру 100-002 в разделе E.]]

### Практические замечания

ECM проверяет наличие этой неисправности **только **при скоростях вращения двигателя до 50 об/мин выше установленной скорости холостого хода. Если давление впускного коллектора в это время показывает слишком высокое значение, ECM регистрирует этот код неисправности.

Устранение неполадок код t05-433


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 433
>
> ### Intake Manifold Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 433 PID(P): P102 SPN: 102 FMI: 2/2 Lamp: Yellow SRT: | Voltage signal at the intake manifold pressure circuit indicates high intake manifold pressure but other engine characteristics indicate that intake manifold pressure **must** be low. | Derate to no-air setting. |
>
> Intake Manifold Pressure Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold pressure sensor monitors intake manifold pressure and passes information to the electronic control module (ECM) through the sensor harness. If intake manifold pressure exceeds 127 mm-Hg \[5 in-Hg\] for more than 20 seconds while the engine is under 5-percent load, it will cause a derate condition.
>
> ### Component Location
>
> The intake manifold pressure sensor is located on the top of the intake manifold toward the front of engine. [[82-100-002 — Engine Diagrams|Refer to Procedure 100-002 in Section E.]]
>
> ### Shoptalk
>
> The ECM checks for this fault **only** at engine speeds up to 50 rpm above the set idle speed. If the intake manifold pressure shows too high of a value at this time, the ECM will log this fault code.
>
> Refer to Troubleshooting Fault Code t05-433
