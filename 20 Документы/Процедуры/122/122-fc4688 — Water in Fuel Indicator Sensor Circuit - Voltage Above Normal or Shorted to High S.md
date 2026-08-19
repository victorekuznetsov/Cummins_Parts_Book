---
aliases:
  - "Цепь датчика воды в топливе — напряжение выше нормы"
type: "Процедура"
doc: "122-fc4688"
title_en: "Water in Fuel Indicator Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика воды в топливе — напряжение выше нормы"
modified: "2017-01-02"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc4688.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc4688.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Water in Fuel Indicator Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика воды в топливе — напряжение выше нормы**

> [!abstract] Процедура · `122-fc4688`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-01-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc4688.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc4688.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 4688

### Цепь датчика воды в топливе — напряжение выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 4688 PID(P): СПН: 97 ФМИ: 3 лампы: Обслуживание SRT: | Цепь датчика воды в топливе — напряжение выше нормы. Высокое напряжение, обнаруженное на воде в цепи индикатора топлива. | Ни одного на выступление. Вода в топливе не доступна. |

![[19k00130.png]]

Вода в топливном индикаторе сенсорной цепи

### Описание цепи

Датчик индикатора воды в топливе установлен производителем оригинального двигателя (OEM). Датчик индикатора воды в топливе посылает сигнал модулю управления двигателем (ECM), когда в топливном фильтре накопился заданный объем воды. Вода в цепи датчика индикатора топлива содержит два провода: a вода в топливном индикаторе ВПЕРЕД (датчик датчика 1) проволоки и вода в топливном индикаторе SIGNAL проволоки.

### Расположение компонента

Датчик индикатора воды в топливе устанавливается производителем оригинального оборудования (OEM). См. сервисное руководство изготовителя машины.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении электронного инструментария INSITETM. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Возможные причины этого кода неисправности:

- Открытая схема возврата или сигнала в электропроводке, разъемах или датчике

- Провод SIGNAL закорочен до подачи датчика или напряжения батареи.

См. Код устранения неполадок t05-4688.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 4688
>
> ### Water in Fuel Indicator Sensor Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 4688 PID(P): SPN: 97 FMI: 3 Lamp: Maintenance SRT: | Water in Fuel Indicator Sensor Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the water in fuel indicator circuit. | None on performance. No water in fuel warning available. |
>
> Water in Fuel Indicator Sensor Circuit
>
> ### Circuit Description
>
> The water in fuel indicator sensor is fitted by the original engine manufacturer (OEM). The water in fuel indicator sensor sends a signal to the engine control module (ECM) when a set volume of water has accumulated in the fuel filter. The water in fuel indicator sensor circuit contains two wires: a water in fuel indicator RETURN (sensor return 1) ground wire and a water in fuel indicator SIGNAL wire.
>
> ### Component Location
>
> The water in fuel indicator sensor is mounted by the original equipment manufacturer (OEM). Refer to the OEM service manual.
>
> ### Shoptalk
>
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected.. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.
>
> Possible causes of this fault code include:
>
> - Open return or signal circuit in the harness, connectors, or sensor
>
> - SIGNAL wire shorted to sensor supply or battery voltage.
>
> Refer to Troubleshooting Fault Code t05-4688.
