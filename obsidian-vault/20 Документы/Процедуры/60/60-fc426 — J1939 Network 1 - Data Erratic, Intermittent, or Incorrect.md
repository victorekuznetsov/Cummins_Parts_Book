---
aliases:
  - "Сеть J1939 №1 — данные нестабильны или неверны"
type: "Процедура"
doc: "60-fc426"
title_en: "J1939 Network #1 - Data Erratic, Intermittent, or Incorrect"
title_ru: "Сеть J1939 №1 — данные нестабильны или неверны"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc426.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc426.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# J1939 Network #1 - Data Erratic, Intermittent, or Incorrect
**Сеть J1939 №1 — данные нестабильны или неверны**

> [!abstract] Процедура · `60-fc426`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc426.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc426.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 426

### J1939 Сеть #1 - данные нестабильные, прерывистые или неправильные

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 426 PID(P): S231 SPN: 639 FMI: 2/2 лампы: Нет, не srt: | Связь между модулем управления двигателем (ECM) и другим устройством на шине данных J1939 CAN была потеряна. | Ни одного на выступление. |

![[19a00871.png]]

J1939 CAN Data Bus Circuit (недоступная ссылка)

### Описание цепи

ECM определила, что другое устройство в сети шины данных J1939 CAN перестало обмениваться данными в сети. Устройства в сети шины данных J1939 CAN включают: ECMs и модуль интерфейса генератора. Упряжка проводов для сети шины данных J1939 CAN имеет экранированную витую пару проводов, которые соединяют каждое из сетевых устройств и резистор завершения.

### Расположение компонента

Расположение шины передачи данных J1939 CAN может варьироваться в зависимости от OEM.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда контроллер генераторного набора активен.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил состояние открытого или короткого замыкания в электропроводке шины данных J1939 CAN.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки отображает неисправность сразу же, когда диагностика работает и выходит из строя.

- Мультиплексное устройство будет работать **не**.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки отключит код неисправности сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправность или повреждение жгута проводов шины данных J1939 CAN.

- Неисправность или повреждение OEM-проводов.

- Сбой связи между устройствами J1939

См. Код 426 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 426
>
> ### J1939 Network \#1 - Data Erratic, Intermittent, or Incorrect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 426 PID(P): S231 SPN: 639 FMI: 2/2 Lamp: None SRT: | Communication between the engine control module (ECM) and another device on the J1939 datalink has been lost. | None on performance. |
>
> J1939 Datalink Circuit
>
> ### Circuit Description
>
> The ECM identified another device on the J1939 datalink network has stopped communicating on the network. The devices on the J1939 datalink network include: ECMs', and the Generator Interface Module. The harness for the J1939 datalink network has a shielded twisted pair of wires that connect each of the network devices and termination resistor.
>
> ### Component Location
>
> The location of the J1939 datalink wiring may vary depending on OEM.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected an open or short circuit condition in the J1939 datalink wiring harness.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays the fault immediately when the diagnostics runs and fails.
>
> - The multiplexed device will **not** operate.
>
> ### Conditions For Clearing The Fault Code
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
> - Malfunctioning or damaged J1939 datalink wiring harness.
>
> - Malfunctioning or damaged OEM wiring harness.
>
> - Communication failure between J1939 devices
>
> Refer to Troubleshooting Fault Code 426.
