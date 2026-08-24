---
aliases:
  - "Хотя бы один модуль имеет неисправность низшего уровня — условие возникло"
type: "Процедура"
doc: "60-fc1519"
title_en: "At Least One Module Has A Least Severe Fault - Condition Exists"
title_ru: "Хотя бы один модуль имеет неисправность низшего уровня — условие возникло"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1519.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1519.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# At Least One Module Has A Least Severe Fault - Condition Exists
**Хотя бы один модуль имеет неисправность низшего уровня — условие возникло**

> [!abstract] Процедура · `60-fc1519`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1519.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1519.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1519

### Хотя бы один модуль имеет неисправность низшего уровня — условие возникло

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1519 P(P): S254 SPN: 1484 FMI: 11/31 лампа: Обслуживание SRT: | По меньшей мере, один модуль обнаружил код сбоя. | Возможно снижение производительности двигателя. |

![[19a00867.png]]

Модуль управления двигателем (ECM)

### Описание цепи

Модуль управления двигателем (ECM) - это компьютер, который отвечает за управление двигателем, диагностику и функции пользователя. Наименее серьезный код неисправности был обнаружен в ECM в сети шины данных J1939 CAN.

### Расположение компонента

Модули управления двигателем (ECM) расположены на пластине, которая находится над корпусом маховика.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда контроллер генераторного набора активен.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил один или несколько наименее серьезных дефектов.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

### Условия сброса кода неисправности

- Этот код неисправности будет неактивным, как только все коды неисправности янтарной лампы во вторичных ECM будут неактивными.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении рекомендуемого инструментария или эквивалента электронного сервиса Cummins®. При устранении неисправности кода используйте адрес источника, отображаемый в рекомендуемой электронной сервисной инструментарии Cummins®, или эквивалент, чтобы определить, какая ECM и схема затронута.

Возможные причины этого кода неисправности:

- Наименее серьезный код неисправности, обнаруженный на другом ЭХМ.

См. Код 1519 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1519
>
> ### At Least One Module Has A Least Severe Fault - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1519 PID(P): S254 SPN: 1484 FMI: 11/31 Lamp: Maintenance SRT: | A least severe fault code has been detected by at least one module | Possible reduced engine performance. |
>
> Engine Control Module (ECM)
>
> ### Circuit Description
>
> The engine control module (ECM) is a computer that is responsible for engine control, diagnostics, and user features. A least severe fault code has been detected from a ECM on the J1939 datalink network.
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
> The Engine Control Module (ECM) has detected one or more least severe faults.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> ### Conditions For Clearing The Fault Code
>
> - This fault code will go inactive once all amber lamp fault codes in secondary ECMs are inactive.
>
> - The generator set controller will turn off the warning indicator immediately after the user presses reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> Each ECM has an individual source address that displays when the recommended Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in the recommended Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.
>
> Possible causes of this fault code include:
>
> - A least severe fault code detected on another ECM.
>
> Refer to Troubleshooting Fault Code 1519.
