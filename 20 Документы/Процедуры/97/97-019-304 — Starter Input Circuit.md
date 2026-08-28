---
type: "Процедура"
doc: "97-019-304"
title_en: "Starter Input Circuit"
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
figures: 25
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-304.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-304.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Starter Input Circuit

> [!abstract] Процедура · `97-019-304`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-304.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-304.pdf)

### Resistance Check

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battey connections can require that the ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the ICON™ idle control module A connector.

Set the multimeter to measure resistance.

![[19c00928.png]]

Touch one of the multimeter leads to pin 8 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to the starter terminal post in the keyswitch assembly.

Read the value displayed on the multimeter.

![[19802887.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, check the ICON™ engine harness and cab harness portions of the circuit.

![[19801619.png]]

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Touch one of the multimeter leads to pin M of the 14-pin pass-through connector, engine harness side.

Touch the other multimeter lead to pin 8 of the ICON™ idle control module A harness connector.

Read the value displayed on the multimeter.

![[19c00930.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit it **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-208, 019-200, or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Touch one of the multimeter leads to pin M of the 14-pin pass-through connector, cab harness side.

Touch the other multimeter lead to the starter terminal post in the keyswitch assembly.

Read the value displayed on the multimeter.

![[19802888.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit it **not** closed, repair or replace the cab harness.

Refer to Procedure 019-197, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].

Connect all components after completing the repair.

![[19801619.png]]

### Check for Short Circuit to Ground

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

Set the multimeter to measure resistance.

Touch one of the multimeter leads to the starter terminal post in the keyswitch assembly.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802889.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit to ground.

Isolate the short circuit to the cab harness or ICON™ engine harness portion of the circuit.

![[19801621.png]]

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Touch one of the multimeter leads to pin M of the 14-pin pass-through connector, cab harness side.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00933.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, check the engine harness side of the circuit.

If the circuit is open, repair or replace the cab harness. Refer to Procedure 019-197 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin M of the 14-pin pass-through connector, engine harness side.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00940.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-200, 019-208, or [[97-019-043 — Engine Wiring Harness|019-043]].

If the circuit is open, repair or replace the cab harness. Refer to Procedure 019-200 or [[97-019-305 — Cab Wiring Harness|019-305]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit from Pin to Pin

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections may require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Set the multimeter to measure resistance.

![[15800040.png]]

Touch one of the multimeter leads to pin M of the 14-pin pass-through connector, cab harness side.

Touch the other multimeter lead to all other pins of the connector, cab harness side, one at a time.

Read the value displayed on the multimeter. The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit from pin M to any other pin in the connector that registered a closed circuit. Repair or replace the cab harness. Refer to Procedure 019-200 or [[97-019-305 — Cab Wiring Harness|019-305]].

![[19c00935.png]]

Check the engine harness side of the connector.

Touch one of the multimeter leads to pin M of the 14-pin pass-through connector, engine harness side.

Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

![[19c00942.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit from pin M to any other pin in the connector that registered a closed circuit.

Repair or replace the ICON™ engine harness. Refer to Procedure 019-200 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Disconnect the ICON™ idle control module A connector.

Touch one of the multimeter leads to pin 8 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

![[19c00943.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit from pin 8 to any other pin in the connector that registered a closed circuit.

Repair or replace the ICON™ engine harness. Refer to Procedure 019-208 or [[97-019-043 — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit to External Voltage Source

Set the multimeter to measure VDC.

Turn the keyswitch to the ON position.

![[19c00963.png]]

Touch one of the multimeter leads to the starter terminal post in the keyswitch assembly.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802889.png]]

The multimeter **must** display a reading of less than 0.5 VDC.

If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the cab or ICON™ engine harness wiring that carries voltage.

Remove the external voltage source.

Connect all components after completing the repair.

![[19c00954.png]]
