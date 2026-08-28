---
aliases:
  - "Привод рейки механически заклинил в закрытом положении — ниже нормы — умеренный уровень"
type: "Процедура"
doc: "60-fc173"
title_en: "Fuel Rack Actuator Driver Mechanically Stuck Closed - Data Valid But Below Normal Operating Range - Moderately Severe Level"
title_ru: "Привод рейки механически заклинил в закрытом положении — ниже нормы — умеренный уровень"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc173.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc173.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Fuel Rack Actuator Driver Mechanically Stuck Closed - Data Valid But Below Normal Operating Range - Moderately Severe Level
**Привод рейки механически заклинил в закрытом положении — ниже нормы — умеренный уровень**

> [!abstract] Процедура · `60-fc173`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc173.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc173.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 173

### Привод рейки механически заклинил в закрытом положении — ниже нормы — умеренный уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 173 PID(P): S23 SPN: 638 FMI: 1/18 лампы: Янтарная СРТ: | Реестр управления топливом находится в застрявшем положении. | Возможно снижение производительности двигателя. |

![[19a00845.png]]

Схема привода привода топливного рейка

### Описание цепи

Реестр управления топливом и соленоид определяют количество топлива, отмеренное для двигателя.

### Расположение компонента

Реестр управления топливом и соленоид являются внутренними частями топливного насоса.

### Условия выполнения диагностики

Эта диагностика выполняется постоянно, пока контроллер генераторной установки активен или двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что топливный стойка застряла или **не** реагирует на команды заправки.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Разъем разъема или поврежденного привода.

- Неисправный топливный насос.

См. Код 173 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 173
>
> ### Fuel Rack Actuator Driver Mechanically Stuck Closed - Data Valid But Below Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 173 PID(P): S23 SPN: 638 FMI: 1/18 Lamp: Amber SRT: | Fuel control rack is in a stuck position. | Possible reduced engine performance. |
>
> Fuel Rack Actuator Driver Circuit
>
> ### Circuit Description
>
> The fuel control rack and solenoid determine the quantity of fuel metered to the engine.
>
> ### Component Location
>
> The fuel control rack and solenoid are internal parts of the fuel injection pump.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the fuel rack is stuck or **not** responding to fueling commands.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, start the engine and let it run for 1 minute at no load.
>
> - The generator set controller will turn off the warning indicator immediately after the user presses reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Loose or damaged actuator connector.
>
> - Malfunctioning fuel pump.
>
> Refer to Troubleshooting Fault Code 173.
