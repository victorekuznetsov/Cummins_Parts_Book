---
aliases:
  - "Выключатель промежуточной частоты вращения"
type: "Процедура"
doc: "98-019-107"
title_en: "Intermediate Speed Control Switch"
title_ru: "Выключатель промежуточной частоты вращения"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-107.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-107.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Intermediate Speed Control Switch
**Выключатель промежуточной частоты вращения**

> [!abstract] Процедура · `98-019-107`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-107.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-107.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Переключатель средней скорости расположен на панели интерфейса драйвера CENTRYTM.

> [!note] Примечание
> Некоторые приложения будут использовать реле вместо переключателя панели интерфейса. Посмотрите руководство OEM, чтобы увидеть, как конкретная система подключена.

![[19801910.png]]

### Проверка сопротивления

Найдите переключатель на панели интерфейса драйвера и удалите его. См. руководство по устранению неполадок и ремонту OEM для процедуры.

Отсоедините провода, подключенные к коммутатору (провод Nos). C6-C, C6-E, C6-H.

> [!note] Примечание
> Коммутатор обычно является открытым коммутатором.

![[19801911.png]]

Выберите функцию сопротивления на мультиметре.

Прикосновение к мультиметру приводит к переключательным терминалам.

Переключитесь на положение выключения (закрытое).

![[19801912.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не **открыта, то внутри переключателя есть короткое замыкание.

Замените выключатель. См. руководство по устранению неполадок и ремонту OEM для процедуры.

![[19801621.png]]

Переключите переключатель на положение ON.

Измерьте сопротивление. Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если схема **не **закрыта, то в переключателе есть открытая схема.

Замените выключатель. См. руководство по устранению неполадок и ремонту OEM для процедуры.

![[19801914.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The intermediate-speed switch is located on the CENTRY™ driver interface panel.
>
> **Note · Примечание**
> Some applications will use a relay instead of an interface panel switch. Refer to the OEM manual to see how a particular system is wired.
>
> ### Resistance Check
>
> Locate the switch on the driver interface panel and remove it. Refer to the OEM troubleshooting and repair manual for the procedure.
>
> Disconnect the wires connected to the switch (wire Nos. C6-C, C6-E, C6-H).
>
> **Note · Примечание**
> The switch is a normally open switch.
>
> Select the resistance function on the multimeter.
>
> Touch the multimeter leads to the switch terminals.
>
> Toggle the switch to the OFF (closed) position.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit within the switch.
>
> Replace the switch. Refer to the OEM troubleshooting and repair manual for the procedure.
>
> Toggle the switch to the ON position.
>
> Measure the resistance. The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is an open circuit within the switch.
>
> Replace the switch. Refer to the OEM troubleshooting and repair manual for the procedure.
