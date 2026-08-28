---
aliases:
  - "Ошибка вспомогательного входа частоты вращения"
type: "Процедура"
doc: "82-fc489"
title_en: "Auxiliary Speed Input Error"
title_ru: "Ошибка вспомогательного входа частоты вращения"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc489.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc489.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Auxiliary Speed Input Error
**Ошибка вспомогательного входа частоты вращения**

> [!abstract] Процедура · `82-fc489`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc489.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc489.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 489 (Индустриальный)

### Ошибка вспомогательного входа частоты вращения

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 489 PID(P): P191 SPN: 191 ФМИ: 1/18 лампы: Желтая СТО: | Вспомогательная частота скорости на входном штифте указывает на то, что частота ниже порога, зависящего от калибровки. | Двигатель будет только  простаивать. |

![[19c00656.png]]

Вспомогательная схема ввода скорости

### Описание цепи

Вспомогательный вход скорости представляет собой частотный сигнал от вспомогательной скорости или пикапа давления. Он отправляется в электронный модуль управления (ECM) и используется для управления скоростью двигателя. Вспомогательная эталонная скорость основана на положении дроссельной заслонки.

### Расположение компонента

Расположение вспомогательного устройства для определения скорости или давления зависит от применения OEM. См. руководство по устранению неполадок и ремонту OEM для определения местоположения компонентов.

### Практические замечания

Вспомогательный регулятор скорости управляет скоростью двигателя на основе измеренной вспомогательной скорости или давления.

См. Код устранения неполадок t05-489


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 489 (INDUSTRIAL)
>
> ### Auxiliary Speed Input Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 489 PID(P): P191 SPN: 191 FMI: 1/18 Lamp: Yellow SRT: | Auxiliary speed frequency on input pin indicates the frequency is below a calibration-dependent threshold. | Engine will **only** idle. |
>
> Auxiliary Speed Input Circuit
>
> ### Circuit Description
>
> The auxiliary speed input is a frequency signal from an auxiliary speed or pressure pickup. It is sent to the electronic control module (ECM) and is used to control the engine speed. Auxiliary reference speed is based on the throttle position.
>
> ### Component Location
>
> The auxiliary speed or pressure pickup device location is dependent on the OEM application. Refer to the OEM troubleshooting and repair manual for component location.
>
> ### Shoptalk
>
> The auxiliary speed governor controls engine speed based on a measured auxiliary speed or pressure.
>
> Refer to Troubleshooting Fault Code t05-489
