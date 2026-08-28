---
aliases:
  - "Неверное время ЭБУ в снимке неисправности INSITE™"
type: "TSB"
doc: "tsb090057"
title_en: "Incorrect ECM Time (Key on time) in INSITE™ Fault Snapshot"
title_ru: "Неверное время ЭБУ в снимке неисправности INSITE™"
released: "2009-08-04"
modified: "2009-08-04"
group: "22 - Service Tools"
engines:
  - "33224404"
  - "33239746"
  - "33239899"
  - "41340468"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK50"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2009/tsb090057.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb090057.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK50"
  - "год/2009"
  - "перевод/машинный"
  - "тема/service-tools"
---

# Incorrect ECM Time (Key on time) in INSITE™ Fault Snapshot
**Неверное время ЭБУ в снимке неисправности INSITE™**

> [!abstract] TSB · `tsb090057`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK50
> **Даты:** выпущен 2009-08-04 · изменён 2009-08-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2009/tsb090057.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb090057.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Неверное время ЭБУ в снимке неисправности INSITE™

### Суть проблемы

В этом раннем уведомлении о поле описывается проблема с электронным сервисом INSITETM 7.3 и более ранними версиями, отображающими время ECM (ключевое время) в данных снимка неисправности неправильно, когда включены часы реального времени.

### Подтверждение

- ISM CM876
- ISB4.5/6.7 ISD4.5/6.7 CM2150 SN (Евро 4.5)
- ISB4.5/6.7 ISD4.5/6.7 CM2150 SN (Евро 5)
- QSK38 CM850 - MCRS
- QSK50/60 CM850 - MCRS
- QSM 11 CM876 - Генерация электроэнергии
- QSK38 CM850 -MCRS - Генерация электроэнергии
- QSK50/60 CM850 - MCRS - Электрогенерация

Время ECM (ключевое время) отображается неправильно в данных моментального снимка неисправности в инструменте электронного обслуживания INSITETM, если часы реального времени включены в расширенные данные ECM. Если часы реального времени отключены, то время ECM будет отображаться правильно на снимке неисправности.

Например: Если часы реального времени включены, то время ECM отображается неправильно как 213274:47:16 (HH:MM:SS). Если часы реального времени отключены, время ECM отображается правильно как 968:12:30 (HH:MM:SS).

Нет

Нет

Нет

### Решение

Эта проблема устраняется с помощью инструментария для электронных услуг INSITETM 7.3 Service Pack 1 и более поздних версий.

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.


> [!quote]- Original (English) · английский оригинал
> ## Incorrect ECM Time (Key on time) in INSITE™ Fault Snapshot
>
> ### Core Issue
>
> This Early Field Notification describes an issue with INSITE™ 7.3 electronic service tool and earlier versions displaying the ECM Time (Key on time) in the fault snapshot data incorrectly when the Real Time Clock is enabled.
>
> ### Confirmation
>
> - ISM CM876
> - ISB4.5/6.7 ISD4.5/6.7 CM2150 SN (Euro 4.5)
> - ISB4.5/6.7 ISD4.5/6.7 CM2150 SN (Euro 5)
> - QSK38 CM850 - MCRS
> - QSK50/60 CM850 - MCRS
> - QSM 11 CM876 - Power Generation
> - QSK38 CM850 -MCRS - Power Generation
> - QSK50/60 CM850 - MCRS - Power Generation
>
> The ECM Time (Key on time) is displayed incorrectly in the fault snapshot data in INSITE™ electronic service tool if the Real Time Clock is enabled in Advanced ECM Data. If the Real Time Clock is disabled, the ECM Time will be displayed correctly in the fault snapshot.
>
> For example: if the Real Time Clock is enabled, the ECM Time is displayed incorrectly as 213274:47:16 (HH:MM:SS). If the Real Time Clock is disabled, the ECM Time is displayed correctly as 968:12:30 (HH:MM:SS).
>
> None
>
> None
>
> None
>
> ### Resolution
>
> This issue is fixed with INSITE™ 7.3 electronic service tool Service Pack 1 and later versions.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
