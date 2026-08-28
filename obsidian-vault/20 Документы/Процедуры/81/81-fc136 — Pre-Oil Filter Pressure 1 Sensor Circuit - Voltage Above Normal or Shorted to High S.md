---
type: "Процедура"
doc: "81-fc136"
title_en: "Pre-Oil Filter Pressure 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2015-07-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc136.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc136.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Pre-Oil Filter Pressure 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `81-fc136`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc136.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc136.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 136

### Давление фильтра перед маслом 1 Сенсорная схема - напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 136 PID(P): 99 SPN: 1208 FMI: 3 лампы: Нет, не srt: 00-688 | Давление фильтра предварительного масла 1 Сенсорная схема - напряжение выше нормального или короткое к высокому источнику. Высокое напряжение, обнаруженное на датчике давления масла префильтра SIGNAL контакт 07 основной проводов ремня разъема A ECM. | Код 612 неисправности отключен. |

![[19800763.png]]

Схема датчика давления масла Prefilter

### Описание цепи

Давление масла префильтра — это давление масла двигателя до того, как масло прошло через масляные фильтры. Датчик давления масла префильтра отправляет сигнал давления масла префильтра в ECM CENSETM.

### Расположение компонента

Датчик давления масла префильтра расположен на впускной стороне масляной системы фильтра головки.

### Практические замечания

- Если неисправность возникает только в холодной среде, позвольте маслу прогреться и проверить, не становится ли неисправность неактивной.

Устранение неполадок код t05-136


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 136
>
> ### Pre-Oil Filter Pressure 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 136 PID(P): 99 SPN: 1208 FMI: 3 Lamp: None SRT: 00-688 | Pre-Oil Filter Pressure 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected on prefilter oil pressure sensor SIGNAL pin 07 of the main harness A ECM connector. | Fault Code 612 is disabled. |
>
> Prefilter Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The prefilter oil pressure is the engine oil pressure before the oil has passed through the oil filters. The prefilter oil pressure sensor sends the prefilter oil pressure signal to the CENSE™ ECM.
>
> ### Component Location
>
> The prefilter oil pressure sensor is located on the oil inlet side of the lubricating oil system filter head.
>
> ### Shoptalk
>
> - If the fault occurs **only** in a cold environment, allow the oil to warm up and check to see if the fault becomes inactive.
>
> Refer to Troubleshooting Fault Code t05-136
