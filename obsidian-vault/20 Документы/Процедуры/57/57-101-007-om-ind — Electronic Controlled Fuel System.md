---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "57-101-007-om-ind"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2003-01-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666134"
figures: 77
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/57/57-101-007-om-ind.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/57-101-007-om-ind.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/57"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `57-101-007-om-ind`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666134 — QST30 Operation and Maintenance Manual|3666134]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2003-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/57/57-101-007-om-ind.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/57-101-007-om-ind.pdf)

### General Information

Power Generation

The generator-drive control system is an electronic control system designed to optimize engine control and reduce exhaust emissions.

![[19600089.png]]

Industrial Applications

The QST30 fuel system is an electronic control system designed to optimize engine control and reduce emissions. This system consists of two in-line fuel injection pumps (one for each engine bank) and two electronic control modules (ECM). These modules work in a primary/secondary arrangement; the left bank module being the primary and the right bank module the secondary. The primary module controls fueling and timing for the left bank pump, and also commands the secondary module how to control the right bank fuel pump. These controls and commands are based on sensor input.

![[nobox.png]]

The QST30 industrial fuel system uses Bosch® RP39 fuel pumps. These pumps contain actuators that control the timing sleeves and fueling racks. Varying the current supply to these actuators via the ECM allows the QST30 fuel system to regulate engine timing and fuel metering. The ECM supply current is based on various sensor inputs it receives.

The ECM processes the information it receives from the sensors and controls the opening and closing of the actuators. This action controls timing and fuel metering and then produces the correct horsepower and torque for the latest engine condition.

![[19a00292.png]]

### QST30 System Components

Generator-Drive

The QST30 fuel system on an engine consists of:

- Fuel pump
- Fuel shutoff valve
- Fueling supply pressure sensor
- Intake manifold pressure sensor
- Oil pressure sensor
- Intake manifold air temperature sensor
- Coolant temperature sensor
- Engine speed sensor
- Rack position sensor
- Coolant level sensor
- Engine harness
- Extension harness
- Electronic control module (ECM)
- Barometric pressure sensor
- Fuel temperature sensor
- Coolant pressure sensor
- Oil level sensor
- Generator interface harness
- Fuel supply pump relay
- Oil temperature sensor.

![[nobox.png]]

The ECM processes the information it receives from the sensors and controls the movement of the fuel rack to control fueling. This action controls fuel metering, and then produces the correct horsepower and torque for the latest engine condition.

![[19a00788.png]]

Generator-Drive ECM Inputs

- Fueling supply pressure sensor (1)
- Engine speed sensor (2)
- Oil level sensor (3).

![[19a00782.png]]

- Intake manifold air pressure sensors (7)
- Oil pressure sensor (8)
- Intake manifold air temperature sensors (9)
- Coolant temperature sensor (10)
- Oil temperature sensor (10)
- Coolant level sensor (11)
- Barometric pressure sensor (12)
- Coolant pressure sensor (13)
- Fuel temperature sensor (14)
- Fueling supply pressure sensor (15).

![[19a00795.png]]

- Alternate frequency switch (16)
- Crank switch (17)
- Emergency stop switch (18)
- Remote emergency stop switch (19)
- Alarm reset switch (20)
- Idle/rated switch (21)
- Diagnostic mode switch (22)
- Droop adjust (23)
- Frequency adjust (24)
- Governor gain adjust (25).

![[19802580.png]]

The intake manifold pressure sensor (1) and the intake manifold air temperature sensor (2) are located in the intake manifold. The intake manifold pressure sensor monitors positive manifold pressures used in the air-fuel control function. The intake manifold air temperature sensor measures the turbocharged air temperature. The intake manifold air temperature sensor is also used for the engine protection system.

Refer to Section E for a more detailed component location.

![[19a00783.png]]

The engine coolant temperature sensor provides data for the engine protection system.

The coolant temperature sensor is located in the thermostat housing.

Refer to Section E for a more detailed component location.

![[19a00784.png]]

The coolant level sensor, if equipped, is mounted in the radiator top tank. It is a fluid-level-actuated switch required for the engine protection system.

> [!note] Note · Примечание
> This is an optional sensor that will **not** be on all engines. A shorting plug will be installed if the coolant level sensor is **not** used.

![[19400354.png]]

The oil pressure sensor sends signals to the ECM for the engine protection system. The sensor is located on the engine block.

Refer to Section E for a more detailed component location.

![[19a00255.png]]

The engine speed sensor provides engine speed information.

The sensor is located in the flywheel housing.

![[19a00246.png]]

Generator-Drive ECM Outputs

The ECM processes all input data and then controls these output parts:

- Fuel lift pump assembly
- Fuel shutoff valve
- Fuel pump rack actuator.

> [!note] Note · Примечание
> There are two fuel pumps/rack actuators for the QST30.

- Meter (engine speed, oil pressure, coolant temperature)
- Fault lamps (warning, shutdown, overspeed, high coolant temperature, low oil pressure, prehigh coolant temperature, prelow oil pressure).

![[19a00787.png]]

Generator-Drive Upgrade

The QST30 Upgrade fuel system on an engine consists of:

- Fuel pumps
- Fuel shutoff valves
- Oil pressure sensor
- Coolant temperature sensor
- Engine speed sensor
- Engine harness
- Engine harness adaptor cable
- OEM harness
- Electronic control module (ECM).

A kit will be available from Cummins, to upfit current QST30 generator-drive engines to the new generator-drive control system.

The upfit kit consists of:

- Generator-drive control system ECM
- Adapter harnesses.

![[nobox.png]]

Generator-Drive Upgrade ECM Inputs

- Oil pressure sensor (1)
- Coolant temperature sensor (2)
- Engine speed sensor (3).

![[19a00789.png]]

- Alternate frequency switch (16)
- Crank switch (17)
- Emergency stop switch (18)
- Remote emergency stop switch (19)
- Alarm reset switch (20)
- Idle/rated switch (21)
- Diagnostic mode switch (22)
- Droop adjust (23)
- Frequency adjust (24)
- Governor gain adjust (25).

![[19802580.png]]

The engine speed sensor provides engine speed information. The sensor is located in the flywheel housing.

![[19a00246.png]]

The oil pressure sensor sends signals to the ECM for the engine protection system. The sensor is located on the engine block.

![[19a00255.png]]

The engine coolant temperature sensor sends signals to the ECM for the engine protection system. The coolant temperature sensor is located in the upper casing of the thermostat housing.

![[00a00036.png]]

Generator-Drive Upgrade ECM Outputs

The ECM processes all of the input data and then controls these output parts:

- Fuel shutoff valves
- Common warning circuit
- Common alarm circuit
- Fuel pump rack actuator
- Relay drivers
- Meter drivers.

![[19a00787.png]]

Generator-Drive

Generator drive QST30 system

The QST30 system on a generator drive engine consists of:

1. Fuel pumps (2)
2. Fuel shutoff valves (2)
3. Oil pressure sensor
4. Coolant temperature sensor
5. Engine speed sensor
6. Engine harness
7. Engine harness adaptor cable
8. Original engine manufacturer (OEM) harness
9. Electronic control module (ECM).

![[19a00074.png]]

Generator-Drive ECM Inputs

1. Oil pressure sensor
2. Coolant temperature sensor
3. Engine speed sensor.

![[00a00028.png]]

The oil pressure sensor sends signals to the ECM for the engine protection system. The sensor is on the left bank side of the engine block behind the fuel pump.

![[19a00255.png]]

The engine coolant temperature sensor sends signals to the ECM for the engine protection system. The coolant temperature sensor is located in the upper casing of the thermostat housing.

![[00a00036.png]]

The engine speed sensor provides engine speed information. The sensor is located in the flywheel housing.

![[19a00067.png]]

Generator-Drive ECM Outputs

The ECM processes all of the input data and then controls these output parts:

- Fuel shutoff valves
- Common warning circuit
- Common alarm circuit
- Fuel pump rack actuator
- Relay drivers
- Meter drivers.

![[00a00034.png]]

Industrial Applications

The QST30 Fuel System on an industrial engine consists of two RP39 fuel injection pumps, fuel injectors, fuel shut off valves (part of the EHAB, which is integral to RP39 fuel pump), two actuators, wiring harnesses, and sensors which provide input to the ECM.

![[nobox.png]]

Industrial ECM Inputs

ECM Inputs

1. Throttle position sensor
2. Intake manifold pressure sensor
3. Intake manifold temperature sensor
4. Oil pressure sensor
5. Coolant temperature sensor
6. Coolant level sensor
7. Coolant pressure sensor
8. Ambient air pressure sensor.

![[19a00294.png]]

1. Needle movement (\#1 injector) sensor (right and left bank)
2. Engine speed/position sensor
3. Crankcase blowby flow sensor (optional)
4. Oil level sensor (optional)
5. Oil temperature sensor (optional).

![[19a00796.png]]

Industrial ECM Outputs

Electronic control module (ECM) outputs

The ECM processes all of the input data and then controls these output parts:

- Rack position actuator (integral to the RP39 fuel pump)
- Sleeve position activator (integral to the RP39 fuel pump)
- Fuel shutoff valve.

![[19a00797.png]]

### Programmable Features

Industrial Applications

INSITE™ Description

INSITE™ is a service tool for the QST30 electronic control system. Use INSITE™ to perform the following:

- Program owner-specified information into the ECM (parameters and features)
- Aid in troubleshooting the engine
- Track fuel consumption and duty cycle information.

![[19a00734.png]]

ESDN Description

The electronic software and database network (ESDN) is a personal computer PC-based system that can transfer new or updated calibration files for the QST30 industrial fuel system ECM from a central location to Cummins distributors. A calibration file is electronic data that give the engine its performance rating.

The calibration file will be loaded into ESDN, which is then used to load the file into the ECM.

Refer to Authorized Cummins Service Representative and INSITE™, Part Number 3162261, for QST30 industrial fuel system.

![[19a00735.png]]

> [!warning] CAUTION · Осторожно
> The maintenance monitor is designed to alert the operator of the need for a routine maintenance stop. Maintenance records must still be maintained for historical purposes.

> [!warning] CAUTION · Осторожно
> Do not overextend the oil drain interval as set forth in this manual. Cummins Inc. does not recommend exceeding these published intervals and is not responsible for damage sustained due to overextending drain intervals.

Refer to Section 2 for oil drain intervals.

The maintenance monitor is an optional feature that will alert the operator when it is time to change oil and perform any other simultaneous maintenance tasks.

This feature allows the customer to enter a desired time interval. The maintenance monitor will then monitor the time the engine has been operating and alert the operator when the interval has been consumed.

![[oi803ka.png]]

Alerting the Operator

The maintenance monitor feature will alert the operator of the need to change oil by flashing the engine protection lamp (fluid lamp) for approximately 12 seconds after the keyswitch is on the ON position. The flashing sequence will be four quick flashes followed by a pause. This flash sequence will go through four cycles in the 12-second period. This sequence will occur at every key-on until the maintenance monitor has been reset.

The diagnostic switch **must** be in the OFF position for the flashing sequence to occur.

Viewing Maintenance Monitor Data

With the use of INSITE™, the following maintenance data from the ECM can be viewed or printed:

- Percent of current interval consumed
- Time since last reset.

Reset Log

The maximum threshold is entered by the user.

The interval reset is the length of the maintenance interval at the time the maintenance monitor was reset.

Interval Alert Percentage

The maintenance setting allows the user to enter the percentage of the present interval at which the light should come on, indicating the need for an oil change. The parameter allows the user to obtain an early warning of the need for a maintenance stop.

For example, if the time is set to 200 hours and the interval alert percentage is set to 90 percent, the lamp will illuminate at 180 hours (90 percent of 200).

![[oi803kb.png]]

Use the following steps to reset the maintenance monitor feature after changing the oil and filters.

This entire procedure **must** be completed in less than 20 seconds.

The engine **must** be stopped to perform this procedure.

Turn the keyswitch to the ON position.

Turn the diagnostic switch to the ON position.

![[08400159.png]]

Move the throttle to 100 percent and hold for more than 3 seconds (4 seconds is sufficient).

Move the throttle to 0 percent and hold for less than 3 seconds.

Move the throttle to 100 percent and hold for less than 3 seconds.

Move the throttle to 0 percent and hold for less than 3 seconds.

Move the throttle to 0 percent and hold for less than 3 seconds.

Move the throttle to 100 percent and wait for more than 3 seconds (4 seconds is sufficient)

Move the throttle to 0 percent.

![[08400160.png]]

Turn the diagnostic switch to the OFF position.

Turn the key off and wait for a least 10 seconds.

Turn the keyswitch to the ON position.

If the fluid light does **not** blink four sets of four blinks, repeat the reset process making sure the process from the first throttle movement to the last throttle movement is completed in less than 20 seconds.

![[08400163.png]]

INSITE™ Monitor Mode

The INSITE™ monitor mode is a useful troubleshooting aid that displays the key ECM inputs and outputs. This feature can be used to spot constant or abnormally fluctuating values.

There is one screen in monitor mode. This screen is user defined by running monitor setup, and limited to 16 parameters. The ECM inputs show the data that are being fed into the ECM by the system's sensors and switches. The ECM outputs are values that ECM commands to the QST30 industrial fuel system. Monitor mode allows the relationship between the ECM inputs and outputs to be monitored and used during troubleshooting.

![[19a00736.png]]

Generator-Drive

The generator-drive control system has been designed to be flexible to meet the wide variety of engine control specifications for power generation.

![[19600089.png]]

Run/Stop Switch

A customer-supplied run/stop input supplies a ground to the ECM. Ground supplied to the ECM allows the ECM to energize the fuel shutoff valve when cranking. This switch can be monitored by using the electronic service tool.

![[19600070.png]]

Idle/Rated Speed Switch

A customer-supplied idle/rated switch allows the selection of idle or rated speed mode. This switch can be monitored by using the electronic service tool.

![[19600071.png]]

Alarm Reset Switch

A customer-supplied switch resets all shutdown/warning functions. Warning relay drivers and relay contacts can be reset while the engine is running or shut down. Shutdown relay drivers and contacts, and inactive fault codes, can be reset **only** when the engine is shut down. Before restarting the engine after a fault-induced shutdown, check the ECM for fault codes by using the electronic service tool.

![[19600088.png]]

Programmable Idle Speed

Idle speed is adjustable by using the electronic service tool. Refer to the manual for the electronic service tool for details on the feature.

![[19800902.png]]

Alternate Frequency Switch

A customer-supplied alternate frequency switch allows the selection of 50- or 60-Hz rated speed operation without requiring an electronic service tool recalibration. This switch can be monitored by using the electronic service tool.

To change frequencies, the engine **must** be shut down. For engines rated for a single operating frequency, the alternate frequency input is nonoperational.

![[00a00030.png]]

Isochronous and Droop Speed Governing

For isochronous speed operation, the governor droop setting needs to be set at 0 percent.

If required, the governor droop setting can be adjusted using the electronic service tool. Refer to the electronic service tool manual for details on the feature.

![[19600073.png]]

> [!warning] CAUTION · Осторожно
> Do not set droop above engine rated speed. Engine damage can occur.

For droop speed operation, the governor droop setting is adjustable between 0 and 10 percent.

If required, the governor droop setting can be adjusted using the electronic service tool. Refer to the electronic service tool manual for details on the feature.

![[19800902.png]]

Engine generator sets that are to operate at 60-Hz full load **must** have the engine no-load governed speed adjusted to:

61.8 Hz \[1854 rpm\] for 3-percent speed droop

or

63.0 Hz \[1890 rpm\] for 5-percent speed droop

![[19a00085.png]]

Engine generator sets that are to operate at 50-Hz full load **must** have the engine no-load governed speed adjusted to:

51.5 Hz \[1545 rpm\] for 3-percent speed droop

or

52.5 Hz \[1575 rpm\] for 5-percent speed droop

Percent speed droop on the engine-generator set can be verified by noting no-load and full-load speeds and using the speed droop formula.

| %S Droop = | (S nl − S fl) x 100 |
|---|---|
| S fl |  |

| Where: | %S Droop | = | Percent speed droop |
|---|---|---|---|
|  | S fl | = | Full-load speed |
|  | S nL | = | No-load speed |

| Example: | 1854 rpm - 1800 rpm | x 100 = 3% |
|---|---|---|
| 1800 rpm |  |  |

Droop governed speed under the available load can be calculated when full-load kW is **not** available using this formula.

| S al = S nl − | Available kW Load | x (S nl − S fl |
|---|---|---|
| Rated kW |  |  |

| Where: |  |  |
|---|---|---|
|  | S al = | Speed at available kW load |
|  | S fl = | Speed at full kW load |
|  | S nl = | Speed at no load |

Example:

| Available kW Load = | 400 |
|---|---|
| Rated kW =available kW = | 500 (generator rating) |
| Speed at full kW load = | 1800 |
| Speed at no load ==load = | 1854 |

| 1854 rpm − ( | 400 kW | ) x (1854 − 1800) |
|---|---|---|
| 500 kW |  |  |

| 1854 rpm - | (0.8 x 54) | = 43.2 rpm |
|---|---|---|

| 1854 rpm - | 43.2 rpm | = 1810.8 or 1811 rpm |
|---|---|---|

![[19600074.png]]

Droop Adjust

The droop adjust potentiometer, located in the control panel, allows the adjustment of the engine speed governor droop without the aid of the electronic service tool.

See Isochronous and Droop Speed Governing for more information on droop.

Frequency Adjust

The frequency adjust potentiometer, located in the control panel, allows the adjustment of the engine speed without the aid of the electronic service tool.

This is **only** a fine adjustment with minimal range.

Gain Adjust

The gain adjust potentiometer, located in the control panel, allows the adjustment of the governor gain without the aid of the electronic service tool.

![[19600075.png]]

> [!warning] CAUTION · Осторожно
> It takes a few seconds to initiate each gain adjustment (by using the potentiometer or electronic service tool). It is recommended that any increases in the governor gain setting be made in increments not exceeding three percent. This will reduce the possibility of prolonged periods of unwanted instability.

Governor gain can be adjusted for optimum engine performance. The governor gain is adjustable between 0.05 and 10 using the electronic service tool.

> [!note] Note · Примечание
> Typical engine-generator combinations will **not** require adjustments to the Governor Gain settings as both 1500- and 1800-rpm generator sets ordinarily exhibit satisfactory steady-state stability and acceptable transient performance with the gain value as set from the factory.

![[19800902.png]]

Speed Ramp Adjustments

The ECM provides for three speed acceleration ramp functions that are adjustable using the electronic service tool:

- Crank to rated - ramp time
- Idle to rated - ramp time
- Rated to idle - ramp time.

Crank-to-rated ramp time provides for speed ramping between cranking and rated speeds.

Idle-to-rated ramp time provides for speed ramping between idle and rated speeds.

Rated-to-idle ramp time provides for speed ramping between rated and idle speeds.

![[19a00076.png]]

Refer to the electronic service tool manual for details on the features.

Ramp times (in seconds) are dependent on idle and rated speed settings. Desired ramp times are selected by choosing ramp numbers, **not** ramp times directly.

Barber-Colman and Woodward Speed Bias Inputs

This feature provides the ability to integrate the ECM with either a Barber-Colman or Woodward Load Sharing, Auto Synchronizing, Load Commander, and so forth.

The hardware can be either analog or digital.

The feature is selectable by using the electronic service tool. Refer to the electronic service tool manual for details on this feature.

Internal Engine Hour Meter

This feature is monitored by using the electronic service tool. It indicates how many hours the engine generator has been in service.

Fault code snapshots will be stamped with a corresponding time stamp.

![[19800902.png]]

Meter Calibration

The meter calibration feature allows the generator OEM-installed meters for engine speed, coolant temperature, and oil pressure to be calibrated to the ECM meter drivers (0 to 1 mA). These calibrations can be performed using the electronic service tool.

![[19a00078.png]]

Shutdown Threshold Adjustment

Shutdown thresholds are engine parameter values at which the ECM will record and report a shutdown fault condition. These values can be adjusted down (or up in the case of the oil or coolant level) from the factory default value. This adjustment can be made using the electronic service tool.

Warning Threshold Adjustment

Warning thresholds are engine parameter values at which the ECM will record and report a warning fault condition. These values can be adjusted down (or up in the case of the oil or coolant level) from the factory default value. This adjustment can be made using the electronic service tool.

![[19800902.png]]

Overspeed Shutdown Adjustment

The overspeed shutdown threshold is the engine speed value at which the ECM will shut off fueling to the engine. This value can be adjusted down from the factory default value. This adjustment can be made using the electronic service tool.

![[19802584.png]]

### Diagnostic Fault Codes

Generator-Drive

The generator-drive control system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which make troubleshooting easier. The fault codes are retained in the ECM.

There are two types of diagnostic codes:

- Information codes inform the operator and electronic system (paralleling controllers and smart switch gear) that an event has occurred.
- Fault codes report to the operator and the electronic system that there is a problem or potential problem with the engine or fuel system.

![[19802544.png]]

Generator-Drive Control System ECM Diagnostic Lamps

The generator-drive control system ECM has five LEDs for diagnostics:

1. OS - overspeed
2. LOP - low oil pressure
3. HET - high engine temperature
4. Shutdown - engine protection shutdown has occurred
5. Warning - engine protection warning condition exists.

Generator-Drive Control System Relay Drivers

The generator-drive control system has eight relay drivers for customer-supplied relays:

- Overspeed
- Low oil pressure
- High engine temperature
- Engine protection shutdown has occurred
- Engine protection warning condition exists
- Prelow oil pressure
- Prehigh engine temperature
- Fail to start.

![[19600091.png]]

Fault Code Flashout

To flash out a fault code, the ECM **must** be put into the diagnostic mode. Enter the diagnostic mode using the diagnostic mode switch or by connecting together the two single-pin diagnostic mode enable connectors. These connectors are located above the flywheel housing near the engine speed sensor. During normal ECM operation, the two connectors are disconnected (open circuit). The ECM is placed in diagnostic mode when these two connectors are joined (short circuit).

The warning lamp will flash (signifying the start of a new fault code), and then the fault code will flash out on the shutdown lamp.

![[19600090.png]]

Fault Codes - Electronic Service Tool

The electronic service tool can be used to read the fault codes. Connect a personal computer, with the electronic service tool installed, to the engine using the service harness, Part Number 3163156. Refer to the electronic service tool manual for specifics about how to use the tool to read the fault codes.

Fault Code - Operator Interface Panel

If the customer-supplied operator interface panel has been integrated with the generator-drive control system using the RS485 datalink, the ability to read the fault codes is available; refer to the manuals supplied with the unit for more details.

Fault Code Snapshot Data

When a diagnostic fault code is recorded in the ECM, the ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.

To Clear a Fault Code

**Only** inactive fault codes can be cleared. The electronic service tool is the **only** way to clear an inactive fault code.

The engine **must** be shut down to clear inactive shutdown faults.

All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (was active at some time, but is **not** presently active).

![[19800902.png]]

Industrial Applications

The QST30 fuel system can record and display certain detectable fault conditions. These failures are displayed as fault codes to simplify troubleshooting efforts. The fault codes are stored in the electronic control module (ECM) and can be viewed either with an INSITE™ service tool or on the control panel of a generator drive, depending on your application. A fault code summary is also available on the generator drive wiring diagram, Bulletin 3666185.

There are two types of fault codes. There are engine electronic fuel system fault codes and engine protection system fault codes.

All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at some previous time, but is **not** presently active).

![[19400328.png]]

Inactive fault codes can **only** be viewed using INSITE™.

To read the fault codes, the ECM **must** be powered up in either the RUN or DIAGNOSTIC mode.

To enter the diagnostic mode, remove the diagnostic connector shorting cap from the engine harness.

To clear fault codes, the engine **must not** be running and the ECM **must** be in the diagnostic mode.

![[19a00042.png]]

The fault conditions will cause the Common Warning or Common Alarm relay outputs (2A at 30 VDC) to be energized by the ECM. Generator OEM selected devices, using these circuits, will make the operator aware that a fault condition exists.

A Common Warning relay output will still allow the engine to be operated. However, if a common warning is caused by a bad sensor, engine protection will be lost for that parameter. The condition **must** be repaired as soon as convenient.

A Common Alarm relay output will shut down the engine and will **not** allow it to be operated until the STOP/RUN switch is cycled.

![[00a00021.png]]

The conditions will cause the Relay Driver (200 mA at 24 VDC) to be energized by the ECM. Generator OEM selected devices, using these circuits, will make the operator aware which fault condition exists.

The Common Warning, Common Alarm and relay driver outputs will remain energized (even if the fault code goes inactive) until the ALARM/RESET button is pushed.

The engine protection system records separate fault codes when an out-of-range condition is found for any of the sensors in the engine protection system.

For explanation of fault codes and procedures for correcting them, contact your Cummins Authorized Repair Location.

![[19a00087.png]]

To exit the diagnostic mode, install the shorting plug in the diagnostic connector.

![[19a00080.png]]

All fault codes recorded will either be active (fault is currently occurring) or inactive (the fault was active for some time, but it is **not** presently active).

Active fault codes can be read using the warning lamps in the vehicle cab or the INSITE™ electronic service tool. Inactive faults can **only** be viewed on INSITE™.

![[19400564.png]]

When the vehicle keyswitch is turned ON, all lamps will light for 2 seconds to show that they are working.

![[19400562.png]]

Two seconds after the lamps go off, the yellow warning lamp will begin to flash out all active CENSE™ fault codes, if there are any active fault codes, or the red warning lamp will flash out all active QST30 fuel system fault codes, if there are any.

![[19400563.png]]

The numbers for the active fault codes will flash out in the following sequence. The yellow or red lamp will flash out the digits of the active fault codes.

There will be a two second delay between digits in a given fault code and a three second delay between different fault codes.

Active fault codes will continue to flash out as long as the vehicle keyswitch is ON.

![[19400567.png]]

Troubleshooting And Repair Charts

The explanation and correction of all of the fault codes are in the troubleshooting charts in Section TF in the Troubleshooting and Repair Manual, Electronic Control System, QST30 Series Engines, Bulletin [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]].

Electronic fault code troubleshooting trees are in numerical order. An index is located at the beginning of Section TF.

Refer to the INSITE™ user's manual for more information.

![[nobox.png]]

Fault Code Datalog

When a diagnostic fault code is recorded in the ECM, the values of certain sensor are captured in a snapshot datalog. This datalog records sensor values for a certain period before and after the fault occurred. For more information, on the fault code datalog feature, refer to the INSITE™ user's manual.

Fault codes can be accessed in three different ways:

1. Flashout
2. Electronic service tool
3. Operator interface panel.

![[19400357.png]]

### Fault Code Snapshot Data

When a diagnostic fault code is recorded in the ECM, the input and output data is recorded from all sensors and switches. Snapshot data allows the relations between ECM inputs and outputs to be views and used during troubleshooting.

Fault code snapshot data can **only** be viewed on the INSITE™ service tool.

When a diagnostic fault code is recorded in the ECM, the ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.

Customer-Selectable Sensor Options

This feature allows the customer to add features to the electronic sensor package if desired. The optional sensors are:

- Oil level switch
- Coolant level switch
- Aftercooler water inlet temperature sensor.

These sensors can be activated via the electronic service tool. Refer to the electronic service tool manual for details on how to activate each of the sensors.

![[19400357.png]]

### Engine Protection System

Generator-Drive

Generator-drive control system engines are equipped with an engine protection system. The system monitors critical engine speeds, temperature, and pressure, and will log diagnostic faults when an over or under-normal operating range condition occurs. If an out-of-range condition exists, the common warning circuit is energized. The common alarm circuit will be energized when an out-of-range condition continues to get worse and engine shutdown occurs.

![[19600090.png]]

INPOWER™ Service Tool

INPOWER™ is a service tool for the generator-drive control system. Use INPOWER™ to:

- Program owner-specified information into the ECM (parameters and features)
- Aid in troubleshooting the engine
- Change the engine power or rated speed calibration.

Refer to INPOWER™ manual for specifics.

INPOWER™ Adjust Mode

The adjustment feature allows adjustments to generator parameters for trims and settings. There are several adjustment parameters; **not** all generator sets will have the same adjustments available.

INPOWER™ Monitor Mode

The INPOWER™ monitor mode is a useful troubleshooting aid that displays the key ECM inputs and outputs. This feature can be used to spot constant or abnormally fluctuating values.

The ECM inputs show the data that are being fed into the ECM by the system's sensors and switches. The ECM outputs are values the ECM commands to the generator-drive control system. Monitor mode allows the relationship between the ECM inputs and outputs to be monitored and used during troubleshooting.

INPOWER™ PRO Description

INPOWER™ PRO allows a user to transfer new or updated calibration files for the generator-drive control system ECM from a central location to Cummins Distributors. A calibration file is electronic data that give the engine its performance rating.

The calibration file will be loaded into INPOWER™, which is then used to load the file into the ECM.

Refer to your Cummins Service Representative and the INPOWER™ manual for more information.

INPOWER™ Test Mode

The test feature is a diagnostic tool used to perform internal self-checks on the PowerCommand Control to verify inputs and outputs of the control system and test engine protection functions.

![[19800902.png]]

Industrial Applications

QST30 industrial fuel system engines are equipped with an engine protection system. The system monitors critical engine temperatures, fluid level, switch position, and pressure, and will log diagnostic faults when an above- or below-normal operating range condition occurs. If an out-of-range condition exists, engine derate action will be initiated. The operator will be alerted by the illumination of the in-cab fluid lamp. The warning lamp will start to flash when out-of-range condition continues to get worse and engine shutdown will occur. The operator **must** pull to the side of the road, when it is safe to do so, to reduce the possibility of engine damage.

The number of fault codes can be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.

The engine protection system monitors the following sensors:

- High coolant temperature
- Low coolant level
- Low coolant pressure
- High intake manifold temperature
- Low to very low oil pressure
- Engine overspeed
- High oil temperature
- Fuel pressure
- Fuel temperature.

Engine protection enable **must** be selected to enable calibration dependent speed and torque derates. Engine protection shutdown **must** be selected to enable calibration dependent engine shutdown features. The engine protection shutdown feature is enabled or disabled in the ECM calibration. Calibration features vary by OEM. Contact the equipment OEM if changes are needed to the engine protection shutdown feature.

![[19400565.png]]

### Flow Diagram

Electric Fuel Lift Pumps

The fuel supply pumps (5) draw fuel from the fuel tank (7). The fuel supply relay (8) turns on the fuel supply pumps (5). The fuel is circulated through a fuel filter and water separator (4). Measurements are taken at the temperature sensor (6) and pressure sensor (3). The fuel then flows to the right bank fuel housing and then is distributed to the left bank and right bank fuel shutoff valves (2). If necessary, the pressure relief bypass valve (9) opens to route fuel to the fuel return line (11). Fuel then flows to the Bosch® fuel injection pumps (10) and injectors (1).

![[19a00773.png]]

Mechanical Fuel Lift Pumps

Upgrade

The fuel lift pump (4) draws fuel from the customer's fuel or day tank (1). The fuel is circulated through a Cummins or customer prefilter (2) and the fuel connection block (3). The fuel then enters the fuel lift pump (4) where it is placed under pressure and circulated through the on-engine fuel filters (5). The fuel flows through the fuel shutoff valve (6) and then enters the injection pump (7), which builds injection pressure and sends fuel to each of the injectors (9) at the appropriate time.

The overflow valve (8) regulates the fuel supply pressure to the injection pump and sends excess fuel back to the fuel tank (1). This fuel will travel through the overflow valve (8) and through a “T” where it will join the unused fuel from the injector (9). The fuel will then flow through the fuel connection block (3) and back to the tank (1).

![[19400492.png]]
