---
aliases:
  - "Низкий уровень масла №1 — критично"
type: "Процедура"
doc: "01-fc253"
title_en: "Engine Oil Level Number 1 Low - Critical"
title_ru: "Низкий уровень масла №1 — критично"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc253.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc253.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Oil Level Number 1 Low - Critical
**Низкий уровень масла №1 — критично**

> [!abstract] Процедура · `01-fc253`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc253.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc253.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 253

### Низкий уровень масла №1 — критично

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 253 P(P): СПН: ФМИ: Лампа: Отключение SRT: | Уровень моторного масла упал ниже порога остановки для низкого уровня масла. | Двигатель отключится. |

![[19803623.png]]

Сенсорная схема уровня масла

### Описание цепи

Датчик уровня масла контролирует уровень масла в нефтяной системе и передает информацию в ECM. Низкий уровень масла может привести к тому, что двигатель запустится.

### Расположение компонента

См. диаграммы двигателя в разделе E этого руководства для определения местоположения компонента.

### Практические замечания

В некоторых конфигурациях двигателя будет использоваться 3-контактный датчик уровня масла, а в других - 4-контактный датчик уровня масла.

См. Код устранения неполадок t05-253


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 253
>
> ### Engine Oil Level Number 1 Low - Critical
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 253 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine oil level has dropped below the shutdown threshold for low oil level. | Engine will shut down. |
>
> Oil Level Sensor Circuit
>
> ### Circuit Description
>
> The oil level sensor monitors the oil level within the oil system and passes information to the ECM. Low oil level can cause the engine to **not** start.
>
> ### Component Location
>
> Refer to the Engine Diagrams in Section E of this manual for the component location.
>
> ### Shoptalk
>
> Some engine configurations will use a 3-pin oil level sensor and others will use a 4-pin oil level sensor.
>
> Refer to Troubleshooting Fault Code t05-253
