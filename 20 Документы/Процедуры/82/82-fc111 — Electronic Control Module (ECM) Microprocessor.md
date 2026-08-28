---
aliases:
  - "Микропроцессор ЭБУ"
type: "Процедура"
doc: "82-fc111"
title_en: "Electronic Control Module (ECM) Microprocessor"
title_ru: "Микропроцессор ЭБУ"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Electronic Control Module (ECM) Microprocessor
**Микропроцессор ЭБУ**

> [!abstract] Процедура · `82-fc111`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc111.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 111

### Микропроцессор ЭБУ

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 111 PID(P): S254 SPN: 629 FMI: 12/12 Лампа: Красная СТО: | Ошибка, внутренняя для ECM, связанная с отказами оборудования памяти или внутренними цепями питания напряжения ECM. | Двигатель не запускается. |

![[19c00010.png]]

микропроцессор ECM

### Описание цепи

ECM - это компьютер, который отвечает за управление двигателем, диагностику и функции пользователя.

### Расположение компонента

ECM прикреплен к стороне топливного насоса двигателя и может быть расположен либо над воздушным компрессором (высокогорный), либо над стартером (низкогорный).

### Практические замечания

Этот код ошибки может быть вызван только внутренней проблемой ECM. Ремонт невозможен для ECM.

Устранение неполадок код t05-111


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 111
>
> ### Electronic Control Module (ECM) Microprocessor
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 111 PID(P): S254 SPN: 629 FMI: 12/12 Lamp: Red SRT: | Error internal to the ECM related to the memory hardware failures or internal ECM voltage supply circuits. | Engine will **not** start. |
>
> ECM Microprocessor
>
> ### Circuit Description
>
> The ECM is a computer that is responsible for engine control, diagnostics, and user features.
>
> ### Component Location
>
> The ECM is bolted to the fuel pump side of the engine and can be located either above the air compressor (high-mount) or above the starter (low-mount).
>
> ### Shoptalk
>
> This fault code can **only** be caused by an internal ECM problem. Repairs are **not** possible for the ECM.
>
> Refer to Troubleshooting Fault Code t05-111
