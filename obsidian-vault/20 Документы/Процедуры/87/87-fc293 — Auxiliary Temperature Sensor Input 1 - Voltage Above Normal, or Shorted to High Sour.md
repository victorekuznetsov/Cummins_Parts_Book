---
aliases:
  - "Вспомогательный вход датчика температуры 1 — напряжение выше нормы"
type: "Процедура"
doc: "87-fc293"
title_en: "Auxiliary Temperature Sensor Input 1 - Voltage Above Normal, or Shorted to High Source"
title_ru: "Вспомогательный вход датчика температуры 1 — напряжение выше нормы"
modified: "2020-01-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc293.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc293.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Auxiliary Temperature Sensor Input 1 - Voltage Above Normal, or Shorted to High Source
**Вспомогательный вход датчика температуры 1 — напряжение выше нормы**

> [!abstract] Процедура · `87-fc293`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2020-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc293.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc293.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 293

### Вспомогательный вход датчика температуры 1 — напряжение выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 293 PID(P): P441 SPN: 441 FMI: 3/3 лампы: Янтарная СРТ: | Напряжение, обнаруженное у изготовителя оригинального оборудования (OEM), контакт питания вспомогательного датчика температуры с левобережной проводкой OEM-интерфейса указывает на то, что датчик вышел из строя. | Ни одного на выступление. |

![[19n00476.png]]

Вспомогательный датчик температуры Input 1 Circuit

### Описание цепи

Вспомогательный датчик температуры OEM используется модулем управления двигателем (ECM) для мониторинга вспомогательной температуры OEM. Вспомогательный датчик температуры OEM, который не справился с низким уровнем, может быть вызван шортами, которые заземляются или открываются в проводах подачи и возврата, или внутренне заземленным датчиком.

### Расположение компонента

Расположение компонентов будет варьироваться в зависимости от OEM. См. сервисную документацию изготовителя оборудования.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения и двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что цепь температурного сигнала OEM находится вне диапазона.

### Действия системы при активном коде неисправности

ECM освещает лампу CHECK ENGINE и/или индикатор неисправности (MIL) сразу же после запуска и выхода из строя диагностического устройства.

### Условия сброса кода неисправности

- Для проверки ремонта выполните ключевой цикл, запустите двигатель и запустите его на холостом ходу в течение 1 минуты.

- Состояние кода ошибки, отображаемого рекомендуемым инструментом или эквивалентом электронного сервиса Cummins, будет изменено на INACTIVE сразу после диагностических запусков и проходов.

- ECM выключит лампу янтарного CHECK ENGINE сразу после диагностических прогонов и проходов.

- Необходимо использовать команду «Сбросить все ошибки» в рекомендуемой электронном сервисе Cummins или эквивалентной для устранения этой ошибки.

### Практические замечания

Возможные причины этого кода неисправности:

- Открытая обратная цепь в электропроводке, разъемах или датчике

- Открытая сигнальная цепь или сокращенная до источника напряжения.

См. Код устранения неполадок t05-293


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 293
>
> ### Auxiliary Temperature Sensor Input 1 - Voltage Above Normal, or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 293 PID(P): P441 SPN: 441 FMI: 3/3 Lamp: Amber SRT: | Voltage detected at the original equipment manufacturer (OEM) auxiliary temperature sensor supply pin of the left bank OEM interface wiring harness indicates the sensor has failed high. | None on performance. |
>
> Auxiliary Temperature Sensor Input 1 Circuit
>
> ### Circuit Description
>
> The OEM auxiliary temperature sensor supply is used by the engine control module (ECM) to monitor OEM auxiliary temperature. An OEM auxiliary temperature sensor that has failed low can be caused by shorts to ground or opens in the supply and return wires, or an internally grounded sensor.
>
> ### Component Location
>
> The component location will vary depending on the OEM. See equipment manufacturer service information.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position and the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the OEM temperature signal circuit is out of range high.
>
> ### Action Taken When The Fault Code Is Active
>
> The ECM illuminates the amber CHECK ENGINE lamp and/or the malfunction indicator lamp (MIL) immediately when the diagnostic runs and fails.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.
>
> - The fault code status displayed by the recommended Cummins electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.
>
> - The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.
>
> - It is necessary to use the "Reset All Faults" command in the recommended Cummins electronic service tool or equivalent to clear this fault.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Open return circuit in the harness, connectors, or sensor
>
> - Open signal circuit or shorted to a voltage source.
>
> Refer to Troubleshooting Fault Code t05-293
