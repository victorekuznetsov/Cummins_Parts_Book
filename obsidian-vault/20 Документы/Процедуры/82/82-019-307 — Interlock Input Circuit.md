---
aliases:
  - "Цепь входа блокировки"
type: "Процедура"
doc: "82-019-307"
title_en: "Interlock Input Circuit"
title_ru: "Цепь входа блокировки"
modified: "2005-01-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 31
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-307.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-307.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Interlock Input Circuit
**Цепь входа блокировки**

> [!abstract] Процедура · `82-019-307`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-307.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-307.pdf)

### Resistance Check

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position.

Disconnect the vehicle battery cables from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Check the engine harness portion of the circuit.

Disconnect the actuator harness connector and the sensor harness connector from the ECM.

Make sure the ICON™ shorting plug is connected to the 6-pin engine harness connector. Disconnect the 31-pin OEM connector.

Set the multimeter to measure resistance.

![[19c00892.png]]

> [!note] Note · Примечание
> Verify that all interlock switches are closed before proceeding with the following electrical check.

Touch one of the multimeter leads to pin 14 of the actuator harness connector.

Touch the other multimeter lead to pin 27 of the 31-pin OEM harness connector, engine harness side

Read the value displayed on the multimeter.

![[19c00728.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, check the ICON™ shorting plug.

![[19801619.png]]

Disconnect the ICON™ shorting plug from the 6-pin engine harness connector.

Touch the multimeter lead to pin 5 of the ICON™ shorting plug. Touch the other multimeter lead to pin 4 of the ICON™ shorting plug. Read the value displayed on the multimeter.

The multimeter **must** display a reading of less than 10 ohms (closed circuit).

If the circuit is **not** closed, replace the shorting plug. Refer to the OEM troubleshooting and repair manual. If the shorting plug tests okay, repair or replace the engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] for harness repairs, and Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]] for harness replacement.

![[19c00730.png]]

Check the OEM harness side of the circuit.

Disconnect the ICON™ starter relay from the OEM harness. Disconnect the OEM harness connector from the ECM.

Touch one of the multimeter leads to pin 27 of the 31-pin OEM connector, OEM harness side. Touch the other multimeter lead to the ICON™ starter relay harness connector, 31-pin connector side. Read the value displayed on the multimeter.

The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure 019-071.

![[19c00731.png]]

Touch one of the multimeter leads to pin 33 of the 50-pin OEM harness connector. Touch the other multimeter lead to pin 86 of the ICON™ starter relay harness connector, ECM side, or the equivalent pin on the ECM side of the relay. Refer to the ISM wiring diagram, Bulletin 3666269. Read the value displayed on the multimeter.

The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure 019-071.

![[19c00726.png]]

Touch one of the multimeter leads to pin 20 of the 31-pin OEM connector, OEM harness side. Touch the other multimeter lead to pin 33 of the 50-pin OEM harness connector. Read the value displayed on the multimeter.

The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, check each interlock switch to see if a defective switch is the cause of the open circuit.

![[19c00727.png]]

Check the interlock switches.

Disconnect the parking brake switch from the OEM harness. Touch one of the multimeter leads to pin 1 (or A) of the switch connector, switch side. Touch the other multimeter lead to pin 2 (or B) of the connector. Read the value displayed on the multimeter.

The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, replace the switch. Refer to the OEM manual.

If the circuit is closed, test the other two interlock switches for an open circuit in the same manner. Replace any defective switches. If all three switches show a closed circuit, repair or replace the OEM harness. Refer to Procedure 019-071.

Connect all components after completing the repair.

![[19c00753.png]]

### Check for Short Circuit to Ground

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test leads, Part No 3822758 and 3822917, when taking a measurement.

Disconnect the neutral position interlock switch, the hood tilt interlock switch, and the parking brake interlock switch from the OEM harness.

Set the multimeter to measure resistance.

![[19c00732.png]]

Check the neutral position interlock switch.

Touch one of the multimeter leads to pin A (or 1) of the neutral position switch, on the switch side of the connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin B (or 2) of the neutral position switch, on the switch side of the connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.

![[19c00733.png]]

For both pin checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit to ground.

Replace the neutral position switch. Refer to the OEM troubleshooting and repair manual.

![[19801621.png]]

Check the hood tilt interlock switch.

Touch one of the multimeter leads to pin A (or 1) of the hood tilt switch, on the switch side of the connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin B (or 2) of the hood tilt switch, on the switch side of the connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.

![[19c00733.png]]

For both pin checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit to ground.

Replace the hood tilt switch. Refer to the OEM troubleshooting and repair manual.

![[19801621.png]]

Check the parking brake interlock switch.

Touch one of the multimeter leads to pin A (or 1) of the parking brake switch, on the switch side of the connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin B (or 2) of the parking brake switch, on the switch side of the connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.

![[19c00733.png]]

For both pin checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit to ground.

Replace the parking brake switch. Refer to the OEM troubleshooting and repair manual.

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit from Pin to Pin

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test lead, Part No 3822758, when taking a measurement.

Disconnect the actuator harness and sensor harness connectors from the ECM.

Disconnect the 31-pin OEM connector.

Make sure the ICON™ shorting plug is connected to the 6-pin engine harness connector.

Set the multimeter to measure resistance.

![[19c00892.png]]

Touch one of the multimeter leads to pin 14 of the actuator harness connector.

Touch the other multimeter lead to all other pins in the actuator harness connector, one at a time.

Then repeat the pin-to-pin check from pin 14 of the actuator harness connector to all pins in the sensor harness connector.

Read the value displayed on the multimeter.

![[19c00893.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between pin 14 and any pin in either harness connector that registered a closed circuit.

Repair or replace the engine harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19801621.png]]

Repeat the pin-to-pin check from pin 46 of the actuator harness connector to all other pins in the actuator harness connector.

Read the value displayed on the multimeter.

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between pin 46 and any other pin that registered a closed circuit.

Repair or replace the engine harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19c00735.png]]

Disconnect the OEM harness connector from the ECM.

Touch one of the multimeter leads to pin 33 of the OEM harness connector.

Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

![[19c00754.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between pin 33 and any other pin that registered a closed circuit.

Repair or replace the OEM harness. Refer to Procedure 019-071.

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit to External Voltage Source

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the neutral position switch from the OEM harness. Disconnect the parking brake switch from the OEM harness. Disconnect the hood tilt switch from the OEM harness.

Set the multimeter to measure VDC.

Turn the keyswitch to the ON position.

![[19c00732.png]]

Check the neutral position interlock switch.

Touch one of the multimeter leads to pin A (or 1) of the neutral position switch harness connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin B (or 2) of the neutral position switch harness connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.

![[19c00733.png]]

For both pin checks, the multimeter **must** display a reading of less than 1.5 VDC. If the voltage is **not** less than 1.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the OEM or engine harness wiring that carries voltage.

Remove the external voltage source.

![[19c00724.png]]

Check the hood tilt interlock switch.

Touch one of the multimeter leads to pin A (or 1) of the hood tilt switch harness connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin B (or 2) of the hood tilt switch harness connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.

![[19c00733.png]]

For both pin checks, the multimeter **must** display a reading of less than 1.5 VDC. If the voltage is **not** less than 1.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the OEM or engine harness wiring that carries voltage.

Remove the external voltage source.

![[19c00724.png]]

Check the parking brake interlock switch.

Touch one of the multimeter leads to pin A (or 1) of the parking brake switch harness connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin B (or 2) of the parking brake switch harness connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.

![[19c00733.png]]

For both pin checks, the multimeter **must** display a reading of less than 1.5 VDC. If the voltage is **not** less than 1.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the OEM or engine harness wiring that carries voltage.

Remove the external voltage source.

Connect all components after completing the repair.

![[19c00724.png]]
