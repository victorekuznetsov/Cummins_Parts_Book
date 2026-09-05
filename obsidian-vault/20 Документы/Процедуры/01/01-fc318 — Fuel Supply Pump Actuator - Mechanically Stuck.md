---
aliases:
  - "Исполнительный механизм топливоподающего насоса — механически заклинил"
type: "Процедура"
doc: "01-fc318"
title_en: "Fuel Supply Pump Actuator - Mechanically Stuck"
title_ru: "Исполнительный механизм топливоподающего насоса — механически заклинил"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc318.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc318.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Supply Pump Actuator - Mechanically Stuck
**Исполнительный механизм топливоподающего насоса — механически заклинил**

> [!abstract] Процедура · `01-fc318`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc318.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc318.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 318

### Исполнительный механизм топливоподающего насоса — механически заклинил

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 318 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Исполнительный механизм топливоподающего насоса — механически заклинил. Погрешность между расчетным давлением топливного насоса и желаемым давлением топливного насоса выходит за допустимые пределы. | Никаких действий со стороны ЕКМ не предпринимается. Возможная потеря производительности. |

![[19400781.png]]

Схема расхода топлива

### Описание цепи

ECM использует сигнал давления топливного насоса и скорость двигателя для оценки фактического заправки, которую получает двигатель, и постоянно сравнивает это значение с желаемым заправкой для заданной скорости и нагрузки. Если в этих значениях слишком много ошибок, код 318 ошибки регистрируется.

### Расположение компонента

Привод топливного насоса находится на топливном насосе, чуть ниже датчика давления топлива.

### Практические замечания

Эта неисправность является проверкой на управление ECM приводом топливного насоса и последующим потоком топлива. Если требуемое заправка может быть выполнено **не**, если требуется больше тока для привода или если требуемое заправка превышена и может **не** быть уменьшено путем ограничения количества тока для привода, то код 318 по умолчанию регистрируется. Код 318 ошибки не регистрируется, если температура охлаждающей жидкости ниже 0°C \[32°F\].

- Убедитесь, что правильная калибровка загружена в ECM. Например, если калибровка QSK45 загружена в QSK60 ECM, этот код неисправности будет активирован.

- Проверьте наличие воздуха в топливной системе.

- Проверьте наличие высокого ограничения впуска топлива (засохший топливный фильтр и т.д.)

См. Код устранения неполадок t05-318


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 318
>
> ### Fuel Supply Pump Actuator - Mechanically Stuck
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 318 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel supply pump actuator - mechanically stuck. The error between the estimated fuel pump pressure and the desired fuel pump pressure is outside the allowable limits. | No action is taken by the ECM. Possible loss of performance. |
>
> Fuel System Flow Schematic
>
> ### Circuit Description
>
> The ECM uses the fuel pump pressure signal and engine speed to estimate the actual fueling the engine is receiving, and constantly compares this value to the desired fueling for the given speed and load. When there is too large of an error in these values for too long of a time, Fault Code 318 is logged.
>
> ### Component Location
>
> The fuel pump actuator is on the fuel pump, just below the fuel pressure sensor.
>
> ### Shoptalk
>
> This fault is a check on the ECM's control of the fuel pump actuator and subsequent fuel flow. If the desired fueling can **not** be met by commanding more current to the actuator or if the desired fueling is being exceeded and can **not** be reduced by limiting the amount of current to the actuator, then Fault Code 318 is logged. Fault Code 318 is **not** logged if the coolant temperature is below 0°C \[32°F\].
>
> - Make sure that the correct calibration loaded into the ECM. For example, if a QSK45 calibration is loaded into a QSK60 ECM, this fault code will be activated.
>
> - Check for air in the fuel system.
>
> - Check for high fuel inlet restriction (plugged fuel filter, etc.)
>
> Refer to Troubleshooting Fault Code t05-318
