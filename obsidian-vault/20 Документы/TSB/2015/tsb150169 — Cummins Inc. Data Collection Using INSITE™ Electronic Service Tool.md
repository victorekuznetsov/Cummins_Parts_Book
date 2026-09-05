---
aliases:
  - "Сбор данных Cummins с помощью INSITE™"
type: "TSB"
doc: "tsb150169"
title_en: "Cummins Inc. Data Collection Using INSITE™ Electronic Service Tool"
title_ru: "Сбор данных Cummins с помощью INSITE™"
released: "2015-10-30"
modified: "2015-10-30"
group: "00 - Complete Engine / Troubleshooting"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33224404"
  - "33239746"
  - "33239899"
  - "35354607"
  - "35373113"
  - "37269910"
  - "37280605"
  - "41340468"
  - "41349633"
  - "41353297"
  - "71156161"
  - "80141463"
  - "80248213"
  - "82099327"
  - "85017333"
  - "93058669"
  - "93087701"
  - "93948840"
families:
  - "C8.3 · 6C8.3"
  - "K19"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150169.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150169.pdf"
tags:
  - "документ/tsb"
  - "двигатель/C8.3"
  - "двигатель/K19"
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
  - "год/2015"
  - "перевод/машинный"
  - "тема/complete-engine-troubleshooting"
---

# Cummins Inc. Data Collection Using INSITE™ Electronic Service Tool
**Сбор данных Cummins с помощью INSITE™**

> [!abstract] TSB · `tsb150169`
> **Раздел Cummins:** 00 - Complete Engine / Troubleshooting
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** C8.3 · 6C8.3, K19, K38/K50 · QSK38, QSK50, QSB6.7, QSK19, QSK23, QSK50, QSK60, QSK60 CM2150 MCRS, QSM11, QSX15, QSZ13
> **Даты:** выпущен 2015-10-30 · изменён 2015-10-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150169.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150169.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Cummins Inc. Сбор данных с помощью инструментария электронного сервиса INSITETM

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- Все продукты, поддерживаемые инструментами электронного сервиса INSITETM

**Клиентская коммуникация**

Изображения электронного модуля управления двигателем (ECM) INSITETM доказали свою ценность в качестве ресурса для решения проблем с продуктами. В рамках усилий по максимальному использованию этого ресурса и сокращению времени цикла решения проблем с продуктами, Cummins Inc. просит персонал на местах поделиться изображениями ECM, выбрав "Enable Cummins Inc. Вариант "Сбор данных" в инструменте электронного обслуживания INSITETM.

**Проверка**

Для проверки того, может ли инструмент электронных услуг INSITETM обмениваться данными:

- Открытие инструментария электронного сервиса INSITETM
- Выберите меню «Инструменты»
- Выберите «варианты»
- Выберите «Рабочие заказы»
- Найдите галочку под названием «Enable Cummins Inc.» Сбор данных. См. рисунок 1 ниже.

![[19r99329.png]]

Рисунок 1 Расположение инструментария электронного сервиса INSITETM «Enable Cummins Inc.» Сбор данных Tick Box и Условия

**Решение**

Проанализируйте условия и положения, прежде чем разрешить сбор данных с Cummins Inc. См. рисунок 1 выше. Если требуется сбор данных, убедитесь, что вы используете Cummins Inc. Выбирается галочка сбора данных.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Cummins Inc. Data Collection Using INSITE™ Electronic Service Tool
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - All products supported by INSITE™ electronic service tool
>
> **Customer Communication**
>
> INSITE™ electronic service tool engine control module (ECM) images have proven a valuable resource to aid in product issue resolution. As part of an effort to start leveraging this resource and reduce product issue resolution cycle times as much as possible, Cummins Inc. requests field personnel share ECM images by selecting the "Enable Cummins Inc. Data Collection" option in the INSITE™ electronic service tool.
>
> **Verification**
>
> To verify if INSITE™ electronic service tool is able to share data:
>
> - Open INSITE™ electronic service tool
> - Select the ‘Tools' drop down menu
> - Select ‘Options'
> - Select ‘Work Orders'
> - Locate the tick box titled ‘Enable Cummins Inc. data collection'. See Figure 1 below.
>
> Figure 1, Location of INSITE™ Electronic Service Tool ‘Enable Cummins Inc. data collection' Tick Box and Terms and Conditions
>
> **Resolution**
>
> Review the terms and conditions prior to enabling data collection with Cummins Inc. See Figure 1 above. If data collection is desired, ensure the ‘Enable Cummins Inc. data collection' tick box is selected.
>
> ### Document History
