---
aliases:
  - "Высокая температура топлива — критично"
type: "Процедура"
doc: "01-fc266"
title_en: "Fuel Temperature High - Critical"
title_ru: "Высокая температура топлива — критично"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc266.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc266.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Temperature High - Critical
**Высокая температура топлива — критично**

> [!abstract] Процедура · `01-fc266`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc266.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc266.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 266

### Высокая температура топлива — критично

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 266 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Температура топлива двигателя превысила порог отключения для высокой температуры топлива. | Двигатель отключится. |

![[19803592.png]]

Схема датчика температуры топлива

### Описание цепи

Датчик температуры топлива используется электронным модулем управления (ECM) для мониторинга температуры топлива. Значение температуры топлива используется ECM для системы защиты двигателя.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Сопротивление всех датчиков температуры изменяется в зависимости от температуры.

См. Код устранения неполадок t05-266


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 266
>
> ### Fuel Temperature High - Critical
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 266 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine fuel temperature has exceeded the shutdown threshold for high fuel temperature. | Engine will shut down. |
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
> Refer to Troubleshooting Fault Code t05-266
