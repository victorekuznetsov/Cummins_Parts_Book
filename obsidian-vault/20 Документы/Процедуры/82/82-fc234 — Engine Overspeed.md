---
aliases:
  - "Разнос двигателя (превышение частоты вращения)"
type: "Процедура"
doc: "82-fc234"
title_en: "Engine Overspeed"
title_ru: "Разнос двигателя (превышение частоты вращения)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc234.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc234.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Overspeed
**Разнос двигателя (превышение частоты вращения)**

> [!abstract] Процедура · `82-fc234`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc234.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc234.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 234

### Разнос двигателя (превышение частоты вращения)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 234 PID(P): P190 SPN: 190 FMI: 0 лампочка: Красная СТО: | Сигнал скорости двигателя указывает на то, что скорость двигателя превышает 2650 об/мин. | Запорный клапан топлива закрывается до тех пор, пока скорость двигателя не упадет. Клапан отключения топлива откроется, когда скорость двигателя упадет ниже 2000 об/мин. |

![[19200127.png]]

Двигатель Overspeed Circuit

### Описание цепи

Датчик скорости/положения двигателя обеспечивает информацию о скорости двигателя и положении электронного модуля управления (ECM) через электропроводку двигателя.

### Расположение компонента

Датчик скорости/положения двигателя расположен над воздушным компрессором.

### Практические замечания

Возможные причины этого кода неисправности включают внешние источники топлива, втягиваемые в воздухозаборник, обратное питание (моторирование) двигателя или подделку датчиков скорости / положения двигателя.

Проверить впускной коллектор на наличие источников легковоспламеняющихся паров. Проверьте уплотнения турбокомпрессора, чтобы убедиться, что нет утечек масла.

- Осмотрите датчики скорости двигателя / положения на предмет повреждения или подделки.

См. Код устранения неполадок t05-234


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 234
>
> ### Engine Overspeed
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 234 PID(P): P190 SPN: 190 FMI: 0 Lamp: Red SRT: | Engine speed signal indicates engine speed is greater than 2650 rpm. | Fuel shutoff valve is closed until the engine speed drops. The fuel shutoff valve will open when engine speed falls below 2000 rpm. |
>
> Engine Overspeed Circuit
>
> ### Circuit Description
>
> The engine speed/position sensor provides engine speed and position information to the electronic control module (ECM) through the engine harness.
>
> ### Component Location
>
> The engine speed/position sensor is located above the air compressor.
>
> ### Shoptalk
>
> Possible causes of this fault code include external fuel sources drawn into the intake air passage, reverse powering (motoring) of the engine, or tampering of the engine speed/position sensors.
>
> Inspect the intake manifold for sources of flammable vapors. Check the turbocharger seals to verify that there are no oil leaks.
>
> - Inspect the engine speed/position sensors for damage or tampering.
>
> Refer to Troubleshooting Fault Code t05-234
