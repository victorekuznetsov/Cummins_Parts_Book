---
aliases:
  - "Температура ОЖ выше нормы — наивысший уровень"
type: "Процедура"
doc: "60-fc151"
title_en: "Engine Coolant Temperature - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Температура ОЖ выше нормы — наивысший уровень"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc151.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc151.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Coolant Temperature - Data Valid But Above Normal Operating Range - Most Severe Level
**Температура ОЖ выше нормы — наивысший уровень**

> [!abstract] Процедура · `60-fc151`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc151.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc151.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 151

### Температура ОЖ выше нормы — наивысший уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 151 PID(P): P110 SPN: 110 FMI: 0/0 лампа: Красная СТО: | Сигнал температуры охлаждающей жидкости двигателя указывает температуру охлаждающей жидкости двигателя выше критического предела защиты двигателя. | Двигатель отключится. |

![[19a00848.png]]

Схема датчика температуры двигателя

### Описание цепи

Датчик температуры охлаждающей жидкости двигателя представляет собой датчик переменного резистора, используемый ECM для мониторинга температуры охлаждающей жидкости двигателя. Датчик температуры охлаждающей жидкости двигателя имеет две схемы: сигнал и обратные цепи. Напряжение сигнала указывает на температуру охлаждающей жидкости.

### Расположение компонента

Датчик температуры охлаждающей жидкости двигателя расположен на корпусе термостата.

### Условия выполнения диагностики

Эта диагностика выполняется постоянно, пока контроллер генераторной установки активен или двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что температура охлаждающей жидкости двигателя была выше предела защиты двигателя.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки отображает неисправность выключения сразу же, когда диагностика работает и выходит из строя.

- Выходной крутящий момент двигателя будет уменьшен.

- Двигатель будет отключен, если включена функция защиты двигателя.

### Условия сброса кода неисправности

- Для проверки ремонта доведите двигатель до рабочей температуры и запускайте его в нормальных условиях нагрузки в течение 15 минут.

- Контроллер генераторной установки отключит индикатор выключения сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Затрудняется протекание воздуха через радиатор.

- Уровень охлаждающей жидкости в двигателе низкий

- Сжатые или ограниченные шланги системы охлаждения.

- Неисправный термостат охлаждающей жидкости двигателя.

- Неисправный водяной насос.

- Неисправный датчик температуры охлаждающей жидкости двигателя

См. Код 151 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 151
>
> ### Engine Coolant Temperature - Data Valid But Above Normal Operating Range - Most Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 151 PID(P): P110 SPN: 110 FMI: 0/0 Lamp: Red SRT: | Engine coolant temperature signal indicates engine coolant temperature above engine protection critical limit. | Engine will shut down. |
>
> Engine Coolant Temperature Sensor Circuit
>
> ### Circuit Description
>
> The engine coolant temperature sensor is a variable resistor sensor used by the ECM to monitor the engine coolant temperature. The engine coolant temperature sensor has two circuits: signal, and return circuits. The signal voltage indicates the coolant temperature.
>
> ### Component Location
>
> The engine coolant temperature sensor is located on the thermostat housing.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the engine coolant temperature was greater than the engine protection limit.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.
>
> - The torque output of the engine will be reduced.
>
> - The engine will be shut down if the Engine Protection Shutdown feature is enabled.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, bring the engine up to operating temperature and run it in normal loaded conditions for 15 minutes.
>
> - The generator set controller will turn off the shutdown indicator immediately after the user presses the reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Obstructed airflow through the radiator.
>
> - Engine coolant level low
>
> - Collapsed or restricted cooling system hoses.
>
> - Malfunctioning engine coolant thermostat.
>
> - A malfunctioning water pump.
>
> - Malfunctioning engine coolant temperature sensor
>
> Refer to Troubleshooting Fault Code 151.
