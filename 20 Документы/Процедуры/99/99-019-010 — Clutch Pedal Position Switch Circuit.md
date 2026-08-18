---
aliases:
  - "Цепь выключателя положения педали сцепления"
type: "Процедура"
doc: "99-019-010"
title_en: "Clutch Pedal Position Switch Circuit"
title_ru: "Цепь выключателя положения педали сцепления"
modified: "2015-06-22"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 8
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-010.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-010.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Clutch Pedal Position Switch Circuit
**Цепь выключателя положения педали сцепления**

> [!abstract] Процедура · `99-019-010`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-010.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-010.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

If electronic service tool is available, monitor the clutch pedal position switch circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.

Insert a test lead into the clutch pedal position switch return pin depending on the OEM application of the OEM connector. Insert the other test lead into the clutch pedal position switch signal pin of the OEM connector.

![[19803969.png]]

Connect the alligator clips to the two probes of the multimeter. Adjust the multimeter to measure resistance.

The multimeter **must** show a closed circuit (10 ohms or less) when the clutch pedal (1) is released.

![[19c01151.png]]

Depress the clutch pedal (1). The multimeter **must** show an open circuit (100k ohms or more). If the resistance values are **not** correct, the clutch pedal position switch signal wire and the return wire **must** be checked for an open circuit, provided the clutch pedal position switch was previously checked.

If the values are correct, the circuit **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.

![[19c01152.png]]

### Check for Short Circuit to Ground

To isolate the clutch pedal position switch circuit when checking for a short circuit to ground, turn all cab panel switches to the OFF or neutral position.

Set the service brake using the trailer brake hand valve.

Disconnect the clutch pedal position switch, the idle validation switch, and the throttle pedal.

![[ee8swsb.png]]

Remove the test lead from the switch return pin.

Disconnect the multimeter probe from the alligator clip.

![[19c01153.png]]

Touch the other multimeter probe to the engine block ground. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the clutch pedal position switch circuit.

Repair or replace the wire connected to the clutch pedal position switch signal pin in the OEM harness according to the vehicle manufacturer's procedures.

Connect all components when the repair is complete.

![[19c01154.png]]

### Check for Short Circuit from Pin to Pin

Isolate the clutch pedal position switch circuit as described in previous step. Set all cab panel switches to the OFF or neutral position, and disconnect the clutch pedal position switch and the throttle pedal.

Adjust the multimeter to measure resistance. Then insert one test lead into the clutch pedal position switch signal pin of the OEM harness connector. Insert the other test lead into the clutch pedal position switch return pin. Connect the alligator clips to the multimeter probes.

Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

With the first test lead still touching the clutch pedal position switch signal pin, remove the test lead from the clutch pedal position switch return pin and touch it to all other pins, one at a time. The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the circuit is **not** open, there is a short circuit between the wire connected to the clutch pedal position switch signal pin and any pin that shows a closed circuit. Repair or replace the wires in the OEM harness according to the vehicle manufacturer's procedures.

Remove the test lead from the clutch pedal position switch signal pin and touch it to the clutch pedal position switch return pin. Touch the other test lead to all other pins, one at a time. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more), except for the clutch pedal position switch return pin.

If the circuit is **not** open, there is a short circuit between the wire connected to the clutch pedal position switch return wire and any pin that measured a closed circuit. Repair or replace the wires in the OEM harness according to the vehicle manufacturer's procedures.

![[19c01155.png]]

### Check for Short Circuit to External Voltage Source

Isolate the clutch pedal position switch circuit as described in the previous steps. Set the cab panel switches to the OFF or neutral position, and disconnect the clutch pedal position switch and the throttle pedal. Turn the keyswitch to the ON position. Adjust the multimeter to measure VDC.

Insert test lead connected to the positive multimeter probe into the clutch pedal position switch signal pin. Disconnect the negative multimeter probe from the test lead and touch it to the engine block ground. Measure the voltage. The voltage **must** be 1.5 VDC or less.

> [!note] Note · Примечание
> An external voltage source is any wire in the OEM wiring that carries voltage.

If the voltage value is more than 1.5 VDC, there is a short circuit between the wire connected to the clutch pedal position switch signal pin and a wire carrying power in the OEM harness. Repair the OEM harness according to the vehicle manufacturer's procedures.

Remove the test lead from clutch pedal position switch signal pin and insert it into the clutch pedal position switch return pin. With the multimeter probe still touching the engine block ground, measure the voltage. The voltage **must** be 1.5 VDC or less. If the voltage value is **not** correct, there is a short circuit between the wire connected to the clutch pedal position switch return and a wire carrying power in the OEM harness. Repair the OEM harness according to the vehicle manufacturer's procedures.

Connect all components after completing the repairs.

![[19c01158.png]]
