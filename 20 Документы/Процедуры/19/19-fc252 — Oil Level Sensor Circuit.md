---
type: "Процедура"
doc: "19-fc252"
title_en: "Oil Level Sensor Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc252.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc252.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Oil Level Sensor Circuit

> [!abstract] Процедура · `19-fc252`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc252.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc252.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 252

### Сенсорная схема уровня масла

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 252 PID(P): P98 SPN: 098 FMI: 2 лампы: Желтая СТО: | Ошибка датчика уровня масла. | Отсутствие защиты двигателя при низком уровне масла. Система CentinelTM отключена. |

![[19400642.png]]

Сенсорная схема уровня масла

### Описание цепи

Датчик уровня моторного масла используется ECM для мониторинга количества масла в двигателе. Низкий уровень масла, обнаруженный при контакте 12, может привести к разрушению системы защиты двигателя и выключению двигателя.

### Расположение компонента

Датчик уровня моторного масла находится в поддоне для моторного масла.

См. Код устранения неполадок t05-252


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 252
>
> ### Oil Level Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 252 PID(P): P98 SPN: 098 FMI: 2 Lamp: Yellow SRT: | Oil level sensor error. | No engine protection for low oil level. Centinel™ system is disabled. |
>
> Oil Level Sensor Circuit
>
> ### Circuit Description
>
> The lubricating oil level sensor is used by the ECM to monitor the amount of oil in the engine. Low oil level detected at pin 12 can cause the engine protection system to derate and shut down the engine.
>
> ### Component Location
>
> The lubricating oil level sensor is in the engine oil pan.
>
> Refer to Troubleshooting Fault Code t05-252
