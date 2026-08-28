---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "10-101-007-om-ind"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2003-04-10"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666423"
figures: 42
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-101-007-om-ind.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-101-007-om-ind.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `10-101-007-om-ind`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666423 — QSX15 Operation and Maintenance Manual|3666423]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2003-04-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-101-007-om-ind.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-101-007-om-ind.pdf)

### General Information

The Signature/ISX fuel system is an electronically controlled fuel injection system that optimizes fuel economy and reduces exhaust emissions. It does this by controlling the torque and horsepower curve, engine high speed, low idle, and road speed.

![[oi800v13.png]]

Signature/ISX has the capability of controlling the fan clutch actuator if an electronically controlled fan clutch is used.

Signature/ISX also allows the engine brakes to be activated by controlling the engine brake solenoids.

The electronic feature, fan control engine braking can be enabled to activate the fan clutch during engine braking. This increases the load on the engine during engine braking.

![[17c00027.png]]

### Diagnostic Fault Codes

Industrial Applications

The QSX15 fuel system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which make troubleshooting easier. The fault codes are retained in the electronic control module (ECM).

![[19400328.png]]

There are two types of fault codes. There are engine electronic fuel system fault codes and engine protection system fault codes.

All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at some time, but is **not** presently active).

| **Diagnostic Fault Codes** |  |  |  |
|---|---|---|---|
| •Engine Electronic Fuel System Fault Codes |  |  |  |
| •Engine Protection System Fault Codes. |  |  |  |

![[nobox.png]]

Active fault codes can be read using the warning (amber) and stop lamps (red) in the cab panel or electronic service tool. Inactive fault codes can **only** be viewed with an electronic service tool.

![[17c00177.png]]

When the vehicle keyswitch is turned on and the diagnostic switch is off, the fault code lamps (red, yellow, and maintenance) will illuminate for approximately 2 seconds, one after the other, to check their operation.

![[19400331.png]]

The lights will remain off until a fault code is recorded. If a stop (red) light comes on while the engine is in operation, the fault can be engine-disabling. Stop the engine in a safe manner as soon as possible.

If the warning (amber) light illuminates, the engine can still be operated, but it can lose some system features that can sometimes result in a power loss. The failure **must** be repaired as soon as is convenient.

![[19400332.png]]

The engine protection system records separate fault codes when an out-of-range condition is found for any of the sensors in the engine protection system. Engine protection is **only** available when the engine protection feature is enabled.

- Coolant Temperature
- Coolant Level
- Intake Manifold Temperature
- Oil Pressure.

![[nobox.png]]

The engine protection system will light the maintenance lamp (orange) when an out-of-range condition occurs.

> [!note] Note · Примечание
> Lamp colors and labels will vary by OEM.

![[19400334.png]]

If the engine protection maintenance lamp comes on while driving, it means that a fault code has been recorded. The light will remain on as long as the fault is occurring.

The light will begin to flash if the condition continues to get worse. The engine power and/or speed will be gradually reduced. If the engine protection shutdown feature is enabled, the engine will shut down to prevent engine damage.

![[19400335.png]]

To check for active fault codes, first turn the vehicle keyswitch to the OFF position. Move the diagnostic switch to the ON position.

> [!note] Note · Примечание
> Some OEMs use a shorting plug.

![[19400336.png]]

Turn the vehicle keyswitch to the ON position. If no active fault codes are recorded, all three lights will come on and stay on. If active fault codes are recorded, all three lights will come on momentarily. The amber (warning) and red (stop) lights will begin to flash the code of the recorded fault.

![[19400337.png]]

The fault code will flash in the following sequence. First, the amber (warning) lamp will flash. Then there will be a short 1-second pause when both the amber and red lights are off. Then the numbers of the recorded fault code will flash in red. There will be a 1-second pause between each number. When the number has stopped flashing, an amber light will appear again. The number will repeat in the same sequence.

![[19400338.png]]

The lights will continue to flash the same fault code until the system has advanced to the next active fault code. To go to the second fault code, move the idle-speed adjust switch to “+,” then release it. You can also go back to the previous fault code by moving the switch to “-,” then releasing it. To check the third or fourth fault code, move the switch to “+,” then release it when all active fault codes have been viewed. Moving the switch to “+” will go back to the first fault code.

The explanation and correction of all fault codes is in the troubleshooting charts of the QSX15 fuel manual. Refer to Troubleshooting and Repair Manual, Electronic Control System, Signature, ISX and QSX15 Engines, Bulletin No. 3666259.

Electronic fault code troubleshooting trees are in ascending numerical order. An index is located at the beginning of the section.

![[19400339.png]]

To stop the diagnostic system, move the diagnostic switch to the OFF position, or remove the shorting plug. Turn the vehicle keyswitch to the OFF position.

> [!note] Note · Примечание
> Some OEMs use a shorting plug.

![[gp8swvv.png]]

Fault Code Snapshot Data

When a diagnostic fault code is recorded in the ECM, ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.

![[19400349.png]]

Power Generation

The QSX15 fuel system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which make troubleshooting easier. The fault codes are retained in the ECM.

There are two types of diagnostic codes:

Information codes are to inform the operator and electronic system (paralleling controllers, smart switch gear) that an event has occurred.

Fault codes are to report to the operator and the electronic system that there is a problem or potential problem with the engine or fuel system.

![[19802544.png]]

Fault codes can be accessed in three different ways:

1. Flash Out
2. Electronic Service Tool
3. Operator Interface Panel.

![[nobox.png]]

Generator-Drive Control System ECM Diagnostic Lamps

The generator-drive control system ECM has five LEDs for diagnostics. Typical lights will include:

1. OS - Overspeed
2. LOP - Low Oil Pressure
3. HET - High Engine Temperature
4. Shutdown - Engine Protection Shutdown Has Occurred
5. Warning - Engine Protection Warning Condition Exists.

![[19600091.png]]

Generator-Drive Control System Relay Drivers

The generator-drive control system has seven relay drivers for customer-supplied relays.

- Overspeed
- Low Oil Pressure
- High Engine Temperature
- Engine Protection Shutdown Has Occurred
- Engine Protection Warning Condition Exists
- Prelow Oil Pressure
- Prehigh Engine Temperature.

![[19600091.png]]

Fault Code Flash-out

To “flash out” a fault code, the ECM **must** be put into the diagnostic mode. Enter the diagnostic mode by removing the diagnostic connector shorting the plug from the engine harness, turning the plug, and reinserting it, or using the diagnostic mode switch.

The warning lamp will flash (signifying the start of a new fault code), and then the fault code will flash out on the shutdown lamp.

![[19600091.png]]

Fault Codes - Electronic Service Tool

The electronic service tool can be used to read the fault codes. Connect a personal computer, with the electronic service tool installed, to the engine using the service harness, Part No. 3163156. Refer to the electronic service tool manual for specifics about how to use the tool to read the fault codes.

![[19800902.png]]

Fault Code - Operator Interface Panel

If the customer supplied an operator interface panel, it has been integrated with the generator-drive control system using the RS485 datalink. The ability to display fault codes is one plus of this panel; refer to the manuals supplied with the unit for more details.

![[19800902.png]]

Fault Code Snapshot Data\\

When a diagnostic fault code is recorded in the ECM, the ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.

![[19800902.png]]

To Clear a Fault Code

**Only** inactive fault codes can be cleared. There are two ways to clear an inactive fault code:

1. The reset switch on the operator interface panel
2. The electronic service tool.

> [!note] Note · Примечание
> The engine **must** be shut down to clear inactive shutdown faults.

All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at some time, but is **not** presently active).

![[19800902.png]]

### Engine Protection System

QSX15 engines are equipped with an engine protection system. The system monitors critical engine temperatures and pressures and will log diagnostic faults when an abnormal operating condition occurs. If an out-of-range condition exists and engine derate action is to be initiated, the operator will be alerted by an in-cab warning light. The warning light will blink or flash when out-of-range conditions continue to worsen. The driver **must** pull to the side of the road, when it is safe to do so, to reduce the possibility of engine damage.

> [!note] Note · Примечание
> Engine power and speed will be gradually reduced, depending on the level of severity of the observed condition. The engine protection system will **not** shut down the engine unless the engine protection shutdown feature has been selected. If the feature has been selected and the engine does shut down, the engine can be started again by turning off the keyswitch and then turning it back on.

![[17c00028.png]]

### Fuel System Description

The QSX15 electronically controlled fuel system consists of:

1. Fuel shutoff valve
2. Oil pressure/temperature sensor
3. Intake manifold pressure/temperature sensor
4. Cooling plate (behind ECM)
5. Electronic control module
6. Fuel in
7. Fuel out
8. ECM actuator harness port (industrial only)
9. ECM OEM harness port (industrial only).

![[19c00617.png]]

The QSX15 electronically controlled fuel system consists of:

1. Camshaft Position Sensor
2. Fueling Actuators
3. Ambient Air Pressure Sensor
4. Timing Actuators
5. Fuel Pressure Sensor
6. Water-in-Fuel Separator
7. Crankshaft Position Sensor
8. Front and Rear Rail Pressure Sensor
9. Fuel Inlet Restriction Sensor
10. Coolant Level Sensor (In Radiator) - Optional\*.

\* Not in this view.

Electronic Control Module (ECM) Dataplate

Industrial

The data tag for the ECM is located on the front of the module housing.

![[17c00046.png]]

Power Generation

The data tag for the ECM is located on the side of the ECM opposite the ECM connectors.

![[19802621.png]]

Electronic Control Module Inputs

Electronic Control Module (ECM) Inputs:

1. Engine Camshaft or Crankshaft Position Sensor
2. Throttle Position Sensor (industrial **only**)\*
3. Idle Validation Switch\*

![[19c00618.png]]

1. Coolant Level Sensor\*
2. Ambient Air Pressure Sensor
3. Oil Pressure/Temperature Sensor
4. Wet Tank Pressure Sensor\*
5. Unintended Fuel Diagnostic Sensor (industrial **only**)
6. Fuel Pressure Sensor
7. Water-in-Fuel Sensor (industrial **only**).

\*These are OEM sensors that are **not** installed on the engine.

![[19c00619.png]]

The engine cam and crank position sensors provide engine speed and position information.

The cam position sensor is located between the ECM and fuel pump. The crank position sensor is located below the air compressor drive or the barring device.

![[17c00050.png]]

The throttle position sensor (industrial **only**) is located in the throttle foot pedal assembly. When the foot pedal is at idle, the engine brakes can be activated. When the throttle pedal is depressed, the sensor deactivates the engine brakes and the PTO. The accelerator pedal can override the cruise control and PTO (if the throttle override in PTO is enabled).

![[en800kf.png]]

The idle validation switch is added to the throttle pedal assembly and will verify that the throttle pedal is in the low-idle position.

![[en800gf.png]]

The intake air pressure/temperature sensor, located in the front of the intake air connection, monitors positive manifold pressure and turbocharged intake air temperature. Both are used in the fuel control function. The intake air pressure/temperature sensor is also used in the engine protection system.

![[17c00051.png]]

The engine coolant temperature sensor, located in the thermostat housing, monitors engine coolant temperature used in the fuel control function and engine protection system.

![[17c00053.png]]

The coolant level sensor is mounted in the radiator top tank or surge tank, depending on the OEM. It is a fluid-level-actuated switch required for the engine protection system.

> [!note] Note · Примечание
> This is an optional sensor that will or will **not** be on all vehicles.

![[en800gd.png]]

The ambient air pressure sensor is located on the fuel pump side of the engine, just below the ECM. It is used to control fueling.

![[17c00054.png]]

The oil pressure/temperature sensor, located on the fuel pump side of the engine, monitors lubricating oil pressure and temperature for the engine protection system.

![[17c00055.png]]

The unintended fuel diagnostic sensors, located behind the fuel actuators on the integrated fuel system module, monitor the fuel actuator's passage pressure.

![[17c00143.png]]

The fuel pressure sensor, located on the integrated fuel system module, monitors actuator supply rail pressure.

![[17c00144.png]]

The water-in-fuel sensor, located on the fuel filter, monitors water in fuel.

![[17c00145.png]]
