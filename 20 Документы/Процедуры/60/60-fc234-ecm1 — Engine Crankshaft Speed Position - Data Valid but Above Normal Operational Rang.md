---
aliases:
  - "Частота/положение коленвала выше нормы — наивысший уровень"
type: "Процедура"
doc: "60-fc234-ecm1"
title_en: "Engine Crankshaft Speed/Position - Data Valid but Above Normal Operational Range - Most Severe Level"
title_ru: "Частота/положение коленвала выше нормы — наивысший уровень"
modified: "2018-06-19"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc234-ecm1.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc234-ecm1.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Crankshaft Speed/Position - Data Valid but Above Normal Operational Range - Most Severe Level
**Частота/положение коленвала выше нормы — наивысший уровень**

> [!abstract] Процедура · `60-fc234-ecm1`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2018-06-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc234-ecm1.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc234-ecm1.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 234-ECM1

### Частота/положение коленвала выше нормы — наивысший уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 234 PID(P): СПН: 190 FMI: 0 лампочка: Красная СТО: | Частота/положение коленвала выше нормы — наивысший уровень. Сигнал скорости двигателя указывает на скорость двигателя выше предела защиты двигателя. | Впрыск топлива отключается до тех пор, пока скорость двигателя не упадет ниже предела скорости. |

![[19a00862.png]]

Скорость коленчатого вала / позиционная схема - Интерфейс QST30

### Описание цепи

Датчик скорости коленчатого вала двигателя и датчик скорости распределительного вала двигателя обеспечивают информацию о скорости двигателя и положении для ECM через электропроводку двигателя.

### Расположение компонента

Датчик скорости коленчатого вала двигателя расположен в корпусе маховика.[[60-100-002 — Engine Diagrams|См. процедуру 100-002 в разделе E.]]

### Практические замечания

Существует несколько ECM. У каждого блока управления свой адрес источника, который отображается при подключении INSITE™. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Возможные причины этого кода неисправности:

- Внешние источники топлива, втягиваемые в воздухозаборник

- Обратное питание (моторирование) двигателя

- Укрощение датчика скорости коленчатого вала двигателя и датчика скорости распредвала двигателя.

Проверить впускной коллектор на наличие источников легковоспламеняющихся паров. Проверьте уплотнения турбокомпрессора, чтобы убедиться, что нет утечек масла. Осмотрите датчик скорости коленчатого вала двигателя и датчик скорости распределительного вала двигателя на предмет повреждения или подделки.

См. Код устранения неполадок t05-234


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 234-ECM1
>
> ### Engine Crankshaft Speed/Position - Data Valid but Above Normal Operational Range - Most Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 234 PID(P): SPN: 190 FMI: 0 Lamp: Red SRT: | Engine Crankshaft Speed/Position - Data Valid but Above Normal Operational Range - Most Severe Level. Engine speed signal indicates engine speed above engine protection limit. | Fuel injection disabled until engine speed falls below the overspeed limit. |
>
> Crankshaft Speed/Position Circuit - QST30 Power Generation Interface Engine
>
> ### Circuit Description
>
> The engine crankshaft speed sensor and engine camshaft speed sensor provide engine speed and position information to the ECM through the engine harness.
>
> ### Component Location
>
> The engine crankshaft speed sensor is located in the flywheel housing. [[60-100-002 — Engine Diagrams|Refer to Procedure 100-002 in Section E.]]
>
> ### Shoptalk
>
> There are multiple ECMs. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.
>
> Possible causes of this fault code include:
>
> - External fuel sources drawn into the intake air passage
>
> - Reverse powering (motoring) of the engine
>
> - Tampering of the engine crankshaft speed sensor and the engine camshaft speed sensor.
>
> Inspect the intake manifold for sources of flammable vapors. Check the turbocharger seals to verify that there are no oil leaks. Inspect the engine crankshaft speed sensor and the engine camshaft speed sensor for damage or tampering.
>
> Refer to Troubleshooting Fault Code t05-234
