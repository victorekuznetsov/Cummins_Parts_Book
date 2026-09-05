---
aliases:
  - "Обновления защиты калибровочных кодов ЭБУ"
type: "TSB"
doc: "tsb190192"
title_en: "Updates to Engine Control Module (ECM) Calibration Code Security"
title_ru: "Обновления защиты калибровочных кодов ЭБУ"
released: "2019-11-11"
modified: "2019-11-11"
group: "22 - Service Tools"
engines:
  - "33224404"
  - "33239746"
  - "33239899"
  - "41340468"
  - "41349633"
  - "41353297"
  - "82099327"
  - "93948840"
families:
  - "K38/K50 · QSK38, QSK50"
  - "QSB6.7"
  - "QSK19"
  - "QSK50"
  - "QSK60 CM2150 MCRS"
  - "QSZ13"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190192.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190192.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSB6.7"
  - "двигатель/QSK19"
  - "двигатель/QSK50"
  - "двигатель/QSK60CM2150MCRS"
  - "двигатель/QSZ13"
  - "год/2019"
  - "перевод/машинный"
  - "тема/service-tools"
---

# Updates to Engine Control Module (ECM) Calibration Code Security
**Обновления защиты калибровочных кодов ЭБУ**

> [!abstract] TSB · `tsb190192`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSB6.7, QSK19, QSK50, QSK60 CM2150 MCRS, QSZ13
> **Даты:** выпущен 2019-11-11 · изменён 2019-11-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190192.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190192.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Обновления защиты калибровочных кодов ЭБУ

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Пострадавшие продукты**

- Все электронно-управляемые двигатели 2007 года выпуска и новее.

**Проблема**

Новые калибровочные коды модуля управления двигателем (ECM) были выпущены с использованием стандартного шифрования для всех продуктов двигателя с электронным управлением. Эти коды калибровки ECM поддерживаются только в электронной версии инструментария INSITETM 8.6.0 и более новой.

**Решение**

Если используется DVD INCALTM с электронной версией 8.6.0, то калибровочные коды ECM должны быть с декабря 2019 года или новее. Эти новые калибровочные коды ECM также можно загрузить из Quickserve® Online (QSOL) или ECM Code Search в инструменте электронного сервиса INSITETM. Любые предыдущие DVD-диски INCALTM или загруженные коды калибровки ECM больше не будут поддерживаться.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Updates to Engine Control Module (ECM) Calibration Code Security
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Products Affected**
>
> - All electronically controlled engine products 2007 and newer.
>
> **Issue**
>
> New engine control module (ECM) calibration codes have been released using industry standard encryption for all electronically controlled engine products. These ECM calibration codes are **only** supported in INSITE™ electronic service tool version 8.6.0 and newer.
>
> **Resolution**
>
> If using an INCAL™ DVD with INSITE™ electronic service tool version 8.6.0, ECM calibration codes **must** be from December 2019 or newer. These new ECM calibration codes can also be downloaded from Quickserve® Online (QSOL) or ECM Code Search within INSITE™ electronic service tool. Any previous INCAL™ DVDs or downloaded ECM calibration codes will no longer be supported.
>
> ### Document History
