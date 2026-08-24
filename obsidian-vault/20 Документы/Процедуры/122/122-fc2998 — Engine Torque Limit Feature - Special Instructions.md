---
aliases:
  - "Функция ограничения крутящего момента — особые указания"
type: "Процедура"
doc: "122-fc2998"
title_en: "Engine Torque Limit Feature - Special Instructions"
title_ru: "Функция ограничения крутящего момента — особые указания"
modified: "2010-09-20"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc2998.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc2998.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Engine Torque Limit Feature - Special Instructions
**Функция ограничения крутящего момента — особые указания**

> [!abstract] Процедура · `122-fc2998`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc2998.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc2998.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2998

### Функция ограничения крутящего момента — особые указания

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2998 PID(P): СПН: 1632 FMI: 14 ламп: Янтарная СРТ: | Функция ограничения крутящего момента — особые указания. Перегрузка двигателя. | Возможный двигатель может сломаться, если включен. |

![[19d02662.png]]

ECM CM2150

### Описание цепи

Не применяется

### Расположение компонента

Не применяется

### Практические замечания

Этот код неисправности предназначен для предотвращения перегрузки двигателя.

Код неисправности запускается, когда скорость двигателя не достигает командной скорости.

Потенциальными причинами этого кода неисправности являются:

- Низкая мощность двигателя

- Высокая регулировка холостого хода слишком высока

- Чрезмерное засорение корпуса

- Неправильная трансмиссия или пропеллер.

См. руководство по обслуживанию OEM по причинам, связанным с чрезмерным загрязнением корпуса и неправильной трансмиссией или винтом, поскольку они являются внешними по отношению к двигателю.

См. Troubleshooting Fault Code 2998.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2998
>
> ### Engine Torque Limit Feature - Special Instructions
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2998 PID(P): SPN: 1632 FMI: 14 Lamp: Amber SRT: | Engine Torque Limit Feature - Special Instructions. Engine overload. | Possible engine derate if enabled. |
>
> ECM CM2150
>
> ### Circuit Description
>
> N/A
>
> ### Component Location
>
> N/A
>
> ### Shoptalk
>
> This fault code is designed to keep the engine from overloading.
>
> The fault code is triggered when the engine speed fails to attain the commanded speed.
>
> Potential causes of this fault code are:
>
> - Low engine power
>
> - High idle adjustment is too high
>
> - Excessive hull fouling
>
> - Incorrect transmission or propeller.
>
> Refer to the OEM service manual for causes associated with excessive hull fouling and incorrect transmission or propeller, as these are external to engine.
>
> Refer to Troubleshooting Fault Code 2998.
