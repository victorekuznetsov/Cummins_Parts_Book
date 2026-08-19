---
aliases:
  - "Возможные сбои связи кабеля INLINE™ 6 (9-контактный) при логировании данных"
type: "TSB"
doc: "tsb130131"
title_en: "Possible Communication Issue with the INLINE™ 6 9-pin Connector Cable During Data Monitor Logging (DML)"
title_ru: "Возможные сбои связи кабеля INLINE™ 6 (9-контактный) при логировании данных"
released: "2024-10-04"
modified: "2024-10-04"
group: "22 - Service Tools"
engines:
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QST30"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2013/tsb130131.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb130131.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "год/2024"
  - "перевод/машинный"
  - "тема/service-tools"
---

# Possible Communication Issue with the INLINE™ 6 9-pin Connector Cable During Data Monitor Logging (DML)
**Возможные сбои связи кабеля INLINE™ 6 (9-контактный) при логировании данных**

> [!abstract] TSB · `tsb130131`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19, QST30
> **Даты:** выпущен 2024-10-04 · изменён 2024-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2013/tsb130131.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb130131.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Возможные сбои связи кабеля INLINE™ 6 (9-контактный) при логировании данных

### Суть проблемы

Возможна проблема связи с 9-контактным соединительным кабелем INLINETM 6 во время регистрации данных (DML), если контакты H и J подключены к чему-то другому, чем сеть CAN.

Используются все 9-контактные соединительные кабели INLINETM 6. Поэтому, если производитель оригинального оборудования (OEM) решит использовать контакты H и J для чего-то, кроме сети CAN, это может помешать схеме INLINE 6 CAN. В частности, соединение теряется во время регистрации DML и возникает ошибка 5201.

### Подтверждение

Не применяется

### Решение

Как показано на графике ниже, при использовании 9-контактного соединительного кабеля INLINETM 5 не возникает никаких проблем, независимо от типа адаптера. Однако возможности сети CAN 2 будут потеряны, когда кабель 9-контактного разъема INLINETM 5 будет использоваться с адаптером шины данных INLINETM 6 CAN. Проблема связи может быть обнаружена только тогда, когда кабель 9-контактного разъема INLINETM 6 используется в сочетании с адаптером шины данных INLINETM 6 CAN. Хотя Cummins Inc. В настоящее время комплект INLINETM 5 не продается, а 9-контактный соединительный кабель INLINETM 5 можно приобрести отдельно под номером 3165159.

| Адаптерный тип | 9-контактный кабель Connector | Результат |
|---|---|---|
| ИНЛИНЕТ 6 | INLINETM 6 9-контактный соединительный кабель | Проблема |
| ИНЛИНЕТ 6 | INLINETM 5 9-контактный соединительный кабель | Нет проблем |
| Интернет 5 | INLINETM 5 9-контактный соединительный кабель | Нет проблем |
| Интернет 5 | INLINETM 6 9-контактный соединительный кабель | Нет проблем |

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Possible Communication Issue with the INLINE™ 6 9-pin Connector Cable During Data Monitor Logging (DML)
>
> ### Core Issue
>
> There is a possible communication issue with the INLINE™ 6 9-pin connector cable during Data Monitor Logging (DML), if pins H and J are connected to something other than a CAN network.
>
> All 9-pins of the INLINE™ 6 connector cable are used. Therefore, if an original equipment manufacturer (OEM) decides to use pins H and J for something other than a CAN network, it may interfere with the INLINE 6 CAN circuitry. More specifically, connection is lost during DML logging and error 5201 is encountered.
>
> ### Confirmation
>
> N/A
>
> ### Resolution
>
> As the chart below illustrates, no issues are encountered when an INLINE™ 5 9-pin connector cable is used, regardless of the adapter type. However, the CAN 2 network capability will be lost when an INLINE™ 5 9-pin connector cable is used with the INLINE™ 6 data link adapter. The communication issue may **only** be encountered when the INLINE™ 6 9-pin connector cable is used in combination with the INLINE™ 6 data link adapter. Although Cummins Inc. no longer sells the INLINE™ 5 kit, the INLINE™ 5 9-pin connector cable can still be purchased separately under the Part Number 3165159.
>
> | Adapter Type | 9-pin Connector Cable Type | Result |
> |---|---|---|
> | INLINE™ 6 | INLINE™ 6 9-pin connector cable | Issue |
> | INLINE™ 6 | INLINE™ 5 9-pin connector cable | No issue |
> | INLINE™ 5 | INLINE™ 5 9-pin connector cable | No issue |
> | INLINE™ 5 | INLINE™ 6 9-pin connector cable | No issue |
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Document History
