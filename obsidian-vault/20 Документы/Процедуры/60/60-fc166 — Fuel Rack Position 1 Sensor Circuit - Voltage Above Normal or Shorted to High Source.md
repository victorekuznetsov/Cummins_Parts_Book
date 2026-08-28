---
aliases:
  - "Цепь датчика положения рейки 1 — напряжение выше нормы"
type: "Процедура"
doc: "60-fc166"
title_en: "Fuel Rack Position 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика положения рейки 1 — напряжение выше нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc166.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc166.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Fuel Rack Position 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика положения рейки 1 — напряжение выше нормы**

> [!abstract] Процедура · `60-fc166`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc166.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc166.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 166

### Цепь датчика положения рейки 1 — напряжение выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 166 PID (P): S24 SPN: 1210 FMI: 3/3 лампы: Янтарная СРТ: | Высокое напряжение сигнала, обнаруженное на цепи сигнала датчика положения топливной стойки. | Возможно снижение производительности двигателя. |

![[19a00845.png]]

Сенсорная схема положения топливного стойка

### Описание цепи

Схема датчика положения топливной стойки снабжена источником переменного тока от ECM. Положение топливной стойки использует этот ток для изменения положения управляющей стойки, которая регулирует количество топлива, подаваемого от топливного насоса. Схема датчика обратной связи положения топливной стойки ретранслирует положение топливной стойки обратно в ECM.

### Расположение компонента

Датчик положения топливной стойки является внутренним для топливного насоса.

### Условия выполнения диагностики

Эта диагностика выполняется постоянно, пока контроллер генераторной установки активен или двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение цепи датчика положения топливной стойки находится вне диапазона.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

- Поврежденный или неисправный датчик положения топливной стойки

- Поврежденные или рыхлые связи.

См. код 166 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 166
>
> ### Fuel Rack Position 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 166 PID(P): S24 SPN: 1210 FMI: 3/3 Lamp: Amber SRT: | High signal voltage detected on the fuel rack position sensor signal circuit. | Possible reduced engine performance. |
>
> Fuel Rack Position Sensor Circuit
>
> ### Circuit Description
>
> The fuel rack position sensor circuit is supplied with a varying current source from the ECM. The fuel rack position uses this current to change the position of the control rack, which regulates the amount of fuel delivered from the fuel pump. The fuel rack position feedback sensor circuit relays the fuel rack position back to the ECM.
>
> ### Component Location
>
> The fuel rack position sensor is internal to the fuel pump.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the fuel rack position sensor circuit voltage is out of range high.
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
> - Damaged or malfunctioning fuel rack position sensor
>
> - Damaged or loose connections.
>
> Refer to Troubleshooting Fault Code 166.
