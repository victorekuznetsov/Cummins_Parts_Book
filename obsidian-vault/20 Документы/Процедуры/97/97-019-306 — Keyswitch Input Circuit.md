---
type: "Процедура"
doc: "97-019-306"
title_en: "Keyswitch Input Circuit"
modified: "2004-10-19"
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
figures: 37
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-306.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-306.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Keyswitch Input Circuit

> [!abstract] Процедура · `97-019-306`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-10-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-306.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-306.pdf)

### Resistance Check

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections may require that the engine ECM real-time clock be reset using INSITE™ electronic service tool.

![[ea8coha.png]]

Remove and inspect the fuse on the ICON™ keyswitch ignition circuit for corrosion, damage or blown fuse.

Replace the fuse if necessary.

![[19400445.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the ICON™ idle control module A connector.

Set the multimeter to measure resistance.

![[19c00928.png]]

Touch one of the multimeter leads to pin 7 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to the ignition terminal post in the keyswitch assembly.

Read the value displayed on the multimeter.

![[19c00938.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, isolate the problem area to the cab harness or engine harness portion of the circuit.

![[19801619.png]]

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, engine harness side.

Touch the other multimeter lead to pin 7 of the ICON™ idle control module A harness connector.

Read the value displayed on the multimeter.

![[19c00930.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the ICON™ engine harness.

Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, cab harness side.

Touch the other multimeter lead to the ignition terminal post in the keyswitch assembly.

Read the value displayed on the multimeter.

![[19c00939.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure [[99-019-207 — Deutsch HD10 Connector Series|019-207]] or [[97-019-305 — Cab Wiring Harness|019-305]].

![[19801619.png]]

Disconnect the cab thermostat jumper harness from the cab thermostat.

Touch one of the multimeter leads to the ignition terminal post in the keyswitch assembly.

Touch the other multimeter lead to pin 4 of the cab thermostat jumper harness connector.

Read the value displayed on the multimeter.

![[19c00937.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the cab thermostat jumper harness. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-295 — Cab Thermostat Harness|019-295]].

Connect all components after completing the repair.

![[19801619.png]]

### Check for Short Circuit to Ground

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections may require that the engine ECM real-time clock be reset using INSITE™ electronic service tool.

![[ea8coha.png]]

Disconnect the ICON™ idle control module A connector.

Set the multimeter to measure resistance.

![[19c00928.png]]

Touch one of the multimeter leads to pin 7 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00932.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit to ground.

Isolate the short circuit to the ICON™ engine harness, cab harness, or cab thermostat jumper harness.

![[19801621.png]]

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, engine harness side.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00940.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, repair or replace the ICON™ engine harness.

Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]], [[99-019-207 — Deutsch HD10 Connector Series|019-207]], or [[97-019-043 — Engine Wiring Harness|019-043]]. If the circuit is open, check the cab harness and cab thermostat jumper harness.

![[19801621.png]]

Disconnect the cab thermostat jumper harness from the cab thermostat.

Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, cab harness side.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00933.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, repair or replace the cab harness.

Refer to Procedure [[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]] or [[97-019-305 — Cab Wiring Harness|019-305]]. If the circuit is open, check the cab thermostat jumper harness.

![[19801621.png]]

Touch one of the multimeter leads to pin 4 of the cab thermostat jumper harness connector.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802892.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, repair or replace the cab thermostat jumper harness.

Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-295 — Cab Thermostat Harness|019-295]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit from Pin to Pin

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™ electronic service tool.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the ICON™ idle control module A connector.

Set the multimeter to measure resistance.

![[19c00928.png]]

Touch one of the multimeter leads to pin 7 of the idle control module A harness connector.

Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

![[19c00943.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit from pin 7 to any other pin in the connector that registered a closed circuit.

Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, engine harness side.

Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

![[19c00942.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit from pin E to any other pin in the connector that registered a closed circuit.

Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Disconnect the cab thermostat jumper harness connector from the cab thermostat.

Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, cab harness side.

Touch the other multimeter lead to all other pins of the connector, one at a time.

Read the value displayed on the multimeter.

![[19c00935.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit from pin E to any other pin in the connector that registered a closed circuit.

Repair or replace the cab harness. Refer to Procedure [[99-019-207 — Deutsch HD10 Connector Series|019-207]] or [[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Touch one of the multimeter leads to pin 4 of the cab thermostat jumper harness connector.

Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

![[19c00941.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit from pin 4 to any other pin in the connector that registered a closed circuit.

Repair or replace the cab thermostat jumper harness. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-295 — Cab Thermostat Harness|019-295]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit to External Voltage Source

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Turn the keyswitch to the OFF position.

Disconnect the ICON™ idle control module A connector.

Set the multimeter to measure VDC.

![[19c00963.png]]

Touch one of the multimeter leads to pin 7 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00932.png]]

The multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the cab or engine harness wiring that carries voltage.

Remove the external voltage source.

![[19c00954.png]]

Disconnect the cab thermostat jumper harness from the thermostat. Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter. The multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.

Remove the external voltage source.

![[19c00933.png]]

Touch one of the multimeter leads to pin 4 of the cab thermostat harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter. The multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.

Remove the external voltage source.

![[19802892.png]]

Touch one of the multimeter leads to the ignition terminal post in the keyswitch assembly. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter. The multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.

Remove the external voltage source.

Connect all components after completing the repair.

![[19c00946.png]]
