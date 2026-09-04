---
aliases:
  - "INSITE: неверное отображение датчика температуры ОГ в мониторе данных"
type: "TSB"
doc: "tsb200195"
title_en: "Insite Data Monitor Exhaust Temperature Sensor Display Issue"
title_ru: "INSITE: неверное отображение датчика температуры ОГ в мониторе данных"
released: "2020-10-13"
modified: "2020-10-13"
group: "11 - Exhaust System"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33224404"
  - "33239746"
  - "33239899"
  - "41340468"
families:
  - "K38/K50 · QSK38, QSK50"
  - "QSK50"
  - "QSK60"
  - "QSK60 CM2150 MCRS"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2020/tsb200195.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb200195.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK50"
  - "двигатель/QSK60"
  - "двигатель/QSK60CM2150MCRS"
  - "год/2020"
  - "перевод/машинный"
  - "тема/exhaust-system"
---

# Insite Data Monitor Exhaust Temperature Sensor Display Issue
**INSITE: неверное отображение датчика температуры ОГ в мониторе данных**

> [!abstract] TSB · `tsb200195`
> **Раздел Cummins:** 11 - Exhaust System
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK50, QSK60, QSK60 CM2150 MCRS
> **Даты:** выпущен 2020-10-13 · изменён 2020-10-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2020/tsb200195.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb200195.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## INSITE: неверное отображение датчика температуры ОГ в мониторе данных

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- QSK38 M850
- QSK38 M2150
- QSK45 CM500
- QSK50 CM850
- QSK50 CM2150
- QSK50 CM2350
- QSK60 CM500
- QSK60 CM850
- QSK60 CM2150
- QSK60 CM2350
- QSK78 CM500
- QSK78 CM2350

> [!note] Примечание
> Все SMN с этими двигателями и моделями управления затронуты.

**Проблема**

Существует проблема получения индивидуальной информации датчика температуры выхлопных газов для отображения в мониторе данных Insite.

Первопричина: Набор версии 8.6.1.96 не имеет возможности отображения датчиков температуры выхлопных газов по отдельности.

**Проверка/подтверждение**

Версия Insite, упомянутое выше, создает дисплей, как показано.

![[17r00841.png]]

Рисунок 1 Индивидуальные датчики температуры выхлопа, которые не видны

**Решение**

Свяжитесь с Cummins IT, чтобы понизить Insite до предыдущей версии 8.6.0.104 или 8.6.0.116 для отображения отдельных датчиков температуры выхлопных газов.

![[17r00842.png]]

Рисунок 2, Видимые индивидуальные датчики температуры выхлопа

Возможность просмотра отдельных датчиков температуры выхлопных газов будет работать при выпуске Insite 8.7.0.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Insite Data Monitor Exhaust Temperature Sensor Display Issue
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - QSK38 CM850
> - QSK38 CM2150
> - QSK45 CM500
> - QSK50 CM850
> - QSK50 CM2150
> - QSK50 CM2350
> - QSK60 CM500
> - QSK60 CM850
> - QSK60 CM2150
> - QSK60 CM2350
> - QSK78 CM500
> - QSK78 CM2350
>
> **Note · Примечание**
> All SMNs with these engines and control models are affected.
>
> **Issue**
>
> There is an issue getting individual exhaust temperature sensor information to display in Insite data monitor.
>
> Root Cause: Insite version 8.6.1.96 does not have the ability to display exhaust temperature sensors individually.
>
> **Verification/Confirmation**
>
> The Insite version mentioned above produces a display as shown.
>
> Figure 1, Individual Exhaust Temperature Sensors Not Visible
>
> **Resolution**
>
> Contact Cummins IT to downgrade Insite to previous version 8.6.0.104 or 8.6.0.116 to display individual exhaust temperature sensors.
>
> Figure 2, Visible Individual Exhaust Temperature Sensors
>
> The ability to view individual exhaust temperature sensors will work when Insite 8.7.0 is released.
>
> ### Document History
