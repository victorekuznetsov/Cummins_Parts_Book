---
aliases:
  - "Регистратор данных CENSE™"
type: "Процедура"
doc: "77-019-431"
title_en: "CENSE™ Datalogger"
title_ru: "Регистратор данных CENSE™"
modified: "2013-01-18"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "3810497"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/77/77-019-431.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/77-019-431.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/77"
  - "перевод/машинный"
---

# CENSE™ Datalogger
**Регистратор данных CENSE™**

> [!abstract] Процедура · `77-019-431`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[3810497 — K38, K50, QSK38 and QSK50 Operation and Maintenance Manual|3810497]]
> **Секции:** Section 4 - Maintenance Procedures at 250 Hours or 6 Months
> **Даты:** изменён 2013-01-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/77/77-019-431.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/77-019-431.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### сброс

Сброс с помощью механического форсунка топлива

- Для модулей CENSETM CM530** только*** данные* должны сбрасываться каждые 250 часов для поддержания максимальной емкости памяти.

1. Сначала извлеките сохраненные данные CENSETM.
2. Выберите коды ошибок и параметры данных тренда для сброса.

- Свяжитесь с авторизованным местом ремонта Cummins® для получения подробных инструкций.

Сброс с помощью электронного форсунки

- Эти двигатели не используют CENSETM. Вместо этого они имеют усовершенствованный мониторинг двигателя, встроенный в электронные модули управления. Эти данные не должны быть сброшены, потому что они будут автоматически записываться по самым старым данным, если емкость памяти станет полной. Однако эта память может быть очищена вручную с помощью инструментария электронного обслуживания INSITETM. Логи ошибок должны быть просмотрены, даже если они не будут сброшены.

> [!note] Примечание
> Модули CENSETM CM2330 не должны быть сброшены.

![[19800902.png]]


> [!quote]- Original (English) · английский оригинал
> ### Reset
>
> Reset with Mechanically Actuated Injectors
>
> - For CENSE™ CM530 modules **only**, the data **must** be reset every 250 hours in order to maintain maximum memory capacity.
>
> 1. First retrieve the CENSE™ data that has been saved.
> 2. Select the fault codes and trend data options for resetting.
>
> - Contact a Cummins® Authorized Repair Location for detailed instructions.
>
> Reset with Electronically Actuated Injectors
>
> - These engines do **not** use CENSE™. Instead they have Advanced Engine Monitoring built into the electronic control modules. This data does **not** need to be reset because it will automatically write over the oldest data in case the memory capacity becomes full. However, this memory can be cleared manually using INSITE™ electronic service tool. Fault logs need to be viewed even if they are **not** going to be reset.
>
> **Note · Примечание**
> The CENSE™ CM2330 modules do **not** need to be reset.
