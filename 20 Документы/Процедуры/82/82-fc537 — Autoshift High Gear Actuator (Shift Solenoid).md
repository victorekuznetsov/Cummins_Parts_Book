---
aliases:
  - "Привод повышающей передачи автопереключения (электромагнит)"
type: "Процедура"
doc: "82-fc537"
title_en: "Autoshift High Gear Actuator (Shift Solenoid)"
title_ru: "Привод повышающей передачи автопереключения (электромагнит)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc537.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc537.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Autoshift High Gear Actuator (Shift Solenoid)
**Привод повышающей передачи автопереключения (электромагнит)**

> [!abstract] Процедура · `82-fc537`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc537.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc537.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 537

### Привод повышающей передачи автопереключения (электромагнит)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 537 PID(P): S043 SPN: 717 FMI: 11/11 Лампа: Желтая СТО: | Либо низкое напряжение, обнаруженное на цепи привода с высокой передачей автоподключения, когда (+) 12 VDC, либо напряжение, обнаруженное, когда напряжение не командуется. | Топ-2 сдвига соленоида будет ** не** функционировать должным образом. Передача будет ** не** правильно сдвинута. |

![[19c00352.png]]

Топ 2 Сдвиг Соленоидной цепи

### Описание цепи

Автосменный привод высокой передачи - это соленоид, управляемый ECM, который управляет коробкой передач Top 2.

### Расположение компонента

Автосменный привод высокой передачи расположен на верхней стороне трансмиссии к задней части. См. диаграмму OEM для конкретного местоположения.

См. Код устранения неполадок t05-537


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 537
>
> ### Autoshift High Gear Actuator (Shift Solenoid)
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 537 PID(P): S043 SPN: 717 FMI: 11/11 Lamp: Yellow SRT: | Either low voltage detected on autoshift high gear actuator circuit when (+) 12 VDC are commanded or voltage detected when no voltage is commanded. | Top 2 shift solenoid will **not** function properly. Transmission will **not** shift properly. |
>
> Top 2 Shift Solenoid Circuit
>
> ### Circuit Description
>
> The autoshift high gear actuator is an ECM-driven solenoid that controls a Top 2 transmission.
>
> ### Component Location
>
> The autoshift high gear actuator is located on the topside of the transmission toward the back. Refer to an OEM diagram for the specific location.
>
> Refer to Troubleshooting Fault Code t05-537
