---
aliases:
  - "Привод понижающей передачи автопереключения (блокировочный электромагнит)"
type: "Процедура"
doc: "82-fc536"
title_en: "Autoshift Low Gear Actuator (Lockout Solenoid)"
title_ru: "Привод понижающей передачи автопереключения (блокировочный электромагнит)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc536.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc536.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Autoshift Low Gear Actuator (Lockout Solenoid)
**Привод понижающей передачи автопереключения (блокировочный электромагнит)**

> [!abstract] Процедура · `82-fc536`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc536.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc536.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 536

### Привод понижающей передачи автопереключения (блокировочный электромагнит)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 536 PID(P): S044 SPN: 718 FMI: 11/11 Лампа: Желтая СТО: | Либо низкое напряжение, обнаруженное на цепи привода с автоматическим переключением на низкое передаточное усилие, когда командуют + 12 VDC, либо напряжение, обнаруженное, когда не командуют напряжением. | Топ 2 локаут соленоид будет ** не** функционировать должным образом. Передача будет ** не** правильно сдвинута. |

![[19c00352.png]]

Топ 2 Lockout Solenoid Circuit

### Описание цепи

Автосменный привод с низким коэффициентом передачи - это соленоид, управляемый ECM, который управляет передачей Top 2.

### Расположение компонента

Автосменный привод с низким коэффициентом передачи расположен на верхней стороне трансмиссии по направлению к задней части. См. диаграмму OEM для конкретного местоположения.

См. Код устранения неполадок t05-536


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 536
>
> ### Autoshift Low Gear Actuator (Lockout Solenoid)
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 536 PID(P): S044 SPN: 718 FMI: 11/11 Lamp: Yellow SRT: | Either low voltage detected on autoshift low gear actuator circuit when + 12 VDC are commanded or voltage detected when no voltage is commanded. | Top 2 lockout solenoid will **not** function properly. Transmission will **not** shift properly. |
>
> Top 2 Lockout Solenoid Circuit
>
> ### Circuit Description
>
> The autoshift low gear actuator is an ECM-driven solenoid that controls a Top 2 transmission.
>
> ### Component Location
>
> The autoshift low gear actuator is located on the topside of a transmission toward the back. Refer to an OEM diagram for a specific location.
>
> Refer to Troubleshooting Fault Code t05-536
