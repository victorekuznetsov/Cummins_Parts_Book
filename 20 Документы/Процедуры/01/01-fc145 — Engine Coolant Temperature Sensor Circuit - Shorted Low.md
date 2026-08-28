---
aliases:
  - "Цепь датчика температуры ОЖ — замыкание на массу"
type: "Процедура"
doc: "01-fc145"
title_en: "Engine Coolant Temperature Sensor Circuit - Shorted Low"
title_ru: "Цепь датчика температуры ОЖ — замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc145.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc145.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Coolant Temperature Sensor Circuit - Shorted Low
**Цепь датчика температуры ОЖ — замыкание на массу**

> [!abstract] Процедура · `01-fc145`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc145.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc145.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 145

### Цепь датчика температуры ОЖ — замыкание на массу

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 145 PID (P): СПН: ФМИ: Лампа: Предупреждение СТО: | Сигнал датчика температуры охлаждающей жидкости двигателя низко закорачивается. | Отсутствие защиты двигателя от температуры охлаждающей жидкости. Возможен белый дым. |

![[19803592.png]]

Цепь датчика температуры охлаждающей жидкости

### Описание цепи

Датчик температуры охлаждающей жидкости используется электронным модулем управления (ECM) для мониторинга температуры охлаждающей жидкости двигателя. Температура охлаждающей жидкости используется ECM для системы защиты двигателя, контроля времени и заправки. Если напряжение низкое более 2 секунд, ECM регистрирует код 145 ошибки. Низкое напряжение может быть вызвано шортами, которые заземляются на проводах питания или возврата или на внутренне заземленном неисправном датчике.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Сопротивление датчика изменяется в зависимости от температуры.

Устранение неполадок код t05-145


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 145
>
> ### Engine Coolant Temperature Sensor Circuit - Shorted Low
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 145 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine coolant temperature sensor signal is shorted low. | No engine protection for coolant temperature. Possible white smoke. |
>
> Coolant Temperature Sensor Circuit
>
> ### Circuit Description
>
> The coolant temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system, timing and fueling control. If the voltage is low for more than 2 seconds, the ECM will log Fault Code 145. Low voltage can be caused by shorts to ground on the supply or return wires or an internally grounded failed sensor.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> The resistance of the sensor varies with the temperature.
>
> Refer to Troubleshooting Fault Code t05-145
