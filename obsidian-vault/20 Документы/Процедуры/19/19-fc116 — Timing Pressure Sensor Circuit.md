---
type: "Процедура"
doc: "19-fc116"
title_en: "Timing Pressure Sensor Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc116.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc116.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Timing Pressure Sensor Circuit

> [!abstract] Процедура · `19-fc116`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc116.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc116.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 116

### Схема датчика давления

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 116 PID(P): P156 SPN: 156 FMI: 3 лампы: Красная СТО: 00-346 | Более 4,78 ВДК обнаружено при датчике давления синхронизации сигнала контакта 33 проводов двигателя ремня. | В зависимости от калибровки двигатель будет выключен или замедлен, или не будет предпринято никаких действий со стороны ECM. |

![[19400803.png]]

Схема датчика давления

### Описание цепи

Датчик давления синхронизации обеспечивает сигнал датчика давления синхронизации к ECM через электропроводку двигателя. ECM использует сигнал датчика давления синхронизации для контроля давления топлива синхронизации, идущего в камеру синхронизации форсунки от корпуса управляющего клапана.

### Расположение компонента

Датчик давления синхронизации расположен на правой стороне корпуса управляющего клапана.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправность или повреждение датчика давления

- Неисправная или поврежденная электропроводка двигателя

Устранение неполадок код t05-116


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 116
>
> ### Timing Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 116 PID(P): P156 SPN: 156 FMI: 3 Lamp: Red SRT: 00-346 | More than 4.78 VDC detected at timing pressure sensor signal pin 33 of the engine harness. | Depending on the calibration, the engine will shut down or speed-derate, or no action by the ECM is taken. |
>
> Timing Pressure Sensor Circuit
>
> ### Circuit Description
>
> The timing pressure sensor provides the timing pressure sensor signal to the ECM through the engine harness. The ECM uses the timing pressure sensor signal to monitor the timing fuel pressure going to the injector's timing chamber from the control valve body.
>
> ### Component Location
>
> The timing pressure sensor is located on the right side of the control valve body.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged timing pressure sensor
>
> - Malfunctioning or damaged engine wiring harness
>
> Refer to Troubleshooting Fault Code t05-116
