---
type: "Процедура"
doc: "98-fc443fa"
title_en: "Accelerator Pedal or Lever Position Sensor Supply Voltage Circuit - Voltage Below Normal or Shorted to Low Source"
modified: "2021-09-15"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc443fa.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc443fa.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Accelerator Pedal or Lever Position Sensor Supply Voltage Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `98-fc443fa`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc443fa.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc443fa.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 443-фа

### Педаль акселератора или датчик положения рычага Снаряжение цепи питания - напряжение ниже нормального или короткого до низкого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 443-фа PID(P): S254 SPN: ФМИ: 4 лампы: Флешинг SRT: 00-637 | Низкое напряжение, обнаруженное на датчике питания для цепи сигнала частотного дроссельного заслонка. | Возможно снижение производительности двигателя. |

![[19802610.png]]

Частотная дроссельная сигнальная схема

### Описание цепи

Датчик положения дроссельной заслонки представляет собой датчик переменной частоты, используемый ECM для мониторинга команды дроссельной заслонки. Этот датчик имеет три схемы: 5-вольтная цепь подачи, возврата и сигнала. Напряжение цепи сигнала указывает положение датчика положения дроссельной заслонки.

### Расположение компонента

Расположение генератора дроссельной заслонки переменной частоты варьируется в зависимости от каждого OEM.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что подачу датчика на частотный сигнал дроссельной заслонки было за пределами диапазона.

### Действия системы при активном коде неисправности

- ECM освещает янтарный свет CHECK ENGINE, когда диагностика проходит и не удается.

Для приложений генерации электроэнергии:

- Контроллер генераторной установки отображает неисправность сразу же, когда диагностика работает и выходит из строя.

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

- Неисправность или повреждение дроссельной заслонки переменной частоты.

- Неисправный или повреждённый жгут проводов двигателя.

- Поврежденные или рыхлые разъемы.

Устранение неполадок код t05-443


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 443-fa
>
> ### Accelerator Pedal or Lever Position Sensor Supply Voltage Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 443-fa PID(P): S254 SPN: FMI: 4 Lamp: Flashing SRT: 00-637 | Low voltage detected at the sensor supply for the frequency throttle signal circuit. | Possible reduced engine performance. |
>
> Frequency Throttle Signal Circuit
>
> ### Circuit Description
>
> The throttle position sensor is a variable frequency sensor used by the ECM to monitor the throttle command. This sensor has three circuits: 5 volt supply, return and signal circuits. The signal circuit voltage indicates the position of the throttle position sensor.
>
> ### Component Location
>
> The variable frequency throttle assembly generator location varies with each OEM.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the sensor supply to the frequency throttle signal was out of range low.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE light when the diagnostic runs and fails.
>
> For Power Generation Applications:
>
> - The generator set controller displays the fault immediately when the diagnostics runs and fails.
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
> - Malfunctioning or damaged variable frequency throttle assembly.
>
> - Malfunctioning or damaged engine wiring harness.
>
> - Damaged or loose connectors.
>
> Refer to Troubleshooting Fault Code t05-443
