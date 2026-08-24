---
aliases:
  - "Цепь потенциометра статизма — напряжение ниже нормы"
type: "Процедура"
doc: "122-fc3696"
title_en: "Droop Adjust Potentiometer Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь потенциометра статизма — напряжение ниже нормы"
modified: "2010-09-27"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc3696.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc3696.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Droop Adjust Potentiometer Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь потенциометра статизма — напряжение ниже нормы**

> [!abstract] Процедура · `122-fc3696`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc3696.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc3696.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 3696

### Цепь потенциометра статизма — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 3696 PID (P): СПН: 4183 FMI: 4 лампы: Янтарная СРТ: | Цепь потенциометра статизма — напряжение ниже нормы | Потенциометр с понижающим регулировкой будет переходить к значению по умолчанию. |

![[19e00970.png]]

QSK38 CM2150 Power Generation - регулировка потенциометра с крутым спуском

![[19602288.png]]

QSK50 CM2150 без усовершенствованного мониторинга двигателя / QSK50 CM2150 с расширенным мониторингом двигателя / QSK60 CM2150 с электрогенерацией - регулировка потенциометра с крутящим моментом

![[19602296.png]]

QSK38 CM2150 Морской вспомогательный модуль с панелью C Command EliteTM и C Command Elite PlusTM

![[19602297.png]]

QSK38 CM2150 Морской вспомогательный прибор с панелью C CommandTM - схема регулировки потенциометра с крутым спуском

![[19602288.png]]

QSK50 и QSK60 CM2150 Морской вспомогательный модуль с системой панели C Command EliteTM и C Command Elite PlusTM / QSK60 CM2150 Drill Rig - Droop Adjust Potentiometer Circuit

![[19602299.png]]

QSK50 и QSK60 CM2150 Морской вспомогательный модуль с панелью C CommandTM - схема регулировки потенциометра с крутым спуском

### Описание цепи

Потенциометр с отрегулировкой слюны используется для регулирования отключения двигателя.

### Расположение компонента

Потенциометр с откидным регулированием расположен на панели управления генератором. См. сервисное руководство изготовителя машины.

### Практические замечания

Существует несколько электронных модулей управления (ECM) для моделей двигателей, включенных в это руководство. У каждого блока управления свой адрес источника, который отображается при подключении INSITE™. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Возможные причины кода неисправности включают:

- Провод SIGNAL открыт или коротко заземлен

- Провода открываются или закорачиваются на землю.

См. Код 3696 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 3696
>
> ### Droop Adjust Potentiometer Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 3696 PID(P): SPN: 4183 FMI: 4 Lamp: Amber SRT: | Droop Adjust Potentiometer Circuit - Voltage Below Normal or Shorted to Low Source | The droop adjust potentiometer will go to the default value. |
>
> QSK38 CM2150 Power Generation -Droop Adjust Potentiometer Circuit
>
> QSK50 CM2150 without Advanced Engine Monitoring/QSK50 CM2150 with Advanced Engine Monitoring/QSK60 CM2150 Power Generation - Droop Adjust Potentiometer Circuit
>
> QSK38 CM2150 Marine Auxiliary with C Command Elite™ and C Command Elite Plus™ Panel System - Droop Adjust Potentiometer Circuit
>
> QSK38 CM2150 Marine Auxiliary with C Command™ Panel System - Droop Adjust Potentiometer Circuit
>
> QSK50 and QSK60 CM2150 Marine Auxiliary with C Command Elite™ and C Command Elite Plus™ Panel System/QSK60 CM2150 Drill Rig - Droop Adjust Potentiometer Circuit
>
> QSK50 and QSK60 CM2150 Marine Auxiliary with C Command™ Panel System - Droop Adjust Potentiometer Circuit
>
> ### Circuit Description
>
> The droop adjust potentiometer is used to regulate the engine droop.
>
> ### Component Location
>
> The droop adjust potentiometer is located on the generator control panel. Refer to the OEM service manual.
>
> ### Shoptalk
>
> There are multiple electronic control module (ECM)s for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.
>
> Possible causes of the fault code include:
>
> - SIGNAL wire open or shorted to ground
>
> - SUPPLY wire open or shorted to ground.
>
> Refer to Troubleshooting Fault Code 3696.
