---
aliases:
  - "Сервисный инструмент и оснастка — обзор"
type: "Процедура"
doc: "00-022-999"
title_en: "Service Tools and Hardware - Overview"
title_ru: "Сервисный инструмент и оснастка — обзор"
modified: "2023-09-06"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33239746"
  - "33239899"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41349633"
  - "41353297"
  - "41370103"
  - "85017333"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "K19"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK19"
  - "QSK23"
  - "QSK60"
  - "QST30"
manuals:
  - "3666070"
  - "3666113"
  - "3666214"
  - "3666266"
  - "4021442"
  - "4022094"
  - "4022102"
figures: 18
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-022-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-022-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/K19"
  - "двигатель/K38/K50"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "группа/00"
---

# Service Tools and Hardware - Overview
**Сервисный инструмент и оснастка — обзор**

> [!abstract] Процедура · `00-022-999`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, K19, K38/K50 · QSK38, QSK50, QSK60, NT/NTA855 · ISM/QSM11, QSK19, QSK23, QSK60, QST30
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]], [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]], [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2023-09-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-022-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-022-999.pdf)

### General Information

Cummins Inc. produces many engines that are electronically controlled. These engines have special diagnostic requirements for the engine control module (ECM) in the system. To interface with the ECMs, electronic service tools have been developed.

The recommended Cummins® electronic service tool or equivalent interfaces with the electronic engines via a data link. A data link provides a means of transmitting and sorting electric signals, and consists of special electronic circuitry and electrical harnesses. Connection points from electronic service tools are also part of the data link. An original equipment manufacturer (OEM) data link, if available, is provided by the OEM and consists of circuitry located in the OEM harness. An engine data link consists of circuitry located in the engine harness. Both engine and OEM data links alike are defined by standards written by the Society of Automotive Engineers (SAE). Cummins Inc. uses two such standards for electronic service tools. One is a combination of SAE J1587 and SAE J1708 and the other is SAE J1939. The J1939 data link is described in more detail in Procedure 019-165 in the appropriate engine service manual. The J1587/J1708 data link is described in more detail in Procedure 019-166 in the appropriate service manual, and is hereafter referred to as J1708 in this document. Engine data links (both J1939 and J1708) are discussed in more detail in Procedure 019-428 in the appropriate engine service manual.

### Electronic Service Tool Description

The recommended Cummins® electronic service tool, or equivalent, is a Windows® based software application that works with Cummins® ECMs to diagnose and troubleshoot engine problems, store and analyze historical information about an engine, and to modify an engine's operating values. The electronic service tool Professional also enables you to transfer calibrations to an ECM.

The electronic service tool is used on a personal computer (PC) that is attached to an ECM through an INLINE™ data link adapter kit.

1. The INLINE™, INLINE™ I, INLINE™ 2, INLINE™ 4, and INLINE™ 5 adapters have become obsolete. They can be used with the electronic service tool, but technical support for these adapters is not available.

After registering a copy of the electronic service tool and connecting to an ECM data source, the electronic service tool enables you to retrieve present or recorded data about an engine, alter ECM settings, store data for viewing at a later time, analyze data to monitor and assess the operation of an engine, and view active or inactive engine fault codes.

The electronic service tool is installed in the INTELECT™ folder on the hard drive of a personal computer. User manuals are available in the INTELECT™ and Manuals folder for specific Cummins® electronic engines. Additional information for service and support from a Cummins® distributor for the electronic service tool questions is included in the front of the user manuals.

Different versions of the electronic service tool may be available for use at one time, although some electronic service tool versions may **not** be compatible with some ECMs. ECM and electronic service tool compatibility information is available at the Product website. Electronic service tool improvements are sometimes released as Feature Packs. The latest Feature Pack information for specific electronic service tool versions is also available at the electronic service tool product website. Maintain the electronic service tool with the latest versions and Feature Packs that become available.

The electronic service tool can utilize either a communication port (COM port), universal serial bus (USB), WIFI, or Bluetooth connection on the PC when communicating with an ECM. A COM port **must** be configured properly for the electronic service tool to function correctly. Other software programs on the PC can take control of a COM port and prevent the electronic service tool from accessing the COM port. Troubleshooting information for the electronic service tool communication issues is available in the base user manual and also in the ECM No Communication Troubleshooting Tree on QuickServe™ Online or Intercept.

### Initial Check

#### Electronic service tool

- In the main electronic service tool window, verify that the data link selected in the ECM Data Source Connection drop-down matches the data link hardware being used
- Verify the correct version is installed. The version can be determined from the main window by selecting Help, About.
- Verify the infrared port is disabled so the serial port is **only** being used for ECM communications.
- If you have the Palm Pilot Hot Sync Manager on a PC that **only** has one serial port, you **must** disable the Hot Sync Manager before connecting to an ECM.

#### Data Link Adapters

- Check the firmware version of the INLINE™ data link adapter is the latest firmware version available.
- Verify that the data link adapter being used is compatible with the data link wiring available on the engine or vehicle.

- A data link adapter is a device that converts the J1708, or J1939 data link messages from the ECM into a message that a PC can process. Because the electronic service tool is a PC based tool, a data link adapter is required to troubleshoot engines.
- Cummins® Service Products offer the following data link adapter kits:

- The following illustration shows INLINE™ data link adapters.

Power for the INLINE™ data link adapters depends upon the communication setup in use. The 12 VDC power is supplied by the vehicle power system for the vehicle and engine communication setups. The 12 VDC power is supplied by an auxiliary power supply for the bench communication setup.

The INLINE™ data link adapter will support either J1708 or J1939 protocol. When connecting with the electronic service tool using an INLINE™ data link adapter, the electronic service tool will attempt to establish communication with an ECM on J1939 first. If no communication is established on J1939, the electronic service tool will then attempt to establish communication on J1708.

![[22800616.png]]

Data Link Adapter Identification Diagram - INLINE™ 4.

1. Power light
2. J1939 communication light
3. J1708 communication light
4. RS-232 to PC light.

The INLINE™ 4 is an RP1210A compliant data link adapter that will support both J1708, and J1939 protocol. RP1210A is an industry wide standard that defines data link message format for service tools. The INLINE™ 4 **must** be configured correctly within the electronic service tool to define the COM port being used on the PC and the type of data link protocol that is available, J1708, J1939, or autodetect.

![[22800617.png]]

Data Link Adapter Identification Diagram - INLINE™ 5.

1. Power light
2. J1939 communication light
3. J1708 communication light
4. RS-232 to PC light
5. USB to PC light.

The INLINE™ 5 is an RP1210A compliant data link adapter that will support both J1708, and J1939 protocol. The adapter can be used with either a COM port or USB port. The INLINE™ 5 **must** be configured correctly within the electronic service tool to define the COM or USB port being used on the PC and the type of data link protocol that is available, J1708, or J193, or autodetect.

![[22r00008.png]]

Data Link Adapter Identification Diagram - INLINE™ 6

1. Power light
2. CAN 1 communication light (J1939)
3. CAN 2 communication light (J1939)
4. J1708 communication
5. RS-232 to PC light
6. USB to PC light.

The INLINE™ 6 is an RP1210A compliant data link adapter that will support both J1708 and J1939 protocols. The adapter can be used with either a COM port or USB port. The INLINE™ 6 **must** be configured correctly within the electronic service tool to define the COM or USB port being used on the PC and the type of data link protocol that is available, J1708, J1939, or autodetect.

![[19r99367.png]]

Data Link Adapter Identification Diagram - INLINE™ 7

1. Power light
2. Communication light
3. Communication-type light/indicator
4. Fault light.

The INLINE™ 7 is an RP1210A, RP1210B, and RP1210C compliant data link adapter that will support J1587/J1708 as well as J1939 (250K, 500K, or 1MB Baud Rate). The adapter can **only** be connected to the PC via USB, WIFI, or Bluetooth connection. The tool **must** be configured correctly within the electronic service tool to define the connection type on the PC and the type of data link protocol that is available, either J1587/J1708 or J1939.

The INLINE™ data link adapters require firmware software in order to operate correctly. Firmware versions are updated periodically and **must** be uploaded into data link adapters when updates are released. The latest firmware version is always available on the most recent INCAL™ DVD-ROM as well as from the website http://cumminsengines.com/inline. The firmware version for a data link adapter can be found within the recommended Cummins electronic service tool or equivalent. When using the electronic service tool, the firmware version is displayed at the lower right corner of the main window when connected to an ECM. The electronic service tool **must** be connected to an ECM in order for the firmware version to be displayed.

### Setup

General Information

Communication with the ECM can be established at three basic locations:

- Bench communication setup
- Vehicle communication setup
- Engine communication setup.

The communication setups are described in more detail in the remainder of this procedure. Each location utilizes different data link adapter cables. All three locations require either a serial cable, USB cable, WIFI, or Bluetooth connection to interface from the data link adapter to the PC. Reference the table below.

The ECM on newer engines can support data link communication on the OEM data link through the OEM connector at the ECM. The ECM can also support data link communication on the engine data link through the engine connector at the ECM. The wiring diagram for a specific engine and ECM **must** be consulted to determine if an ECM supports both OEM data link and engine data link communication.

For Midrange and Heavy Duty engines, the recommended communication setup, if available, is the Cummins Inc. bench communication setup which establishes communication directly to the ECM. The bench communication setup can support both J1708 and J1939 data link protocols, when used with ECMs that support both protocols.

For High Horsepower engines with multiple ECMs, the recommended communication setup is the engine communication setup through the 9 pin connector provided in the engine harness.

J1939 data link communication, if available, is preferred for transferring calibrations because of less interference from other data link devices such as traction control systems and electronic dashes. J1708 communication can require extra time to disable the OEM ECMs that are also communicating on the J1708 data link in order to avoid interference from those devices. Also, the J1939 information transfer rate is faster than J1708 and a calibration download will take less time to complete using J1939 communication compared to J1708 communication.

The functionality of a communication setup can be verified by testing the communication setup on a second ECM or vehicle, if available, or by completing the resistance checks defined for each setup type.

The following table summarizes the ECM communication setups.

| Communication Setup | Data Link Connection Location | Engine ECM data link Source | Data Link Protocols Supported |
|---|---|---|---|
| Bench | ECM connector | OEM | J1708, J1939 |
| Vehicle 6 pin | Dash 6 pin connector | OEM | J1708 |
| Vehicle 9 pin | Dash 9 pin connector | OEM | J1708, J1939 1 |
| Engine | Engine harness 3 pin connector | Engine | J1939 |
| Engine | Engine harness 6 pin connector | Engine | J1708 2 |
| Engine | Engine harness 9 pin connector | Engine | J1939 3 |

#### Notes:

1. The 9 pin connector **must** be fully wired to support J1939 protocol.
2. Available **only** on selected older engines.
3. Available **only** on selected High Horsepower engines.

Bench Communication Setup

The bench communication setup establishes communication directly with the ECM through the connector port on the ECM. An example of a bench communication setup is shown below.

The bench calibration harness (1) is common for most bench setups and can be used with the appropriate bench calibration cable (5) to communicate with various ECMs. A list of available bench calibration cables (5) for various ECMs is included in Service Tool Instruction, Bulletin 3377791, which is accessible on QuickServe™ Online. Proper function of the bench calibration harness (1) and bench calibration cable (5) can be verified by using the wiring diagrams provided to complete resistance checks.

![[22800563.png]]

Bench Communication Setup

1. Bench calibration harness, Part Number 3163151
2. Power supply 1
3. Electronic service tool
4. Data link adapter
5. ECM 1 bench calibration cable
6. USB cable, Part Number 4918591, or serial cable, Part Number 4918418 (reference table above for cable type)
7. Data link adapter cable, Part Number 3165159 (INLINE™ 4, 5, and 6
8. CM570 ECM (example).

1. See Service Tool Instruction, ECM Bench Calibration Base Harness, Bulletin 3377791, for part number.

Vehicle Communication Setup

An additional communication setup is a 9 pin or 6 pin Deutsch™ connection that is commonly located in the cab of a vehicle. The vehicle communication setup utilizes the OEM harness and connects to the ECM at the OEM connector port. A 9 pin connector in the cab, if fully wired, is capable of supporting both J1939 and J1708 protocol. Some OEMs place a 9 pin connector in the cab but do **not** provide wiring to support J1939 protocol. A 6 pin connector will **only** support J1708 protocol.

![[22800562.png]]

On Vehicle Communication Setup

1. Data link adapter
2. USB cable, Part Number 4918591, or serial cable, Part Number 4918418 (reference table above for cable type)
3. Data link adapter cable 1
4. Electronic service tool
5. Vehicle data link adapter connector 1.

1. See Service Tool Instruction, ECM Bench Calibration Base Harness, Bulletin 3377791, for part number.

INLINE™ 6 data link networks equipped to support 500K baud data link speeds require an adapter tool, Part Number 5299126, to connect to the 9 pin connector.

Only the INLINE™ 6 and INLINE™ 7 are capable of supporting data link speeds of 500K baud. The INLINE™ 4 and INLINE™ 5 do **not** support 500K baud data link speeds.

Engine Communication Setup

The engine communication setup utilizes the engine data link provided on the engine wiring harness. Depending upon the engine, the engine communication setup available on the engine harness can be a 3 pin Deutsch™ connector, a 6 pin Deutsch™ connector, or a 9 pin Deutsch™ connector.

A 3 pin Deutsch™ connector on the engine harness is available on newer engines and provides a connection point to the J1939 data link. A mini-backbone cable, which includes a 60 ohm resistor and a gender changer cable, may be required in order to connect to the ECM on the J1939 protocol. An auxiliary power supply is required for the data link adapter.

![[22800620.png]]

3 Pin Deutsch™ Connector

1. Data link cable 1
2. Power supply cable 1
3. Electronic service tool
4. Data link adapter
5. Gender changer cable, Part Number 3163597
6. Mini-backbone cable, Part Number 3163096
7. USB cable, Part Number 4918591, or serial cable, Part Number 4918418 (reference table above for cable type)
8. Engine harness 3 pin connector, Part Number 3165141.

1. See Service Tool Instruction, ECM Bench Calibration Base Harness, Bulletin 3377791, for part number.

A 6 pin Deutsch™ connector is available on the engine harness for some older engines and provides a connection point to the engine J1939 data link. The 6 pin connector includes a power supply for the data link adapter.

### Resistance Check

A serial cable is required to interface from the data link adapter to the PC, or a USB cable can be used with an INLINE™ 5/6/7 data link adapter.

> [!warning] CAUTION · Осторожно
> Use test lead, Part Number 3822758, and test lead, Part Number 3822917, to avoid the possibility of damage to the serial cable pins.

![[22800565.png]]

Serial Cable, Part Number 4918418

1. Open
2. Transmit data
3. Receive data
4. Data terminal ready (+5 VDC)
5. Signal ground
6. Open
7. Request to send (+5 VDC)
8. Clear to send
9. Open.

- Insert a test lead into pin 1 of the female end of the serial cable, and connect lead to the multimeter probe. Attach the other test lead to pin 1 of the male end of the serial cable, and connect lead to the multimeter probe.
- Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). Repeat the resistance measurement for pins 2 through 9. The multimeter **must** show a closed circuit (10 ohms or less) for each pin. If the circuit is **not** closed, replace the serial cable.

> [!warning] CAUTION · Осторожно
> To avoid the possibility of damage to connector pins, use test lead, Part Number 3823993, on the 8 pin connector. Use test lead, Part Number 3823994, on the round 9 pin connector. Use test lead, Part Number 3824812, on the 3 pin connector.

![[22800618.png]]

Bench Calibration Harness, Part Number 3163151

1. J1939 data link (+)
2. J1939 data link shield
3. Battery (+)
4. Battery (-)
5. Keyswitch
6. J1939 data link (-)
7. J1708 data link (+)
8. J1708 data link (-)

- Measure the resistance from each pin in the 8 pin connector to the corresponding location in the 9 pin and/or 3 pin connector. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the bench calibration harness.

> [!warning] CAUTION · Осторожно
> To avoid the possibility of damage to connector pins, use test lead, Part Number 382994, on the 8 pin connector. Determine the appropriate test lead needed for the ECM connector on the bench calibration cable.

![[22800619.png]]

Bench Calibration Cable

1. J1939 data link (+)
2. J1939 data link shield
3. Battery (+)
4. Battery (-)
5. Keyswitch
6. J1939 data link (-)
7. J1708 data link (+)
8. J1708 data link (-).
9. ECM Connector (See wiring diagram for ECM connector pin identification).

- Measure the resistance from each pin in the 8 pin connector to the corresponding location in the ECM connector. See wiring diagram for the ECM for connector pin identification. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the bench calibration cable.

> [!warning] CAUTION · Осторожно
> To avoid the possibility of damage to connector pins, use male test lead, Part Number 3823993, on the 9 pin Deutsch™ connector. Use male test lead, Part Number 3822758, on the 25 pin connector.

![[22800621.png]]

![[19400739.png]]

9 Pin Data Link Cable, Part Number 3165159

9 Pin In-Cab Data Link Connector

- A. Ground
- B. Battery (+)
- C. J1939 data link (+)
- D. J1939 data link (-)
- E. J1939 data link shield
- F. J1708 data link (+)
- G. J1708 data link (-)
- H. Open
- J. Open

- Measure the resistance from pins A, B, C, D, E, F, and G in the 9 pin connector to the corresponding location in the 25 pin connector, as shown. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the data link cable.

> [!warning] CAUTION · Осторожно
> To avoid the possibility of damage to connector pins, use male test lead, Part Number 3824811, on the 6 pin Deutsch™ connector. Use male test lead, Part Number 3822758, on the 25 pin connector.

![[05800054.png]]

![[19400740.png]]

6 Pin Data Link Cable, Part Number 3165160

6 Pin In-Cab Data Link Connector

1. J1708 data link (+)
2. J1708 data link (-)
3. Battery (+)
4. Open
5. Ground
6. Open.

- Measure the resistance from pins A, B, C, and E in the 6 pin connector to the corresponding location in the 25 pin connector, as shown. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the data link cable.

> [!warning] CAUTION · Осторожно
> To avoid the possibility of damage to the connector pins, use male test lead, Part Number 3822758, on the 25 pin connector. Use female test lead, Part Number 3823994, on the 3 pin connector. Use male test lead, Part Number 3822995, on the 2 pin power connector.

![[22800568.png]]

3 Pin Data Link Cable, Part Number 3165141

- Measure the resistance from pins A, B, and C in the 3 pin connector to the corresponding location in the 25 pin connector, as shown. Measure the resistance from pins D and E in the 2 pin power supply connector to the corresponding location in the 5 pin connector, as shown. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the data link cable.

> [!warning] CAUTION · Осторожно
> To avoid the possibility of damage to connector pins, use two male test leads, Part Number 3823993, on each 3 pin connector.

![[19803849.png]]

Mini Backbone Cable, Part Number 3163096

- Measure the resistance from pin A in one end of the backbone cable to pin A in the opposite end of the backbone cable. Repeat for pins B and C. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the backbone cable. Measure the resistance across pins A and B at either end of the cable to measure the terminating resistance. The terminating resistance value **must** measure between 50 to 70 ohms.

> [!warning] CAUTION · Осторожно
> To avoid the possibility of damage to connector pins, use two female test leads, Part Number 3823994, on each 3 pin connector.

![[19901672.png]]

Gender Changer Cable, Part Number 3163597

- Measure the resistance from pin A in one end of the gender changer cable to pin A in the opposite end of the gender changer cable. Repeat for pins B and C. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the gender changer cable.

> [!warning] CAUTION · Осторожно
> To avoid the possibility of damage to connector pins, use two male test leads, Part Number 3164113, on the 26 pin connector to the INLINE™ 7. Use male test lead, Part Number 3824811, on the 6 pin Deutsch™ connector. Use male test lead, Part Number 3823993, on the 9 pin Deutsch™ connector.

![[19r99368.png]]

INLINE™ 7 Data Link Cable

#### 6 Pin Deutsch™ Connector Troubleshooting

- Measure the resistance from pins A, B, C, and E in the 6 pin connector to the corresponding location in the 26 pin connector, as shown. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the data link cable.

#### 9 Pin Deutsch™ Connector Troubleshooting

- Measure the resistance from pins A, B, C, D, E, F, and G in the 9 pin connector to the corresponding location in the 26 pin connector, as shown. The multimeter **must** show a closed circuit (10 ohms or less). If a circuit is **not** closed, replace the data link cable.
