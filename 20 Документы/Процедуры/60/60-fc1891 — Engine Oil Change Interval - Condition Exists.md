---
aliases:
  - "Достигнут интервал замены масла — условие возникло"
type: "Процедура"
doc: "60-fc1891"
title_en: "Engine Oil Change Interval - Condition Exists"
title_ru: "Достигнут интервал замены масла — условие возникло"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1891.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1891.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Oil Change Interval - Condition Exists
**Достигнут интервал замены масла — условие возникло**

> [!abstract] Процедура · `60-fc1891`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1891.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1891.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1891

### Достигнут интервал замены масла — условие возникло

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1891 PID(P): S115 SPN: 1378 FMI: 11/31 лампа: Янтарная СРТ: | Условия двигателя препятствуют работе клапана сгорания моторного масла. | Моторное масло сжигает клапан соленоида, неспособного впрыскивать масло. |

![[19a00860.png]]

Двигатель сжигает соленоидную цепь.

### Описание цепи

Двигатель сжигающего клапана моторного масла контролирует поток масла в клапане управления маслом во время цикла горения.

### Расположение компонента

Соленоид горящего клапана моторного масла расположен в верхней части горящего клапана моторного масла. Расположение ожогового клапана зависит от OEM.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что система клапанов сгорания масла двигателя не может работать в течение длительного периода времени из-за условий двигателя.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

### Условия сброса кода неисправности

- Для проверки ремонта, выполнить ключевой цикл, запустить двигатель и выполнить эксплуатационный тест CentinelTM с использованием рекомендуемой электронной сервисной оснастки Cummins® или эквивалента.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Когда моторное масло сжигает клапан соленоида, пытается впрыснуть масло и не может, это создает количество промахов. Когда эти подсчеты достигают заданного уровня, код ошибки становится активным. Если бак для масляной косметики ** не используется, рекомендуется менять моторное масло в следующий интервал технического обслуживания.

Возможные причины этого кода неисправности:

- Неправильное давление моторного масла

- Неправильная температура охлаждающей жидкости двигателя

- низкий уровень моторного масла

- Неисправный клапан сгорания моторного масла

- Неисправный или повреждённый жгут проводов двигателя.

- Неисправность или повреждение OEM-проводов.

См. Troubleshooting Fault Code 1891.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1891
>
> ### Engine Oil Change Interval - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1891 PID(P): S115 SPN: 1378 FMI: 11/31 Lamp: Amber SRT: | Engine conditions are preventing engine oil burn valve operation. | Engine oil burn valve solenoid unable to inject oil. |
>
> Engine Oil Burn Valve Solenoid Driver Circuit.
>
> ### Circuit Description
>
> The engine oil burn valve solenoid driver controls the flow of oil in the oil control valve during the burn cycle.
>
> ### Component Location
>
> The engine oil burn valve solenoid is located in the top of the engine oil burn valve. The location of the burn valve is OEM dependent.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the engine oil burn valve system has been unable to operate for an extended period of time due to engine conditions.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, perform a keycycle, start the engine and perform the Centinel™ Operational Test using the recommended Cummins® electronic service tool or equivalent.
>
> - The generator set controller will turn off the warning indicator immediately after the user presses reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> When the engine oil burn valve solenoid tries to inject oil and can not, it generates a miss count. When these counts reach a predefined level, the fault code becomes active. If an oil make up tank is **not** used, it is recommended to change the engine oil at the next maintenance interval.
>
> Possible causes of this fault code include:
>
> - Incorrect engine oil pressure
>
> - Incorrect engine coolant temperature
>
> - low lubrication oil level
>
> - A faulty engine oil burn valve
>
> - Malfunctioning or damaged engine wiring harness.
>
> - Malfunctioning or damaged OEM wiring harness.
>
> Refer to Troubleshooting Fault Code 1891.
