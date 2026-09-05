---
aliases:
  - "Цепь питания датчиков 2 — напряжение выше нормы или замыкание на плюс"
type: "Процедура"
doc: "60-fc227"
title_en: "Sensor Supply 2 Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь питания датчиков 2 — напряжение выше нормы или замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc227.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc227.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Sensor Supply 2 Circuit - Voltage Above Normal or Shorted to High Source
**Цепь питания датчиков 2 — напряжение выше нормы или замыкание на плюс**

> [!abstract] Процедура · `60-fc227`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc227.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc227.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 227

### Цепь питания датчиков 2 — напряжение выше нормы или замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 227 P(P): S211 SPN: 3510 FMI: 3/3 лампы: Янтарная СРТ: | Высокое напряжение, обнаруженное на цепи питания датчика 2. | Возможные снижение производительности двигателя, выключение или потеря защиты двигателя. |

![[19a00855.png]]

Сенсорная схема поставки

### Описание цепи

Схема подачи датчика 2 модуля управления двигателем (ECM) обеспечивает подачу 5 вольт на различные датчики на ремне электропроводки двигателя.

### Расположение компонента

Схема подачи датчика 2 расположена в жгуте проводов двигателя.

### Условия выполнения диагностики

Эта диагностика выполняется постоянно, пока контроллер генераторной установки активен или двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала датчика питания 2 было вне диапазона.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

- Значение по умолчанию используется для всех датчиков на цепи питания 2 датчика.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении электронного инструментария или эквивалента Cummins®. При устранении неисправности кода используйте адрес источника, отображаемый в инструменте электронного обслуживания Cummins® или эквивалент, чтобы определить, какая ECM и схема затронута.

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

- Поврежденные или рыхлые связи.

См. Код 227 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 227
>
> ### Sensor Supply 2 Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 227 PID(P): S211 SPN: 3510 FMI: 3/3 Lamp: Amber SRT: | High voltage detected at sensor supply 2 circuit. | Possible reduced engine performance, shutdown or loss of engine protection. |
>
> Sensor Supply Circuit
>
> ### Circuit Description
>
> The sensor supply 2 circuit of the engine control module (ECM) provides a 5 volt supply to various sensors on the engine wiring harness.
>
> ### Component Location
>
> The sensor supply 2 circuit is located in the engine wiring harness.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the sensor supply 2 signal voltage was out of range high.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> - A default value is used for all of the sensors on the sensor supply 2 circuit.
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
> Refer to Troubleshooting Fault Code 227.
