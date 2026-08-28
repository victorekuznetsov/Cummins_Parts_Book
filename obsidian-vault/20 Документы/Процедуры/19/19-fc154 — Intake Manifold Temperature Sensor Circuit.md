---
aliases:
  - "Цепь датчика температуры во впускном коллекторе"
type: "Процедура"
doc: "19-fc154"
title_en: "Intake Manifold Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры во впускном коллекторе"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc154.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc154.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Intake Manifold Temperature Sensor Circuit
**Цепь датчика температуры во впускном коллекторе**

> [!abstract] Процедура · `19-fc154`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc154.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc154.pdf)

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
| Код неисправности: 154 PID(P): P105 SPN: 105 FMI: 4 лампы: Желтая СТО: 00-359 | Менее 0,08 VDC обнаруживается при контакте 23 впускного коллектора с температурным сигналом воздуха проводной ремни двигателя. | Отсутствие защиты двигателя от температуры воздуха впускного коллектора. |

![[19400062.png]]

Цепь датчика температуры во впускном коллекторе

### Описание цепи

Датчик температуры впускного коллектора используется ECM для мониторинга температуры воздуха в впускном коллекторе ниже по течению от элемента послеохладителя. Датчик температуры впускного коллектора используется ECM для системы защиты двигателя и контроля времени и заправки. ECM контролирует напряжение на контакте 23. ECM ожидает, что напряжение будет варьироваться от 0,5 до 4,5 VDC. Если напряжение ниже 0,08 VDC, то ECM регистрирует код 154 по умолчанию. Напряжение ниже 0,08 VDC при контакте 23 может быть вызвано шортами, которые заземляются на проводах подачи или возврата, или внутренним заземленным датчиком.

### Расположение компонента

Двигатели серии QSK19 - датчик температуры впускного коллектора расположен над топливным насосом, рядом с датчиком давления впускного коллектора.

### Практические замечания

Все температурные датчики:

- Сопротивление датчика изменяется в зависимости от температуры. Считывание, которое вы наблюдаете, может сравниться со следующей таблицей, если датчик работает должным образом.

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
> | Fault Code: 154 PID(P): P105 SPN: 105 FMI: 4 Lamp: Yellow SRT: 00-359 | Less than 0.08 VDC detected at the intake manifold air temperature signal pin 23 of the engine harness. | No engine protection for the intake manifold air temperature. |
>
> Intake Manifold Temperature Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold temperature sensor is used by the ECM to monitor the temperature of the air in the intake manifold downstream of the aftercooler element. The intake manifold temperature sensor is used by the ECM for the engine protection system and timing and fueling control. The ECM monitors the voltage on pin 23. The ECM expects to see the voltage vary between 0.5 and 4.5 VDC. If the voltage is below 0.08 VDC, then the ECM will log Fault Code 154. Voltage below 0.08 VDC on pin 23 can be caused by shorts to ground on the supply or return wires, or an internally grounded, failed sensor.
>
> ### Component Location
>
> QSK19 series engines - The intake manifold temperature sensor is located above the fuel pump, next to the intake manifold pressure sensor.
>
> ### Shoptalk
>
> All temperature sensors:
>
> - The resistance of the sensor varies with the temperature. The reading that you observe could possibly compare to the following table if the sensor is functioning properly.
>
> | Temperature(°C) | Temperature\[°F\] | Resistance(ohms) |
> |---|---|---|
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> Refer to Troubleshooting Fault Code t05-154
