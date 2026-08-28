---
type: "Процедура"
doc: "19-fc455"
title_en: "Rail Actuator Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc455.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc455.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Rail Actuator Circuit

> [!abstract] Процедура · `19-fc455`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc455.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc455.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 455

### Железнодорожный привод

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 455 PID(P): S18 SPN: 633 FMI: 3 лампы: Красная СТО: 00-376 | Схема привода рельсового привода открыта, или контакт 3 подачи закорачивается до напряжения батареи или земли, или обратный контакт 10 закорачивается до напряжения батареи или земли в ремне электропроводки двигателя. | Никаких действий со стороны ЕКМ не предпринимается. Привод закрыт или частично закрыт. Двигатель будет **не** работать, или будет работать на одной скорости. Код 514 ошибки может быть зарегистрирован. |

![[19400039.png]]

Железнодорожный привод

### Описание цепи

Схема привода рельса подает ток в привод рельса. ECM командует переменным количеством тока к приводу рельса, чтобы контролировать количество давления рельса к топливному форсунке.

### Расположение компонента

Рельсовой привод расположен на дне корпуса управляющего клапана, по направлению к передней части двигателя, позади ECM.

### Практические замечания

- Подтвердите, что разъем привода прочно на месте.

- Когда нет питания на приводе, привод закрывается и поток топлива останавливается. Это приведет к неисправности кода 514, что приведет к несоответствию потока.

- Когда к приводу закорочена мощность, привод открывается и поток топлива не контролируется. Это приведет к несоответствию кода 234, скорости двигателя или кода 514, что приведет к несоответствию потока.

Устранение неполадок код t05-455


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 455
>
> ### Rail Actuator Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 455 PID(P): S18 SPN: 633 FMI: 3 Lamp: Red SRT: 00-376 | Rail actuator circuit is open, or supply pin 3 is shorted to battery voltage or ground, or return pin 10 is shorted to battery voltage or ground in the engine harness. | No action by the ECM is taken. Actuator is closed, or partially closed. Engine will **not** run, or runs at one speed. Fault Code 514 can be logged. |
>
> Rail Actuator Circuit
>
> ### Circuit Description
>
> The rail actuator circuit supplies current to the rail actuator. The ECM commands a varying amount of current to the rail actuator to control the amount of rail pressure to the injectors.
>
> ### Component Location
>
> The rail actuator is located on the bottom of the control valve body, toward the front of the engine, behind the ECM.
>
> ### Shoptalk
>
> - Confirm that the actuator connector is firmly in place.
>
> - When there is no power to the actuator, the actuator closes and fuel flow stops. This will cause Fault Code 514, fueling flow mismatch.
>
> - When there is shorted power to the actuator, the actuator opens and fuel flow is uncontrolled. This will cause Fault Code 234, engine overspeed, or Fault Code 514, fueling flow mismatch.
>
> Refer to Troubleshooting Fault Code t05-455
