---
type: "Процедура"
doc: "19-fc514"
title_en: "Rail Fueling Flow Mismatch"
modified: "2011-03-01"
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
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc514.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc514.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Rail Fueling Flow Mismatch

> [!abstract] Процедура · `19-fc514`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc514.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc514.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 514

### Железнодорожное топливо расходует несоответствие

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 514 PID(P): S18 SPN: 633 FMI: 7 ламп: Красная СТО: 00-378 | Погрешность между расчетным заправкой рельсов и желаемым заправкой рельсов выходит за допустимые пределы. | Зависимое от калибровки отключение двигателя или снижение мощности или отсутствие действий со стороны ECM. Двигатель будет перегружаться, или работать на одной скорости или **не **работать. |

![[19400109.png]]

Схема расхода топлива

### Описание цепи

Электронный модуль управления (ECM) использует сигнал давления рельса и скорость двигателя для оценки фактического заправки, которую получает двигатель, а затем постоянно сравнивает это значение с желаемым заправкой для заданной скорости и нагрузки. Когда в этих значениях слишком большая ошибка в течение слишком долгого времени, эта ошибка регистрируется.

### Расположение компонента

Рельсовой привод расположен на нижней части корпуса управляющего клапана, по направлению к передней части двигателя, позади ECM.

### Практические замечания

Оценка заправки рельсами и желаемые параметры заправки рельсами могут контролироваться на электронном сервисном оборудовании INSITETM. Эта неисправность является проверкой контроля ECM привода рельса и последующего расхода топлива. Если требуемое заправочное усилие для рельсов может быть выполнено **не** путем подачи команды большему току на привод, или если требуемое топливное заправочное устройство превышено и может **не** быть уменьшено путем уменьшения тока на привод, эта ошибка регистрируется.

Эта ошибка не зарегистрирована, когда:

- Скорость двигателя ниже 1200 об/мин

- Температура охлаждающей жидкости ниже 0°C[32°F]

- Код 451 или 452 ошибки активен. После того, как переключатель зажигания цикличен, ошибка становится неактивной.

Устранение неполадок код t05-514


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 514
>
> ### Rail Fueling Flow Mismatch
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 514 PID(P): S18 SPN: 633 FMI: 7 Lamp: Red SRT: 00-378 | The error between the estimated rail fueling and the desired rail fueling is outside the acceptable limits. | Calibration-dependent engine shutdown or power derate or no action by the ECM is taken. Engine will overspeed, or run at one speed or **not** run. |
>
> Fuel System Flow Schematic
>
> ### Circuit Description
>
> The electronic control module (ECM) uses the rail pressure signal and the engine speed to estimate the actual fueling that the engine is receiving and then constantly compares this value to the desired fueling for the given speed and load. When there is too large an error in these values for too long a time, this fault is logged.
>
> ### Component Location
>
> The rail actuator is located on the bottom of the control valve body, toward the engine front, behind the ECM.
>
> ### Shoptalk
>
> The estimated rail fueling and the desired rail fueling parameters can be monitored on INSITE™ electronic service tool. This fault is a check on the ECM's control of the rail actuator and subsequent fuel flow. If the desired rail fueling can **not** be met by commanding more current to the actuator, or if the desired fuel railing is being exceeded and can **not** be reduced by reducing the current to the actuator, this fault is logged.
>
> This fault is **not** logged when:
>
> - Engine speed is below 1200 rpm
>
> - Coolant temperature is below 0°C \[32°F\]
>
> - Fault Code 451 or 452 is active. Once the keyswitch is cycled, the fault becomes inactive.
>
> Refer to Troubleshooting Fault Code t05-514
