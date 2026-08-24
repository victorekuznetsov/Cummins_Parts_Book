---
aliases:
  - "Высокая температура моторного масла — предупреждение"
type: "Процедура"
doc: "01-fc421"
title_en: "Engine Oil Temperature High - Warning"
title_ru: "Высокая температура моторного масла — предупреждение"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc421.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc421.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Oil Temperature High - Warning
**Высокая температура моторного масла — предупреждение**

> [!abstract] Процедура · `01-fc421`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc421.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc421.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 421

### Высокая температура моторного масла — предупреждение

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 421 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Температура моторного масла превысила пороговое значение для высокой температуры масла. | Никаких действий со стороны ЕКМ не предпринимается. Возможная потеря производительности. |

![[19803595.png]]

Цепь датчика температуры масла

### Описание цепи

Датчик температуры масла используется электронным модулем управления (ECM) для мониторинга температуры масла двигателя. Температура масла становится слишком высокой, и обеспечивается защита двигателя, может возникнуть ухудшение состояния, что может привести к отключению.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Сопротивление всех датчиков температуры изменяется в зависимости от температуры.

См. Код устранения неполадок t05-421


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 421
>
> ### Engine Oil Temperature High - Warning
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 421 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine oil temperature has exceeded the warning threshold for high oil temperature. | No action is taken by the ECM. Possible loss of performance. |
>
> Oil Temperature Sensor Circuit
>
> ### Circuit Description
>
> The oil temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine oil. The oil temperature becomes too high and engine protection is enabled, a derate condition could by incurred, possibly leading to shutdown.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> The resistance of all the temperature sensors varies with the temperature.
>
> Refer to Troubleshooting Fault Code t05-421
