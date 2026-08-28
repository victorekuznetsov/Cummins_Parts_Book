---
aliases:
  - "Частота/положение коленвала выше нормы — умеренный уровень"
type: "Процедура"
doc: "60-fc1992"
title_en: "Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Moderately Severe Level"
title_ru: "Частота/положение коленвала выше нормы — умеренный уровень"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1992.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc1992.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Moderately Severe Level
**Частота/положение коленвала выше нормы — умеренный уровень**

> [!abstract] Процедура · `60-fc1992`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1992.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc1992.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1992

### Частота/положение коленвала выше нормы — умеренный уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1992 PID(P): P190 SPN: 190 FMI: 0/16 лампа: Красная СТО: | Сигнал скорости коленчатого вала двигателя указывает на скорость двигателя выше предела защиты двигателя. | Двигатель отключится. |

![[19a00864.png]]

Двигатель Crankshaft Speed Sensor Circuit

### Описание цепи

Датчики положения коленчатого вала и положения распределительного вала являются датчиками типа эффекта Холла. Модуль управления двигателем (ECM) обеспечивает подачу 5 вольт на датчик положения и обратную цепь. Когда зубы на коленчатом валу или ямочки в задней части распределительного устройства перемещаются мимо датчика положения, на цепи сигнала датчика положения генерируется сигнал. ECM интерпретирует этот сигнал и преобразует его в скорость двигателя. Отсутствующий зуб на коленчатом валу используется ECM для определения положения двигателя.

### Расположение компонента

Датчик скорости/положения коленчатого вала двигателя расположен на корпусе маховика.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что датчик скорости коленчатого вала двигателя выше пределов защиты двигателя.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки отображает неисправность выключения сразу же, когда диагностика работает и выходит из строя.

- Двигатель будет отключен.

- Заправка двигателя прекращается до тех пор, пока скорость двигателя не упадет до нормальных рабочих скоростей.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки отключит индикатор выключения сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении электронного инструментария или эквивалента Cummins®. При устранении неисправности кода используйте адрес источника, отображаемый в инструменте электронного обслуживания Cummins® или эквивалент, чтобы определить, какая ECM и схема затронута.

Возможные причины этого кода неисправности:

- Внешние источники топлива, втягиваемые в воздухозаборник

- Обратное питание (моторирование) двигателя

- Уплотнение датчиков скорости/положения двигателя.

См. Troubleshooting Fault Code 1992.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1992
>
> ### Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1992 PID(P): P190 SPN: 190 FMI: 0/16 Lamp: Red SRT: | Engine crankshaft speed signal indicates engine speed above engine protection limit. | Engine will shut down. |
>
> Engine Crankshaft Speed Sensor Circuit
>
> ### Circuit Description
>
> The crankshaft position and camshaft position sensors are Hall effect type sensors. The engine control module (ECM) provides a 5 volt supply to the position sensor and a return circuit. As the teeth on the crankshaft speed ring or the dimples in the back of the camshaft gear move past the position sensor, a signal is generated on the position sensor signal circuit. The ECM interprets this signal and converts it to an engine speed. A missing tooth on the crankshaft gear is used by the ECM to determine the position of the engine.
>
> ### Component Location
>
> The engine crankshaft speed/position sensor is located on the flywheel housing.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the engine crankshaft speed sensor is higher than the engine protection limits.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.
>
> - The engine will be shut down.
>
> - Fueling to the engine is stopped until the engine speed drops to normal operating speeds.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, start the engine and let it run for 1 minute at no load.
>
> - The generator set controller will turn off the shutdown indicator immediately after the user presses the reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.
>
> Possible causes of this fault code include:
>
> - External fuel sources drawn into the intake air passage
>
> - Reverse powering (motoring) of the engine
>
> - Tampering of the engine speed/position sensors.
>
> Refer to Troubleshooting Fault Code 1992.
