---
aliases:
  - "Лампа предупреждения защиты двигателя"
type: "Процедура"
doc: "87-019-040"
title_en: "Engine Protection Warning Lamp"
title_ru: "Лампа предупреждения защиты двигателя"
modified: "2003-02-10"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-040.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-040.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Engine Protection Warning Lamp
**Лампа предупреждения защиты двигателя**

> [!abstract] Процедура · `87-019-040`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-040.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-040.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система защиты двигателя использует лампу или гудильщик для оповещения водителя об одном из следующих условий:

1. Низкий уровень охлаждающей жидкости
2. Высокая температура охлаждающей жидкости
3. Низкое давление масла
4. Низкое давление охлаждающей жидкости
5. Высокая температура коллектора впуска
6. Высокая температура топлива
7. Высокое давление.

![[nobox.png]]

Система защиты двигателя предупреждающая лампа представляет собой положительный (+) источник 24-VDC от переключателя зажигания транспортного средства и лампы или зуммера.

> [!note] Примечание
> Количество неисправных ламп может быть сокращено до двух для некоторых OEM-производителей. Защита двигателя и стоп-сигналы соединены вместе как красная лампа. Предупреждающая лампа остается желтой лампой.

![[19a00164.png]]

### Проверка напряжения

Измерьте напряжение между неисправной лампой и землей. Переключатель зажигания транспортного средства в положение Включения. Прикоснитесь к положительному (+) многометровому щупу к зуммеру или к оконечному устройству лампы. Прикоснитесь к отрицательному (-) многометровому щупу к земле шасси. Измерьте напряжение. Повторите эту проверку для другого терминала гудка или лампы неисправности. Мультиметр **должен** показывать напряжение батареи. Если напряжение батареи **не присутствует**, возникает проблема с проводом переключателя зажигания, или лампа (или гудильщик) вышла из строя. См. руководство по ремонту OEM для инструкций по ремонту.

> [!note] Примечание
> Напряжение батареи будет варьироваться между автомобилями, в зависимости от возраста и состояния батарей. Там должно быть достаточно напряжения, чтобы освещать лампу или управлять зуммером.

![[ee8cok69.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The engine protection system uses a lamp or a buzzer to alert the driver of one of the following conditions:
>
> 1. Low coolant level
> 2. High coolant temperature
> 3. Low oil pressure
> 4. Low coolant pressure
> 5. High intake manifold temperature
> 6. High fuel temperature
> 7. High blowby pressure.
>
> The engine protection system warning lamp circuit is a positive (+) 24-VDC supply from the vehicle keyswitch, and a lamp or buzzer.
>
> **Note · Примечание**
> The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.
>
> ### Voltage Check
>
> Measure the voltage between the fault lamp and ground. Turn the vehicle keyswitch to the ON position. Touch the positive (+) multimeter probe to the buzzer or lamp terminal. Touch the negative (-) multimeter probe to the chassis ground. Measure the voltage. Repeat this check for the other terminal of the buzzer or fault lamp. The multimeter **must** show the battery voltage. If battery voltage is **not** present, there is a problem with the keyswitch wire, or the lamp (or buzzer) has failed. Refer to the OEM repair manual for repair instructions.
>
> **Note · Примечание**
> Battery voltage will vary between vehicles, depending on the age and condition of the batteries. There **must** be enough voltage available to illuminate the lamp or operate the buzzer.
