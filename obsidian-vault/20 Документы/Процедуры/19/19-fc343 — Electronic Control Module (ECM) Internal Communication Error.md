---
aliases:
  - "Внутренняя ошибка связи ЭБУ"
type: "Процедура"
doc: "19-fc343"
title_en: "Electronic Control Module (ECM) Internal Communication Error"
title_ru: "Внутренняя ошибка связи ЭБУ"
modified: "2011-03-01"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc343.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc343.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Electronic Control Module (ECM) Internal Communication Error
**Внутренняя ошибка связи ЭБУ**

> [!abstract] Процедура · `19-fc343`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc343.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc343.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 343

### Внутренняя ошибка связи ЭБУ

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 343 P(P): S254 SPN: 629 FMI: 12 ламп: Желтая СТО: 00-341 | Микропроцессорная ошибка связи внутри ECM. | Переменная; производительность будет или не будет затронута. |

![[19400316.png]]

Электронный блок управления

### Описание цепи

ECM - это компьютер, который отвечает за управление двигателем, диагностику и функции пользователя.

### Расположение компонента

ECM прикреплен к корпусу управляющего клапана на левой стороне двигателя.

### Практические замечания

- Это является ошибкой внутренней схемы ECM. Ремонт модуля в полевых условиях невозможен.

См. Код устранения неполадок t05-343


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 343
>
> ### Electronic Control Module (ECM) Internal Communication Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 343 PID(P): S254 SPN: 629 FMI: 12 Lamp: Yellow SRT: 00-341 | Microprocessor communication error internal to the ECM. | Variable; performance will or will **not** be affected. |
>
> Electronic Control Module
>
> ### Circuit Description
>
> The ECM is a computer that is responsible for engine control, diagnostics, and user features.
>
> ### Component Location
>
> The ECM is bolted to the control valve body on the left side of the engine.
>
> ### Shoptalk
>
> - This is a fault with the internal circuitry of the ECM. There are no repairs possible for the module in the field.
>
> Refer to Troubleshooting Fault Code t05-343
