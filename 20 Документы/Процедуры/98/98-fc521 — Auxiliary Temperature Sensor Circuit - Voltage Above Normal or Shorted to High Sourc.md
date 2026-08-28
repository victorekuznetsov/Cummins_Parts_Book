---
type: "Процедура"
doc: "98-fc521"
title_en: "Auxiliary Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc521.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc521.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Auxiliary Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `98-fc521`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc521.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc521.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 521

### Вспомогательная схема датчика температуры - напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 521 P(P): P177 SPN: ФМИ: 3 лампы: На SRT: 00-645 | Высокое напряжение сигнала, обнаруженное на вспомогательной схеме датчика температуры. | Ни одного на выступление. |

![[19802303.png]]

Вспомогательная схема датчика температуры

### Описание цепи

Вспомогательный датчик температуры представляет собой датчик переменного резистора, используемый ECM для мониторинга вспомогательной температуры. Вспомогательный датчик температуры имеет две схемы: сигнал и обратные цепи. Напряжение сигнала указывает на вспомогательную температуру.

### Расположение компонента

Расположение вспомогательного датчика температуры может варьироваться и зависит от OEM.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что напряжение сигнала вспомогательного датчика температуры было вне диапазона.

### Действия системы при активном коде неисправности

- ECM освещает янтарный свет CHECK ENGINE, когда диагностика проходит и не удается.

- На CENTRYTM отсутствует система защиты двигателя от вспомогательных температур.

Для приложений генерации электроэнергии:

- Контроллер генераторной установки отображает неисправность сразу же, когда диагностика работает и выходит из строя.

- На CENTRYTM отсутствует система защиты двигателя от вспомогательных температур.

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

- Поврежденная проводка OEM.

- Поврежденные или рыхлые разъемы.

- Неисправный вспомогательный датчик температуры.

См. Код устранения неполадок t05-521


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 521
>
> ### Auxiliary Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 521 PID(P): P177 SPN: FMI: 3 Lamp: On SRT: 00-645 | High signal voltage detected at the auxiliary temperature sensor circuit. | None on performance. |
>
> Auxiliary Temperature Sensor Circuit
>
> ### Circuit Description
>
> The auxiliary temperature sensor is a variable resistor sensor used by the ECM to monitor the auxiliary temperature. The auxiliary temperature sensor has two circuits: signal, and return circuits. The signal voltage indicates the auxiliary temperature.
>
> ### Component Location
>
> The location of the auxiliary temperature sensor may vary and is OEM dependent.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected that the auxiliary temperature sensor signal voltage was out of range high.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE light when the diagnostic runs and fails.
>
> - There is no engine protection system for auxiliary temperature on CENTRY™.
>
> For Power Generation Applications:
>
> - The generator set controller displays the fault immediately when the diagnostics runs and fails.
>
> - There is no engine protection system for auxiliary temperature on CENTRY™.
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
> - Damaged OEM wiring harness.
>
> - Damaged or loose connectors.
>
> - Malfunctioning auxiliary temperature sensor.
>
> Refer to Troubleshooting Fault Code t05-521
