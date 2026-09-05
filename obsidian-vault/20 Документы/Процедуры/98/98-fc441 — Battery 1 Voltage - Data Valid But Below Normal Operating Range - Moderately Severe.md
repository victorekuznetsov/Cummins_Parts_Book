---
type: "Процедура"
doc: "98-fc441"
title_en: "Battery 1 Voltage - Data Valid But Below Normal Operating Range - Moderately Severe Level"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc441.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc441.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Battery 1 Voltage - Data Valid But Below Normal Operating Range - Moderately Severe Level

> [!abstract] Процедура · `98-fc441`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc441.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc441.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 441

### Напряжение батареи 1 - данные действительны, но ниже нормального диапазона работы - умеренно тяжелый уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 441 PID(P): S168 SPN: ФМИ: 4 лампы: На SRT: 00-635 | Напряжение питания ECM ниже минимального уровня напряжения системы. | Двигатель может работать грубо, может перестать работать, может **не **начаться, или может быть трудно начать. |

![[19802314.png]]

Переключенная схема поставки аккумуляторов

### Описание цепи

Модуль управления двигателем (ECM) получает постоянное напряжение от батарей через непереключенные провода батареи, которые подключены непосредственно к положительному (+) посту батареи. ECM принимает вводимую аккумуляторную батарею через провод переключателя зажигания, когда переключатель зажигания включен.

### Расположение компонента

Расположение батареи будет варьироваться в зависимости от производителя оригинального оборудования (OEM).

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил низкое напряжение питания батареи.

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

- Неправильная настройка напряжения батареи.

- Поврежденные предохранители или реле.

- Поврежденные или рыхлые разъемы.

- Неисправность или поврежденный генератор.

- Слабая или поврежденная батарея.

Устранение неполадок код t05-441


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 441
>
> ### Battery 1 Voltage - Data Valid But Below Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 441 PID(P): S168 SPN: FMI: 4 Lamp: On SRT: 00-635 | ECM supply voltage is below the minimum system voltage level. | Engine may run rough, may stop running, may **not** start, or may be difficult to start. |
>
> Switched Battery Supply Circuit
>
> ### Circuit Description
>
> The engine control module (ECM) receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the positive (+) battery post. The ECM receives switched battery input through the keyswitch wire when the keyswitch is turned ON.
>
> ### Component Location
>
> The location of the battery will vary with the original equipment manufacturer (OEM).
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected low battery supply voltage.
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
> - Incorrect battery voltage setting.
>
> - Damaged fuses or relays.
>
> - Damaged or loose connectors.
>
> - Malfunctioning or damaged alternator.
>
> - A weak or damaged battery.
>
> Refer to Troubleshooting Fault Code t05-441
