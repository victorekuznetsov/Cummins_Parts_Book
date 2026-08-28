---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "81-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2013-01-18"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 26
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `81-101-007`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2013-01-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-101-007.pdf)

### CENSE™ System Description

The CENSE™ system is an electronic engine monitoring system. This system is used primarily to provide enhanced engine diagnostics and to record engine operating data over time.

![[cent337.png]]

The CENSE™ engine control module (ECM) is physically identical to some other Cummins® engine control modules (ECMs). Refer to the ECM part numbers to tell the difference between ECMs. The ECM part number is shown on the ECM external dataplate.

The CENSE™ system operates similarly to any other Cummins® electronic system and measures many of the same temperatures and pressures. In addition, the CENSE™ system measures some additional parameters such as exhaust temperatures and differential pressures across filters.

![[19800559.png]]

The CENSE™ system uses a thermocouple mounted in the exhaust port of each cylinder to measure the exhaust gas temperature. A low exhaust temperature indicates that the cylinder is low on power. A high exhaust temperature indicates that the cylinder is receiving too much fuel.

The CENSE™ system measures a number of differential pressures on the engine. By measuring the pressure drop across a filter, the CENSE™ system can tell when a filter needs to be changed.

![[nobox.png]]

There are two generations of CENSE™ systems. The CENSE™ CM530 and the next generation, CENSE™ CM2330.

The CENSE™ CM530 module features J1587 communication and supports the RS422 and RS232 interfaces. INSITE™ electronic service tool for CENSE™ **must** be used to communicate with this module.

The CENSE™ CM2330 module features J1939 communication. The base INSITE™ electronic service tool **must** be used to communicate with this module.

![[nobox.png]]

### Programmable Features

The CENSE™ system has been designed to be flexible to meet a wide variety of engine monitoring needs.

Reference the INSITE™ Electronic Service Tool User's Manual for complete information on programmable features.

![[19400357.png]]

### Engine Trend Data

The CENSE™ system is capable of storing engine operating information for later analysis. INSITE™ electronic service tool can be used to adjust the data sampling rate and to download the trend data.

Reference the INSITE™ Electronic Service Tool User's Manual for more information.

![[19800902.png]]

### Diagnostic Fault Codes

The CENSE™ system can display and record certain detectable fault conditions. These malfunctions are displayed as fault codes which makes troubleshooting easier. The fault codes are retained in the ECM.

![[19400328.png]]

There are two types of fault codes. There are CENSE™ system faults and engine protection faults.

CENSE™ system faults light the blue warning lamp. Engine protection faults light the red or yellow lamp.

![[19800561.png]]

All fault codes recorded will either be active (fault is presently occurring) or inactive (the fault was active for some time, but it is **not** presently active).

Active fault codes can be read using the warning lamps in the vehicle cab or INSITE™ electronic service tool. Inactive faults can **only** be viewed with INSITE™ electronic service tool.

![[19800562.png]]

If the red lamp comes on while the engine is in operation, there is a fault occurring that can cause severe engine damage. Stop the engine in a safe manner as soon as possible.

If the yellow warning lamp lights, the engine can still be operated. This type of failure can be repaired at the next scheduled maintenance event.

![[19800563.png]]

The blue lamp indicates a CENSE™ system problem. These faults do **not** affect engine performance, but do reduce the ability of the CENSE™ system to detect engine problems.

![[19800564.png]]

When the vehicle key switch is turned ON, all lamps will light for 2 seconds to show that they are working.

![[19800565.png]]

Two seconds after the lamps go off, the yellow warning lamp will begin to flash out all active fault codes, if there are any active fault codes.

![[19800566.png]]

The numbers for the active fault codes will flash out in the following sequence. The yellow lamp will flash out the digits of the active fault codes.

There will be a 2 second delay between digits in a given fault code and a 3 second delay between different fault codes.

Active fault codes will continue to flash out as long as the vehicle key switch is ON.

![[19800567.png]]

The procedures for fault code troubleshooting are contained in Section TF of this manual.

The fault code troubleshooting procedures can also be found in the INSITE™ Fault Information System.

Reference the INSITE™ User's Manual for more information.

![[19400340.png]]

Fault Code Datalog

When a diagnostic fault code is recorded in the ECM, the values of certain sensor values are captured in a snapshot datalog. This datalog records sensor values for a certain period before and after the fault occurred. For more information on the fault code datalog feature, reference the INSITE™ User's Manual.

![[19400357.png]]

### Engine Protection System

If the CENSE™ system detects an engine problem, all it can do is turn on the warning lamp in the vehicle cab and broadcast the fault over the Modular Mining system, if installed.

![[19800568.png]]

### CENSE™ System Components

The CENSE™ system has been designed to monitor and record a wide variety of engine operating parameters. There are parameters that are unique to the CENSE™ system, as well as parameters that **must** be shared with the engine fuel system controller.

![[19800569.png]]

Engine Control Module Inputs

The following sensors will **only** be available with CENSE™ on a QSK45 CENSE™ or QSK60 CENSE™ engine:

1. Pre-filter and Post-filter Oil Pressure Sensor
2. J1939 Data Link
3. Turbocharger Compressor Inlet Temperature Sensor
4. Exhaust Temperature Sensor
5. Oil Pan Temperature Sensor.

![[19802670.png]]

The CENSE™ system can receive sensor information over the J1939 data link. The CENSE™ system can do without certain sensors if the desired information is broadcast over the J1939 data link by the engine fuel system ECM.

The CENSE™ system **only** receives information on this data link. The CENSE™ ECM **cannot** send information over the J939 data link.

![[19800573.png]]

Engine Control Module Outputs

The CENSE™ CM530 has the following outputs:

1. Warning Lamps
2. RS422 Data Link
3. RS232 Data Link.

The CENSE™ CM2330 has the following outputs:

1. Warning Lamps
2. J1939 Data Link.

![[19800574.png]]

The RS422 data link is used to communicate with the Modular Mining system and certain other vehicle electronic systems. The data link connector is typically located in the vehicle cab.

> [!note] Note · Примечание
> For engines with a CENSE™ CM2330 module, a J1939-capable Modular Mining system will have to be used.

![[cent337.png]]

For CENSE™ CM530: The RS232 data link is used to communicate with the INSITE™ electronic service tool. This data link is located on the engine wiring harness and is typically also in the vehicle cab.

For CENSE™ CM2330: The J1939 data link is used to communicate with INSITE™ electronic service tool. This data link is located on the engine wiring harness.

![[19400357.png]]

### Maintenance Monitor

The CENSE™ system has a maintenance monitor feature that monitors the change intervals for the fuel filter, the lubricating oil, the lubricating oil filters, the coolant, and the coolant filters. Reference the INSITE™ Electronic Service Tool User's Manual for more information.

![[ff6etha.png]]

### Real-Time Clock

The CENSE™ ECM has a real-time clock that can be set to the local time of day. The ECM records the time of day when events occur. For example, the ECM will record the exact time of day that a fault code was logged.

![[nobox.png]]

### Monitor Capabilities

INSITE™ electronic service tool can be used to monitor any of the CENSE™ sensors in real time while the engine is running.

![[19400357.png]]
