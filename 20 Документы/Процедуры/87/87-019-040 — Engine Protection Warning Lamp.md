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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-040.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-040.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Engine Protection Warning Lamp
**Лампа предупреждения защиты двигателя**

> [!abstract] Процедура · `87-019-040`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-040.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-040.pdf)

### General Information

The engine protection system uses a lamp or a buzzer to alert the driver of one of the following conditions:

1. Low coolant level
2. High coolant temperature
3. Low oil pressure
4. Low coolant pressure
5. High intake manifold temperature
6. High fuel temperature
7. High blowby pressure.

![[nobox.png]]

The engine protection system warning lamp circuit is a positive (+) 24-VDC supply from the vehicle keyswitch, and a lamp or buzzer.

> [!note] Note · Примечание
> The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.

![[19a00164.png]]

### Voltage Check

Measure the voltage between the fault lamp and ground. Turn the vehicle keyswitch to the ON position. Touch the positive (+) multimeter probe to the buzzer or lamp terminal. Touch the negative (-) multimeter probe to the chassis ground. Measure the voltage. Repeat this check for the other terminal of the buzzer or fault lamp. The multimeter **must** show the battery voltage. If battery voltage is **not** present, there is a problem with the keyswitch wire, or the lamp (or buzzer) has failed. Refer to the OEM repair manual for repair instructions.

> [!note] Note · Примечание
> Battery voltage will vary between vehicles, depending on the age and condition of the batteries. There **must** be enough voltage available to illuminate the lamp or operate the buzzer.

![[ee8cok69.png]]
