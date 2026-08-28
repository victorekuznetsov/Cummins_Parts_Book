---
aliases:
  - "Цепь питания моторного тормоза"
type: "Процедура"
doc: "82-fc388"
title_en: "Engine Brake Supply Circuit"
title_ru: "Цепь питания моторного тормоза"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc388.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc388.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Brake Supply Circuit
**Цепь питания моторного тормоза**

> [!abstract] Процедура · `82-fc388`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc388.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc388.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 388

### Цепь питания моторного тормоза

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 388 PID(P): S079 SPN: 1072 FMI: 11 лампочка: Желтая СТО: | Менее 6 VDC, обнаруженных в цепи 1 тормоза двигателя, когда на ней указывается избыточный ток, выходящий из электронного модуля управления (ECM) или неисправной выходной цепи ECM. | Тормоз 1 двигателя может быть активирован **не**. |

![[19200178.png]]

Цепь питания моторного тормоза

### Описание цепи

ECM позволяет тормозу двигателя, посылая сигнал непосредственно на тормоза двигателя. ECM будет **только** включать тормоза двигателя при определенных условиях.

### Расположение компонента

См. диаграмму OEM для определения местоположения тормоза двигателя.

### Практические замечания

Возможная причина этого кода неисправности - водитель тормоза двигателя ECM 1, расположенный на расстоянии от земли.

Устранение неполадок код t05-388


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 388
>
> ### Engine Brake Supply Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 388 PID(P): S079 SPN: 1072 FMI: 11 Lamp: Yellow SRT: | Less than 6 VDC detected at the engine brake circuit 1 when on indicates an excessive current draw from the electronic control module (ECM) or faulty ECM output circuit. | Engine brake 1 can **not** be activated. |
>
> Engine Brake Supply Circuit
>
> ### Circuit Description
>
> The ECM enables the engine brake by sending a signal directly to the engine brakes. The ECM will **only** enable the engine brakes under certain conditions.
>
> ### Component Location
>
> Refer to an OEM diagram for the location of the engine brake.
>
> ### Shoptalk
>
> A possible cause for this fault code is an ECM engine brake driver 1 short to ground.
>
> Refer to Troubleshooting Fault Code t05-388
