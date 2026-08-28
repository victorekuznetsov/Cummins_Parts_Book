---
type: "Процедура"
doc: "98-fc131as"
title_en: "Accelerator Pedal or Lever Position Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2021-09-22"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc131as.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc131as.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Accelerator Pedal or Lever Position Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `98-fc131as`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc131as.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc131as.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 131-я как

### Педаль ускорителя или датчик положения рычага 1 - напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 131 как PID(P): P91 SPN: ФМИ: 3 лампы: Флешинг SRT: 00-622 | Высокое напряжение, обнаруженное в цепи сигнала положения дроссельной заслонки. | Возможно снижение производительности двигателя. |

![[19802609.png]]

Сенсорная схема Throttle Position

### Описание цепи

Датчик положения дроссельной заслонки представляет собой переключатель, используемый ECM для мониторинга команды дроссельной заслонки. Этот датчик имеет две схемы: 5 вольт питания и сигнальные цепи. Напряжение цепи сигнала указывает положение датчика положения дроссельной заслонки.

### Расположение компонента

Расположение датчика положения дроссельной заслонки может варьироваться и зависит от OEM.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала положения дроссельной заслонки было вне диапазона высоко.

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

- Неисправный или повреждённый жгут проводов двигателя.

- Неисправность или повреждение OEM-проводов.

- Неисправный или поврежденный датчик положения дроссельной заслонки.

- Поврежденные или рыхлые разъемы.

См. Код устранения неполадок t05-131


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 131-as
>
> ### Accelerator Pedal or Lever Position Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 131-as PID(P): P91 SPN: FMI: 3 Lamp: Flashing SRT: 00-622 | High voltage detected at throttle position signal circuit. | Possible reduced engine performance. |
>
> Throttle Position Sensor Circuit
>
> ### Circuit Description
>
> The throttle position sensor is a switch used by the ECM to monitor the throttle command. This sensor has two circuits: 5 volt supply, and signal circuits. The signal circuit voltage indicates the position of the throttle position sensor.
>
> ### Component Location
>
> Throttle position sensor location may vary and is OEM dependent.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the throttle position signal voltage was out of range high.
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
> - Malfunctioning or damaged engine wiring harness.
>
> - Malfunctioning or damaged OEM wiring harness.
>
> - Malfunctioning or damaged throttle position sensor.
>
> - Damaged or loose connectors.
>
> Refer to Troubleshooting Fault Code t05-131
