---
type: "Процедура"
doc: "98-fc234"
title_en: "Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Most Severe Level"
modified: "2021-09-09"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc234.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc234.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Most Severe Level

> [!abstract] Процедура · `98-fc234`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc234.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc234.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 234

### Скорость/позиция коленчатого вала двигателя - данные действительны, но выше нормального рабочего диапазона - самый тяжелый уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 234 PID(P): P190 SPN: ФМИ: 0 лампочка: Флешинг SRT: 00-628 | Сигнал скорости двигателя указывает на скорость двигателя выше предела защиты двигателя. | Двигатель отключится. |

![[19802309.png]]

Цепь датчика частоты вращения двигателя

### Описание цепи

Датчик скорости двигателя - это датчик скорости с двумя каналами, используемый ECM для мониторинга скорости двигателя. Датчик скорости имеет четыре схемы: Две сигнальные цепи и две обратные цепи. Когда зубы на маховике коленчатого вала проходят мимо датчика скорости, на цепях сигналов датчика скорости генерируется сигнал.

### Расположение компонента

Датчик скорости двигателя расположен в корпусе маховика в задней части двигателя.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

ECM обнаруживает, что скорость двигателя превысила предел калибровки для чрезмерной скорости двигателя.

### Действия системы при активном коде неисправности

- ECM освещает красную лампу STOP ENGINE сразу же после запуска и отказа диагностического устройства.

Для приложений генерации электроэнергии:

- Контроллер генераторной установки отображает неисправность сразу же, когда диагностика работает и выходит из строя.

### Условия сброса кода неисправности

- Выключите замок зажигания. Позвольте ECM полностью выключить питание и включить переключатель зажигания.

- Состояние кода ошибки, отображаемого рекомендованным электронным сервисным инструментом Cummins® или его эквивалентом, будет изменено на INACTIVE сразу после диагностических запусков и проходов.

- ECM выключит красную лампу STOP ENGINE сразу после диагностических прогонов и проходов.

- Команда «Сбросить все ошибки» в рекомендуемой электронной сервисной оснастке Cummins® или эквиваленте может использоваться для устранения активных и неактивных ошибок.

Для приложений генерации электроэнергии:

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки выключит индикатор сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Внешние источники топлива, втягиваемые в давление впускного воздуха.

- Обратное питание (управление) двигателя.

- Укрощение датчиков скорости двигателя.

- Неисправный или поврежденный топливный насос.

- Неисправность или повреждение уплотнений масла турбокомпрессора.

См. Код устранения неполадок t05-234


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 234
>
> ### Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Most Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 234 PID(P): P190 SPN: FMI: 0 Lamp: Flashing SRT: 00-628 | Engine speed signal indicates engine speed above engine protection limit. | Engine will shut down. |
>
> Engine Speed Sensor Circuit
>
> ### Circuit Description
>
> The engine speed sensor is dual channel speed sensor used by the ECM to monitor the engine speed. The speed sensor has four circuits: two signal circuits, and two return circuits. As the teeth on the crankshaft flywheel move past the speed sensor, a signal is generated on the speed sensor signal circuits.
>
> ### Component Location
>
> The engine speed sensor is located in the flywheel housing at the rear of the engine.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The ECM detects the engine speed has exceeded the calibration limit for excessive engine speed.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the red STOP ENGINE lamp immediately when the diagnostic runs and fails.
>
> For Power Generation Applications:
>
> - The generator set controller displays the fault immediately when the diagnostics runs and fails.
>
> ### Conditions For Clearing The Fault Code
>
> - Turn the keyswitch OFF. Allow the ECM to completely power down and turn the keyswitch ON.
>
> - The fault code status displayed by the recommended Cummins® electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.
>
> - The ECM will turn off the red STOP ENGINE lamp immediately after the diagnostic runs and passes.
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
> - External fuel sources drawn into the intake air pressure.
>
> - Reverse powering (motering) of the engine.
>
> - Tampering of the engine speed sensors.
>
> - Malfunctioning or damaged fuel pump.
>
> - Malfunctioning or damaged turbocharger oil seals.
>
> Refer to Troubleshooting Fault Code t05-234
