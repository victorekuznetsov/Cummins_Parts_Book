---
aliases:
  - "Цепь выключателя выбора альтернативной кривой момента"
type: "Процедура"
doc: "87-fc528"
title_en: "Alternate Torque Curve Select Switch Circuit"
title_ru: "Цепь выключателя выбора альтернативной кривой момента"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc528.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc528.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Alternate Torque Curve Select Switch Circuit
**Цепь выключателя выбора альтернативной кривой момента**

> [!abstract] Процедура · `87-fc528`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc528.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc528.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 528

### Цепь выключателя выбора альтернативной кривой момента

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 528 PID(P): P093 SPN: 093 FMI: 2 лампы: Желтая СТО: | Электронный модуль управления (ECM) обнаружил недействительное значение от альтернативного выключателя выбора крутящего момента при контакте 39 с проводкой OEM-интерфейса, указывая на то, что значение находится вне диапазона. | Альтернативный выбор крутящего момента отключен. Кривая крутящего момента, устанавливающая по умолчанию переключатель положения 2 (или наименьшего) предварительно запрограммированного крутящего момента. |

![[19801022.png]]

Альтернативная кривая крутящего момента Выберите коммутатор сигнала

### Описание цепи

Схема переключателя кривой крутящего момента позволяет оператору выбирать из трех заранее запрограммированных кривых крутящего момента с помощью переключателя с тремя состояниями.

### Расположение компонента

Расположение схемы переключателя кривой крутящего момента варьируется в зависимости от каждой модели OEM и оборудования. См. руководство по OEM.

### Практические замечания

Переключатель должен контролироваться для правильной работы в INSITETM. Если коммутатор правильно меняет состояние на инструменте службы, то проблема заключается в **не** в схеме коммутатора. В трехгосударственном переключателе есть три состояния:

- Позиция 1 - открытая

- Позиция 2 - закрытая

- Положение 3 - сопротивление 1500-ом.

См. Код устранения неполадок t05-528


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 528
>
> ### Alternate Torque Curve Select Switch Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 528 PID(P): P093 SPN: 093 FMI: 2 Lamp: Yellow SRT: | The electronic control module (ECM) has detected an invalid value from the alternate torque selection switch at pin 39 of the OEM interface harness, indicating the value is out of range. | Alternate torque selection is disabled. Torque curve setting defaults to switch position 2 (or lowest) preprogrammed torque curve. |
>
> Alternate Torque Curve Select Switch Signal Circuit
>
> ### Circuit Description
>
> The torque curve switch circuit allows the operator to select from three preprogrammed torque curves using a tristate switch.
>
> ### Component Location
>
> The location of the torque curve switch circuit varies with each OEM and equipment model. Refer to the OEM manual.
>
> ### Shoptalk
>
> The switch should be monitored for proper operation in INSITE™. If the switch is changing state correctly on the service tool, then the problem is **not** in the switch circuit. The tristate switch has three states:
>
> - Position 1 - open
>
> - Position 2 - closed
>
> - Position 3 - 1500-ohm resistance.
>
> Refer to Troubleshooting Fault Code t05-528
