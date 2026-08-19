---
aliases:
  - "Давление ОЖ ниже нормы — наивысший уровень"
type: "Процедура"
doc: "60-fc228"
title_en: "Coolant Pressure - Data Valid But Below Normal Operating Range - Most Severe Level"
title_ru: "Давление ОЖ ниже нормы — наивысший уровень"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc228.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc228.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Coolant Pressure - Data Valid But Below Normal Operating Range - Most Severe Level
**Давление ОЖ ниже нормы — наивысший уровень**

> [!abstract] Процедура · `60-fc228`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc228.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc228.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 228

### Давление ОЖ ниже нормы — наивысший уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 228 PID(P): P109 SPN: 109 FMI: 1/1 лампа: Красная СТО: | Сигнал давления охлаждающей жидкости указывает на то, что давление охлаждающей жидкости ниже критического предела защиты двигателя. | Двигатель может отключиться. |

![[19a00861.png]]

Цепь датчика давления охлаждающей жидкости

### Описание цепи

Датчик давления охлаждающей жидкости двигателя представляет собой датчик переменного сопротивления, используемый ECM для мониторинга давления охлаждающей жидкости. Датчик давления охлаждающей жидкости двигателя имеет три схемы: 5-вольтная цепь подачи, возврата и сигнала. Напряжение цепи сигнала указывает на давление охлаждающей жидкости в системе охлаждения двигателя.

### Расположение компонента

Датчик давления охлаждающей жидкости расположен на подсоединении водяного насоса к блоку двигателя.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что давление охлаждающей жидкости двигателя было меньше предела защиты двигателя.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки отображает неисправность выключения сразу же, когда диагностика работает и выходит из строя.

- Двигатель будет отключен, если включена функция защиты двигателя.

- Выходной крутящий момент двигателя будет уменьшен.

### Условия сброса кода неисправности

- Для проверки ремонта, работайте с двигателем под нагрузкой не менее 5 минут.

- Контроллер генераторной установки отключит индикатор выключения сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Низкий уровень охлаждающей жидкости

- Неисправная крышка радиатора.

- Неисправный датчик давления охлаждающей жидкости.

- Неисправный водяной насос.

См. Код 228 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 228
>
> ### Coolant Pressure - Data Valid But Below Normal Operating Range - Most Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 228 PID(P): P109 SPN: 109 FMI: 1/1 Lamp: Red SRT: | Coolant pressure signal indicates coolant pressure is below the engine protection critical limit. | Engine may shutdown. |
>
> Coolant Pressure Sensor Circuit
>
> ### Circuit Description
>
> The engine coolant pressure sensor is a variable resistance sensor used by the ECM to monitor the coolant pressure. The engine coolant pressure sensor has three circuits: 5 volt supply, return and signal circuits. The signal circuit voltage indicates the coolant pressure in the engine cooling system.
>
> ### Component Location
>
> The coolant pressure sensor is located on the water pump connection to the engine block.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the engine coolant pressure was less than the engine protection limit.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.
>
> - The engine will be shut down if the Engine Protection Shutdown feature is enabled.
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
> Possible causes of this fault code include:
>
> - Low coolant level
>
> - A malfunctioning radiator cap.
>
> - A malfunctioning coolant pressure sensor.
>
> - A malfunctioning water pump.
>
> Refer to Troubleshooting Fault Code 228.
