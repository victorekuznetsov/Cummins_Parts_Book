---
aliases:
  - "Цепь выключателя круиз-контроля или отбора мощности"
type: "Процедура"
doc: "99-019-022"
title_en: "Cruise Control or PTO ON/OFF Switch Circuit"
title_ru: "Цепь выключателя круиз-контроля или отбора мощности"
modified: "2015-06-25"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 8
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-022.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-022.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Cruise Control or PTO ON/OFF Switch Circuit
**Цепь выключателя круиз-контроля или отбора мощности**

> [!abstract] Процедура · `99-019-022`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-022.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-022.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

If electronic service tool is available, monitor the switch circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.

![[19803969.png]]

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.

Insert the test lead into the cruise control ON/OFF switch signal pin of the original equipment manufacturer (OEM) harness connector and attach it to the multimeter probe. Touch the other probe to the engine block ground.

![[19c01166.png]]

Move the ON/OFF switch to the ON position. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect the cruise control ON/OFF switch input for an open circuit. Refer to the OEM troubleshooting and repair manual.

If the resistance is within specification, the cruise control ON/OFF switch input **must** be checked for a short circuit to ground, a short circuit from terminal to terminal, and a short circuit to an external voltage source.

![[19c01167.png]]

### Check for Short Circuit to Ground

To isolate the cruise control circuit when checking for a short circuit, disconnect the OEM harness connector from the ECM and the OEM harness from the cruise control switch.

Disconnect the clutch pedal position switch, idle validation on/off switch, and the accelerator pedal position switch. Set all cab panel switches to the OFF or neutral position.

Set the service brake using the trailer brake hand valve.

![[19200292.png]]

Adjust the multimeter to measure resistance. Insert a test lead into the cruise control ON/OFF switch input of the OEM harness connector and attach it to a multimeter probe. Remove the other multimeter probe from the alligator clip and touch it to the engine block ground.

Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the cruise control circuit, provided that the switch has been previously checked.

Repair or replace the wire connected to the cruise control ON/OFF switch input in the OEM harness according to the vehicle manufacturer's procedures.

![[19c01166.png]]

### Check for Short Circuit from Pin to Pin

Check for a short circuit from pin-to-pin. Isolate the cruise control circuit by setting the switches as in the previous section. Set the cruise control/PTO ON/OFF switch to the OFF position. Insert the lead into the cruise control ON/OFF switch input. Connect the alligator clip to the multimeter. With the other lead inserted into the switch return wire(s), measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19c01168.png]]

Remove the lead from the cruise control ON/OFF switch input and check all other pins. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, there is a short circuit between the cruise control ON/OFF switch input circuit and any pin that shows a closed circuit, provided the switch has previously been checked.

Repair or replace the wires in the OEM harness according to the vehicle manufacturer's procedures.

![[19c01155.png]]

### Check for Short Circuit to External Voltage Source

Turn the vehicle keyswitch to the ON position. Set the cruise control/PTO ON/OFF switch to ON. Adjust the multimeter to measure VDC. Insert a test lead into the cruise control ON/OFF switch input and attach it to a multimeter probe. Disconnect the other multimeter probe from the other lead and touch it to the engine block ground. Measure the voltage. The voltage **must** be 1.5 VDC or less.

If the voltage is **not** correct, there is an external voltage source connected to the circuit, or there is a short circuit between the cruise control/PTO ON/OFF switch circuit and a wire carrying power in the OEM harness. Remove the voltage source or repair the wiring in the OEM harness according to the vehicle manufacturer's procedures. Connect all components after completing the repair.

> [!note] Note · Примечание
> If the cruise control/PTO ON/OFF switch circuit was approved in all of the previous tests, it is functioning correctly.

![[19c01169.png]]
