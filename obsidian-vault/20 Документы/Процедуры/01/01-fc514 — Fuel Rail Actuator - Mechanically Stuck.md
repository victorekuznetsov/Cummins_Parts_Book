---
aliases:
  - "Привод топливной рампы механически заклинил"
type: "Процедура"
doc: "01-fc514"
title_en: "Fuel Rail Actuator - Mechanically Stuck"
title_ru: "Привод топливной рампы механически заклинил"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc514.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc514.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Rail Actuator - Mechanically Stuck
**Привод топливной рампы механически заклинил**

> [!abstract] Процедура · `01-fc514`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc514.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc514.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 514

### Привод топливной рампы механически заклинил

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 514 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Клапан управления топливом — механически застрял. Ранее это называлось цепью привода топливного рельса. Погрешность между расчетным заправкой на рельсах и желаемым заправкой на рельсах выходит за пределы допустимых пределов. | Двигатель будет перегружаться, работать на одной скорости или будет **не** работать. |

![[19400781.png]]

Квантовая топливная система потока Схематический

### Описание цепи

ECM использует сигнал давления рельсов топлива и скорость двигателя для оценки фактического заправки, которую получает двигатель, а затем постоянно сравнивает это значение с желаемым заправкой для заданной скорости и нагрузки. Если ошибка в этих значениях слишком велика, то код 514 ошибки регистрируется.

### Расположение компонента

Привод топливной рельсы расположен на левой стороне (внизу) ECVA.

### Практические замечания

Расчетные топливные рельсы и требуемые параметры топливных рельсов можно контролировать на электронном сервисном оборудовании. Эта неисправность является проверкой контроля ECM привода рельса и последующего расхода топлива. Если требуемый топливный рельс может быть выполнен **не**, если требуется больше тока для привода, или если требуемый топливный рельс превышен и может **не** быть уменьшен путем уменьшения тока для привода, то код 514 по умолчанию регистрируется. Эта ошибка ** не зарегистрирована, когда:

- Скорость двигателя ниже 1200 об/мин

- Температура охлаждающей жидкости ниже 0°C[32°F]

- Код 451 или 452 ошибки активен. После того, как выключатель Run/Stop будет запущен, ошибка становится неактивной.

Устранение неполадок код t05-514


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 514
>
> ### Fuel Rail Actuator - Mechanically Stuck
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 514 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Fuel control valve - mechanically stuck. This was formerly called the fuel rail actuator circuit. The error between the estimated rail fueling and desired rail fueling is outside of acceptable limits. | Engine will overspeed, run at one speed, or will **not** run. |
>
> Quantum Fuel System Flow Schematic
>
> ### Circuit Description
>
> The ECM uses the fuel rail pressure signal and the engine speed to estimate the actual fueling that the engine is receiving, and then constantly compares this value to the desired fueling for the given speed and load. When there is too large of an error in these values for too long, then Fault Code 514 is logged.
>
> ### Component Location
>
> The fuel rail actuator is located on the left-side (bottom) of the ECVA.
>
> ### Shoptalk
>
> The estimated fuel rail and the desired fuel rail parameters can be monitored on the electronic service tool. This fault is a check on the ECM's control of the rail actuator and subsequent fuel flow. If the desired fuel rail can **not** be met by commanding more current to the actuator, or if the desired fuel rail is being exceeded and can **not** be reduced by reducing the current to the actuator, then Fault Code 514 is logged. This fault is **not** logged when:
>
> - Engine speed is below 1200 rpm
>
> - Coolant temperature is below 0°C \[32°F\]
>
> - Fault Code 451 or 452 is active. Once the Run/Stop switch is cycled, the fault becomes inactive.
>
> Refer to Troubleshooting Fault Code t05-514
