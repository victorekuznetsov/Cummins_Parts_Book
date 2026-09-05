---
aliases:
  - "Датчик температуры впускного коллектора — защита двигателя"
type: "Процедура"
doc: "87-fc155"
title_en: "Intake Manifold Temperature Sensor - Engine Protection"
title_ru: "Датчик температуры впускного коллектора — защита двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc155.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc155.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Intake Manifold Temperature Sensor - Engine Protection
**Датчик температуры впускного коллектора — защита двигателя**

> [!abstract] Процедура · `87-fc155`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc155.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc155.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 155

### Датчик температуры впускного коллектора — защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 155 P(P): P105 SPN: 105 FMI: 0 лампочка: Защита двигателя SRT: | Была обнаружена высокая температура впускного коллектора воздуха. Сигнал напряжения при контакте 34 датчика температуры воздуха впускного коллектора указывает температуру воздуха впускного коллектора выше калиброванного значения 104°C \[219°F\]. | В зависимости от калибровки, прогрессивная мощность и скорость ухудшаются, а двигатель отключается по мере повышения температуры над порогами. |

![[19900359.png]]

Цепь датчика температуры во впускном коллекторе

### Описание цепи

Датчик температуры впускного коллектора используется электронным модулем управления (ECM) для мониторинга температуры воздуха в впускном коллекторе после охладителя. Датчик температуры впускного коллектора используется ECM для системы защиты двигателя, управления временем и заправкой. ECM контролирует напряжение на контакте 34. ECM ожидает, что напряжение будет варьироваться от 0,5 до 4,5 VDC.

### Расположение компонента

Два датчика температуры впускного коллектора используются на промышленном двигателе QST30, по одному с каждой стороны. Датчики расположены в впускном коллекторе в задней части двигателя.

### Практические замечания

Напряжение сигнала изменяется между 0,5 и 4,5 ВДК, так как внутреннее сопротивление датчика изменяется из-за изменения температуры охлаждающей жидкости. Когда напряжение сигнала датчика указывает на температуру, превышающую установленный предел, код 155 по умолчанию регистрируется.

На следующей диаграмме показано сопротивление датчика температуры впускного коллектора при различных показаниях температуры.

| Температура (°C) | Температура \[°F\] | Сопротивление (Омс) |
|---|---|---|
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

Примечание: Количество неисправных ламп может быть сокращено до двух для некоторых OEM-производителей. Защита двигателя и стоп-сигналы соединены вместе как красная лампа. Предупреждающая лампа остается желтой лампой.

Устранение неполадок код t05-155


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 155
>
> ### Intake Manifold Temperature Sensor - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 155 PID(P): P105 SPN: 105 FMI: 0 Lamp: Engine Protection SRT: | High intake air manifold temperature has been detected. Voltage signal at intake manifold air temperature sensor signal pin 34 indicates intake manifold air temperature above the calibrated value 104°C \[219°F\]. | Depending on the calibration, a progressive power and speed derate and engine shutdown as the temperature increases over thresholds. |
>
> Intake Manifold Temperature Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the air in the intake manifold after the aftercooler. The intake manifold temperature sensor is used by the ECM for the engine protection system, timing, and fueling control. The ECM monitors the voltage on pin 34. The ECM expects to see the voltage vary between 0.5 and 4.5 VDC.
>
> ### Component Location
>
> Two intake manifold temperature sensors are used on the QST30 industrial engine, one on each side. The sensors are located in the intake manifold at the rear of the engine.
>
> ### Shoptalk
>
> The signal voltage varies between 0.5 and 4.5 VDC as the internal resistance of the sensor changes due to changing coolant temperature. When the sensor signal voltage indicates a temperature exceeding a set limit, Fault Code 155 is logged.
>
> The following chart shows resistance of the intake manifold temperature sensor at various temperature readings.
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
> Refer to Troubleshooting Fault Code t05-155
