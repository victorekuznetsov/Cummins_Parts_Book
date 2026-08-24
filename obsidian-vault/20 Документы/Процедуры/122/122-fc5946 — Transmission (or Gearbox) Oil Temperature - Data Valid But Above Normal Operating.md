---
aliases:
  - "Температура масла трансмиссии — данные достоверны, выше нормы — умеренный уровень"
type: "Процедура"
doc: "122-fc5946"
title_en: "Transmission (or Gearbox) Oil Temperature - Data Valid But Above Normal Operating Range - Moderately Severe Level"
title_ru: "Температура масла трансмиссии — данные достоверны, выше нормы — умеренный уровень"
modified: "2017-01-03"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc5946.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc5946.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Transmission (or Gearbox) Oil Temperature - Data Valid But Above Normal Operating Range - Moderately Severe Level
**Температура масла трансмиссии — данные достоверны, выше нормы — умеренный уровень**

> [!abstract] Процедура · `122-fc5946`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-01-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc5946.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc5946.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 5946

### Температура масла трансмиссии — данные достоверны, выше нормы — умеренный уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 5946 PID(P): СПН: 175 ФМИ: 0 лампочка: Красная СТО: | Температура масла трансмиссии — данные достоверны, выше нормы — умеренный уровень. Датчик температуры масла трансмиссии (или коробки передач) указывает, что температура масла трансмиссии (или коробки передач) выше предела защиты. | Отсутствие защиты двигателя от температуры масла. |

![[19k00131.png]]

Температура моторного масла 1 Сенсорная схема

### Описание цепи

Датчик температуры масла трансмиссии (или коробки передач) используется модулем управления двигателем (ECM) для мониторинга температуры масла трансмиссии. ECM контролирует напряжение на контакте сигнала и преобразует его в температурное значение.

### Расположение компонента

Датчик температуры масла трансмиссии (или коробки передач) расположен в трансмиссии.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. У каждого блока управления свой адрес источника, который отображается при подключении INSITE™. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Этот код неисправности указывает на то, что температура коробки передач (или коробки передач) превысила пределы защиты для высокой температуры коробки передач (или коробки передач).

См. Код 5946 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 5946
>
> ### Transmission (or Gearbox) Oil Temperature - Data Valid But Above Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 5946 PID(P): SPN: 175 FMI: 0 Lamp: Red SRT: | Transmission (or Gearbox) Oil Temperature - Data Valid But Above Normal Operating Range - Moderately Severe Level. The transmission (or gearbox) oil temperature sensor indicates the transmission (or gearbox) oil temperature is above the protection limit. | No engine protection for engine oil temperature. |
>
> Engine Oil Temperature 1 Sensor Circuit
>
> ### Circuit Description
>
> The transmission (or gearbox) oil temperature sensor is used by the engine control module (ECM) to monitor the transmission oil temperature. The ECM monitors the voltage on the SIGNAL pin and converts it to a temperature value.
>
> ### Component Location
>
> The transmission (or gearbox) oil temperature sensor is located in the transmission.
>
> ### Shoptalk
>
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.
>
> This fault code indicates that the transmission (or gearbox) temperature has exceeded the protection limits for high transmission (or gearbox) temperature.
>
> Refer to Troubleshooting Fault Code 5946.
