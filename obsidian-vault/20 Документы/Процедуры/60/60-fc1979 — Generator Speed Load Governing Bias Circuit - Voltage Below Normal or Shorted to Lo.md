---
aliases:
  - "Цепь коррекции регулирования частоты/нагрузки — напряжение ниже нормы"
type: "Процедура"
doc: "60-fc1979"
title_en: "Generator Speed/Load Governing Bias Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь коррекции регулирования частоты/нагрузки — напряжение ниже нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1979.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1979.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Generator Speed/Load Governing Bias Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь коррекции регулирования частоты/нагрузки — напряжение ниже нормы**

> [!abstract] Процедура · `60-fc1979`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1979.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1979.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1979

### Цепь коррекции регулирования частоты/нагрузки — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1979 PID(P): СПН: 3938 FMI: 4/4 лампы: Янтарная СРТ: | Генератор скорости/загрузки управляющий Bias Circuit обнаружил напряжение ниже нормального или сокращенного до низкого источника. | Двигатель будет **не** синхронизироваться с сеткой, если он подключен. |

![[19a00879.png]]

Генератор скорости / нагрузки управляющий поворотом.

### Описание цепи

Скорость генератора / нагрузка, управляющая схемой смещения, управляет скоростью двигателя, чтобы соответствовать требуемой частоте и фазе сетки.

### Расположение компонента

Скорость генератора/нагрузка, управляющая контролем смещения, расположена в контроллере генераторной установки на генераторной установке.

### Условия выполнения диагностики

Эта диагностика выполняется постоянно, пока контроллер генераторной установки активен или двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаруженный сигнал с отклонением скорости/нагрузки генератора выходит за пределы диапазона.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

См. Troubleshooting Fault Code 1979.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1979
>
> ### Generator Speed/Load Governing Bias Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1979 PID(P): SPN: 3938 FMI: 4/4 Lamp: Amber SRT: | Generator Speed/Load Governing Bias Circuit has detected voltage below normal or shorted to low source. | Engine will **not** synchronize with the grid, if connected. |
>
> Generator Speed/Load Governing Bias Circuit.
>
> ### Circuit Description
>
> The generator speed/load governing bias circuit controls the engine speed in order to match a required grid frequency and phase.
>
> ### Component Location
>
> The generator speed/load governing bias control is located in the generator set controller on the generator set.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected generator speed/load governing bias signal is out of range low.
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
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged engine wiring harness.
>
> Refer to Troubleshooting Fault Code 1979.
