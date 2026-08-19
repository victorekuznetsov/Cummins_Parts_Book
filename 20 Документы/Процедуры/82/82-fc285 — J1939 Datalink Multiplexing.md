---
aliases:
  - "Мультиплексирование шины J1939"
type: "Процедура"
doc: "82-fc285"
title_en: "J1939 Datalink Multiplexing"
title_ru: "Мультиплексирование шины J1939"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc285.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc285.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# J1939 Datalink Multiplexing
**Мультиплексирование шины J1939**

> [!abstract] Процедура · `82-fc285`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc285.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc285.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 285

### Мультиплексирование шины J1939

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 285 PID(P): S231 SPN: 639 FMI: 9/9 лампа: Желтая СТО: | ECM ожидала информацию от мультиплексного устройства, но не получила ее достаточно быстро или вообще не получила. | По крайней мере, одно мультиплексное устройство будет работать ** не**. |

![[19c00340.png]]

J1939 CAN шина данных Multiplexing Circuit

### Описание цепи

Такие входные данные, как педали дроссельной заслонки, переключатели и датчики, могут быть переданы в ECM через шину данных J1939 CAN. Сообщения, отправленные от электронных блоков управления транспортным средством (VECU), принимаются ECM и используются для управления двигателем. И ECM, и VECU должны быть правильно настроены так, чтобы информация каждого устройства передавалась VECU и принималась ECM.

### Расположение компонента

ECM расположен на впускной стороне двигателя, рядом с передней. J1939 CAN шина передачи данных и VECU(ы) варьируются в зависимости от опций OEM.

### Практические замечания

Эта ошибка возникает, когда ECM настроен на получение информации о мультиплексном устройстве от VECU по шине данных J1939 CAN и не получает сообщение с этой информацией. Эта ошибка может быть вызвана, если ECM не получает информацию достаточно быстро, чтобы правильно управлять двигателем. Это состояние может быть вызвано следующим:

- Шина данных J1939 CAN имеет электрическую проблему

- Отсутствие заглушек для блокировки шины данных J1939 CAN

- ECM **not** настраивается для получения информации

- Мультиплексное устройство, которое действительно является **не** мультиплексированным

- VECU ** не** правильно настроен для передачи информации на одном из своих мультиплексированных устройств.

См. Код устранения неполадок t05-285


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 285
>
> ### J1939 Datalink Multiplexing
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 285 PID(P): S231 SPN: 639 FMI: 9/9 Lamp: Yellow SRT: | The ECM expected information from a multiplexed device but did **not** receive it soon enough, or did **not** receive it at all. | At least one multiplexed device will **not** operate properly. |
>
> J1939 Datalink Multiplexing Circuit
>
> ### Circuit Description
>
> Inputs such as throttle pedals, switches, and sensors can be communicated to the ECM over the J1939 datalink. Messages sent from the vehicle electronic control units (VECU) are received by the ECM and used for controlling the engine. Both the ECM and VECU **must** be properly configured so that each device's information is transmitted by the VECU and received by the ECM.
>
> ### Component Location
>
> The ECM is located on the intake side of the engine, near the front. The J1939 datalink wiring and VECU(s) vary by OEM options.
>
> ### Shoptalk
>
> This fault occurs when the ECM is set up to receive information about a multiplexed device from a VECU over the J1939 datalink and does **not** receive a message with that information. This fault can also be caused if the ECM does **not** get the information fast enough to control the engine properly. This condition can be caused by the following:
>
> - The J1939 datalink having an electrical problem
>
> - A lack of terminating plugs on the J1939 datalink backbone
>
> - The ECM **not** being set up to receive information
>
> - A multiplexed device that truly is **not** multiplexed
>
> - A VECU **not** being correctly set up to transmit information on one of its multiplexed devices.
>
> Refer to Troubleshooting Fault Code t05-285
