---
aliases:
  - "Цепь управляющего электромагнита Centinel™"
type: "Процедура"
doc: "96-019-139"
title_en: "Centinel™ Control Solenoid Circuit"
title_ru: "Цепь управляющего электромагнита Centinel™"
modified: "2004-02-25"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 5
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-139.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-019-139.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
---

# Centinel™ Control Solenoid Circuit
**Цепь управляющего электромагнита Centinel™**

> [!abstract] Процедура · `96-019-139`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-139.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-019-139.pdf)

### General Information

Heavy-Duty

The solenoid circuits are the supply and return wires in the wiring harness to each of the solenoids. The return wires go from the wiring harness at the Centinel™ control module to the 2-pin connector of the solenoid wires that connect to each solenoid. The supply wires go from the power relay to the 2-pin connector of the solenoid wires that connect to each solenoid.

![[05600052.png]]

High-Horsepower

The solenoid circuits are the supply and return wires in the wiring harness to each of the solenoids. The return wires go from the terminal of the battery to the 2-pin connector of the solenoid wires that connect to each solenoid. The supply wires go from the wiring harness at the Centinel™ control module to the 2-pin connector of the solenoid wires that connect to each solenoid.

![[05600052.png]]

Disconnect the wiring harness from the Centinel™ control module and check for damaged pins.

![[05400055.png]]

### Resistance Check

The resistance value of the solenoid circuit is very low. The solenoid resistance is also temperature sensitive. To read an accurate resistance value, the resistance of the multimeter **must** be subtracted from the total resistance of the solenoid circuit.

![[nobox.png]]

> [!note] Note · Примечание
> Use a digital multimeter for this procedure. Use Cummins digital multimeter, Part Number 3377161, or a multimeter with the same accuracy of ±1/2 percent.

Turn the multimeter to the ON position. Set the multimeter range to the lowest ohm scale. Measure the resistance across the two test leads. This is the multimeter resistance value that will be subtracted from the solenoid resistance value.

![[ee8cok80.png]]
