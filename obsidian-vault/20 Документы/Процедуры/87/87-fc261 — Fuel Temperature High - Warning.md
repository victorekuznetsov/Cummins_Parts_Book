---
aliases:
  - "Высокая температура топлива — предупреждение"
type: "Процедура"
doc: "87-fc261"
title_en: "Fuel Temperature High - Warning"
title_ru: "Высокая температура топлива — предупреждение"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc261.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc261.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Fuel Temperature High - Warning
**Высокая температура топлива — предупреждение**

> [!abstract] Процедура · `87-fc261`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc261.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc261.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 261

### Высокая температура топлива — предупреждение

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 261 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Температура топлива двигателя превысила пороговое значение для высокой температуры топлива. | Калибровка-зависимая не принимается никаких действий ECM или выключение двигателя по мере повышения температуры над порогами. |

![[19803592.png]]

Схема датчика температуры топлива

### Описание цепи

Датчик температуры топлива используется электронным модулем управления (ECM) для мониторинга температуры топлива. Значение температуры топлива используется ECM для системы защиты двигателя.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Сопротивление всех датчиков температуры изменяется в зависимости от температуры.

См. Код устранения неполадок t05-261


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 261
>
> ### Fuel Temperature High - Warning
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 261 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine fuel temperature has exceeded the warning threshold for high fuel temperature. | Calibration-dependent no action is taken by the ECM, or engine shutdown as temperature increases over thresholds. |
>
> Fuel Temperature Sensor Circuit
>
> ### Circuit Description
>
> The fuel temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the fuel. The fuel temperature value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> The resistance of all the temperature sensors varies with the temperature.
>
> Refer to Troubleshooting Fault Code t05-261
