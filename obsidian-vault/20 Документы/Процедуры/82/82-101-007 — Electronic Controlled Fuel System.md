---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "82-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2005-01-27"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 28
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `82-101-007`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2005-01-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-101-007.pdf)

### Base Control System Description

The Signature, ISX, and ISM engine control system is an electronically operated fuel control system that also provides many operator and vehicle or equipment features.

The base functions of the control system include:

- Fueling and timing control
- Limiting the engine speed operating range between the low- and high-idle set points
- Reducing exhaust emissions while optimizing engine performance.

The system can also control the engine brakes, up to two cooling fans, an air compressor, and a Top 2 transmission.

The control system uses inputs from the operator and its sensors to determine the fueling and timing required to operate at the desired engine speed.

The electronic control module (ECM) is the control center of the system. It processes all of the inputs and sends commands to the fuel system, vehicle, and engine control devices.

The ECM performs diagnostic tests on most of its circuits and will activate a fault code if a problem is detected in one of these circuits. Along with the fault code identifying the problem, a snapshot of engine operating parameters at the time of fault activation is also stored in memory.

Active fault codes will cause a diagnostic lamp to activate to signal the driver.

The ECM can communicate with the INSITE™ service tool and some other vehicle controllers, such as transmissions, antilock braking system, automatic slip reduction, electronic dash displays, etc., through the new SAE J1939 datalink or the older SAE J1708 datalink.

Some vehicles and equipment will have J1939 networks on them that link many of the smart controllers together. Vehicle control devices can temporarily command engine speed or torque to perform one of its functions, such as transmission shifting, antilock braking, etc.

The control system utilizes a number of sensors to provide information on engine operating parameters. These sensors include:

- Coolant temperature sensor
- Intake air temperature sensor
- Intake manifold pressure sensor
- Oil pressure and temperature sensor
- Crankshaft engine position sensor (Signature, ISX, QSX15 **only**)
- Camshaft engine position sensor
- Ambient air pressure sensor
- Fuel supply pressure sensor (Signature, ISX, QSX15 **only**)
- Front and rear rail pressure sensors (Signature, ISX, QSX15 **only**)
- Fuel inlet restriction sensor
- Water-in-fuel sensor
- Wet tank pressure sensor.

The following inputs are provided by OEM-selected devices:

- Accelerator pedal position sensor
- Idle validation switch
- Engine brake selector switches
- Coolant level sensor
- Vehicle speed sensors
- Feature control switches (i.e., cruise control switches)
- Air conditioner pressure switch
- Remote throttle
- Remote PTO
- Top 2 autoshift transmission gear position sensor.

> [!note] Note · Примечание
> These inputs are application-dependent. Some applications will **not** use all of these inputs.

### Programmable Features

Slow Idle

> [!danger] WARNING · Опасно
> Deactivate the SLOW-IDLE feature during docking maneuvers. In slow-idle mode, propeller inertia can cause the engine to stall when shifting into forward or reverse, which can cause the user to collide with the dock. To reduce the possibility of personal injury, damage to the vessel, and/or the dock, turn off the SLOW-IDLE feature during docking maneuvers.

The SLOW-IDLE feature allows for lower idle speed for operation in “No Wake Zones.” When activated, the slow-idle feature reduces the engine speed to 550 rpm.

![[13200052.png]]

A single switch controls both engines on twin engine vessels.

To use the SLOW-IDLE feature:

1. The vessel **must** be in gear
2. The throttle **must** be in the idle position
3. Put the SLOW-IDLE switch in the ON position (1) by depressing the top of the rocker switch.

The engine(s) idle will decrease to 550 rpm.

![[13200060.png]]

To turn the slow-idle feature off, put the SLOW-IDLE switch in the OFF position (2) by depressing the bottom of the rocker switch.

The engine(s) will adjust to the idle set speed.

> [!note] Note · Примечание
> When the slow-idle switch is on, increasing the throttle will temporarily turn off the slow-idle feature. When the throttle is moved back into the idle position, the slow-idle feature will automatically turn itself ON again.

![[13200061.png]]

Engine Speed Control

The engine speed control (rpm ±) switch (2) allows the idle speed to be adjusted in 25-rpm increments by pressing the rocker switch.

Pressing the top of the switch increases (+) engine rpm.

Pressing the bottom of the switch decreases (-) engine rpm.

![[13200069.png]]

When the RPM ± switch (2) is used with the engine at idle, the switch will **only** work from 600 to 1000 rpm.

> [!note] Note · Примечание
> The RPM ± switch (2) will **not** change the idle speed when the engine is in SLOW-IDLE mode.

Use of the slow-idle feature will deactivate the rpm ± feature.

![[13200069.png]]

If the engine speed between the twin-engine vessels engines is **not** the same, adjust both engines to the minimum rpm setting, 600 rpm, by depressing the bottom (-) of the switch until both engines are at 600 rpm.

Then using the RPM ± switch (1), adjust the idle to the desired speed, rpm.

![[19200370.png]]

Engine Synchronization Switch

> [!danger] WARNING · Опасно
> The engine synchronization feature must be turned off before docking or low-speed maneuvering; this allows full and separate control of each engine. To reduce the possibility of personal injury, damage to the vessel, and/or the dock, turn off the engine synchronization feature before docking or low-speed maneuvering.

> [!note] Note · Примечание
> The engine synchronization feature is an option available **only** on twin-engine vessels.

The engine synchronization feature is used to electronically control the speed of both engines, using one throttle lever.

![[13200063.png]]

Normally the starboard throttle is used as the master throttle. The distributor or dealer can change it to the port throttle, if desired, by changing the master and slave plugs in the engine wiring. See the installation manual.

![[13200062.png]]

To use the engine synchronization feature:

1. Both engines **must** be in the same throttle position, running at the same rpm.
2. Put the ENG SYNC switch (1) in the ON position by depressing the top of the rocker-switch.

Both engines will adjust to the same rpm. The master throttle will control both engines.

![[13200063.png]]

> [!warning] CAUTION · Осторожно
> Adjust both throttles to the same position before turning the engine synchronization feature off. Turning the engine synchronization feature off without having both throttles in the same position can cause a sudden port or starboard turn.

To turn the engine synchronization feature off:

1. Both throttles **must** be in the same position.
2. Put the ENG SYNC switch (1) in the OFF position by depressing the bottom of the rocker-switch.

The engines speed will slowly ramp to their physical throttle settings.

![[13200063.png]]

Marine Cruise Control

The marine cruise control feature provides two adjustable engine speeds. The cruise control can be used to run the engine(s) at the optimal cruise rpm or trolling rpm.

CRUISE 1 has a default setting of 2100 rpm.

CRUISE 2 has a default setting of 1200 rpm.

> [!note] Note · Примечание
> The marine cruise control feature can be used in conjunction with the engine synchronization feature.

![[13200069.png]]

To activate the marine cruise control feature:

1. Put the cruise switch (1) in the desired position, CRUISE 1 or CRUISE 2.
2. Move the throttle(s) past the desired cruise speed.

The engine(s) speed will increase to the cruise setting.

> [!note] Note · Примечание
> When using the engine synchronization feature, the master throttle is the **only** throttle that **must** be moved past the cruise point.

![[13200069.png]]

To turn the marine cruise control off, put the cruise switch (1) in the off position (rocker-switch in the center position).

The engine(s) rpm will slowly ramp to the throttle lever setting.

![[13200069.png]]

To change the CRUISE 1 or CRUISE 2 default setting rpm:

1. With the engine running select the cruise setting that you want by setting the cruise control switch (1) to CRUISE 1 or CRUISE 2.
2. Move the throttle to the full throttle position while underway, or at the dock with the gear in neutral. The engine will not exceed the existing cruise setting. For example; if CRUISE two is at the factory setting of 1200 rpm, the engine will only reach 1200 rpm at full throttle.
3. Using the RPM ± switch (2), adjust to the cruise rpm to the new desired engine speed.

> [!note] Note · Примечание
> The cruise speeds can be set between 600 and 2100 rpm. This new setting will be saved until the cruise is adjusted again.

![[13200069.png]]

If the twin-engines are running at different speeds:

Adjust the cruise to the minimum or maximum setting, using the RPM ± switch.

Adjust the cruise to the desired setting, using the RPM ± switch.

![[13200052.png]]

If an engine will **not** reach rated rpm, make sure the marine cruise control feature is in the OFF position. If the marine cruise control feature is left in the CRUISE 1 or CRUISE 2 position, maximum engine speed will be limited to the set point of the position that the cruise switch is in.

![[13200052.png]]

### Diagnostic Fault Codes

The control system can show and record operation anomalies that present themselves as fault codes. These codes will make troubleshooting easier. The fault codes are recorded in the ECM. They can be read using the fault lamps in the cab, using a diagnostic switch, or with INSITE™.

There are two types of fault codes:

- Engine electronic control fault codes (fault has been detected with the engine or control system)
- Information codes (event that can provide important information has occurred with the engine or control system).

All fault codes recorded will either be active (fault code is currently active on the engine) or inactive (fault code was active at one time but is **not** currently active).

The WARNING lamp is yellow and indicates the need to repair the fault at the first available opportunity.

The STOP lamp is red and indicates the need to stop the engine as soon as it can be safely done. The engine **must** remain shut down until the fault can be repaired.

The MAINTENANCE lamp will illuminate, indicating some form of maintenance is required. This lamp could indicate water in the fuel filter, low coolant level, high coolant temperature, high intake air temperature, or high oil temperature.

> [!note] Note · Примечание
> The names and colors of these lamps can vary with equipment manufacturer.

To check for active engine electronic fuel system and engine protection system fault codes, turn the keyswitch to the OFF position, and move the diagnostic switch to the ON position.

Turn the vehicle keyswitch to the ON position.

If no active fault codes are recorded, both red and yellow lamps come on, go out in sequence, and remain off.

If active fault codes are recorded, both lamps come on momentarily, then begin to flash the code of the recorded faults.

The fault code will flash in the following sequence:

First, a WARNING (yellow) lamp will flash. Then, there will be a short 1- or 2-second pause after which the number of the recorded fault code will flash in STOP (red). There will be a 1- or 2-second pause between each number. When the number has finished flashing in red, a yellow lamp appear again. The three-digit code will repeat in the same sequence.

To skip to the next fault code, move the set/resume switch (if equipped) momentarily to the increment (+) position. The operator can go back to the previous fault code by momentarily moving the set/resume switch (if equipped) to the decrement (-) position. If **only** one active fault is recorded, the same fault code displays continuously when either (+) or (-) switch is depressed.

See Section TF for fault code troubleshooting.

When **not** using the diagnostic system, turn off the diagnostic switch.

### Fault Code Snapshot Data

This is additional fault code information that can be obtained by using INSITE™. The snapshot data records the value or state of the control system sensors and switches at the time a fault occurred. This data is stored for the first occurrence of the fault, since it was last cleared, and the most recent occurrence. This data can be very valuable when trying to recreate or determine engine operating conditions at the time of a fault.

### Circuit Breakers

Marine Applications

The QSM11 marine engine is equipped with two circuit breakers, located on the ECM side of the engine.

A 5-amp circuit breaker (1) is used for keyswitched power and a 10-amp circuit breaker (2) is used for non-keyswitched power. The circuit breaker panel also houses a 40-pin OEM connector (3).

![[13200057.png]]

### Engine Protection System

Illuminated Indicator Symbols

The indicator symbols (1) provide additional information on the type of fault that the ECM has detected. The individual symbols will flash during a fault condition.

> [!note] Note · Примечание
> Pressing the alarm cancel button (6) when the keyswitch is turned on will illuminate the symbols for a self-test.

![[13200088.png]]

The high intake manifold temperature lamp (1) comes on when the intake manifold temperature is above specification.

![[13200073.png]]

The high engine oil temperature lamp (2) comes on when the engine oil temperature is above specification.

![[13200074.png]]

The water-in-fuel lamp (3) interfaces with the optional water-in-fuel sensor in the primary fuel filter. It comes on when there is water in the fuel filter.

![[13200075.png]]

The high coolant temperature lamp (4) comes on when the engine coolant temperature is above specification.

![[13200076.png]]

The low coolant level lamp (5) comes on when the coolant level is below specification. Refer to Procedure [[35-018-018-tr — Cooling System|018-018]] in the Troubleshooting and Repair Manual, ISM and QSM11 Series Engines, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]], for coolant specifications.

![[13200077.png]]

The low battery voltage lamp (6) comes on when the battery voltage is below specification.

![[13200078.png]]

The low engine oil pressure lamp (7) comes on when the engine oil pressure is below specification. Refer to Procedure [[35-018-017-tr — Lubricating Oil System|018-017]] in the Troubleshooting and Repair Manual, ISM and QSM11 Series Engines, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]], for oil pressure specifications.

![[13200079.png]]

Audible Alarm/Alarm Silence

The audible alarm (8) comes on anytime the warning or caution symbols are illuminated.

![[13200066.png]]

The alarm silence button (6) will temporarily silence the audible alarm.

> [!note] Note · Примечание
> The alarm will be silenced for up to 2 minutes. As long as the fault condition exists, the alarm will “chirp” every 2 minutes to remind the operator that a fault exists.

![[13200066.png]]

The alarm silence button (6) is also used to test the warning and caution symbol lamps (1) and the gauges.

> [!note] Note · Примечание
> Like the illuminated indicator lamps, to test the gauges and symbol lamps, press the alarm silence button (6) while turning on the keyswitch. The alarm will come on for 5 seconds and for 25 seconds all symbols will illuminate and the gauge needles will move from the lowest position to the highest position and back to the lowest position.

![[13200066.png]]
