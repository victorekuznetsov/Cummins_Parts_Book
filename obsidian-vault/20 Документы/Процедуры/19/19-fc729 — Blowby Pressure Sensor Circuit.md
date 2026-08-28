---
type: "Процедура"
doc: "19-fc729"
title_en: "Blowby Pressure Sensor Circuit"
modified: "2013-04-15"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc729.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc729.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Blowby Pressure Sensor Circuit

> [!abstract] Процедура · `19-fc729`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2013-04-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc729.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc729.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 729

### Схема датчика давления Blowby Pressure Sensor Circuit

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 729 PID(P): P22 SPN: 1264 FMI: 4 лампы: Желтая СТО: 00-678 | Менее 0,29-VDC обнаружено на датчике давления SIGNAL 25 контакта проводов двигателя. | Отсутствие защиты двигателя от давления продува. |

![[r8j00045.png]]

Схема датчика давления Blowby Pressure Sensor Circuit

### Описание цепи

Датчик давления продувки контролирует давление продувки и передает эту информацию модулю управления двигателем (ECM) через контакт 25 с ремнем электропроводки двигателя. ECM контролирует напряжение на контакте 25 и ожидает, что напряжение будет варьироваться от 0,5 до 4,5-VDC во время нормальной работы двигателя. Напряжение ниже 0,29-VDC при контакте 25 будет сбивать Код 729 по умолчанию и может быть вызвано шортами в проводах SUPPLY, SIGNAL или RETURN, открытым в проводе RETURN или неисправным датчиком.

### Расположение компонента

Датчик давления надувной системы расположен на стороне выхлопа двигателя, ниже водяного насоса на топливных системах QSK19.[[19-100-002-tr — Engine Diagrams|См. процедуру 100-002 (Диаграммы двигателей) в разделе E для определения местоположения компонентов двигателей QSK23, QSK45, QSK60 и QSK78.]]

### Практические замечания

Подтвердите, что дыхательные аппараты, дыхательные трубки и датчик продува **не **затрудняются.

См. Код устранения неполадок t05-729


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 729
>
> ### Blowby Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 729 PID(P): P22 SPN: 1264 FMI: 4 Lamp: Yellow SRT: 00-678 | Less than 0.29-VDC detected at the blowby pressure sensor SIGNAL pin 25 of the engine harness. | No engine protection for blowby pressure. |
>
> Blowby Pressure Sensor Circuit
>
> ### Circuit Description
>
> The blowby pressure sensor monitors blowby pressure and passes this information to the engine control module (ECM) through pin 25 of the engine harness. The ECM monitors the voltage on pin 25 and expects to see the voltage vary between 0.5 and 4.5-VDC during normal engine operation. Voltage below 0.29-VDC on pin 25 will trip Fault Code 729 and can be caused by shorts in the SUPPLY, SIGNAL, or RETURN wires, an open in the RETURN wire, or a malfunctioning sensor.
>
> ### Component Location
>
> The blowby pressure sensor is located on the exhaust side of the engine, below the water pump on the QSK19 fuel systems. [[19-100-002-tr — Engine Diagrams|Refer to Procedure 100-002 (Engine Diagrams) in Section E for component location for QSK23, QSK45, QSK60, and QSK78 Series engines.]]
>
> ### Shoptalk
>
> Confirm that the crankcase breathers, breather tubes, and blowby sensor are **not** obstructed.
>
> Refer to Troubleshooting Fault Code t05-729
