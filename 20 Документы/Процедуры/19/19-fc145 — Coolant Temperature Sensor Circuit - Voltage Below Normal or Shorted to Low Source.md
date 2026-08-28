---
aliases:
  - "Цепь датчика температуры ОЖ — напряжение ниже нормы"
type: "Процедура"
doc: "19-fc145"
title_en: "Coolant Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика температуры ОЖ — напряжение ниже нормы"
modified: "2010-08-19"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc145.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc145.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Coolant Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика температуры ОЖ — напряжение ниже нормы**

> [!abstract] Процедура · `19-fc145`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-08-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc145.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc145.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 145

### Цепь датчика температуры ОЖ — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 145 PID (P): P110 SPN: 110 FMI: 4 лампы: Желтая СТО: 00-356 | Цепь датчика температуры ОЖ — напряжение ниже нормы | Возможен белый дым. Отсутствие защиты двигателя от температуры охлаждающей жидкости. Система Centinel может быть отключена. |

![[19400019.png]]

Цепь датчика температуры охлаждающей жидкости

### Описание цепи

Датчик температуры охлаждающей жидкости двигателя используется электронным модулем управления (ECM) для мониторинга температуры охлаждающей жидкости двигателя. Температура охлаждающей жидкости двигателя используется ECM для системы защиты двигателя, управления временем и заправкой.

### Расположение компонента

Датчик температуры охлаждающей жидкости расположен на стороне корпуса термостата на большинстве применений. См. раздел E для подробного описания местоположения компонента.

### Практические замечания

Все температурные датчики:

| Температура (°C) | Температура (°F) | Сопротивление (Омс) |
|---|---|---|
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

Сопротивление датчика варьируется в зависимости от температуры. Сравнение показаний, которые вы наблюдаете, со столом, заключается в том, что датчик работает правильно.

Код 145 ошибки может быть вызван следующим:

- Открытая линия напряжения

- Сигнальная линия, сокращенная до земли

- Короткий сенсор.

Устранение неполадок код t05-145


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 145
>
> ### Coolant Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 145 PID(P): P110 SPN: 110 FMI: 4 Lamp: Yellow SRT: 00-356 | Coolant Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source | Possible white smoke. No engine protection for coolant temperature. Centinel system may be disabled. |
>
> Coolant Temperature Sensor Circuit
>
> ### Circuit Description
>
> The engine coolant temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The engine coolant temperature is used by the ECM for the engine protection system, timing, and fueling control.
>
> ### Component Location
>
> The coolant temperature sensor is located on the side of the thermostat housing on most applications. Refer to Section E for a detailed component location view.
>
> ### Shoptalk
>
> All temperature sensors:
>
> | Temperature (°C) | Temperature (°F) | Resistance (ohms) |
> |---|---|---|
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> The resistance of the sensor varies with temperature. The reading that you observe will compare to the table is the sensor is functioning properly.
>
> Fault Code 145 can be caused by the following:
>
> - Open voltage line
>
> - Signal line shorted to ground
>
> - Shorted sensor.
>
> Refer to Troubleshooting Fault Code t05-145
