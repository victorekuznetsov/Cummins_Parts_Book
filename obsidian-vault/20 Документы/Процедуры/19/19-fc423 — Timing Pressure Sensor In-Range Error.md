---
type: "Процедура"
doc: "19-fc423"
title_en: "Timing Pressure Sensor In-Range Error"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc423.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc423.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Timing Pressure Sensor In-Range Error

> [!abstract] Процедура · `19-fc423`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc423.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc423.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 423

### Датчик давления в диапазоне погрешностей

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 423 PID(P): P156 SPN: 156 FMI: 2 лампы: Желтая СТО: 00-369 | Более 1,83 VDC обнаружены при контакте сигнала давления 33 с проводкой двигателя на ключе двигателя. | Калибровочная зависимость мощности и скорости снижается. |

![[19400803.png]]

Схема датчика давления

### Описание цепи

Датчик давления синхронизации обеспечивает сигнал к ECM через электропроводку двигателя. ECM использует сигнал датчика давления синхронизации для контроля количества топлива, поступающего в камеру синхронизации форсунки из корпуса управляющего клапана.

### Расположение компонента

Датчик давления синхронизации расположен на верхней правой стороне корпуса управляющего клапана.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправность или повреждение датчика давления

- Неисправная или поврежденная электропроводка двигателя

- Сопротивление магистрали слива топлива

См. Код устранения неполадок t05-423


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 423
>
> ### Timing Pressure Sensor In-Range Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 423 PID(P): P156 SPN: 156 FMI: 2 Lamp: Yellow SRT: 00-369 | More than 1.83 VDC detected at the timing pressure signal pin 33 of the engine harness at engine key on. | Calibration-dependent power and speed derate. |
>
> Timing Pressure Sensor Circuit
>
> ### Circuit Description
>
> The timing pressure sensor provides a signal to the ECM through the engine harness. The ECM uses the timing pressure sensor signal to monitor the amount of fuel going to the injector's timing chamber from the control valve body.
>
> ### Component Location
>
> The timing pressure sensor is located on the upper right side of the control valve body.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged timing pressure sensor
>
> - Malfunctioning or damaged engine wiring harness
>
> - Fuel drain line restriction
>
> Refer to Troubleshooting Fault Code t05-423
