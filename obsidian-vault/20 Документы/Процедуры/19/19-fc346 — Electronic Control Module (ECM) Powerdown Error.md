---
type: "Процедура"
doc: "19-fc346"
title_en: "Electronic Control Module (ECM) Powerdown Error"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc346.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc346.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Electronic Control Module (ECM) Powerdown Error

> [!abstract] Процедура · `19-fc346`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc346.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc346.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 346

### Электронный модуль управления (ECM) с ошибкой выключения

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 346 P(P): S253 SPN: 630 FMI: 12 ламп: Желтая СТО: 00-366 | ECM Powerdown - внутренняя ошибка хранения данных. | Данные Powerdown теряются. Данные Powerdown включают мониторинг технического обслуживания, текущее время ECM и дельта двигателя, а также прошлые данные о неисправности. |

![[19400081.png]]

Мощность аккумулятора и наземная схема

### Описание цепи

ECM - это компьютер, который отвечает за управление двигателем, диагностику и функции пользователя.

### Расположение компонента

ECM прикреплен к корпусу управляющего клапана на левой стороне двигателя.

### Практические замечания

- Это связано с внутренней памятью ECM. Эта неисправность может быть вызвана перебоем питания в ECM или полной потерей мощности батареи.

- Код 346 неисправности может быть вызван **не** после правильной процедуры отключения двигателя. Если используется главный выключатель отключения, вы должны выключить замок зажигания, подождать 30 секунд, а затем отключить батареи с помощью главного выключателя отключения. Если оператор не будет ждать 30 секунд, прежде чем отсоединить батареи, код 346 по умолчанию будет зарегистрирован.

- Если код 346 ошибки активен, включите переключатель зажигания, затем выключите его и подождите 30 секунд. Повторите этот шаг три раза с 30-секундной задержкой между каждым ключевым циклом.

Устранение неполадок код t05-346


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 346
>
> ### Electronic Control Module (ECM) Powerdown Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 346 PID(P): S253 SPN: 630 FMI: 12 Lamp: Yellow SRT: 00-366 | ECM powerdown internal data store error. | Powerdown data are lost. Powerdown data include maintenance monitoring, present ECM and engine delta times, and past fault data. |
>
> Battery Power and Ground Circuit
>
> ### Circuit Description
>
> The ECM is a computer that is responsible for engine control, diagnostics, and user features.
>
> ### Component Location
>
> The ECM is bolted to the control valve body on the left side of the engine.
>
> ### Shoptalk
>
> - This is a fault with the internal memory of the ECM. This fault can be caused by a power interruption to the ECM or a total loss of battery power.
>
> - Fault Code 346 can be caused by **not** following the correct engine shutdown procedure. If a master disconnect switch is being used, you **must** turn the keyswitch OFF, wait 30 seconds, then disconnect the batteries using the master disconnect switch. If the operator does **not** wait 30 seconds before disconnecting the batteries, Fault Code 346 will be logged.
>
> - If Fault Code 346 is active, turn the keyswitch ON, then turn it to OFF and wait 30 seconds. Repeat this step three times with a 30-second delay between each key cycle.
>
> Refer to Troubleshooting Fault Code t05-346
