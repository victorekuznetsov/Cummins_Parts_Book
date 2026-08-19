---
aliases:
  - "Питание датчиков"
type: "Процедура"
doc: "82-fc386"
title_en: "Sensor Voltage Supply"
title_ru: "Питание датчиков"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc386.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc386.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Sensor Voltage Supply
**Питание датчиков**

> [!abstract] Процедура · `82-fc386`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc386.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc386.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 386

### Питание датчиков

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 386 PID(P): S232 SPN: 620 FMI: 3 лампы: Желтая СТО: | Высокое напряжение, обнаруженное на внутреннем электронном модуле управления (ECM), подводит провод к датчикам. | Двигатель отнесен к параметрам без воздуха. |

![[19200188.png]]

Сенсорная схема напряжённости

### Описание цепи

ECM поставляет каждый из этих датчиков с +5 VDC. Если провод подачи к любому датчику поврежден, датчик будет работать ** не** правильно.

### Расположение компонента

В подаче напряжения датчика участвуют два компонента: Датчик давления впускного коллектора и датчик давления окружающего воздуха. Датчик давления окружающего воздуха расположен слева от ECM при взгляде на сторону двигателя напротив впускного коллектора. Датчик давления впускного коллектора расположен на верхней стороне впускного коллектора по направлению к передней части двигателя.

### Практические замечания

Высокое напряжение на датчике +5-VDC питающего провода будет вызвано короткой батареей питающего провода или короткой между приводным проводом и питающим проводом.

Устранение неполадок код t05-386


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 386
>
> ### Sensor Voltage Supply
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 386 PID(P): S232 SPN: 620 FMI: 3 Lamp: Yellow SRT: | High voltage detected on the internal electronic control module (ECM) supply wire to the sensors. | Engine is derated to no-air setting. |
>
> Sensor Voltage Supply Circuit
>
> ### Circuit Description
>
> The ECM supplies each of these sensors with +5 VDC. If the supply wire to any sensor is damaged, the sensor will **not** work correctly.
>
> ### Component Location
>
> There are two components involved in the sensor voltage supply: The intake manifold pressure sensor and the ambient air pressure sensor. The ambient air pressure sensor is located to the left of the ECM when looking at the side of the engine opposite the intake manifold. The intake manifold pressure sensor is located on the topside of the intake manifold toward the front of the engine.
>
> ### Shoptalk
>
> High voltage on the sensor +5-VDC supply wire will be caused by a short to battery of the supply wire or a short between an actuator wire and the supply wire.
>
> Refer to Troubleshooting Fault Code t05-386
