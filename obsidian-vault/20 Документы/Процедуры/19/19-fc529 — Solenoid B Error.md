---
aliases:
  - "Ошибка электромагнита B"
type: "Процедура"
doc: "19-fc529"
title_en: "Solenoid B Error"
title_ru: "Ошибка электромагнита B"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc529.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc529.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Solenoid B Error
**Ошибка электромагнита B**

> [!abstract] Процедура · `19-fc529`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc529.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc529.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 529

### Ошибка электромагнита B

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 529 PID(P): S51 SPN: 703 FMI: 3 лампы: Желтая СТО: | Двойной выходной сигнал B-контакта 9 интерфейса OEM-проводов указывает на открытое или короткое замыкание. | OEM-зависимые. |

![[19400891.png]]

Соленоидная B-схема

### Описание цепи

Водитель соленоида будет управлять двигателем и функциями транспортного средства, закрывая или открывая переключаемый выход соленоида, на основе 11 выбранных параметров двигателя. Выход соленоидов будет контролировать такие функции, как сцепление вентилятора, нагреватель впускной сетки, индикатор ограничения очистки воздуха или индикатор дифференциального давления масляного фильтра.

### Расположение компонента

Соленоидный драйвер является OEM-устройством, и местоположение соленоида зависит от OEM-устройства.

См. Код устранения неполадок t05-529


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 529
>
> ### Solenoid B Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 529 PID(P): S51 SPN: 703 FMI: 3 Lamp: Yellow SRT: | The dual output B signal pin 9 of the OEM interface harness indicates an open or short circuit. | OEM-dependent. |
>
> Solenoid B Circuit
>
> ### Circuit Description
>
> The solenoid driver will control engine and vehicle functions by closing or opening a switched solenoid output, based on 11 selected engine parameters. The solenoid output will control functions such as a fan clutch, intake grid heater, air cleaner restriction indicator, or an oil filter differential pressure indicator.
>
> ### Component Location
>
> The solenoid driver is an OEM device and the location of the solenoid is dependent upon the OEM.
>
> Refer to Troubleshooting Fault Code t05-529
