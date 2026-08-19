---
aliases:
  - "Потерян один из двух сигналов частоты/положения коленвала — недопустимая скорость изменения"
type: "Процедура"
doc: "60-fc121"
title_en: "Engine Magnetic Crankshaft Speed/Position Lost One of Two Signals - Abnormal Rate of Change"
title_ru: "Потерян один из двух сигналов частоты/положения коленвала — недопустимая скорость изменения"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc121.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc121.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Magnetic Crankshaft Speed/Position Lost One of Two Signals - Abnormal Rate of Change
**Потерян один из двух сигналов частоты/положения коленвала — недопустимая скорость изменения**

> [!abstract] Процедура · `60-fc121`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc121.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc121.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 121

### Потерян один из двух сигналов частоты/положения коленвала — недопустимая скорость изменения

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 121 PID(P): P190 SPN: 190 FMI: 10/10 лампа: Янтарная СРТ: | Сигнал о скорости двигателя не был обнаружен ни с основных, ни с резервных датчиков скорости. | Возможно снижение производительности двигателя. |

![[19a00846.png]]

Схема датчика скорости/позиции коленчатого вала двигателя.

### Описание цепи

Датчики положения коленчатого вала и положения распределительного вала являются датчиками типа эффекта Холла. Модуль управления двигателем (ECM) обеспечивает подачу 5 вольт на датчик положения и обратную цепь. Когда зубы на коленчатом валу или ямочки в задней части распределительного устройства перемещаются мимо датчика положения, на цепи сигнала датчика положения генерируется сигнал. ECM интерпретирует этот сигнал и преобразует его в скорость двигателя. Отсутствующий зуб на коленчатом валу используется ECM для определения положения двигателя.

### Расположение компонента

Датчик скорости двигателя и датчик положения двигателя расположены в корпусе маховика.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил сбой сигнала с датчиком скорости коленчатого вала двигателя или датчиком положения двигателя.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

- Двигатель будет работать на резервном сигнале скорости, предоставляемом датчиком положения двигателя.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении электронного инструментария или эквивалента Cummins®. При устранении неисправности кода используйте адрес источника, отображаемый в инструменте электронного обслуживания Cummins® или эквивалент, чтобы определить, какая ECM и схема затронута.

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

- Поврежденный или неисправный датчик скорости двигателя

- Поврежденный или неисправный датчик положения двигателя.

- Поврежденное колесо тона

См. Код 121 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 121
>
> ### Engine Magnetic Crankshaft Speed/Position Lost One of Two Signals - Abnormal Rate of Change
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 121 PID(P): P190 SPN: 190 FMI: 10/10 Lamp: Amber SRT: | No engine speed signal detected from either the main or backup speed sensors. | Possible reduced engine performance. |
>
> Engine Crankshaft Speed/Position Sensor Circuit.
>
> ### Circuit Description
>
> The crankshaft position and camshaft position sensors are Hall effect type sensors. The engine control module (ECM) provides a 5 volt supply to the position sensor and a return circuit. As the teeth on the crankshaft speed ring or the dimples in the back of the camshaft gear move past the position sensor, a signal is generated on the position sensor signal circuit. The ECM interprets this signal and converts it to an engine speed. A missing tooth on the crankshaft gear is used by the ECM to determine the position of the engine.
>
> ### Component Location
>
> The engine speed sensor and the engine position sensor are located in the flywheel housing.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected a signal failure with engine crankshaft speed sensor or engine position sensor.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> - Engine will run on backup speed signal provided by engine position sensor.
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
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged engine wiring harness.
>
> - Damaged or malfunctioning engine speed sensor
>
> - Damaged or malfunctioning engine position sensor.
>
> - Damaged tone wheel
>
> Refer to Troubleshooting Fault Code 121.
