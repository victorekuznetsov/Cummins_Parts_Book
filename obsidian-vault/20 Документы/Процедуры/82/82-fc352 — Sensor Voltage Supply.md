---
aliases:
  - "Питание датчиков"
type: "Процедура"
doc: "82-fc352"
title_en: "Sensor Voltage Supply"
title_ru: "Питание датчиков"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc352.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc352.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Sensor Voltage Supply
**Питание датчиков**

> [!abstract] Процедура · `82-fc352`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc352.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc352.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 352

### Питание датчиков

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 352 PID(P): S232 SPN: 620 FMI: 4 лампы: Желтая СТО: | Низкое напряжение, обнаруженное на внутренней линии электронного управления (ECM) для некоторых датчиков. | Двигатель отнесен к параметрам без воздуха. |

![[19200188.png]]

Сенсорная схема поставки

### Описание цепи

ECM поставляет каждый из этих датчиков с +5 VDC. Если линия подачи на любой датчик повреждена, датчик будет работать неправильно.

### Расположение компонента

В подаче напряжения датчика участвуют два компонента: Датчик давления впускного коллектора и датчик давления окружающего воздуха. Датчик давления окружающего воздуха расположен слева от ECM при взгляде на сторону двигателя, противоположную впускному коллектора. Датчик давления впускного коллектора расположен на верхней стороне коллектора впуска воздуха по направлению к передней части двигателя.

### Практические замечания

Низкое напряжение на линии питания датчика +5-VDC будет вызвано коротким заземлением в линии питания, коротким замыканием между линией питания или обратной линией, неисправным датчиком или неисправным источником питания ECM.

См. Код устранения неполадок t05-352


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 352
>
> ### Sensor Voltage Supply
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 352 PID(P): S232 SPN: 620 FMI: 4 Lamp: Yellow SRT: | Low voltage detected on the internal electronic control module (ECM) supply line to some of the sensors. | Engine is derated to no-air setting. |
>
> Sensor Supply Circuit
>
> ### Circuit Description
>
> The ECM supplies each of these sensors with +5 VDC. If the supply line to any sensor is damaged, the sensor will **not** work correctly.
>
> ### Component Location
>
> There are two components involved in the sensor voltage supply: The intake manifold pressure sensor and the ambient air pressure sensor. The ambient air pressure sensor is located to the left of the ECM when looking at the side of the engine opposite of the intake manifold. The intake manifold pressure sensor is located on the topside of the air intake manifold toward the front of the engine.
>
> ### Shoptalk
>
> Low voltage on the sensor +5-VDC supply line will be caused by a short to ground in a supply line, a short circuit between a supply line or a return line, a failed sensor, or a failed ECM power supply.
>
> Refer to Troubleshooting Fault Code t05-352
