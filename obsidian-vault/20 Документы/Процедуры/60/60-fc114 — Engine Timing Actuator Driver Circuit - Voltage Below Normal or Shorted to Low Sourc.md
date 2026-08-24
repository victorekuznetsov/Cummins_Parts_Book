---
aliases:
  - "Цепь драйвера привода опережения — напряжение ниже нормы"
type: "Процедура"
doc: "60-fc114"
title_en: "Engine Timing Actuator Driver Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь драйвера привода опережения — напряжение ниже нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc114.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc114.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Timing Actuator Driver Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь драйвера привода опережения — напряжение ниже нормы**

> [!abstract] Процедура · `60-fc114`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc114.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc114.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 114

### Цепь драйвера привода опережения — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 114 PID(P): S20 SPN: 635 FMI: 4/4 лампы: Янтарная СРТ: | Низкое напряжение сигнала, обнаруженное в цепи привода привода синхронизации. | Возможно снижение производительности двигателя. |

![[19a00845.png]]

Схема привода привода двигателя

### Описание цепи

Схема привода синхронизации подает ток на привод синхронизации. ECM командует переменным количеством тока к приводу синхронизации, чтобы контролировать количество давления синхронизации на топливном форсунке.

### Расположение компонента

Привод синхронизации расположен на электронном клапанном узле управления.

### Условия выполнения диагностики

Эта диагностика выполняется, когда включается привод рельсового привода синхронизации.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение цепи привода синхронизации находится вне диапазона низкого.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

- Поврежденные или рыхлые связи.

См. Код 114 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 114
>
> ### Engine Timing Actuator Driver Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 114 PID(P): S20 SPN: 635 FMI: 4/4 Lamp: Amber SRT: | Low signal voltage detected at the timing actuator driver circuit. | Possible reduced engine performance. |
>
> Engine Timing Actuator Driver Circuit
>
> ### Circuit Description
>
> The timing actuator circuit supplies current to the timing actuator. The ECM commands a varying amount of current to the timing actuator to control the amount of timing pressure to the injectors.
>
> ### Component Location
>
> The timing actuator is located on the electronic control valve assembly.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs when the timing rail actuator is commanded ON.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the timing actuator circuit voltage is out of range low.
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
> - Malfunctioning or damaged engine wiring harness.
>
> - Damaged or loose connections.
>
> Refer to Troubleshooting Fault Code 114.
