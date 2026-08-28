---
aliases:
  - "Цепь реле зажигания"
type: "Процедура"
doc: "97-019-308"
title_en: "Ignition Relay Circuit"
title_ru: "Цепь реле зажигания"
modified: "2004-10-14"
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
figures: 40
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-308.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-308.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Ignition Relay Circuit
**Цепь реле зажигания**

> [!abstract] Процедура · `97-019-308`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-10-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-308.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-308.pdf)

### Resistance Check

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

Disconnect the ignition bus relay from the ICON™ cab wiring harness.

Measure the resistance from pin 85 to pin 86 on the relay.

Read the value displayed on the multimeter. The multimeter **must** display a reading of 70 to 100 ohms.

Measure the resistance from pin 85 of the ignition bus relay(s) to pin 30, 87, and 87A.

Read the value displayed on the multimeter. The multimeter **must** display a reading of more than 100k ohms (open circuit).

![[19803846.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the ICON™ idle control module B connector.

Disconnect the 14-pin pass through connector at the vehicle's firewall.

Disconnect the ignition bus relay from the cab harness.

Set the multimeter to measure resistance.

![[19c00961.png]]

Check the output wire.

Touch one of the multimeter leads to pin 4 of the ICON™ idle control module B harness connector.

Touch the other multimeter lead to pin F of the 14-pin pass-through connector, engine harness side.

Read the value displayed on the multimeter.

![[19c00955.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]] or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, cab harness side.

Touch the other multimeter lead to pin 85 of the ignition bus relay harness connector.

Read the value displayed on the multimeter.

![[19802925.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-305 — Cab Wiring Harness|019-305]].

![[19801619.png]]

Check the return wire.

Touch one of the multimeter leads to pin C of the 14-pin pass-through connector, engine harness side.

Touch the other multimeter lead to the negative (-) battery terminal post.

Read the value displayed on the multimeter.

![[19802926.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-197 — Ring Terminal|019-197]] or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Touch one of the multimeter leads to pin C of the 14-pin pass-through connector, cab harness side.

Touch the other multimeter lead to pin 86 of the ignition bus relay harness connector.

Read the value displayed on the multimeter.

![[19802925.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-305 — Cab Wiring Harness|019-305]].

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
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the ICON™ idle control module B connector.

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Disconnect the ignition bus relay from the cab harness.

Set the multimeter to measure resistance.

![[19c00961.png]]

Touch one of the multimeter leads to pin 4 of the ICON™ idle control module B harness connector.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802900.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]] or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, ICON™ engine harness side.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00940.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, cab harness side.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00933.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure [[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Touch one of the multimeter leads to pin 86 of the ignition bus relay harness connector.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802927.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, repair or replace the cab harness. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-305 — Cab Wiring Harness|019-305]].

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
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the ICON™ idle control module A and B connectors.

Disconnect the 14-pin pass through connector at the vehicle's firewall.

Disconnect the ignition bus relay from the cab harness.

Set the multimeter to measure resistance.

![[19c00917.png]]

Touch one of the multimeter leads to pin 4 of the ICON™ idle control module B harness connector. Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

![[19c00962.png]]

Then, touch one of the multimeter leads to pin 2 of the ICON™ idle control module A harness connector. Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

![[19c00943.png]]

For both pin-to-pin checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]] or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, ICON™ engine harness side. Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

Repeat the pin-to-pin check from pin C. Touch one of the multimeter leads to pin C of the 14-pin pass-through connector, ICON™ engine harness side. Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

![[19c00942.png]]

For both pin-to-pin checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

Repeat the pin-to-pin check from pin C. Touch one of the multimeter leads to pin C of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

![[19c00935.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure [[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Touch one of the multimeter leads to pin 86 of the ignition bus relay harness connector.

Touch the other multimeter lead to all other pins in the relay harness connector, one at a time

Read the value displayed on the multimeter.

![[19802885.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, repair or replace the cab harness. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-305 — Cab Wiring Harness|019-305]].

Connect all components after completing the repair.

![[19801621.png]]

### Voltage Check

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test lead, Part Number 3822917, when taking a measurement.

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Set the multimeter to measure VDC.

Turn the keyswitch to the ON position.

![[15800040.png]]

Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, cab harness side.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00935.png]]

The multimeter **must** display a reading of less than 0.5 VDC.

If the voltage is **not** less than 0.5 VDC, repair or replace the ignition bus relay. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-301 — Ignition Bus Relay 1 and 2|019-301]].

Connect all components after completing the repair.

![[19c00954.png]]

### Check for Short Circuit to External Voltage Source

Turn the keyswitch to the OFF position. Disconnect the ICON™ idle control module B connector. Set the multimeter to measure VDC.

![[19c00961.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test lead, Part Number 3822917, when taking a measurement.

Turn the keyswitch to the ON position.

Touch one of the multimeter leads to pin 4 of the ICON™ idle control module B harness connector. Touch the other multimeter lead to ground.

Measure the voltage.

![[19802900.png]]

The multimeter **must** display a reading of less than 0.5 VDC.

If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the cab or engine harness that carries voltage.

Isolate the short to the proper portion of the circuit.

![[19c00954.png]]

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, cab harness side.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00933.png]]

The multimeter **must** display a reading of less than 0.5 VDC.

If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source on the cab harness side of the circuit.

If the VDC is less than 0.5 VDC, the short circuit is on the ICON™ engine harness side of the circuit.

Remove the external voltage source.

Connect all components after completing the repair.

![[19c00954.png]]
