---
aliases:
  - "Цепь датчика давления масла — данные достоверны, ниже нормы"
type: "Процедура"
doc: "07-fc143"
title_en: "Oil Pressure Sensor Circuit - Data Valid but Below Normal Operating Range"
title_ru: "Цепь датчика давления масла — данные достоверны, ниже нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc143.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc143.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Oil Pressure Sensor Circuit - Data Valid but Below Normal Operating Range
**Цепь датчика давления масла — данные достоверны, ниже нормы**

> [!abstract] Процедура · `07-fc143`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc143.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc143.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 143

### Цепь датчика давления масла — данные достоверны, ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 143 PID(P): P100 SPN: 100 FMI: 18 ламп: Янтарная СРТ: | Давление масла низкое - данные действительны, но ниже нормального диапазона работы. | Защита двигателя включена, двигатель выключен. Защита двигателя включена, защита двигателя от потери мощности отключена, никаких действий не предпринято. |

![[19a00194.png]]

Цепь датчика давления масла

### Описание цепи

Датчик давления масла используется электронным модулем управления (ECM) для мониторинга давления моторного масла. ECM контролирует напряжение на контакте сигнала и преобразует это напряжение сигнала в значение давления. Значение давления масла используется ECM для системы защиты двигателя.

### Расположение компонента

Справочный раздел E для подробного описания местоположения компонента. Датчик давления масла расположен между фильтром охлаждающей жидкости и соленоидами нагревателя.

### Практические замечания

Подтвердите, что напряжение питания датчика давления масла составляет от 4,75 до 5,25 ВДК на датчике. Код ошибки 141.

Проверьте с оператором, на какой скорости двигателя происходит неисправность. Если двигатель работает на слишком низкой скорости под нагрузкой (вспашка), давление масла может опускаться ниже пределов защиты двигателя из-за температуры масла.

Давление масла является функцией скорости двигателя, уровня масла и функции регулятора. Работа двигателя на низкой скорости под нагрузкой будет **не** привести к низкому давлению масла, если масло не нагревается, уровень масла низкий, регулятор неисправен, или потери происходят где-то в системе.

Неисправный датчик также может вызвать неисправность кода 143.

Количество неисправных ламп может быть уменьшено до двух для некоторых OEM-производителей. В этом случае защита двигателя и стоп-сигналы соединены вместе как красная лампа. Предупреждающая лампа остается янтарной лампой.

См. Код устранения неполадок t05-143


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 143
>
> ### Oil Pressure Sensor Circuit - Data Valid but Below Normal Operating Range
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 143 PID(P): P100 SPN: 100 FMI: 18 Lamp: Amber SRT: | Oil pressure low - data valid but below normal operating range. | Engine protection shutdown enabled, engine will shut down. Engine protection derate enabled, power derate engine protection disabled, no action taken. |
>
> Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The oil pressure sensor is used by the electronic control module (ECM) to monitor the lubricating oil pressure. The ECM monitors the voltage on the signal pin and converts this signal voltage to a pressure value. The oil pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> Reference Section E for a detailed component location view. The oil pressure sensor is located between the coolant filter and the heater solenoids.
>
> ### Shoptalk
>
> Confirm that the oil pressure sensor supply voltage is between 4.75 and 5.25 VDC at the sensor. Reference Fault Code 141.
>
> Verify with the operator at what engine speed the fault occurs. If the engine is being operated at too low of a speed under load (lugging), the oil pressure can drop below the engine protection limits because of oil temperature.
>
> Oil pressure is a function of engine speed, oil level, and regulator function. Operating the engine at a low speed under load will **not** cause the oil pressure to be low unless the oil is hot, the oil level is low, the regulator has malfunctioned, or a loss is occurring somewhere in the system.
>
> A faulty sensor can also cause Fault Code 143.
>
> The number of fault lamps can be reduced to two for certain OEMs. In this case, the engine protection and stop lamps are wired together as a red lamp. The warning lamp remains an amber lamp.
>
> Refer to Troubleshooting Fault Code t05-143
