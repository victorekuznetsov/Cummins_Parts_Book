---
type: "Процедура"
doc: "98-fc412"
title_en: "SAE J1587/J1922 Datalink - Data Erratic, Intermittent, or Incorrect"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc412.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc412.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# SAE J1587/J1922 Datalink - Data Erratic, Intermittent, or Incorrect

> [!abstract] Процедура · `98-fc412`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc412.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc412.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 412

### SAE J1587/J1922 CAN Data Bus - данные непостоянные, прерывистые или неправильные

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 412 P(P): S250 SPN: ФМИ: 3 лампы: На SRT: 00-632 | Данные, нерегулярные, прерывистые или неправильные, обнаруженные на шине данных J1587/1922 CAN. | Нет. |

![[19802306.png]]

Сеть передачи данных

### Описание цепи

Шина данных J1587/1922 CAN является публичной шиной данных CAN, которая транслирует данные об эксплуатации двигателя, а также коды неисправностей.

### Расположение компонента

Шина данных J1587/1922 CAN расположена в ремне электропроводки двигателя между разъемами шины данных ECM и CAN.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что связь шины данных J1587/1992 CAN является неустойчивой.

### Действия системы при активном коде неисправности

- ECM регистрирует код неисправности сразу же, когда диагностика проходит и выходит из строя.

Для приложений генерации электроэнергии:

- Контроллер генераторной установки отображает неисправность сразу же, когда диагностика работает и выходит из строя.

### Условия сброса кода неисправности

- Выключите замок зажигания. Позвольте ECM полностью выключить питание и включить переключатель зажигания.

- Состояние кода ошибки, отображаемого рекомендованным электронным сервисным инструментом Cummins® или его эквивалентом, будет изменено на INACTIVE сразу после диагностических запусков и проходов.

- Команда «Сбросить все ошибки» в рекомендуемой электронной сервисной оснастке Cummins® или эквиваленте может использоваться для устранения активных и неактивных ошибок.

Для приложений генерации электроэнергии:

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки отключит код неисправности сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

- Неисправность или повреждение OEM-проводов.

- Поврежденные или рыхлые связи.

Устранение неполадок код t05-412


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 412
>
> ### SAE J1587/J1922 Datalink - Data Erratic, Intermittent, or Incorrect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 412 PID(P): S250 SPN: FMI: 3 Lamp: On SRT: 00-632 | Data erratic, intermittent, or incorrect data detected on the J1587/1922 data link. | None. |
>
> Datalink Circuit
>
> ### Circuit Description
>
> The J1587/1922 data link is a public data link that broadcasts engine operating data as well as fault codes.
>
> ### Component Location
>
> The J1587/1922 datalink is located in the engine wiring harness between the ECM and the datalink connectors.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) has detected that the J1587/1992 datalink communication is erratic.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM logs the fault code immediately when the diagnostic runs and fails.
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
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active and inactive faults.
>
> For Power Generation Applications:
>
> - To validate the repair, start the engine and let it run for 1 minute at no load.
>
> - The generator set controller will turn off the fault code immediately after the user presses reset.
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
> - Damaged or loose connections.
>
> Refer to Troubleshooting Fault Code t05-412
