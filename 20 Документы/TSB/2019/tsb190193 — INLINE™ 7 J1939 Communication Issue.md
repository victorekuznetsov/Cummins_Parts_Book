---
aliases:
  - "Проблема связи J1939 адаптера INLINE™ 7"
type: "TSB"
doc: "tsb190193"
title_en: "INLINE™ 7 J1939 Communication Issue"
title_ru: "Проблема связи J1939 адаптера INLINE™ 7"
released: "2019-11-11"
modified: "2019-11-11"
group: "22 - Service Tools"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190193.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb190193.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "год/2019"
  - "перевод/машинный"
  - "тема/service-tools"
---

# INLINE™ 7 J1939 Communication Issue
**Проблема связи J1939 адаптера INLINE™ 7**

> [!abstract] TSB · `tsb190193`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Даты:** выпущен 2019-11-11 · изменён 2019-11-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190193.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb190193.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Проблема связи J1939 адаптера INLINE™ 7

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

** Пострадавшие продукты**

- ISX CM870
- ISX CM871
- ISB CM2150
- ISC CM2150
- ISL CM2150

**Проблема**

Инситем 5200 Ошибка при использовании INLINETM 7. См. рисунок 1 для 5200 ошибок.

![[22r00348.png]]

Рисунок 1 Инсайт Электронный сервис 5200 Ошибка.

**Решение**

- Используем протокол J1708: Пользователь может создать соединение INLINETM 7 J1708 с помощью мастера ECM Connection Wizard в инструменте электронного сервиса INSITETM. См. рисунок 2.

![[22r00349.png]]

Рисунок 2, Связь INLINETM 7 J1708.

- Используйте Интернет 6.
- Разрабатываются и тестируются новые прошивки и драйверы INLINETM 7.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## INLINE™ 7 J1939 Communication Issue
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Products Affected**
>
> - ISX CM870
> - ISX CM871
> - ISB CM2150
> - ISC CM2150
> - ISL CM2150
>
> **Issue**
>
> INSITE™ electronic service tool 5200 Error when using INLINE™ 7. See Figure 1 for 5200 Error displayed.
>
> Figure 1, INSITE™ Electronic Service Tool 5200 Error.
>
> **Resolution**
>
> - Use J1708 protocol: User can create an INLINE™ 7 J1708 connection using the ECM Connection Wizard in the INSITE™ electronic service tool. See Figure 2.
>
> Figure 2, INLINE™ 7 J1708 Connection.
>
> - Use an INLINE™ 6.
> - New INLINE™ 7 firmware and drivers are being developed and tested.
>
> ### Document History
