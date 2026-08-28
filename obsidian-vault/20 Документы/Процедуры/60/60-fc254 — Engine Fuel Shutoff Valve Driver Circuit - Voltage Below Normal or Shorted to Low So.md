---
aliases:
  - "Цепь драйвера клапана отсечки топлива — напряжение ниже нормы"
type: "Процедура"
doc: "60-fc254"
title_en: "Engine Fuel Shutoff Valve Driver Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь драйвера клапана отсечки топлива — напряжение ниже нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc254.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc254.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Fuel Shutoff Valve Driver Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь драйвера клапана отсечки топлива — напряжение ниже нормы**

> [!abstract] Процедура · `60-fc254`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc254.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc254.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 254

### Цепь драйвера клапана отсечки топлива — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 254 PID(P): S17 SPN: 632 FMI: 4/4 лампы: Красная СТО: | Низкое напряжение, обнаруженное на цепи управления отключения топлива. | Двигатель отключится. |

![[19a00865.png]]

Клапан отсечки топлива

### Описание цепи

Клапан отключения топлива представляет собой устройство, используемое ECM для управления подачей топлива в насос для впрыска.

### Расположение компонента

Клапаны отключения топлива расположены на рельсе масляного поддона около середины блока на обоих берегах.

### Условия выполнения диагностики

Эта диагностика выполняется, когда включён клапан отключения топлива.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что контроль за отключением топлива находится вне диапазона.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки отображает неисправность выключения сразу же, когда диагностика работает и выходит из строя.

- Двигатель будет отключен.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки отключит индикатор выключения сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении рекомендуемого инструментария или эквивалента электронного сервиса Cummins®. При устранении неисправности кода используйте адрес источника, отображаемый в рекомендуемой электронной сервисной инструментарии Cummins®, или эквивалент, чтобы определить, какая ECM и схема затронута.

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

- Неисправный клапан отключения топлива.

- Поврежденные или рыхлые связи.

См. Код 254 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 254
>
> ### Engine Fuel Shutoff Valve Driver Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 254 PID(P): S17 SPN: 632 FMI: 4/4 Lamp: Red SRT: | Low voltage detected on the fuel shutoff control circuit. | Engine will shut down. |
>
> Fuel Shutoff Valve
>
> ### Circuit Description
>
> The fuel shutoff valve is a device used by the ECM to control the fuel supply into the injection pump.
>
> ### Component Location
>
> The fuel shutoff valves are located on the oil pan rail near the middle of the block on both banks.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs when the fuel shutoff valve is commanded ON.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) has detected the fuel shutoff control is out of range low.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.
>
> - The engine will be shut down.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, start the engine and let it run for 1 minute at no load.
>
> - The generator set controller will turn off the shutdown indicator immediately after the user presses the reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> Each ECM has an individual source address that displays when the recommended Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in the recommended Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged engine wiring harness.
>
> - A malfunctioning fuel shutoff valve.
>
> - Damaged or loose connections.
>
> Refer to Troubleshooting Fault Code 254.
