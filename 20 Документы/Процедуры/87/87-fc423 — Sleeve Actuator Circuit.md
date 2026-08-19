---
aliases:
  - "Цепь исполнительного механизма гильзы"
type: "Процедура"
doc: "87-fc423"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc423.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc423.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Sleeve Actuator Circuit
**Цепь исполнительного механизма гильзы**

> [!abstract] Процедура · `87-fc423`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc423.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc423.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 423

### Цепь исполнительного механизма гильзы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 423 PID(P): 156 SPN: 156 FMI: 2 лампы: Желтая СТО: | Не удается достичь требуемого времени насоса. Эта неисправность может быть вызвана неправильными статическими временными характеристиками насоса, засоренными топливными фильтрами или входным экраном, застрявшими рукавами синхронизации, воздухом в топливных линиях или ошибками калибровки. | Электронный модуль управления не принимает никаких мер. Выходная мощность может быть низкой, а двигатель может производить белый или черный дым. |

![[19a00103.png]]

Цепь исполнительного механизма гильзы

### Описание цепи

Схема привода в рукаве используется для управления началом впрыска через контакт 6 проводов двигателя. Электронный модуль управления контролирует ток на контакте 6 и ожидает, что во время нормальной работы двигателя усилие будет варьироваться от 1,0 до 6,2 ампер.

### Расположение компонента

Схема привода в рукаве является неотъемлемой частью топливного насоса RP39.

### Практические замечания

Увеличение тока, подаваемого в цепь привода рукава, увеличивает продвижение по времени впрыска.

Застрявший тайминговый рукав может быть результатом загрязнения топлива.

Высокое ограничение впуска топлива и/или низкий уровень топлива могут привести к низкому уровню мощности.

См. Код устранения неполадок t05-423


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 423
>
> ### Sleeve Actuator Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 423 PID(P): 156 SPN: 156 FMI: 2 Lamp: Yellow SRT: | Unable to achieve the requested pump timing. This fault can be caused by incorrect static pump timing, clogged fuel filters or inlet screen, a stuck timing sleeve, air in the fuel lines, or calibration errors. | No action is taken by the electronic control module. Power output can be low and engine can produce white or black smoke. |
>
> Sleeve Actuator Circuit
>
> ### Circuit Description
>
> The sleeve actuator circuit is used to control the start of injection through pin 6 of the engine harness. The electronic control module monitors the current on pin 6 and expects the amperage to vary between 1.0 and 6.2 amperes during normal engine operation.
>
> ### Component Location
>
> The sleeve actuator circuit is an integral part of the RP39 fuel pump.
>
> ### Shoptalk
>
> Increasing the current supplied to the sleeve actuator circuit increases the timing advancement of injection.
>
> A stuck timing sleeve can be the result of fuel contamination.
>
> High fuel inlet restriction and/or low fuel level may cause a low power condition.
>
> Refer to Troubleshooting Fault Code t05-423
