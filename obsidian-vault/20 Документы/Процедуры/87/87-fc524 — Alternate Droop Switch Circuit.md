---
aliases:
  - "Цепь выключателя альтернативного статизма"
type: "Процедура"
doc: "87-fc524"
title_en: "Alternate Droop Switch Circuit"
title_ru: "Цепь выключателя альтернативного статизма"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc524.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc524.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Alternate Droop Switch Circuit
**Цепь выключателя альтернативного статизма**

> [!abstract] Процедура · `87-fc524`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc524.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc524.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 524

### Цепь выключателя альтернативного статизма

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 524 P(P): P113 SPN: 113 ФМИ: 2 лампы: Желтая СТО: | Электронный модуль управления (ECM) обнаружил недействительный выключатель выбора сбрасывания на контакте 22 с ремнем проводов двигателя, что указывает на то, что значение находится вне диапазона. | Отбор дропов отключен. Уменьшить настройки по умолчанию для переключения позиции 1 (или нормального) предварительно запрограммированного значения управляющего упадка. |

![[19a00760.png]]

Цепь выключателя альтернативного статизма

### Описание цепи

Альтернативная схема переключателя сбрасывания позволяет оператору выбирать из трех заранее запрограммированных значений сбрасывания с помощью переключателя с тремя состояниями.

### Расположение компонента

Расположение альтернативной схемы выключателя сбрасывания варьируется в зависимости от каждой модели OEM и оборудования. См. руководство по OEM.

### Практические замечания

Переключатель должен контролироваться для правильной работы на INSITETM. Если коммутатор правильно меняет состояние на инструменте службы, то проблема заключается в **не** в схеме коммутатора. Переключатель имеет три состояния:

- Позиция 1 - открытая

- Позиция 2 - закрытая

- Положение 3 - сопротивление 1500-ом.

См. Код устранения неполадок t05-524


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 524
>
> ### Alternate Droop Switch Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 524 PID(P): P113 SPN: 113 FMI: 2 Lamp: Yellow SRT: | Electronic control module (ECM) has detected an invalid droop selection switch on pin 22 of the engine harness, indicating the value is out of range. | Droop selection is disabled. Droop setting defaults to switch position 1 (or normal) preprogrammed droop governor values. |
>
> Alternate Droop Switch Circuit
>
> ### Circuit Description
>
> The alternate droop switch circuit allows the operator to select from three preprogrammed droop values using a tristate switch.
>
> ### Component Location
>
> The location of the alternate droop switch circuit varies with each OEM and equipment model. Refer to the OEM manual.
>
> ### Shoptalk
>
> The switch should be monitored for proper operation on INSITE™. If the switch is changing state correctly on the service tool, then the problem is **not** in the switch circuit. The switch has three states:
>
> - Position 1 - open
>
> - Position 2 - closed
>
> - Position 3 - 1500-ohm resistance.
>
> Refer to Troubleshooting Fault Code t05-524
