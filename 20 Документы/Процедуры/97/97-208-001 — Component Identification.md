---
aliases:
  - "Идентификация компонентов"
type: "Процедура"
doc: "97-208-001"
title_en: "Component Identification"
title_ru: "Идентификация компонентов"
modified: "2007-01-29"
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
  - "3666422"
figures: 19
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-208-001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-208-001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Component Identification
**Идентификация компонентов**

> [!abstract] Процедура · `97-208-001`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]], [[3666422 — ICON™ Idle Control System|3666422]]
> **Секции:** Section E - Component Identification · Section E - System Identification
> **Даты:** изменён 2007-01-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-208-001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-208-001.pdf)

### General Information

ICON™ System

ICON™ idle control system is an optional or aftermarket product that is designed to reduce excessive idle time when accomplishing the following tasks:

- Keeping the engine oil temperature above 16°C \[60°F\] in cold weather environments
- Keeping the batteries fully charged at all times
- Maintaining a desired temperature inside the cab. (This feature requires the cab thermostat to be installed.)

The complete ICON™ system consists of the following components:

1. Cab thermostat
2. Ambient air temperature sensor
3. ICON™ lamp
4. Dash relay (optional)
5. Neutral position switch
6. Parking brake switch
7. Ignition bus relay 1 and 2
8. ICON™ cab harness
9. ICON™ engine harness
10. Cab thermostat harness
11. Temperature sensor harness
12. ICON™ idle control module
13. Start relay
14. Engine start alarm
15. Hood tilt switch (non-mercury)

### Cab Thermostat

The cab thermostat is a device that allows the user to set the temperature inside the cab. When the temperature exceeds either the high or low temperature threshold, the cab thermostat directs the ICON™ system to start and run the engine until the desired temperature inside the cab has been reestablished. The cab thermostat is typically mounted inside the bunk area of the cab.

At initial turn-on of the cab thermostat, the thermostat will display the revision level of the software loaded in the thermostat, that is “01”, “02”, “03”, and so forth.

| Component Identification |  |
|---|---|
| Component | Revision Level |
| ICON™ Idle Control Module | 11, 14, 15, 16, 18, or 19 |
| Thermostat | 01, 02, 03, 04, 05, or 06 |

Any revision of the ICON™ control module is compatible with any revision of the ICON™ thermostat, although a wiring change can possibly be required.

![[15800001.png]]

### Ambient Air Temperature Sensor

The ambient air temperature sensor is a sensor mounted outside the cab, under the fifth wheel. The sensor is connected to the cab thermostat. The sensor allows the ICON™ system to use the ambient air temperature as a factor in determining when to operate the engine.

![[15800014.png]]

### ICON™ Lamp

The ICON™ lamp provides a visual display that shows the status of the ICON™ system. Depending on the status of the ICON™ system, the lamp either will illuminate steadily, will flash in certain patterns, or will remain off. The ICON™ lamp is mounted on the dash.

> [!note] Note · Примечание
> A LED can **only** be used with ICON™ idle control module revision 18.

![[15800003.png]]

### Dash Relay

The dash relay allows the ICON™ system and engine ECM to be isolated from the electronic dash while the ICON™ system is active but the ignition bus is unpowered.

The dash relay is installed when electronic dashes interfere with the ICON™ system operation. The installation of the dash relay does **not** affect normal dash operation when the ICON™ system is **not** active.

![[15800013.png]]

### Neutral Position Switch

The neutral position switch is a device that is installed on the vehicle's transmission. The neutral position switch lets the ICON™ system know whether the vehicle's transmission is in gear or in neutral. The switch is closed when the transmission is in neutral, and is open when the transmission is in gear. The ICON™ system will **not** start the engine or become active unless the transmission is in the NEUTRAL position.

![[15800006.png]]

### Parking Brake Switch

The parking brake switch is a device that is installed in the vehicle's parking brake line under the dash behind the hand valve. The parking brake switch lets the ICON™ system know whether the vehicle's parking brake is set or released. The switch closes when the parking brakes are on and the switch opens when the parking brakes are off. The ICON™ system will **not** start the engine or become active unless the parking brake is set.

![[15800011.png]]

### Ignition Bus Relay 1 and 2

The ignition bus relay 1 and 2 are relays that allow the ICON™ system to control the OEM ignition circuit automatically. Under normal conditions, the operator sends power to the vehicle's circuits by turning the keyswitch on. The ICON™ system, while active, controls these circuits with the ignition bus relays. Though the ICON™ kit includes **only** one relay (ignition bus relay 1), a second relay (ignition bus relay 2) can be installed to control multiple accessory packages. The ignition bus relay 1 and 2 are mounted under the dash.

![[15800002.png]]

### ICON™ Cab Harness

Aftermarket

The ICON™ cab harness connects all of the ICON™ system components inside the cab. The cab harness is connected to the ICON™ engine harness with a pass-through connector at the vehicle firewall.

![[15800009.png]]

### ICON™ Engine Harness

Aftermarket

The ICON™ engine harness connects all of the ICON™ system components in the engine bay. The ICON™ engine harness also provides primary power and grounding for the ICON™ system.

![[15800010.png]]

### Cab Thermostat Jumper Harness

Aftermarket

The cab thermostat harness connects the cab harness to the cab thermostat.

![[15800073.png]]

### Temperature Sensor Harness

Aftermarket

The temperature sensor harness connects the cab thermostat to the ambient air temperature sensor.

![[15800072.png]]

### ICON™ Idle Control Module

Aftermarket

The ICON™ idle control module is a small, powerful computer that controls the ICON™ system. The ICON™ idle control module communicates with all the ICON™ system switches and the engine ECM on the J1587 datalink to gather data and send commands. The ICON™ idle control module controls idle speed, idle time, engine starting and stopping, ignition bus power, and overall ICON™ system control. The ICON™ idle control module is mounted on the firewall of the vehicle.

The ICON™ idle control module's dataplate is located on the front of the idle control module and in the upper left corner. It contains the following:

1. P/N - ICON™ idle control module part number
2. S/N - ICON™ idle control module serial number

![[19803433.png]]

### Starter Relay

The starter relay is used by the ICON™ system to engage the engine starter. Since the engine start is automatic, the idle control module uses the starter relay to engage the starter without the necessity of an operator to push the start button or turn the key. The starter relay is mounted on the firewall of the vehicle.

![[15800004.png]]

### Engine Start Alarm

Prior to automatic engine starting, the ICON™ system sounds the engine start alarm (if enabled). This alarm warns anyone near the engine that the engine is about to start. The ICON™ system allows time during this alarm for personnel to move away from places that could cause personal injury when the engine starts. The engine start alarm is mounted on the firewall of the vehicle.

![[15800007.png]]

### Hood Tilt Switch

> [!danger] WARNING · Опасно
> Some hood tilt switches contain Mercury, a chemical known to some state and federal agencies to cause birth defects or other reproductive harm. Do not dispose. Recycle in accordance with state regulations.

The hood tilt switch is a safety device that is installed on the vehicle's hood. The hood tilt switch lets the ICON™ system know whether the vehicle's hood is open or closed. The ICON™ system will **not** start the engine or be active unless the hood is closed.

> [!note] Note · Примечание
> Some non-mercury hood tilt switches can be supplied without a bracket.

![[15800005.png]]

### Engine Brake Harness

Integrated

The ICON™ engine brake harness is required for Signature and ISX Series engines **only**. The engine brake harness reduces the number of possible engine brake levels from six to three. This allows increment and decrement drivers for ICON™ system use on Signature and ISX Series engines.

1. Engine brake connectors
2. Engine Brake harness connector

![[19c01037.png]]

### Component List

Aftermarket

![[19802979.png]]

ICON™ Cab Harness and Mating Components and Connections

1. Cab thermostat \*
2. Thermostat jumper harness
3. Thermostat jumper harness connector
4. Ambient air temperature sensor
5. Temperature sensor harness
6. 14-pin bulkhead pass-through
7. Datalink splice wired
8. ICON™ lamp and connector
9. Parking brake switch and connector
10. Cab harness fuse holder
11. Keyswitch splice wires
12. Keyswitch assembly
13. Ignition bus relays and connector
14. ICON™ engine harness
15. Ignition bus for OEM electrical circuits.

\* Required Cummins Inc. supplied part

![[19803843.png]]

ICON™ Engine Harness, Mating Components and Connections

1. ICON™ idle control module \*
2. ICON™ idle control module and harness connectors
3. Engine start alarm
4. Engine start alarm connector
5. Neutral position switch and connector
6. Engine ECM and ICON™ idle control module splice wire (keyswitch input wire)
7. Starter relay and connector
8. ICON™ engine harness fuse holder
9. Hood tilt switch
10. Hood tilt switch connector
11. 14-pin bulkhead pass-through connector
12. Battery terminal connectors
13. Cab harness.

\* Required Cummins Inc. supplied part

Integrated

![[19803460.png]]

ICON™ OEM Supplied Harness and Cummins Supplied Parts As Required

1. Engine OEM harness
2. Engine actuator harness
3. Engine sensor harness
4. 31-pin OEM connector
5. Starter relay
6. Parking brake switch and connector
7. Start alarm and connector\*
8. Neutral position switch and connector
9. Hood tilt switch
10. ICON™ lamp and connector
11. ICON™ engine brake harness
12. Ignition bus relay
13. Ambient air temperature sensor and harness\*
14. Cab thermostat\*
15. Bulkhead connector

\* Required Cummins Inc. supplied part
