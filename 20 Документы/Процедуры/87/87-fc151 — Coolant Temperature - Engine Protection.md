---
aliases:
  - "Температура охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "87-fc151"
title_en: "Coolant Temperature - Engine Protection"
title_ru: "Температура охлаждающей жидкости — защита двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc151.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc151.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Coolant Temperature - Engine Protection
**Температура охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `87-fc151`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc151.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc151.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 151

### Температура охлаждающей жидкости — защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 151 PID(P): P110 SPN: 110 FMI: 0 лампочка: Защита двигателя SRT: | Выявлена высокая температура охлаждающей жидкости. Сигнал напряжения при контакте 23 с температурой охлаждающей жидкости указывает, что температура охлаждающей жидкости выше калиброванного значения 100°C \[212°F\]. | Калибровочная зависимость прогрессивной мощности и скорости ухудшается, а двигатель отключается по мере повышения температуры над порогами. |

![[19900358.png]]

Цепь датчика температуры охлаждающей жидкости

### Описание цепи

Датчик температуры охлаждающей жидкости используется электронным модулем управления (ECM) для мониторинга температуры охлаждающей жидкости двигателя. Температура охлаждающей жидкости используется ECM для системы защиты двигателя, управления временем и заправкой.

ECM контролирует напряжение на контакте 23. ECM ожидает, что напряжение будет варьироваться от 0,5 до 4,5 VDC.

### Расположение компонента

Датчик температуры охлаждающей жидкости расположен на левой стороне двигателя в корпусе термостата.

### Практические замечания

Напряжение сигнала изменяется между 0,5 и 4,5 ВДК, так как внутреннее сопротивление датчика изменяется из-за изменения температуры охлаждающей жидкости. Когда напряжение сигнала датчика указывает на температуру, превышающую установленный предел, код 151 по умолчанию регистрируется.

- Убедитесь, что поток воздуха через радиатор не затрудняется.

- Сопротивление всех датчиков температуры изменяется в зависимости от температуры. Считывание, которое вы наблюдаете, должно быть сопоставимо со следующей таблицей, если датчик работает должным образом.

| Температура (°C) | Температура \[°F\] | Сопротивление (Омс) |
|---|---|---|
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

Примечание: Количество неисправных ламп может быть сокращено до двух для некоторых OEM-производителей. Защита двигателя и стоп-сигналы соединены вместе как красная лампа. Предупреждающая лампа остается желтой лампой.

Устранение неполадок код t05-151


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 151
>
> ### Coolant Temperature - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 151 PID(P): P110 SPN: 110 FMI: 0 Lamp: Engine Protection SRT: | High coolant temperature has been detected. Voltage signal at coolant temperature signal pin 23 indicates the coolant temperature is above the calibrated value 100°C \[212°F\]. | Calibration-dependent progressive power and speed derate and engine shutdown as temperature increases over thresholds. |
>
> Coolant Temperature Sensor Circuit
>
> ### Circuit Description
>
> The coolant temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system, timing, and fueling control.
>
> The ECM monitors the voltage on pin 23. The ECM expects to see the voltage vary between 0.5 and 4.5 VDC.
>
> ### Component Location
>
> The coolant temperature sensor is located on the left side of the engine in the thermostat housing.
>
> ### Shoptalk
>
> The signal voltage varies between 0.5 and 4.5 VDC as the internal resistance of the sensor changes due to changing coolant temperature. When the sensor signal voltage indicates a temperature exceeding a set limit, Fault Code 151 is logged.
>
> - Make sure the airflow through the radiator is **not** obstructed.
>
> - The resistance of all the temperature sensors varies with the temperature. The reading you observe should compare to the following table if the sensor is functioning properly.
>
> | Temperature (°C) | Temperature \[°F\] | Resistance (ohms) |
> |---|---|---|
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> Note: The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.
>
> Refer to Troubleshooting Fault Code t05-151
