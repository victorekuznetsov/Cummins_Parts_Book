---
aliases:
  - "Цепь датчика температуры наружного воздуха"
type: "Процедура"
doc: "82-fc256"
title_en: "Ambient Air Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры наружного воздуха"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc256.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc256.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Ambient Air Temperature Sensor Circuit
**Цепь датчика температуры наружного воздуха**

> [!abstract] Процедура · `82-fc256`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc256.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc256.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 256

### Цепь датчика температуры наружного воздуха

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 256 PID(P): P171 SPN: 171 ФМИ: 4/4 лампы: Желтая СТО: | Низкое напряжение, обнаруженное в контуре температуры окружающего воздуха. | Никакого влияния на производительность двигателя. Функция перекрытия температуры окружающего воздуха при холостом отключении будет использовать значение датчика температуры воздуха впускного коллектора для определения отключения холостого хода и доступности перекрытия (автомобильного **только**). |

![[19802766.png]]

Цепь датчика температуры наружного воздуха

### Описание цепи

Датчик температуры окружающего воздуха используется электронным модулем управления (ECM) для мониторинга температуры окружающего воздуха. Сигнал температуры окружающего воздуха используется ECM для переопределения температуры окружающего воздуха при холостом отключении и функций ICONTM.

### Расположение компонента

Расположение датчика температуры окружающего воздуха зависит от OEM. См. руководство изготовителя машины по диагностике и ремонту.

### Практические замечания

Сопротивление датчика изменяется в зависимости от температуры. Чтение, которое вы наблюдаете, должно быть сравнимо с этой таблицей:

| Температура (°C) | Температура \[°F\] | Сопротивление (Омс) |
|---|---|---|
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

См. Код устранения неполадок t05-256


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 256
>
> ### Ambient Air Temperature Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 256 PID(P): P171 SPN: 171 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected at the ambient air temperature circuit. | No effect on engine performance. The idle shutdown ambient air temperature override feature will use the intake manifold air temperature sensor value to determine idle shutdown and availability of override (automotive **only**). |
>
> Ambient Air Temperature Sensor Circuit
>
> ### Circuit Description
>
> The ambient air temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the ambient air. The ambient air temperature signal is used by the ECM for the idle shutdown ambient air temperature override and ICON™ features.
>
> ### Component Location
>
> The ambient air temperature sensor location is OEM-dependent. Refer to the OEM troubleshooting and repair manual.
>
> ### Shoptalk
>
> The resistance of the sensor varies with the temperature. The reading you observe should compare to this table:
>
> | Temperature (°C) | Temperature \[°F\] | Resistance (ohms) |
> |---|---|---|
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> Refer to Troubleshooting Fault Code t05-256
