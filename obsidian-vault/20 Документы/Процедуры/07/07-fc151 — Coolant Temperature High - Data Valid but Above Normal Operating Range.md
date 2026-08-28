---
aliases:
  - "Высокая температура ОЖ — данные достоверны, выше нормы"
type: "Процедура"
doc: "07-fc151"
title_en: "Coolant Temperature High - Data Valid but Above Normal Operating Range"
title_ru: "Высокая температура ОЖ — данные достоверны, выше нормы"
modified: "2012-12-18"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc151.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc151.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Coolant Temperature High - Data Valid but Above Normal Operating Range
**Высокая температура ОЖ — данные достоверны, выше нормы**

> [!abstract] Процедура · `07-fc151`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc151.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc151.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 151

### Высокая температура ОЖ — данные достоверны, выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 151 PID(P): P110 SPN: 110 FMI: 0 лампочка: Красная СТО: | Высокие температуры охлаждающей жидкости - данные действительны, но выше нормального диапазона работы (наиболее серьезный уровень). | Защита двигателя включена, двигатель выключен. Защита двигателя включена, защита двигателя от потери мощности отключена, никаких действий не предпринято. |

![[19900358.png]]

Цепь датчика температуры охлаждающей жидкости

### Описание цепи

Датчик температуры охлаждающей жидкости используется электронным модулем управления (ECM) для мониторинга температуры охлаждающей жидкости двигателя. Датчик температуры охлаждающей жидкости используется ECM для системы защиты двигателя, управления временем и заправкой. ECM контролирует напряжение на контакте сигнала датчика температуры охлаждающей жидкости.

### Расположение компонента

Справочный раздел E для подробного описания местоположения компонента. Датчик температуры охлаждающей жидкости расположен в корпусе термостата.

### Практические замечания

Напряжение сигнала изменяется между 0,5 и 4,5 ВДК, так как внутреннее сопротивление датчика изменяется из-за изменения температуры охлаждающей жидкости. Когда напряжение сигнала датчика указывает на температуру, превышающую установленный предел, код 151 по умолчанию регистрируется.

Эта неисправность часто связана с поврежденным насосом морской воды, засоренным охладителем или морским сетчатым устройством, загрязненным теплообменником или неисправным термостатом.

Неисправный датчик может вызвать неисправность кода 151.

На следующей диаграмме показано сопротивление датчика температуры охлаждающей жидкости при различных показаниях температуры.

| Температура (°F) | Температура (°C) | Сопротивление (Омс) |
|---|---|---|
| 32 | 0 | 30k до 36k |
| 77 | 25 | 9k до 11k |
| 122 | 50 | 3k - 4k |
| 167 | 75 | 1350—1500 |
| 212 | 100 | 600-675 |

Количество неисправных ламп может быть уменьшено до двух для некоторых OEM-производителей. Защита двигателя и стоп-сигналы соединены вместе как красная лампа. Предупреждающая лампа остается янтарной лампой.

Устранение неполадок код t05-151


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 151
>
> ### Coolant Temperature High - Data Valid but Above Normal Operating Range
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 151 PID(P): P110 SPN: 110 FMI: 0 Lamp: Red SRT: | Coolant temperature high - data valid but above normal operating range (most severe level). | Engine protection shutdown enabled, engine will shut down. Engine protection derate enabled, power derate engine protection disabled, no action taken. |
>
> Coolant Temperature Sensor Circuit
>
> ### Circuit Description
>
> The coolant temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The coolant temperature sensor is used by the ECM for the engine protection system, timing, and fueling control. The ECM monitors the voltage on coolant temperature sensor signal pin.
>
> ### Component Location
>
> Reference Section E for a detailed component location view. The coolant temperature sensor is located in the thermostat housing.
>
> ### Shoptalk
>
> The signal voltage varies between 0.5 and 4.5 VDC as the internal resistance of the sensor changes due to changing coolant temperature. When the sensor signal voltage indicates a temperature exceeding a set limit, Fault Code 151 is logged.
>
> This fault is often associated with a damaged sea water pump, a clogged aftercooler or sea strainer, a fouled heat exchanger or a malfunctioning thermostat.
>
> A faulty sensor can cause Fault Code 151.
>
> The following chart shows resistance of the coolant temperature sensor at various temperature readings.
>
> | Temperature (°F) | Temperature (°C) | Resistance (ohms) |
> |---|---|---|
> | 32 | 0 | 30k to 36k |
> | 77 | 25 | 9k to 11k |
> | 122 | 50 | 3k to 4k |
> | 167 | 75 | 1350 to 1500 |
> | 212 | 100 | 600 to 675 |
>
> The number of fault lamps can be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains an amber lamp.
>
> Refer to Troubleshooting Fault Code t05-151
