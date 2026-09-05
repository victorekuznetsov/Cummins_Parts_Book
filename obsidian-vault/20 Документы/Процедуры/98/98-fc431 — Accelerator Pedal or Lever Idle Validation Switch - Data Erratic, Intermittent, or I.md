---
type: "Процедура"
doc: "98-fc431"
title_en: "Accelerator Pedal or Lever Idle Validation Switch - Data Erratic, Intermittent, or Incorrect"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc431.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc431.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Accelerator Pedal or Lever Idle Validation Switch - Data Erratic, Intermittent, or Incorrect

> [!abstract] Процедура · `98-fc431`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc431.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc431.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 431

### Переключатель проверки педалей или рычагов холостого хода - данные нерегулярные, прерывистые или неправильные

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 431 PID(P): P91 SPN: ФМИ: 2 лампы: На SRT: 00-633 | Напряжение, обнаруживаемое одновременно как на холостых валидационных, так и на выключателях валидации. | Возможно снижение производительности двигателя. |

![[19802311.png]]

Цепь подтверждения холостого хода

### Описание цепи

Сигнал проверки бездействия является функцией безопасности, которая отключает управление дроссельной заслонки, в то время как неправильный сигнал проверки обнаруживается ECM. Регулятор валидации бездействия обеспечивает сигнал валидации на холостом ходу и вне холостого хода для ECM через электропроводку OEM и электропроводку двигателя.

### Расположение компонента

Переключатель проверки бездействия установлен на педали дроссельной заслонки. Расположение педали дроссельной заслонки варьируется в зависимости от каждого OEM.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM), обнаруженный на холостом ходу и сигнал на холостом ходу, был включен или выключен одновременно.

### Действия системы при активном коде неисправности

- ECM освещает лампу янтарного CHECK ENGINE сразу же, когда диагностика проходит и выходит из строя.

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

- Неисправный или повреждённый жгут проводов двигателя.

- Неисправность или повреждение OEM-проводов.

- Неисправный или поврежденный датчик положения дроссельной заслонки.

- Поврежденные или рыхлые разъемы.

Устранение неполадок код t05-431


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 431
>
> ### Accelerator Pedal or Lever Idle Validation Switch - Data Erratic, Intermittent, or Incorrect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 431 PID(P): P91 SPN: FMI: 2 Lamp: On SRT: 00-633 | Voltage detected simultaneously on both idle validation and off-idle validation switches. | Possible reduced engine performance. |
>
> Idle Validation Circuit
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
> - The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.
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
> - Malfunctioning or damaged engine wiring harness.
>
> - Malfunctioning or damaged OEM wiring harness.
>
> - Malfunctioning or damaged throttle position sensor.
>
> - Damaged or loose connectors.
>
> Refer to Troubleshooting Fault Code t05-431
