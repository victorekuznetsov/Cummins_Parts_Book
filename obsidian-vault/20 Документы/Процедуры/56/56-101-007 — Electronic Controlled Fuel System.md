---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "56-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2005-11-02"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "37292556"
  - "37295879"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
  - "QST30"
manuals:
  - "3666134"
  - "3666260"
  - "4021374"
figures: 19
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "группа/56"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `56-101-007`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60, QST30
> **Входит в руководства:** [[3666134 — QST30 Operation and Maintenance Manual|3666134]], [[3666260 — QSK45 and QSK60 Operation and Maintenance Manual|3666260]], [[4021374 — QSK23 Operation and Maintenance Manual|4021374]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2005-11-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-101-007.pdf)

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

Refer to a Cummins Authorized Repair Location for more specifics on this tool.

![[19400357.png]]

Power Generation

The generator-drive control system is an electronic control system designed to:

- Optimize engine control.
- Reduce exhaust emissions.

The QSK45 and QSK60 fuel system design controls engine speed and fuel pressure utilizing electronic sensors with the Quantum™ system.

The power-generation electronic control system has its own electronic tool called INPOWER™. INSITE™ is the **only** electronic service tool that can be used with power-generation engines with electronically actuated injectors. INPOWER™ electronic service tool can be purchased through Cummins Inc.

Refer to a Cummins Authorized Repair Location for specifics on the these tools:

- INPOWER™
- INPOWER PRO™.

INPOWER™ is an electronic service tool for the generator-drive control systems. Use the INPOWER™ electronic service tool to:

- Program owner-specified information into the ECM (parameters and features)
- Aid in troubleshooting the engine
- Change the engine power or rated speed calibration.

Refer to a Cummins Authorized Repair Location for specifics on this tool.

The INPOWER™ electronic service tool adjustment feature allows adjustments to be made to the generator-drive parameters for trims and settings. There are several adjustment parameters. **Not** all generator sets will have the same adjustments available.

The INPOWER™ electronic service tool monitor mode is a useful troubleshooting aid that displays the key ECM inputs and outputs. This feature can be used to spot constant or abnormally fluctuating values.

The ECM inputs show the data that is being fed into the ECM by the system's sensors and switches. The ECM outputs are values that the ECM commands to the generator-drive control system.

The monitor mode allows the relationship between the ECM inputs and outputs to be monitored and used during troubleshooting.

The INPOWER PRO™ electronic service tool allows the user to transfer new or updated calibration files for the generator-drive control system ECM from a central location to Cummins Inc. distributors.

A calibration file is electronic data that gives the engine its performance rating.

The calibration file will be loaded into the INPOWER™ electronic service tool, which is used to load the file into the ECM.

Refer to a Cummins Authorized Repair Location for more specifics on this tool.

The INPOWER™ electronic service tool test mode feature is a diagnostic tool that is used to perform internal self-checks on the PowerCommand™ control to verify inputs and outputs of the control system and test engine protection functions.

### Diagnostic Fault Codes

Industrial Applications

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

When the vehicle keyswitch is turned on and the diagnostic switch is off, the fault code lamps (red, yellow, and engine protection) will illuminate for approximately two seconds, one after the other to check their operation.

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
> Some OEM's use a shorting plug.

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

The lights will continue to flash the same fault code until the system has advanced to the next active fault code.

To advance to the second fault code, move the idle speed adjust switch to the positive (+), then release it.

The previous fault code can be accessed by moving the switch to the negative (-) position, then releasing it.

To check the third or fourth fault code, move the switch to the positive (+) position, then release it.

When all active fault codes have been viewed, moving the switch to the positive (+) position will return the system to the first fault code.

The explanation and correction of all fault codes is in the troubleshooting charts of the Quantum™ fuel manual. Refer to a Cummins Authorized Repair Location.

Electronic fault code troubleshooting trees are in ascending numerical order. An index is located at the beginning of the section.

![[19400339.png]]

> [!note] Note · Примечание
> Some OEMs use a shorting plug

To stop the diagnostic system, move the diagnostic switch to the OFF position.

Turn the vehicle keyswitch to the OFF position.

![[gp8swvv.png]]

Power Generation

The generator-drive system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which make troubleshooting easier. The fault codes are retained in the ECM.

There are two types of fault codes. There are engine electronic fuel system fault codes and engine protection system fault codes.

All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at some time, but is **not** presently active).

- Engine electronic fuel system fault codes
- Engine protection system fault codes.

Fault codes can be accessed in three different ways:

- Flashout
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
- Prelow oil pressure
- Prehigh engine temperature
- Fail to start.

![[19600091.png]]

To flash out a fault code, the ECM **must** be put into the diagnostic mode. Enter the diagnostic mode using the diagnostic mode switch or by connecting together the two single-pin diagnostic mode enable connectors. During normal ECM operation, the two connectors are disconnected (open circuit). The ECM is placed in diagnostic mode when these two connectors are joined together (short circuit).

The warning lamp will flash (signifying the start of a new fault code), and then the fault code will flash out on the shutdown lamp.

![[19600090.png]]

The electronic service tool can be used to read the fault codes. Connect a personal computer, with the electronic service tool installed, to the engine using the service harness, Part Number 3163156.

Refer to a Cummins® Authorized Repair Location for specifics on how to read the fault codes.

![[19800902.png]]

If the customer-supplied operator interface panel has been integrated with the generator-drive control system using the RS485 datalink, the ability to read the fault codes is available.

Refer to a Cummins Authorized Repair Location for specifics on how to read the fault codes.

![[19802725.png]]

### Fault Code Snapshot Data

Industrial and Power Generation

When a diagnostic fault code is recorded in the ECM, ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.

To Clear a Fault Code:

**Only** inactive fault codes can be cleared. The **only** way to clear an inactive fault code is to use the electronic service tool.

The engine **must** be shut down to clear inactive shutdown faults.

All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (was active at some time, but is **not** presently active).

![[19400349.png]]

### Engine Protection System

Industrial and Power Generation

All QSK45 and QSK60 series engines are equipped with an engine protection system. The system monitors critical engine temperatures, fluid level, switch position, and pressure and will log diagnostic faults when an over or under normal operating range condition occurs. If an out-of-range condition exists, engine derate action will be initiated. The operator will be alerted by the illumination of the in-cab maintenance lamp. The warning lamp will start to flash when an out-of-range condition continues to worsen and engine shutdown will occur. The operator **must** pull to the side of the road when it is safe to do so to reduce the possibility of engine damage.

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
