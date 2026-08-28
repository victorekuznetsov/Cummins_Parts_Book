---
aliases:
  - "Цепь выключателя моторного тормоза"
type: "Процедура"
doc: "99-019-035"
title_en: "Engine Brake ON/OFF Switch Circuit"
title_ru: "Цепь выключателя моторного тормоза"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-035.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-035.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Engine Brake ON/OFF Switch Circuit
**Цепь выключателя моторного тормоза**

> [!abstract] Процедура · `99-019-035`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-035.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-035.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

If electronic service tool is available, monitor the engine brake switch circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.

Insert one of the test leads into the switch return of the OEM harness connector and connect the alligator clip to the multimeter probe. Insert the other lead into engine brake selector signal number 1 of the OEM harness connector and connect the alligator clip to the other multimeter probe.

![[19803969.png]]

Move the engine brake ON/OFF switch to the ON position. Move the engine brake level switch to position number 1 for a six-position switch or to position number 2 for a three-position switch. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect the switch return and engine brake selector signal number 1 for an open circuit, provided that the switch has been previously checked. Refer to the OEM troubleshooting and repair manual for repair procedures. If the resistance is within the specification, the switch return and engine brake selector signal number 1 **must** be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.

Remove the lead from engine brake selector signal number 1 and insert it into engine brake selector signal number 2 of the OEM harness connector.

Move the engine brake ON/OFF switch to the ON position. Move the engine brake level switch to position number 2 for a six-position switch or to position number 1 for a three-position switch.

The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect engine brake selector signal number 2 wire for an open circuit, provided that the switch has been previously checked. Refer to the OEM troubleshooting and repair manual for repair procedures.

If the resistance is within the specification, engine brake selector signal number 2 wire **must** be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.

Remove the lead from engine brake selector signal number 2 and insert it into engine brake selector signal number 3 of the OEM harness.

Move the engine brake ON/OFF switch to the ON position. Move engine brake level switch to position number 3.

The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect the engine brake selector signal number 3 wire for an open circuit, provided that the switch has been previously checked. Refer to the OEM troubleshooting and repair manual for repair procedures.

If the resistance is within the specification, the engine brake selector signal number 3 wire **must** be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.

Connect all components after completing the repair.

![[19c01194.png]]

### Check for Short Circuit to Ground

To isolate the engine brake circuit when checking for an electrical short, turn all cab panel switches to the OFF or neutral position.

![[19200292.png]]

Move the engine brake level switch to position number 1 for a six-position switch or position number 2 for a three-position switch.

Insert a test lead into engine brake selector signal number 1 pin of the OEM harness connector and connect it to a multimeter probe.

Touch the other multimeter probe to the engine block ground.

Switch the engine brake ON/OFF switch to the OFF position.

Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the engine brake circuit, provided the engine brake ON/OFF switch and engine brake selector switch have been previously checked.

Repair or replace the wire connected to the switch return or engine brake selector signal number pin 1 in the OEM harness connector according to the vehicle manufacturer's procedures.

Remove the lead from engine brake selector signal number 1 pin and insert it into engine brake selector signal number 2 pin of the OEM harness connector.

Move engine brake level switch to position number 2 for a six-position switch or to position number 1 for a three-position switch.

Switch the engine brake ON/OFF switch to OFF.

Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the engine brake circuit, provided the engine brake ON/OFF switch has been previously checked.

Repair or replace the wire connected to engine brake selector signal number 2 pin in the OEM harness according to the vehicle manufacturer's procedures.

![[19c01222.png]]

Remove the lead from engine brake selector signal number 2 pin and insert it into engine brake selector signal number 3 pin of the OEM harness connector.

Move engine brake level switch to position number 3.

Switch the engine brake ON/OFF switch to the OFF position.

Measure the resistance with the multimeter.

The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the engine brake circuit, provided the engine brake ON/OFF switch has been previously checked.

Repair or replace the wire connected to engine brake selector signal number 3 pin in the OEM harness according to the vehicle manufacturer's procedures.

![[19c01211.png]]

### Check for Short Circuit from Pin to Pin

Isolate the circuit by setting the cab panel switches as described in the previous section. Set the engine brake ON/OFF switch to the ON position. Place engine brake level to position number 6 for a six-position switch or position number 3 for a three-position switch.

Insert a test lead into the switch return of the OEM harness connector and check all pins except the switch return, engine brake selector signal number 1 pin, and engine brake selector signal number 3 pin.

Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

Remove the lead from the switch return and insert it into engine brake selector signal number 2 pin. Check all pins except the switch return engine, brake selector signal number 1 pin and engine brake selector signal number 3 pin. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

Remove the lead from engine brake selector signal number 2 pin and insert it into engine brake selector signal number 3 pin. Check all pins except the switch return. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

Remove the lead from the engine brake selector signal number 3 pin and inert it in the engine brake selector signal number 1 pin. Check all pins except the switch return. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19c01155.png]]

### Check for Short Circuit to External Voltage Source

Turn the vehicle keyswitch to the ON position. Set the engine brake ON/OFF switch to the ON position.

Adjust the multimeter to measure the VDC.

Insert a test lead into the switch signal pin of the OEM harness connector.

Disconnect the multimeter probe from the test lead and touch it to the engine block ground. Measure the voltage. The voltage **must** be 1.5 VDC or less.

If the voltage is **not** correct, there is an external voltage source connected to the circuit, or there is a short circuit between the engine brake on/off circuit and a wire carrying power in the OEM harness. Remove the voltage source or repair the wiring in the OEM harness according to the vehicle manufacturer's procedures.

Connect all components after completing the repair.

![[19c01189.png]]
