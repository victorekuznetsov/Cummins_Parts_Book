---
aliases:
  - "Питание датчика подачи топлива"
type: "Процедура"
doc: "82-fc443"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc443.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc443.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Throttle Voltage Supply
**Питание датчика подачи топлива**

> [!abstract] Процедура · `82-fc443`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc443.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc443.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 443

### Питание датчика подачи топлива

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 443 PID(P): S221 SPN: 1043 FMI: 4/4 лампы: Желтая СТО: | Низкое напряжение, обнаруженное на линии электронного модуля управления (ECM) подачи напряжения на дроссель (дроссель). | Двигатель будет только простаивать. |

![[19c00644.png]]

Throttle Position - система напряжения питания

### Описание цепи

ECM поставляет ускоритель и дистанционный дроссел с +5 VDC. Если линия подачи на ускорители повреждена, ускорители будут работать неправильно.

### Расположение компонента

Педаль акселератора находится в кабине. См. руководство OEM для удаленного местоположения дроссельной заслонки.

### Практические замечания

Низкое напряжение на линии питания +5-VDC будет вызвано коротким замыканием на землю в линии питания, коротким замыканием между линией питания или обратной линией, неисправным ускорителем или неисправным источником питания ECM.

Устранение неполадок код t05-443


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 443
>
> ### Throttle Voltage Supply
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 443 PID(P): S221 SPN: 1043 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected on the electronic control module (ECM) voltage supply line to the throttle(s). | Engine will **only** idle. |
>
> Throttle Position Supply Voltage Circuit
>
> ### Circuit Description
>
> The ECM supplies the accelerator and the remote throttle with +5 VDC. If the supply line to the accelerators is damaged, the accelerators will **not** work correctly.
>
> ### Component Location
>
> Accelerator pedal is located in the cab. Refer to the OEM manual for remote throttle location.
>
> ### Shoptalk
>
> Low voltage on the +5-VDC supply line will be caused by a short circuit to ground in a supply line, a short circuit between a supply line or a return line, a failed accelerator, or a failed ECM power supply.
>
> Refer to Troubleshooting Fault Code t05-443
