---
aliases:
  - "INSITE™ 7.4: проблема отображения функций и параметров"
type: "TSB"
doc: "tsb100051"
title_en: "INSITE™ 7.4 Features and Parameters Display Issue"
title_ru: "INSITE™ 7.4: проблема отображения функций и параметров"
released: "2010-06-17"
modified: "2010-06-17"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100051.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb100051.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "год/2010"
  - "перевод/машинный"
  - "тема/service-tools"
---

# INSITE™ 7.4 Features and Parameters Display Issue
**INSITE™ 7.4: проблема отображения функций и параметров**

> [!abstract] TSB · `tsb100051`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Даты:** выпущен 2010-06-17 · изменён 2010-06-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100051.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb100051.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## INSITE™ 7.4: проблема отображения функций и параметров

### Суть проблемы

В настоящем бюллетене по техническим услугам описывается проблема с неправильной (слишком узкой) дисплеем колонки «Особенности и параметры» в версии 7.4 (7.4.0.244) электронного инструментария INSITETM. Это приводит к расширению строк и затрудняет чтение названий функций.

### Подтверждение

Все двигатели поддерживаются электронным сервисным оборудованием INSITETM.

Открытые функции и параметры при подключении к ECM и первая колонка узкая, а строки широкие.

Нет

В электронной службе INSITETM 7.4 (7.4.0.244) автоматически неправильно настраивается ширина первой колонки на некоторых разрешениях экрана.

Нет

### Решение

Ручно отрегулировать ширину первой колонки:

- Переместите проклятье по колонной линии, пока оно не изменится на двойную стрелку.
- При удерживании левой кнопки мыши вниз, переместить линию столбца вправо, пока ширина столбца не увеличится, а затем отпустите кнопку мыши.

![[22000028.png]]

После изменения размера колонки ширина строки будет автоматически регулироваться.

![[22000029.png]]

Измените разрешение дисплея на любую из следующих настроек:

- 800 на 600
- 1024 к 768
- 1280, любой
- 1152 к 864

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.


> [!quote]- Original (English) · английский оригинал
> ## INSITE™ 7.4 Features and Parameters Display Issue
>
> ### Core Issue
>
> This Technical Service Bulletin describes an issue with INSITE™ electronic service tool version 7.4 (7.4.0.244) displaying the Features and Parameters column incorrectly (too narrow). This causes the rows to widen and makes it difficult to read the feature names.
>
> ### Confirmation
>
> All Engines supported by INSITE™ electronic service tool.
>
> Open Features and Parameters while connected to an ECM and the first column is narrow and the rows are wide.
>
> None
>
> INSITE™ electronic service tool version 7.4 (7.4.0.244) is automatically adjusting the first column width incorrectly on some screen resolutions.
>
> None
>
> ### Resolution
>
> Manually adjust the width of the first column:
>
> - Move the curser over the column line until it changes to a double arrow.
> - While holding the left mouse button down, move the column line to the right until the column width has increased and then release the mouse button.
>
> After resizing the column, the row width will automatically adjust.
>
> Change the display resolution to any of the following settings:
>
> - 800 by 600
> - 1024 by 768
> - 1280 by Any
> - 1152 by 864
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
