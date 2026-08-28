---
aliases:
  - "Замена моторного масла и фильтра"
type: "Процедура"
doc: "87-fc649"
title_en: "Change Lubricating Oil and Filter"
title_ru: "Замена моторного масла и фильтра"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc649.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc649.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Change Lubricating Oil and Filter
**Замена моторного масла и фильтра**

> [!abstract] Процедура · `87-fc649`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc649.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc649.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 649

### Замена моторного масла и фильтра

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 649 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Замена моторного масла и фильтра. Система Centinel не смогла заменить старое масло новым. Состояние сохраняется достаточно долго, чтобы качество масла гарантировало полное изменение. | Никаких действий со стороны ЕКМ не предпринимается. Возможные повреждения двигателя могут произойти. |

![[19802494.png]]

### Описание цепи

Масляный резервуар обеспечивает чистое масло для восполняющего клапана системы Centinel, чтобы пополнить масло, которое было сожжено системой Centinel.

### Расположение компонента

Разнообразие по установке. См. руководство по ремонту Centinel Master [[3666231 — Centinel™ Master Repair Manual\|3666231]] для получения дополнительной информации.

### Практические замечания

Эта ошибка указывает на то, что старая масло не пополнилась новой.

См. Код устранения неполадок t05-649


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 649
>
> ### Change Lubricating Oil and Filter
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 649 PID(P): SPN: FMI: Lamp: Warning SRT: | Change lubricating oil and filter. The Centinel system has **not** been able to replace old oil with new. The condition has persisted long enough that the oil quality warrants a full change out. | No action is taken by the ECM. Possible damage to engine can occur. |
>
> ### Circuit Description
>
> The oil make up tank provides clean oil to the make up valve of the Centinel system to replenish oil that was burned by the Centinel system.
>
> ### Component Location
>
> Varies by installation. Refer to Centinel Master Repair Manual [[3666231 — Centinel™ Master Repair Manual\|3666231]] for further information.
>
> ### Shoptalk
>
> This fault indicates that the old oil has **not** been replenished with new oil.
>
> Refer to Troubleshooting Fault Code t05-649
