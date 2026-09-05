---
type: "Процедура"
doc: "19-fc318"
title_en: "Fuel Pump Fueling Flow Mismatch"
modified: "2022-05-04"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc318.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc318.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Fuel Pump Fueling Flow Mismatch

> [!abstract] Процедура · `19-fc318`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2022-05-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc318.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc318.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 318

### Топливный насос Топливный поток Несоответствие

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 318 P(P): S78 SPN: 931 FMI: 7 ламп: Желтая СТО: 00-671 | Давление топливного насоса и желаемое давление топливного насоса **не** в пределах калиброванных значений. | Никаких действий со стороны ЕКМ не предпринимается. |

![[19803917.png]]

Схема подачи топлива - QSK19 Industrial

![[19803920.png]]

Схема подачи топлива - QSK23 Industrial

![[19803919.png]]

Схема сигнала расхода топлива - привод генератора QSK23

![[19803918.png]]

Схема подачи топлива - QSK45 и QSK60

![[19803916.png]]

Схема подачи топлива - QSK60

![[19803915.png]]

Схема подачи топлива - QSK78

### Описание цепи

Модуль управления двигателем (ECM) использует сигнал давления топливного насоса и скорость двигателя для оценки фактического заправки, которую получает двигатель, а затем постоянно сравнивает это значение с желаемым заправкой для заданной скорости и нагрузки.

### Расположение компонента

Привод топливного насоса расположен на топливном насосе.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения или когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил значительную разницу между фактическим и расчетным заправкой.

### Действия системы при активном коде неисправности

- ECM освещает лампу янтарного CHECK ENGINE сразу же, когда диагностика проходит и выходит из строя.

### Условия сброса кода неисправности

- Для проверки ремонта выполните ключевой цикл, запустите двигатель и запустите его на холостом ходу в течение 1 минуты.

- Состояние кода ошибки, отображаемого рекомендованным электронным сервисным инструментом Cummins® или его эквивалентом, будет изменено на INACTIVE сразу после диагностических запусков и проходов.

- ECM выключит лампу янтарного CHECK ENGINE сразу после диагностических прогонов и проходов.

- Необходимо использовать команду «Сбросить все ошибки» в рекомендованной электронном сервисном инструменте Cummins® или эквиваленте для устранения этой ошибки.

### Практические замечания

Эта неисправность является проверкой на управление ECM приводом топливного насоса и последующим потоком топлива. Если требуемое заправка может быть выполнена **не**, если требуется меньше тока для привода, или если требуемое заправка превышена и может **не** быть уменьшено путем увеличения тока для привода, то код 318 по умолчанию регистрируется.

См. Код устранения неполадок t05-318


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 318
>
> ### Fuel Pump Fueling Flow Mismatch
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 318 PID(P): S78 SPN: 931 FMI: 7 Lamp: Yellow SRT: 00-671 | Fuel pump pressure and desired fuel pump pressure is **not** within the calibrated values. | No action is taken by the ECM. |
>
> Fuel Flow Signal Circuit - QSK19 Industrial
>
> Fuel Flow Signal Circuit - QSK23 Industrial
>
> Fuel Flow Signal Circuit - QSK23 Generator Drive
>
> Fuel Flow Signal Circuit - QSK45 and QSK60
>
> Fuel Flow Signal Circuit - QSK60
>
> Fuel Flow Signal Circuit - QSK78
>
> ### Circuit Description
>
> The Engine Control Module (ECM) uses the fuel pump pressure signal and engine speed to estimate the actual fueling the engine is receiving, and then constantly compares this value to the desired fueling for the given speed and load.
>
> ### Component Location
>
> The fuel pump actuator is located on the fuel pump.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected a significant difference between actual and calculated fueling.
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
> - It is necessary to use the "Reset All Faults" command in the recommended Cummins® electronic service tool or equivalent to clear this fault.
>
> ### Shoptalk
>
> This fault is a check on the ECM's control of the fuel pump actuator and subsequent fuel flow. If the desired fueling can **not** be met by commanding less current to the actuator, or if the desired fueling is being exceeded and can **not** be reduced by increasing the current to the actuator, then Fault Code 318 is logged.
>
> Refer to Troubleshooting Fault Code t05-318
