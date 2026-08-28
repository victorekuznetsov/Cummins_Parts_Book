---
aliases:
  - "Ошибка цепи подогревателя впускного воздуха 1"
type: "Процедура"
doc: "82-fc381"
title_en: "Intake Air Heater Number 1 Circuit Error"
title_ru: "Ошибка цепи подогревателя впускного воздуха 1"
modified: "2011-08-23"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc381.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc381.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Intake Air Heater Number 1 Circuit Error
**Ошибка цепи подогревателя впускного воздуха 1**

> [!abstract] Процедура · `82-fc381`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-08-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc381.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc381.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 381

### Ошибка цепи подогревателя впускного воздуха 1

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 381 PID(P): S237 SPN: 626 FMI: 11 лампочка: Желтая СТО: | Ошибка, обнаруженная в реле 1 помощи холодного старта, позволяет включить схему. | Впускной воздушный обогреватель № 1 может быть включен или выключен все время или поврежден. |

![[19p00010.png]]

Впускной воздушный нагреватель No1

### Описание цепи

Впускной воздушный обогреватель улучшает пусковой и контроль белого дыма в холодных условиях окружающей среды. Электронный модуль управления (ECM) управляет реле, которые переключают питание на воздушный нагреватель.

### Расположение компонента

Приемный воздушный нагреватель расположен на входном соединении воздуха с впускным коллектором. Расположение реле нагревателя будет варьироваться в зависимости от производителя оригинального оборудования (OEM).

### Условия выполнения диагностики

Эта диагностика выполняется, когда переключатель зажигания находится в положении Включения и когда устройство активировано. В некоторых случаях диагностика может также проводиться через определенные промежутки времени.

### Условия установки кодов неисправностей

- Схемы впуска воздушного нагревателя коротко замыкаются.

### Действия системы при активном коде неисправности

- ECM освещает янтарный свет CHECK ENGINE сразу же, когда диагностика проходит и не удается.

- Работа впускного воздушного обогревателя будет отключена.

### Условия сброса кода неисправности

ECM выключит янтарный свет CHECK ENGINE, и состояние кода неисправности станет неактивным сразу после диагностических запусков и проходов. Код неисправности также может быть очищен с помощью электронного инструментария обслуживания INSITETM.

### Практические замечания

- Эти неисправности также могут указывать на то, что схемы впускного воздушного нагревателя сокращены до положительной батареи (+). Это позволит сеткам работать полный рабочий день. Это будет истощать батареи, выжигать сетки и / или уничтожать впускные прокладки.

- Схемы впускного воздушного нагревателя будут активироваться только тогда, когда температура впускного коллектора ниже 19 ° C \[66 ° F \], когда переключатель зажигания находится в положении Включения.

- Если впускные воздушные обогреватели установлены **не** и код 381 по умолчанию активен, используйте INSITETM для отключения этой функции «Входной воздушный обогреватель».

См. Код устранения неполадок t05-381.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 381
>
> ### Intake Air Heater Number 1 Circuit Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 381 PID(P): S237 SPN: 626 FMI: 11 Lamp: Yellow SRT: | Error detected in the cold start aid relay 1 enable circuit. | Intake air heater number 1 can be ON or OFF all of the time or is damaged. |
>
> Intake Air Heater Number 1 Circuit
>
> ### Circuit Description
>
> The intake air heater improves starting and white smoke control in cold ambient conditions. The electronic control module (ECM) controls relays that switch power to the air heater.
>
> ### Component Location
>
> The intake air heater is located at the air inlet connection into the intake manifold. The location of the heater relays will vary with original equipment manufacturer (OEM).
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs when the keyswitch is in the ON position and when the device is activated. In some cases the diagnostic can also run at some fixed intervals.
>
> ### Conditions For Setting The Fault Codes
>
> - Intake air heater circuits are short circuited.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE light immediately when the diagnostic runs and fails.
>
> - The intake air heater operation will be disabled.
>
> ### Conditions For Clearing The Fault Code
>
> The ECM will turn OFF the amber CHECK ENGINE light and the fault code state will become inactive immediately after the diagnostic runs and passes. The fault code can also be cleared with INSITE™ electronic service tool.
>
> ### Shoptalk
>
> - These faults could also indicate the intake air heater circuits are shorted to battery positive (+). This would command the grids to be on full time. This will drain the batteries, burn out grids, and/or destroy intake gaskets.
>
> - The intake air heater circuits will **only** activate when intake manifold temperature is below 19°C \[66°F\] when the keyswitch is in the ON position.
>
> - If the intake air heaters are **not** installed and Fault Code 381 is active, then use INSITE™ to disable this feature, “Intake Air Heater.”
>
> Refer to Troubleshooting Fault Code t05-381.
