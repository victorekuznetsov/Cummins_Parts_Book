---
aliases:
  - "Температура во впускном коллекторе 2 выше нормы — наивысший уровень"
type: "Процедура"
doc: "60-fc158"
title_en: "Intake Manifold 2 Temperature - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Температура во впускном коллекторе 2 выше нормы — наивысший уровень"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc158.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc158.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Intake Manifold 2 Temperature - Data Valid But Above Normal Operating Range - Most Severe Level
**Температура во впускном коллекторе 2 выше нормы — наивысший уровень**

> [!abstract] Процедура · `60-fc158`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc158.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc158.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 158

### Температура во впускном коллекторе 2 выше нормы — наивысший уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 158 PID (P): СПН: 1131 FMI: 0/0 лампа: Красная СТО: | Температура впускного коллектора 2 выше критического предела защиты двигателя. | Двигатель отключится. |

![[19a00850.png]]

Манифольд 2 давления/температурный датчик

### Описание цепи

Датчик температуры впускного коллектора представляет собой датчик переменного резистора, используемый ECM для мониторинга температуры впускного коллектора. Датчик температуры впускного коллектора имеет две схемы: сигнал и обратные цепи. Напряжение сигнала указывает на температуру впускного коллектора.

### Расположение компонента

Датчик температуры впускного коллектора 2 расположен в правом береге заднего коллектора воздухозаборника.

### Условия выполнения диагностики

Эта диагностика выполняется постоянно, пока контроллер генераторной установки активен или двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что температура впускного коллектора 2 была выше предела защиты двигателя.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки отображает неисправность выключения сразу же, когда диагностика работает и выходит из строя.

- Двигатель будет отключен.

- Значение по умолчанию используется для показания температуры впускного коллектора.

- Выходной крутящий момент двигателя будет уменьшен.

### Условия сброса кода неисправности

- Для проверки ремонта, работайте с двигателем под нагрузкой не менее 5 минут.

- Контроллер генераторной установки отключит индикатор выключения сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении электронного инструментария или эквивалента Cummins®. При устранении неисправности кода используйте адрес источника, отображаемый в инструменте электронного обслуживания Cummins® или эквивалент, чтобы определить, какая ECM и схема затронута.

Возможные причины этого кода неисправности:

- Ограниченный поток воздуха через охладитель заряда воздуха

- Низкий уровень охлаждающей жидкости

- Недостаточный охладитель

- Высокая температура розетки компрессора турбокомпрессора.

См. Код 158 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 158
>
> ### Intake Manifold 2 Temperature - Data Valid But Above Normal Operating Range - Most Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 158 PID(P): SPN: 1131 FMI: 0/0 Lamp: Red SRT: | Intake manifold 2 temperature above engine protection critical limit. | Engine will shut down. |
>
> Intake Manifold 2 Pressure/Temperature Sensor Circuit
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
> The Engine Control Module (ECM) detected the intake manifold 2 temperature was greater than the engine protection limit.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.
>
> - The engine will be shut down.
>
> - A default value is used for the intake manifold temperature reading.
>
> - The torque output of the engine will be reduced.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, operate the engine under load for at least 5 minutes.
>
> - The generator set controller will turn off the shutdown indicator immediately after the user presses the reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.
>
> Possible causes of this fault code include:
>
> - Restricted air flow through the charge-air cooler
>
> - Low coolant level
>
> - Undersized aftercooler
>
> - High turbocharger compressor outlet temperature.
>
> Refer to Troubleshooting Fault Code 158.
