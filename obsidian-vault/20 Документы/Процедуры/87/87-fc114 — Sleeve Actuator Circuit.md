---
aliases:
  - "Цепь исполнительного механизма гильзы"
type: "Процедура"
doc: "87-fc114"
title_en: "Sleeve Actuator Circuit"
title_ru: "Цепь исполнительного механизма гильзы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc114.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc114.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Sleeve Actuator Circuit
**Цепь исполнительного механизма гильзы**

> [!abstract] Процедура · `87-fc114`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc114.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc114.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 114

### Цепь исполнительного механизма гильзы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 114 PID(P): S020 SPN: 635 FMI: 4 лампы: Желтая СТО: | Менее 1,0 ампера обнаруживается на схеме привода рукава контакт 6 проводов двигателя ремня. | Не предпринимается никаких действий с помощью электронного модуля управления (ECM). Двигатель излучает белый дым и теряет мощность. |

![[19a00103.png]]

Цепь исполнительного механизма гильзы

### Описание цепи

Схема привода в рукаве используется для управления началом впрыска через контакт 6 проводов двигателя. ECM контролирует ток на контакте 6 и ожидает, что во время нормальной работы двигателя будет наблюдаться разность усилителей от 1,0 до 6,2 ампер. Отдача ниже 1,0 ампер на контакте 6 будет срабатывать код 114 ошибки.

### Расположение компонента

Схема привода в рукаве является неотъемлемой частью топливного насоса RP39.

### Практические замечания

Эта неисправность может быть вызвана внутренней проблемой ECM или открытой схемой в проводах. Ремонт модуля в полевых условиях невозможен.

Устранение неполадок код t05-114


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 114
>
> ### Sleeve Actuator Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 114 PID(P): S020 SPN: 635 FMI: 4 Lamp: Yellow SRT: | Less than 1.0 amp is detected at the sleeve actuator circuit pin 6 of the engine harness. | No action by the electronic control module (ECM) is taken. Engine emits white smoke and loses power. |
>
> Sleeve Actuator Circuit
>
> ### Circuit Description
>
> The sleeve actuator circuit is used to control the start of injection through pin 6 of the engine harness. The ECM monitors the current on pin 6 and expects to see the amperage vary between 1.0 and 6.2 amps during normal engine operation. Amperage below 1.0 amp on pin 6 will trip Fault Code 114.
>
> ### Component Location
>
> The sleeve actuator circuit is an integral part of the RP39 fuel pump.
>
> ### Shoptalk
>
> This fault can be caused by an internal ECM problem or a open circuit in the wiring. There are no repairs possible for the module in the field.
>
> Refer to Troubleshooting Fault Code t05-114
