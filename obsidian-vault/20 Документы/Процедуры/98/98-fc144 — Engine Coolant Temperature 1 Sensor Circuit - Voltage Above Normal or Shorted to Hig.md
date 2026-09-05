---
aliases:
  - "Цепь датчика температуры ОЖ 1 — напряжение выше нормы"
type: "Процедура"
doc: "98-fc144"
title_en: "Engine Coolant Temperature 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика температуры ОЖ 1 — напряжение выше нормы"
modified: "2021-09-10"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc144.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc144.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Coolant Temperature 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика температуры ОЖ 1 — напряжение выше нормы**

> [!abstract] Процедура · `98-fc144`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc144.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc144.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 144

### Цепь датчика температуры ОЖ 1 — напряжение выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 144 PID(P): P110 SPN: ФМИ: 3 лампы: На SRT: 00-626 | Высокое напряжение сигнала, обнаруженное в цепи датчика температуры охлаждающей жидкости двигателя. | Ни одного на выступление. |

![[19802305.png]]

Цепь датчика температуры охлаждающей жидкости

### Описание цепи

Датчик температуры охлаждающей жидкости двигателя представляет собой датчик переменного резистора, используемый ECM для мониторинга температуры охлаждающей жидкости двигателя. Сигналы от датчика температуры охлаждающей жидкости двигателя не используются CENTRYTM ECM для управления двигателем. Датчик температуры охлаждающей жидкости двигателя имеет две схемы: сигнал и обратные цепи. Напряжение сигнала указывает на температуру охлаждающей жидкости.

### Расположение компонента

Расположение датчика температуры охлаждающей жидкости может варьироваться и зависит от OEM.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала датчика температуры охлаждающей жидкости двигателя было вне диапазона.

### Действия системы при активном коде неисправности

- ECM освещает янтарный свет CHECK ENGINE, когда диагностика проходит и не удается.

- Отсутствие защиты двигателя от температуры охлаждающей жидкости двигателя.

Для приложений генерации электроэнергии:

- Контроллер генераторной установки отображает неисправность сразу же, когда диагностика работает и выходит из строя.

- Отсутствие защиты двигателя от температуры охлаждающей жидкости двигателя.

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

- Неисправность или повреждение OEM-проводов.

- Поврежденные или рыхлые разъемы.

- Неисправный или поврежденный датчик температуры охлаждающей жидкости двигателя.

Устранение неполадок код t05-144


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 144
>
> ### Engine Coolant Temperature 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 144 PID(P): P110 SPN: FMI: 3 Lamp: On SRT: 00-626 | High signal voltage detected at the engine coolant temperature sensor circuit. | None on performance. |
>
> Coolant Temperature Sensor Circuit
>
> ### Circuit Description
>
> The engine coolant temperature sensor is a variable resistor sensor used by the ECM to monitor the engine coolant temperature. Signals from the engine coolant temperature sensor are not used by the CENTRY™ ECM to control the engine. The engine coolant temperature sensor has two circuits: signal, and return circuits. The signal voltage indicates the coolant temperature.
>
> ### Component Location
>
> The location of the coolant temperature sensor may vary and is OEM dependent.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected that the engine coolant temperature sensor signal voltage was out of range high.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE light when the diagnostic runs and fails.
>
> - No engine protection for engine coolant temperature.
>
> For Power Generation Applications:
>
> - The generator set controller displays the fault immediately when the diagnostics runs and fails.
>
> - No engine protection for engine coolant temperature.
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
> - Malfunctioning or damaged OEM wiring harness.
>
> - Damaged or loose connectors.
>
> - Malfunctioning or damaged engine coolant temperature sensor.
>
> Refer to Troubleshooting Fault Code t05-144
