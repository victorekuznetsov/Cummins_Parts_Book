---
aliases:
  - "Давление охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "19-fc233"
title_en: "Coolant Pressure - Engine Protection"
title_ru: "Давление охлаждающей жидкости — защита двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc233.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc233.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Coolant Pressure - Engine Protection
**Давление охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `19-fc233`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc233.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc233.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 233

### Давление охлаждающей жидкости — защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 233 PID(P): P109 SPN: 109 FMI: 1 лампа: Защита двигателя SRT: 00-389 | Было обнаружено низкое давление охлаждающей жидкости. Сигнал напряжения при контакте 16 давления охлаждающей жидкости с проводкой двигателя указывает на давление охлаждающей жидкости ниже 28 кПа \[4 psi\] при 800 об/мин, 41 кПа \[6 psi\] при 1300 об/мин, 76 кПа \[11 psi\] при 1800 об/мин, 96 кПа \[14 psi\] при 2000 об/мин и 103 кПа \[15 psi\] выше 2100 об/мин. | Калибровочная зависимость прогрессивной мощности и скорости ухудшается, а выключение двигателя увеличивается с увеличением времени после оповещения. |

![[19800988.png]]

Цепь датчика давления охлаждающей жидкости

### Описание цепи

Датчик давления охлаждающей жидкости используется ECM для мониторинга давления охлаждающей жидкости. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления. Значение давления охлаждающей жидкости используется ECM для системы защиты двигателя.

### Расположение компонента

Датчик давления охлаждающей жидкости расположен на стороне выхлопа двигателя, ниже масляного охладителя.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный или поврежденный датчик давления охлаждающей жидкости

См. Код устранения неполадок t05-233


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 233
>
> ### Coolant Pressure - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 233 PID(P): P109 SPN: 109 FMI: 1 Lamp: Engine Protection SRT: 00-389 | Low coolant pressure has been detected. Voltage signal at coolant pressure signal pin 16 of the engine harness indicates coolant pressure lower than 28 kPa \[4 psi\] at 800 rpm, 41 kPa \[6 psi\] at 1300 rpm, 76 kPa \[11 psi\] at 1800 rpm, 96 kPa \[14 psi\] at 2000 rpm, and 103 kPa \[15 psi\] above 2100 rpm. | Calibration-dependent progressive power and speed derate and engine shutdown with increasing time after alert. |
>
> Coolant Pressure Sensor Circuit
>
> ### Circuit Description
>
> The coolant pressure sensor is used by the ECM to monitor the coolant pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The coolant pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> The coolant pressure sensor is located on the exhaust side of the engine, below the oil cooler.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged coolant pressure sensor
>
> Refer to Troubleshooting Fault Code t05-233
