---
aliases:
  - "Цепь драйвера реле блокировки втягивающего реле"
type: "Процедура"
doc: "82-fc474"
title_en: "Starter Solenoid Lockout Relay Driver Circuit"
title_ru: "Цепь драйвера реле блокировки втягивающего реле"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc474.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc474.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Starter Solenoid Lockout Relay Driver Circuit
**Цепь драйвера реле блокировки втягивающего реле**

> [!abstract] Процедура · `82-fc474`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc474.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc474.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 474

### Цепь драйвера реле блокировки втягивающего реле

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 474 PID(P): S237 SPN: 1321 FMI: 2/2 лампы: Желтая СТО: | Либо низкое напряжение, обнаруженное при командовании + 12 VDC, либо напряжение, обнаруженное при отсутствии команд напряжения. | Либо двигатель будет **не** запускаться, либо двигатель ** не будет** иметь защиту от блокировки стартера. |

![[19c00486.png]]

Скриншоты Solenoid Lockout Relay Circuit

### Описание цепи

Стартерная схема локаута-ретранслятора представляет собой соленоид, приводимый в движение электронным модулем управления (ECM), который электрически изолирует реле стартера при работе двигателя.

### Расположение компонента

Смотрите диаграмму OEM для точного местоположения.

Устранение неполадок код t05-474


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 474
>
> ### Starter Solenoid Lockout Relay Driver Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 474 PID(P): S237 SPN: 1321 FMI: 2/2 Lamp: Yellow SRT: | Either low voltage detected when + 12 VDC are commanded or voltage detected when no voltage is commanded. | Either the engine will **not** start or the engine will **not** have starter lockout protection. |
>
> Starter Solenoid Lockout Relay Circuit
>
> ### Circuit Description
>
> The starter solenoid lockout relay driver circuit is a solenoid driven by the electronic control module (ECM) that electrically isolates the starter motor relay when the engine is running.
>
> ### Component Location
>
> Refer to an OEM diagram for the exact location.
>
> Refer to Troubleshooting Fault Code t05-474
