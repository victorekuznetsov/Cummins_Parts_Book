---
aliases:
  - "Потеряны оба сигнала частоты/положения — данные нестабильны или неверны"
type: "Процедура"
doc: "60-fc115"
title_en: "Engine Magnetic Speed/Position Lost Both of Two Signals - Data Erratic, Intermittent, or Incorrect"
title_ru: "Потеряны оба сигнала частоты/положения — данные нестабильны или неверны"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc115.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc115.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Magnetic Speed/Position Lost Both of Two Signals - Data Erratic, Intermittent, or Incorrect
**Потеряны оба сигнала частоты/положения — данные нестабильны или неверны**

> [!abstract] Процедура · `60-fc115`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc115.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc115.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 115

### Потеряны оба сигнала частоты/положения — данные нестабильны или неверны

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 115 P(P): P190 SPN: 612 FMI: 2/2 лампы: Красная СТО: | Оба сигнала не были обнаружены в цепи датчика положения двигателя. | Двигатель выключится или не запустится. |

![[19a00846.png]]

Двигатель Crankshaft Speed Sensor Circuit

### Описание цепи

Датчики положения коленчатого вала и положения распределительного вала являются датчиками типа эффекта Холла. Модуль управления двигателем (ECM) обеспечивает подачу 5 вольт на датчик положения и обратную цепь. Когда зубы на коленчатом валу или ямочки в задней части распределительного устройства перемещаются мимо датчика положения, на цепи сигнала датчика положения генерируется сигнал. ECM интерпретирует этот сигнал и преобразует его в скорость двигателя. Отсутствующий зуб на коленчатом валу используется ECM для определения положения двигателя.

### Расположение компонента

Датчик скорости двигателя и датчик положения двигателя расположены в корпусе маховика.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что положение коленчатого вала и входы сигнала положения распределительного вала в ECM отсутствуют или обращены вспять.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки отображает неисправность выключения сразу же, когда диагностика работает и выходит из строя.

- Энергетический момент двигателя будет уменьшен, если двигатель работает в течение длительного периода времени с активным разломом.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки отключит индикатор выключения сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Датчик положения коленчатого вала и разъёмы разъёма ремня положения распределительного вала обращены вспять.

- Поврежденные или рыхлые разъемы.

- Неисправный или повреждённый жгут проводов двигателя.

См. Код 115 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 115
>
> ### Engine Magnetic Speed/Position Lost Both of Two Signals - Data Erratic, Intermittent, or Incorrect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 115 PID(P): P190 SPN: 612 FMI: 2/2 Lamp: Red SRT: | Both signals failed to be detected at the engine position sensor circuit. | The engine will shut down or will **not** start. |
>
> Engine Crankshaft Speed Sensor Circuit
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
> The Engine Control Module (ECM) detected the crankshaft position and camshaft position signal inputs to the ECM are missing or reversed.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.
>
> - Engine torque will be reduced if the engine is operated for an extended period of time with this fault active.
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
> Possible causes of this fault code include:
>
> - Crankshaft position sensor and the camshaft position sensor wiring harness connectors are reversed.
>
> - Damaged or loose connectors.
>
> - Malfunctioning or damaged engine wiring harness.
>
> Refer to Troubleshooting Fault Code 115.
