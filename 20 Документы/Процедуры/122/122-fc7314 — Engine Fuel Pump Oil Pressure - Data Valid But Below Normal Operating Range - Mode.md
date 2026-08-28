---
aliases:
  - "Давление масла топливного насоса ниже нормы — умеренный уровень"
type: "Процедура"
doc: "122-fc7314"
title_en: "Engine Fuel Pump Oil Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level"
title_ru: "Давление масла топливного насоса ниже нормы — умеренный уровень"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc7314.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc7314.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Engine Fuel Pump Oil Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level
**Давление масла топливного насоса ниже нормы — умеренный уровень**

> [!abstract] Процедура · `122-fc7314`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2020-04-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc7314.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc7314.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 7314

### Давление масла топливного насоса ниже нормы — умеренный уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 7314 PID(P): SID(S) SPN: 520754 FMI: 1/18 лампы: Янтарная СРТ: | Сигнал давления масла топливного насоса двигателя указывает, что давление масла ниже предела предупреждения о защите двигателя. | Ни одного на выступление. |

![[19j00658.png]]

Схема датчика давления накачки топлива

### Описание цепи

Модуль управления двигателем (ECM) обеспечивает 5-вольтовую подачу на датчик давления масла топливного насоса двигателя на датчике.

Схема снабжения. ECM также обеспечивает заземление на обратной цепи датчика. Датчик давления масла в топливном насосе двигателя

обеспечивает сигнал к ECM на цепи сигнала датчика давления масла топливного насоса двигателя. Это датчик сигнала напряжения

изменения, основанные на давлении в пути потока нефти. ECM будет обнаруживать низкое напряжение сигнала в условиях работы

Когда давление масла может быть немного ниже. ECM будет обнаруживать высокое напряжение сигнала во время высоких оборотов двигателя или

условия эксплуатации, когда давление масла высокое.

### Расположение компонента

Датчик давления масла топливного насоса двигателя расположен в головке фильтра масла топливного насоса двигателя, установленной на верхней части

Адаптер топливного насоса. Некоторые двигатели могут иметь головку фильтра, установленную удаленно.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что давление масла в топливном насосе было ниже минимальных эксплуатационных пределов.

### Действия системы при активном коде неисправности

- ECM освещает лампу янтарного CHECK ENGINE сразу же, когда диагностика проходит и выходит из строя.

### Условия сброса кода неисправности

- Для проверки ремонта выполните ключевой цикл, запустите двигатель и запустите его на холостом ходу в течение 1 минуты.

- Состояние кода ошибки, отображаемого рекомендованным электронным сервисным инструментом Cummins® или его эквивалентом, будет изменено на INACTIVE сразу после диагностических запусков и проходов.

- ECM выключит лампу янтарного CHECK ENGINE сразу после диагностических прогонов и проходов.

- Команда «Сбросить все ошибки» в рекомендуемой электронной сервисной оснастке Cummins® или эквиваленте может использоваться для устранения активных и неактивных ошибок.

### Практические замечания

Возможные причины этого кода неисправности:

- Низкое давление масла

- Неправильный уровень масла

- Поврежденный датчик давления масла

- Засоряемый или ограниченный фильтр моторного масла.

- Путь потока моторного масла с ограниченным или зажатым потоком.

См. Код устранения неполадок t05-7314.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 7314
>
> ### Engine Fuel Pump Oil Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 7314 PID(P): SID(S) SPN: 520754 FMI: 1/18 Lamp: Amber SRT: | Engine fuel pump oil pressure signal indicates oil pressure is below the engine protection warning limit. | None on performance. |
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
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the fuel pump oil pressure was below minimum operating limits.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.
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
> - Low oil pressure
>
> - Incorrect oil level
>
> - Damaged oil pressure sensor
>
> - Plugged or restricted lubricating oil filter.
>
> - Plugged or restricted lubricating oil flow path.
>
> Refer to Troubleshooting Fault Code t05-7314.
