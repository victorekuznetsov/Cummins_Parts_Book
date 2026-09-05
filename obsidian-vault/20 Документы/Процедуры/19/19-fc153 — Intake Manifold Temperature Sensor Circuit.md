---
aliases:
  - "Цепь датчика температуры во впускном коллекторе"
type: "Процедура"
doc: "19-fc153"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc153.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc153.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Intake Manifold Temperature Sensor Circuit
**Цепь датчика температуры во впускном коллекторе**

> [!abstract] Процедура · `19-fc153`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc153.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc153.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 153

### Цепь датчика температуры во впускном коллекторе

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 153 P(P): P105 SPN: 105 FMI: 3 лампы: Желтая СТО: 00-358 | Более 4,88 ВДК обнаружено при впускном коллекторе температурного датчика контакта 23 проводов двигателя с ремешком разъема ECM. | Отсутствие защиты двигателя от температуры воздуха впускного коллектора. |

![[19400062.png]]

Цепь датчика температуры во впускном коллекторе

### Описание цепи

Датчик температуры впускного коллектора используется ECM для мониторинга температуры воздуха в впускном коллекторе после охладителя. Датчик температуры впускного коллектора используется ECM для системы защиты двигателя, управления временем и заправкой. ECM контролирует напряжение на контакте 23. ECM ожидает, что напряжение будет варьироваться от 0,5 до 4,88 VDC. Если напряжение выше 4,88 VDC, ECM регистрирует код 153 ошибки. Напряжение выше 4,88 VDC на контакте 23 может быть вызвано отверстиями в сигнальных или обратных проводах, шортами напряжения на сигнальных или обратных проводах или неисправным открытым датчиком.

### Расположение компонента

Двигатели серии QSK19 - датчик температуры впускного коллектора расположен над топливным насосом, рядом с датчиком давления впускного коллектора.

### Практические замечания

- Сопротивление всех датчиков температуры изменяется в зависимости от температуры. Считывание, которое вы наблюдаете, может сравниться со следующей таблицей, если датчик работает должным образом.

| Температура (°C) | Температура \[°F\] | Сопротивление (Омс) |
|---|---|---|
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

Устранение неполадок код t05-153


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 153
>
> ### Intake Manifold Temperature Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 153 PID(P): P105 SPN: 105 FMI: 3 Lamp: Yellow SRT: 00-358 | More than 4.88 VDC detected at the intake manifold temperature sensor signal pin 23 of the engine harness ECM connector. | No engine protection for the intake manifold air temperature. |
>
> Intake Manifold Temperature Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold temperature sensor is used by the ECM to monitor the temperature of the air in the intake manifold after the aftercooler. The intake manifold temperature sensor is used by the ECM for the engine protection system, timing, and fueling control. The ECM monitors the voltage on pin 23. The ECM expects to see the voltage vary between 0.5 and 4.88 VDC. If the voltage is above 4.88 VDC, the ECM will log Fault Code 153. Voltage above 4.88 VDC on pin 23 can be caused by openings in the signal or return wires, voltage shorts to the signal or return wires, or a failed open sensor.
>
> ### Component Location
>
> QSK19 series engines - The intake manifold temperature sensor is located above the fuel pump, next to the intake manifold pressure sensor.
>
> ### Shoptalk
>
> - The resistance of all the temperature sensors varies with the temperature. The reading that you observe could possibly compare to the following table if the sensor is functioning properly.
>
> | Temperature(°C) | Temperature\[°F\] | Resistance(ohms) |
> |---|---|---|
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> Refer to Troubleshooting Fault Code t05-153
