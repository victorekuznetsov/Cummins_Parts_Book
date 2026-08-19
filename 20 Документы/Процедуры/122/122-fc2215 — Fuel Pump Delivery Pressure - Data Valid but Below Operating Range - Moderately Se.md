---
aliases:
  - "Давление подачи топливного насоса ниже рабочего диапазона — умеренный уровень"
type: "Процедура"
doc: "122-fc2215"
title_en: "Fuel Pump Delivery Pressure - Data Valid but Below Operating Range - Moderately Severe Level"
title_ru: "Давление подачи топливного насоса ниже рабочего диапазона — умеренный уровень"
modified: "2010-12-13"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc2215.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc2215.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Fuel Pump Delivery Pressure - Data Valid but Below Operating Range - Moderately Severe Level
**Давление подачи топливного насоса ниже рабочего диапазона — умеренный уровень**

> [!abstract] Процедура · `122-fc2215`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-12-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc2215.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc2215.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2215

### Давление подачи топливного насоса ниже рабочего диапазона — умеренный уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2215 PID(P): СПН: 94 ФМИ: 18 ламп: Янтарная СРТ: | Давление подачи топливного насоса ниже рабочего диапазона — умеренный уровень. Давление подачи топливного насоса низкое. | Низкая мощность. |

![[19602267.png]]

QSK38 CM2150 Industrial - Схема датчика давления подачи топлива

![[19e00960.png]]

QSK38 CM2150 Power Generation/QSK38 CM2150 Power Generation (Military Application) - Схема датчика давления подачи топлива

![[19602268.png]]

QSK38 CM2150 Marine - Схема датчика давления при доставке топлива

![[19602269.png]]

QSK50 CM2150 Power Generation без усовершенствованного мониторинга двигателя / QSK50 CM2150 Power Generation с расширенным мониторингом двигателя и QSK60 CM2150 Power Generation - схема датчика давления подачи топлива

![[19602270.png]]

QSK50 CM2150 Industrial - Схема датчика давления подачи топлива

![[19602271.png]]

QSK60 CM2150 Промышленный - Схема датчика давления подачи топлива

![[19602272.png]]

QSK50 CM2150 Marine - Схема датчика давления при доставке топлива

![[19602273.png]]

QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - Схема датчика давления подачи топлива

### Описание цепи

Датчик давления подачи топлива используется электронным модулем управления (ECM) для мониторинга давления подачи топлива непосредственно перед фильтром второй ступени. ECM контролирует напряжение на контакте сигнала давления подачи топлива и преобразует его в значение давления.

### Расположение компонента

Датчик давления подачи топлива расположен во второй ступени топливного фильтра, устанавливающего головку.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. У каждого блока управления свой адрес источника, который отображается при подключении INSITE™. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Возможные причины этого кода неисправности:

- 1 стадия ограничения топливного фильтра

- Высокое ограничение впуска топлива

- Низкий расход топлива из геротора

- Застрявший механический клапан в героторной оболочке

- Застрял регулятор низкого давления в топливном насосе высокого давления

- Воздух в топливе.

См. код 2215 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2215
>
> ### Fuel Pump Delivery Pressure - Data Valid but Below Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2215 PID(P): SPN: 94 FMI: 18 Lamp: Amber SRT: | Fuel Pump Delivery Pressure - Data Valid but Below Operating Range - Moderately Severe Level. Fuel pump supply pressure low. | Low power. |
>
> QSK38 CM2150 Industrial - Fuel Delivery Pressure Sensor Circuit
>
> QSK38 CM2150 Power Generation/QSK38 CM2150 Power Generation (Military Application) - Fuel Delivery Pressure Sensor Circuit
>
> QSK38 CM2150 Marine - Fuel Delivery Pressure Sensor Circuit
>
> QSK50 CM2150 Power Generation without Advanced Engine Monitoring/QSK50 CM2150 Power Generation with Advanced Engine Monitoring and QSK60 CM2150 Power Generation - Fuel Delivery Pressure Sensor Circuit
>
> QSK50 CM2150 Industrial - Fuel Delivery Pressure Sensor Circuit
>
> QSK60 CM2150 Industrial - Fuel Delivery Pressure Sensor Circuit
>
> QSK50 CM2150 Marine - Fuel Delivery Pressure Sensor Circuit
>
> QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - Fuel Delivery Pressure Sensor Circuit
>
> ### Circuit Description
>
> The fuel delivery pressure sensor is used by the electronic control module (ECM) to monitor fuel supply pressure directly before the second stage filter. The ECM monitors the voltage on the fuel delivery pressure signal pin and converts it to a pressure value.
>
> ### Component Location
>
> The fuel delivery pressure sensor is located in the second stage fuel filter head.
>
> ### Shoptalk
>
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.
>
> Possible causes of this fault code include:
>
> - Stage 1 fuel filter restriction high
>
> - Fuel inlet restriction high
>
> - Low fuel flow from gerotor
>
> - Stuck mechanical dump valve in gerotor housing
>
> - Stuck low-pressure regulator in high-pressure fuel pump
>
> - Air in fuel.
>
> Refer to Troubleshooting Fault Code 2215.
