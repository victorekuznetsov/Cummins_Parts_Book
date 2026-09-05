---
aliases:
  - "Лампа предупреждения защиты двигателя"
type: "Процедура"
doc: "19-019-040"
title_en: "Engine Protection Warning Lamp"
title_ru: "Лампа предупреждения защиты двигателя"
modified: "2002-08-20"
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
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-040.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-040.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Engine Protection Warning Lamp
**Лампа предупреждения защиты двигателя**

> [!abstract] Процедура · `19-019-040`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-040.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-040.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система защиты двигателя использует лампу или гудильщик, чтобы предупредить водителя об одном из следующих условий:

1. Низкий уровень охлаждающей жидкости
2. Высокая температура охлаждающей жидкости
3. Низкое давление масла
4. Низкое давление охлаждающей жидкости (**не** на QSK19)
5. Высокая температура коллектора впуска
6. Высокая температура топлива (**не** на QSK19)
7. Высокое давление.

![[nobox.png]]

Система защиты двигателя предупреждающая лампа представляет собой источник питания +24-VDC от переключателя зажигания транспортного средства, лампы или зуммера и контакта 2 (водитель защиты двигателя).

![[19400229.png]]

### Проверка напряжения

Измерьте напряжение между неисправной лампой и землей. Включите переключатель зажигания автомобиля. Прикоснитесь к положительному (+) многометровому щупу к зуммеру или к оконечному устройству лампы. Прикоснитесь к отрицательному (-) многометровому щупу к земле шасси. Измерьте напряжение. Повторите эту проверку для другого терминала гудка или лампы неисправности. Мультиметр **должен** показывать напряжение батареи. Если напряжение батареи **не присутствует**, возникает проблема с проводом переключателя зажигания или лампа (или зуммер) вышла из строя. См. руководство по ремонту OEM для инструкций по ремонту.

> [!note] Примечание
> Напряжение батареи будет варьироваться в зависимости от возраста и состояния батарей. Там должно быть достаточно напряжения, чтобы освещать лампу или управлять зуммером.

![[ee8cok69.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The engine protection system uses a lamp or a buzzer to alert the driver to one of the following conditions:
>
> 1. Low coolant level
> 2. High coolant temperature
> 3. Low oil pressure
> 4. Low coolant pressure (**not** on QSK19)
> 5. High intake manifold temperature
> 6. High fuel temperature (**not** on QSK19)
> 7. High blowby pressure.
>
> The engine protection system warning lamp circuit is a +24-VDC supply from the vehicle keyswitch, a lamp or buzzer, and pin 2 (engine protection output driver).
>
> ### Voltage Check
>
> Measure the voltage between the fault lamp and ground. Turn the vehicle keyswitch ON. Touch the positive (+) multimeter probe to the buzzer or lamp terminal. Touch the negative (-) multimeter probe to the chassis ground. Measure the voltage. Repeat this check for the other terminal of the buzzer or fault lamp. The multimeter **must** show the battery voltage. If battery voltage is **not** present, there is a problem with the keyswitch wire or the lamp (or buzzer) has failed. Refer to the OEM repair manual for repair instructions.
>
> **Note · Примечание**
> Battery voltage will vary among vehicles depending on the age and condition of the batteries. There **must** be enough voltage available to illuminate the lamp or operate the buzzer.
