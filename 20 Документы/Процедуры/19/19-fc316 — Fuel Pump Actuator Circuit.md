---
type: "Процедура"
doc: "19-fc316"
title_en: "Fuel Pump Actuator Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc316.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc316.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Fuel Pump Actuator Circuit

> [!abstract] Процедура · `19-fc316`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc316.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc316.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 316

### Схема привода топливного насоса

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 316 P(P): S78 SPN: 931 FMI: 3 лампы: Желтая СТО: 00-670 | Схема привода топливного насоса открыта, или контакт 11 подачи закорачивается до напряжения батареи или земли, или обратный контакт 40 закорачивается до напряжения батареи или земли в ремне электропроводки двигателя. | Никаких действий со стороны ЕКМ не предпринимается. Привод открыт или закрыт, или частично закрыт. |

![[19800999.png]]

Схема привода топливного насоса

### Описание цепи

Схема привода топливного насоса подает ток в привод топливного насоса. ECM командует переменным количеством тока к приводу топливного насоса для управления выходным давлением топливного насоса к управляющему клапану.

### Расположение компонента

Привод топливного насоса расположен на топливном насосе.

### Практические замечания

- Подтвердите, что разъем привода прочно на месте.

- Когда нет питания на приводе, привод закрывается и поток топлива продолжается.

Устранение неполадок код t05-316


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 316
>
> ### Fuel Pump Actuator Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 316 PID(P): S78 SPN: 931 FMI: 3 Lamp: Yellow SRT: 00-670 | Fuel pump actuator circuit is open, or supply pin 11 is shorted to battery voltage or ground, or return pin 40 is shorted to battery voltage or ground in the engine harness. | No action by the ECM is taken. Actuator is open or closed, or partially closed. |
>
> Fuel Pump Actuator Circuit
>
> ### Circuit Description
>
> The fuel pump actuator circuit supplies current to the fuel pump actuator. The ECM commands a varying amount of current to the fuel pump actuator to control the fuel pump output pressure to the control valve assembly.
>
> ### Component Location
>
> The fuel pump actuator is located on the fuel pump.
>
> ### Shoptalk
>
> - Confirm that the actuator connector is firmly in place.
>
> - When there is no power to the actuator, the actuator closes and fuel flow continues.
>
> Refer to Troubleshooting Fault Code t05-316
