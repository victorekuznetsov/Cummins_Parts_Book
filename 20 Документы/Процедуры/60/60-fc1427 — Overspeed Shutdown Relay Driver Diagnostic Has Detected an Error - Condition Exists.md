---
aliases:
  - "Диагностика драйвера реле останова по разносу выявила ошибку — условие возникло"
type: "Процедура"
doc: "60-fc1427"
title_en: "Overspeed Shutdown Relay Driver Diagnostic Has Detected an Error - Condition Exists"
title_ru: "Диагностика драйвера реле останова по разносу выявила ошибку — условие возникло"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1427.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc1427.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Overspeed Shutdown Relay Driver Diagnostic Has Detected an Error - Condition Exists
**Диагностика драйвера реле останова по разносу выявила ошибку — условие возникло**

> [!abstract] Процедура · `60-fc1427`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1427.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc1427.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1427

### Диагностика драйвера реле останова по разносу выявила ошибку — условие возникло

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1427 P(P): СПН: 4185 FMI: 11/31 лампа: Янтарная СРТ: | Ошибка обнаружена в цепи водителя сверхскоростной лампы. | Светильник выключения скорости **не** включается. |

![[19a00878.png]]

Выключатель сверхскоростной лампы Circuit

### Описание цепи

Светильник выключения сверхскоростной сигнализации будет указывать, когда двигатель достиг сверхскоростной скорости.

### Расположение компонента

Светильник выключения сверхскоростной системы расположен на панели управления генераторной установкой.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил ошибку в цепи лампы накаливания двигателя.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Поврежденная или неисправная лампа выключения сверхскоростной

- Низкое напряжение на лампе выключения сверхскоростной

- Неисправный или повреждённый жгут проводов двигателя.

- Неисправность или повреждение OEM-проводов.

См. Код 1427 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1427
>
> ### Overspeed Shutdown Relay Driver Diagnostic Has Detected an Error - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1427 PID(P): SPN: 4185 FMI: 11/31 Lamp: Amber SRT: | Error detected in the overspeed lamp driver circuit. | The overspeed shutdown lamp will **not** turn on. |
>
> Overspeed shutdown lamp Circuit
>
> ### Circuit Description
>
> The overspeed shutdown lamp will indicate when the engine has reached overspeed.
>
> ### Component Location
>
> The overspeed shutdown lamp is located on the generator set control panel.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected an error in the engine overspeed lamp circuit.
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
> - Damaged or malfunctioning overspeed shutdown lamp
>
> - Low voltage to the overspeed shutdown lamp
>
> - Malfunctioning or damaged engine wiring harness.
>
> - Malfunctioning or damaged OEM wiring harness.
>
> Refer to Troubleshooting Fault Code 1427.
