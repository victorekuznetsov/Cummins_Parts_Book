---
aliases:
  - "Цепь датчика давления во впускном коллекторе"
type: "Процедура"
doc: "82-fc122"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc122.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc122.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Intake Manifold Pressure Sensor Circuit
**Цепь датчика давления во впускном коллекторе**

> [!abstract] Процедура · `82-fc122`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc122.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc122.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 122

### Цепь датчика давления во впускном коллекторе

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 122 P(P): P102 SPN: 102 FMI: 3/3 лампы: Желтая СТО: | Высокое напряжение, обнаруженное на цепи датчика давления впускного коллектора. | Уменьшите выходную мощность двигателя. |

![[19200329.png]]

Цепь датчика давления во впускном коллекторе

### Описание цепи

Датчик давления впускного коллектора контролирует давление впускного коллектора и передает информацию в электронный модуль управления (ECM) через электропроводку двигателя. Если давление коллектора потребления становится слишком высоким, это вызовет ухудшение состояния.

### Расположение компонента

Датчик давления впускного коллектора расположен в коллекторе воздухозаборника по направлению к передней части двигателя.

### Практические замечания

- Определите, перегружен ли двигатель.

- Подтвердите, что используется правильный номер детали датчика давления коллектора впуска.

- Подтвердите, что используется правильный турбокомпрессор.

- Если есть подозрение, что холодный воздух является причиной высокого давления впускного коллектора, проверьте двигатель с теплым воздухом.

- Осмотрите цепь датчика давления впускного коллектора на наличие признаков подделки. Удалите любые дополнительные провода из схемы.

См. Код устранения неполадок t05-122


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 122
>
> ### Intake Manifold Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 122 PID(P): P102 SPN: 102 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at the intake manifold pressure sensor circuit. | Derate in power output of the engine. |
>
> Intake Manifold Pressure Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold pressure sensor monitors intake manifold pressure and passes information to the electronic control module (ECM) through the engine harness. If the intake manifold pressure becomes too high, it will cause a derate condition.
>
> ### Component Location
>
> The intake manifold pressure sensor is located in the air intake manifold toward the front of the engine.
>
> ### Shoptalk
>
> - Determine if engine is being overfueled.
>
> - Confirm that the correct intake manifold pressure sensor part number is being used.
>
> - Confirm that the correct turbocharger is being used.
>
> - If it is suspected that cold intake air is the cause of the high intake manifold pressure, test the engine with warm intake air.
>
> - Inspect the intake manifold pressure sensor circuit for signs of tampering. Remove any extra wires from the circuit.
>
> Refer to Troubleshooting Fault Code t05-122
