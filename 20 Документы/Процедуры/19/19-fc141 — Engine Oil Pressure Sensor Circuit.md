---
type: "Процедура"
doc: "19-fc141"
title_en: "Engine Oil Pressure Sensor Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Engine Oil Pressure Sensor Circuit

> [!abstract] Процедура · `19-fc141`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc141.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 141

### Схема датчика давления моторного масла

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 141 PID(P): P100 SPN: 100 FMI: 4 лампы: Желтая СТО: 00-353 | Менее 0,31-VDC обнаруживается при датчике давления масла двигателя, контактном 24 провода двигателя жгута. | Отсутствие защиты двигателя от давления масла. Система CentinelTM отключена. |

![[19400133.png]]

Схема датчика давления моторного масла

### Описание цепи

Датчик давления моторного масла контролирует давление масла и передает информацию в ECM через контакт 24 с ремнем электропроводки двигателя. ECM контролирует напряжение на контакте 24 и ожидает, что напряжение будет варьироваться от 0,5 до 4,5-VDC во время нормальной работы двигателя. Напряжение ниже 0,31-VDC при контакте 24 будет сбивать Код 141 по умолчанию и может быть вызвано шортами в подаче, сигнале или обратном проводе, открытым в подаче или сигнальных проводах, низким напряжением питания от ECM или неисправным датчиком.

### Расположение компонента

Датчик давления масла двигателя расположен на блоке двигателя в верхнем левом углу ECM.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправность или повреждение датчика давления моторного масла

- Неисправная или поврежденная электропроводка двигателя

Устранение неполадок код t05-141


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 141
>
> ### Engine Oil Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 141 PID(P): P100 SPN: 100 FMI: 4 Lamp: Yellow SRT: 00-353 | Less than 0.31-VDC detected at the engine oil pressure sensor signal pin 24 of the engine harness. | No engine protection for oil pressure. Centinel™ system is disabled. |
>
> Engine Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The engine oil pressure sensor monitors oil pressure and passes information to the ECM through pin 24 of the engine harness. The ECM monitors the voltage on pin 24 and expects to see the voltage vary between 0.5 and 4.5-VDC during normal engine operation. Voltage below 0.31-VDC on pin 24 will trip Fault Code 141 and can be caused by shorts in the supply, signal, or return wires, an open in the supply or signal wires, low supply voltage from the ECM, or a failed sensor.
>
> ### Component Location
>
> The engine oil pressure sensor is located on the engine block to the upper left of the ECM.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged engine oil pressure sensor
>
> - Malfunctioning or damaged engine wiring harness
>
> Refer to Troubleshooting Fault Code t05-141
