---
aliases:
  - "Цепь датчика давления коллектора 2 — напряжение ниже нормы"
type: "Процедура"
doc: "60-fc1386"
title_en: "Intake Manifold 2 Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика давления коллектора 2 — напряжение ниже нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1386.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1386.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Intake Manifold 2 Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика давления коллектора 2 — напряжение ниже нормы**

> [!abstract] Процедура · `60-fc1386`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1386.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1386.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1386

### Цепь датчика давления коллектора 2 — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1386 PID(P): СПН: 1128 FMI: 4/4 лампы: Обслуживание SRT: | Низкое напряжение сигнала, обнаруженное на цепи датчика давления впускного коллектора 2. | Возможно снижение производительности двигателя. |

![[19a00895.png]]

Схема датчика давления Manifold 2.

### Описание цепи

Датчик давления впускного коллектора представляет собой датчик переменного сопротивления, используемый ECM для мониторинга давления впускного коллектора. Датчик давления впускного коллектора имеет три схемы: 5-вольтная цепь подачи, возврата и сигнала. Напряжение цепи сигнала указывает на заряженное давление воздуха во впускном коллекторе.

### Расположение компонента

Датчик давления впускного коллектора 2 расположен в левобережном впускном коллекторе.

### Условия выполнения диагностики

Эта диагностика выполняется постоянно, пока контроллер генераторной установки активен или двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала датчика давления 2 впускного коллектора находится вне диапазона низкого.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

- Датчик давления 1 впускного коллектора используется для считывания давления впускного коллектора.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении электронного инструментария или эквивалента Cummins®. При устранении неисправности кода используйте адрес источника, отображаемый в инструменте электронного обслуживания Cummins® или эквивалент, чтобы определить, какая ECM и схема затронута.

Возможные причины этого кода неисправности:

- Неисправный датчик давления впускного коллектора 2.

- Неисправный или повреждённый жгут проводов двигателя.

См. код 1386 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1386
>
> ### Intake Manifold 2 Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1386 PID(P): SPN: 1128 FMI: 4/4 Lamp: Maintenance SRT: | Low signal voltage detected at the intake manifold 2 pressure sensor circuit. | Possible reduced engine performance. |
>
> Intake Manifold 2 Pressure Sensor Circuit.
>
> ### Circuit Description
>
> The intake manifold pressure sensor is a variable resistance sensor used by the ECM to monitor the intake manifold pressure. The intake manifold pressure sensor has three circuits: 5 volt supply, return and signal circuits. The signal circuit voltage indicates the charged air pressure in the intake manifold.
>
> ### Component Location
>
> The intake manifold 2 pressure sensor is located in the left bank intake manifold.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the intake manifold 2 pressure sensor signal voltage is out of range low.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> - Intake manifold 1 pressure sensor is used for intake manifold pressure reading.
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
> - Malfunctioning intake manifold 2 pressure sensor.
>
> - Malfunctioning or damaged engine wiring harness.
>
> Refer to Troubleshooting Fault Code 1386.
