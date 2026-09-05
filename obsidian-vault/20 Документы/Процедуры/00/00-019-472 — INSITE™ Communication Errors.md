---
type: "Процедура"
doc: "00-019-472"
title_en: "INSITE™ Communication Errors"
modified: "2017-03-14"
manuals:
  - "5411181"
figures: 11
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-019-472.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-019-472.pdf"
tags:
  - "документ/процедура"
  - "группа/00"
---

# INSITE™ Communication Errors

> [!abstract] Процедура · `00-019-472`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2017-03-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-019-472.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-019-472.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- No Cummins® service tools required.

#### Additional Service Items

- No additional service items required.

### General Information

Turn the keyswitch to the ON position.

- Verify the POWER lamp is illuminated on the data link adapter.

![[19c01704.png]]

Check the settings in INSITE™ electronic service tool that the data link adapter being connected is selected.

> [!note] Note · Примечание
> Use the Auto Configure function to assist with data link configuration.

Check the communication port selected for other devices.

If any are detected, disable. If necessary, contact administration support for assistance.

![[19800902.png]]

Inspect all the component connectors or cable connectors to make sure there is no pin damage.

#### On Vehicle Communication Setup

1. Data link adapter
2. Universal serial bus (USB) or personal computer (PC) serial cable
3. Data link adapter cable
4. PC with INSITE™ electronic service tool
5. Vehicle data link adapter connector.

Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection|Refer to Procedure 019-361 in Section 19.]]

- If damage is found, the component or cable **must** be repaired or replaced.
- Connect the cables to the computer, data link adapter, and vehicle.

![[22800562.png]]

#### Data Link Adapter Identification Diagram and Error Information

1. Data link adapter
2. USB or PC serial cable
3. Data link adapter cable
4. PC with INSITE™ electronic service tool (not shown)
5. Vehicle data link adapter connector.

Verify that the data link adapter is communicating with the selected protocol.

For INSITE™ electronic service tool errors 5200, 5202, and 5023:

- Verify that the power light is on or flashing.
- Verify the communication light is on or flashing when transferring information from the computer to the electronic control module (ECM).

For INSITE™ electronic service tool errors 5201 or 5204 (Data Link J1587/J1708 connections):

- Verify that the specified protocol light is flashing.

If it is **not** flashing, check the voltage level from the engine. Go to the appropriate wiring diagram for details.

![[19r99378.png]]

#### Data Link Adapter Identification Diagram - INLINE™ 4, 5, and 6.

1. Power light
2. J1939 communication light
3. J1708 communication light
4. RS-232 To PC light
5. USB To PC light (INLINE™ 5 and 6 **only**).

The INLINE™ 4, 5, and 6 is an RP1210A compliant data link adapter that will support both J1587/J1708, and J1939 protocol. It can be used with either a COM port or USB port. The INLINE™ 4, 5, and 6 **must** be configured correctly within INSITE™ electronic service tool to define the COM or USB port being used on the PC and the type of data link protocol that is available, either J1587/J1708, or J1939.

![[22800617.png]]

#### Data Link Adapter Identification Diagram - INLINE™ 7

1. Power light
2. Communication light
3. Communication-type light/indicator
4. Fault light.

The INLINE™ 7 is a RP1210A, RP1210B, and RP1210C compliant data link adapter that will support J1587/J1708 as well as J1939 (250K, 500K, or 1MB Baud Rate). It can **only** be connected to the PC via USB, WIFI, or Bluetooth connection. The tool **must** be configured correctly within INSITE™ electronic service tool to define the connection type on the PC and the type data link protocol that is available, either J1587/J1708 or J1939.

![[19r99367.png]]

#### On Vehicle Communication Setup

1. Data link adapter
2. USB or PC serial cable
3. Data link adapter cable
4. PC with INSITE™ electronic service tool
5. Vehicle data link adapter connector.

For Data Link J1939 connections:

- Verify that the selected protocol light is flashing.
- If it's **not** flashing, check the resistance measurement from the engine.
- Use the appropriate wiring diagram and the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter|Refer to Procedure 019-360 in Section 19.]]

![[22800562.png]]

> [!note] Note · Примечание
> There is no flashing light when using the 3 pin on-engine connector.

#### Mini Backbone Cable Pin Identification

1. J1939 data link supply
2. J1939 data link return
3. J1939 data link shield.

![[19803849.png]]

#### Data Link Adapter Identification Diagram - INLINE™ 4, 5, and 6.

1. Power light
2. J1939 communication light
3. J1708 communication light
4. RS-232 To PC light
5. USB To PC light (INLINE™ 5 and 6 **only**).

If a connection is **not** established, replace the data link adapter and cables to establish a connection.

![[22800617.png]]

#### Data Link Adapter Identification Diagram - INLINE™ 7

1. Power light
2. Communication light
3. Communication-type light/indicator
4. Fault light.

If a connection is **not** established, replace the data link adapter and cables to establish a connection.

![[19r99367.png]]

If after replacing the data link and cables, a connection is still **not** established:

- Close INSITE™ electronic service tool program
- Shut down the computer
- Inspect the the cables to the computer, data link adapter, and vehicle connection
- Start the computer
- Start the INSITE™ electronic service tool
- Attempt to communicate with the ECM.

If all steps have been completed and checked again, close INSITE™ electronic service tool and contact a Cummins® Authorized Repair Location.

![[19800902.png]]
