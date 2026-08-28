---
type: "Процедура"
doc: "98-fc442"
title_en: "Battery 1 Voltage - Data Valid But Above Normal Operating Range - Moderately Severe Level"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc442.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc442.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Battery 1 Voltage - Data Valid But Above Normal Operating Range - Moderately Severe Level

> [!abstract] Процедура · `98-fc442`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc442.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc442.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 442

### Батарея 1 Вольт - данные действительны, но выше нормального диапазона работы - умеренно тяжелый уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 442 P(P): S168 SPN: ФМИ: 3 лампы: На SRT: 00-636 | Напряжение питания ECM ниже минимального уровня напряжения системы. | Двигатель будет работать только на холостом ходу|

![[19802314.png]]

Переключенная схема поставки аккумуляторов

### Описание цепи

Модуль управления двигателем (ECM) получает постоянное напряжение от батарей через непереключенные провода батареи, которые подключены непосредственно к положительному (+) посту батареи. ECM принимает вводимую аккумуляторную батарею через провод переключателя зажигания, когда переключатель зажигания включен.

### Расположение компонента

Расположение батареи будет варьироваться в зависимости от производителя оригинального оборудования (OEM).

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил высокое напряжение питания батареи.

### Действия системы при активном коде неисправности

- ECM освещает лампу янтарного CHECK ENGINE сразу же, когда диагностика проходит и выходит из строя.

- Двигатель будет только простаивать.

Для приложений генерации электроэнергии:

- Контроллер генераторной установки отображает неисправность сразу же, когда диагностика работает и выходит из строя.

- Двигатель будет только простаивать.

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

- Неисправный генератор, который перегружается.

- Аккумуляторы подключаются последовательно, а не параллельно.

- Неправильная процедура запуска прыжка.

- Слабая или поврежденная батарея.

Устранение неполадок код t05-442


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 442
>
> ### Battery 1 Voltage - Data Valid But Above Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 442 PID(P): S168 SPN: FMI: 3 Lamp: On SRT: 00-636 | ECM supply voltage is below the minimum system voltage level. | Engine will run at idle **only.** |
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
> The Engine Control Module (ECM) detected high battery supply voltage.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.
>
> - Engine will **only** idle.
>
> For Power Generation Applications:
>
> - The generator set controller displays the fault immediately when the diagnostics runs and fails.
>
> - Engine will **only** idle.
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
> - Malfunctioning alternator that is overcharging.
>
> - Batteries connected in series instead of parallel.
>
> - Incorrect jump-starting procedure.
>
> - A weak or damaged battery.
>
> Refer to Troubleshooting Fault Code t05-442
