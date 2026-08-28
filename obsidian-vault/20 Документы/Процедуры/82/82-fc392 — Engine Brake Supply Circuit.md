---
aliases:
  - "Цепь питания моторного тормоза"
type: "Процедура"
doc: "82-fc392"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc392.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc392.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Brake Supply Circuit
**Цепь питания моторного тормоза**

> [!abstract] Процедура · `82-fc392`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc392.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc392.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 392

### Цепь питания моторного тормоза

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 392 P(P): S080 SPN: 1073 ФМИ: 11 лампочка: Желтая СТО: | Менее 6 VDC, обнаруженных в цепи 2 тормоза двигателя, когда на ней указывается избыточный ток, выходящий из электронного модуля управления (ECM) или неисправная выходная цепь ECM. | Тормоз 2 двигателя может быть активирован **не**. |

![[19200178.png]]

Ретранслятор реле двигателя Схема подачи

### Описание цепи

ECM позволяет тормозу двигателя, посылая сигнал непосредственно на тормоза двигателя. ECM будет **только **включать тормоза двигателя при определенных условиях эксплуатации.

### Расположение компонента

См. диаграмму OEM для определения местоположения тормоза двигателя.

### Практические замечания

Возможная причина этого кода неисправности - водитель тормоза двигателя ECM 2, короткое время на земле.

См. Код устранения неполадок t05-392


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 392
>
> ### Engine Brake Supply Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 392 PID(P): S080 SPN: 1073 FMI: 11 Lamp: Yellow SRT: | Less than 6 VDC detected at engine brake circuit 2 when on indicates an excessive current draw from the electronic control module (ECM) or a faulty ECM output circuit. | Engine brake 2 can **not** be activated. |
>
> Engine Brake Relay Supply Circuit
>
> ### Circuit Description
>
> The ECM enables the engine brake by sending a signal directly to the engine brakes. The ECM will **only** enable the engine brakes under certain operating conditions.
>
> ### Component Location
>
> Refer to an OEM diagram for the location of the engine brake.
>
> ### Shoptalk
>
> A possible cause for this fault code is an ECM engine brake driver 2 short to ground.
>
> Refer to Troubleshooting Fault Code t05-392
