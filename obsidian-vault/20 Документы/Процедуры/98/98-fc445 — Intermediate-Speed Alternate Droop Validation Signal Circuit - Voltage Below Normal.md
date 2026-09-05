---
type: "Процедура"
doc: "98-fc445"
title_en: "Intermediate-Speed/Alternate Droop Validation Signal Circuit - Voltage Below Normal or Shorted to Low Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc445.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc445.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Intermediate-Speed/Alternate Droop Validation Signal Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `98-fc445`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc445.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc445.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 445

### Схема сигнала промежуточной скорости / альтернативной валидации с понижением - напряжение ниже нормального или короткое до низкого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 445 PID (P): S254 SPN: ФМИ: 3 лампы: На SRT: 00-639 | Сигнал проверки промежуточной скорости/альтернативной скорости сбрасывания включен, а сигнал промежуточной скорости или альтернативный сигнал сбрасывания отключен. | Потеря функций промежуточной скорости и альтернативного сбрасывания. |

![[19802310.png]]

Схема сигнала промежуточной скорости/альтернативной валидации

### Описание цепи

Сигнал проверки промежуточной скорости/альтернативной скорости сбрасывания является функцией безопасности, которая позволяет использовать функции промежуточной скорости и альтернативной проверки сбрасывания, в то время как сигнал проверки обнаруживается как высокое напряжение. Переключатель средней скорости и альтернативный переключатель сбрасывания обеспечивают сигналы проверки с промежуточной скоростью, альтернативным сбрасыванием и промежуточным сбрасыванием / альтернативным сбрасыванием для ECM через электропроводку OEM и главный электропроводной жгут проводов двигателя.

### Расположение компонента

Переключатель средней скорости и альтернативное местоположение переключателя сбрасывания могут варьироваться и зависят от OEM.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил низкое напряжение на сигнале проверки промежуточной скорости / альтернативного падения и высокое напряжение, обнаруженное на сигнале промежуточной скорости или высоком напряжении, обнаруженном на альтернативном сигнале падения.

### Действия системы при активном коде неисправности

- ECM освещает янтарный свет CHECK ENGINE, когда диагностика проходит и не удается.

- Отсутствие защиты двигателя от давления масла.

Для приложений генерации электроэнергии:

- Контроллер генераторной установки отображает неисправность сразу же, когда диагностика работает и выходит из строя.

- Отсутствие защиты двигателя от давления масла в двигателе.

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

- Этот код неисправности будет **не** активен, в то время как промежуточные или альтернативные выключатели находятся в положении выключения.

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

- Неисправность или повреждение OEM-проводов.

- Поврежденные или рыхлые разъемы.

- Неисправный или поврежденный альтернативный выключатель крутящего момента.

- Неисправный или поврежденный переключатель средней скорости (отсталый).

- Неисправный или поврежденный альтернативный выключатель слюны.

Устранение неполадок код t05-445


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 445
>
> ### Intermediate-Speed/Alternate Droop Validation Signal Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 445 PID(P): S254 SPN: FMI: 3 Lamp: On SRT: 00-639 | The intermediate-speed/alternate droop validation signal is on and the intermediate-speed signal or alternate droop signal is off. | Loss of intermediate-speed and alternate droop features. |
>
> Intermediate-Speed/Alternate Droop Validation Signal Circuit
>
> ### Circuit Description
>
> The intermediate-speed/alternate droop validation signal is a safety feature that enables the intermediate-speed and alternate droop features while the validation signal is detected as a high voltage. The intermediate-speed switch and alternate droop switch provide the intermediate-speed, alternate droop, and intermediate-speed/alternate droop validation signals to the ECM through the OEM harness and the main engine harness.
>
> ### Component Location
>
> The intermediate-speed switch and the alternate droop switch location may vary and is OEM dependent.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected low voltage at the intermediate-speed/alternate droop validation signal, and high voltage detected at the intermediate-speed signal or high voltage detected at the alternate droop signal.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE light when the diagnostic runs and fails.
>
> - No engine protection for engine oil pressure.
>
> For Power Generation Applications:
>
> - The generator set controller displays the fault immediately when the diagnostics runs and fails.
>
> - No engine protection for engine engine oil pressure.
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
> - This fault code will **not** be active while the intermediate-speed or alternate droop switches are in the OFF position.
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged engine wiring harness.
>
> - Malfunctioning or damaged OEM wiring harness.
>
> - Damaged or loose connectors.
>
> - Malfunctioning or damaged alternate torque idle switch.
>
> - Malfunctioning or damaged intermediate-speed switch (retard).
>
> - Malfunctioning or damaged alternate droop switch.
>
> Refer to Troubleshooting Fault Code t05-445
