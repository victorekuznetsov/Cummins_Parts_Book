---
aliases:
  - "Цепь датчика давления ресивера"
type: "Процедура"
doc: "82-fc218"
title_en: "Wet Tank Pressure Sensor Circuit"
title_ru: "Цепь датчика давления ресивера"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc218.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc218.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Wet Tank Pressure Sensor Circuit
**Цепь датчика давления ресивера**

> [!abstract] Процедура · `82-fc218`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc218.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc218.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 218

### Цепь датчика давления ресивера

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 218 P(P): P046 SPN: 46 ФМИ: 2/2 лампы: Желтая СТО: | Напряжение при сигнале давления в мокром резервуаре указывает на то, что давление в мокром резервуаре слишком высокое или слишком низкое. | Воздушный компрессор будет работать непрерывно. |

![[19c00651.png]]

Цепь датчика давления ресивера

### Описание цепи

Датчик давления в мокром резервуаре обеспечивает сигнал датчика давления в мокром резервуаре к электронному модулю управления (ECM).

### Расположение компонента

Датчик давления влажного резервуара расположен на воздушном компрессоре. Он является частью электронного воздушного регулятора и не обслуживается.

### Практические замечания

Эта неисправность указывает на то, что давление во влажном резервуаре ниже или выше, чем указано в спецификациях.

См. Код устранения неполадок t05-218


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 218
>
> ### Wet Tank Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 218 PID(P): P046 SPN: 46 FMI: 2/2 Lamp: Yellow SRT: | Voltage at wet tank pressure signal indicates wet tank pressure is too high or too low. | Air compressor will run continuously. |
>
> Wet Tank Pressure Sensor Circuit
>
> ### Circuit Description
>
> The wet tank pressure sensor provides the wet tank pressure sensor signal to the electronic control module (ECM).
>
> ### Component Location
>
> The wet tank pressure sensor is located on the air compressor. It is part of the electronic air governor and is nonserviceable.
>
> ### Shoptalk
>
> This fault indicates that the pressure in the wet tank is lower or higher than specifications.
>
> Refer to Troubleshooting Fault Code t05-218
