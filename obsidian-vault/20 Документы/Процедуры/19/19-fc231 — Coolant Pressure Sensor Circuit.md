---
aliases:
  - "Цепь датчика давления охлаждающей жидкости"
type: "Процедура"
doc: "19-fc231"
title_en: "Coolant Pressure Sensor Circuit"
title_ru: "Цепь датчика давления охлаждающей жидкости"
modified: "2026-05-28"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc231.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc231.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Coolant Pressure Sensor Circuit
**Цепь датчика давления охлаждающей жидкости**

> [!abstract] Процедура · `19-fc231`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc231.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc231.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 231

### Цепь датчика давления охлаждающей жидкости

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 231 PID(P): P109 SPN: 109 FMI: 3 лампы: Желтая СТО: 00-387 | Более 4,72-VDC обнаружено при контакте датчика давления охлаждающей жидкости 16 проводов двигателя ремня. | Отсутствие защиты двигателя от давления охлаждающей жидкости. |

![[19800988.png]]

Цепь датчика давления охлаждающей жидкости

### Описание цепи

Датчик давления охлаждающей жидкости контролирует давление охлаждающей жидкости и передает информацию в ECM через контакт 16 с ремнем электропроводки двигателя. ECM контролирует напряжение на контакте 16 и ожидает, что напряжение будет варьироваться от 0,5 до 4,5-VDC во время нормальной работы. Напряжение выше 4,72-VDC при контакте 16 будет сбивать Код 231 по умолчанию и может быть вызвано шортами в проводах подачи, сигнала или возврата, открытым в обратном проводе или неисправным датчиком.

### Расположение компонента

Датчик давления охлаждающей жидкости расположен на стороне выхлопа двигателя, ниже масляного охладителя.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный или поврежденный датчик давления охлаждающей жидкости

- Неисправная или поврежденная электропроводка двигателя

См. Код устранения неполадок t05-231


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 231
>
> ### Coolant Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 231 PID(P): P109 SPN: 109 FMI: 3 Lamp: Yellow SRT: 00-387 | More than 4.72-VDC detected at the coolant pressure sensor signal pin 16 of the engine harness. | No engine protection for coolant pressure. |
>
> Coolant Pressure Sensor Circuit
>
> ### Circuit Description
>
> The coolant pressure sensor monitors coolant pressure and passes information to the ECM through pin 16 of the engine harness. The ECM monitors the voltage on pin 16 and expects to see the voltage vary between 0.5 and 4.5-VDC during normal operation. Voltage above 4.72-VDC on pin 16 will trip Fault Code 231 and can be caused by shorts in the supply, signal, or return wires, an open in the return wire, or a failed sensor.
>
> ### Component Location
>
> The coolant pressure sensor is located on the exhaust side of the engine, below the oil cooler.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged coolant pressure sensor
>
> - Malfunctioning or damaged engine wiring harness
>
> Refer to Troubleshooting Fault Code t05-231
