---
aliases:
  - "Высокая температура впускного коллектора 1 — предупреждение"
type: "Процедура"
doc: "01-fc488"
title_en: "Intake Manifold Temperature Number 1 High - Warning"
title_ru: "Высокая температура впускного коллектора 1 — предупреждение"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc488.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc488.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Intake Manifold Temperature Number 1 High - Warning
**Высокая температура впускного коллектора 1 — предупреждение**

> [!abstract] Процедура · `01-fc488`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc488.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc488.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 488

### Высокая температура впускного коллектора 1 — предупреждение

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 488 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Температура воздуха впускного коллектора двигателя превысила пороговое значение для высокой температуры впускного коллектора. | Калибровка зависима. Модуль управления двигателем не предпринимает никаких действий или выключения двигателя по мере повышения температуры над порогами. Водитель реле Pre-HET заряжается энергией. |

![[19803595.png]]

Цепь датчика температуры во впускном коллекторе

### Описание цепи

Датчик температуры впускного коллектора используется электронным модулем управления (ECM) для мониторинга температуры воздуха в впускном коллекторе после охладителя. Температура впускного коллектора используется ECM для системы защиты двигателя, управления временем и заправкой.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Сопротивление датчика изменяется в зависимости от температуры.

Устранение неполадок код t05-488


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 488
>
> ### Intake Manifold Temperature Number 1 High - Warning
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 488 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine intake manifold air temperature has exceeded the warning threshold for high intake manifold temperature. | Calibration-dependent. No action is taken by the engine control module, or engine shutdown as temperature increases over thresholds. Pre-HET relay driver is energized. |
>
> Intake Manifold Temperature Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the air in the intake manifold after the aftercooler. The intake manifold temperature is used by the ECM for the engine protection system, timing, and fueling control.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> The resistance of the sensor varies with the temperature.
>
> Refer to Troubleshooting Fault Code t05-488
