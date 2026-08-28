---
aliases:
  - "Таймаут при загрузке калибровки"
type: "TSB"
doc: "tsb101003"
title_en: "Calibration Download Timeout Issue"
title_ru: "Таймаут при загрузке калибровки"
released: "2009-10-24"
modified: "2009-10-24"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101003.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101003.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK50"
  - "год/2009"
  - "перевод/машинный"
  - "тема/service-tools"
---

# Calibration Download Timeout Issue
**Таймаут при загрузке калибровки**

> [!abstract] TSB · `tsb101003`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK50
> **Даты:** выпущен 2009-10-24 · изменён 2009-10-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101003.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101003.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Таймаут при загрузке калибровки

### Суть проблемы

Это раннее уведомление о поле описывает проблему, которая возникает с некоторыми электронными модулями управления (ECM) во время попытки калибровки. Из-за возможной проблемы с тайм-аутом во время загрузки калибровки, первоначальная передача калибровки может выйти из строя и привести к загрузке ECM. Все остальные попытки калибровки будут неудачными.

### Подтверждение

- ISB CM2150
- ISC CM2150
- ISL CM2150
- ISLE CM2150
- ISX CM871
- ISM CM876
- ИСО CM2150
- QSB CM850
- QSC CM850
- QSL CM850
- QSK19 MCRS
- QSK38 MCRS
- QSK50/60 MCRS
- QSK19 MCRS Power Generation (Электрогенерация)
- QSK38 MCRS Power Generation (Электрогенерация)
- QSK50/60 MCRS Power Generation (Электрогенерация)

При попытке калибровать ECM, который не выполнил калибровку, следующие попытки могут не сработать на 70% процесса «Подготовка ECM к получению калибровки».

Нет

Во время процесса загрузки калибровки в электронном сервисном оборудовании INSITETM происходит тайм-аут, который приводит к сбою процесса калибровки и загрузке ECM в ROM.

Нет

### Решение

Эта проблема была решена с помощью инструментария для электронных услуг INSITETM 7.3, Feature Pack 2. Используйте инструмент для электронных услуг INSITETM, который был обновлен с помощью пакета функций INSITETM 7.3 2, для калибровки ECM, которые столкнулись с этой проблемой.

- Загрузите и установите инструмент InSITETM 7.3 для электронных услуг Feature Pack 2 с помощью менеджера обновлений для электронных услуг Cummins® INSITETM, либо через Интернет, либо через CD Option.
- Инструмент для электронного сервиса INSITETM 7.3 Feature Pack 2 можно бесплатно скачать через Интернет. CD-диски будут доступны для покупки у вашего местного дистрибьютора.

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.


> [!quote]- Original (English) · английский оригинал
> ## Calibration Download Timeout Issue
>
> ### Core Issue
>
> This Early Field Notification describes an issue that occurs with some Electronic Control Modules (ECMs) during a calibration attempt. Due to a possible timeout issue during calibration download, the initial calibration transfer can fail and cause the ECM to be ROM booted. All other calibration attempts will fail.
>
> ### Confirmation
>
> - ISB CM2150
> - ISC CM2150
> - ISL CM2150
> - ISLe CM2150
> - ISX CM871
> - ISM CM876
> - ISZ CM2150
> - QSB CM850
> - QSC CM850
> - QSL CM850
> - QSK19 MCRS
> - QSK38 MCRS
> - QSK50/60 MCRS
> - QSK19 MCRS Power Generation
> - QSK38 MCRS Power Generation
> - QSK50/60 MCRS Power Generation
>
> When attempting to calibrate an ECM that has failed calibration download, the next attempts can fail at 70 percent of “Preparing ECM to receive calibration.”, or early during the “Transferring ECM calibration.” process.
>
> None
>
> A timeout occurs, during the calibration download process in INSITE™ electronic service tool, that causes the calibration process to fail and the ECM to become ROM booted.
>
> None
>
> ### Resolution
>
> This issue has been resolved with INSITE™ 7.3 electronic service tool, Feature Pack 2. Use INSITE™ electronic service tool that has been updated with INSITE™ 7.3 Feature Pack 2, to calibrate ECMs that have experienced this issue.
>
> - Download and install INSITE™ 7.3 electronic service tool Feature Pack 2 using the Cummins® INSITE™ electronic service tool Update Manager, by either the Internet or the CD Option.
> - The INSITE™ 7.3 electronic service tool Feature Pack 2, is a free download through the Internet. CDs will be available for purchase from your local distributor.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
