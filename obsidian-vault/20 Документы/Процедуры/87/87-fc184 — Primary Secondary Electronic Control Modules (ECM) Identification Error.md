---
aliases:
  - "Ошибка идентификации основного и резервного ЭБУ"
type: "Процедура"
doc: "87-fc184"
title_en: "Primary/Secondary Electronic Control Modules (ECM) Identification Error"
title_ru: "Ошибка идентификации основного и резервного ЭБУ"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc184.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc184.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Primary/Secondary Electronic Control Modules (ECM) Identification Error
**Ошибка идентификации основного и резервного ЭБУ**

> [!abstract] Процедура · `87-fc184`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc184.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc184.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 184

### Ошибка идентификации основного и резервного ЭБУ

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 184 PID(P): S233 SPN: 609 FMI: 2 лампы: Красная СТО: | Первичная и/или вторичная ошибка идентификации ECM. | Идентификация модуля при включении питания не будет работать; оба модуля будут работать как вторичные ECM. Возможная потеря производительности. |

![[19a00382.png]]

Первичная/вторая ошибка идентификации ECM

### Описание цепи

Система управления QST30 использует два ECM, один первичный и один вторичный.

### Расположение компонента

Один ECM расположен по обе стороны двигателя перед топливными насосами.

### Практические замечания

Идентификация между первичным и вторичным модулями осуществляется при включении ключа через электропроводку. Контакты 47 и 48 ремня электропроводки двигателя для каждого банка обеспечивают определение первичного или вторичного. См. следующую таблицу для первичной/вторичной идентификации:

| Идентификация ECM | VDC в контакте 47 | VDC в контакте 48 |
|---|---|---|
| первичный | +5 VDC | 0 VDC |
| вторичный | 0 VDC | +5 VDC |

См. Код устранения неполадок t05-184


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 184
>
> ### Primary/Secondary Electronic Control Modules (ECM) Identification Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 184 PID(P): S233 SPN: 609 FMI: 2 Lamp: Red SRT: | Primary and/or secondary ECM identification error. | Module identification at power-up will fail; both modules will run as secondary ECMs. Possible loss of performance. |
>
> Primary/Secondary ECM Identification Error
>
> ### Circuit Description
>
> The QST30 control system utilizes two ECMs, one primary and one secondary.
>
> ### Component Location
>
> One ECM is located on both sides of the engine in front of the fuel pumps.
>
> ### Shoptalk
>
> Identification between primary and secondary modules is done at key-on through the harness. Pins 47 and 48 of the engine harness for each bank provide the determination of primary or secondary. Reference the following table for primary/secondary identification:
>
> | ECM Identification | VDC at Pin 47 | VDC at Pin 48 |
> |---|---|---|
> | Primary | +5 VDC | 0 VDC |
> | Secondary | 0 VDC | +5 VDC |
>
> Refer to Troubleshooting Fault Code t05-184
