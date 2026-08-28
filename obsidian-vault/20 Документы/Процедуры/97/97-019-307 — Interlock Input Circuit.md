---
aliases:
  - "Цепь входа блокировки"
type: "Процедура"
doc: "97-019-307"
title_en: "Interlock Input Circuit"
title_ru: "Цепь входа блокировки"
modified: "2003-06-13"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 67
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-307.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-307.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Interlock Input Circuit
**Цепь входа блокировки**

> [!abstract] Процедура · `97-019-307`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-307.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-307.pdf)

### Resistance Check

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the ICON™ idle control module A and B connectors.

Disconnect the parking brake switch from the cab harness.

Disconnect the ICON™ lamp from the cab harness.

Set the multimeter to measure resistance.

![[19802893.png]]

Check the interlock output circuit.

Touch one of the multimeter leads to pin 5 of the ICON™ idle control module A harness connector. Touch the other multimeter lead to pin B of the parking brake switch harness connector.

Read the value displayed on the multimeter.

Remove the lead from pin B of the parking brake switch harness connector. Touch the multimeter lead to pin B of the ICON™ lamp harness connector.

Read the value displayed on the multimeter.

![[19802894.png]]

Finally, touch one of the multimeter leads to pin 6 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to pin A of the ICON™ lamp harness connector.

Read the value displayed on the multimeter.

![[19802894.png]]

For all three pin checks, the multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If any of the circuits are **not** closed, isolate the problem to the cab harness or ICON™ engine harness side of the circuit. If the circuit is closed, check the interlock input circuit.

![[19801619.png]]

Check the interlock input circuit.

Make sure that the hood tilt and neutral position switches are closed.

Touch one of the multimeter leads to pin 3 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to pin A of the parking brake switch harness connector.

Read the value displayed on the multimeter.

![[19802894.png]]

Then, with one lead still touching pin A of the parking brake switch harness connector, touch the other multimeter lead to pin 2 of the ICON™ idle control module B harness connector.

Read the value displayed on the multimeter.

![[19802895.png]]

For both pin checks, the multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If either circuit is **not** closed, isolate the problem to the cab harness or ICON™ engine harness side of the circuit.

![[19801619.png]]

Check the output wire on the cab harness side.

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Touch one of the multimeter leads to pin J of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to pin B of the parking brake switch harness connector.

Read the value displayed on the multimeter.

![[19c00931.png]]

Then, with one lead still touching to pin J of the 14-pin connector, cab harness side, touch the second multimeter lead to pin B of the ICON™ lamp harness connector.

Read the value displayed on the multimeter.

![[19c00931.png]]

For both pin checks, the multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If either circuit is **not** closed, repair or replace the cab harness. Refer to Procedure 019-202, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].

If both circuits are closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-202, 019-208, or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Touch one multimeter lead to pin D of the 14-pin pass-through connector, cab harness side.

Touch the other multimeter lead to pin A of the ICON™ lamp harness connector.

Read the value displayed on the multimeter.

![[19c00931.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure 019-202, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].

If the circuit is closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-202, 019-208, or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Check the input wire on the cab harness side.

Touch one of the multimeter leads to pin K of the 14-pin pass-through connector, cab harness side.

Touch the other multimeter lead to pin A of the parking brake switch harness connector.

Read the value displayed on the multimeter.

![[19c00931.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure 019-202, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].

If the circuit is closed, isolate the problem to the correct portion of the ICON™ engine harness.

![[19801619.png]]

Touch one of the multimeter leads to pin K of the 14-pin pass-through connector, engine harness side.

Touch the other multimeter lead to pin 3 of the ICON™ idle control module A harness connector.

Read the value displayed on the multimeter.

![[19c00930.png]]

Then, leaving the first lead in place on pin K of the 14-pin connector, touch the second multimeter lead to pin 2 of the ICON™ idle control module B harness connector.

Read the value displayed on the multimeter.

![[19802896.png]]

For both pin checks, the multimeter **must** display a reading of less than 10 ohms (closed circuit).

If the circuit is **not** closed, check the portion of the circuit to the neutral position switch.

![[19801619.png]]

First, verify that the neutral position switch is good. Replace neutral position switch as required.

Disconnect the neutral position switch from the ICON™ engine harness.

Touch one of the multimeter leads to pin K of the 14-pin pass-through connector, engine harness side. Touch the other multimeter lead to pin B of the neutral position switch harness connector.

Read the value displayed on the multimeter.

![[19802897.png]]

The multimeter **must** display a reading of less than 10 ohms (closed circuit).

If the circuit is **not** closed, repair or replace the ICON™ engine harness.

Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Disconnect the hood tilt switch from the ICON™ engine harness.

Touch one of the multimeter leads to pin A of the neutral position switch harness connector.

Touch the other multimeter lead to pin B of the hood tilt switch harness connector.

Read the value displayed on the multimeter.

![[19802898.png]]

The multimeter **must** display a reading of less than 10 ohms (closed circuit).

If the circuit is **not** closed, repair or replace the ICON™ engine harness.

Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Verify that the hood tilt switch is good.

Touch one of the multimeter leads to pin A of the hood tilt switch harness connector.

Touch the other multimeter lead to pin 3 of the ICON™ idle control module A harness connector.

Read the value displayed on the multimeter.

![[19802894.png]]

The multimeter **must** display a reading of less than 10 ohms (closed circuit).

If the circuit is **not** closed, repair or replace the ICON™ engine harness.

Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19801619.png]]

### Check for Short Circuit to Ground

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part No 3822758 and 3822917, when taking a measurement.

Disconnect the ICON™ idle control module A and B connectors.

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Disconnect the parking brake switch and the ICON™ lamp from the cab harness.

Disconnect the neutral position switch and hood tilt switch from the ICON™ engine harness.

Set the multimeter to measure resistance.

![[19802893.png]]

Touch one of the multimeter leads to pin B of the ICON™ lamp harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin A of the ICON™ lamp harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802899.png]]

For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit to ground.

Isolate the short to the cab harness or engine harness portion of the circuit.

![[19801621.png]]

Touch one of the multimeter leads to pin B of the parking brake switch harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin A of the parking brake switch harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802899.png]]

For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit to ground.

Isolate the short to the cab harness or engine harness portion of the circuit.

![[19801621.png]]

Touch one of the multimeter leads to pin J of the 14-pin pass-through connector, engine harness side. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin D of the 14-pin pass-through connector, engine harness side. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.

![[19c00940.png]]

For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If either circuit is **not** open, check for a short circuit from the appropriate idle control module harness connector pin.

If either circuit is open, repair or replace the cab harness. Refer to Procedure 019-202, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Touch one of the multimeter leads to pin K of the 14-pin pass-through connector, engine harness side.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00940.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, isolate the short to either idle control module connector.

If the circuit is open, repair or replace the cab harness. Refer to Procedure 019-202, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Touch one of the multimeter leads to pin 5 of the ICON™ idle control module A harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin 6 of the ICON™ idle control module A harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00932.png]]

For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If either circuit is **not** open, repair or replace the ICON™ engine harness.

Refer to Procedure 019-208 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin 2 of the ICON™ idle control module B harness connector.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802900.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, repair or replace the ICON™ engine harness.

Refer to Procedure 019-208 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin A of the neutral position switch harness connector. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin B of the neutral position switch harness connector. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.

![[19802899.png]]

For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If either circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin A of the hood tilt switch harness connector. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin B of the hood tilt switch harness connector. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.

![[19802899.png]]

For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If either check is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin 3 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00932.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If either circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit from Pin to Pin

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part No 3822758 and 3822917, when taking a measurement.

Disconnect the ICON™ idle control module A and B connectors. Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Disconnect the parking brake switch and the ICON™ lamp from the cab harness.

Disconnect the neutral position switch and the hood tilt switch from the ICON™ engine harness.

Set the multimeter to measure resistance.

![[19802893.png]]

Touch one of the multimeter leads to pin A of the parking brake switch harness connector.

Touch the other multimeter lead to pin B of the harness connector.

Read the value displayed on the multimeter.

![[19802901.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between pin A and pin B.

Repair or replace the cab harness. Refer to Procedure 019-202 or [[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Touch one of the multimeter leads to pin A of the ICON™ lamp harness connector.

Touch the other multimeter lead to pin B of the harness connector.

Read the value displayed on the multimeter.

![[19802901.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between pin A and pin B.

Repair or replace the cab harness. Refer to Procedure 019-202 or [[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Touch one of the multimeter leads to pin J of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to all other pins in the connector, one at a time.

Repeat the pin-to-pin check from pin D of the 14-pin connector, cab harness side, to all other pins in the connector, and from pin K to all other pins.

Read the value displayed on the multimeter.

![[19c00935.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit from pin J, pin D, or pin K to any other pin in the connector that registered a closed circuit.

Repair or replace the cab harness. Refer to Procedure 019-200 or [[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Touch one of the multimeter leads to pin J of the 14-pin pass-through connector, engine harness side. Touch the other multimeter lead to all other pins in the connector, one at a time.

Repeat the pin-to-pin check from pin D of the 14-pin connector, engine harness side, to all other pins in the connector, and from pin K to all other pins.

Read the value displayed on the multimeter.

![[19c00942.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit from pin J, pin D, or pin K in the 14-pin pass-through connector to any other pin in the connector that registered a closed circuit.

Repair or replace the ICON™ engine harness. Refer to Procedure 019-200 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin 3 of the ICON™ idle control module A harness connector. Touch the other multimeter lead to all other pins in the connector, one at a time.

Repeat the pin-to-pin check from pin 5 of the ICON™ idle control module A harness connector to all other pins in the connector, and from pin 6 to all other pins.

Read the value displayed on the multimeter.

![[19c00943.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit from pin 3, pin 5, or pin 6 in the ICON™ idle control module A connector to any other pin in the connector that registered a closed circuit.

Repair or replace the ICON™ engine harness. Refer to Procedure 019-208 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin 2 of the ICON™ idle control module B harness connector.

Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

![[19c00962.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit from pin 2 in the ICON™ idle control module B connector to any other pin in the connector that registered a closed circuit.

Repair or replace the ICON™ engine harness. Refer to Procedure 019-208 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin A of the neutral position switch harness connector.

Touch the other multimeter lead to pin B of the connector.

Read the value displayed on the multimeter.

![[19802901.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit from pin A to pin B in the neutral position switch harness connector.

Repair or replace the ICON™ engine harness. Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin A of the hood tilt switch harness connector.

Touch the other multimeter lead to pin B of the connector.

Read the value displayed on the multimeter.

![[19802901.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit from pin A to pin B in the hood tilt switch harness connector.

Repair or replace the ICON™ engine harness. Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit to External Voltage Source

Disconnect the ICON™ idle control module A and B connectors.

Disconnect the ICON™ lamp and the parking brake switch from the cab harness.

Set the multimeter to measure VDC.

Turn the keyswitch to the ON position.

![[19802893.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.

Touch one of the multimeter leads to pin A of the ICON™ lamp harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin B of the ICON™ lamp harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802899.png]]

For both pin-to-ground checks, the multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the cab or engine harness wiring that carries voltage.

Remove the external voltage source.

![[19c00963.png]]

Touch one of the multimeter leads to pin A of the parking brake switch harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin B of the parking brake switch harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802899.png]]

For both pin-to-ground checks, the multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the cab or engine harness wiring that carries voltage.

Remove the external voltage source.

Connect all components after completing the repair.

![[19c00963.png]]
