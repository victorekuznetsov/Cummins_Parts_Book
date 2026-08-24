---
aliases:
  - "Давление масла в главной магистрали ниже нормы — наивысший уровень"
type: "Процедура"
doc: "60-fc415"
title_en: "Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Most Severe Level"
title_ru: "Давление масла в главной магистрали ниже нормы — наивысший уровень"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc415.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc415.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Most Severe Level
**Давление масла в главной магистрали ниже нормы — наивысший уровень**

> [!abstract] Процедура · `60-fc415`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc415.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc415.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 415

### Давление масла в главной магистрали ниже нормы — наивысший уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 415 PID(P): P100 SPN: 100 FMI: 1/1 лампа: Красная СТО: | Давление масла ниже критического предела защиты двигателя. | Двигатель отключится. |

![[19a00847.png]]

Схема датчика давления в реактивной винтовке

### Описание цепи

Датчик давления винтовки моторного масла представляет собой датчик переменного сопротивления, используемый ECM для мониторинга давления моторного масла. Датчик давления винтовки с моторным маслом имеет три схемы: 5-вольтная цепь подачи, возврата и сигнала. Напряжение цепи сигнала указывает на давление масла в масляной винтовке.

### Расположение компонента

Датчик давления масла двигателя расположен в масляной винтовке.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что давление винтовки с моторным маслом ниже пределов защиты двигателя.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки отображает неисправность выключения сразу же, когда диагностика работает и выходит из строя.

- Двигатель будет отключен.

- Выходной крутящий момент двигателя будет уменьшен.

### Условия сброса кода неисправности

- Для проверки ремонта доведите двигатель до рабочей температуры и запускайте его в нормальных условиях нагрузки в течение 15 минут.

- Контроллер генераторной установки отключит индикатор выключения сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Уровень моторного масла выше или ниже спецификации.

- Засоряемый или ограниченный фильтр моторного масла.

- Датчик давления моторного масла работает неправильно.

- Главный регулятор давления масла работает неправильно

- Моторное масло всасывание или перенос трубки неисправен.

- Повреждение внутреннего двигателя.

См. Код 415 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 415
>
> ### Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Most Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 415 PID(P): P100 SPN: 100 FMI: 1/1 Lamp: Red SRT: | Oil pressure is below the engine protection critical limit. | Engine will shut down. |
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
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the engine oil rifle pressure is below the engine protection limits.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.
>
> - The engine will be shut down.
>
> - The torque output of the engine will be reduced.
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
> - Lubricating oil level is above or below specification.
>
> - Plugged or restricted lubricating oil filter.
>
> - Lubrication oil pressure sensor is malfunctioning.
>
> - Main oil pressure regulator is malfunctioning
>
> - Lubricating oil suction or transfer tube is malfunctioning.
>
> - Internal engine damage.
>
> Refer to Troubleshooting Fault Code 415.
