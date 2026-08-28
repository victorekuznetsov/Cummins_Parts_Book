---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "10-101-007-om-auto"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2003-04-10"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666251"
figures: 26
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-101-007-om-auto.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-101-007-om-auto.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `10-101-007-om-auto`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666251 — Signature and ISX Operation and Maintenance Manual|3666251]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2003-04-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-101-007-om-auto.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-101-007-om-auto.pdf)

### General Information

The Signature/ISX fuel system is an electronically controlled fuel injection system that optimizes fuel economy and reduces exhaust emissions. It does this by controlling the torque and horsepower curve, engine high speed, low idle, and road speed.

![[oi800v13.png]]

Signature/ISX has the capability of controlling the fan clutch actuator if an electronically controlled fan clutch is used.

Signature/ISX also allows the engine brakes to be activated by controlling the engine brake solenoids.

The electronic feature, fan control engine braking can be enabled to activate the fan clutch during engine braking. This increases the load on the engine during engine braking.

![[17c00027.png]]

### Diagnostic Fault Codes

Automotive Applications

The electronically controlled fuel system can show and record certain engine faults. The faults are shown as fault codes. These codes will make troubleshooting easier. The fault codes are recorded in the ECM.

Refer to the Signature and ISM Features Manual, Bulletin No. 3666320, for the description of the fault codes.

> [!note] Note · Примечание
> **Not** all engine irregularities are shown as fault codes.

![[17c00067.png]]

There are two types of fault codes:

- Engine electronic fuel system codes
- Engine protection system codes.

![[17c00066.png]]

The engine electronic fuel system fault codes can be seen on the WARNING and STOP lights in the cab panel.

> [!note] Note · Примечание
> Inactive fault codes can **not** be flashed out. An electronic service tool **must** be used to read inactive faults in the ECM. Refer to your Cummins Authorized Repair Location.

![[17c00030.png]]

The STOP fault light will be red. The WARNING light will be yellow or red, depending on the OEM's preference. When the vehicle keyswitch is turned on and the diagnostic switch is off, all three lights will illuminate to check their operation. The lights will go off in sequence after about 2 seconds.

![[19200053.png]]

The lights will remain off until a fault code is recorded. If a light remains on, an active fault exists.

If the STOP light (red) is illuminated while driving, the fault can be engine disabling. The vehicle **must** be driven to the side of the road and shut off as soon as it can be done in a safe manner. The vehicle **must** remain parked as long as this fault exists. If the WARNING light (yellow) is illuminated, the vehicle can be safely driven, but the fault **must** be corrected as soon as possible.

![[19200068.png]]

The engine protection system logs separate fault codes for out-of-range conditions associated with any of the following sensors:

- Coolant Temperature
- Coolant Level
- Oil Temperature
- Oil Pressure
- Intake Manifold Temperature
- Water in Fuel.

![[17c00068.png]]

This system will activate an in-cab warning device when an out-of-range condition occurs. The warning device is a light, a buzzer, or both. This system will also activate the yellow fluid lamp, if equipped.

![[oi803vz.png]]

If the light or buzzer comes on while driving, it means a fault code has been recorded. The lamp will remain on as long as the fault exists, and engine power and speed will gradually be reduced. If the out-of-range conditions continue, the light will start to flash or blink. the vehicle **must** be parked whenever severe power derates are noticed.

The fault **must** be corrected as soon as possible.

![[17c00069.png]]

Turn off the vehicle. To check for engine electronic fuel system and engine protection system fault codes, move the diagnostic switch to the ON position, or connect the shorting plug into the diagnostic connector.

![[gp8swvs.png]]

Turn on the vehicle keyswitch. If any fault codes were active during system power-down, the lights will begin to flash the code of the recorded faults. If no fault codes are recorded, the lamps will **not** flash, but will be illuminated.

![[gp8swgr.png]]

The fault code will flash in the following sequence:

First, a WARNING (yellow) light will flash. Then there will be a short 1- or 2-second pause after which the number of the recorded fault code will flash in (red) STOP. There will be a 1- or 2-second pause between each number. When the number has finished flashing in red, a yellow light will appear again. The three-digit code will repeat in the same sequence.

![[gp800kd.png]]

The lights will continue to flash the same code until the system is told to do something else. To go to the next fault code, move the cruise control/PTO switch momentarily to the RESUME/ACCEL position. You can go back to the previous fault code by momentarily moving the cruise control/PTO switch to the SET/COAST position. If **only** one active fault is recorded, the system will continuously display the same fault code when either the RESUME/ACCEL or SET/COAST switch is depressed.

![[gp8swkq.png]]

When **not** using the diagnostic system, turn off the diagnostic switch, or remove the shorting plug. If the diagnostic switch is left on or the shorting plug left in, the ECM will **not** log some faults. The maintenance monitor will **not** function correctly, either.

To stop the diagnostic system, move the diagnostic switch to the OFF position, or remove the shorting plug. Turn off the vehicle switch.

![[gp8swvv.png]]

### Engine Protection System

Signature/ISX engines are equipped with an engine protection system. The system monitors critical engine temperatures and pressures and will log diagnostic faults when an abnormal operating condition occurs. If an out-of-range condition exists and engine derate action is to be initiated, the operator will be alerted by an in-cab warning light. The warning light will blink or flash when out-of-range conditions continue to worsen. The driver **must** pull to the side of the road, when it is safe to do so, to reduce the possibility of engine damage.

> [!note] Note · Примечание
> Engine power and speed will be gradually reduced, depending on the level of severity of the observed condition. The engine protection system will **not** shut down the engine unless the engine protection shutdown feature has been selected. If the feature has been selected and the engine does shut down, the engine can be started again by turning off the keyswitch and then turning it back on.

![[17c00028.png]]

### Fuel System Description

The one data tag for the ECM is located on the front of the module housing.

![[17c00046.png]]

The engine cam and crank position sensors provide engine speed and position information.

The cam position sensor is located between the ECM and fuel pump. The crank position sensor is located below the air compressor drive.

![[17c00050.png]]

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
