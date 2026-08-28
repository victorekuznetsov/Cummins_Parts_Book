---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "28-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2005-11-11"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "3810497"
figures: 42
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/28"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `28-101-007`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[3810497 — K38, K50, QSK38 and QSK50 Operation and Maintenance Manual|3810497]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2005-11-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-101-007.pdf)

### General Information

CENTRY™

The CENTRY™ system is an intelligent electronic engine control system designed to optimize engine control system on mining, construction, agriculture, and other off-highway equipment. This system can be applied to all engine models that use the PT®, pressure timed, fuel system. The CENTRY™ system controls engine speed and fuel pressure based on input from the electronic throttle and other equipment-specific and/or engine-model-specific features.

The CENTRY™ system consists of hydromechanical and electronic subsystems. The electronic subsystem manages fuel delivery using an electronic fuel control (EFC) valve while the hydromechanical subsystem provides backup maximum engine torque and speed protection.

![[19801556.png]]

Electronic Subsystem

The engine subsystem contains:

1. ECM
2. Main Engine Harness
3. Rail Pressure Sensor
4. Engine Speed Sensor
5. Electronic Fuel Control Valve (EFC).

![[19801566.png]]

The CENTRY™ system has been designed for both 12- and 24-VDC original equipment manufacturer (OEM) electrical systems. The following components are different between 12- and 24-VDC systems:

1. ECM
2. Electronic Fuel Control (EFC)
3. Fuel Shutoff Valve
4. Electronic step timing control (STC) Actuator (if used)
5. Auxiliary Shutdown Device (if used).

![[19801567.png]]

The following components are the same in both 12- and 24- VDC systems:

1. Main Engine Harness
2. Rail Pressure Sensor
3. Engine Speed Sensor
4. OEM Throttle Switch Interface.

![[19801568.png]]

The CENTRY™ ECM is loaded with a calibration containing engine control and OEM application-specific information. A Cummins Authorized Repair Location can recalibrate an ECM on the equipment by use of the INSITE™ electronic service tool, Compulink™, or Echeck™, and the Electronic Software Database and Network (ESDN). Some adjustments can be made with the Cummins INSITE™ electronic service tool, Compulink™, or Echeck™, when a CENTRY™ cartridge is used.

![[19800109.png]]

CENTRY™ features used in an application will be displayed in INSITE™ electronic service tool, Compulink™, or Echeck™ monitor mode and view parameter screens. The OEM and calibration will determine which features are used and which parameters can be adjustable.

![[19800109.png]]

The CENTRY™ main engine harness contains the following connections and fuses:

1. ECM Connector
2. Electronic Fuel Control (EFC) Valve 90° Connectors
3. Fuel Shutoff Valve Ring Terminal
4. Fuses (5-amp)
5. Engine-Side Datalink Connector
6. Rail Pressure Sensor Connector
7. OEM 9-pin Connector (C-5)
8. OEM 9-pin Connector (C-6)
9. CENTRY™ Ground Ring Terminal
10. Electronic STC Ring Terminal (optional)
11. Engine Speed Sensor Connectors

> [!note] Note · Примечание
> Harness connector breakout locations differ between engine families.

![[19801570.png]]

Hydromechanical Subsystem

This subsystem contains:

1. Fuel Pump

1A. Electronic Fuel Control Module Assembly

1B. Backup Mechanical Governor

1C. Air-Fuel Control

2. Fuel Shutoff Valve

3. Fuel Tubes

4. Fuel Block (Rail Pressure Sensor Mount)

5. Step Timing Control

6. Injectors.

![[19801557.png]]

The fuel pump is the main part of the hydromechanical subsystem because it supplies the fuel pressure controlled by the electronic fuel control valve. The mechanical governor for the fuel pump provides backup maximum engine torque and speed control.

![[19801558.png]]

The fuel pump air-fuel control uses a turbocharger boost pressure line to regulate the fuel pressure supplied to the electronic fuel control valve. The air-fuel control reduces black smoke and improves engine performance during low-boost conditions.

![[19801559.png]]

The air-fuel control, NO-AIR setting is the maximum fuel rail pressure that the fuel pump can supply when no boost pressure is detected on the boost pressure sensing line. The following graph illustrates a typical rail pressure versus boost pressure acceleration transition curve. The air-fuel control allows the maximum available fuel rail pressure to increase as boost pressure increases.

![[19801560.png]]

Many engine models use a fuel shutdown valve having a manual override screw. Turning this screw in overrides the shutdown valve and/or shutdown systems connected to the fuel shutoff valve.

> [!note] Note · Примечание
> This screw does **not** override the electronic fuel control valve in the CENTRY™ system.

![[19801561.png]]

The CENTRY™ system uses a fuel block to provide a solid location for the rail pressure sensor.

![[19801562.png]]

On engine models that use STC, some engines will use a fuel pressure sensing line to control a hydromechanical STC switch and other engines will use the CENTRY™ system to switch an electronic STC solenoid.

STC identification:

1. Fuel Pressure Sensing Line
2. Oil Line to the Tappets
3. Oil Vent Line
4. Oil Supply Line
5. CENTRY™ STC Actuator Lead Wire.

The STC allows the engine to operate in advanced injection timing immediately after start-up and light-duty engine load conditions and to return to normal timing during medium and high engine load conditions. The benefits of this feature include:

- Improved cold weather idling characteristics
- Reduced cold weather white smoke
- Improved light-load fuel economy.

![[19801563.png]]

The hydromechanical STC allows two different injection timing modes based on fuel rail pressure detected on the fuel pressure sensing line. Hysteresis provides the maximum rail pressure for the engine to shift from ADVANCED™ to normal timing and minimum rail pressure for a shift from normal to ADVANCED™ timing. Hysteresis prevents unstable and rapid switching of STC timing modes when the engine is operating at rail pressures within the hysteresis rail pressure range.

![[19801564.png]]

The CENTRY™ electronic STC also allows two different injection timing modes based on measured rail pressure and engine speed. However, CENTRY™ has the capability to provide two different sets of rail pressure STC switch points above and below a calibrated engine speed point. This provides further optimization of engine performance with STC. The ECM provides 12- and 24- VDC to the electronic STC actuator when it is commanding ADVANCED™ timing mode.

![[19801565.png]]

### QSK System Description

Industrial Applications

The QSK fuel system is an electronically controlled system designed to optimize engine control and reduce exhaust emissions. The QSK fuel system controls engine speed and fuel pressure, based on input from the electric throttle and other equipment-specific, model-specific, or both, features.

Industrial applications fuel systems:

- Optimized engine control
- Reduced exhaust emissions.

![[05600069.png]]

INSITE™ is an electronic service tool for the industrial applications fuel systems. Use INSITE™ electronic service tool to:

- Program owner-specified information into the ECM (parameters and features)
- Aid in troubleshooting the engine
- Change the engine power or rated speed calibration.

Contact a Cummins Authorized Repair Location for more specifics on this tool.

![[19400357.png]]

Power Generation

The generator-drive control system is an electronic control system designed to:

- Optimize engine control.
- Reduce exhaust emissions.

The QSK50 fuel system design controls engine speed and fuel pressure utilizing electronic sensors with the Quantum™ system.

The power-generation electronic control system has its own electronic tool called INPOWER™. INSITE™ is the **only** electronic service tool that can be used with power-generation engines with electronically actuated injectors. INPOWER™ electronic service tool can be purchased through Cummins Inc.

Contact a Cummins Authorized Repair Location for specifics on the these service tools:

- INPOWER™
- INPOWER PRO™.

INPOWER™ is an electronic service tool for the generator-drive control systems. Use the INPOWER™ electronic service tool to:

- Program owner-specified information into the ECM (parameters and features)
- Aid in troubleshooting the engine
- Change the engine power or rated speed calibration.

Contact a Cummins Authorized Repair Location for specifics on this tool.

The INPOWER™ electronic service tool adjustment feature allows adjustments to be made to the generator-drive parameters for trims and settings. There are several adjustment parameters. **Not** all generator sets will have the same adjustments available.

The INPOWER™ electronic service tool monitor mode is a useful troubleshooting aid that displays the key ECM inputs and outputs. This feature can be used to spot constant or abnormally fluctuating values.

The ECM inputs show the data that is being fed into the ECM by the system's sensors and switches. The ECM outputs are values that the ECM commands to the generator-drive control system.

The monitor mode allows the relationship between the ECM inputs and outputs to be monitored and used during troubleshooting.

The INPOWER PRO™ electronic service tool allows the user to transfer new or updated calibration files for the generator-drive control system ECM from a central location to Cummins Inc. distributors.

A calibration file is electronic data that gives the engine its performance rating.

The calibration file will be loaded into the INPOWER™ electronic service tool, which is used to load the file into the ECM.

Contact a Cummins Authorized Repair Location for more specifics on this tool.

The INPOWER™ electronic service tool test mode feature is a diagnostic tool that is used to perform internal self-checks on the PowerCommand™ control to verify inputs and outputs of the control system and test engine protection functions.

### Diagnostic Fault Codes

CENTRY™

The CENTRY™ system can display and record detectable fault conditions within its systems and circuits. A yellow diagnostic lamp near the operator's controls will be illuminated when a system fault becomes active.

![[19801604.png]]

The fault lamp should light for about 1 to 2 seconds after key-on, and then go out after no faults have been detected.

![[19802499.png]]

While a fault condition is being detected, the fault lamp will turn ON or ON FLASHING. CENTRY™ will turn the lamp ON for warning faults, and ON FLASHING for more severe faults that can affect engine operation and need immediate attention. Active fault conditions **must** be corrected as soon as possible.

![[19801605.png]]

To determine an active CENTRY™ fault code, shut off the engine and turn keyswitch on (engine **not** running). Toggle the diagnostic switch to the ON position for 1 to 2 seconds and then release the switch. The fault lamp will illuminate while the diagnostic switch is held in the ON position.

![[19801606.png]]

After releasing the diagnostic switch, there is a short pause followed by the first fault code. CENTRY™ fault codes consist of three digits with up to five flashes for each digit. There is a short pause between each digit of the fault code. Once the three digits have flashed and the code is known, there is a longer pause followed by a repeating of the same fault code sequence.

![[19801607.png]]

Toggling the diagnostic switch will advance to the next fault code. Once all active fault codes have been displayed, the fault code flash sequence will be repeated, starting from the first fault code.

![[19801608.png]]

Starting the engine or turning the keyswitch to the OFF position will exit the diagnostic's fault flash mode.

![[19801609.png]]

Industrial Applications

> [!note] Note · Примечание
> This information does **not** apply to the K38, K50 Series engines.

The industrial application fuel system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which make troubleshooting easier. The fault codes are retained in the ECM.

There are two types of fault codes:

- Engine electronic fuel system fault codes
- Engine protection system fault codes.

All fault codes recorded will either be active (fault code is presently active on engine) or inactive (fault code was active at some time, but is **not** presently active).

![[19400328.png]]

Active fault codes can be read using the WARNING (amber) and STOP (red) lamps in the cab panel.

The active fault codes can also be accessed using INSITE™ electronic service tool, Part Number 3824801.

Inactive fault codes can **only** be read with the INSITE™ electronic service tool.

![[19400330.png]]

When the vehicle keyswitch is turned on and the diagnostic switch is off, the fault code lamps (red, yellow, and engine protection) will illuminate for approximately 2 seconds, one after the other, to check their operation.

![[19400331.png]]

The lights will remain off until a fault code is recorded. If a STOP (red) light illuminates while the engine is in operation, the fault can be engine-disabling. Stop the engine in a safe manner as soon as possible.

If the WARNING (amber) lamp illuminates, the engine can still be operated, but it can lose some system features that can sometimes result in a power loss. The failure **must** be repaired as soon as it is convenient.

The engine protection system records separate fault codes when an out-of-range condition is found for any of the sensors in the engine protection system.

The following engine protection sensors will **only** be available with the CENSE™ electronic engine monitoring system option:

- Engine coolant pressure
- Fuel temperature
- Blowby pressure.

![[19400332.png]]

> [!note] Note · Примечание
> Lamp colors and labels will vary by OEM.

The engine protection system will illuminate the maintenance lamp (orange) when an out-of-range condition occurs.

![[19400334.png]]

If the engine protection maintenance lamp illuminates while driving, it means that a fault code has been recorded. The lamp will remain illuminated as long as the fault is occurring.

The lamp will begin to flash if the condition continues to get worse. The engine power, speed, or both, will be gradually reduced. If the engine protection shutdown feature is enabled, the engine will shut down to prevent damage.

![[19400335.png]]

To check for active fault codes:

1. Turn the keyswitch to the OFF position.
2. Move the diagnostic switch to the ON position.

> [!note] Note · Примечание
> Some OEMs use a shorting plug.

![[19400336.png]]

Turn the vehicle keyswitch to the ON position.

If active fault codes are **not** recorded, all three lamps will illuminate and stay illuminated.

If active fault codes are recorded, all three lamps will illuminate momentarily. The WARNING (amber) and the STOP (red) lamps will begin to flash the code of the recorded fault.

![[19400337.png]]

The fault code will flash in the following sequence:

1. The WARNING (amber) lamp will flash.
2. A one second pause with both WARNING (amber) and STOP (red) lamps off.
3. The STOP (red) lamp will flash the recorded fault code with a one second pause between digits.
4. When the number has stopped flashing, the WARNING (amber) lamp will illuminate.
5. The fault code number will repeat in the same sequence.

![[19400338.png]]

The lights will continue to flash the same fault code until the system has been advanced to the next active fault code.

To advance to the second fault code, move the idle speed adjust switch to the positive (+), then release it.

The previous fault code can be accessed by moving the switch to the negative (-) position, then releasing it.

To check the third or fourth fault code, move the switch to the positive (+) position, then release it.

When all active fault codes have been viewed, moving the switch to the positive (+) position will return the system to the first fault code.

The explanation and correction of all fault codes can be found in the troubleshooting charts of the appropriate electronic fuel systems troubleshooting and repair manual. Contact a Cummins Authorized Repair Location.

Electronic fault code troubleshooting trees are in ascending numerical order. An index is located at the beginning of the section.

![[19400339.png]]

> [!note] Note · Примечание
> Some OEMs use a shorting plug

To stop the diagnostic system, move the diagnostic switch to the OFF position.

Turn the vehicle keyswitch to the OFF position.

![[gp8swvv.png]]

Power Generation

> [!note] Note · Примечание
> This information does **not** apply to the K38, K50 Series engines.

The generator-drive system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which make troubleshooting easier. The fault codes are retained in the ECM.

There are two types of fault codes. There are engine electronic fuel system fault codes and engine protection system fault codes.

All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at some time, but is **not** presently active).

- Engine electronic fuel system fault codes
- Engine protection system fault codes.

Fault codes can be accessed in three different ways:

- Flash out
- Electronic service tool
- Operator interface panel.

![[19802544.png]]

The generator-drive control system ECM has five LEDs for diagnostics:

- OS - overspeed
- LOP - low oil pressure
- HET - high engine temperature
- Shutdown - engine protection shutdown has occurred
- Warning - engine protection warning condition exists.

The generator-drive control system has eight relay drivers for customer-supplied relays:

- OS - Overspeed
- LOP - Low oil pressure
- HET - High engine temperature
- Shutdown - Engine protection shutdown has occurred
- Warning - Engine protection warning condition exists
- Pre-low oil pressure
- Pre-high engine temperature
- Fail to start.

![[19600091.png]]

To flash out a fault code, the ECM **must** be put into the diagnostic mode. Enter the diagnostic mode using the diagnostic mode switch or by connecting together the two single-pin diagnostic mode enable connectors. During normal ECM operation, the two connectors are disconnected (open circuit). The ECM is placed in diagnostic mode when these two connectors are joined together (short circuit).

The warning lamp will flash (signifying the start of a new fault code), and then the fault code will flash out on the shutdown lamp.

![[19600090.png]]

The electronic service tool can be used to read the fault codes. Connect a personal computer, with the electronic service tool installed, to the engine using the service harness, Part Number 3163156.

Contact a Cummins Authorized Repair Location for specifics on how to read the fault codes.

![[19800902.png]]

If the customer-supplied operator interface panel has been integrated with the generator-drive control system using the RS485 datalink, the ability to read the fault codes is available.

Contact a Cummins Authorized Repair Location for specifics on how to read the fault codes.

![[19802725.png]]

### Fault Code Snapshot Data

Industrial and Power Generation

> [!note] Note · Примечание
> This information does **not** apply to the K38, K50 Series engines.

When a diagnostic fault code is recorded in the ECM, ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.

To Clear a Fault Code:

**Only** inactive fault codes can be cleared. The **only** way to clear an inactive fault code is to use the electronic service tool.

The engine **must** be shut down to clear inactive shutdown faults.

All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (was active at some time, but is **not** presently active).

![[19400349.png]]

### Engine Protection System

Industrial and Power Generation

> [!note] Note · Примечание
> This information does **not** apply to the K38, K50 Series engines.

All QSK50 series engines are equipped with an engine protection system. The system monitors critical engine temperatures, fluid levels, switch positions, and pressures and will log diagnostic faults when an over or under normal operating range condition occurs. If an out-of-range condition exists, engine derate action will be initiated. The operator will be alerted by the illumination of the in-cab maintenance lamp. The warning lamp will start to flash when an out-of-range condition continues to worsen and engine shutdown will occur. The operator **must** pull to the side of the road when it is safe to do so to reduce the possibility of engine damage.

- High engine coolant temperature
- Low engine coolant level (optional)
- Low engine coolant pressure
- High fuel temperature
- High intake manifold temperature
- Low and very low lubricating oil pressure
- High blowby pressure.

The engine protection system has three selectable features. If the engine protection enable feature has been selected, engine power and speed will be gradually reduced depending on the level of severity of the observed condition. If the engine protection shutdown feature has been selected, the engine will be shut down. If the engine restart feature has been selected, the engine can **not** be started again after shutdown.

- Engine protection enable
- Engine protection shut down
- Engine protection restart.
