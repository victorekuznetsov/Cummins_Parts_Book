---
type: "Процедура"
doc: "98-fc525"
title_en: "Engine Control Module Not Calibrated - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc525.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc525.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Control Module Not Calibrated - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `98-fc525`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc525.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc525.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 525

### Модуль управления двигателем не калиброван - напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 525 P(P): S254 SPN: ФМИ: 3 лампы: На SRT: 00-649 | Неправильная калибровка ECM или отказ ECM. | Двигатель может работать грубо, может перестать работать, может **не **начаться, или может быть трудно начать. |

![[19802469.png]]

Модуль управления двигателем (ECM)

### Описание цепи

ECM имеет внутреннюю диагностику, которая постоянно работает и проверяет внутреннюю память.

### Расположение компонента

ECM прикреплен к топливному насосу на левой стороне двигателя.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил ошибку памяти в ECM.

### Действия системы при активном коде неисправности

- ECM освещает красную лампу STOP ENGINE сразу после диагностических прогонов и выходит из строя.

- Двигатель может **не** завестись.

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

- Неисправность программного обеспечения ECM или ошибка калибровки.

- Внутренний сбой ECM.

См. Код устранения неполадок t05-525


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 525
>
> ### Engine Control Module Not Calibrated - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 525 PID(P): S254 SPN: FMI: 3 Lamp: On SRT: 00-649 | Incorrect ECM calibration, or ECM failure. | Engine may run rough, may stop running, may **not** start, or may be difficult to start. |
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
> The Engine Control Module (ECM) has detected a memory error in the ECM.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the red STOP ENGINE lamp immediately after the diagnostic runs and fails.
>
> - The engine may **not** start.
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
> - A malfunction of the ECM software or calibration error.
>
> - Internal ECM failure.
>
> Refer to Troubleshooting Fault Code t05-525
