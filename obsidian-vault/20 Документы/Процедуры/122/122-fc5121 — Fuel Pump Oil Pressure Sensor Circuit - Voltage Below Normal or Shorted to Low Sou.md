---
aliases:
  - "Цепь датчика давления масла топливного насоса — напряжение ниже нормы"
type: "Процедура"
doc: "122-fc5121"
title_en: "Fuel Pump Oil Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика давления масла топливного насоса — напряжение ниже нормы"
modified: "2020-04-16"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc5121.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc5121.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Fuel Pump Oil Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика давления масла топливного насоса — напряжение ниже нормы**

> [!abstract] Процедура · `122-fc5121`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2020-04-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc5121.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc5121.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 5121

### Цепь датчика давления масла топливного насоса — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 5121 P(P): SID(S) SPN: 520754 FMI: 4/4 лампы: Янтарная СРТ: | Низкое напряжение сигнала или открытая схема, обнаруженная в цепи давления масла топливного насоса. | Ни одного на выступление. |

![[19j00658.png]]

Схема датчика давления накачки топлива

### Описание цепи

Модуль управления двигателем (ECM) обеспечивает 5-вольтовую подачу на датчик давления масла топливного насоса двигателя на датчике.

Схема снабжения. ECM также обеспечивает заземление на обратной цепи датчика. Датчик давления масла в топливном насосе двигателя

обеспечивает сигнал к ECM на цепи сигнала датчика давления масла топливного насоса двигателя. Это датчик сигнала напряжения

изменения, основанные на давлении в пути потока масла. ECM будет обнаруживать низкое напряжение сигнала в условиях работы

Когда давление масла может быть немного ниже. ECM будет обнаруживать высокое напряжение сигнала во время высоких оборотов двигателя или

условия эксплуатации, когда давление масла высокое.

### Расположение компонента

Датчик давления масла топливного насоса двигателя расположен в головке фильтра масла топливного насоса двигателя, установленной на верхней части

Адаптер топливного насоса. Некоторые двигатели могут иметь головку фильтра, установленную удаленно.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

### Действия системы при активном коде неисправности

- ECM освещает лампу янтарного CHECK ENGINE сразу же, когда диагностика проходит и выходит из строя.

- Используется значение по умолчанию для показания давления масла топливного насоса.

### Условия сброса кода неисправности

- Для проверки ремонта выполните ключевой цикл, запустите двигатель и запустите его на холостом ходу в течение 1 минуты.

- Состояние кода ошибки, отображаемого рекомендованным электронным сервисным инструментом Cummins® или его эквивалентом, будет изменено на INACTIVE сразу после диагностических запусков и проходов.

- ECM выключит лампу янтарного CHECK ENGINE сразу после диагностических прогонов и проходов.

- Команда «Сбросить все ошибки» в рекомендуемой электронной сервисной оснастке Cummins® или эквиваленте может использоваться для устранения активных и неактивных ошибок.

### Практические замечания

Возможные причины этого кода неисправности:

- Схема сигнала открыта или закорочена до земли в ремне электропроводки двигателя или датчике.

- Провода снабжения открыты или закорочены на землю.

См. Код устранения неполадок t05-5121.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 5121
>
> ### Fuel Pump Oil Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 5121 PID(P): SID(S) SPN: 520754 FMI: 4/4 Lamp: Amber SRT: | Low signal voltage or open circuit detected at the fuel pump oil pressure circuit. | None on performance. |
>
> Engine Fuel Pump Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The engine control module (ECM) provides a 5-volt supply to the engine fuel pump oil pressure sensor on the sensor
>
> supply circuit. The ECM also provides a ground on the sensor return circuit. The engine fuel pump oil pressure sensor
>
> provides a signal to the ECM on the engine fuel pump oil pressure sensor signal circuit. This sensor signal voltage
>
> changes based on the pressure in the oil flow path. The ECM will detect a low signal voltage at operating conditions
>
> when the oil pressure may be slightly lower. The ECM will detect a high signal voltage during high engine speeds or
>
> operating conditions when the oil pressure is high.
>
> ### Component Location
>
> The engine fuel pump oil pressure sensor is located in the engine fuel pump oil filter head mounted to the top of the
>
> fuel pump adapter drive. Certain engines may have the filter head mounted remotely.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.
>
> - A default value for the fuel pump oil pressure reading is used.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.
>
> - The fault code status displayed by the recommended Cummins® electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.
>
> - The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active and inactive faults.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Signal circuit open or shorted to ground in the engine wiring harness or sensor.
>
> - Supply wire open or shorted to ground.
>
> Refer to Troubleshooting Fault Code t05-5121.
