---
aliases:
  - "Интерфейсы RS422 и RS232 не поддерживаются CENSE™ CM2330 нового поколения"
type: "TSB"
doc: "tsb120308"
title_en: "RS422 and RS232 Interfaces Not Supported by Next Generation CENSE™ CM2330"
title_ru: "Интерфейсы RS422 и RS232 не поддерживаются CENSE™ CM2330 нового поколения"
released: "2013-01-18"
modified: "2013-01-18"
group: "19 - Electronic Engine Controls"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120308.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb120308.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2013"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# RS422 and RS232 Interfaces Not Supported by Next Generation CENSE™ CM2330
**Интерфейсы RS422 и RS232 не поддерживаются CENSE™ CM2330 нового поколения**

> [!abstract] TSB · `tsb120308`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2013-01-18 · изменён 2013-01-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120308.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb120308.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Интерфейсы RS422 и RS232 не поддерживаются CENSE™ CM2330 нового поколения

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

В этом документе сообщается, что модуль CENSETM CM2330 следующего поколения будет поддерживать интерфейсы RS422 и RS232. Вместо этого он будет общаться только через шину данных J1939 CAN.

Это изменение коснется производителей оригинального оборудования (OEM), использующих систему RS422 Modular Mining Dispatch для получения данных о двигателе. Клиентам, использующим эту систему, необходимо будет обновить модульную систему майнинга J1939.

Это изменение также повлияет на OEM-производителей, использующих радиостанции RS232 для дистанционного мониторинга, и кабины OEM, которые не имеют порта подключения шины передачи данных J1939 к двигателю.

Отдельный документ будет выпущен в 1 квартале 2013 года, чтобы объявить дату устаревания используемого в настоящее время модуля CM530 CENSETM.

| Пострадавшие номера частей |  |
|---|---|
| Название части | Номер детали |
| Электронный блок управления двигателем | 3098771 |

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## RS422 and RS232 Interfaces Not Supported by Next Generation CENSE™ CM2330
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> This document announces that the next generation CENSE™ CM2330 module will **not** be supporting the RS422 and RS232 interfaces. Instead, it will **only** communicate via the J1939 data link.
>
> This change will affect original equipment manufacturers (OEMs) using RS422 Modular Mining Dispatch system to acquire engine data. Customers currently using this system will need to upgrade to J1939-capable Modular Mining Dispatch.
>
> This change will also affect OEMs using RS232 Radios for Remote Monitoring and OEM cabs that do **not** have a J1939 data link connection port to the engine.
>
> A separate document will be released in Q1 2013 to announce the obsolescence date of the presently used CM530 CENSE™ module.
>
> | Affected Part Numbers |  |
> |---|---|
> | Part Name | Part Number |
> | Engine Control Module | 3098771 |
>
> ### Document History
