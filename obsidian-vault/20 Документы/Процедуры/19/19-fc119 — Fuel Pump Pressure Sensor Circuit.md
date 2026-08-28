---
type: "Процедура"
doc: "19-fc119"
title_en: "Fuel Pump Pressure Sensor Circuit"
modified: "2026-05-28"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc119.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc119.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Fuel Pump Pressure Sensor Circuit

> [!abstract] Процедура · `19-fc119`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc119.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc119.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 119

### Схема датчика давления топливного насоса

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 119 P(P): P135 SPN: 135 FMI: 4 лампы: Желтая СТО: 00-384 | Менее 0,30-VDC обнаруживается при датчике давления топливного насоса, сигнале контакта 32 проводов двигателя с ремнем. | Никаких действий со стороны ЕКМ не предпринимается. |

![[19801091.png]]

Схема датчика давления топливного насоса

### Описание цепи

Датчик давления топливного насоса обеспечивает сигнал датчика давления топливного насоса к ECM через электропроводку двигателя. ECM использует сигнал давления топливного насоса для контроля давления топливного насоса, идущего к корпусу управляющего клапана.

### Расположение компонента

Датчик давления топливного насоса расположен на топливном насосе.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправность или повреждение датчика давления топливного насоса

- Неисправная или поврежденная электропроводка двигателя

Устранение неполадок код t05-119


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 119
>
> ### Fuel Pump Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 119 PID(P): P135 SPN: 135 FMI: 4 Lamp: Yellow SRT: 00-384 | Less than 0.30-VDC detected at fuel pump pressure sensor signal pin 32 of the engine harness. | No action by the ECM is taken. |
>
> Fuel Pump Pressure Sensor Circuit
>
> ### Circuit Description
>
> The fuel pump pressure sensor provides the fuel pump pressure sensor signal to the ECM through the engine harness. The ECM uses the fuel pump pressure signal to monitor the fuel pump pressure going to the control valve body.
>
> ### Component Location
>
> The fuel pump pressure sensor is located on the fuel pump.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged fuel pump pressure sensor
>
> - Malfunctioning or damaged engine wiring harness
>
> Refer to Troubleshooting Fault Code t05-119
