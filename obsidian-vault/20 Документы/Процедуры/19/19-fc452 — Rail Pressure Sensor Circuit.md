---
type: "Процедура"
doc: "19-fc452"
title_en: "Rail Pressure Sensor Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc452.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc452.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Rail Pressure Sensor Circuit

> [!abstract] Процедура · `19-fc452`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc452.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc452.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 452

### Схема датчика давления на железной дороге

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 452 PID (P): 157 SPN: 157 ФМИ: 4 лампы: Красная СТО: 00-375 | Менее 0,15-VDC обнаруживается при контакте 31 сигнала датчика давления рельсовой электропроводки ремня электропередачи двигателя. | В зависимости от калибровки двигатель будет выключен или выключен, или ECM не предпримет никаких действий. |

![[19400880.png]]

Схема датчика давления на железной дороге

### Описание цепи

Датчик давления на рельсах обеспечивает сигнал к ECM через электропроводку двигателя. ECM использует сигнал датчика давления рельсов для контроля количества топлива, поступающего в камеру учета топливного форсунка из корпуса управляющего клапана.

### Расположение компонента

Датчик давления в рельсах расположен на нижней правой стороне корпуса управляющего клапана.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправность или повреждение датчика давления в рельсах

- Неисправная или поврежденная электропроводка двигателя

См. Код устранения неполадок t05-452


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 452
>
> ### Rail Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 452 PID(P): 157 SPN: 157 FMI: 4 Lamp: Red SRT: 00-375 | Less than 0.15-VDC detected at the rail pressure sensor signal pin 31 of the engine harness. | Depending on the calibration, the engine will shut down or power-derate, or no action is taken by the ECM. |
>
> Rail Pressure Sensor Circuit
>
> ### Circuit Description
>
> The rail pressure sensor provides a signal to the ECM through the engine harness. The ECM uses the rail pressure sensor signal to monitor the amount of fuel going to the injector's metering chamber from the control valve body.
>
> ### Component Location
>
> The rail pressure sensor is located on the lower right side of the control valve body.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged rail pressure sensor
>
> - Malfunctioning or damaged engine wiring harness
>
> Refer to Troubleshooting Fault Code t05-452
