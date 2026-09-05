---
type: "Процедура"
doc: "19-fc261"
title_en: "Fuel Temperature - Engine Protection"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc261.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc261.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Fuel Temperature - Engine Protection

> [!abstract] Процедура · `19-fc261`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc261.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc261.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 261

### Температура топлива - защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 261 P(P): P174 SPN: 174 ФМИ: 0 лампочка: Защита двигателя SRT: 00-397 | Выявлена высокая температура топлива. Сигнал напряжения при контакте сигнала температуры топлива 26 с проводкой двигателя указывает температуру топлива выше 71°C \[160°F\]. | Калибровочная зависимость прогрессивной мощности и скорости ухудшается, а выключение двигателя увеличивается с увеличением времени после оповещения. |

![[19800991.png]]

Схема датчика температуры топлива

### Описание цепи

Датчик температуры топлива используется ECM для мониторинга температуры топлива. ECM контролирует напряжение на контакте 26 и преобразует это напряжение в температурное значение. Значение температуры топлива используется ECM для системы защиты двигателя.

### Расположение компонента

Двигатели серии QSK19 - датчик температуры топлива расположен на левой стороне корпуса управляющего клапана, над клапаном отключения топлива. Двигатели серии QSK45 и QSK60 - датчик температуры топлива расположен с правой стороны электронного клапана управления между рельсом и датчиками давления синхронизации. Двигатели серии QSK78 - датчик температуры топлива расположен на правой стороне электронного клапана управления между рельсом и датчиками давления синхронизации.

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

См. Код устранения неполадок t05-261


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 261
>
> ### Fuel Temperature - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 261 PID(P): P174 SPN: 174 FMI: 0 Lamp: Engine Protection SRT: 00-397 | High fuel temperature has been detected. Voltage signal at fuel temperature signal pin 26 of engine harness indicates fuel temperature above 71°C \[160°F\]. | Calibration-dependent progressive power and speed derate and engine shutdown with increasing time after alert. |
>
> Fuel Temperature Sensor Circuit
>
> ### Circuit Description
>
> The fuel temperature sensor is used by the ECM to monitor the temperature of the fuel. The ECM monitors the voltage on pin 26 and converts this voltage to a temperature value. The fuel temperature value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> QSK19 Series engines - The fuel temperature sensor is located on the left side of the control valve body, above the fuel shutoff valve. QSK45 and QSK60 Series engines - The fuel temperature sensor is located on the right side of the electronic control valve assembly between the rail and timing pressure sensors. QSK78 Series engines - The fuel temperature sensor is located on the right side of the electronic control valve assembly between the rail and timing pressure sensors.
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
> Refer to Troubleshooting Fault Code t05-261
