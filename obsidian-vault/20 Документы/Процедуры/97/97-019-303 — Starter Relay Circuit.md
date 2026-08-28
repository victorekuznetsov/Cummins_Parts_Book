---
aliases:
  - "Цепь реле стартера"
type: "Процедура"
doc: "97-019-303"
title_en: "Starter Relay Circuit"
title_ru: "Цепь реле стартера"
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
figures: 29
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-303.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-303.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Starter Relay Circuit
**Цепь реле стартера**

> [!abstract] Процедура · `97-019-303`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-303.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-303.pdf)

### Resistance Check

General Information

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position.

Disconnect the vehicle battery cables from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the starter relay from the ICON™ engine harness.

Set the multimeter to measure resistance.

![[19802877.png]]

> [!note] Note · Примечание
> The starter relay is a normally open relay.

Touch one of the multimeter leads to pin 87 of the starter relay harness connector.

Touch the other multimeter lead to the battery terminal post in the keyswitch assembly.

Read the value displayed on the multimeter.

![[19802878.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, check the ICON™ engine harness and cab harness portions of the circuit.

![[19801619.png]]

ICON™ Engine Harness Side Check

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Touch one of the multimeter leads to pin 87 of the starter relay harness connector. Touch the other multimeter lead to pin L of the 14-pin pass-through connector, engine harness side. Read the value displayed on the multimeter.

The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-204, 019-200, or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19802879.png]]

Then, touch one of the multimeter leads to pin 30 of the starter relay harness connector. Touch the other multimeter lead to pin N of the 14-pin pass-through connector, engine harness side. Read the value displayed on the multimeter.

The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-204, 019-200, or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19802879.png]]

Disconnect the engine ECM 50-pin OEM harness connector from the engine ECM (on Signature, ISX, and ISM engines). If your application is a CELECT™ Plus engine, disconnect the engine 21-pin OEM connector. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module.

Touch one of the multimeter leads to pin 85 of the starter relay harness connector. Touch the other multimeter lead to pin 5 of the ICON™ idle control module B harness connector. Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin 86 of the starter relay harness connector. Touch the other multimeter lead to pin 6 of the ICON™ idle control module B harness connector. Read the value displayed on the multimeter.

![[19802880.png]]

For both checks, the multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-204, 019-208, or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Touch one of the multimeter leads to pin 85 of the starter relay harness connector. Touch the other multimeter lead to pin 38 of the engine ECM 50-pin harness connector (Signature, ISX, and ISM engines).

If your application is a CELECT™ Plus engine, touch the other multimeter lead to pin A of the 21-pin OEM harness connector. Read the value displayed on the multimeter.

![[19802881.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-204 or [[97-019-043 — Engine Wiring Harness|019-043]].

Or, repair or replace the engine OEM connector. Refer to the appropriate base engine troubleshooting and repair manual.

![[19801619.png]]

ICON™ Cab Harness Side Check

Touch one of the multimeter leads to pin L of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to the battery terminal post in the keyswitch assembly. Read the value displayed on the multimeter.

The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure 019-200, 019-197, or [[97-019-305 — Cab Wiring Harness|019-305]].

![[19802882.png]]

Touch one of the multimeter leads to pin N of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to the magnetic switch wire terminal post (switch is located on the starter). Read the value displayed on the multimeter.

The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, check the integrity of the butt splice of the starter magnetic switch wire to the ICON™ cab harness magnetic switch power wire (wire Number 017). If the butt splice is good, repair or replace the cab harness. Refer to Procedure 019-200 or [[97-019-305 — Cab Wiring Harness|019-305]].

Connect all components after completing the repair.

![[19802883.png]]

### Check for Short Circuit to Ground

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables and ICON™ battery harness connectors from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.

Set the multimeter to measure resistance.

Touch one of the multimeter leads to the battery terminal post in the keyswitch assembly.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19802884.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit to ground.

Isolate the short to the cab harness or ICON™ engine harness portion of the circuit.

![[19801621.png]]

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Touch one of the multimeter leads to pin L of the 14-pin pass-through connector, engine harness side. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.

Then, repeat the short-to-ground check from pin N of the 14-pin pass-through connector, engine harness side, to engine block ground. Read the value displayed on the multimeter.

![[19c00940.png]]

For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is open, the short circuit is on the cab harness side of the circuit. Repair or replace the cab harness. Refer to Procedure 019-197, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].

If the circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure 019-200 or [[97-019-043 — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit from Pin to Pin

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables and ICON™ battery harness connectors from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the 14-pin pass-through connector on the vehicle's firewall.

Set the multimeter to measure resistance.

![[15800040.png]]

Touch one of the multimeter leads to pin L of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to all other pins in the connector, one at a time. Read the value displayed on the multimeter for each pin-to-pin check.

Then, repeat the pin-to-pin check from pin N of the 14-pin pass-through connector, cab harness side, to all other pins in the connector. Read the value displayed on the multimeter for each pin-to-pin check.

![[19c00935.png]]

For each pin-to-pin check, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If any circuit is **not** open, there is a short circuit from pin L (or pin N) to any other pin in the connector that registered a closed circuit.

Repair or replace the cab harness. Refer to Procedure 019-200 or [[97-019-305 — Cab Wiring Harness|019-305]].

Check the engine harness side of the connector.

![[19801621.png]]

Touch one of the multimeter leads to pin L of the 14-pin pass-through connector, engine harness side. Touch the other multimeter lead to all other pins in the connector, one at a time. Read the value displayed on the multimeter for each pin-to-pin check.

Then, repeat the pin-to-pin check from pin N of the 14-pin pass-through connector, engine harness side, to all other pins in the connector. Read the value displayed on the multimeter for each pin-to-pin check.

![[19c00942.png]]

For each pin-to-pin check, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If any circuit is **not** open, there is a short circuit from pin L (or pin N) to any other pin in the connector that registered a closed circuit.

Repair or replace the ICON™ engine harness. Refer to Procedure 019-200 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Disconnect the starter relay from the engine harness.

Touch one of the multimeter leads to pin 87 of the relay harness connector.

Touch the other multimeter lead to all other pins in the connector, one at a time.

Read the value displayed on the multimeter.

![[19802885.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit from pin 87 to any other pin in the connector that registered a closed circuit.

Repair or replace the engine harness or relay connector.

Refer to Procedure 019-204 or [[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Repeat the pin-to-pin check from pins 85, 86, and 30 of the starter relay harness connector to all other pins in the connector. Read the value displayed on the multimeter for each pin-to-pin check.

For each pin-to-pin check, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If any circuit is **not** open, there is a short circuit from pin 85 (or 86 or 30) to any other pin in the connector that registered a closed circuit.

Repair or replace the engine harness or relay connector. Refer to Procedure 019-204 or [[97-019-043 — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19802885.png]]

### Voltage Check

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test lead, Part Number 3822917, when taking a measurement.

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Set the multimeter to measure VDC.

Turn the keyswitch to the ON position.

![[15800040.png]]

Touch one of the multimeter leads to pin L of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.

Then, repeat the voltage check from pin N of the 14-pin pass-through connector, cab harness side, to engine block ground. Read the value displayed on the multimeter.

![[19c00933.png]]

For the check from pin L to ground, the multimeter **must** display a reading of greater than 12 VDC. For the check from pin N to ground, the multimeter **must** display a reading of 0 VDC.

If the voltage readings are **not** the correct VDC for each pin, repair or replace the cab harness. Refer to Procedure 019-197, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].

Connect all components after completing the repair.

![[19802886.png]]
