---
aliases:
  - "Проблема анализатора образов в INSITE™"
type: "TSB"
doc: "tsb190194"
title_en: "Image Analyzer Issue in INSITE™ Electronic Service Tool"
title_ru: "Проблема анализатора образов в INSITE™"
released: "2019-11-11"
modified: "2019-11-11"
group: "22 - Service Tools"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33224404"
  - "33239746"
  - "33239899"
  - "35354607"
  - "35373113"
  - "41340468"
  - "41349633"
  - "41353297"
  - "71156161"
  - "80141463"
  - "80248213"
  - "82099327"
  - "85017333"
  - "93948840"
families:
  - "K38/K50 · QSK38, QSK50"
  - "QSB6.7"
  - "QSK19"
  - "QSK23"
  - "QSK50"
  - "QSK60"
  - "QSK60 CM2150 MCRS"
  - "QSM11"
  - "QSX15"
  - "QSZ13"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190194.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190194.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSB6.7"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK50"
  - "двигатель/QSK60"
  - "двигатель/QSK60CM2150MCRS"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "двигатель/QSZ13"
  - "год/2019"
  - "перевод/машинный"
  - "тема/service-tools"
---

# Image Analyzer Issue in INSITE™ Electronic Service Tool
**Проблема анализатора образов в INSITE™**

> [!abstract] TSB · `tsb190194`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSB6.7, QSK19, QSK23, QSK50, QSK60, QSK60 CM2150 MCRS, QSM11, QSX15, QSZ13
> **Даты:** выпущен 2019-11-11 · изменён 2019-11-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190194.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190194.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Проблема анализатора образов в INSITE™

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Пострадавшие продукты**

- Все продукты двигателя с электронным управлением.

**Проблема**

Изображения рабочего заказа, созданные с помощью электронных средств инструментального обеспечения INSITETM версий 8.5.0 и 8.5.1, не могут быть должным образом просмотрены в ECM Image Analyzer в новых версиях электронных средств инструментального обеспечения INSITETM. См. рисунок 1 ниже для отображения ошибки.

![[19r99593.png]]

Рисунок 1, ECM Image Analyzer сообщение об ошибке в инструменте электронного сервиса INSITETM.

**Решение**

Создайте новый образ рабочего заказа с помощью последней версии инструментария для электронных услуг INSITETM.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Image Analyzer Issue in INSITE™ Electronic Service Tool
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Products Affected**
>
> - All electronically controlled engine products.
>
> **Issue**
>
> Work order images created with INSITE™ electronic service tool versions 8.5.0 and 8.5.1 are not able to be properly viewed in ECM Image Analyzer in newer INSITE™ electronic service tool versions. See Figure 1 below for error displayed.
>
> Figure 1, ECM Image Analyzer Error Message in INSITE™ Electronic Service Tool.
>
> **Resolution**
>
> Create a new work order image with the latest version of INSITE™ electronic service tool.
>
> ### Document History
