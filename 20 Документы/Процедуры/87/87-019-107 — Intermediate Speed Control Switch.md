---
aliases:
  - "Выключатель промежуточной частоты вращения"
type: "Процедура"
doc: "87-019-107"
title_en: "Intermediate Speed Control Switch"
title_ru: "Выключатель промежуточной частоты вращения"
modified: "2003-02-10"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 7
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-107.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-107.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Intermediate Speed Control Switch
**Выключатель промежуточной частоты вращения**

> [!abstract] Процедура · `87-019-107`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-107.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-107.pdf)

### General Information

The intermediate-speed control (ISC) ON, OFF, and ON switch circuit signals the QST system that the operator is requesting to go to one of two preset speeds between low idle and high idle. There is one three-position switch that selects ISC 1, OFF, and ISC 2.

![[19400281.png]]

The ISC circuit is shown for ISC 1 and ISC 2 features. The ISC circuit is wired with a double-pole, double-throw (called a DPDT switch), three-position switch.

![[19a00341.png]]

The DPDT three-position switch selectively grounds wire numbers 35 and 37, or wire numbers 38 and 37, or no wires. The logic of the switch is shown.

The lines that connect the switch terminals at the three lever positions are lines of continuity between the terminals.

In position 1, switch terminal numbers 2, 3 and 5, 6 are connected, which shorts ISC 2 and ISC validation (pins 38 and 37) to ground.

In position 2, no pins are grounded.

In position 3, switch terminal numbers 1, 2 and 4, 5 are connected, which shorts ISC 1 and ISC validation (pins 35 and 37) to ground.

![[19400283.png]]

### Resistance Check

If INSITE™, Part Number 3824801, is available, monitor the ISC switch for proper operation. If **not**, follow the troubleshooting procedures in this section.

Remove the four connectors from the switch.

Label the wires with the switch location and the wire numbers.

![[19a00342.png]]

With the switch in position 1, measure the resistance from switch terminal 2 to switch terminal 3. The resistance **must** be 10 ohms or less.

Measure the resistance from switch terminal 5 to switch terminal 6. The resistance **must** be 10 ohms or less.

Measure the resistance from switch terminal 1 to all switch terminals. The resistance **must** be 100k ohms or more.

Measure the resistance from switch terminal 4 to all other terminals. The resistance **must** be 100k ohms or more.

![[19400285.png]]

Move the switch lever to position 2.

Measure the resistance from switch terminal 1 to all other terminals. The resistance **must** be 100k ohms or more.

Measure the resistance from switch terminal 2 to all other terminals. The resistance **must** be 100k ohms or more.

![[19400286.png]]

Move the switch lever to position 3.

Measure the resistance from switch terminal 1 to terminal 2. The resistance **must** be 10 ohms or less.

Measure the resistance from switch terminal 4 to terminal 5. The resistance **must** be 10 ohms or less.

Measure the resistance from switch terminal 3 to all other terminals. The resistance **must** be 100k ohms or more.

Measure the resistance from switch terminal 6 to all other terminals. The resistance **must** be 100k ohms or more.

If the multimeter does **not** show the correct values, the switch has failed. Verify the switch type and terminal location numbers. Refer to the OEM troubleshooting and repair manual for switch replacement procedures, and to verify the switch type and terminal location.

![[19400287.png]]
