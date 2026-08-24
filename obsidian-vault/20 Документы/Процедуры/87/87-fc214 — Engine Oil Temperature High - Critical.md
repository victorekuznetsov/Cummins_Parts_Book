---
aliases:
  - "Высокая температура моторного масла — критично"
type: "Процедура"
doc: "87-fc214"
title_en: "Engine Oil Temperature High - Critical"
title_ru: "Высокая температура моторного масла — критично"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc214.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc214.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Engine Oil Temperature High - Critical
**Высокая температура моторного масла — критично**

> [!abstract] Процедура · `87-fc214`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc214.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc214.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 214

### Высокая температура моторного масла — критично

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 214 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Температура моторного масла превысила порог тревоги (затвора) для высокой температуры масла. | Двигатель отключится. |

![[19803595.png]]

Цепь датчика температуры масла

### Описание цепи

Датчик температуры масла используется ECM для мониторинга температуры моторного масла. Если температура масла становится слишком высокой и включена защита двигателя, будет понесено ухудшение состояния, что, возможно, приведет к отключению.

### Расположение компонента

См. диаграммы двигателя в разделе E этого руководства для определения местоположения компонента.

### Практические замечания

Сопротивление всех датчиков температуры изменяется в зависимости от температуры.

См. Код устранения неполадок t05-214


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 214
>
> ### Engine Oil Temperature High - Critical
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 214 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine oil temperature has exceeded the alarm (shutdown) threshold for high oil temperature. | Engine will shut down. |
>
> Oil Temperature Sensor Circuit
>
> ### Circuit Description
>
> The oil temperature sensor is used by the ECM to monitor the temperature of the engine oil. If the oil temperature becomes too high and engine protection is enabled, a derate condition will be incurred, possibly leading to shutdown.
>
> ### Component Location
>
> Refer to the Engine Diagrams in Section E of this manual for the component location.
>
> ### Shoptalk
>
> The resistance of all the temperature sensors varies with the temperature.
>
> Refer to Troubleshooting Fault Code t05-214
