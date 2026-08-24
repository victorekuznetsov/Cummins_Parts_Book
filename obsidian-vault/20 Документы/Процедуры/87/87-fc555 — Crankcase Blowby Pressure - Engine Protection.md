---
aliases:
  - "Давление прорыва газов в картер — защита двигателя"
type: "Процедура"
doc: "87-fc555"
title_en: "Crankcase Blowby Pressure - Engine Protection"
title_ru: "Давление прорыва газов в картер — защита двигателя"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc555.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc555.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Crankcase Blowby Pressure - Engine Protection
**Давление прорыва газов в картер — защита двигателя**

> [!abstract] Процедура · `87-fc555`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc555.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc555.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 555

### Давление прорыва газов в картер — защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 555 PID(P): 101 SPN: 101 FMI: 0 лампочка: Защита двигателя SRT: | Выявлено высокое давление газообменного газа. Сигнал напряжения при контакте 25 с сигналом давления продувки указывает на давление продувки выше 368 мм Н 2 О \[14,5 в Н 2 О\]. | Калибровочная зависимость прогрессивной мощности, скорости ухудшается, и выключение двигателя, как давление увеличивается за пороги. |

![[19a00237.png]]

Цепь датчика давления прорыва газов в картер

### Описание цепи

Датчик давления в продувке используется электронным модулем управления (ECM) для мониторинга давления в картере двигателя. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления. Значение давления продувки используется ECM для системы защиты двигателя.

### Расположение компонента

Датчик давления продувки расположен в чехле передач на левой стороне двигателя.

### Практические замечания

- Подтвердите, что дыхательные пути и дыхательные трубки ** не** затрудняются.

- Датчик давления газодувного картера используется совместно с системой мониторинга двигателя CENSETM.

Примечание: Количество неисправных ламп может быть сокращено до двух для некоторых OEM-производителей. Защита двигателя и стоп-сигналы соединены вместе как красная лампа. Предупреждающая лампа остается желтой лампой.

Устранение неполадок код t05-555


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 555
>
> ### Crankcase Blowby Pressure - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 555 PID(P): 101 SPN: 101 FMI: 0 Lamp: Engine Protection SRT: | High crankcase blowby pressure has been detected. Voltage signal at blowby pressure signal pin 25 indicates blowby pressure above 368 mm H 2 O \[14.5 in H 2 O\]. | Calibration-dependent progressive power, speed derate, and engine shutdown as pressure increases over thresholds. |
>
> Crankcase Blowby Pressure Sensor Circuit
>
> ### Circuit Description
>
> The blowby pressure sensor is used by the electronic control module (ECM) to monitor the engine crankcase pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The blowby pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> The blowby pressure sensor is located in the gear case on the left side of the engine.
>
> ### Shoptalk
>
> - Confirm that the crankcase breathers and breather tubes are **not** obstructed.
>
> - The crankcase blowby pressure sensor is used in conjunction with the CENSE™ engine monitoring system.
>
> Note: The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.
>
> Refer to Troubleshooting Fault Code t05-555
