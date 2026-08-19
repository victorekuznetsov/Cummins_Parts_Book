---
aliases:
  - "Привод рейки — механическая система не отвечает или разрегулирована"
type: "Процедура"
doc: "07-fc172"
title_en: "Rack Actuator - Mechanical System Not Responding Properly or Out of Adjustment"
title_ru: "Привод рейки — механическая система не отвечает или разрегулирована"
modified: "2012-12-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc172.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc172.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Rack Actuator - Mechanical System Not Responding Properly or Out of Adjustment
**Привод рейки — механическая система не отвечает или разрегулирована**

> [!abstract] Процедура · `07-fc172`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc172.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc172.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 172

### Привод рейки — механическая система не отвечает или разрегулирована

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 172 PID(P): S23 SPN: 638 FMI: 7 ламп: Красная СТО: | Редуктор стойки - механическая система ** не**, реагирующая должным образом или не настраиваемая. | Останов двигателя. |

![[19901354.png]]

Цепь привода рейки

### Описание цепи

Реестр управления топливом и соленоид определяют количество топлива, отмеренное для двигателя.

### Расположение компонента

Реестр управления топливом и соленоид являются неотъемлемой частью топливного насоса P7100.

### Практические замечания

- Подтвердите, что разъем привода прочно на месте.

- Неисправный топливный насос может вызвать неисправность кода 172.

См. Код устранения неполадок t05-172


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 172
>
> ### Rack Actuator - Mechanical System Not Responding Properly or Out of Adjustment
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 172 PID(P): S23 SPN: 638 FMI: 7 Lamp: Red SRT: | Rack actuator - mechanical system **not** responding properly or out of adjustment. | Engine shutdown. |
>
> Rack Actuator Circuit
>
> ### Circuit Description
>
> The fuel control rack and solenoid determine the quantity of fuel metered to the engine.
>
> ### Component Location
>
> The fuel control rack and solenoid are integral parts of the P7100 fuel pump
>
> ### Shoptalk
>
> - Confirm the actuator connector is firmly in place.
>
> - A defective fuel pump can cause Fault Code 172.
>
> Refer to Troubleshooting Fault Code t05-172
