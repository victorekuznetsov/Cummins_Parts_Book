---
aliases:
  - "Давление масла — защита двигателя"
type: "Процедура"
doc: "19-fc143"
title_en: "Oil Pressure - Engine Protection"
title_ru: "Давление масла — защита двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc143.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc143.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Oil Pressure - Engine Protection
**Давление масла — защита двигателя**

> [!abstract] Процедура · `19-fc143`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc143.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc143.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 143

### Давление масла — защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 143 PID(P): P100 SPN: 100 FMI: 1 лампа: Защита двигателя SRT: 00-354 | Было обнаружено низкое давление масла. Сигнал напряжения при контакте 24 с сигналом давления масла в ремне электропроводки двигателя указывает на давление масла ниже 103 кПа[15 psi\] при 600 об/мин, 131 кПа\[19 psi\] при 800 об/мин, 165 кПа\[24 psi\] при 1500 об/мин и 207 кПа\[30 psi\] выше 2100 об/мин. | Калибровка-зависимая прогрессивная мощность ухудшается и выключение двигателя с увеличением времени после оповещения. Система CentinelTM отключена. |

![[19400133.png]]

Цепь датчика давления масла

### Описание цепи

Датчик давления масла используется ECM для мониторинга давления моторного масла. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления. Значение давления масла используется ECM для системы защиты двигателя.

### Расположение компонента

Датчик давления масла расположен на блоке двигателя, в направлении передней части ECM.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправность или повреждение датчика давления моторного масла

- Низкий уровень масла

- Внешние утечки масла

- Фильтры моторного масла

- Загрязненное масло

- Аэрация масла

- Высокая температура масла

- Неисправность или повреждение главного регулятора давления масляной винты

- Неисправность или повреждение форсунки для охлаждения поршня

- Неисправность или повреждение всасывающей трубки масла

- Неисправность или повреждение водопровода для передачи масла

- Неисправность или повреждение масляного насоса

- Неисправный или поврежденный смазочный насос клапан высокого давления

- Повреждение внутреннего двигателя

- Неисправный или поврежденный элемент масляного охладителя

См. Код устранения неполадок t05-143


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 143
>
> ### Oil Pressure - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 143 PID(P): P100 SPN: 100 FMI: 1 Lamp: Engine Protection SRT: 00-354 | Low oil pressure has been detected. Voltage signal at oil pressure signal pin 24 of the engine harness indicates oil pressure lower than 103 kPa \[15 psi\] at 600 rpm, 131 kPa \[19 psi\] at 800 rpm, 165 kPa \[24 psi\] at 1500 rpm, and 207 kPa \[30 psi\] above 2100 rpm. | Calibration-dependent progressive power derate and engine shutdown with increasing time after alert. Centinel™ system is disabled. |
>
> Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The oil pressure sensor is used by the ECM to monitor the lubricating oil pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The oil pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> The oil pressure sensor is located on the engine block, toward the front of the ECM.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged engine oil pressure sensor
>
> - Low oil level
>
> - External oil leaks
>
> - Plugged lubricating oil filters
>
> - Contaminated oil
>
> - Oil aeration
>
> - High oil temperature
>
> - Malfunctioning or damaged main oil rifle pressure regulator
>
> - Malfunctioning or damaged piston cooling nozzle
>
> - Malfunctioning or damaged oil suction tube
>
> - Malfunctioning or damaged oil transfer plumbing
>
> - Malfunctioning or damaged oil pump
>
> - Malfunctioning or damaged lubricating pump high pressure relief valve
>
> - Internal engine damage
>
> - Malfunctioning or damaged oil cooler element
>
> Refer to Troubleshooting Fault Code t05-143
