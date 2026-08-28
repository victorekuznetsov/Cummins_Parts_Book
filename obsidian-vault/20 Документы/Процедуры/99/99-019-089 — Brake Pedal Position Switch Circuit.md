---
aliases:
  - "Цепь выключателя положения педали тормоза"
type: "Процедура"
doc: "99-019-089"
title_en: "Brake Pedal Position Switch Circuit"
title_ru: "Цепь выключателя положения педали тормоза"
modified: "2015-06-25"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-089.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-089.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Brake Pedal Position Switch Circuit
**Цепь выключателя положения педали тормоза**

> [!abstract] Процедура · `99-019-089`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-089.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-089.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

If electronic service tool is available, monitor the brake pedal position switch for proper operation. If **not**, follow the troubleshooting procedures in this section.

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.

![[19803969.png]]

Make sure the brake pedal position switch is connected to the circuit.

Insert a test lead into the brake pedal position switch signal pin of the OEM harness connector. Attach the lead to a multimeter probe. Insert the other test lead into the switch return pin of the connector and attach it to the other probe.

Adjust the multimeter to the resistance setting and measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less) when the brakes are **not** engaged (brake pedal released). If the circuit is **not** closed, there is a problem with the OEM harness, provided the brake pedal position switch has been previously checked.

![[19c01262.png]]

> [!warning] CAUTION · Осторожно
> The vehicle must have enough air pressure to activate the brakes.

Depress the vehicle brake pedal and repeat the resistance check. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a problem with the OEM harness, provided the brake pedal position switch has been previously checked.

If the values are correct, the circuit **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.

![[19c01263.png]]

### Check for Short Circuit to Ground

To isolate the brake pedal position switch circuit when checking for a short circuit, turn all cab panel switches to the OFF or neutral position.

Disconnect the OEM harness connector from the ECM and the OEM harness from the brake pedal position switch.

Set the service brake using the trailer brake hand valve.

Disconnect the clutch pedal position switch, accelerator position switch and the idle validation on/off switch.

![[19200292.png]]

Insert a test lead into the brake pedal position switch signal pin of the OEM harness connector. Connect the lead to the multimeter probe. Remove the alligator clip from the other multimeter probe and touch the probe to the engine block.

The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the brake pedal position switch signal wire, provided that the switch has been previously checked.

Repair or replace the wire connected to the brake pedal position switch signal pin in the OEM harness according to the vehicle manufacturer's procedures.

Measure the resistance.

![[19c01241.png]]

### Check for Short Circuit from Pin to Pin

Isolate the brake pedal position switch circuit by disconnecting the brake pedal position switch connector and the OEM harness connector at the ECM. Insert a test lead into the brake pedal position switch signal pin of the OEM harness connector. Insert the other test lead into the switch return pin of the OEM harness connector. Connect the alligator clips to the multimeter probes. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

Remove the lead from the switch return pin and test all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more) at all pins. If the circuit is **not** open, there is a short circuit between the wire connected to the service brake switch signal pin and any pin that did **not** show an open circuit.

Repair or replace the wires in the OEM harness according to the vehicle manufacturer's procedures.

![[19c01155.png]]

### Check for Short Circuit to External Voltage Source

Disconnect the brake pedal position switch from the OEM harness and disconnect the OEM harness from the ECM. Turn the vehicle keyswitch to the ON position. Adjust the multimeter to measure VDC. Insert a test lead into the brake pedal position switch signal pin and connect it to the positive multimeter probe. Remove the lead from the negative multimeter probe and touch the probe to the engine block ground. Measure the voltage. The voltage **must** be 1.5 VDC or less.

> [!note] Note · Примечание
> An external voltage source is any wire in the OEM wiring that carries voltage.

If the voltage is more than 1.5 VDC, there is a short circuit between the wire connected to the brake pedal position switch signal pin and a wire carrying power in the OEM harness. Repair the OEM harness according to the vehicle manufacturer's procedures.

Connect all components after completing the repair.

![[19c01266.png]]
