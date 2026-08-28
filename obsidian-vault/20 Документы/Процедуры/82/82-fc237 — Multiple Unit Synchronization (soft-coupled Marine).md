---
aliases:
  - "Синхронизация нескольких агрегатов (судовое исполнение)"
type: "Процедура"
doc: "82-fc237"
title_en: "Multiple Unit Synchronization (soft-coupled Marine)"
title_ru: "Синхронизация нескольких агрегатов (судовое исполнение)"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc237.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc237.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Multiple Unit Synchronization (soft-coupled Marine)
**Синхронизация нескольких агрегатов (судовое исполнение)**

> [!abstract] Процедура · `82-fc237`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc237.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc237.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 237

### Синхронизация нескольких агрегатов (судовое исполнение)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 237 P(P): S030 SPN: 644 FMI: 2/2 лампы: Желтая СТО: 00-395 | Рабочий цикл входного сигнала дроссельной заслонки на первичный или вторичный двигатель для многократной синхронизации агрегатов составляет менее 3 процентов или более 97 процентов. | Все двигатели (первичные и вторичные) выключаются с увеличением времени после оповещения при жесткой сцепке. Только вторичные двигатели отключаются с увеличением времени после оповещения, если они мягкие. |

![[19802765.png]]

Многоцелевой синхронизационный контур, мягкий морской

### Описание цепи

Основной двигатель передает сообщение управления скоростью двигателя через шину данных SAE J1939 CAN всем вторичным двигателям. Провода джампера используются для настройки двигателя в качестве основного двигателя или в качестве вторичного двигателя. Только один двигатель может быть выполнен в качестве основного двигателя. До 5 двигателей могут быть сконфигурированы как вторичные двигатели на той же шине данных SAE J1939 CAN.

### Расположение компонента

Связи между шиной данных и прыжком SAE J1939 CAN являются частью проводной сети OEM. Расположение проводных соединений прыгуна варьируется в зависимости от OEM. См. руководство OEM по местоположению компонентов.

### Практические замечания

Конфигурация 3-контактных входов в электронный модуль управления (ECM) на электропроводке OEM определяет, является ли двигатель первичным или вторичным двигателем. Смотрите предоставленную матрицу. Чтобы активировать штифт, штифт **должен быть заземлен. Чтобы деактивировать штифт, штифт** должен быть открытым контуром.

| Контакт 3 | Контакт 2 | Контакт 1 | Первичный/вторичный |
|---|---|---|---|
| ИНАКТИВНЫЙ | ИНАКТИВНЫЙ | ИНАКТИВНЫЙ | По умолчанию первичный |
| ИНАКТИВНЫЙ | ИНАКТИВНЫЙ | активный | первичный |
| ИНАКТИВНЫЙ | активный | ИНАКТИВНЫЙ | Вторичный 0 |
| ИНАКТИВНЫЙ | активный | активный | Вторичный 1 |
| активный | ИНАКТИВНЫЙ | ИНАКТИВНЫЙ | Вторичный 2 |
| активный | ИНАКТИВНЫЙ | активный | Вторичный 3 |
| активный | активный | ИНАКТИВНЫЙ | Вторичный 4 |
| активный | активный | активный | По умолчанию первичный |

Убедитесь, что переключатель зажигания включен для всех двигателей синхронизации с несколькими блоками. Убедитесь, что никакие дефекты дроссельной заслонки не активны.

Убедитесь, что шина данных SAE J1939 CAN активна и правильно взаимодействует с инструментами электронного обслуживания INSITETM на всех двигателях. Если какой-либо ECM не будет обмениваться данными через шину данных SAE J1939 CAN.[[00-022-999 — Service Tools and Hardware - Overview|См. процедуру 022-999 в разделе F.]]

См. Код устранения неполадок t05-237


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 237
>
> ### Multiple Unit Synchronization (soft-coupled Marine)
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 237 PID(P): S030 SPN: 644 FMI: 2/2 Lamp: Yellow SRT: 00-395 | Duty cycle of the throttle input signal to the primary or secondary engine for multiple unit synchronization is less than 3 percent or more than 97 percent. | All engines (primary and secondary) are shut down with increasing time after alert if hard-coupled. **Only** secondary engines are shut down with increasing time after alert if soft-coupled. |
>
> Multiple Unit Synchronization Circuit, Soft-Coupled Marine
>
> ### Circuit Description
>
> The primary engine broadcasts the engine speed control message over the SAE J1939 datalink to all secondary engines. Jumper wires are used to configure an engine as a primary engine or as a secondary engine. **Only** one engine can be configured as the primary engine. Up to 5 engines can be configured as secondary engines on the same SAE J1939 datalink.
>
> ### Component Location
>
> The SAE J1939 datalink and jumper wire connections are part of the OEM harness. Location of the jumper wire connections vary by the OEM. Refer to the OEM manual for component location.
>
> ### Shoptalk
>
> The configuration of the 3-pin inputs to the electronic control module (ECM) on the OEM harness determines if an engine is a primary or secondary engine. See the matrix provided. To activate a pin, the pin **must** be grounded. To deactivate a pin, the pin **must** be an open circuit.
>
> | Pin 3 | Pin 2 | Pin 1 | Primary/Secondary |
> |---|---|---|---|
> | INACTIVE | INACTIVE | INACTIVE | Default to Primary |
> | INACTIVE | INACTIVE | ACTIVE | Primary |
> | INACTIVE | ACTIVE | INACTIVE | Secondary 0 |
> | INACTIVE | ACTIVE | ACTIVE | Secondary 1 |
> | ACTIVE | INACTIVE | INACTIVE | Secondary 2 |
> | ACTIVE | INACTIVE | ACTIVE | Secondary 3 |
> | ACTIVE | ACTIVE | INACTIVE | Secondary 4 |
> | ACTIVE | ACTIVE | ACTIVE | Default to Primary |
>
> Verify that the keyswitch is on for all multiple unit synchronization engines. Verify that no throttle faults are active.
>
> Verify that the SAE J1939 datalink is active and communicates correctly with INSITE™ electronic service tool on all engines. If any ECM will not communicate over the SAE J1939 datalink. [[00-022-999 — Service Tools and Hardware - Overview|Refer to Procedure 022-999 in Section F.]]
>
> Refer to Troubleshooting Fault Code t05-237
