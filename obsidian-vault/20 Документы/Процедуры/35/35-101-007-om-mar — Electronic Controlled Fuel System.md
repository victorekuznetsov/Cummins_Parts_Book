---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "35-101-007-om-mar"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2013-03-05"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4021940"
figures: 88
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-101-007-om-mar.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-101-007-om-mar.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `35-101-007-om-mar`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4021940 — QSM11 Marine Operation and Maintenance Manual|4021940]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2013-03-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-101-007-om-mar.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-101-007-om-mar.pdf)

### General Information

The system is an electronically controlled fuel injection system that optimizes fuel economy. It does this by controlling the torque and horsepower curve, air-fuel control (AFC) function, engine high speed, low idle, and road speed.

![[oi800v13.png]]

The engine has the capability of controlling the fan clutch actuator if an electronically controlled fan clutch is used.

The engine also allows the engine brakes to be activated by controlling the engine brake solenoids.

![[20200005.png]]

### Diagnostic Fault Codes

Engine Fault and Maintenance Lamps

The ENGINE FAULT and MAINTENANCE lamps are illuminated for 2 seconds when the keyswitch is turned to the ON position.

After 2 seconds, the red STOP ENGINE lamp will turn off. After an additional 1/2 second, the amber CHECK ENGINE lamp will turn off. After an additional 1/2 second, the amber ENGINE MAINT lamp will turn off.

The lamps will remain off until a fault is detected.

> [!note] Note · Примечание
> This is a self-test feature of the lamp wiring and lamps.

> [!note] Note · Примечание
> The names and colors of the lamps can vary with vessel manufacturer if non-Cummins panels are used.

![[13200070.png]]

The following chart summarizes the different lamps and their operation.

| Feature | Operator Message | Lamp Operation |  |  |
|---|---|---|---|---|
| Check Engine | Stop Engine | Engine Maintenance |  |  |
| Lamp Display | Power-up lamp test | ON then OFF | ON then OFF | ON then OFF |
| Diagnostics | Fault code flashout | Flash once/code | Flash code Number |  |
| Engine Protection | System problem |  | Slow flash |  |
| Maintenance Monitor | Interval expired |  |  | 3x5 fast flash |
| Maintenance Monitor | Interval rest |  |  | 3x5 fast flash |
| Diagnostics | Nonfatal system error | On steady |  |  |
| Diagnostics | Fatal system error |  | On steady |  |
| Diagnostics | Maintenance required |  |  | On steady |

If the STOP or CHECK ENG lamp comes on when the engine is running, it means a fault code has been recorded. The lamp will remain on as long as the fault exists. The severity of the fault will determine the lamp that will come on.

Stop Engine Lamp

The STOP ENGINE lamp is a red lamp. This lamp indicates that the engine needs to be shut down before permanent damage occurs to the engine.

> [!note] Note · Примечание
> The engine should be shut off as soon as it can be shut off safely. The engine should **not** be run until the fault is corrected.

This lamp is also used to flash out the fault code number in the diagnostic mode.

![[13200065.png]]

Check Engine Lamp

The CHECK ENGINE lamp comes on during a nonfatal system error. The engine can still be run, but the fault should be corrected as soon as possible.

> [!note] Note · Примечание
> In the diagnostic mode, the check engine lamp will flash after the stop engine lamp completes the three-digit fault code.

![[13200071.png]]

Engine Maintenance Lamp

The ENGINE MAINT lamp comes on when engine maintenance is required.

![[13200072.png]]

Engine Diagnostics

When a fault or maintenance lamp is lit, the engine diagnostics switch allows the operator to view the fault codes. The receptacle to the right of the switch is for the technician's computer connection using INSITE™ electronic service tool or Echek™ service tool.

Active fault codes can be viewed using the stop engine warning lamp as described below.

![[13200054.png]]

To view the fault codes:

1. The engine **must** be shut off (**not** running)
2. The keyswitch **must** be in the ON position
3. The ENG DIAG switch (1) **must** be in the ON position.

![[13200058.png]]

The check engine and stop engine lamps flash if there are any fault codes to display.

If there are no fault codes to display, the check engine and stop engine lamps will remain lit.

![[13200068.png]]

If there are fault codes to be displayed, the check engine lamp will flash momentarily. Then the stop engine lamp will flash the first, second, and third digits of the fault code.

Example:

- Fault Code 432
- 4 flashes, pause
- 3 flashes, pause
- 2 flashes.

> [!note] Note · Примечание
> The check engine lamp will flash between each fault code.

The pattern repeats itself until the fault is cleared or the switch is turned off.

![[13200068.png]]

To view the next fault code, press the rpm ± switch (4) in the + direction.

To view the previous fault code, press the rpm ± switch (4) in the - direction.

![[13200059.png]]

The audible alarm (8) comes on anytime the warning or caution symbols are illuminated.

![[13200066.png]]

The alarm silence button (6) will temporarily silence the audible alarm.

> [!note] Note · Примечание
> The alarm will be silenced for up to 2 minutes. As long as the fault condition exists, the alarm will “chirp” every 2 minutes to remind the operator that a fault exists.

![[13200066.png]]

The alarm silence button (6) is also used to test the warning and caution symbol lamps (1) and the gauges.

> [!note] Note · Примечание
> To test the gauges and symbol lamps, press the alarm silence button (6) while turning ON the keyswitch. The alarm will come on for 5 seconds and for 25 seconds all symbols will illuminate and the gauge needles will move from the lowest position to the highest position and back to the lowest position.

![[13200066.png]]

### Engine Protection System

Low Engine Oil Pressure

The low engine oil pressure lamp (7) comes on when the engine oil pressure is below specification. [[35-018-017-om-mar — Lubricating Oil System|Refer to Procedure 018-017]] in Section V.

![[13200079.png]]

High Intake Manifold Temperature

The high intake manifold temperature lamp (1) comes on when the intake manifold temperature is above specification.

![[13200073.png]]

High Engine Oil Temperature

The high engine oil temperature lamp (2) comes on when the engine oil temperature is above specification.

![[13200074.png]]

Water in Fuel

The water-in-fuel lamp (3) interfaces with the optional water-in-fuel sensor in the suction side fuel filter. It comes on when there is water in the fuel filter.

![[13200075.png]]

High Coolant Temperature

The high coolant temperature lamp (4) comes on when the engine coolant temperature is above specification.

![[13200076.png]]

Low Coolant Level

The low coolant level lamp (5) comes on when the coolant level is below specification. [[35-018-018-om-mar — Cooling System|Refer to Procedure 018-018]] in Section V.

![[13200077.png]]

Low Battery Voltage

> [!note] Note · Примечание
> This voltage lamp **only** applies to marine applications.

The low battery voltage lamp (6) comes on when the battery voltage is below specification.

![[13200078.png]]

### Fuel System Description

Industrial Applications

The fuel system on a QSM11 engine consists of:

1. Fuel shutoff valve
2. Oil pressure sensor and temperature sensor
3. Intake manifold boost sensor
4. Cooling plate
5. ECM
6. Engine wiring harness Deutsch connector.

![[19200112.png]]

1. OEM wiring harness
2. Engine wiring harness Deutsch connector
3. Fuel in
4. Fuel out
5. Fuel gear pump
6. Engine position sensor (EPS)
7. Coolant temperature sensor (in thermostat support)
8. Coolant level sensor (in overflow tank) - optional
9. Intake manifold temperature sensor
10. Ambient air pressure sensor.

![[19200113.png]]

The idle adjustment is in the cab panel. Use this switch to adjust the engine idle speed in increments of 25 rpm.

- Industrial - 650 to 800 rpm.

![[gp2swkp01.png]]

Each time the switch is briefly moved to the minus (-) position, the idle speed is decreased by 25 rpm. When the switch is briefly moved to the plus (+) position, the idle speed is increased by 25 rpm.

![[gp8swki.png]]

### Programmable Features

General Information

The system provides additional electronic features that enhance engine and vehicle performance and control. These are programmable features in the ECM. For more information on additional features, contact a Cummins® Authorized Repair Location.

![[19c00185.png]]

Marine Applications

Slow Idle

> [!danger] WARNING · Опасно
> Deactivate the SLOW-IDLE feature during docking maneuvers. In slow-idle mode, propeller inertia can cause the engine to stall when shifting into forward or reverse, which can cause the user to collide with the dock. Failure to turn off the SLOW-IDLE feature can cause personal injury, damage to the vessel, and/or the dock.

The SLOW-IDLE feature allows for lower idle speed for operation in “No Wake Zones.” When activated, the slow-idle feature reduces the engine speed to 550 rpm.

![[13200052.png]]

> [!note] Note · Примечание
> A single switch controls both engines on twin-engine vessels.

To use the SLOW-IDLE feature:

1. The vessel **must** be in gear
2. The throttle **must** be in the idle position
3. Put the SLOW-IDLE switch in the ON position (1) by depressing the top of the rocker switch.

The engine(s) idle will decrease to 550 rpm.

![[13200060.png]]

To turn the slow-idle feature off, put the SLOW-IDLE switch in the OFF position (2) by depressing the bottom of the rocker switch.

The engine(s) will adjust to the idle set speed.

> [!note] Note · Примечание
> When the slow-idle switch is on, increasing the throttle will **temporarily** turn off the slow-idle feature. When the throttle is moved back into the idle position, the slow-idle feature will automatically turn itself on again.

![[13200061.png]]

Engine Speed Control

The engine speed control (rpm ±) switch (2) allows the idle speed to be adjusted in 25-rpm increments by pressing the rocker switch.

Pressing the top of the switch increases (+) engine rpm.

Pressing the bottom of the switch decreases (-) engine rpm.

![[13200069.png]]

When the rpm ± switch (2) is used with the engine at idle, the switch will **only** work from 600 to 1000 rpm.

> [!note] Note · Примечание
> The rpm ± switch (2) will **not** change the idle speed when the engine is in SLOW-IDLE mode.

Use of the slow-idle feature will deactivate the rpm ± feature.

![[13200069.png]]

Twin-Engine Vessels

If the engine speed between the two engines is **not** the same, adjust both engines to the minimum rpm setting, 600 rpm, by depressing the bottom (-) of the switch until both engines are at 600 rpm.

Then using the rpm ± switch (1), adjust the idle to the desired speed, rpm.

![[19200370.png]]

Engine Synchronization Switch

> [!danger] WARNING · Опасно
> The engine synchronization feature must be turned off before docking or low-speed maneuvering; this allows full and separate control of each engine. Failure to turn off the engine synchronization feature can cause personal injury, damage to the vessel, and/or the dock.

> [!note] Note · Примечание
> The engine synchronization feature is an option available **only** on twin-engine vessels.

The engine synchronization feature is used to control the speed of both engines electronically, using one throttle lever.

![[13200063.png]]

Normally the starboard throttle is used as the master throttle. The distributor or dealer can change it to the port throttle, if desired, by changing the master and slave plugs in the engine wiring. Refer to the OEM service manual.

![[13200062.png]]

To use the engine synchronization feature:

1. Both engines **must** be in the same throttle position, running at the same rpm.
2. Put the ENG SYNC switch (1) in the ON position by depressing the top of the rocker switch.

Both engines will adjust to the same rpm. The master throttle will control both engines.

![[13200063.png]]

> [!warning] CAUTION · Осторожно
> Adjust both throttles to the same position before turning the engine synchronization feature off. Failure to do so can cause a sudden port or starboard turn.

To turn the engine synchronization feature off:

1. Both throttles **must** be in the same position.
2. Put the ENG SYNC switch (1) in the OFF position by depressing the bottom of the rocker switch.

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

To turn the marine cruise control off, put the cruise switch (1) in the OFF position (rocker switch in the center position).

The engine(s) rpm will slowly ramp to the throttle lever setting.

![[13200069.png]]

To change the CRUISE 1 or CRUISE 2 default setting rpm:

1. With the engine running, select the cruise setting that you want by setting the cruise control switch (1) to CRUISE 1 or CRUISE 2.
2. Move the throttle to the full-throttle position while underway, or at the dock with the gear in neutral. The engine will **not** exceed the existing cruise setting. For example, if CRUISE 2 is at the factory setting of 1200 rpm, the engine will **only** reach 1200 rpm at full throttle.
3. Using the rpm ± switch (2), adjust the cruise rpm to the new desired engine speed.

> [!note] Note · Примечание
> The cruise speeds can be set between 600 and 2100 rpm. This new setting will be saved until the cruise is readjusted.

![[13200069.png]]

Twin-Engine Applications

If the engines are running at different speeds:

- Adjust the cruise to the minimum or maximum setting, using the rpm ± switch.
- Adjust the cruise to the desired setting, using the rpm ± switch.

![[13200052.png]]

> [!note] Note · Примечание
> If an engine will **not** reach rated rpm, make sure the marine cruise control feature is in the OFF position. If the marine cruise control feature is left in the CRUISE 1 or CRUISE 2 position, maximum engine speed will be limited to the set point of the position of the cruise switch.

![[13200052.png]]

Industrial Applications

Alternate Droop

The alternate droop feature allows characteristics to be changed for the automotive governor and for the variable speed governor. Droop is usually expressed as a percentage. The graph to the right illustrates the isochronous (0-percent droop) and droop (more than 0-percent droop) governor characteristics. Less governor droop provides a more responsive governor for more precise engine control. More governor droop provides smoother shifting and smoother mechanical clutch engagement.

Alternate droop is available for industrial calibrations **only** and is specific to each calibration and application.

![[19801364.png]]

The alternate droop feature provides the ability to select different droop settings as follows. An OEM-provided switch can be used to select up to three droop settings (base, alternate 1, and alternate 2) and/or vehicle speed can be used to select up to five droop settings (base, alternate 1, alternate 2, Jcomm, and no selection). The final droop is based on a user-defined priority assigned to either the switch or the vehicle speed. The availability of these droop settings and abilities is dependent on the individual OEM setup and application.

![[19801365.png]]

Each alternate droop setting provides the ability to select the breakpoint droop percent for the automotive governor and droop percent for VS governor. The breakpoint speed determines what position on the engine torque curve the automotive governor will start to limit engine torque output.

![[19801366.png]]

Alternate Low Idle Speed

This feature allows for two different low-idle speed settings with normal throttle control above the low-idle speed setting. This feature is often used on electric drive haul trucks when they are traveling above 5 kph \[3 mph\].

![[19801588.png]]

The alternate low-idle feature is activated whenever the normally closed alternate low-idle switch is opened and 5 VDC are detected on the alternate low-idle signal line. The following art illustrates an alternate low-idle speed that is above the normal low-idle speed.

![[19801589.png]]

Automatic Boost Power

The automatic boost power feature will limit the time that the engine can operate on the 100-percent torque curve. Engine load intake manifold temperature and coolant temperature will be compared to thresholds to determine if boost power is available Once boost power has been selected, the amount of the time spent on the 100-percent torque curve is limited. Boost power will be active and **not** time-limited when the engine speed is below a calibration threshold. A boost power lamp will be illuminated while active, and will flash as boost power is about to time out. The availability of this feature is dependent on the individual OEM application.

![[19100058.png]]

Sensed Parameters

This feature allows an OEM-provided pressure sensor and/or an OEM-provided temperature sensor to be read by the ECM. It also determines the out-of-range limits for each sensor. If the sensor value is outside the limits, then a fault will be logged corresponding to the out-of-range sensor and a default value will be used for the out-of-range sensor. This feature can be enabled or disabled by INSITE™ electronic service tool. The Number of Inputs, Upper and Lower Pressure Thresholds, and Upper and Lower Temperature Thresholds can be adjusted by INSITE™ electronic service tool.

The temperature and pressure sensors can be used by the ECM to control other features, such as the Electronic Fan Clutch or Switched Outputs.

![[nobox.png]]

Low Idle Shutdown

The low-idle shutdown feature automatically shuts off an engine after a period of idling when there is no activity from the driver such as clutch, brake, or throttle actuation. The time interval can be changed using an electronic service tool.

The idle shutdown system will **not** be active at coolant temperatures below 43°C \[109°F\].

After an engine has been automatically shut OFF, the key **must** be turned OFF for 5 seconds before attempting a restart.

> [!note] Note · Примечание
> This feature will shut off the engine **only**. It will **not** remove power from other accessories powered by the keyswitch.

![[nobox.png]]

Hot Shutdown Monitor

The hot shutdown monitor is a selectable feature within the INSITE™ electronic service tool. If this feature is enabled, the ECM will log an inactive fault when the engine is turned OFF while still “hot” by the operator or by the engine protection feature.

![[19400357.png]]

An engine is considered “hot” when the hot shutdown load percent of the engine is above the threshold set by the INSITE™ electronic service tool. The hot shutdown load percent is based on the duty cycle load factor, which is determined from engine fueling levels.

![[nobox.png]]

Engine Protection Shutdown Manual Override

The engine protection shutdown manual override feature can override the engine shutdown process when it is necessary. The engine protection shutdown manual override feature detects the operator request for engine protection shutdown manual override, records the times of occurrences, and sends a flag to inform the engine protection shutdown feature and lamp control to restart the shutdown warning period. This feature can be enabled by INSITE™ electronic service tool.

During an engine protection shutdown sequence, the warning lamp will flash. With the engine protection shutdown manual override feature enabled, the shutdown will be overridden if the dash-mounted override switch is turned on as the warning lamp is flashing. The feature will also record a snapshot that can be viewed under the Engine Protection Data in INSITE™ electronic service tool.

![[nobox.png]]

Electronic Fan Clutch

The electronic fan clutch feature provides a pulse-width modulated signal to control a variable-speed fan clutch based on the need provided by eight possible sensor inputs, or an input from an electronic service tool. This feature will reduce fuel consumption by minimizing fan on-time and lengthen belt life by eliminating belt hop and slippage.

![[nobox.png]]

The electronic fan clutch can be enabled or disabled with the INSITE™ electronic service tool. The fan percent ON (0 to 100 percent) can be monitored and the fan clutch ramp rate adjusted in units of percent/second. Adjusting the ramp rate allows different applications to be tuned for different fan characteristics.

![[19400357.png]]

The INSITE™ electronic service tool also has the capability to control the fan clutch percent ON with the fan clutch control dialog. While the engine is running and the service tool is connected to the datalink, the user can enter the fan percent ON request between 0 and 100 percent. Controlling the fan clutch with the service tool will aid in troubleshooting and diagnostics of the fan clutch and engine cooling system. Reference the INSITE™ Electronic Service Tool Manual, Bulletin 3666148.

![[19400357.png]]

Switchable (Alternate) Torque

This feature enables an alternative electronically controlled maximum engine torque curve for optimum operating efficiency in loaded versus unloaded conditions.

![[nobox.png]]

The alternate torque feature is activated whenever the normally closed alternate torque switch is opened and 5 VDC are detected on the alternate torque signal line. Five torque versus engine speed points define the alternate torque curve.

Shown is a graph illustrating an alternate torque curve that is below the normal torque curve.

![[19801587.png]]

Multiple Unit Synchronization

The multiple unit synchronization feature allows two or more engines (up to a maximum of 11) to be controlled by a single throttle signal. There are three engine configurations available with this feature. They are soft-coupled, hard-coupled, and soft-coupled marine.

![[19801084.png]]

The soft-coupled configuration has all secondary engines in parallel.

![[19400715.png]]

The hard-coupled configuration has all secondary engines in series.

![[19400716.png]]

The soft-coupled marine configuration has all engines connected to a J1939 datalink.

![[19400714.png]]

In the soft-coupled configuration, the primary engine outputs a throttle signal on ECM pin 24. This signal is received by the secondary engine(s) on ECM pin 17. The secondary engine also receives a +5-VDC supply (OEM provided) to ECM pin 18 to complete the circuit. This setup allows all engines to remain running if a secondary engine stops running.

![[19400717.png]]

In the hard-coupled configuration, the primary engine outputs a throttle signal on ECM pin 24. This signal is received by the secondary engine(s) on ECM pin 17. The secondary engine also receives a +5-VDC supply (OEM provided) to ECM pin 18. The secondary engine then outputs the throttle signal on ECM pin 24 to the next secondary engine in the series. This process is repeated by all secondary engines until the throttle signal and +5-VDC supply are received by the primary engine.

![[19400718.png]]

In the soft-coupled marine configuration, the primary engine outputs a throttle signal to the J1939 data link pins 31, 32, and 33. Secondary engines that are connected to the data link then read the throttle value. The soft-coupled marine application also allows for primary/secondary configuration via wiring harness jumpers (pins 29, 39, and 36) instead of specific calibrations. The soft-coupled marine configuration uses a multiple unit synchronization on/off switch (pins 13 and 34) to control the enabling or disabling of the engine synchronization.

![[19400713.png]]

INSITE™ electronic service tool can be used to monitor the following parameters:

- Multiple unit synchronization couple type (soft-coupled, hard-coupled, or soft-coupled marine)
- Multiple unit synchronization engine type (primary or secondary)
- Multiple unit synchronization on/off switch
- Percent pulse-width modulate output (throttle signal).

The multiple unit synchronization couple type is **not** adjustable by the INSITE™ electronic service tool, but the type can be changed by downloading a calibration to the ECM.

![[19800902.png]]

This feature can **only** be enabled or disabled by calibration. An electronic service tool (1) will be required to download a calibration from the ESDN (2) to the engine control module (3) if this feature needs to be enabled or disabled.

![[19800897.png]]

Intermediate-Speed Control

The intermediate-speed control feature can control the engine to three programmable engine set speeds (1, 2, 3) in three different modes of operation. The three set speeds are determined by a three-position switch and a two-position switch. The three modes of operation are a manual normal set speed operation, a low speed limit operation, and a high speed limit operation.

> [!note] Note · Примечание
> These three modes of operation are set by the calibration and are **not** customer-adjustable.

An intermediate-speed droop is also programmable.

> [!note] Note · Примечание
> Depending on the electronic calibration, the third intermediate speed switch can act as a validation switch. The purpose of the validation switch is to eliminate accidentally switching to intermediate speed 1 or 2. To switch to intermediate speed 1 or 2, the validation switch **must** be engaged first; then move the intermediate-speed switch to 1 or 2.

This feature also uses a momentary increment and decrement switch to raise the engine set speed while in operation.

![[19800940.png]]

Switched Outputs

This feature provides up to two fully independent switched outputs for OEM use. The state of each switched output is determined by up to 12 different inputs to the ECM. The ECM can provide different outputs if any of the inputs are above or below calibrated thresholds. Each switched output is independent of the other in controlling parameter input and threshold settings. This feature can be enabled or disabled with INSITE™ electronic service tool. The thresholds can **not** be adjusted with INSITE™ electronic service tool.

The ECM can determine the state of the switched outputs based on the following possible inputs (either or both switched outputs can use the same inputs):

- Engine speed
- Fueling command (cubic mm per second)
- Boost pressure (in Hg)
- Auxiliary speed input (rpm)
- Oil pressure (psi)
- Coolant temperature (degrees Fahrenheit)
- Commanded throttle (percent)
- ISC 2 status (off or active)
- OEM temperature (degrees Fahrenheit)
- OEM pressure (psi)
- OEM supplied sensor (volts)
- OEM supplied switch (open or ground)

Each of these inputs can have a specified threshold and threshold type (over or under). Each of the switched outputs can be calibrated to either "on" or "off" after a threshold is crossed. Also, each output can be calibrated to change states if either any threshold is crossed or all thresholds are crossed.

![[nobox.png]]

Throttle Activated Diagnostic Switch

Throttle-activated diagnostic switch is intended to eliminate the need for a dash-mounted diagnostic switch, which is used to activate the diagnostic mode to display active fault codes in a sequence of flashing lamps. The throttle-activated diagnostic switch feature eliminates the need for a dash-mounted diagnostic switch by providing a simple sequence of throttle movements that activate the diagnostic mode.

> [!note] Note · Примечание
> This feature will work with all throttle types.

![[19400734.png]]

When the engine is **not** running, the keyswitch is turned on, and the feature flag is enabled, a sequence of three throttle cycles from 30 to 70 percent within a specific time will activate the diagnostic mode. The increment/decrement switch can be used to navigate to the next or previous fault code. In case these switches are **not** available, a throttle cycle from 30 to 70 percent will also increment to the next fault.

![[19400735.png]]

A sensitive mode is enabled when this feature is enabled. The sensitive mode is an algorithm that will automatically activate the diagnostic mode when the engine is **not** running, the keyswitch is turned ON, and any throttle-related errors are detected. This allows the user to activate the diagnostic mode when throttle errors prevent them from doing so with throttle movements.

![[19400736.png]]

Duty Cycle Monitor

The duty cycle monitor tracks the time the engine spends in 50 different operating regions. These operating regions are based on engine speed and engine torque.

![[19801115.png]]

This feature provides two short-term 500-hour resettable data blocks and one long-term 100,000-hour nonresettable data block.

![[19801116.png]]

Fuel Consumption Rate Logger

The fuel consumption rate feature allows an electronic service tool to access fuel consumption data (1=time, 2=gallons/hour).

![[19800943.png]]

This feature provides two resettable 40-hour fuel consumption periods (1 and 2). Each period records fuel consumption data in forty 1-hour segments. These 40 data segments can be graphed to show fuel consumption over both 40-hour periods (A=hours, B=gallons/hour).

![[19800944.png]]

An instantaneous fuel consumption rate and a nonresettable lifetime or running average fuel consumption rate are available on the monitor screen of an electronic service tool. In addition, the two 40-hour fuel consumption periods are individually resettable using an electronic service tool.

![[19800902.png]]

Maintenance Monitor

> [!note] Note · Примечание
> The maintenance monitor is designed to alert the operator of the need for a routine maintenance stop. Maintenance records **must** still be maintained for historical purposes.

> [!note] Note · Примечание
> The maintenance monitor uses data received from the ECM to determine the amount of fuel burned. Whenever a VSS, injector circuit, or battery voltage fault has occurred, the maintenance monitor data can be inaccurate.

The maintenance monitor is an optional feature that will alert the operator when it is time to change oil and perform any other simultaneous maintenance tasks. The maintenance monitor continuously monitors the time the engine has been operating and the amount of fuel burned to determine when it is time to change oil.

The operator **must** still be alert for any indications that the engine needs other service.

![[oi803ka.png]]

The maintenance monitor has two modes of operation:

- Automatic mode
- Time mode.

![[19200062.png]]

The automatic mode alerts the operator when it is time to change oil based on Cummins Inc. recommended interval. It determines the maintenance interval based on engine operating time and fuel burned.

When the automatic mode is selected, the severe oil drain interval duty cycle is the default.

The original factory programmed value is AUTOMATIC.

![[19200063.png]]

> [!warning] CAUTION · Осторожно
> Select the correct oil change interval for your application. Cummins Engine Company, does not recommend exceeding these published intervals and is not responsible for damage sustained due to overextended drain intervals.

The maintenance monitor automatic mode is easily adjusted to accommodate severe-, normal-, or light-duty applications and Valvoline Premium Blue 2000™ engine oil. This is done by using a Compulink™ or Echek™ service tool to enter an interval factor that corresponds to the appropriate duty cycle and type of product used.

When selecting the correct interval factor for your application, Refer to Procedure 102-002 in Section 2, to determine which oil drain interval duty cycle fits your application: Severe duty, normal duty, or light duty. Once the duty cycle is chosen, use an interval factor of 1.00 for severe duty, 1.50 for normal duty, and 2.00 for light duty.

> [!note] Note · Примечание
> These interval factors **must** be adjusted accordingly if Valvolive Premium Blue 2000™ oil is used to extend the oil drain interval. See the Valvolive Premium Blue 2000™ product literature to determine how much your drain interval can be extended.

The time mode allows the customer to enter a desired time interval. The maintenance monitor will then monitor the time the engine has been operating and alert the operator when the interval has been consumed.

![[19c00185.png]]

Alerting the operator: The maintenance monitor will alert the operator of the need to change oil by flashing the engine protection lamp (fluids lamp) for approximately 12 seconds after keyswitch ON. The flashing sequence will be three quick flashes, followed by a pause. This flash sequence will go through five cycles in the 12-second period. This sequence will occur at every keyswitch ON until the maintenance monitor has been reset.

> [!note] Note · Примечание
> The diagnostic switch **must** be in the OFF position for the flashing sequence to occur.

![[oi803kb.png]]

Resetting the Maintenance Monitor. The maintenance monitor can be reset using INSITE™ electronic service tool or by following steps 1 through 10 below. Steps 3 through 8 **must** be done within 12 seconds in order for the maintenance monitor to be reset. The diagnostic switch **must** be in the OFF position and the vehicle air system **must** be fully charged.

1. Turn the keyswitch ON (engine **must not** be operating)
2. Make sure brakes are released (service and trailer brakes)
3. Hold throttle pedal at 100-percent throttle
4. Press and release service brake three times
5. Release throttle pedal
6. Depress and hold throttle pedal at 100-percent throttle again
7. Press and release service brake three more times
8. Release throttle pedal
9. The light will flash three times
10. Turn the keyswitch OFF.

As soon as the throttle pedal is released (step 8), the engine protection lamp will flash three quick flashes. This means that the reset command has been received and the maintenance monitor will reset its distance (miles or kilometers), time (hours), and fuel (gallons or liters) to zero the next time the keyswitch is turned off (step 10).

> [!note] Note · Примечание
> If the engine protection lamp does **not** flash after the throttle pedal is released on step 8 above, the reset sequence **must** be performed again.

![[oi803kd.png]]

When viewing maintenance monitor data with INSITE™ electronic service tool, the following maintenance data can be viewed or printed from the ECM:

- Percent of present interval consumed (by either distance, time, or fuel burned)
- Distance since last reset
- Time since last reset
- Reset log (distance and time at the last three resets).

![[19c00185.png]]

The interval factor is **only** used in the maintenance monitor Auto mode to adjust the following applications:

- Severe duty
- Normal duty
- Light duty
- Extended interval when using Valvoline® Premium Blue® 2000
- Other products that extend maintenance intervals.

The interval factor can be adjusted between 0 and 5.0.

The original factory programmed value is 1.

![[nobox.png]]

The maintenance monitor interval alert percentage allows the user to enter the percentage of the present interval at which the light should come on indicating the need for an oil change. The parameter allows the user to obtain an early warning of the need for a maintenance stop.

For example, if the distance mode is set to 24,194 km \[15,000 mi\] and the interval alert percentage is set to 90 percent, the lamp will illuminate at 21,774 km \[13,500 mi\], which is 90 percent of 24,174 km \[15,000 miles\].

The interval alert percentage can be set between 0 and 100 percent.

The original factory programmed value is 100 percent.

![[nobox.png]]

Fault Lamp Sequencing

The fault lamp sequencing feature is used to determine whether the diagnostic dashboard lamps have been installed and wired correctly. After keyswitch ON, all dashboard diagnostic lamps will turn on at once and then turn off in sequence.

![[17c00030.png]]

### Circuit Breakers

Marine Applications

The QSM11 marine engine is equipped with two circuit breakers, located on the ECM side of the engine.

A 5-amperage circuit breaker (1) is used for keyswitched power and a 10-amperage circuit breaker (2) is used for non-keyswitched power. The circuit breaker panel also houses a 40-pin OEM connector (3).

![[13200057.png]]
