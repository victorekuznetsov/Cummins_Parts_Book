---
aliases:
  - "INSITE™: значения давления масла не меняются в мониторе данных"
type: "TSB"
doc: "tsb150154"
title_en: "INSITE™ Electronic Service Tool Engine Oil Pressure Values Will Not Change In the Data Monitor/Logger"
title_ru: "INSITE™: значения давления масла не меняются в мониторе данных"
released: "2015-10-06"
modified: "2018-10-04"
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
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
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
  - "K19"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSB6.7"
  - "QSK19"
  - "QSK23"
  - "QSK50"
  - "QSK60"
  - "QSM11"
  - "QST30"
  - "QSX15"
  - "QSZ13"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150154.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150154.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K19"
  - "двигатель/K38/K50"
  - "двигатель/QSB6.7"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK50"
  - "двигатель/QSK60"
  - "двигатель/QSM11"
  - "двигатель/QST30"
  - "двигатель/QSX15"
  - "двигатель/QSZ13"
  - "год/2015"
  - "перевод/машинный"
  - "тема/service-tools"
---

# INSITE™ Electronic Service Tool Engine Oil Pressure Values Will Not Change In the Data Monitor/Logger
**INSITE™: значения давления масла не меняются в мониторе данных**

> [!abstract] TSB · `tsb150154`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** K19, K38/K50 · QSK38, QSK50, QSK60, QSB6.7, QSK19, QSK23, QSK50, QSK60, QSM11, QST30, QSX15, QSZ13
> **Даты:** выпущен 2015-10-06 · изменён 2018-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150154.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150154.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## INSITE™: значения давления масла не меняются в мониторе данных

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Проблема**

В электронной службе INSITETM версии 8.1.1.199 при попытке контролировать или регистрировать давление масла в двигателе в мониторе данных / в кассете во время работы двигателя значение давления масла будет **не **изменяться.

**Решение**

Временным решением является установка электронного сервисного инструментария INSITETM версии 8.0.3.142.

Инструменты для электронного обслуживания INSITETM версии 8.0.3.142 можно загрузить по ссылке ниже.

> [!note] Примечание
> [https://www.cummins.com/support/electronic-service-tools-support/insite-support](https://www.cummins.com/support/electronic-service-tools-support/insite-support)

Разрабатывается постоянное исправление, которое будет выпущено с помощью пакета услуг InsiteTM 8.1.1 версии 1.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## INSITE™ Electronic Service Tool Engine Oil Pressure Values Will Not Change In the Data Monitor/Logger
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Issue**
>
> In INSITE™ electronic service tool version 8.1.1.199, while trying to monitor or data log engine oil pressure in data monitor/logger during engine operation, the oil pressure value will **not** change.
>
> **Resolution**
>
> A temporary solution is to install INSITE™ electronic service tool version 8.0.3.142.
>
> INSITE™ electronic service tool version 8.0.3.142 can be downloaded using the link below.
>
> **Note · Примечание**
> [https://www.cummins.com/support/electronic-service-tools-support/insite-support](https://www.cummins.com/support/electronic-service-tools-support/insite-support)
>
> A permanent fix is being developed and will be released with INSITE™ electronic service tool version 8.1.1 service pack 1.
>
> ### Document History
