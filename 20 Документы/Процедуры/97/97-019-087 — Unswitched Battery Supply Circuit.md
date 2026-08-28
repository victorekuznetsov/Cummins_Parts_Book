---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "97-019-087"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
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
figures: 27
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-087.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-087.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `97-019-087`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-087.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-087.pdf)

### Resistance Check

General Information

Turn the keyswitch to the OFF position.

Remove and inspect the power fuse on the ICON™ engine harness for corrosion, damage, or a blown fuse.

Replace the fuse if necessary.

![[15800036.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) cable last.

Disconnect the vehicle battery cables from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

Remove the ICON™ engine harness battery connectors from the battery terminal posts.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the ICON™ idle control module A connector.

Disconnect the 4-pin cab thermostat jumper harness connector from the cab thermostat.

Set the multimeter to measure resistance.

![[19802871.png]]

Engine Harness Check

Touch one of the multimeter leads to pin 1 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to the positive (+) ICON™ engine harness connector ring terminal (normally connected to the vehicle battery). Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin 1 of the thermostat jumper harness connector (on the end that connects to the thermostat).

Touch the other lead to the positive (+) ICON™ engine harness connector ring terminal. Read the value displayed on the multimeter.

![[19c00967.png]]

For both checks, the multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, recheck the engine harness fuse and replace, if necessary.

If the fuse is good, replace the ICON engine harness, or isolate the problem to the correct battery ring terminal, or the ICON™ idle control module A connector.

![[19801619.png]]

Touch one of the multimeter leads to pin 1 of the cab thermostat jumper harness 4-pin connector (the connector on the cab harness).

Touch the other multimeter lead to the positive (+) ICON™ engine harness battery connector ring terminal. Measure the resistance. The multimeter **must** display a reading of 10 ohms or less. If the circuit is **not** closed, isolate the problem to the ICON™ engine, cab, or thermostat jumper harness.

![[19c00968.png]]

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Touch one of the multimeter leads to pin A of the 14-pin pass-through connector, engine harness side.

Touch the other multimeter lead to the positive (+) ICON™ engine harness battery connector ring terminal.

Read the value displayed on the multimeter.

![[19c00969.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-200 or [[97-019-043 — Engine Wiring Harness|019-043]].

If the circuit is closed, check the cab harness portion of the circuit.

![[19801619.png]]

Connect the 14-pin pass-through connector.

Touch one of the multimeter leads to pin 2 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to the negative (-) ICON™ engine harness connector ring terminal (normally connected to the vehicle battery). Read the value displayed on the multimeter.

Then, touch one of the multimeter leads to pin 2 of the thermostat jumper harness connector (on the end that connects to the thermostat). Touch the other lead to the negative (-) ICON™ engine harness connector ring terminal. Read the value displayed on the multimeter.

![[19c00967.png]]

For both checks, the multimeter **must** display a reading of 10 ohms or less, which is a closed circuit. If the circuit is **not** closed, isolate the problem to the ICON™ engine, cab, or thermostat jumper harness.

![[19801619.png]]

Touch one of the multimeter leads to pin 2 of the ICON™ idle control module A harness connector.

Touch the other multimeter lead to the negative (-) ICON™ engine harness connector ring terminal.

Read the value displayed on the multimeter.

![[19c00972.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the ICON™ engine harness.

Refer to Procedure 019-208 or 019-197 for harness repair, or Procedure [[97-019-043 — Engine Wiring Harness|019-043]] for harness replacement.

![[19801619.png]]

Disconnect the 14-pin pass-through connector at the vehicle's firewall.

Touch one of the multimeter leads to pin C of the 14-pin pass-through connector, engine harness side.

Touch the other multimeter lead to the negative (-) ICON™ engine harness battery connector ring terminal.

Read the value displayed on the multimeter.

![[19c00969.png]]

The multimeter **must** display a reading of 10 ohms or less, which is a closed circuit. If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-200 or 019-197 for harness repair, or Procedure [[97-019-043 — Engine Wiring Harness|019-043]] for harness replacement.

If the circuit is closed, check the cab harness portion of the circuit.

![[19801619.png]]

Cab Harness Check

Disconnect the cab thermostat jumper harness from the cab harness. Touch one of the multimeter leads to pin 1 of the cab thermostat jumper harness 4-pin connector (the connector on the cab harness under the dash).

Touch the other multimeter lead to pin A of the 14-pin pass-through connector, cab harness side.

Read the value displayed on the multimeter.

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the ICON™ cab harness. Refer to Procedure [[97-019-305 — Cab Wiring Harness|019-305]].

![[19c00970.png]]

Touch one of the multimeter leads to pin 2 of the cab thermostat jumper harness connector (the connector on the cab harness).

Touch the other multimeter lead to pin C of the 14-pin pass-through connector, cab harness side.

Read the value displayed on the multimeter.

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure [[97-019-305 — Cab Wiring Harness|019-305]].

![[19c00970.png]]

Cab Thermostat Jumper Harness Check

Touch one of the multimeter leads to pin 1 of the 4-pin cab thermostat jumper harness connector, jumper harness side. This connector is located on the end of the cab thermostat jumper harness that connects to the cab harness.

Touch the other multimeter lead to pin 1 of the cab thermostat jumper harness connector on the end of the harness that connects to the thermostat's power/data 4-pin connector.

Read the value displayed on the multimeter.

![[19c00971.png]]

The multimeter **must** display a reading of 10 ohms or less which is a closed circuit.

If the circuit is **not** closed, replace the cab thermostat jumper harness. Refer to Procedure [[97-019-295 — Cab Thermostat Harness|019-295]].

![[19801619.png]]

Touch one of the multimeter leads to pin 2 of the 4-pin thermostat jumper harness connector, jumper harness side. This connector is located on the end of the thermostat jumper harness that connects to the cab harness.

Touch the other multimeter lead to pin 2 of the thermostat jumper harness connector, the connector located on the end of the harness that connects to the thermostat's power and data 4-pin connector.

Read the value displayed on the multimeter.

![[19c00971.png]]

The multimeter **must** display a reading of 10 ohms or less, which is a closed circuit.

If the circuit is **not** closed, repair or replace the thermostat jumper harness. Refer to Procedure [[97-019-295 — Cab Thermostat Harness|019-295]].

![[19801619.png]]

ICON™ Battery Connectors to Datalink Check

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

Remove the ICON™ engine harness positive (+) battery connector from the battery terminal post.

Remove the OEM datalink (6-pin or 9-pin) connector cap.

Set the multimeter to measure resistance.

![[15800045.png]]

> [!note] Note · Примечание
> Check the OEM wiring diagram to confirm the positive and negative datalink connector pin assignments. The following steps describe a “typical” vehicle configuration, but possibly will **not** correspond to your vehicle's configuration.

Touch one of the multimeter leads to the positive (+) chassis battery harness connector ring terminal.

Touch the other multimeter lead to the pin attached to the positive (+) battery wire in the datalink connector (typically, pin C in the 6-pin Deutsch connector or pin B in the 9-pin Deutsch connector).

Read the value displayed on the multimeter.

![[19c00973.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the OEM wiring connected to the datalink connector.

Refer to the OEM troubleshooting and repair manual.

![[19801619.png]]

Touch one of the multimeter leads to the positive (+) OEM battery harness connector ring terminal. Touch the other multimeter lead to the battery terminal post in the keyswitch assembly.

Read the value displayed on the multimeter.

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the OEM harness.

Refer to the OEM troubleshooting and repair manual.

![[19c00974.png]]

Remove the OEM harness negative (-) battery connector from the battery terminal post.

Touch one of the multimeter leads to the negative (-) OEM harness connector ring terminal.

Touch the other multimeter lead to the pin attached to the negative (-) battery wire in the datalink connector (typically, pin E in the 6-pin Deutsch connectors or pin A in the 9-pin Deutsch connector).

Read the value displayed on the multimeter.

![[19c00973.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the OEM harness or isolate cable to right battery.

Refer to the OEM troubleshooting and repair manual.

![[19801619.png]]
