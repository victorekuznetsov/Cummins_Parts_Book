---
aliases:
  - "Цепь частотного задания акселератора"
type: "Процедура"
doc: "19-fc148"
title_en: "Frequency Accelerator Circuit"
title_ru: "Цепь частотного задания акселератора"
modified: "2011-03-01"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc148.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc148.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Frequency Accelerator Circuit
**Цепь частотного задания акселератора**

> [!abstract] Процедура · `19-fc148`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc148.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc148.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 148

### Цепь частотного задания акселератора

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 148 PID(P): P91 SPN: 091 ФМИ: 8 ламп: Красная СТО: | Частота более 1500 Гц была обнаружена при частотном ускорительном сигнале контакта 17 проводов OEM-интерфейса. | Калибровочная зависимость мощности и скорости снижается. |

![[19400892.png]]

Цепь частотного задания акселератора

### Описание цепи

Ускоритель частоты обеспечивает команду акселератора водителя к ECM через OEM-проводку и OEM-интерфейс. ECM использует этот сигнал для определения команды заправки.

### Расположение компонента

Месторасположение ускорителя варьируется в зависимости от каждого OEM. См. руководство по OEM.

### Практические замечания

Частотный ускоритель может использоваться либо в сочетании с ускорителем напряжения, либо сам по себе.

Устранение неполадок код t05-148


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 148
>
> ### Frequency Accelerator Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 148 PID(P): P91 SPN: 091 FMI: 8 Lamp: Red SRT: | A frequency of more than 1500 Hz has been detected at the frequency accelerator signal pin 17 of the OEM interface harness. | Calibration-dependent power and speed derate. |
>
> Frequency Accelerator Circuit
>
> ### Circuit Description
>
> The frequency accelerator provides the driver's accelerator command to the ECM through the OEM harness and the OEM interface harness. The ECM uses this signal to determine the fueling command.
>
> ### Component Location
>
> Accelerator location varies with each OEM. Refer to the OEM manual.
>
> ### Shoptalk
>
> The frequency accelerator can be used either in conjunction with a voltage accelerator or by itself.
>
> Refer to Troubleshooting Fault Code t05-148
