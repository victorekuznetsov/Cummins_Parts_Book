---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "19-fc121"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2024-12-19"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc121.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc121.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `19-fc121`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2024-12-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc121.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc121.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 121

### Цепь датчика частоты вращения двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 121 PID(P): P190 SPN: 190 FMI: 10 ламп: Желтая СТО: 00-345 | Цепь датчика частоты вращения двигателя. Ни один сигнал скорости двигателя не обнаруживается на одной паре контактов, ни 27, 28, 37, ни 38 с жгутом проводов двигателя. | Не предпринимается никаких действий со стороны модуля управления двигателем (ECM). |

![[19j00575.png]]

Цепь датчика частоты вращения двигателя

### Описание цепи

Датчик скорости двигателя представляет собой схему с двумя катушками, которая обеспечивает сигнал скорости двигателя к ECM через электропроводку двигателя.

### Расположение компонента

Датчик скорости двигателя расположен на корпусе маховика.

### Практические замечания

- Если проблема возникает только при определенной температуре двигателя, обязательно проверьте схему датчика скорости двигателя, пока двигатель находится при этой конкретной температуре.

- Измерьте зазор конца распределительного вала, чтобы убедиться, что передача распределительного вала **не **движется слишком далеко от конца датчика скорости двигателя.

См. Код устранения неполадок t05-121


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 121
>
> ### Engine Speed Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 121 PID(P): P190 SPN: 190 FMI: 10 Lamp: Yellow SRT: 00-345 | Engine Speed Sensor Circuit. No engine speed signal detected at one pair of pins, either pin 27, 28, 37, or 38 of the engine harness. | No action by the engine control module (ECM) is taken. |
>
> Engine Speed Sensor Circuit
>
> ### Circuit Description
>
> The engine speed sensor is a dual-coil circuit that provides the engine speed signal to the ECM through the engine harness.
>
> ### Component Location
>
> The engine speed sensor is located on the flywheel housing.
>
> ### Shoptalk
>
> - If the problem occurs **only** at a certain engine temperature, be sure to check the engine speed sensor circuit while the engine is at that particular temperature.
>
> - Measure camshaft end clearance to make sure that camshaft gear is **not** moving too far away from the end of the engine speed sensor.
>
> Refer to Troubleshooting Fault Code t05-121
