---
aliases:
  - "Выключатель промежуточной частоты вращения"
type: "Процедура"
doc: "19-019-107"
title_en: "Intermediate Speed Control Switch"
title_ru: "Выключатель промежуточной частоты вращения"
modified: "2002-11-07"
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
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-107.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-107.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Intermediate Speed Control Switch
**Выключатель промежуточной частоты вращения**

> [!abstract] Процедура · `19-019-107`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-11-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-107.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-107.pdf)

### General Information

The intermediate speed control ON, OFF, and ON switch circuit signals the QSK system that the operator is requesting to go to one of two preset speeds between low idle and high idle. There is one three-position switch that selects ISC1, OFF, and ISC2.

![[19400281.png]]

The intermediate speed control circuit is shown for intermediate speed control 1 and intermediate speed control 2 features. The calibration can **only** have one intermediate speed control active feature. The intermediate speed control circuit is wired with a double pole, double throw (DPDT), three-position switch.

![[19400282.png]]

The DPDT three-position switch functions to selectively ground wires number 35 and 37, or wires number 38 and 37, or ground number wires. The logic of the switch is shown.

The lines that connect the switch terminals at the three lever positions are lines of continuity between the terminals.

In position 1, switch terminals number 2, 3 and 5, 6 are connected which shorts intermediate speed control 2 and intermediate speed control validation (pins 38 and 37) to ground.

In position 2, no pins are grounded.

In position 3, switch terminals number 1, 2 and 4, 5 are connected which shorts intermediate speed control 1 and intermediate speed control validation (pins 35 and 37) to ground.

![[19400283.png]]

### Initial Check

Connect an electronic service tool to the vehicle datalink.

Turn the keyswitch to the ON position.

Operate the intermediate speed control switch while monitoring with INSITE™. The INSITE™ reading should change with the switch position.

![[19900524.png]]

### Resistance Check

If INSITE™, Part Number 3824801, is available, monitor the intermediate speed control switch for proper operation. If **not**, follow the troubleshooting procedures in this section.

Remove the four connectors from the switch. Label the wires with the switch location and the wire numbers.

![[19400284.png]]

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

If the multimeter does **not** show the correct values, the switch has failed. Verify the switch type and terminal location numbers. Refer to the OEM repair manual for replacement and to verify the switch type and terminal location.

![[19400287.png]]
