---
aliases:
  - "Цепь датчика давления ОЖ — напряжение ниже нормы"
type: "Процедура"
doc: "60-fc232"
title_en: "Coolant Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика давления ОЖ — напряжение ниже нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc232.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc232.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Coolant Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика давления ОЖ — напряжение ниже нормы**

> [!abstract] Процедура · `60-fc232`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc232.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc232.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 232

### Цепь датчика давления ОЖ — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 232 PID(P): P109 SPN: 109 FMI: 4/4 лампы: Янтарная СРТ: | Низкое напряжение сигнала, обнаруженное в цепи датчика давления охлаждающей жидкости. | Ни одного на выступление. |

![[19a00861.png]]

Цепь датчика давления охлаждающей жидкости

### Описание цепи

Датчик давления охлаждающей жидкости двигателя представляет собой датчик переменного сопротивления, используемый ECM для мониторинга давления охлаждающей жидкости. Датчик давления охлаждающей жидкости двигателя имеет три схемы: 5-вольтная цепь подачи, возврата и сигнала. Напряжение цепи сигнала указывает на давление охлаждающей жидкости в системе охлаждения двигателя.

### Расположение компонента

Датчик давления охлаждающей жидкости расположен на подсоединении водяного насоса к блоку двигателя.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда контроллер генераторного набора активен.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала давления охлаждающей жидкости было вне диапазона низкого.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный датчик давления охлаждающей жидкости.

- Неисправный или повреждённый жгут проводов двигателя.

См. Код 232 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 232
>
> ### Coolant Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 232 PID(P): P109 SPN: 109 FMI: 4/4 Lamp: Amber SRT: | Low signal voltage detected at the coolant pressure sensor circuit. | None on performance. |
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
> This diagnostic runs continuously when the generator set controller is active.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the coolant pressure signal voltage was out of range low.
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
> - A malfunctioning coolant pressure sensor.
>
> - Malfunctioning or damaged engine wiring harness.
>
> Refer to Troubleshooting Fault Code 232.
