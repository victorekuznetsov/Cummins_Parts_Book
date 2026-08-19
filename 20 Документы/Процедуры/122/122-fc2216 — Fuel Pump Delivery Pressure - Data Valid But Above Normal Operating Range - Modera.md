---
aliases:
  - "Давление подачи топливного насоса выше нормы — умеренный уровень"
type: "Процедура"
doc: "122-fc2216"
title_en: "Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Moderately Severe Level"
title_ru: "Давление подачи топливного насоса выше нормы — умеренный уровень"
modified: "2017-05-30"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc2216.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc2216.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Moderately Severe Level
**Давление подачи топливного насоса выше нормы — умеренный уровень**

> [!abstract] Процедура · `122-fc2216`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-05-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc2216.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc2216.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2216

### Давление подачи топливного насоса выше нормы — умеренный уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2216 PID(P): СПН: 94 ФМИ: 16 ламп: Янтарная СРТ: | Давление подачи топливного насоса выше нормы — умеренный уровень. Давление подачи топливного насоса очень высокое. | Низкая мощность или дым двигателя. |

![[19602267.png]]

QSK38 CM2150 Industrial - Схема датчика давления подачи топлива

![[19e00960.png]]

QSK38 CM2150 Power Generation/QSK38 Power Generation (Военное применение) - Схема датчика давления подачи топлива

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

Датчик давления подачи топлива используется модулем управления двигателем (ECM) для контроля давления подачи топлива непосредственно перед фильтром 2-й ступени. ECM контролирует напряжение на контакте сигнала давления подачи топлива и преобразует его в значение давления.

### Расположение компонента

Датчик давления подачи топлива расположен в головке установки топливного фильтра 2-й ступени.

### Условия выполнения диагностики

- Скорость двигателя ** должна быть выше 500 оборотов в минуту в течение 10 секунд, а заправка должна быть выше 20 мг / стк в течение 5 секунд, прежде чем начнет приниматься диагностическое решение.

- Температура топлива ** должна быть больше или равна -10 0С

### Условия установки кодов неисправностей

При давлении подачи топлива более 1100 кПа (160 psi) более 3 секунд.

### Действия системы при активном коде неисправности

- ECM освещает лампу янтарного CHECK ENGINE сразу же, когда диагностика обнаруживает высокое давление подачи топлива.

### Условия сброса кода неисправности

FC2216 - код сцепления сбоев. Диагностика позволяет устранить ошибки только в том случае, если давление подачи топлива ниже 850 кПа. После того, как код ошибки будет использован, единственным способом его очистки будет выполнение следующих действий:

- Выключите двигатель и следуйте шагам по устранению неполадок для разрешения.

- Перезагрузите двигатель и запустите двигатель с номинальным значением в течение нескольких минут.

- ECM выключит лампу янтарного CHECK ENGINE сразу после диагностических прогонов и проходов.

- Состояние кода ошибки, отображаемого инструментами электронного сервиса INSITETM, будет изменено на INACTIVE сразу после запуска и прохождения диагностики.

- Команда Reset All Faults в инструменте электронного сервиса INSITETM может использоваться для устранения активных и неактивных ошибок.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. У каждого блока управления свой адрес источника, который отображается при подключении INSITE™. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Возможные причины этого кода неисправности:

- 2 стадия ограничения топливного фильтра

- Укупорка или повреждение линии подачи топлива

- Застрявший героторный насос регулятор давления топлива, расположенный в насосе высокого давления.

См. Код устранения неполадок t05-2216.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2216
>
> ### Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2216 PID(P): SPN: 94 FMI: 16 Lamp: Amber SRT: | Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Moderately Severe Level. Fuel pump supply pressure very high. | Low power or engine smoke. |
>
> QSK38 CM2150 Industrial - Fuel Delivery Pressure Sensor Circuit
>
> QSK38 CM2150 Power Generation/QSK38 Power Generation (Military Application) - Fuel Delivery Pressure Sensor Circuit
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
> The fuel delivery pressure sensor is used by the engine control module (ECM) to monitor fuel delivery pressure directly before the Stage 2 filter. The ECM monitors the voltage on the fuel delivery pressure SIGNAL pin and converts it to a pressure value.
>
> ### Component Location
>
> The fuel delivery pressure sensor is located in the Stage 2 fuel filter head.
>
> ### Conditions For Running The Diagnostics
>
> - The engine speed **must** be above 500 RPM for 10 seconds, and fueling must be above 20 mg/stk for 5 seconds before a diagnostic decision begins to be made.
>
> - The fuel temperature **must** be greater than, or equal to -10 ⁰C
>
> ### Conditions For Setting The Fault Codes
>
> When the fuel supply pressure is greater than 1100 kPa (160 psi) for more than 3 seconds.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostics detects high fuel supply pressure.
>
> ### Conditions For Clearing The Fault Code
>
> FC2216 is a latching fault code. The diagnostic only clears errors if the fuel supply pressure is below 850 kPa. Once the fault code is invoked, the only way to clear it would be to perform the following steps:
>
> - Turn off engine and follow the troubleshooting steps for resolution.
>
> - Restart engine, and run the engine at rated for a few minutes.
>
> - The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.
>
> - The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately after the diagnostic runs and passes.
>
> - The Reset All Faults command in INSITE™ electronic service tool can be used to clear active and inactive faults.
>
> ### Shoptalk
>
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.
>
> Possible causes of this fault code include:
>
> - Stage 2 fuel filter restriction high
>
> - Pinched or damaged fuel supply line
>
> - Stuck gerotor pump fuel pressure regulator located in high-pressure pump.
>
> Refer to Troubleshooting Fault Code t05-2216.
