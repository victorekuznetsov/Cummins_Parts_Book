---
type: "Процедура"
doc: "513-015-999"
title_en: "Instruments and Controls - Overview"
modified: "2025-06-05"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
figures: 13
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Instruments and Controls - Overview

> [!abstract] Процедура · `513-015-999`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2025-06-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-999.pdf)

### General Information

The Marine C Command Connect and C Command Connect Premier Panel System is used to monitor various vessel sensors, basic engine operating characteristics, and to control engine start and stop functions. The display is capable of receiving engine, generator set, and transmission information from the engine control module (ECM) via Society of Automotive Engineers (SAE) J1939 or National Marine Electronics Association (NMEA) 2000 data link. The helm display receives vessel and transmission sensor NEMA 2000 information from the customer interface box (CIB) display. The C Command Connect and Connect Premier panel system is comprised of the following components, which may or may **not** be supplied by Cummins Inc.:

- Engine interface wiring harness (Cummins Inc. supplied **only**)
- CIB (with or without ED-4 display) (Cummins Inc. supplied **only**)
- Display (Cummins Inc. or original equipment manufacturer (OEM)-supplied)
- Drive application wiring harness (Cummins Inc. or OEM-supplied)
- Water in fuel sensor extension wiring harness (Cummins Inc. or OEM-supplied)
- Main extension wiring harness and Tee (Cummins Inc. or OEM-supplied)
- Helm wiring harness (includes data link connector) (Cummins Inc. or OEM-supplied)
- System enable switch (Cummins Inc. or OEM-supplied)
- Start switch (Cummins Inc. or OEM-supplied)
- Stop switch (Cummins Inc. or OEM-supplied)
- Start / Stop Switch, single quick press (PS103) (Cummins Inc. or OEM-supplied)
- External alarm horn (Cummins Inc. or OEM-supplied)
- Dimmer (OEM supplied **only**)
- Throttle adapter wiring harness (Cummins Inc. or OEM-supplied)
- Transmission gear oil pressure and temperature sensor adapter wiring harness, if equipped. (Cummins Inc. or OEM-supplied)
- OEM interface wiring harness (Cummins Inc. or OEM-supplied)
- OEM sensor wiring harness (Cummins Inc. or OEM-supplied)
- Display adapter wiring harness (Cummins Inc. or OEM-supplied). **Note:** The Marine C Command Connect and Connect Premier Panel System requires the OEM to use a Cummins Inc. designed CIB and engine interface harness. The remaining system components (displays, sensors, e.g.) and wiring harnesses can be designed and procured by the OEM as long as the components meet the Cummins® application engineering guidelines and pass installation quality assessment.

Wiring Harnesses:

The C Command Connect and Connect Premier system uses multiple wiring harnesses. The J1939 backbone has terminating resistors on each end, typically one behind the farthest helm dash and one on the engine.

- Engine interface wiring harness: Harness interface for the engine CIB, throttle, and ECM power
- Drive application wiring harness (PS102): Harness connections for system enable, exhaust temperature, neutral safety, and transmission gear oil cooler pressure and temperature sensor
- Drive application wiring harness (PS103): Harness connections for system enable, exhaust temperature, neutral safety sensor
- Water in fuel sensor extension wiring harness: Harness connects the OEM interface wiring harness to the water in fuel sensor
- OEM interface wiring harness: Harness connects to CIB for water in fuel, throttle, fire suppression, idle validation, and neutral safety signals. This harness can either have standard wiring connectors or a terminal strip.
- OEM sensor wiring harness: Harness connects CIB to OEM sensors by terminal strip.
- Main extension wiring harness: Harness connects CIB to the helm wiring harness(s)
- Main extension wiring harness tee: Extension connection for additional helm wiring harness.
- Helm wiring harness: Harness connects to main extension wiring harness for connection to the display adapter wiring harness, switches (system enable, start, and stop), external alarm horn, and J1939 3-pin connector with terminating resistor (if it is the end of the datalink).
- Display adapter wiring harness: Harness connects the helm wiring harness to the display(s), dimmer, if equipped, and NMEA 2000, if equipped. This harness can be either a standard, advanced, or twin engine wiring harness design.
- Throttle adapter wiring harness: Connection to the throttle system
- Transmission gear oil pressure and temperature sensor adapter wiring harness, if equipped: Adapter harness connected to the drive application wiring harness for connection to the sensors typically located in the marine gear oil cooler.

Data Link Connector:

The 9 pin diagnostic connector is located on the engine near the ECM. If equipped, the 9 pin diagnostic connector could also be located at the helm of the vessel. Cummins Inc. produces many engines today that are electronically controlled. These engines have special diagnostic requirements because of the ECM in the system. To interface with these ECMs, electronic service tools have been developed, such as INSITE™ electronic service tool. INSITE™ electronic service tool interfaces with the electronic engines by means of a data link. A data link provides a physical means for transmitting and sorting electronic signals. A data link consists of special electronic circuitry and electrical harnesses. Connection points for electronic service tools are also part of the data link. Data links are defined by standards written by the SAE. Cummins Inc. uses two such standards for electronic service tools. One is a combination of SAE J1587/SAE J1708 and the other is SAE J1939. Engines can support one or both of these data link standards.

The recommended data link connector for Cummins® engines is a 9 pin Deutsch™ connector. This connector can supply SAE J1587/SAE J1708 and SAE J1939 communications and battery voltage. The following are pin-outs for the 9 pin connector:

| Pin | Signal |
|---|---|
| A | Battery Voltage 1 Return |
| B | Battery Voltage 1 Supply |
| C | SAE J1939 Data Link Supply |
| D | SAE J1939 Data Link Return |
| E | SAE J1939 Data Link Shield |
| F | **Not** Used |
| G | **Not** Used |
| H | **Not** Used |
| I | **Not** Used |

![[19400739.png]]

CIB:

There are two configurations of the CIB.

1. C Command Connect
2. C Command Connect Premier.

![[15e00014.png]]

The CIB is located in the engine room and receives engine data from the ECM through a 31 pin connector.

The engine receives start and stop commands through the CIB. The CIB can also receive OEM data from various vessel sensors.

The CIB contains the following:

1. Engine start and stop switch
2. ED-4 display (Connect Premier option **only**)
3. Circuit breakers
4. Battery positive connection lug
5. Polytetrafluoroethylene (PTFE) sealed membrane vent
6. Battery negative connection lug
7. J1939 3-pin connection
8. Main extension wiring harness connection
9. OEM sensor wiring harness connection (Connect Premier option **only**)
10. NMEA 2000 connection (Connect Premier option **only**)
11. OEM interface wiring harness connection
12. Engine interface wiring harness connection.

**Not** shown:

- Printed circuit board (PCB) (internal to CIB)
- Relays (internal to CIB).

![[15e00015.png]]

CIB Circuit Protection:

The CIB contains circuit breakers (1) to protect the system from over voltage. The circuit breakers are accessible on the side CIB.

The CIB printed circuit board (PCB) has auto-resetting fuses for the following. These fuses are **not** serviceable.

- Neutral safety
- Accessory relay
- Shutdown
- Auto/manual switching circuit
- XDRG (sensor ground).

Use the following for circuit breaker information. Refer to Procedure 018-021 in section V.

![[15e00016.png]]

CIB J1939 Data Link Connection:

The J1939 3 pin connection (1) on the CIB is typically used by the OEM to access data link information.

![[15e00017.png]]

CIB NMEA 2000 Data Link Connection:

The NMEA 2000 connection (1) on the CIB is typically used by the OEM to access datalink information.

![[15e00018.png]]

CIB Engine Start/Stop Switch:

The engine start/stop switch (1) allows direct engine start and stop from the CIB.

![[15e00019.png]]

CIB PCB and Relays:

The printed circuit board contain switches for voltage setup that should **not** be moved.

The relays connected to the printed circuit board are used for starter lockout, shutdown, and accessory relay.

The printed circuit board and relays are **not** serviceable.

![[15e00020.png]]

CIB ED-4 Display:

The ED-4 display (1) is connected with the ECM through a SAE J1939 data link. The display will indicate engine operating parameters and fault codes. The display is the gateway for relaying engine ECM information to NMEA 2000.

When mounted at the CIB, the display requires a unique software load for the C Command Connect Premier Panel System and is **not** common with other Cummins® controls systems.

The display software name and version is displayed on the screen after the system enable switch is turned ON and it can be found in the “About” menu screen.

The display comes preloaded with software and is updateable. Use the following procedure for information on software. [[513-015-107 — Display Software|Refer to Procedure 015-107 in Section 15.]]

When mounted at the CIB, the display's vessel personality file will need to be updated for each vessel application at initial install by the OEM or, if replaced, during a service event.

Use the following procedure for information on vessel personality files. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]

![[15e00021.png]]

Helm Components:

- System Enable Switch
- Start Switch (PS102)
- Stop Switch (PS102)
- Start / Stop Switch (PS103)
- Dimmer:
- External Alarm Horn:

ED-4 Display (Helm Mounted):

The display is typically connected to the ECM through a SAE J1939 data link. The display will indicate engine operating parameters and fault codes. The display is the gateway for relaying engine ECM information to NMEA 2000. When mounted at the helm, the display requires a unique software load for the C Command Connect and Connect Premier Panel System and is **not** common with other Cummins® controls systems.

The display software name and version is displayed on the ED-4 screen after the system enable switch is turned ON and it can be found in the “About” menu screen.

The display comes preloaded with software and is updateable. Use the following procedure for information on software. [[513-015-107 — Display Software|Refer to Procedure 015-107 in Section 15.]]

When mounted at the helm, the display's vessel personality file will need to be updated for each vessel application at initial install by the OEM or, if replaced, during a service event.

Use the following procedure for information on vessel personality files. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]

![[15e00022.png]]

ED-5 or ED-7 Display (Helm Mounted):

The display is a touch screen unit and is typically connected to the ECM through a SAE J1939 data link. The display will indicate engine operating parameters and fault codes. The display is the gateway for relaying engine ECM information to NMEA 2000.

The display software name and version is displayed on the ED-5 / ED-7 screen after the system enable switch is turned ON and it can be found in the “About” menu screen.

The display comes preloaded with software and display's vessel personality file and is field updateable if required. Use the following procedure for information on software. [[513-015-107 — Display Software|Refer to Procedure 015-107 in Section 15.]]

When mounted at the helm, the preloaded display's vessel personality file will need to be selected for each vessel application at initial install by the OEM or, if replaced, during a service event.

Use the following procedure for information on vessel personality files. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]

![[00e00312.png]]

Remote Keypad (Helm Mounted):

The optional remote keypad is connected to the ED-5 / ED-7 display through a SAE J1939 data link. The remote keypad enables to easily control touchscreen function of the display using the keys on the pad.

![[00e00313.png]]

MFD (Multifunction Display) (Helm-Mounted):

The MFD is connected with the engine ECM through a J1939 or NMEA 2000 data link.

The MFD will indicate engine operating parameters and fault information.

The MFD is typically **not** supplied by Cummins Inc. See equipment manufacturer service information for service or software updates.

![[15d00958.png]]
