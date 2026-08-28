---
aliases:
  - "Критический внутренний отказ ЭБУ — неисправное устройство"
type: "Процедура"
doc: "98-fc111"
title_en: "Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component"
title_ru: "Критический внутренний отказ ЭБУ — неисправное устройство"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component
**Критический внутренний отказ ЭБУ — неисправное устройство**

> [!abstract] Процедура · `98-fc111`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc111.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 111

### Критический внутренний отказ ЭБУ — неисправное устройство

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 111 PID(P): S254 SPN: ФМИ: 12 ламп: Флешинг SRT: 00-618 | Ошибка, внутренняя для модуля управления двигателем (ECM), связанная с неисправностями оборудования памяти или внутренними цепями питания напряжения ECM. | Двигатель может **не** завестись. Двигатель может отключиться. Возможно снижение производительности двигателя. |

![[19802469.png]]

Модуль управления двигателем (ECM)

### Описание цепи

ECM имеет внутреннюю диагностику, которая постоянно работает и проверяет внутреннюю память.

### Расположение компонента

ECM прикреплен к топливному насосу на левой стороне двигателя.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил ошибку показаний или записи внутри ECM.

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

- Внутренний сбой ECM.

Устранение неполадок код t05-111


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 111
>
> ### Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 111 PID(P): S254 SPN: FMI: 12 Lamp: Flashing SRT: 00-618 | Error internal to the engine control module (ECM) related to memory hardware malfunctions or internal ECM voltage supply circuits. | Engine may **not** start. Engine may shut down. Possible reduced engine performance. |
>
> Engine Control Module (ECM)
>
> ### Circuit Description
>
> The ECM has internal diagnostics that continuously run and check the internal memory.
>
> ### Component Location
>
> The ECM is bolted to the fuel pump on the left side of the engine.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected a read or write error internal to the ECM.
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
> - Internal ECM failure.
>
> Refer to Troubleshooting Fault Code t05-111
