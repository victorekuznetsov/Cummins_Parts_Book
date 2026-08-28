---
aliases:
  - "Цепь датчика температуры масла 1 — напряжение ниже нормы"
type: "Процедура"
doc: "60-fc213"
title_en: "Engine Oil Temperature Sensor 1 Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика температуры масла 1 — напряжение ниже нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc213.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc213.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Oil Temperature Sensor 1 Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика температуры масла 1 — напряжение ниже нормы**

> [!abstract] Процедура · `60-fc213`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc213.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc213.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 213

### Цепь датчика температуры масла 1 — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 213 P(P): P175 SPN: 175 ФМИ: 4/4 лампы: Янтарная СРТ: | Низкое напряжение сигнала, обнаруженное в цепи датчика температуры моторного масла. | Ни одного на выступление. |

![[19a00857.png]]

Схема датчика температуры моторного масла

### Описание цепи

Датчик температуры моторного масла представляет собой датчик переменного резистора, используемый ECM для мониторинга температуры моторного масла. Датчик температуры моторного масла имеет две схемы: сигнал и обратные цепи. Напряжение сигнала указывает на температуру моторного масла.

### Расположение компонента

Датчик температуры моторного масла расположен в адаптере масляной поддона на левом берегу.

### Условия выполнения диагностики

Эта диагностика выполняется постоянно, пока контроллер генераторной установки активен или двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала датчика температуры масла двигателя было вне диапазона низкого.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

- Используется значение по умолчанию для показания температуры моторного масла.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

- Неисправный или поврежденный датчик температуры моторного масла.

См. Код 213 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 213
>
> ### Engine Oil Temperature Sensor 1 Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 213 PID(P): P175 SPN: 175 FMI: 4/4 Lamp: Amber SRT: | Low signal voltage detected at engine oil temperature sensor circuit. | None on performance. |
>
> Engine Oil Temperature Sensor Circuit
>
> ### Circuit Description
>
> The engine oil temperature sensor is a variable resistor sensor used by the ECM to monitor the engine oil temperature. The engine oil temperature sensor has two circuits: signal, and return circuits. The signal voltage indicates the engine oil temperature.
>
> ### Component Location
>
> The engine oil temperature sensor is located in the oil pan adapter on the left bank.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active or when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the engine oil temperature sensor signal voltage was out of range low.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> - A default value for the engine oil temperature reading is used.
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
> - A malfunctioning or damaged engine oil temperature sensor.
>
> Refer to Troubleshooting Fault Code 213.
