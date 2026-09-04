---
aliases:
  - "Давление в топливной рампе 1 ниже нормы — умеренный уровень"
type: "Процедура"
doc: "122-fc559"
title_en: "Injector Metering Rail 1 Pressure - Data Valid but Below Normal Operating Range - Moderately Severe Level"
title_ru: "Давление в топливной рампе 1 ниже нормы — умеренный уровень"
modified: "2010-09-17"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "4022102"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc559.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc559.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Injector Metering Rail 1 Pressure - Data Valid but Below Normal Operating Range - Moderately Severe Level
**Давление в топливной рампе 1 ниже нормы — умеренный уровень**

> [!abstract] Процедура · `122-fc559`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc559.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc559.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 559

### Давление в топливной рампе 1 ниже нормы — умеренный уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 559 PID(P): СПН: 157 ФМИ: 1/18 лампы: Янтарная СРТ: | Форсунка Metering Rail 1 Pressure - Data Valid - но ниже нормального диапазона работы - умеренно тяжелый уровень. ECM обнаружил, что давление топлива ниже, чем указывалось. | Низкая мощность, возможное отключение или отсутствие запуска. |

![[19602101.png]]

QSK38 CM2150 Industrial - форсунка Metering Rail 1 Pressure Circuit

![[19602102.png]]

QSK38 CM2150 Marine - форсунка Metering Rail 1 Pressure Circuit

![[19e00958.png]]

QSK38 CM2150 Power Generation/QSK38 CM2150 Power Generation (Military Application) - форсунка Metering Rail 1 Pressure Circuit

![[19602103.png]]

QSK50 CM2150 Промышленный - форсунка Метерная рельсовая 1 Тормозная магистраль

![[19602105.png]]

QSK50 CM2150 Marine - форсунка Metering Rail 1 Pressure Circuit

![[19602106.png]]

QSK60 CM2150 Industrial - форсунка Metering Rail 1 Pressure Circuit

![[19e00959.png]]

QSK50 CM2150 Power Generation без усовершенствованного мониторинга двигателя / QSK50 CM2150 Power Generation с усовершенствованным мониторингом двигателя / QSK60 CM2150 Power Generation - форсунка Metering Rail 1 Pressure Circuit

![[19602107.png]]

QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - форсунка Metering Rail 1 Pressure Circuit

### Описание цепи

Контур управления давлением зависит от давления топлива, подаваемого на насос высокого давления героторным насосом. ECM контролирует давление в топливной форсунке 1 и условия работы двигателя, а также изменяет команду потока для поддержания надлежащего давления в топливной форсунке 1. Изменения в команде потока приводят к открытию или закрытию герметизирующего узла 1 топливного насоса.

### Расположение компонента

Топливный насос высокого давления крепится к корпусу передней передачи на левом берегу двигателя.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. У каждого блока управления свой адрес источника, который отображается при подключении INSITE™. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Возможные причины этого кода неисправности:

- Сопротивление на входе топлива

- Засорение топливного фильтра

- Низкий выход героторного насоса

- Регулятор давления героторного насоса, прилипающий или протекающий

- Распад мощности насоса высокого давления

- Утечка механических клапанов для сброса

- Механический клапан откидывания открывается при низком давлении

- Утечка внутренней стенки форсунки высокого давления

- Неисправный топливный насос, дающий давление в сборе.

См. Код 559 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 559
>
> ### Injector Metering Rail 1 Pressure - Data Valid but Below Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 559 PID(P): SPN: 157 FMI: 1/18 Lamp: Amber SRT: | Injector Metering Rail 1 Pressure - Data Valid - but Below Normal Operating Range - Moderately Severe Level. The ECM has detected that the fuel pressure is lower than commanded. | Low Power, possible shutdown, or no start. |
>
> QSK38 CM2150 Industrial - Injector Metering Rail 1 Pressure Circuit
>
> QSK38 CM2150 Marine - Injector Metering Rail 1 Pressure Circuit
>
> QSK38 CM2150 Power Generation/QSK38 CM2150 Power Generation (Military Application) - Injector Metering Rail 1 Pressure Circuit
>
> QSK50 CM2150 Industrial - Injector Metering Rail 1 Pressure Circuit
>
> QSK50 CM2150 Marine - Injector Metering Rail 1 Pressure Circuit
>
> QSK60 CM2150 Industrial - Injector Metering Rail 1 Pressure Circuit
>
> QSK50 CM2150 Power Generation without Advanced Engine Monitoring/QSK50 CM2150 Power Generation with Advanced Engine Monitoring/QSK60 CM2150 Power Generation - Injector Metering Rail 1 Pressure Circuit
>
> QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - Injector Metering Rail 1 Pressure Circuit
>
> ### Circuit Description
>
> The pressure control loop relies on fuel pressure supplied to the high-pressure pump by the gerotor pump. The ECM monitors the injector metering rail 1 pressure and engine operating conditions, and changes the flow command to maintain the proper injector metering rail 1 pressure. Changes to the flow command result in opening or closing of the fuel pump pressurizing assembly 1.
>
> ### Component Location
>
> The high-pressure fuel pump is mounted to the front gear housing on the left bank of the engine.
>
> ### Shoptalk
>
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.
>
> Possible causes of this fault code include:
>
> - Fuel inlet restriction
>
> - Fuel filter plugging
>
> - Gerotor pump output low
>
> - Gerotor pump pressure regulator sticking or leaking
>
> - High-pressure pump capacity decay
>
> - Mechanical dump valve leaks to drain
>
> - Mechanical dump valve opens at low pressure
>
> - High-pressure injector supply line inner wall leak
>
> - Malfunctioning fuel pump pressurizing assembly.
>
> Refer to Troubleshooting Fault Code 559.
