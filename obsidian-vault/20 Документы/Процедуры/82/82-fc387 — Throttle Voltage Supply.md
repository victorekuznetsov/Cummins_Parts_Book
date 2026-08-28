---
aliases:
  - "Питание датчика подачи топлива"
type: "Процедура"
doc: "82-fc387"
title_en: "Throttle Voltage Supply"
title_ru: "Питание датчика подачи топлива"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc387.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc387.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Throttle Voltage Supply
**Питание датчика подачи топлива**

> [!abstract] Процедура · `82-fc387`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc387.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc387.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 387

### Питание датчика подачи топлива

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 387 PID(P): P221 SPN: 1043 FMI: 3/3 лампы: Желтая СТО: | Высокое напряжение, обнаруженное на линии подачи напряжения ECM к дроссельной заслоне (поставке VTP). | Двигатель будет только * простаивать. |

![[19c00644.png]]

Схема напряжения питания Throttle Sensor

### Описание цепи

ECM поставляет дросселя и дистанционного дросселя с +5 VDC. Если линия подачи на дроссель повреждена, дроссель будет работать **не** правильно.

### Расположение компонента

Педаль дросселя расположена в кабине. Смотрите руководство по устранению неполадок и ремонту OEM для определения местоположения удаленного дроссельной заслонки.

### Практические замечания

Высокое напряжение на линии питания + 5-VDC будет вызвано коротким замыканием к батарее линии питания или коротким замыканием между приводом и линией питания.

См. Код устранения неполадок t05-387


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 387
>
> ### Throttle Voltage Supply
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 387 PID(P): P221 SPN: 1043 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected on the ECM voltage supply line to the throttle(s) (VTP supply). | Engine will **only** idle. |
>
> Throttle Sensor Supply Voltage Circuit
>
> ### Circuit Description
>
> The ECM supplies the throttle and remote throttle with +5 VDC. If the supply line to the throttles is damaged, the throttle will **not** work correctly.
>
> ### Component Location
>
> The throttle pedal is located in the cab. Refer to the OEM troubleshooting and repair manual for the location of the remote throttle.
>
> ### Shoptalk
>
> High voltage on the + 5-VDC supply line will be caused by a short circuit to battery of the supply line or a short circuit between an actuator and the supply line.
>
> Refer to Troubleshooting Fault Code t05-387
