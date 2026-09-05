---
type: "Процедура"
doc: "81-fc2154"
title_en: "Post-Oil Filter Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc2154.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc2154.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Post-Oil Filter Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `81-fc2154`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc2154.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc2154.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2154

### Схема датчика давления после фильтрации масла - напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2154 PID(P): 100 SPN: 611 FMI: 3 лампы: Нет, не srt: 00-686 | Схема датчика давления после фильтрации масла - напряжение выше нормального или короткое до высокого источника. Высокое напряжение, обнаруженное на контакте SIGNAL 09 основной проводов ремня разъема A ECM. | Код 612 неисправности отключен. |

![[19802529.png]]

Схема датчика давления после фильтра

### Описание цепи

Давление масла после фильтра - это давление масла двигателя после того, как масло прошло через масляные фильтры. Датчик давления масла после фильтра посылает сигнал давления масла после фильтра в ECM CENSETM.

### Расположение компонента

Датчик давления масла после фильтра расположен на стороне выхода масла головки фильтра системы моторного масла.

### Практические замечания

- Если неисправность возникает только в холодной среде, позвольте маслу прогреться и посмотрите, не станет ли неисправность неактивной.

См. Код устранения неполадок t05-2154


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2154
>
> ### Post-Oil Filter Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2154 PID(P): 100 SPN: 611 FMI: 3 Lamp: None SRT: 00-686 | Post-Oil Filter Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected on SIGNAL pin 09 of the main harness A ECM connector. | Fault Code 612 is disabled. |
>
> Post-Filter Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The post-filter oil pressure is the engine oil pressure after the oil has passed through the oil filters. The post-filter oil pressure sensor sends the post-filter oil pressure signal to the CENSE™ ECM.
>
> ### Component Location
>
> The post-filter oil pressure sensor is located on the oil outlet side of the lubricating oil system filter head.
>
> ### Shoptalk
>
> - If the fault occurs **only** in a cold environment, allow the oil to warm up and see if the fault becomes inactive.
>
> Refer to Troubleshooting Fault Code t05-2154
