---
aliases:
  - "Цепь датчика давления OEM"
type: "Процедура"
doc: "19-fc297"
title_en: "OEM Pressure Sensor Circuit"
title_ru: "Цепь датчика давления OEM"
modified: "2011-03-01"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc297.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc297.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# OEM Pressure Sensor Circuit
**Цепь датчика давления OEM**

> [!abstract] Процедура · `19-fc297`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc297.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc297.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 297

### Цепь датчика давления OEM

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 297 PID(P): P223 SPN: 1084 FMI: 3 лампы: Желтая СТО: | VDC, обнаруженный на датчике давления OEM, контакт 15 интерфейса OEM с проводкой указывает на то, что датчик вышел из строя. | Отсутствие защиты двигателя от давления OEM. |

![[19400645.png]]

Цепь датчика давления OEM

### Описание цепи

Сигнал датчика OEM используется ECM для мониторинга давления OEM. Давление OEM используется ECM для системы защиты двигателя. Датчик, который вышел из строя высоко, может быть вызван открытой цепью в сигнале или обратном проводе, шортами напряжения в сигнале или обратном проводе или неисправным датчиком.

### Расположение компонента

Месторасположение варьируется в зависимости от OEM. См. руководство по OEM.

### Практические замечания

Сигнал напряжения датчика является ответственностью OEM. См. руководство OEM для спецификаций.

См. Код устранения неполадок t05-297


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 297
>
> ### OEM Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 297 PID(P): P223 SPN: 1084 FMI: 3 Lamp: Yellow SRT: | VDC detected at the OEM pressure sensor signal pin 15 of the OEM interface harness indicates the sensor has failed high. | No engine protection for OEM pressure. |
>
> OEM Pressure Sensor Circuit
>
> ### Circuit Description
>
> The OEM sensor signal is used by the ECM to monitor the OEM pressure. The OEM pressure is used by the ECM for the engine protection system. A sensor that has failed high can be caused by an open circuit in the signal or return wire, voltage shorts in the signal or return wire, or a faulty sensor.
>
> ### Component Location
>
> The location varies with the OEM. Refer to the OEM manual.
>
> ### Shoptalk
>
> The sensor voltage signal is the responsibility of the OEM. Refer to the OEM manual for specifications.
>
> Refer to Troubleshooting Fault Code t05-297
