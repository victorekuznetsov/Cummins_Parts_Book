---
aliases:
  - "Микропроцессор ЭБУ"
type: "Процедура"
doc: "01-fc111"
title_en: "Electronic Control Module (ECM) Microprocessor"
title_ru: "Микропроцессор ЭБУ"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Electronic Control Module (ECM) Microprocessor
**Микропроцессор ЭБУ**

> [!abstract] Процедура · `01-fc111`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc111.pdf)

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
| Код неисправности: 111 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Ошибка внутри ECM. | Двигатель не запускается. |

![[19802494.png]]

СХУ ECM

### Описание цепи

ECM - это компьютер, который отвечает за управление двигателем, диагностику и функции пользователя.

### Расположение компонента

См. руководство OEM для определения местоположения компонента.

### Практические замечания

Этот код ошибки может быть вызван только внутренней проблемой ECM.

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
> | Fault Code: 111 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Error internal to the ECM. | Engine will **not** start. |
>
> GCS ECM
>
> ### Circuit Description
>
> The ECM is a computer that is responsible for engine control, diagnostics, and user features.
>
> ### Component Location
>
> Refer to the OEM manual for the component location.
>
> ### Shoptalk
>
> This fault code can **only** be caused by an internal ECM problem.
>
> Refer to Troubleshooting Fault Code t05-111
