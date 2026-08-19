---
aliases:
  - "Ошибка электромагнита A"
type: "Процедура"
doc: "87-fc527"
title_en: "Solenoid A Error"
title_ru: "Ошибка электромагнита A"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc527.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc527.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Solenoid A Error
**Ошибка электромагнита A**

> [!abstract] Процедура · `87-fc527`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc527.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc527.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 527

### Ошибка электромагнита A

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 527 P(P): S040 SPN: P02 FMI: 3 лампы: Желтая СТО: | Менее 17 VDC обнаружены при контакте 41 подачи соленоида А с проводкой двигателя. | Электронный модуль управления (ECM) не выполняет никаких действий. |

![[19a00700.png]]

Соленоидная схема

### Описание цепи

Водитель соленоида будет управлять двигателем и функциями транспортного средства, закрывая или открывая переключаемый выход соленоида, на основе 11 выбранных параметров двигателя. Выход соленоидов будет контролировать такие функции, как сцепление вентилятора, нагреватель впускной сетки, индикатор ограничения очистки воздуха или индикатор дифференциального давления масляного фильтра.

### Расположение компонента

Соленоидный драйвер является OEM-устройством, и местоположение соленоида зависит от OEM-устройства.

См. Код устранения неполадок t05-527


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 527
>
> ### Solenoid A Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 527 PID(P): S040 SPN: P02 FMI: 3 Lamp: Yellow SRT: | Less than 17 VDC detected at solenoid A supply pin 41 of the engine harness. | No action is taken by the electronic control module (ECM). |
>
> Solenoid A Circuit
>
> ### Circuit Description
>
> The solenoid driver will control engine and vehicle functions by closing or opening a switched solenoid output, based on 11 selected engine parameters. The solenoid output will control functions like a fan clutch, intake grid heater, air cleaner restriction indicator, or an oil filter differential pressure indicator.
>
> ### Component Location
>
> The solenoid driver is an OEM device and the location of the solenoid is dependent upon the OEM.
>
> Refer to Troubleshooting Fault Code t05-527
