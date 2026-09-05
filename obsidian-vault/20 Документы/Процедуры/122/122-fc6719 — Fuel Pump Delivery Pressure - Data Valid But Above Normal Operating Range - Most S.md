---
aliases:
  - "Давление подачи топливного насоса — данные достоверны, но выше нормы — наивысший уровень"
type: "Процедура"
doc: "122-fc6719"
title_en: "Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Давление подачи топливного насоса — данные достоверны, но выше нормы — наивысший уровень"
modified: "2017-05-30"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "4022102"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc6719.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc6719.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level
**Давление подачи топливного насоса — данные достоверны, но выше нормы — наивысший уровень**

> [!abstract] Процедура · `122-fc6719`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-05-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc6719.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc6719.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 6719

### Давление подачи топливного насоса — данные достоверны, но выше нормы — наивысший уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 6719 PID(P): СПН: 94 ФМИ: 0/0 лампа: Красная СТО: | Давление подачи топливного насоса — данные достоверны, но выше нормы — наивысший уровень. Давление подачи топливного насоса очень высокое. | Возможная скорость двигателя снижается. Низкая мощность или дым двигателя. |

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

- Скорость двигателя **должна быть выше 500 оборотов в минуту в течение 10 секунд, а заправка **должна быть выше 20 мг / стк в течение 5 секунд, прежде чем начнет приниматься диагностическое решение.

- Температура топлива должна быть больше или равна -10 0С.

### Условия установки кодов неисправностей

- Когда давление подачи топлива превышает 1200 кПа (174 psi) более чем на 3 секунды, FC4615 устанавливается изначально.

- FC4615 также активирует снижение скорости двигателя, которое пытается снизить давление подачи топлива на уровне или ниже 1000 кПа.

- Если через 30 минут скорость размывания не сможет снизить давление подачи топлива до 1000 кПа, то активируется FC 6719 (Красный).

### Действия системы при активном коде неисправности

- ECM освещает красную лампу CHECK ENGINE сразу же, когда диагностика обнаруживает высокое давление подачи топлива.

### Условия сброса кода неисправности

- FC 6719 (Красная лампа) очищается на каждом ключевом цикле. Тем не менее, настоятельно рекомендуется немедленно прекратить работу двигателя и следовать шагам по устранению неполадок для разрешения.

- После перезапуска двигателя статус кода неисправности, отображаемый инструментами электронного обслуживания INSITETM, немедленно изменится на INACTIVE.

- Команда Reset All Faults в инструменте электронного сервиса INSITETM может использоваться для устранения активных и неактивных ошибок.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. У каждого блока управления свой адрес источника, который отображается при подключении INSITE™. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Возможные причины этого кода неисправности:

- 2 стадия ограничения топливного фильтра

- Укупорка или повреждение линии подачи топлива

- Застрявший героторный насос регулятор давления топлива, расположенный в насосе высокого давления.

См. Код устранения неполадок t05-6719.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 6719
>
> ### Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 6719 PID(P): SPN: 94 FMI: 0/0 Lamp: Red SRT: | Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level. Fuel pump supply pressure very high. | Possible engine speed derate. Low power or engine smoke. |
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
> - The engine speed **must** be above 500 RPM for 10 seconds, and fueling **must** be above 20 mg/stk for 5 seconds before a diagnostic decision begins to be made.
>
> - The fuel temperature **must** be greater than, or equal to -10 ⁰C.
>
> ### Conditions For Setting The Fault Codes
>
> - When the fuel supply pressure is greater than 1200 kPa (174 psi) for more than 3 seconds, FC4615 is initially set.
>
> - FC4615 also activates an engine speed derate that attempts to bring down the fuel supply pressure at or below 1000 kPa.
>
> - If after 30 minutes, the speed derate is unable to bring down the fuel supply pressure to 1000 kPa, then FC 6719 (Red) is activated.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the red CHECK ENGINE lamp immediately when the diagnostics detects high fuel supply pressure.
>
> ### Conditions For Clearing The Fault Code
>
> - FC 6719 (Red Lamp) is cleared at every key-cycle. However, it is strongly recommended to stop engine operation and follow the troubleshooting steps for resolution immediately.
>
> - Once the engine has been restarted, the fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately.
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
> Refer to Troubleshooting Fault Code t05-6719.
