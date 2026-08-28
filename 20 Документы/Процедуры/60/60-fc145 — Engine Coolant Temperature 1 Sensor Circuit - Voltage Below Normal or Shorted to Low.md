---
aliases:
  - "Цепь датчика температуры ОЖ 1 — напряжение ниже нормы"
type: "Процедура"
doc: "60-fc145"
title_en: "Engine Coolant Temperature 1 Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика температуры ОЖ 1 — напряжение ниже нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc145.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc145.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Coolant Temperature 1 Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика температуры ОЖ 1 — напряжение ниже нормы**

> [!abstract] Процедура · `60-fc145`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc145.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc145.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 145

### Цепь датчика температуры ОЖ 1 — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 145 PID (P): P110 SPN: 110 FMI: 4/4 лампы: Янтарная СРТ: | Низкое напряжение сигнала, обнаруженное в цепи температуры охлаждающей жидкости двигателя. | Вентилятор будет оставаться включенным, если он контролируется модулем управления двигателем (ECM). |

![[19a00848.png]]

Схема датчика температуры двигателя

### Описание цепи

Датчик температуры охлаждающей жидкости двигателя представляет собой датчик переменного резистора, используемый ECM для мониторинга температуры охлаждающей жидкости двигателя. Датчик температуры охлаждающей жидкости двигателя имеет две схемы: сигнал и обратные цепи. Напряжение сигнала указывает на температуру охлаждающей жидкости.

### Расположение компонента

Датчик температуры охлаждающей жидкости двигателя расположен на корпусе термостата.

### Условия выполнения диагностики

Эта диагностика выполняется постоянно, пока контроллер генераторной установки активен или двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала датчика температуры охлаждающей жидкости двигателя было за пределами диапазона низкого.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

- Значение по умолчанию используется для считывания температуры охлаждающей жидкости двигателя.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный датчик температуры охлаждающей жидкости двигателя

- Неисправный или повреждённый жгут проводов двигателя.

См. код 145 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 145
>
> ### Engine Coolant Temperature 1 Sensor Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 145 PID(P): P110 SPN: 110 FMI: 4/4 Lamp: Amber SRT: | Low signal voltage detected at engine coolant temperature circuit. | Fan will stay ON if controlled by the engine control module (ECM). |
>
> Engine Coolant Temperature Sensor Circuit
>
> ### Circuit Description
>
> The engine coolant temperature sensor is a variable resistor sensor used by the ECM to monitor the engine coolant temperature. The engine coolant temperature sensor has two circuits: signal, and return circuits. The signal voltage indicates the coolant temperature.
>
> ### Component Location
>
> The engine coolant temperature sensor is located on the thermostat housing.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected that the engine coolant temperature sensor signal voltage was out of range low.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> - A default value is used for the engine coolant temperature reading.
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
> - Malfunctioning engine coolant temperature sensor
>
> - Malfunctioning or damaged engine wiring harness.
>
> Refer to Troubleshooting Fault Code 145.
