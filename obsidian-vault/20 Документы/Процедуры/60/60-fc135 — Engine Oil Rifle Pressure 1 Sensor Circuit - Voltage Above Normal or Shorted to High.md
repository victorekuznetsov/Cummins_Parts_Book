---
aliases:
  - "Цепь датчика давления масла в главной магистрали 1 — напряжение выше нормы"
type: "Процедура"
doc: "60-fc135"
title_en: "Engine Oil Rifle Pressure 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика давления масла в главной магистрали 1 — напряжение выше нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc135.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc135.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Oil Rifle Pressure 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика давления масла в главной магистрали 1 — напряжение выше нормы**

> [!abstract] Процедура · `60-fc135`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc135.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc135.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 135

### Цепь датчика давления масла в главной магистрали 1 — напряжение выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 135 PID (P): P100 SPN: 100 FMI: 3/3 лампы: Янтарная СРТ: | Высокое напряжение сигнала, обнаруженное в цепи давления масла двигателя. | Ни одного на выступление. |

![[19a00847.png]]

Схема датчика давления в реактивной винтовке

### Описание цепи

Датчик давления винтовки моторного масла представляет собой датчик переменного сопротивления, используемый ECM для мониторинга давления моторного масла. Датчик давления винтовки с моторным маслом имеет три схемы: 5-вольтная цепь подачи, возврата и сигнала. Напряжение цепи сигнала указывает на давление масла в масляной винтовке.

### Расположение компонента

Датчик давления масла двигателя расположен в масляной винтовке.

### Условия выполнения диагностики

Эта диагностика выполняется постоянно, пока контроллер генераторной установки активен или двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала давления масла двигателя было вне диапазона.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

- Используется значение по умолчанию для показания давления масла в двигателе.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

- Неисправный или поврежденный датчик давления винтовки с моторным маслом.

См. код 135 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 135
>
> ### Engine Oil Rifle Pressure 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 135 PID(P): P100 SPN: 100 FMI: 3/3 Lamp: Amber SRT: | High signal voltage detected at the engine oil pressure circuit. | None on performance. |
>
> Engine Oil Rifle Pressure Sensor Circuit
>
> ### Circuit Description
>
> The engine oil rifle pressure sensor is a variable resistance sensor used by the ECM to monitor the lubricating oil pressure. The engine oil rifle pressure sensor has three circuits: 5 volt supply, return, and signal circuits. The signal circuit voltage indicates the oil pressure in the oil rifle.
>
> ### Component Location
>
> The engine oil pressure sensor is located in the oil rifle.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the engine oil pressure signal voltage was out of range high.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> - A default value for the engine oil pressure reading is used.
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
> - Malfunctioning or damaged engine oil rifle pressure sensor.
>
> Refer to Troubleshooting Fault Code 135.
