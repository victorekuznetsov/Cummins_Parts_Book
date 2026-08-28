---
type: "Процедура"
doc: "98-fc432nctap"
title_en: "Accelerator Pedal or Lever Idle Validation Switch Circuit - Out of Calibration"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc432nctap.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc432nctap.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Accelerator Pedal or Lever Idle Validation Switch Circuit - Out of Calibration

> [!abstract] Процедура · `98-fc432nctap`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc432nctap.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc432nctap.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 432-nctap

### Схема переключения валидации на ускорителе Pedal или Lever Idle - Out of Calibration

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 432-nctap PID(P): P91 SPN: ФМИ: 13 ламп: Флешинг SRT: 00-634 | Напряжение, обнаруживаемое одновременно как на холостых валидационных, так и на выключателях валидации. | Возможно снижение производительности двигателя. |

![[19802318.png]]

Датчик положения ускорителя (Non-CELECTTM Type Accelerator Pedal)

### Описание цепи

Сигнал проверки бездействия является функцией безопасности, которая отключает управление дроссельной заслонки, в то время как неправильный сигнал проверки обнаруживается ECM. Регулятор валидации бездействия обеспечивает сигнал валидации на холостом ходу и вне холостого хода для ECM через электропроводку OEM и электропроводку двигателя.

### Расположение компонента

Переключатель проверки бездействия установлен на педали дроссельной заслонки. Расположение педали дроссельной заслонки варьируется в зависимости от каждого OEM.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM), обнаруженный на холостом ходу и сигнал на холостом ходу, был включен или выключен одновременно.

### Действия системы при активном коде неисправности

- ECM освещает красную лампу STOP ENGINE сразу после диагностических прогонов и выходит из строя.

- Двигатель может отключиться.

- Двигатель будет работать на низкой, высокой или средней скорости.

Для приложений генерации электроэнергии:

- Контроллер генераторной установки отображает неисправность сразу же, когда диагностика работает и выходит из строя.

- Двигатель может отключиться.

- Двигатель будет работать на низкой, высокой или средней скорости.

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

Устранение неполадок код t05-432


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 432-nctap
>
> ### Accelerator Pedal or Lever Idle Validation Switch Circuit - Out of Calibration
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 432-nctap PID(P): P91 SPN: FMI: 13 Lamp: Flashing SRT: 00-634 | Voltage detected simultaneously on both idle validation and off-idle validation switches. | Possible reduced engine performance. |
>
> Accelerator Position Sensor - (Non-CELECT™ Type Accelerator Pedal)
>
> ### Circuit Description
>
> The idle validation signal is a safety feature that disables throttle control while an improper validation signal is detected by the ECM. The idle validation switch provides an on-idle and off-idle validation signal to the ECM through the OEM wiring harness and engine wiring harness.
>
> ### Component Location
>
> The idle validation switch is mounted on the throttle pedal. The throttle pedal location varies with each OEM.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected on-idle signal and off-idle signal were both on or both off at the same time.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the red STOP ENGINE lamp immediately after the diagnostic runs and fails.
>
> - The engine may shut down.
>
> - The engine will run at low idle, high idle, or intermediate speed.
>
> For Power Generation Applications:
>
> - The generator set controller displays the fault immediately when the diagnostics runs and fails.
>
> - The engine may shut down.
>
> - The engine will run at low idle, high idle, or intermediate speed.
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
> Refer to Troubleshooting Fault Code t05-432
