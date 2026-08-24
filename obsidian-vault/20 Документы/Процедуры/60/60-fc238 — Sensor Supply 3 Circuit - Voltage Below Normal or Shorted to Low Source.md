---
aliases:
  - "Цепь питания датчиков 3 — напряжение ниже нормы"
type: "Процедура"
doc: "60-fc238"
title_en: "Sensor Supply 3 Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь питания датчиков 3 — напряжение ниже нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc238.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc238.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Sensor Supply 3 Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь питания датчиков 3 — напряжение ниже нормы**

> [!abstract] Процедура · `60-fc238`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc238.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc238.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 238

### Цепь питания датчиков 3 — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 238 P(P): S232 SPN: 3511 FMI: 4/4 лампы: Янтарная СРТ: | Низкое напряжение, обнаруженное на цепи питания датчика 3. | Возможные снижение производительности двигателя, выключение или потеря защиты двигателя. |

![[19a00864.png]]

Сенсорная схема 3

### Описание цепи

Схемы подачи датчика модуля управления двигателем (ECM) обеспечивают подачу 5 вольт на различные датчики на ремне электропроводки двигателя.

### Расположение компонента

Схема подачи датчика 3 расположена в жгуте проводов двигателя.

### Условия выполнения диагностики

Эта диагностика выполняется постоянно, пока контроллер генераторной установки активен или двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала датчика питания 3 было вне диапазона низкого.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении электронного инструментария или эквивалента Cummins®. При устранении неисправности кода используйте адрес источника, отображаемый в инструменте электронного обслуживания Cummins® или эквивалент, чтобы определить, какая ECM и схема затронута.

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

- Поврежденные или рыхлые связи.

- Неисправный датчик

См. Код 238 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 238
>
> ### Sensor Supply 3 Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 238 PID(P): S232 SPN: 3511 FMI: 4/4 Lamp: Amber SRT: | Low voltage detected at the sensor supply 3 circuit. | Possible reduced engine performance, shutdown or loss of engine protection. |
>
> Sensor Supply 3 Circuit
>
> ### Circuit Description
>
> The sensor supply circuits of the engine control module (ECM) provides a 5 volt supply to various sensors on the engine wiring harness.
>
> ### Component Location
>
> The sensor supply 3 circuit is located in the engine wiring harness.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the sensor supply 3 signal voltage was out of range low.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
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
> - Malfunctioning or damaged engine wiring harness.
>
> - Damaged or loose connections.
>
> - Malfunctioning sensor
>
> Refer to Troubleshooting Fault Code 238.
