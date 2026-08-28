---
aliases:
  - "Низкая температура охлаждающей жидкости — предупреждение"
type: "Процедура"
doc: "01-fc152"
title_en: "Engine Coolant Temperature Low - Warning"
title_ru: "Низкая температура охлаждающей жидкости — предупреждение"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc152.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc152.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Coolant Temperature Low - Warning
**Низкая температура охлаждающей жидкости — предупреждение**

> [!abstract] Процедура · `01-fc152`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc152.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc152.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 152

### Низкая температура охлаждающей жидкости — предупреждение

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 152 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Температура охлаждающей жидкости двигателя упала ниже порога предупреждения для низкой температуры охлаждающей жидкости. | Никаких действий со стороны ЕКМ не предпринимается. Никакого влияния на производительность. |

![[19803592.png]]

Цепь датчика температуры охлаждающей жидкости

### Описание цепи

Датчик температуры охлаждающей жидкости используется электронным модулем управления (ECM) для мониторинга температуры охлаждающей жидкости двигателя. Температура охлаждающей жидкости используется ECM для системы защиты двигателя, управления временем и заправкой. Если напряжение высокое более 2 секунд, ECM регистрирует код 152 ошибки.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Убедитесь, что поток воздуха через радиатор не затрудняется.Сопротивление всех датчиков температуры изменяется в зависимости от температуры.

См. Код устранения неполадок t05-152


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 152
>
> ### Engine Coolant Temperature Low - Warning
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 152 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine coolant temperature has dropped below the warning threshold for low coolant temperature. | No action is taken by the ECM. No effect on performance. |
>
> Coolant Temperature Sensor Circuit
>
> ### Circuit Description
>
> The coolant temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system, timing, and fueling control. If the voltage is high for more than 2 seconds, the ECM will log Fault Code 152.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Make sure the airflow through the radiator is **not** obstructed.The resistance of all the temperature sensors varies with the temperature.
>
> Refer to Troubleshooting Fault Code t05-152
