---
aliases:
  - "Цепь датчика барометрического давления — напряжение ниже нормы"
type: "Процедура"
doc: "19-fc222"
title_en: "Barometric Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика барометрического давления — напряжение ниже нормы"
modified: "2024-03-06"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc222.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc222.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Barometric Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика барометрического давления — напряжение ниже нормы**

> [!abstract] Процедура · `19-fc222`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2024-03-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc222.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc222.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 222

### Цепь датчика барометрического давления — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 222 PID(P): P108 SPN: 108 FMI: 4/4 лампы: Янтарная СРТ: | Низкое напряжение, обнаруженное на датчике давления окружающего воздуха. | Возможно снижение производительности двигателя. |

![[11m00068.png]]

Цепь датчика атмосферного давления

### Описание цепи

Датчик давления окружающего воздуха обеспечивает сигнал давления окружающего воздуха к ECM через электропроводку двигателя. ECM использует датчик давления окружающего воздуха для регулировки заправки топливом в зависимости от высоты.

### Расположение компонента

Датчик давления окружающего воздуха расположен ниже ECM на корпусе управляющего клапана.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения или когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала давления окружающего воздуха было вне диапазона низкого.

### Действия системы при активном коде неисправности

- ECM освещает лампу янтарного CHECK ENGINE сразу же, когда диагностика проходит и выходит из строя.

- Используется значение по умолчанию для показания давления окружающего воздуха.

### Условия сброса кода неисправности

- Для проверки ремонта выполните ключевой цикл, запустите двигатель и запустите его на холостом ходу в течение 1 минуты.

- Состояние кода ошибки, отображаемого рекомендованным электронным сервисным инструментом Cummins® или его эквивалентом, будет изменено на INACTIVE сразу после диагностических запусков и проходов.

- ECM выключит лампу янтарного CHECK ENGINE сразу после диагностических прогонов и проходов.

- Команда «Сбросить все ошибки» в рекомендуемой электронной сервисной оснастке Cummins® или эквиваленте может использоваться для устранения активных и неактивных ошибок.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправность или повреждение датчика давления окружающего воздуха.

- Неисправный или повреждённый жгут проводов двигателя.

См. Код устранения неполадок t05-222


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 222
>
> ### Barometric Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 222 PID(P): P108 SPN: 108 FMI: 4/4 Lamp: Amber SRT: | Low voltage detected at the ambient air pressure sensor. | Possible reduced engine performance. |
>
> Ambient Air Pressure Sensor Circuit
>
> ### Circuit Description
>
> The ambient air pressure sensor provides the ambient air pressure signal to the ECM through the engine harness. The ECM uses the ambient air pressure sensor to adjust fueling based on the altitude.
>
> ### Component Location
>
> The ambient air pressure sensor is located below the ECM on the control valve body.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the ambient air pressure signal voltage was out of range low.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.
>
> - A default value for the ambient air pressure reading is used.
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
> - Malfunctioning or damaged ambient air pressure sensor.
>
> - Malfunctioning or damaged engine wiring harness.
>
> Refer to Troubleshooting Fault Code t05-222
