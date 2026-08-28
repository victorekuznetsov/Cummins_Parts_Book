---
aliases:
  - "Цепь датчика температуры коллектора 2 — напряжение выше нормы"
type: "Процедура"
doc: "60-fc156"
title_en: "Intake Manifold 2 Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика температуры коллектора 2 — напряжение выше нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc156.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc156.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Intake Manifold 2 Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика температуры коллектора 2 — напряжение выше нормы**

> [!abstract] Процедура · `60-fc156`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc156.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc156.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 156

### Цепь датчика температуры коллектора 2 — напряжение выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 156 P(P): СПН: 1131 FMI: 3/3 лампы: Янтарная СРТ: | Высокое напряжение сигнала, обнаруженное в цепи датчика температуры впускного коллектора 2. | Ни одного на выступление. |

![[19a00850.png]]

Схема датчика температуры Manifold 2

### Описание цепи

Датчик температуры впускного коллектора представляет собой датчик переменного резистора, используемый ECM для мониторинга температуры впускного коллектора. Датчик температуры впускного коллектора имеет две схемы: сигнал и обратные цепи. Напряжение сигнала указывает на температуру впускного коллектора.

### Расположение компонента

Датчик температуры впускного коллектора 2 расположен в правом береге заднего коллектора воздухозаборника.

### Условия выполнения диагностики

Эта диагностика выполняется постоянно, пока контроллер генераторной установки активен или двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала датчика температуры 2 впускного коллектора находится вне диапазона.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

- Отсутствие защиты двигателя от температуры воздуха впускного коллектора.

- Значение по умолчанию используется для показания температуры впускного коллектора.

- Выходной крутящий момент двигателя будет уменьшен.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении электронного инструментария или эквивалента Cummins®. При устранении неисправности кода используйте адрес источника, отображаемый в инструменте электронного обслуживания Cummins® или эквивалент, чтобы определить, какая ECM и схема затронута.

Возможные причины этого кода неисправности:

- Неисправный датчик температуры впускного коллектора 2.

- Неисправный или повреждённый жгут проводов двигателя.

См. Код 156 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 156
>
> ### Intake Manifold 2 Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 156 PID(P): SPN: 1131 FMI: 3/3 Lamp: Amber SRT: | High signal voltage detected at intake manifold 2 temperature sensor circuit. | None on performance. |
>
> Intake Manifold 2 Temperature Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold temperature sensor is a variable resistor sensor used by the ECM to monitor the intake manifold temperature. The intake manifold temperature sensor has two circuits: signal, and return circuits. The signal voltage indicates the intake manifold temperature.
>
> ### Component Location
>
> The intake manifold 2 temperature sensor is located in the right bank rear air intake manifold.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the intake manifold 2 temperature sensor signal voltage is out of range high.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> - No engine protection for intake manifold air temperature.
>
> - A default value is used for the intake manifold temperature reading.
>
> - The torque output of the engine will be reduced.
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
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.
>
> Possible causes of this fault code include:
>
> - Malfunctioning intake manifold 2 temperature sensor.
>
> - Malfunctioning or damaged engine wiring harness.
>
> Refer to Troubleshooting Fault Code 156.
