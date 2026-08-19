---
aliases:
  - "Цепь датчика воды в топливе — напряжение ниже нормы"
type: "Процедура"
doc: "123-fc4689"
title_en: "Water in Fuel Indicator Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика воды в топливе — напряжение ниже нормы"
modified: "2016-12-12"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc4689.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc4689.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# Water in Fuel Indicator Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика воды в топливе — напряжение ниже нормы**

> [!abstract] Процедура · `123-fc4689`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-12-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc4689.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc4689.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 4689

### Цепь датчика воды в топливе — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 4689 PID(P): СПН: 97 ФМИ: 4 лампы: Обслуживание SRT: | Цепь датчика воды в топливе — напряжение ниже нормы. Низкое напряжение, обнаруженное на воде в цепи датчика индикатора топлива. | Ни одного на выступление. Вода в топливе не доступна. |

![[19r99369.png]]

Вода в топливном индикаторе сенсорной цепи

### Описание цепи

Датчик индикатора воды в топливе устанавливается производителем оригинального оборудования (OEM). Датчик индикатора воды в топливе посылает сигнал модулю управления двигателем (ECM), когда в топливном фильтре накопился заданный объем воды. Вода в цепи датчика индикатора топлива содержит два провода: a вода в топливном индикаторе ВПЕРЕД (датчик датчика 1) проволоки и вода в топливном индикаторе SIGNAL проволоки.

### Расположение компонента

Датчик индикатора воды в топливе устанавливается OEM. См. сервисную документацию изготовителя оборудования.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. У каждого блока управления свой адрес источника, который отображается при подключении INSITE™. При устранении неисправности кода используйте адрес источника, отображаемый в инструменте электронного обслуживания INSITETM, чтобы определить, какая ECM или схема затронута.

Возможные причины этого кода неисправности включают:

- Схема сигнала, закороченная до земли в проводной упряжке, датчике или разъеме.

См. Код устранения неполадок t05-4689.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 4689
>
> ### Water in Fuel Indicator Sensor Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 4689 PID(P): SPN: 97 FMI: 4 Lamp: Maintenance SRT: | Water in Fuel Indicator Sensor Circuit - Voltage Below Normal or Shorted to Low Source. Low voltage detected at the water in fuel indicator sensor circuit. | None on performance. No water in fuel warning available. |
>
> Water in Fuel Indicator Sensor Circuit
>
> ### Circuit Description
>
> The water in fuel indicator sensor is installed by the original equipment manufacturer (OEM). The water in fuel indicator sensor sends a signal to the engine control module (ECM) when a set volume of water has accumulated in the fuel filter. The water in fuel indicator sensor circuit contains two wires: a water in fuel indicator RETURN (sensor return 1) ground wire and a water in fuel indicator SIGNAL wire.
>
> ### Component Location
>
> The water in fuel indicator sensor is mounted by the OEM. See equipment manufacturer service information.
>
> ### Shoptalk
>
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM or circuit is affected.
>
> Possible causes for this fault code include:
>
> - Signal circuit shorted to ground in the harness, sensor, or connector.
>
> Refer to Troubleshooting Fault Code t05-4689.
