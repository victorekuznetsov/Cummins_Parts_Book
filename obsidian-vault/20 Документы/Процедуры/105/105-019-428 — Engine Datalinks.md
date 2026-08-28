---
aliases:
  - "Шины данных двигателя"
type: "Процедура"
doc: "105-019-428"
title_en: "Engine Datalinks"
title_ru: "Шины данных двигателя"
modified: "2023-02-28"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
  - "85017333"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "K19"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK23"
  - "QSK60"
  - "QST30"
manuals:
  - "3666070"
  - "3666113"
  - "3666214"
  - "3666266"
  - "4021442"
figures: 31
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-019-428.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/105-019-428.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/K19"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "группа/105"
---

# Engine Datalinks
**Шины данных двигателя**

> [!abstract] Процедура · `105-019-428`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, K19, NT/NTA855 · ISM/QSM11, QSK23, QSK60, QST30
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]], [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2023-02-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-019-428.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/105-019-428.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Digital multimeter, Part Number 3164489

#### Additional Service Items

- Appropriate test lead(s)

### General Information

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

The engine data link consists of circuitry located in the engine wiring harness which transmits digital information between the engine control module (ECM) and other devices on the engine and chassis. On older engines, the engine data link circuitry supports J1587/J1708 protocol. On newer engines, the engine data link circuitry supports J1939 protocol.

The engine data link provides an access point for a service tool, such as a recommended Cummins® electronic service tool or equivalent, to communicate with the ECM. A service tool can communicate with the ECM on the engine data link free from data link traffic from other electronic devices that can be present on the OEM data link.

The data link network on model year 2016 and newer engines can operate at either 250K baud or 500K baud rates. Baud rate refers to the speed at which information is broadcasted on a data link network. Only one baud rate can be set for any data link network. The default baud rate for model year 2016 and newer engines is 500K baud. The default baud rate for model year 2015 and older engines is 250K baud.

Applications equipped with data link networks capable of supporting 500K baud data link speeds are differentiated by the key pattern on the 9 pin data link connector. This connector is also a different color from the 9 pin connectors that support only 250K baud data link speeds. An adapter tool, Part Number 5299126, is available in order to connect to applications equipped with 500K baud data link networks through the 9 pin connector.

SAE J1939 Backbone Harness Overview:

SAE J1939 has strict guidelines that **must** be followed for successful communication. Understanding some fundamentals about SAE J1939 will help verify these guidelines are followed.

The main component of an SAE J1939 system is a backbone harness. The harness can be up to 40 m \[ 131 feet \] long. The backbone harness is terminated at each end with 120 ohm resistors.

A maximum of 30 different devices can be attached to the SAE J1939 backbone at once. Each device, such as the data link adapter, is connected to the backbone through a stub which can be up to 1 m \[ 3.2 feet \] in length. The stub connector is a 3-pin plug.

![[19802395.png]]

The terminating resistor caps (1) **must** be in place on the OEM backbone harness plugs (2) to maintain proper communication. Each resistor is 120 ohms and is located in a removable cap. This resistance is required when communicating with a recommended Cummins® electronic service tool or equivalent over the J1939 data link.

![[19802397.png]]

Some engine harnesses include a complete SAE J1939 backbone harness. If this backbone harness is supplied, connection to a recommended Cummins® electronic service tool or equivalent is accomplished either by a 9-pin data link connector (1), Part Number 4918416, or a 3-pin receptacle (2), Part Number 3165141.

To check for the J1939 backbone, turn the keyswitch to the OFF position. Measure the resistance from the SAE J1939 data link positive (+) pin to the SAE J1939 data link negative (-) pin of the 3-pin Deutsch™ connector.

The multimeter will show 60 ohms when the engine harness has provided a backbone on the data link bus.

![[19802614.png]]

If the engine harness does **not** supply the J1939 backbone harness and the data link connector is a 3-pin receptacle, a mini-backbone harness will have to be added.

![[19802394.png]]

Engine Data Link Connectors

The engine data link connector available on the engine harness will depend upon the data link circuitry in the engine harness and the vintage of the engine. Engine data link connectors available on Cummins® engines are summarized in the table below.

| Connector Type | Data Link Protocols Supported |
|---|---|
| 2 pin Weather Pack™ | J1587/J1708 |
| 3 pin Deutsch™ | J1939 |
| 6 pin Deutsch™ | J1587/J1708 |
| 9 pin Deutsch™ | J1587/J1708, J1939 |

![[nobox.png]]

Each connector type is described in more detail in the following information.

The 9 pin Deutsch™ connector can supply SAE J1587/SAE 1708 and SAE J1939 communications at 250k baud data link speed, and battery voltage. The following are pin-outs for the 9 pin connector:

| Type I (250k) |  |
|---|---|
| Pin | Signal |
| A | Ground |
| B | Unswitched Battery |
| C | J1939 data link (+) |
| D | J1939 data link (-) |
| E | J1939 data link (shield) (**not** applicable for Marine) |
| F | J1708 data link (+) |
| G | J1708 data link (-) |
| H | Open |
| J | Open |

![[19400739.png]]

A similar 9 pin Deutsch™ connector can also supply SAE J1939 communications at 500K baud data link speed, and battery voltage. The following are pin-outs for the 9 pin connector:

| Type II Green (500K) |  |
|---|---|
| Pin | Signal |
| A | Ground |
| B | Unswitched Battery |
| C | J1939 data link (+) |
| D | J1939 data link (-) |
| E | J1939 data link (shield) (**not** applicable for Marine) |
| F | J1708 data link (+) |
| G | J1708 data link (-) |
| H | Open |
| J | Open |

![[19r99337.png]]

The 6 pin Deutsch™ connector, Part Number 3824805, is found on some engines. This connector supplies SAE J1587/J1708, as well as the battery voltage. The following are pin-outs for the 6 pin connector:

| Pin | Signal |
|---|---|
| A | J1708 data link (+) |
| B | J1708 data link (-) |
| C | Unswitched battery (+) |
| D | Open |
| E | Ground |
| F | Open |

![[19400740.png]]

> [!note] Note · Примечание
> For CELECT Plus™ engines, do **not** use the in-cab 6-pin data link connector to calibrate the ECM. Use the data link connector found on the engine.

![[19400418.png]]

The 3 pin SAE J1939 Deutsch™ connectors are also found on some Cummins® engine harnesses. Two possible types of 3 pin connectors can be present: A 3 pin plug (1), Part Number 3824288; and a 3 pin receptacle (2), Part Number 3824290. The following are the pin-outs for the 3 pin connector:

| Pin | Signal |
|---|---|
| A | J1939 data link (+) |
| B | J1939 data link (-) |
| C | J1939 data link (shield) |

The 3-pin connector **only** supports the SAE J1939 data link.

To meet the SAE J1939 standard, the 3 pin receptacle connector **must** be within 0.66 m \[ 2.16 feet \] of the ECM. Use of the J1939 mini-backbone harness, Part Number 3163096, may be required for proper termination resistance. The mini-backbone harness is required when **no** backbone is provided on the data link. Gender changer cable, Part Number 3163597, may be required to connect the mini-backbone harness to the engine harness or service tool cable.

> [!note] Note · Примечание
> If there is 60 ohm resistance measured between pins A and B of the 3 pin connector, a backbone is on the data link.

![[19802392.png]]

The 2 pin connector is on many older engines, and **only** supplies SAE J1587/J1708 support (no battery voltage supply). The following are the pin-outs for the 2 pin connector:

| Pin | Signal |
|---|---|
| A | J1587/J1708 data link (+) |
| B | J1587/1708 data link (-) |

![[19400406.png]]

Some engines have a 2 pin service tool power supply Weather Pack™ receptacle located in the engine harness. The connector can be used to power up any service tool device.

| Pin | Signal |
|---|---|
| A | Unswitched battery (+) |
| B | Ground (-) |

![[ee8coge.png]]

### Resistance Check

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> For the J1939 engine data link, use test lead, Part Number 3822758, on the ECM connector to avoid damage to the connector pins. Use test lead, Part Number 3824811, for the 9 pin Deutsch™ connector. Use test lead, Part Number 3823993 for the 3 pin Deutsch™ connector pin receptacle or test lead, Part Number 3823994 for the 3 pin Deutsch™ connector.

> [!warning] CAUTION · Осторожно
> For the J1587/J1708 engine data link, use test lead, Part Number 3622758, on the ECM connector to reduce the possibility of damage to the connector pins. Use test lead 3824800 for the 6 pin Deutsch™ connector. Use test lead 3823995 for the 2 pin Packard™ connector.

Determine the type of engine data link available on the engine, either J1939 or J1587/J1708. Follow the instructions provided to measure the resistance for the type of engine data link identified.

![[19802614.png]]

J1939 Engine Data Link

- Disconnect the batteries.
- Disconnect the engine harness connector from the ECM. Turn the keyswitch to the OFF position.

![[19c01212.png]]

Insert a test lead into the SAE J1939 data link positive (+) pin of the engine harness ECM connector, and connect the test lead to the multimeter probe. Insert the other test lead into the SAE J1939 data link positive (+) pin of the 3 pin or 9 pin Deutsch™ connector, and connect the test lead to the multimeter.

Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[nobox.png]]

Insert the multimeter lead into the SAE J1939 data link negative (-) of the engine harness ECM connector. Touch the other lead to the SAE J1939 data link negative (-) pin of the 3 pin or 9 pin Deutsch™ connector. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[nobox.png]]

If the values are correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin-to-pin.

Remove the test lead from the SAE J1939 data link negative (-) pin of the engine harness ECM connector and insert the test lead into the SAE J1939 data link (shield) pin. Touch the negative multimeter lead to the SAE J1939 data link (shield) pin of the 3 pin or 9 pin Deutsch™ connector. Measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less). If more than 10 ohms are measured in any of these steps, there could be an open circuit in the SAE J1939 data link (shield) pin, the SAE J1939 data link negative (-) pin, or the SAE J1939 data link positive (+) pin, or the polarity is **not** correct.

![[19c01212.png]]

J1587/J1708 Engine Data Link

Turn the keyswitch to the OFF position. Disconnect the engine harness from the ECM.

Insert a test lead into the SAE J1587 data link positive (+) pin of the engine harness ECM connector and connect the test lead to a multimeter probe. Insert the other test lead into the SAE J1587 data link positive (+) pin of the 2 pin or 6 pin connector and connect the test lead to the other multimeter probe. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[19c01188.png]]

Remove the test lead from the SAE J1587 data link positive (+) pin and insert the test lead into the SAE J1587 data link negative (-) pin of the ECM connector. Remove the other test lead from the SAE J1587 data link positive (+) pin and insert the test lead into the SAE J1587 data link negative (-) pin of the 2 pin or 6 pin connector. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[nobox.png]]

Remove the test lead from the SAE J1587 data link negative (-) pin and insert the test lead into the battery negative (-) pin of the 6 pin Deutsch™ connector. Remove the test lead from the SAE J1587 data link negative (-) pin of the engine connector and disconnect the test lead from the multimeter probe. Touch the multimeter probe to the engine block ground. Measure the resistance. The multimeter should show a closed circuit (10 ohms or less).

If the circuit is not closed, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[nobox.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> Use test lead, Part Number 3824811, for the 6 pin Deutsch™ connector.

Disconnect the batteries.

Measure the resistance from the positive (+) battery terminal to battery positive (+) of the 6-pin Deutsch™ connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

If the values are correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin-to-pin.

![[19c01191.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> For the J1939 engine data link, use test lead, Part Number 3822758, on the ECM connector to avoid damage to the connector pins.

> [!warning] CAUTION · Осторожно
> For the J1587/J1708 engine data link, use test lead, Part Number 3822758, on the ECM connector to avoid damage to the connector pins.

Determine the type of engine data link available on the engine, either J1939 or J1587/J1708. Follow the instructions provided for short circuit to ground check for the type of engine data link identified.

J1939 Engine Data Link

Disconnect the engine harness connector from the ECM. Insert a test lead into SAE J1939 data link positive (+) pin of the engine harness ECM connector and connect the test lead to a multimeter probe. Touch the other multimeter probe to engine block ground.

Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[19c01270.png]]

Remove the test lead from the SAE J1939 data link positive (+) pin and insert the test lead into the SAE J1939 data link negative (-) pin of the ECM connector. Measure the resistance from the SAE J1939 data link negative (-) pin of the engine harness ECM connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

If less than 100k ohms is measured in any of the previous steps, there is a short to circuit to ground. Repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[19c01270.png]]

J1587/J1708 Engine Data Link

Disconnect the engine harness connector from the ECM.

Insert a test lead into the SAE J1587 data link positive (+) pin of the engine harness ECM connector and connect the test lead to a multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[19202568.png]]

Remove the test lead from the SAE J1587 data link positive (+) pin and insert the test lead into the SAE J1587 data link negative (-) pin of the engine harness ECM connector. Touch the other multimeter probe to the engine block ground. Measure the resistance from the SAE J1587 data link negative (-) pin of the engine harness ECM connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[nobox.png]]

### Check for Short Circuit from Pin-to-Pin

> [!warning] CAUTION · Осторожно
> For the J1939 engine data link, use test lead, Part Number 3822758, on the ECM connector to avoid damage to the connector pins.

> [!warning] CAUTION · Осторожно
> For the J1587/J1708 engine data link, use test lead, Part Number 3822758, on the ECM connector to avoid damage to the connector pins.

J1939 Engine Data Link

Disconnect the engine harness connector from the ECM.

Insert a test lead into the SAE J1939 data link positive (+) pin of the engine harness ECM connector and connect the test lead to the multimeter probe. Insert the other test lead into another pin in the connector of the engine harness ECM connector and connect the test lead to the other multimeter probe.

Measure the resistance from the SAE J1939 data link positive (+) pin to the first pin in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[19c01272.png]]

Remove the lead from the first pin in the connector and measure the resistance from the SAE J1939 data link positive (+) pin of the engine harness ECM connector to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the circuit is **not** open, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[nobox.png]]

Remove the test lead from the J1939 data link positive (+) pin and insert the test lead into the J1939 data link (shield) pin of the engine harness ECM connector. Insert the other test lead into another pin in the connector. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

Measure the resistance from the SAE J1939 data link (shield) pin to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[nobox.png]]

Remove the test lead from the SAE J1939 data link (shield) pin and insert the test lead into the SAE J1939 data link negative (-) pin of the engine harness ECM connector. Insert the other test lead into another pin in the connector. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

Measure the resistance from the SAE J1939 data link negative (-) pin of the engine harness connector to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[nobox.png]]

J1587/J1708 Engine Data Link

Disconnect the engine harness connector from the ECM.

Insert a test lead into the SAE J1587 data link positive (+) pin of the engine harness ECM connector and connect the test lead to the multimeter probe. Insert the other test lead into another multimeter probe. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[nobox.png]]

Remove the lead from the first pin in the connector and test all other pins in the connector. Measure the resistance from the SAE J1587 data link positive (+) pin of the engine harness ECM connector to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (100k ohms or more).

Remove the test lead from the SAE J1587 data link positive (+) pin of the engine harness ECM connector and insert the test lead into the SAE J1587 data link negative (-) pin.

Measure the resistance from the SAE J1587 data link negative (-) pin to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the circuit is **not** open, repair or replace the engine harness.

See the Troubleshooting and Repair manual for additional information.

![[19c01272.png]]
