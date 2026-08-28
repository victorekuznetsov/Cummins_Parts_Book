---
aliases:
  - "Высокий уровень масла №1 — предупреждение"
type: "Процедура"
doc: "01-fc688"
title_en: "Engine Oil Level Number 1 High - Warning"
title_ru: "Высокий уровень масла №1 — предупреждение"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc688.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc688.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Oil Level Number 1 High - Warning
**Высокий уровень масла №1 — предупреждение**

> [!abstract] Процедура · `01-fc688`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc688.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc688.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 688

### Высокий уровень масла №1 — предупреждение

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 688 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Уровень моторного масла No1 высокий - критический. Сигнал напряжения указывает на очень высокий уровень моторного масла в двигателе. | Двигатель отключится. |

![[19803584.png]]

Сенсорная схема уровня масла

### Описание цепи

Датчик уровня масла используется ECM для мониторинга количества масла в двигателе. Высокие уровни масла могут привести к выключению двигателя или запуску **не**.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

4-контактный датчик уровня масла будет **не** запускать код 688.

Устранение неполадок код t05-688


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 688
>
> ### Engine Oil Level Number 1 High - Warning
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 688 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine oil level Number 1 high - critical. Voltage signal indicates very high lubricating oil level in the engine. | Engine will shut down. |
>
> Oil Level Sensor Circuit
>
> ### Circuit Description
>
> The oil level sensor is used by the ECM to monitor the amount of oil in the engine. High oil level detected can cause the engine to shut down or **not** start.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> A 4-pin oil level sensor will **not** trigger Fault Code 688.
>
> Refer to Troubleshooting Fault Code t05-688
