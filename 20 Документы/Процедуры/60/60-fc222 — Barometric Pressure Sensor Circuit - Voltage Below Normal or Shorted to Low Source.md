---
aliases:
  - "Цепь датчика барометрического давления — напряжение ниже нормы"
type: "Процедура"
doc: "60-fc222"
title_en: "Barometric Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика барометрического давления — напряжение ниже нормы"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc222.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc222.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Barometric Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика барометрического давления — напряжение ниже нормы**

> [!abstract] Процедура · `60-fc222`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc222.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc222.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 222

### Цепь датчика барометрического давления — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 222 PID(P): P108 SPN: 108 FMI: 4/4 лампы: Янтарная СРТ: | Низкое напряжение сигнала, обнаруженное в цепи барометрического давления. | Возможно снижение производительности двигателя. |

![[19a00859.png]]

Схема датчика барометрического давления

### Описание цепи

Барометрический датчик давления реагирует на изменения давления в атмосфере. Изменения давления происходят на основании высоты, на которой в настоящее время работает двигатель. Датчик барометрического давления имеет цепь питания 5 вольт, напряжение сигнала датчика и обратную цепь.

### Расположение компонента

Датчик барометрического давления устанавливается на главную ветку электропроводки двигателя на левой стороне двигателя.

### Условия выполнения диагностики

Эта диагностика выполняется постоянно, пока контроллер генераторной установки активен или двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала барометрического давления было вне диапазона низкого.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

- Используется значение по умолчанию для показания барометрического давления.

- Энергетический момент двигателя будет уменьшен, если двигатель работает в течение длительного периода времени с активным разломом.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправность или повреждение датчика барометрического давления.

- Неисправный или повреждённый жгут проводов двигателя.

См. код 222 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 222
>
> ### Barometric Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 222 PID(P): P108 SPN: 108 FMI: 4/4 Lamp: Amber SRT: | Low signal voltage detected at barometric pressure circuit. | Possible reduced engine performance. |
>
> Barometric Pressure Sensor Circuit
>
> ### Circuit Description
>
> The barometric pressure sensor responds to pressure changes in the atmospheric pressure. The pressure changes occur based on the elevation where the engine is presently operating. The barometric pressure sensor has a 5 volt supply circuit, a sensor signal voltage, and a return circuit.
>
> ### Component Location
>
> The barometric pressure sensor is mounted on the main branch of the engine harness on the left side of the engine.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the barometric pressure signal voltage was out of range low.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> - A default value for the barometric pressure reading is used.
>
> - Engine torque will be reduced if the engine is operated for an extended period of time with this fault active.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, start the engine and let it run for 1 minute at no load.
>
> - The generator set controller will turn off the warning indicator immediately after the user presses reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged barometric pressure sensor.
>
> - Malfunctioning or damaged engine wiring harness.
>
> Refer to Troubleshooting Fault Code 222.
