---
aliases:
  - "Цепь датчика давления прорыва газов в картер"
type: "Процедура"
doc: "87-fc719"
title_en: "Crankcase Blowby Pressure Sensor Circuit"
title_ru: "Цепь датчика давления прорыва газов в картер"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc719.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc719.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Crankcase Blowby Pressure Sensor Circuit
**Цепь датчика давления прорыва газов в картер**

> [!abstract] Процедура · `87-fc719`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc719.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc719.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 719

### Цепь датчика давления прорыва газов в картер

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 719 P(P): P101 SPN: 101 FMI: 3 лампы: Желтая СТО: | Более 4,77 ВДК обнаружены на картере газодувного датчика давления контактным сигналом 25 электропроводки двигателя ремня. | Защита двигателя от давления продувки газом из картера отключена. |

![[19a00237.png]]

Цепь датчика давления прорыва газов в картер

### Описание цепи

Датчик давления продувки картерного газа контролирует давление продувки и передает эту информацию электронному модулю управления (ECM) через контакт 25 проводов двигателя.

ECM контролирует напряжение на контакте 25 и ожидает, что напряжение будет варьироваться от 0,5 до 4,5 ВДК во время нормальной работы двигателя.

### Расположение компонента

Датчик давления продувки расположен в чехле передач на левой стороне двигателя.

### Практические замечания

- Подтвердите, что датчик продува, капканы и дыхательные трубки **не **затрудняются.

- Датчик давления газодувного картера используется совместно с системой мониторинга двигателя CENSETM.

Устранение неполадок код t05-719


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 719
>
> ### Crankcase Blowby Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 719 PID(P): P101 SPN: 101 FMI: 3 Lamp: Yellow SRT: | More than 4.77 VDC detected at the crankcase blowby pressure sensor signal pin 25 of the engine harness. | Engine protection for crankcase blowby pressure is disabled. |
>
> Crankcase Blowby Pressure Sensor Circuit
>
> ### Circuit Description
>
> The crankcase blowby pressure sensor monitors blowby pressure and passes this information to the electronic control module (ECM) through pin 25 of the engine harness.
>
> The ECM monitors the voltage on pin 25 and expects the voltage to vary between 0.5 and 4.5 VDC during normal engine operation.
>
> ### Component Location
>
> The blowby pressure sensor is located in the gear case on the left side of the engine.
>
> ### Shoptalk
>
> - Confirm that the blowby sensor, crankcase breathers, and breather tubes are **not** obstructed.
>
> - The crankcase blowby pressure sensor is used in conjunction with the CENSE™ engine monitoring system.
>
> Refer to Troubleshooting Fault Code t05-719
