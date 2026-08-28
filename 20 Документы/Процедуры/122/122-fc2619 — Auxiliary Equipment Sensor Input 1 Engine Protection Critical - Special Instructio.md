---
aliases:
  - "Вход датчика вспомогательного оборудования 1, защита двигателя — особые указания"
type: "Процедура"
doc: "122-fc2619"
title_en: "Auxiliary Equipment Sensor Input 1 Engine Protection Critical - Special Instructions"
title_ru: "Вход датчика вспомогательного оборудования 1, защита двигателя — особые указания"
modified: "2010-09-21"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc2619.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc2619.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Auxiliary Equipment Sensor Input 1 Engine Protection Critical - Special Instructions
**Вход датчика вспомогательного оборудования 1, защита двигателя — особые указания**

> [!abstract] Процедура · `122-fc2619`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc2619.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc2619.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2619

### Вход датчика вспомогательного оборудования 1, защита двигателя — особые указания

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2619 PID(P): СПН: 701 FMI: 31 лампа: Янтарная СРТ: | Вход датчика вспомогательного оборудования 1, защита двигателя — особые указания. Выключение воздуха активируется от скорости двигателя или E-stop оператора. | Двигатель отключается, если включена функция защиты двигателя. |

![[19f00001.png]]

Air Shutoff (OEM Switch/Dual Output) и E-stop Circuit

### Описание цепи

Схема использует сигнал OEM E-stop или сверхскоростной двигатель для активации отключения воздуха.

### Расположение компонента

Кнопка E-Stop расположена на двери панели клиентского интерфейса (CIB).

### Практические замечания

Это для двигателей с одним или несколькими OEM-предоставленными клапанами отключения воздуха.

Отключение воздуха использует вход OEM-коммутатора для аварийной остановки отключения воздуха. Закрытие переключателя от E-stop оператора или от скорости двигателя приведет к активации отключения воздуха. Причинами этого кода неисправности являются:

- Оператор нажимает кнопку остановки двигателя.

- Событие отключения скорости, как командует ECM.

См. Код устранения неисправностей t05-2619


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2619
>
> ### Auxiliary Equipment Sensor Input 1 Engine Protection Critical - Special Instructions
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2619 PID(P): SPN: 701 FMI: 31 Lamp: Amber SRT: | Auxiliary Equipment Sensor Input 1 Engine Protection Critical - Special Instructions. The air shutoff is activated from engine overspeed or operator's E-stop. | Engine shuts down if engine protection shutdown feature is enabled. |
>
> Air Shutoff (OEM Switch/Dual Output) and E-stop Circuit
>
> ### Circuit Description
>
> The circuit uses the OEM E-stop signal or engine overspeed to activate the air shutoff.
>
> ### Component Location
>
> The E-Stop button is located on the door of the customer interface box (CIB) panel.
>
> ### Shoptalk
>
> This is for engines with one or more OEM supplied air shutoff valves.
>
> The air shutoff uses the OEM switch input for the emergency air shutoff stop. A switch closure from either the operator's E-stop or engine overspeed will cause the air shutoff to activate. Causes of this fault code are:
>
> - Operator pushes engine stop button.
>
> - Overspeed shutdown event as commanded by the ECM.
>
> Refer to Troubleshooting Fault Code t05-2619
