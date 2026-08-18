---
aliases:
  - "Цепь выключателя управления вентилятором"
type: "Процедура"
doc: "99-019-381"
title_en: "Fan Control Switch Circuit"
title_ru: "Цепь выключателя управления вентилятором"
modified: "2015-06-25"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 7
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-381.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-381.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Fan Control Switch Circuit
**Цепь выключателя управления вентилятором**

> [!abstract] Процедура · `99-019-381`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-381.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-381.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

If electronic service tool is available, monitor the fan control switch circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.

![[19803969.png]]

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram. Insert one of the test leads into the switch return pin of the OEM harness connector and connect the alligator clip to the multimeter probe. Insert the other lead into the fan control switch signal pin of the OEM harness connector and connect the alligator clip to the other multimeter probe.

Move the fan control switch to the OFF position. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect the fan control switch, switch return wire, and the fan control switch signal wire for an open circuit, provided that the switch has been previously checked. Refer to the OEM troubleshooting and repair manual for repair procedures. If the resistance is within the specification, the fan control switch, switch return (-) wire, and the fan control signal wire **must** be checked for a short circuit to ground, a short circuit from pin-to-pin, and a short circuit to an external voltage source.

![[19c01194.png]]

### Check for Short Circuit to Ground

To isolate the fan control switch circuit when checking for an electrical short, disconnect the OEM harness from the ECM and fan control switch. Disconnect the clutch position switch/engine protection override switch and the accelerator pedal assembly. Set all cab panel switches to the OFF or neutral position. Set the service brake using the trailer brake hand valve.

![[19200292.png]]

Adjust the multimeter to measure resistance. Insert a test lead into the fan control switch signal pin of the OEM harness connector and connect it to a multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the fan switch control circuit, provided that the switch has been previously checked. Repair or replace the wire connected to the fan control switch signal in the OEM harness according to the vehicle manufacturer's procedure.

![[19c01241.png]]

### Check for Short Circuit from Pin to Pin

Isolate the fan control switch circuit by setting the switches as in the previous section. Set the fan control switch to the ON position. Insert the lead into the fan control switch signal pin. Connect the alligator clip to the multimeter. With the other lead inserted into the switch return pin, measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

Remove the lead from the fan control switch signal pin and check all other pins. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit between the fan control switch circuit and any pin that shows a closed circuit, provided the switch has previously been checked. Repair or replace the wires in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].

![[19c01236.png]]

### Check for Short Circuit to External Voltage Source

Turn the keyswitch to the ON position. Set the fan control switch to OFF. Adjust the multimeter to measure VDC. Insert a test lead into the fan control switch signal pin and attach it to a multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the voltage. The voltage **must** be 1.5 VDC or less.

![[19c01266.png]]

If the voltage is **not** correct, there is an external voltage source connected to the circuit, or there is a short circuit between the fan control switch circuit and a wire carrying power in the OEM harness. Remove the voltage source or repair the wiring in the OEM harness according to the vehicle manufacturer's procedures.

Connect all components after completing the repair.

> [!note] Note · Примечание
> If the fan control switch circuit was approved in all of the previous tests, it is functioning correctly.

![[19c01181.png]]
