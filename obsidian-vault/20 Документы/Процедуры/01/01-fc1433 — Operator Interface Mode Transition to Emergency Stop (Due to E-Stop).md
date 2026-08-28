---
aliases:
  - "Переход панели оператора в режим аварийного останова (кнопка E-Stop)"
type: "Процедура"
doc: "01-fc1433"
title_en: "Operator Interface Mode Transition to Emergency Stop (Due to E-Stop)"
title_ru: "Переход панели оператора в режим аварийного останова (кнопка E-Stop)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1433.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1433.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Operator Interface Mode Transition to Emergency Stop (Due to E-Stop)
**Переход панели оператора в режим аварийного останова (кнопка E-Stop)**

> [!abstract] Процедура · `01-fc1433`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1433.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1433.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1433

### Переход панели оператора в режим аварийного останова (кнопка E-Stop)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1433 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Переход панели оператора в режим аварийного останова (кнопка E-Stop). | Двигатель отключится и не будет перезагружаться до тех пор, пока выключатель аварийной остановки не будет сброшен. |

![[19802494.png]]

### Описание цепи

### Расположение компонента

См. Код устранения неисправностей t05-1433


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1433
>
> ### Operator Interface Mode Transition to Emergency Stop (Due to E-Stop)
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1433 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Operator interface mode transition to emergency stop (due to E-Stop). | Engine will shut down and will **not** restart until the emergency stop switch has been reset. |
>
> ### Circuit Description
>
> ### Component Location
>
> Refer to Troubleshooting Fault Code t05-1433
