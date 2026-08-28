---
type: "Процедура"
doc: "19-fc555"
title_en: "Blowby Pressure - Engine Protection"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc555.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc555.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Blowby Pressure - Engine Protection

> [!abstract] Процедура · `19-fc555`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc555.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc555.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 555

### Давление в виде удара - защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 555 PID(P): P101 SPN: 1264 FMI: 0 лампочка: Защита двигателя SRT: 00-676 | Выявлено высокое давление удара. Сигнал напряжения при контакте 25 с сигналом давления продувки указывает на давление продувки выше 368 мм Н 2 О \[14,5 в Н 2 О\]. | Калибровка зависима. Прогрессивная мощность и скорость снижаются, а двигатель отключается по мере увеличения давления над порогами. |

![[19800996.png]]

Схема датчика давления Blowby Pressure Sensor Circuit

### Описание цепи

Датчик давления продувки используется ECM для контроля давления картерного ящика двигателя. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления. Значение давления продувки используется ECM для системы защиты двигателя.

### Расположение компонента

Датчик давления надува расположен на стороне выхлопа двигателя, ниже водяного насоса на двигателях серии QSK19. См. информацию о местоположении двигателей QSK23, QSK45, QSK60 и QSK78 в разделе E.

### Практические замечания

- Подтвердите, что дыхательные пути и дыхательные трубки **не** затрудняются.

Устранение неполадок код t05-555


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 555
>
> ### Blowby Pressure - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 555 PID(P): P101 SPN: 1264 FMI: 0 Lamp: Engine Protection SRT: 00-676 | High blowby pressure has been detected. Voltage signal at blowby pressure signal pin 25 indicates blowby pressure above 368 mm H 2 O \[14.5 in H 2 O\]. | Calibration-dependent. Progressive power and speed derate and engine shutdown as pressure increases over thresholds. |
>
> Blowby Pressure Sensor Circuit
>
> ### Circuit Description
>
> The blowby pressure sensor is used by the ECM to monitor the engine crankcase pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The blowby pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> The blowby pressure sensor is located on the exhaust side of the engine, below the water pump on the QSK19 series engines. See engine component views in Section E for location information for the QSK23, QSK45, QSK60, and QSK78 series engines.
>
> ### Shoptalk
>
> - Confirm that the crankcase breathers and breather tubes are **not** obstructed.
>
> Refer to Troubleshooting Fault Code t05-555
