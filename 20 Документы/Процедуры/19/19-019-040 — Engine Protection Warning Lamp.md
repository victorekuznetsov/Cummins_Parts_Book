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
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-040.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-040.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
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

### General Information

The engine protection system uses a lamp or a buzzer to alert the driver to one of the following conditions:

1. Low coolant level
2. High coolant temperature
3. Low oil pressure
4. Low coolant pressure (**not** on QSK19)
5. High intake manifold temperature
6. High fuel temperature (**not** on QSK19)
7. High blowby pressure.

![[nobox.png]]

The engine protection system warning lamp circuit is a +24-VDC supply from the vehicle keyswitch, a lamp or buzzer, and pin 2 (engine protection output driver).

![[19400229.png]]

### Voltage Check

Measure the voltage between the fault lamp and ground. Turn the vehicle keyswitch ON. Touch the positive (+) multimeter probe to the buzzer or lamp terminal. Touch the negative (-) multimeter probe to the chassis ground. Measure the voltage. Repeat this check for the other terminal of the buzzer or fault lamp. The multimeter **must** show the battery voltage. If battery voltage is **not** present, there is a problem with the keyswitch wire or the lamp (or buzzer) has failed. Refer to the OEM repair manual for repair instructions.

> [!note] Note · Примечание
> Battery voltage will vary among vehicles depending on the age and condition of the batteries. There **must** be enough voltage available to illuminate the lamp or operate the buzzer.

![[ee8cok69.png]]
