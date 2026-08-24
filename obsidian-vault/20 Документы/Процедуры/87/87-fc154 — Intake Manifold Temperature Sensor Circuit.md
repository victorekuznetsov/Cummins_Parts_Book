---
aliases:
  - "Цепь датчика температуры во впускном коллекторе"
type: "Процедура"
doc: "87-fc154"
title_en: "Intake Manifold Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры во впускном коллекторе"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc154.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc154.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Intake Manifold Temperature Sensor Circuit
**Цепь датчика температуры во впускном коллекторе**

> [!abstract] Процедура · `87-fc154`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc154.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc154.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 154

### Цепь датчика температуры во впускном коллекторе

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 154 PID(P): P105 SPN: ФМИ: 4 лампы: Желтая СТО: | Менее 0,05 VDC обнаруживается при контакте датчика температуры впускного коллектора 34 разъема электронного модуля управления (ECM) проводов двигателя. | Защита двигателя от температуры воздуха впускного коллектора отключена. |

![[19900359.png]]

Цепь датчика температуры во впускном коллекторе

### Описание цепи

Датчик температуры впускного коллектора используется ECM для мониторинга температуры воздуха в впускном коллекторе ниже по течению от элемента послеохладителя. Датчик температуры впускного коллектора используется ECM для системы защиты двигателя и контроля времени и заправки.

ECM контролирует напряжение на контакте 34. ECM ожидает, что напряжение будет варьироваться от 0,5 до 4,5 VDC. Если напряжение ниже 0,05 VDC, ECM регистрирует код 154 ошибки.

Напряжение ниже 0,05 VDC на контакте 34 может быть вызвано короткими замыканиями для заземления на податочных или обратных проводах или внутренне заземленным датчиком.

### Расположение компонента

Два датчика температуры впускного коллектора используются на промышленном двигателе QST30, по одному с каждой стороны. Датчики расположены в впускном коллекторе в задней части двигателя.

### Практические замечания

Сопротивление датчика изменяется в зависимости от температуры. Считывание, которое вы наблюдаете, должно быть сопоставимо со следующей таблицей, если датчик работает должным образом.

| Температура (°C) | Температура \[°F\] | Сопротивление (Омс) |
|---|---|---|
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

Устранение неполадок код t05-154


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 154
>
> ### Intake Manifold Temperature Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 154 PID(P): P105 SPN: FMI: 4 Lamp: Yellow SRT: | Less than 0.05 VDC detected at the intake manifold temperature sensor signal pin 34 of the engine harness electronic control module (ECM) connector. | Engine protection for the intake manifold air temperature is disabled. |
>
> Intake Manifold Temperature Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold temperature sensor is used by the ECM to monitor the temperature of the air in the intake manifold downstream of the aftercooler element. The intake manifold temperature sensor is used by the ECM for the engine protection system and timing and fueling control.
>
> The ECM monitors the voltage on pin 34. The ECM expects to see the voltage vary between 0.5 and 4.5 VDC. If the voltage is below 0.05 VDC, the ECM will log Fault Code 154.
>
> Voltage below 0.05 VDC on pin 34 can be caused by short circuits to ground on the supply or return wires, or an internally grounded, failed sensor.
>
> ### Component Location
>
> Two intake manifold temperature sensors are used on the QST30 industrial engine, one on each side. The sensors are located in the intake manifold at the rear of the engine.
>
> ### Shoptalk
>
> The resistance of the sensor varies with the temperature. The reading you observe should compare to the following table if the sensor is functioning properly.
>
> | Temperature (°C) | Temperature \[°F\] | Resistance (ohms) |
> |---|---|---|
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> Refer to Troubleshooting Fault Code t05-154
