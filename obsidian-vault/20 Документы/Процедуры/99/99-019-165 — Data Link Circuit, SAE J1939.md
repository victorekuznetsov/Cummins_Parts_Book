---
aliases:
  - "Цепь шины данных SAE J1939"
type: "Процедура"
doc: "99-019-165"
title_en: "Data Link Circuit, SAE J1939"
title_ru: "Цепь шины данных SAE J1939"
modified: "2015-06-25"
engines:
  - "41343322"
  - "41370103"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
  - "4021442"
figures: 13
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-165.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-165.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Data Link Circuit, SAE J1939
**Цепь шины данных SAE J1939**

> [!abstract] Процедура · `99-019-165`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-165.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-165.pdf)

### General Information

The OEM J1939 datalink circuit is located in the OEM wiring harness.

The purpose of this datalink is to allow communication with vehicle control-operated systems such as transmission controllers, traction control system, etc.

The traditional OEM J1939 datalink circuit is described as a shielded twisted pair and includes the wires connected to the J1939 datalink positive (+) pin, the J1939 datalink negative (-) pin, and the J1939 (shield) pin in the OEM harness.

On newer vehicles and equipment, OEM's can utilize an OEM J1939 datalink circuit that is described as an unshielded twisted pair (UTP). The unshielded twisted pair (UTP) J1939 datalink does **not** include the J1939 (shield) pin and **only** includes the J1939 datalink positive (+) pin and the J1939 datalink negative (-) pin in the OEM harness.

With the keyswitch in the ON position, public datalink messages will be broadcast on the OEM J1939 datalink. The broadcast will stop when the keyswitch is turned to the OFF position.

![[19803969.png]]

The Society of Automotive Engineers (SAE) J1939 has strict guidelines that **must** be followed for successful communication. Understanding some fundamentals about SAE J1939 will help make sure these guidelines are followed.

The main component of an SAE J1939 system is a backbone harness. The harness can be up to 40 meters \[131 feet\] in length. The backbone harness is terminated at each end with a 120 ohm resistor.

A maximum of thirty different devices can be attached to the SAE J1939 backbone at once. Each device, such as the datalink adapter, is connected to the backbone through a stub, which can be up to 1 meter \[3.3 ft\] in length. The stub connector is a 3-pin plug.

![[19802395.png]]

The terminating resistor caps (1) **must** be in place on the OEM backbone harness plugs (2) to maintain proper communication. Each resistor is 120 ohms and can be located in a removable cap.

![[19802397.png]]

Some OEMs will choose to provide a complete SAE J1939 backbone harness. If this is supplied, connection to the electronic service tool is accomplished by a 9-pin datalink connector (1), Part Number 3162848.

> [!note] Note · Примечание
> Some OEM's place a 9-pin connector in the cab, but do **not** connect all of the pins to support J1939 protocol.

To check for the OEM J1939 backbone, turn the keyswitch to the OFF position. Measure the resistance from the SAE J1939 datalink positive (+) pin to the SAE J1939 datalink negative (-) pin of the 9-pin Deutsch™ connector.

The multimeter **must** read between 50 and 65 ohms for the electronic service tool to be able to establish communication.

If the OEM does **not** supply the J1939 backbone harness to the 9-pin connector, the **only** way to establish J1939 communication is through either the bench communication setup or for the Engine Control Module through the engine communication setup. [[00-022-999 — Service Tools and Hardware - Overview|Refer to Procedure 022-999]].

> [!note] Note · Примечание
> The typical SAE J1939 connector will be a 9-pin connector.

![[19c01495.png]]

| Pin | Signal |
|---|---|
| A | Ground |
| B | Unswitched Battery |
| C | J1939 datalink (+) |
| D | J1939 datalink (-) |
| E | J1939 datalink (shield) (if available) |
| F | J1708 datalink (+) |
| G | J1708 datalink (-) |
| H | Open |
| J | Open |

![[19400739.png]]

### Resistance Check

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

Turn the keyswitch to the OFF position.

Disconnect the batteries.

Disconnect the OEM harness connector from the ECU.

Insert a test lead into the SAE J1939 datalink positive (+) pin of the OEM harness connector, and connect it to the multimeter probe. Insert the other test lead into the SAE J1939 datalink positive (+) pin of the 9-pin Deutsch™ connector, and connect it to the multimeter.

Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual for the procedures.

Insert the multimeter lead into the SAE J1939 datalink negative (-) of the OEM harness connector. Touch the other lead to the SAE J1939 datalink negative (-) pin of the 9-pin Deutsch™ connector. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less)

If the circuit is **not** closed, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual for the procedures.

If the values are correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.

Remove the lead from the SAE J1939 datalink negative (-) pin of the OEM harness connector and insert it into the SAE J1939 datalink (shield) pin, if the shield pin is available.

If the J1939 datalink circuit is an unshielded twisted pair (UTP), the shield pin will **not** be provided.

If the shield pin is provided, measure the resistance from the SAE J1939 datalink (shield) pin of the OEM harness connector to the SAE J1939 datalink (shield) pin of the 9-pin Deutsch™ connector.

The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual for the procedures.

If the (shield) pin is provided, measure the resistance from the SAE J1939 datalink (shield) pin of the 9-pin Deutsch™ connector to the engine block or chassis ground. The SAE J1939 datalink shield **must** be grounded to the vehicle battery ground. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, refer to the OEM troubleshooting and repair manual for repair instruction.

If more than 10 ohms are measured in any of these steps, there can be an open circuit in the SAE J1939 datalink positive (+) pin, the SAE J1939 datalink negative (-) pin, or the SAE J1939 (shield) pin, or the polarity is **not** correct. There can also be an open circuit from the datalink (shield) pin to vehicle battery ground.

If the values are correct, the SAE J1939 datalink positive (+) pin and the datalink negative (-) pin **must** still be checked for a short circuit to ground. The SAE J1939 datalink positive (+) pin, the datalink negative (-) pin, and the datalink (shield) pin **must** still be checked for a short circuit from pin to pin.

![[19c01496.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.Insert a test lead into the SAE J1939 datalink positive (+) pin of the OEM harness connector and connect it to a multimeter probe. Touch the other multimeter probe to the engine block or chassis ground.

Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

Remove the test lead from the SAE J1939 datalink positive (+) pin and insert it into the SAE J1939 datalink negative (-) pin. Measure the resistance from the SAE J1939 datalink negative (-) pin of the OEM harness connector to the engine block or chassis ground. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

![[19c01270.png]]

### Check for Short Circuit from Pin to Pin

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.

Insert a test lead into the SAE J1939 datalink positive (+) pin of the OEM harness connector and connect it to the multimeter probe. Insert the other test lead into another pin in the connector of the OEM harness and connect it to the other multimeter probe.

Measure the resistance from the SAE J1939 datalink positive (+) pin to the first pin in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

![[19c01271.png]]

Measure the resistance from the SAE J1939 datalink positive (+) pin of the OEM harness connector to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (100k ohms or more) at all pins, except the J1939 datalink negative (-).

If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

![[19c01215.png]]

Remove the test lead from the J1939 datalink positive (+) pin and insert it into the J1939 datalink (shield) pin of the OEM harness connector, if the shield pin is available

> [!note] Note · Примечание
> If the J1939 datalink circuit is an unshielded twisted pair (UTP), the (shield) pin will **not** be provided. If the shield pin is **not** provided, the datalink negative (-) pin **must** still be checked for a short circuit to the other pins.

Insert the other test lead into another pin in the connector. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

![[19c01271.png]]

Measure the resistance from the SAE J1939 datalink (shield) pin, if available, to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

![[19c01215.png]]

Remove the test lead from the SAE J1939 datalink (shield) pin and insert it into the SAE J1939 datalink negative (-) pin of the OEM harness connector. Insert the other test lead into another pin in the connector. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

![[19c01271.png]]

Measure the resistance from the SAE J1939 datalink negative (-) pin of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more) at all pins, except the J1939 datalink positive (+) pin.

If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

Connect all the components after the repair is complete.

![[19c01215.png]]
