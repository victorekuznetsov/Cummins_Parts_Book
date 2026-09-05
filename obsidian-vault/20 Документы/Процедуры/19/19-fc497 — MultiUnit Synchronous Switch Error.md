---
type: "Процедура"
doc: "19-fc497"
title_en: "MultiUnit Synchronous Switch Error"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc497.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc497.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# MultiUnit Synchronous Switch Error

> [!abstract] Процедура · `19-fc497`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc497.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc497.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 497

### MultiUnit Synchronous Switch ошибка

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 497 PID(P): S114 SPN: 1377 FMI: 2 лампы: Желтая СТО: | Многоединый синхронный переключатель включения/выключения и многоединый синхронный бесплатный переключатель включения/выключения имеют разные значения в ECM. | Многоединая синхронная функция отключена. |

![[19400687.png]]

MultiUnit Synchronous коммутационная схема

### Описание цепи

Многоединичная синхронная система использует дополнительный переключатель для подачи двух противоположных сигналов в ECM.

### Расположение компонента

Многоузловой синхронный переключатель установлен кабиной. См. руководство OEM для конкретного местоположения.

См. Код устранения неполадок t05-497


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 497
>
> ### MultiUnit Synchronous Switch Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 497 PID(P): S114 SPN: 1377 FMI: 2 Lamp: Yellow SRT: | Multiunit synchronous on/off switch and multiunit synchronous complimentary on/off switch have different values at the ECM. | Multiunit synchronous feature is disabled. |
>
> MultiUnit Synchronous Switch Circuit
>
> ### Circuit Description
>
> The multiunit synchronous uses a complimentary switch to provide two opposite signals into the ECM.
>
> ### Component Location
>
> The multiunit synchronous switch is cab-mounted. Refer to the OEM manual for specific location.
>
> Refer to Troubleshooting Fault Code t05-497
