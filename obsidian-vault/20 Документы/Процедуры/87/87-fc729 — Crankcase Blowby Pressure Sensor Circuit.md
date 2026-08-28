---
aliases:
  - "Цепь датчика давления прорыва газов в картер"
type: "Процедура"
doc: "87-fc729"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc729.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc729.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Crankcase Blowby Pressure Sensor Circuit
**Цепь датчика давления прорыва газов в картер**

> [!abstract] Процедура · `87-fc729`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc729.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc729.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 729

### Цепь датчика давления прорыва газов в картер

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 729 PID(P): P030 SPN: 101 FMI: 4 лампы: Желтая СТО: | Менее 0,34 VDC обнаружено на картере газа, продуваемого датчиком давления, контактным 25 проводов двигателя. | Защита двигателя от давления продувки газом из картера отключена. |

![[19a00237.png]]

Цепь датчика давления прорыва газов в картер

### Описание цепи

Датчик давления продувки контролирует давление продувки и передает эту информацию электронному модулю управления (ECM) через контакт 25 с электропроводкой ремня.

ECM контролирует напряжение на контакте 25 и ожидает, что напряжение будет варьироваться от 0,5 до 4,5 ВДК во время нормальной работы двигателя.

Напряжение ниже 0,34 VDC при контакте 25 будет сбивать Код 729 по умолчанию и может быть вызвано короткими замыканиями в проводах подачи, сигнала или возврата, открытым в обратном проводе или неисправным датчиком.

### Расположение компонента

Датчик давления продувки расположен в чехле передач на левой стороне двигателя.

### Практические замечания

- Подтвердите, что датчик продува, капканы и дыхательные трубки **не **затрудняются.

- Датчик давления газодувного картера используется совместно с системой мониторинга двигателя CENSETM.

См. Код устранения неполадок t05-729


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 729
>
> ### Crankcase Blowby Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 729 PID(P): P030 SPN: 101 FMI: 4 Lamp: Yellow SRT: | Less than 0.34 VDC detected at the crankcase blowby pressure sensor signal pin 25 of the engine harness. | Engine protection for crankcase blowby pressure is disabled. |
>
> Crankcase Blowby Pressure Sensor Circuit
>
> ### Circuit Description
>
> The blowby pressure sensor monitors blowby pressure and passes this information to the electronic control module (ECM) through pin 25 of the engine harness.
>
> The ECM monitors the voltage on pin 25 and expects to see the voltage vary between 0.5 and 4.5 VDC during normal engine operation.
>
> Voltage below 0.34 VDC on pin 25 will trip Fault Code 729 and can be caused by short circuits in the supply, signal, or return wires, an open in the return wire, or a failed sensor.
>
> ### Component Location
>
> The blowby pressure sensor is located in the gear case on the left side of the engine.
>
> ### Shoptalk
>
> - Confirm that the blowby sensor, crankcase breathers, and breather tubes are **not** obstructed.
>
> - The crankcase blowby pressure sensor is used in conjunction with CENSE™ engine monitoring system.
>
> Refer to Troubleshooting Fault Code t05-729
