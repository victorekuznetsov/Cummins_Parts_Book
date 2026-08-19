---
aliases:
  - "Ошибка состояния входа идентификации ЭБУ — данные нестабильны или неверны"
type: "Процедура"
doc: "60-fc184"
title_en: "Engine Control Module Identification Input State Error - Data erratic, intermittent or incorrect"
title_ru: "Ошибка состояния входа идентификации ЭБУ — данные нестабильны или неверны"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc184.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc184.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Control Module Identification Input State Error - Data erratic, intermittent or incorrect
**Ошибка состояния входа идентификации ЭБУ — данные нестабильны или неверны**

> [!abstract] Процедура · `60-fc184`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc184.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc184.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 184

### Ошибка состояния входа идентификации ЭБУ — данные нестабильны или неверны

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 184 PID(P): S233 SPN: 609 FMI: 2/2 лампы: Янтарная СРТ: | Состояние ввода идентификации модуля управления является неправильным. | Двигатель отключится. Двигатель может ** не** завестись. |

![[19a00854.png]]

Модуль управления двигателем (ECM)

### Описание цепи

Модуль управления двигателем (ECM) использует схему идентификации модуля управления для проверки его местоположения в электропроводке. Комбинация штифтов сигнала идентификации модуля управления, которые соединены с возвратом, позволяет ECM сделать это определение.

### Расположение компонента

Модули управления двигателем (ECM) расположены на пластине, которая находится над корпусом маховика.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда контроллер генераторного набора активен.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что калибровка ** не** соответствует идентификационному входу модуля управления.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки отображает неисправность выключения сразу же, когда диагностика работает и выходит из строя.

- Двигатель будет отключен, если включена функция защиты двигателя.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки отключит индикатор выключения сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении электронного инструментария или эквивалента Cummins®. При устранении неисправности кода используйте адрес источника, отображаемый в инструменте электронного обслуживания Cummins® или эквивалент, чтобы определить, какая ECM и схема затронута.

Возможные причины этого кода неисправности:

- Дублирующие или неправильные калибровки ECM, загруженные в ECM (ы).

- Две или более ECM, установленных в неправильном месте.

- Неправильные параметры.

- Неисправный или повреждённый жгут проводов двигателя.

- Поврежденные или рыхлые разъемы.

См. Код 184 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 184
>
> ### Engine Control Module Identification Input State Error - Data erratic, intermittent or incorrect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 184 PID(P): S233 SPN: 609 FMI: 2/2 Lamp: Amber SRT: | The control module identification input state is incorrect. | Engine will shut down. Engine may **not** start. |
>
> Engine Control Module (ECM)
>
> ### Circuit Description
>
> The engine control module (ECM) uses the control module identification circuit to verify its location in the harness. The combination of control module identification signal pins that are connected to return allow the ECM to make this determination.
>
> ### Component Location
>
> The Engine Control Modules (ECM) are located on a plate that is above the flywheel housing.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the calibration does **not** match the control module identification input.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.
>
> - The engine will be shut down if the Engine Protection Shutdown feature is enabled.
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
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.
>
> Possible causes of this fault code include:
>
> - Duplicate or incorrect ECM calibrations downloaded to the ECM(s).
>
> - Two or more ECMs installed in the wrong location.
>
> - Incorrect parameter settings.
>
> - Malfunctioning or damaged engine wiring harness.
>
> - Damaged or loose connectors.
>
> Refer to Troubleshooting Fault Code 184.
