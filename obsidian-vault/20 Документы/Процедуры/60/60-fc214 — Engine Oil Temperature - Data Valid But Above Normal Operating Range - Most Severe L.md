---
aliases:
  - "Температура моторного масла выше нормы — наивысший уровень"
type: "Процедура"
doc: "60-fc214"
title_en: "Engine Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Температура моторного масла выше нормы — наивысший уровень"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc214.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc214.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level
**Температура моторного масла выше нормы — наивысший уровень**

> [!abstract] Процедура · `60-fc214`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc214.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc214.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 214

### Температура моторного масла выше нормы — наивысший уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 214 PID(P): P175 SPN: 175 ФМИ: 0/0 лампа: Красная СТО: | Температура масла двигателя выше предела защиты двигателя. | Двигатель отключится. |

![[19a00857.png]]

Схема датчика температуры моторного масла

### Описание цепи

Датчик температуры моторного масла представляет собой датчик переменного резистора, используемый ECM для мониторинга температуры моторного масла. Датчик температуры моторного масла имеет две схемы: сигнал и обратные цепи. Напряжение сигнала указывает на температуру моторного масла.

### Расположение компонента

Датчик температуры моторного масла расположен в адаптере масляной поддона на левом берегу.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что температура масла двигателя была выше предела защиты двигателя.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки отображает неисправность выключения сразу же, когда диагностика работает и выходит из строя.

- Выходной крутящий момент двигателя будет уменьшен.

- Двигатель будет отключен.

### Условия сброса кода неисправности

- Для проверки ремонта доведите двигатель до рабочей температуры и запускайте его в нормальных условиях нагрузки в течение 15 минут.

- Контроллер генераторной установки отключит индикатор выключения сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный охладитель моторного масла.

- Неисправный или поврежденный датчик температуры моторного масла.

См. Код 214 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 214
>
> ### Engine Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 214 PID(P): P175 SPN: 175 FMI: 0/0 Lamp: Red SRT: | Engine oil temperature is above the engine protection limit. | Engine will shut down. |
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
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the engine oil temperature was greater than the engine protection limit.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.
>
> - The torque output of the engine will be reduced.
>
> - The engine will be shut down.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, bring the engine up to operating temperature and run it in normal loaded conditions for 15 minutes.
>
> - The generator set controller will turn off the shutdown indicator immediately after the user presses the reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning lubricating oil cooler.
>
> - A malfunctioning or damaged engine oil temperature sensor.
>
> Refer to Troubleshooting Fault Code 214.
