---
aliases:
  - "Цепь датчика давления OEM"
type: "Процедура"
doc: "82-fc297"
title_en: "OEM Pressure Sensor Circuit"
title_ru: "Цепь датчика давления OEM"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc297.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc297.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# OEM Pressure Sensor Circuit
**Цепь датчика давления OEM**

> [!abstract] Процедура · `82-fc297`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc297.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc297.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 297 (ИНДУСТРИАЛ)

### Цепь датчика давления OEM

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 297 PID(P): S223 SPN: 1084 FMI: 3/3 лампы: Желтая СТО: | Высокое напряжение, обнаруженное при контакте сигнала датчика давления OEM. | Отсутствие защиты двигателя от давления OEM. |

![[19200386.png]]

Цепь датчика давления OEM

### Описание цепи

Сигнал датчика OEM используется ECM для мониторинга давления OEM. Давление OEM используется ECM для системы защиты двигателя. Датчик, который вышел из строя высоко, может быть вызван открытой цепью в сигнале или обратном проводе, напряжением, коротким в сигнале или обратном проводе, или неисправным датчиком.

### Расположение компонента

Месторасположение варьируется в зависимости от OEM. См. руководство изготовителя машины по диагностике и ремонту.

### Практические замечания

Сигнал напряжения датчика подается ECM на контакте 18 разъёма проводов датчика.

См. Код устранения неполадок t05-297


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 297 (INDUSTRIAL)
>
> ### OEM Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 297 PID(P): S223 SPN: 1084 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at the OEM pressure sensor signal pin. | No engine protection for OEM pressure. |
>
> OEM Pressure Sensor Circuit
>
> ### Circuit Description
>
> The OEM sensor signal is used by the ECM to monitor the OEM pressure. The OEM pressure is used by the ECM for the engine protection system. A sensor that has failed high can be caused by an open circuit in the signal or return wire, a voltage short in the signal or return wire, or a faulty sensor.
>
> ### Component Location
>
> The location varies with the OEM. Refer to the OEM troubleshooting and repair manual.
>
> ### Shoptalk
>
> The sensor voltage signal is supplied by the ECM on pin 18 of the sensor harness connector.
>
> Refer to Troubleshooting Fault Code t05-297
