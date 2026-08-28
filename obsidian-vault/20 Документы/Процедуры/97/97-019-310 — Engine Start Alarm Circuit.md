---
aliases:
  - "Цепь сигнализации пуска двигателя"
type: "Процедура"
doc: "97-019-310"
title_en: "Engine Start Alarm Circuit"
title_ru: "Цепь сигнализации пуска двигателя"
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
figures: 35
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-310.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-310.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Engine Start Alarm Circuit
**Цепь сигнализации пуска двигателя**

> [!abstract] Процедура · `97-019-310`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-10-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-310.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-310.pdf)

### Test

Turn the keyswitch to the ON position.

Connect the ICON™ electronic service tool (Aftermarket or OEM systems), or INSITE™ electronic service tool (Integrated systems).

Initiate the Alarm Test.

If the alarm sounds, the alarm circuit passed the test and no repairs are needed.

![[nobox.png]]

### Resistance Check

Turn the keyswitch to the OFF position.

Remove and inspect the power fuse on the ICON™ engine harness for corrosion, damage, or a blown fuse.

Replace the fuse if necessary.

![[15800036.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (--) battery cable last.

Disconnect the vehicle battery cables from the battery. Remove the ICON™ engine harness positive (+) battery connector from the battery terminal post.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the engine start alarm connector from the ICON™ engine harness. Disconnect the ICON™ idle control module A and B connectors.

Set the multimeter to measure resistance.

![[19c00920.png]]

Touch one of the multimeter leads to the positive (+) ICON™ engine harness connector ring terminal.

Touch the other multimeter lead to pin B of the engine start alarm harness connector.

Read the value displayed on the multimeter.

![[19802930.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the ICON™ engine harness.

Refer to Procedure [[99-019-197 — Ring Terminal|019-197]], [[99-019-202 — Metripack Connector Series|019-202]], or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Touch one of the multimeter leads to pin 1 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to pin B of the engine start alarm harness connector.

Read the value displayed on the multimeter.

![[19802894.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the ICON™ engine harness.

Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]], [[99-019-202 — Metripack Connector Series|019-202]], or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Touch one of the multimeter leads to pin 3 of the ICON™ idle control module B harness connector.

Touch the other multimeter lead to pin A of the engine start alarm harness connector.

Read the value displayed on the multimeter.

![[19802895.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the ICON™ engine harness.

Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]], [[99-019-202 — Metripack Connector Series|019-202]], or [[97-019-043 — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19801619.png]]

### Check for Short Circuit to Ground

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Remove the ICON™ engine harness positive (+) battery connector from the positive (+) battery terminal post.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the engine alarm from the ICON™ engine harness. Disconnect the ICON™ idle control module A and B connectors.

Set the multimeter to measure resistance.

![[19c00920.png]]

Touch one of the multimeter leads to the ICON™ engine harness positive (+) battery ring terminal connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802931.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit to ground. Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-197 — Ring Terminal|019-197]] or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin A of the engine alarm harness connector. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin B of the engine alarm harness connector. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.

![[19802899.png]]

For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit to ground. Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin 1 of the ICON™ idle control module A harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00932.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit to ground. Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin 3 of the ICON™ idle control module B harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802900.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit to ground. Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit from Pin to Pin

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Remove the ICON™ engine harness positive (+) battery connector from the positive (+) battery terminal post.

Set the multimeter to measure resistance.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the ICON™ idle control module A and B connectors.

Disconnect the engine start alarm from the ICON™ engine harness.

![[19c00917.png]]

Touch one of the multimeter leads to pin 1 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to all other pins in the connector.

Read the value displayed on the multimeter.

![[19c00943.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit from pin 1 in the ICON™ idle control module A harness connector to any other pin in the connector that registered a closed circuit.

Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin 3 of the ICON™ idle control module B harness connector.

Touch the other multimeter lead to all other pins in the connector.

Read the value displayed on the multimeter.

![[19c00962.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit from pin 3 in the ICON™ idle control module B harness connector to any other pin in the connector that registered a closed circuit.

Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin A of the engine start alarm harness connector.

Touch the other multimeter lead to pin B of the connector.

Read the value displayed on the multimeter.

![[19802901.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit from pin A to pin B in the engine start alarm harness connector. Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or [[97-019-043 — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit to External Voltage Source

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the ICON™ engine harness ring terminal positive (+) battery connector from the positive (+) battery post. Disconnect the ICON™ idle control module A and B connectors. Disconnect the engine start alarm from the ICON™ engine harness.

Set the multimeter to measure VDC.

Turn the keyswitch to the ON position.

![[19c00917.png]]

Touch one of the multimeter leads to pin 1 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00932.png]]

The multimeter **must** display a reading of less than 0.5 VDC.

If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the cab harness or engine harness wiring that carries voltage.

Remove the external voltage source.

![[19c00954.png]]

Touch one of the multimeter leads to pin 3 of the ICON™ idle control module B harness connector.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802900.png]]

The multimeter **must** display a reading of less than 0.5 VDC.

If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the cab harness or engine harness wiring that carries voltage.

Remove the external voltage source.

![[19c00954.png]]

Touch one of the multimeter leads to pin A of the engine start alarm harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

Repeat the pin-to-ground check from pin B. Touch one of the multimeter leads to pin B of the engine start alarm harness connector. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802899.png]]

For both checks, the multimeter **must** display a reading of less than 0.5 VDC.

If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the cab harness or engine harness wiring that carries voltage.

Remove the external voltage source.

Connect all components after completing the repair.

![[19c00954.png]]
