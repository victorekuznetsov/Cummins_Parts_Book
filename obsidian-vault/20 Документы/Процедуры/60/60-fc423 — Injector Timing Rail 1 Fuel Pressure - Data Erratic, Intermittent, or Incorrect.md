---
aliases:
  - "Давление топлива в рампе опережения 1 — данные нестабильны или неверны"
type: "Процедура"
doc: "60-fc423"
title_en: "Injector Timing Rail 1 Fuel Pressure - Data Erratic, Intermittent, or Incorrect"
title_ru: "Давление топлива в рампе опережения 1 — данные нестабильны или неверны"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc423.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc423.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Injector Timing Rail 1 Fuel Pressure - Data Erratic, Intermittent, or Incorrect
**Давление топлива в рампе опережения 1 — данные нестабильны или неверны**

> [!abstract] Процедура · `60-fc423`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc423.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc423.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 423

### Давление топлива в рампе опережения 1 — данные нестабильны или неверны

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 423 PID(P): P156 SPN: 156 FMI: 2/2 лампы: Янтарная СРТ: | Напряжение сигнала указывает на то, что сигнал датчика давления времени является иррациональным. | Возможно снижение производительности двигателя. |

![[19a00870.png]]

Схема привода привода двигателя

### Описание цепи

Схема привода привода синхронизации двигателя используется для управления началом впрыска. Модуль управления двигателем (ECM) контролирует ток на цепи питания с модулированной шириной импульса привода синхронизации.

### Расположение компонента

Привод давления в момент двигателя является внутренним для топливного насоса.

### Условия выполнения диагностики

Эта диагностика выполняется, когда включается привод рельсового привода синхронизации.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил ошибку времени или количества заправки для всех топливных форсунок.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

### Условия сброса кода неисправности

- Для проверки ремонта доведите двигатель до рабочей температуры и запускайте его в нормальных условиях нагрузки в течение 15 минут.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Поврежденный или неисправный привод двигателя синхронизации

- Поврежденные или рыхлые разъемы.

- Неисправный или повреждённый жгут проводов двигателя.

- Ограничение дренажа

См. Код 423 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 423
>
> ### Injector Timing Rail 1 Fuel Pressure - Data Erratic, Intermittent, or Incorrect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 423 PID(P): P156 SPN: 156 FMI: 2/2 Lamp: Amber SRT: | Signal voltage indicates that the timing pressure sensor signal is irrational. | Possible reduced engine performance. |
>
> Engine Fuel Timing Actuator Circuit
>
> ### Circuit Description
>
> The engine fuel timing actuator circuit is used to control the start of injection. The engine control module (ECM) monitors the current on the timing actuator pulse width modulated supply circuit.
>
> ### Component Location
>
> The engine timing pressure actuator is internal to the fuel pump.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs when the timing rail actuator is commanded ON.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected a fueling timing or quantity error for all injectors.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, bring the engine up to operating temperature and run it in normal loaded conditions for 15 minutes.
>
> - The generator set controller will turn off the warning indicator immediately after the user presses reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Damaged or malfunctioning engine fuel timing actuator
>
> - Damaged or loose connectors.
>
> - Malfunctioning or damaged engine wiring harness.
>
> - Drainline restriction
>
> Refer to Troubleshooting Fault Code 423.
