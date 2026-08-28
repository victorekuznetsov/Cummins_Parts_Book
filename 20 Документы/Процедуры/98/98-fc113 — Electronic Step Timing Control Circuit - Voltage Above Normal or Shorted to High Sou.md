---
type: "Процедура"
doc: "98-fc113"
title_en: "Electronic Step Timing Control Circuit - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc113.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc113.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Electronic Step Timing Control Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `98-fc113`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc113.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc113.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 113

### Электронная схема управления временем шага - напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 113 P(P): S20 SPN: ФМИ: 3 лампы: На SRT: 00-619 | Высокое напряжение, обнаруженное в электронной схеме управления временем шага. | Возможно снижение производительности двигателя. |

![[19802315.png]]

Электронный контроль времени шага (STC)

### Описание цепи

Электронный привод управления синхронизацией ступени управляет клапаном управления синхронизацией ступени на топливном насосе. Электронный привод управления временем шага имеет одну цепь; драйвер управления временем шага / драйвер вывода крутящего момента. Модуль управления двигателем (ECM) регулирует время работы двигателя от предварительного до нормального с электронным приводом управления временем шага.

### Расположение компонента

Электронный клапан управления временем шага установлен на левой стороне двигателя.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что электронное напряжение управления временем шага было вне диапазона.

### Действия системы при активном коде неисправности

- ECM освещает лампу янтарного CHECK ENGINE сразу же, когда диагностика проходит и выходит из строя.

- Электронный клапан управления временем шага находится в полном синхронном движении.

Для приложений генерации электроэнергии:

- Контроллер генераторной установки отображает неисправность сразу же, когда диагностика работает и выходит из строя.

- Электронный клапан управления временем шага находится в полном синхронном движении.

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

- Неисправность или повреждение электронного привода управления временем шага.

- Разряженные или поврежденные разъемы.

Устранение неполадок код t05-113


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 113
>
> ### Electronic Step Timing Control Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 113 PID(P): S20 SPN: FMI: 3 Lamp: On SRT: 00-619 | High voltage detected at the electronic step timing control circuit. | Possible reduced engine performance. |
>
> Electronic Step Timing Control (STC) Circuit
>
> ### Circuit Description
>
> The electronic step timing control actuator controls the step timing control valve on the fuel pump. The electronic step timing control actuator has a single circuit; step timing control driver/ torque output driver. The Engine Control Module (ECM) adjusts the engine timing from advance to normal with the electronic step timing control actuator.
>
> ### Component Location
>
> The electronic step timing control valve is mounted on the left side of the engine.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the electronic step timing control voltage was out of range high.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.
>
> - The electronic step timing control valve is in full timing advance.
>
> For Power Generation Applications:
>
> - The generator set controller displays the fault immediately when the diagnostics runs and fails.
>
> - The electronic step timing control valve is in full timing advance.
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
> - Malfunctioning or damaged electronic step timing control actuator.
>
> - Loose or damaged connectors.
>
> Refer to Troubleshooting Fault Code t05-113
