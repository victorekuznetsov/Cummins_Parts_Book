---
aliases:
  - "Инструкции по снятию образа ЭБУ в формате eif через INSITE™"
type: "TSB"
doc: "tsb110081"
title_en: "Instructions to Capture an ECM Job Image with INSITE™ Electronic Service Tool in eif Format"
title_ru: "Инструкции по снятию образа ЭБУ в формате eif через INSITE™"
released: "2024-10-04"
modified: "2024-10-04"
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
  - "71156161"
  - "80141463"
  - "80248213"
  - "82099327"
  - "85017333"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSB6.7"
  - "QSK23"
  - "QSK50"
  - "QSK60"
  - "QSM11"
  - "QSX15"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110081.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110081.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSB6.7"
  - "двигатель/QSK23"
  - "двигатель/QSK50"
  - "двигатель/QSK60"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "год/2024"
  - "перевод/машинный"
  - "тема/service-tools"
---

# Instructions to Capture an ECM Job Image with INSITE™ Electronic Service Tool in eif Format
**Инструкции по снятию образа ЭБУ в формате eif через INSITE™**

> [!abstract] TSB · `tsb110081`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSB6.7, QSK23, QSK50, QSK60, QSM11, QSX15
> **Даты:** выпущен 2024-10-04 · изменён 2024-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110081.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110081.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Инструкции по снятию образа ЭБУ в формате eif через INSITE™

### Суть проблемы

Во время устранения неполадок RAPIDSERVETM или дилерская техническая поддержка могут запросить изображение работы ECM. Это изображение работы может помочь устранителю неисправностей понять, какие коды ошибок активны, как долго они были активны и какие следующие логические шаги по устранению неисправностей или исправлению могут быть.

### Подтверждение

Неприменимые

### Решение

Запустите приложение ниже для инструкций, подробно описывающих, как захватить изображение работы ECM с помощью инструментария электронного обслуживания INSITETM. Полученный файл будет иметь расширение «eif».

> [!note] Примечание
> [https://quickserve.cummins.com/protected/files/qsol/en/service/video/ecm\_image\_upload\_tsb\_final.mp4](https://quickserve.cummins.com/protected/files/qsol/en/service/video/ecm_image_upload_tsb_final.mp4)

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Instructions to Capture an ECM Job Image with INSITE™ Electronic Service Tool in eif Format
>
> ### Core Issue
>
> During troubleshooting, RAPIDSERVE™ or Dealer Technical Support may ask for an ECM job image. This job image can help the troubleshooter understand which fault codes are active, how long they have been active, and what the next logical troubleshooting or repair steps might be.
>
> ### Confirmation
>
> Not Applicable
>
> ### Resolution
>
> Launch the attachment below for instructions detailing how to capture an ECM job image with INSITE™ electronic Service Tool. The resulting file will have an “eif” extension.
>
> **Note · Примечание**
> [https://quickserve.cummins.com/protected/files/qsol/en/service/video/ecm\_image\_upload\_tsb\_final.mp4](https://quickserve.cummins.com/protected/files/qsol/en/service/video/ecm_image_upload_tsb_final.mp4)
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Document History
