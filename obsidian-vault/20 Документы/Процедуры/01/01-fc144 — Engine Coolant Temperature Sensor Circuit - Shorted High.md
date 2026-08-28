---
aliases:
  - "Цепь датчика температуры ОЖ — замыкание на плюс"
type: "Процедура"
doc: "01-fc144"
title_en: "Engine Coolant Temperature Sensor Circuit - Shorted High"
title_ru: "Цепь датчика температуры ОЖ — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc144.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc144.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Coolant Temperature Sensor Circuit - Shorted High
**Цепь датчика температуры ОЖ — замыкание на плюс**

> [!abstract] Процедура · `01-fc144`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc144.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc144.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 144

### Цепь датчика температуры ОЖ — замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 144 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Сигнал датчика температуры охлаждающей жидкости двигателя высоко закорочен. | Отсутствие защиты двигателя от температуры охлаждающей жидкости. Возможен белый дым. |

![[19803592.png]]

Схема датчика температуры двигателя

### Описание цепи

Датчик температуры охлаждающей жидкости используется электронным модулем управления (ECM) для мониторинга температуры охлаждающей жидкости двигателя. Температура охлаждающей жидкости используется ECM для системы защиты двигателя, управления временем и заправкой. Если напряжение высокое, ECM регистрирует код 144 ошибки. Высокое напряжение может быть вызвано открытиями в сигнале или обратных проводах, шортами напряжения к сигналу или обратным проводам или неисправным открытым датчиком.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Сопротивление датчика изменяется в зависимости от температуры.

Устранение неполадок код t05-144


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 144
>
> ### Engine Coolant Temperature Sensor Circuit - Shorted High
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 144 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine coolant temperature sensor signal is shorted high. | No engine protection for coolant temperature. Possible white smoke. |
>
> Engine Coolant Temperature Sensor Circuit
>
> ### Circuit Description
>
> The coolant temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system, timing, and fueling control. If the voltage is high, the ECM will log Fault Code 144. Voltage high can be caused by opens in the signal or return wires, voltage shorts to the signal or return wires, or a failed open sensor.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> The resistance of the sensor varies with the temperature.
>
> Refer to Troubleshooting Fault Code t05-144
