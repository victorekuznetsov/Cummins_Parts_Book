---
aliases:
  - "Сеть SAE J1939 №2 — недопустимая частота обновления"
type: "Процедура"
doc: "60-fc2727"
title_en: "SAE J1939 Data Link 2 Engine Network - Abnormal Update Rate"
title_ru: "Сеть SAE J1939 №2 — недопустимая частота обновления"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc2727.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc2727.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# SAE J1939 Data Link 2 Engine Network - Abnormal Update Rate
**Сеть SAE J1939 №2 — недопустимая частота обновления**

> [!abstract] Процедура · `60-fc2727`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc2727.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc2727.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2727

### Сеть SAE J1939 №2 — недопустимая частота обновления

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2727 PID(P): S206 SPN: 1231 FMI: 9/9 лампа: Обслуживание SRT: | Связь между модулем управления двигателем (ECM) и другим устройством на шине данных J1939 CAN была потеряна. | Возможно снижение производительности двигателя. |

![[19a00854.png]]

J1939 CAN шина 2 цепи сети двигателя

### Описание цепи

ECM определила, что другое устройство в сети шины данных J1939 CAN перестало обмениваться данными в сети. Устройства в сети шины данных J1939 CAN включают: ECMs и модуль интерфейса генератора. Упряжка проводов для сети шины данных J1939 CAN имеет экранированную витую пару проводов, которые соединяют каждое из сетевых устройств и резистор завершения.

### Расположение компонента

Модули управления двигателем (ECM) расположены на пластине, которая находится над корпусом маховика.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда контроллер генераторного набора активен.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) не получал сообщения от мультиплексированного устройства.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

- Мультиплексное устройство будет работать **не**.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки отключит код неисправности сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении электронного инструментария или эквивалента Cummins®. При устранении неисправности кода используйте адрес источника, отображаемый в инструменте электронного обслуживания Cummins® или эквивалент, чтобы определить, какая ECM и схема затронута.

Каждое интеллектуальное устройство в сети шины данных J1939 CAN нуждается в питании и наземном питании для включения, после включения интеллектуального устройства оно может затем обмениваться данными в сети шины данных J1939 CAN.

Возможные причины этого кода неисправности:

- Неисправность или повреждение жгута проводов шины данных J1939 CAN.

См. Код 2727 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2727
>
> ### SAE J1939 Data Link 2 Engine Network - Abnormal Update Rate
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2727 PID(P): S206 SPN: 1231 FMI: 9/9 Lamp: Maintenance SRT: | Communication between the engine control module (ECM) and another device on the J1939 datalink has been lost. | Possible reduced engine performance. |
>
> J1939 Data Link 2 Engine Network Circuit
>
> ### Circuit Description
>
> The ECM identified another device on the J1939 datalink network has stopped communicating on the network. The devices on the J1939 datalink network include: ECMs', and the Generator Interface Module. The harness for the J1939 datalink network has a shielded twisted pair of wires that connect each of the network devices and termination resistor.
>
> ### Component Location
>
> The Engine Control Modules (ECM) are located on a plate that is above the flywheel housing.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) did **not** receive a message from a multiplexed device.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
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
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.
>
> Each smart device on the J1939 datalink network need power and ground to turn on, after the smart device turns on, it can then communicate on the J1939 datalink network.
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged J1939 datalink wiring harness.
>
> Refer to Troubleshooting Fault Code 2727.
