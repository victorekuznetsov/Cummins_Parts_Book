---
aliases:
  - "Цепь датчика-реле давления кондиционера"
type: "Процедура"
doc: "99-019-262"
title_en: "Air Conditioning Pressure Switch Circuit"
title_ru: "Цепь датчика-реле давления кондиционера"
modified: "2015-06-29"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-262.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-262.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Air Conditioning Pressure Switch Circuit
**Цепь датчика-реле давления кондиционера**

> [!abstract] Процедура · `99-019-262`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-262.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-262.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram. Insert one of the test leads into the switch return of the OEM harness connector and connect the alligator clip to the multimeter probe. Insert the other lead into the air conditioning pressure switch signal pin of the harness connector and connect the alligator clip to the other multimeter probe.

When the system head pressure is low, the multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect the switch return and the air conditioning pressure switch signal wire for an open circuit, provided that the switch has been previously checked. Refer to the OEM troubleshooting and repair manual for repair procedures. If the resistance is within the specification, the switch return and the air conditioning pressure switch wire **must** be checked for a short circuit to ground, a short circuit from pin-to-pin, and a short circuit to an external voltage source.

![[19c01194.png]]

### Check for Short Circuit to Ground

To isolate the air conditioning switch circuit when checking for an electrical short, disconnect the OEM harness engine interface connector.

Adjust the multimeter to measure resistance. When the system head pressure is low, insert a test lead into the air conditioning pressure switch signal pin of the OEM harness connector and connect it to a multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the air conditioning switch circuit, provided that the switch has been previously checked. Repair or replace the wire connected to the air conditioning pressure switch signal pin in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].

![[19c01241.png]]

### Check for Short Circuit from Pin to Pin

Check for a short circuit from pin-to-pin. Isolate the air conditioning circuit by removing the OEM harness from the ECM. Insert the lead into the air conditioning pressure switch signal pin. Connect the alligator clip to the multimeter. With the other lead inserted into the switch return pin, measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

Allow the head pressure to drop and remove the lead from the air conditioning pressure switch signal pin and check all other pins. When the system head pressure is low, measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit between the air conditioning pressure circuit and any pin that shows a closed circuit. Repair or replace the wires in the engine harness. Refer to Procedure 019-043. Repair or replace the wires in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].

![[19c01194.png]]

### Check for Short Circuit to External Voltage Source

Turn the keyswitch to the ON position. When the system head pressure is low, adjust the multimeter to measure VDC. Insert a test lead into the air conditioning pressure switch signal pin of the OEM connector and attach it to a multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the voltage. The voltage **must** be 1.5 VDC or less. If the voltage is **not** correct, there is an external voltage source connected to the circuit, or there is a short circuit between the air conditioning pressure switch circuit and a wire carrying power in the engine or OEM harness. Remove the voltage source, or repair or replace the wiring in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]]. Remove the voltage source or repair or replace the wires in the engine harness. Connect all components after completing the repair.

> [!note] Note · Примечание
> If the air conditioning pressure switch circuit was approved in all of the previous tests, it is functioning properly.

![[19c01266.png]]
