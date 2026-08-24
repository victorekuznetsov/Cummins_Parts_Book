---
aliases:
  - "Неисправность электромагнита клапана впрыска масла"
type: "Процедура"
doc: "82-fc223"
title_en: "Burn Valve Solenoid Fault"
title_ru: "Неисправность электромагнита клапана впрыска масла"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc223.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc223.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Burn Valve Solenoid Fault
**Неисправность электромагнита клапана впрыска масла**

> [!abstract] Процедура · `82-fc223`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc223.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc223.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 223

### Неисправность электромагнита клапана впрыска масла

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 223 PID(P): S085 SPN: 1265 FMI: 4/4 лампы: Желтая СТО: | Неправильное напряжение, обнаруженное в цепи привода CentinelTM ECM. | Ни одного на выступление. CentinelTM деактивирован. |

![[19c00572.png]]

Сжигать соленоиды клапан

### Описание цепи

Сгорающий клапан соленоид контролирует поток масла в дренажную линию топлива во время цикла горения.

### Расположение компонента

Сложный соленоид находится поверх клапана управления маслом. Клапан управления маслом находится на левой стороне двигателя ниже корпуса подачи топлива.

См. Код устранения неполадок t05-223


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 223
>
> ### Burn Valve Solenoid Fault
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 223 PID(P): S085 SPN: 1265 FMI: 4/4 Lamp: Yellow SRT: | Incorrect voltage detected at the Centinel™ actuator circuit by the ECM. | None on performance. Centinel™ deactivated. |
>
> Burn Valve Solenoid
>
> ### Circuit Description
>
> The burn valve solenoid controls the flow of oil into the fuel drainline during the burn cycle.
>
> ### Component Location
>
> The burn valve solenoid is on top of the oil control valve. The oil control valve is on the left side of the engine below the fuel delivery housing.
>
> Refer to Troubleshooting Fault Code t05-223
