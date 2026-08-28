---
aliases:
  - "Цепь управляющего электромагнита Centinel™"
type: "Процедура"
doc: "19-019-139"
title_en: "Centinel™ Control Solenoid Circuit"
title_ru: "Цепь управляющего электромагнита Centinel™"
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
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-139.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-139.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Centinel™ Control Solenoid Circuit
**Цепь управляющего электромагнита Centinel™**

> [!abstract] Процедура · `19-019-139`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-139.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-139.pdf)

### General Information

**High Horse Power**

The solenoid circuits are the supply and return wires in the wiring harness to each of the solenoids. The return wires go from the terminal of the battery to the 2-pin connector of the solenoid wires which connect to each solenoid. The supply wires go from the wiring harness at the ECM to the 2-pin connector of the solenoid wires which connect to each solenoid.

![[19400640.png]]

Disconnect the wiring harness from the ECM and check for damaged pins. Refer to Procedure 019-999, Connector Pins - Checking.

![[19400641.png]]

### Resistance Check

The resistance value of the solenoid circuit is very low. The solenoid resistance is also temperature sensitive. To read an accurate resistance value, the resistance of the multimeter **must** be subtracted from the total resistance of the solenoid circuit.

![[nobox.png]]

> [!warning] CAUTION · Осторожно
> Use a digital multimeter for this procedure. Use Cummins digital multimeter, Part Number 3377161, or a multimeter with the same accuracy of ±½ percent.

Turn the multimeter to the ON position. Set the multimeter range to the lowest ohm scale. Measure the resistance across the two test leads. This is the multimeter resistance value which will be subtracted from the solenoid resistance value.

![[ee8cok80.png]]
