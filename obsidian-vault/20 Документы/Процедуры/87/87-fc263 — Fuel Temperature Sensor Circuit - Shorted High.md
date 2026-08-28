---
aliases:
  - "Цепь датчика температуры топлива — замыкание на плюс"
type: "Процедура"
doc: "87-fc263"
title_en: "Fuel Temperature Sensor Circuit - Shorted High"
title_ru: "Цепь датчика температуры топлива — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc263.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc263.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Fuel Temperature Sensor Circuit - Shorted High
**Цепь датчика температуры топлива — замыкание на плюс**

> [!abstract] Процедура · `87-fc263`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc263.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc263.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 263

### Цепь датчика температуры топлива — замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 263 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Сигнал датчика температуры топлива двигателя высоко закорочен. | Отсутствие защиты двигателя от температуры топлива. Никакого влияния на производительность. |

![[19803592.png]]

Схема датчика температуры топлива

### Описание цепи

Датчик температуры топлива используется электронным модулем управления (ECM) для мониторинга температуры топлива. Температура топлива используется ECM для системы защиты двигателя, управления временем и заправкой. Если напряжение высокое, ECM регистрирует код 263 ошибки. Высокое напряжение может быть вызвано открытиями в сигнале или обратных проводах, шортами напряжения к сигналу или обратным проводам или неисправным открытым датчиком.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Сопротивление датчика изменяется в зависимости от температуры.

См. Код устранения неполадок t05-263


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 263
>
> ### Fuel Temperature Sensor Circuit - Shorted High
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 263 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine fuel temperature sensor signal is shorted high. | No engine protection for fuel temperature. No effect on performance. |
>
> Fuel Temperature Sensor Circuit
>
> ### Circuit Description
>
> The fuel temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the fuel. The fuel temperature is used by the ECM for the engine protection system, timing, and fueling control. If the voltage is high, the ECM will log Fault Code 263. High voltage can be caused by opens in the signal or return wires, voltage shorts to the signal or return wires, or a failed open sensor.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> The resistance of the sensor varies with the temperature.
>
> Refer to Troubleshooting Fault Code t05-263
