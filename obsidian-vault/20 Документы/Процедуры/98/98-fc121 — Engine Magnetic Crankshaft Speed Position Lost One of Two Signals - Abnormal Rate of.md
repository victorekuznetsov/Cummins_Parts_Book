---
aliases:
  - "Потерян один из двух сигналов частоты/положения коленвала — недопустимая скорость изменения"
type: "Процедура"
doc: "98-fc121"
title_en: "Engine Magnetic Crankshaft Speed/Position Lost One of Two Signals - Abnormal Rate of Change"
title_ru: "Потерян один из двух сигналов частоты/положения коленвала — недопустимая скорость изменения"
modified: "2021-09-08"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc121.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc121.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Magnetic Crankshaft Speed/Position Lost One of Two Signals - Abnormal Rate of Change
**Потерян один из двух сигналов частоты/положения коленвала — недопустимая скорость изменения**

> [!abstract] Процедура · `98-fc121`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc121.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc121.pdf)

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
| Код неисправности: 121 PID(P): 190 SPN: ФМИ: 10 ламп: Флешинг SRT: 00-621 | Сигнал о скорости двигателя не был обнаружен ни с основных, ни с резервных датчиков скорости. | Ни одного на выступление. |

![[19802309.png]]

Цепь датчика частоты вращения двигателя

### Описание цепи

Датчик скорости двигателя - это датчик скорости с двумя каналами, используемый ECM для мониторинга скорости двигателя. Датчик скорости имеет четыре схемы: Две сигнальные цепи и две обратные цепи. Когда зубы на маховике коленчатого вала проходят мимо датчика скорости, на цепях сигналов датчика скорости генерируется сигнал.

### Расположение компонента

Датчик скорости двигателя расположен на корпусе маховика.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил сбой сигнала с датчиком скорости двигателя.

### Действия системы при активном коде неисправности

- ECM освещает лампу янтарного CHECK ENGINE сразу же, когда диагностика проходит и выходит из строя.

Для приложений генерации электроэнергии:

- Контроллер генераторной установки отображает неисправность сразу же, когда диагностика работает и выходит из строя.

- Двигатель будет работать на резервном сигнале скорости, обеспечиваемом датчиком положения распредвала.

### Условия сброса кода неисправности

- Для проверки ремонта выполните ключевой цикл, запустите двигатель и запустите его на холостом ходу в течение 1 минуты.

- Состояние кода ошибки, отображаемого рекомендованным электронным сервисным инструментом Cummins® или его эквивалентом, будет изменено на INACTIVE сразу после диагностических запусков и проходов.

- ECM выключит лампу янтарного CHECK ENGINE сразу после диагностических прогонов и проходов.

- Команда «Сбросить все ошибки» в рекомендуемой электронной сервисной оснастке Cummins® или эквиваленте может использоваться для устранения активных и неактивных ошибок.

Для приложений генерации электроэнергии:

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки выключит индикатор сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

• Неисправный или поврежденный датчик скорости двигателя.

См. Код устранения неполадок t05-121


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
> | Fault Code: 121 PID(P): 190 SPN: FMI: 10 Lamp: Flashing SRT: 00-621 | No engine speed signal detected from either the main or backup speed sensors. | None on performance. |
>
> Engine Speed Sensor Circuit
>
> ### Circuit Description
>
> The engine speed sensor is dual channel speed sensor used by the ECM to monitor the engine speed. The speed sensor has four circuits: two signal circuits, and two return circuits. As the teeth on the crankshaft flywheel move past the speed sensor, a signal is generated on the speed sensor signal circuits.
>
> ### Component Location
>
> The engine speed sensor is located on the flywheel housing.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected a signal failure with engine speed sensor.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.
>
> For Power Generation Applications:
>
> - The generator set controller displays the fault immediately when the diagnostics runs and fails.
>
> - Engine will run on backup speed signal provided by the camshaft position sensor.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.
>
> - The fault code status displayed by the recommended Cummins® electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.
>
> - The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active and inactive faults.
>
> For Power Generation Applications:
>
> - To validate the repair, start the engine and let it run for 1 minute at no load.
>
> - The generator set controller will turn off the indicator immediately after the user presses reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged engine wiring harness.
>
> • Malfunctioning or damaged engine speed sensor.
>
> Refer to Troubleshooting Fault Code t05-121
