---
aliases:
  - "Электронный блок управления — предупреждение"
type: "Процедура"
doc: "01-fc343"
title_en: "Engine Control Module - Warning"
title_ru: "Электронный блок управления — предупреждение"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc343.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc343.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Control Module - Warning
**Электронный блок управления — предупреждение**

> [!abstract] Процедура · `01-fc343`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc343.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc343.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 343

### Электронный блок управления — предупреждение

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 343 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Внутренняя ошибка ECM. | Никаких действий со стороны ЕКМ не предпринимается. Возможная потеря производительности. |

![[19803627.png]]

Электронный блок управления

### Описание цепи

Электронный модуль управления (ECM) - это компьютер, который отвечает за управление двигателем, диагностику и функции пользователя.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Это неисправность внутренней схемы электронного модуля управления (ECM). Свободные соединения двигателя или шасси могут привести к регистрации кода 343 поломки, а также к жалобам на периодические споты. Обратите особое внимание на отрицательное соединение начального сообщения. Влажность в разъемах ECM также может привести к тому, что ECM введет в систему код 343 ошибки.

См. Код устранения неполадок t05-343


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 343
>
> ### Engine Control Module - Warning
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 343 PID(P): SPN: FMI: Lamp: Warning SRT: | Internal ECM error. | No action is taken by the ECM. Possible loss of performance. |
>
> Electronic Control Module
>
> ### Circuit Description
>
> The electronic control module (ECM) is a computer that is responsible for engine control, diagnostics, and user features.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> This is a fault with the internal circuitry of the electronic control module (ECM). Loose engine or chassis ground connections can cause Fault Code 343 to be logged, as well as complaints of an intermittent stumble. Pay special attention to the negative starter post connection. Moisture in the ECM connectors can also cause the ECM to log Fault Code 343.
>
> Refer to Troubleshooting Fault Code t05-343
