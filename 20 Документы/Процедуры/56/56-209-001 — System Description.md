---
aliases:
  - "Описание системы"
type: "Процедура"
doc: "56-209-001"
title_en: "System Description"
title_ru: "Описание системы"
modified: "2006-03-03"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "4021555"
figures: 28
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-209-001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-209-001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/56"
---

# System Description
**Описание системы**

> [!abstract] Процедура · `56-209-001`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[4021555 — QSK60 Marine Alarm and Safety System Master Repair Manual|4021555]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2006-03-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-209-001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-209-001.pdf)

### General Information

The QSK60 Marine propulsion and QSK60 Dominion Marine auxiliary engines are each available as classed or non-classed engines. One of the requirements of a classed engine is an independent safety and alarm system in addition to the base engine control system. The safety system has the ability to shut down the engine, while the alarm system displays information- **only** faults onto a display panel. The terms classed and non-classed are often interchanged with full and base, respectively.

There are four different engine monitoring system options. See Tables 1 and 2.

| Table 1: Alarm and Safety System |  |  |  |  |
|---|---|---|---|---|
|  | Propulsion | Auxiliary |  |  |
| Component | Classed SD6008 | Non-Classed SD6011 | Classed SD6009 | Non-Classed SD6007 |
| Safety Module | Standard |  | Standard |  |
| 5 Safety System Switches | Standard |  | Standard |  |
| Power Module | Standard | Standard | Standard | Standard |
| Vessel Interface Terminal Strip | Standard | Standard | Standard | Standard |
| Printed Circuit Board | Standard |  | Standard | Standard |
| Speed Comparator |  |  | Standard |  |
| Quantum CM500 Base Engine ECM | Standard | Standard |  |  |
| Dominion Base Engine ECM |  |  | Standard | Standard |
| 12 Base Engine Sensors | Standard | Standard | Standard | Standard |
| Local Analog Display | Optional 1 | Optional 2 | Standard | Standard |
| 34 Alarm Sensors | Standard |  | Standard |  |
| Cetrek Display | Optional 1 | Optional 2 |  |  |
| Remote Analog Panel | Optional 3 | Optional 3 | Optional 3 | Optional 3 |
| Remote Mount Display(s) | Optional 4 | Optional 4 |  |  |

| Footnotes |  |  |  |
|---|---|---|---|
|  | Option | Description | Comment(s) |
| 1 | EG6015 | Classed engine room panel | Contains local analog display and is housed in engine room panel. |
| 2 | EG6003 | Non-classed engine room panel | Contains local analog and is housed in engine room panel with six alarm sensors. |
| 3 | EG6005 | 1 Remote analog panel |  |
|  | EG6009 | 2 Remote analog panel |  |
|  | EG6010 | 3 Remote analog panel |  |
|  | EG6011 | 4 Remote analog panel |  |
| 4 | EG6004 | 1 Remote Cetrek display |  |
|  | EG6006 | 2 Remote Cetrek display |  |
|  | EG6007 | 3 Remote Cetrek display |  |
|  | EG6008 | 4 Remote Cetrek display |  |

| Table 2: Alarm and Safety System |  |  |  |  |
|---|---|---|---|---|
|  | Location By Application |  |  |  |
| Component | Customer Interface Box | Engine Room Panel | On Engine | Remote |
| Safety Module | Auxiliary and Propulsion |  |  |  |
| 5 Safety System Switches |  |  | Auxiliary and Propulsion |  |
| Power Module | Auxiliary and Propulsion |  |  |  |
| Vessel Interface Terminal Strip | Auxiliary and Propulsion |  |  |  |
| Printed Circuit Board | Auxiliary and Propulsion |  |  |  |
| Speed Comparator | Auxiliary |  |  |  |
| Quantum CM500 Base Engine ECM |  |  | Propulsion |  |
| Dominion Base Engine ECM | Auxiliary |  |  |  |
| 12 Base Engine Sensors |  |  | Auxiliary and Propulsion |  |
| Local Analog Display | Auxiliary | Propulsion |  |  |
| 34 Alarm Sensors |  |  | Auxiliary and Propulsion |  |
| Cetrek Display |  | Propulsion |  |  |
| Remote Analog Panel |  |  |  | Auxiliary and Propulsion |
| Remote Mount Cetrek Display(s) |  |  |  | Propulsion |

![[15600056.png]]

The alarm and safety system consists of three independent systems:

| A. Control | B. Alarm | C. Safety |
|---|---|---|
| 1. Control Sensors | 6. Alarm Sensors | 10. Safety Sensor |
| 2. Cetrek Display | 7. Local Analog Display | 11. Safety Module |
| 3. ECM | 8. Interface Box |  |
| 4. Fuel System Control Valves | 9. Remote Analog Display |  |
| 5. Fuel System Shutoff Valve |  |  |

The propulsion and auxiliary options share much of the same basic hardware, although they are packaged differently. One primary reason for this difference is that the auxiliary engines have the Dominion ECM mounted off-engine in the customer interface box, while the propulsion engines have a CM500 ECM mounted on-engine in the same fashion as the industrial configuration.

The local analog display and the remote analog panel have a common display. There are seven analog channels and an hour meter displayed on the screen. Each analog channel features:

![[15600117.png]]

A. Parameter icon, ISO standard when possible

B. Digital value for the parameter

C. Icon, indicating units

D. Bar or dial RPM indicator

E. System fault icon, indicates sensor or wiring fault

F. Hour meter

G. General system fault icon, indicates internal local analog display or remote analog panel failure.

![[15600057.png]]

1. Coolant temperature
2. Left bank exhaust stack temperature
3. RPM
4. Right bank exhaust stack temperature
5. Battery voltage
6. Engine oil pressure
7. Marine gear oil pressure (optional).

The local analog display and remote analog panel performs a self-test at startup.

- Yellowish-green segments, red default icons and green bars and dials are lit for three to five seconds
- Bars and dials turn red for three to five seconds
- Displays real-time values.

After the self-test, the screen displays the current value present on the analog card inputs, unless the configuration serial link is connected and active. In that case, the lamps remain red as long as the serial link is active.

The configuration serial link is shipped with the local analog display from the factory.

![[15600096.png]]

If the local analog display and the remote analog panel need to be configured when replaced in the field, the following changes can be made by a Cummins technician or end user using a personal computer with HyperTerminal or other telnet software and the configuration serial link:

- Gear oil pressure channel enabling or disabling
- Gear oil pressure threshold setting
- Gear oil pressure RPM inhibit setting
- Metric versus Imperial units
- Hour meter display.

> [!note] Note · Примечание
> HyperTerminal is a standard program found on most personal computers with Microsoft® Windows.

To change software setting a personal computer **must** be connected to the serial port (RS-232) as shown.

The following is for the local analog and remote analog panel.

Customer Interface Box

The customer interface box provides an interface point from the vessel to the alarm and safety system to the terminal strip. It also displays information to the local analog display (auxiliary **only**) and safety module. The customer interface box is located in the engine room.

![[15600104.png]]

Engine Room Panel

The engine room panel displays information to the local analog display and the Cetrek display. Located in the engine room (propulsion **only**).

![[15600105.png]]

Displays

The safety module is used on classed propulsion and auxiliary applications and monitors five safety switches as well as an optional external input. The safety module will shut down the engine when a parameter drops below the set threshold.

> [!note] Note · Примечание
> The shutdown feature is inhibited below 500 rpm.

![[15600106.png]]

The local analog display is located in the engine room and is used to start and stop the engine, acknowledge alarm faults, toggle the local and remote start function, as well as display certain engine parameters. It is installed in the engine room panel and customer interface box on propulsion and auxiliary applications, respectively.

> [!note] Note · Примечание
> The alarm faults do **not** cause an engine derate or shutdown. A derate or shutdown can **only** be triggered by the base engine ECM or the safety module.

Up to four remote analog panels can be mounted remotely and are used to display engine information as well as to start the engine when the local analog display has granted remote control. The remote analog panel can **not** be used to acknowledge alarm faults, but it can be used to silence alarms by pressing the Silence Horn button.

![[15600109.png]]

Displays engine information and fault codes and is located in the engine room panel or remotely (propulsion **only**).

![[nobox.png]]

Alarm status is **only** monitored by the local analog display unit, as **only** the local analog display has access to the analog signal inputs. The local analog display broadcasts alarm status and parameter values to each remote analog panel. Alarm acknowledgement is possible **only** on local analog display.

There are two possible kinds of alarms: process alarms and system faults.

Process alarm: Monitors parameters that exceed a defined limit, such as a pressure or temperature threshold.

Actions:

- The associated bar graph will flash red upon the sensor value passing the threshold value
- The buzzer will sound
- Pressing the silence horn button ceases the horn, but the bar graph will still be flashing red
- Pressing the Acknowledge button will stop the bar graph from flashing, but will remain orange until the threshold issue has been resolved.

![[nobox.png]]

System Fault: A fault on the monitoring equipment itself, such as a sensor fault, a broken wire or bad contact, or an internal default in the local analog display or the remote analog panel failure.

Actions:

- The associated bar graph will flash red upon the sensor fault issue as well as the sensor fault light (located directly beneath the bar graph)
- The buzzer will sound
- Pressing the silence horn button ceases the horn, but the bar graph will still be flashing red
- Pressing the Acknowledge button will stop the bar graph from flashing, but will remain orange until the sensor fault issue has been resolved.

General System Fault: Indicates internal local analog display or remote analog panel failure.

The icon lights to indicate an internal local analog display or remote analog panel failure.

![[nobox.png]]

The safety system is a completely independent engine monitoring system. The safety switches monitor various engine parameters and provides a signal to the safety module in the customer interface box. The safety system is designed to shutdown the engine when certain operation parameters exceed the switch setpoint for a specified length of time.

![[nobox.png]]

Power Module

The power module, also known as the power supply monitoring and safety device, is used in both propulsion and auxiliary classed applications and is located inside the customer interface box. The purpose of the power module is to filter the AC power from the two classed-required power supplies and to help protect the customer interface box circuitry to the two 15 Amp blade fuses and the three 2 Amp blade fuses.

There is a green indicator lamp for each power supply. The lamp will be lit when 24 VDC is present.

![[15600107.png]]

Vessel Interface Terminal Strip

The vessel interface terminal strip provides an interface point from the vessel to the alarm and safety system. The vessel interface terminal strip in located inside the customer interface box.

![[15600104.png]]

Printed Circuit Board

The printed circuit board provides a common connection point for many of the different harness connections associated with the customer interface box. It also provides a location for the relays used to implement the control functions. Thirdly, it provides a location for the electronic circuitry that is required to interface to the electronic control module (ECM) and other modules in the system.

![[15600115.png]]

Speed Comparator

The speed comparator monitors engine speed with a 0-1mA input on pins 1 and 2 provided by the Dominion ECM. The speed comparator closes a relay when the engine speed is greater than or equal to 85 percent of rated speed. The relay opens when engine speed is less than 85 percent of rated speed. The speed comparator output signal is used by the OEM control system for verification to engine operating state.

The OEM control system will **not** allow the generator set to accept load if the speed comparator output on pins 6 and 8 is open circuit. When engine speed is greater than or equal to 85 percent of rated speed, the red alarm lamp on the front of the speed comparator will be illuminated. The threshold potentiometer below the alarm lamp is used to adjust the setpoint at initial installation of the generator set. The speed comparator is mounted inside of the customer interface box next to the printed circuit board. Refer to Procedure [[56-209-001 — System Description|209-001]] for setpoint adjustment.

![[15600060.png]]

Remote Analog Panel

The remote analog panel is used to display engine information as well as start the engine when the local analog display has granted remote control. The remote analog panel can **not** be used to acknowledge alarm faults, but can be used to silence alarms by pressing the silence horn button.

![[15600105.png]]

Alarm Sensors

The alarm system is a completely independent engine monitoring system that uses sensors to monitor various engine parameters. As described in the local analog display, six of these sensors are alarmed by the local analog display: coolant temperature, left and right bank exhaust stack temperature, engine oil pressure, marine gear oil pressure (optional), and the rpm. Battery voltage is also alarmed and measured by the local analog display. The remaining sensors are wired to the terminal strip in the customer interface box and **must** be alarmed by the vessel alarm system.

> [!note] Note · Примечание
> **Only** the base engine control system and safety system can derate or shutdown the engine.

![[15600104.png]]

Master Switch

The master switch is the master battery switch and is located in the customer interface box in the auxiliary application and in engine room panel propulsion applications.

![[15600105.png]]

Terminal Box

The terminal block allows the alarm system pressure sensors to be tested for proper operation while the engine is running, and also provide a convenient test point to measure fluid pressures.

![[15600110.png]]

The Local and Remote button is **only** present on the local analog display and the status is indicated by a lamp. The Control button toggles the Local and Remote lamps.

![[15600108.png]]

On the remote analog panel unit, the Acknowledgement push button is replaced by a dimmer push button. Repeatedly pressing the Dimmer push button will cycle through four brightness levels. When the unit is powered on, brightness is automatically set to level four (brightest).

![[15600105.png]]

### Setup

The following equipment is needed:

- A personal computer or laptop with an available 9-pin COM port (serial port) and HyperTerminal or other telnet software
- Configuration serial link cable (a RS232 or Universal Serial Bus adapter may be needed for some laptops).
- Local analog display and remoter analog panel.

Using the configuration serial link cable.

1. Connect the 9-pin connector to the personal computer serial connector
2. Connect the 4-pin terminal block connector to the RS-232 connector (J8) on the back of the local analog display and remote analog panel.

1. Start HyperTerminal (Start/All Programs/Accessories/Communications/HyperTerminal)
2. In the Connection Description window, type local analog display into the Name: field and click OK
3. In the Connect To window, change the Connect using: drop down menu to select the appropriate COM port.
4. Click OK
5. HyperTerminal will have to be configured the first time it is used. In the COM Properties window, use the following settings:

- Bits per second: 4800
- Data bits: 8
- Parity: None
- Stop bits: 1
- Flow control: None

1. Click OK.

1. Push the Reset button on the back of the local analog display (upper left corner) to put the local analog display in Configuration Mode. All the lights on the front of the panel will turn on
2. After a couple seconds you will see the following prompt appear in the HyperTerminal screen: Start Serial Link local analog display /remote analog display, followed by an asterisk. The asterisk prompt indicates the local analog display /remote analog panel is ready to be configured.

1. At the \* prompt, type unitc and hit Enter to display metric units or type unitf and hit Enter to display imperial units
2. Type save and press Enter. HyperTerminal will display: Wait Please/General OK/Threshold OK/Calibration/End Save Up
3. Type end and press Enter. This puts the local analog display /remote analog panel back in normal monitoring mode
4. Disconnect the RS-232 cable
5. Shut down HyperTerminal. Click yes when prompted to save the connection local analog display. This will save the HyperTerminal configuration.

1. At the \* prompt, type rhc and hit Enter to change the hour meter. When prompted, enter in the correct engine hours and hit Enter
2. Type save and press Enter. HyperTerminal will display: Wait Please/General OK/Threshold OK/Calibration/End Save Up
3. Type end and press Enter. This puts the local analog display /remote analog panel back in normal monitoring mode
4. Disconnect the configuration serial cable
5. Shut down HyperTerminal. Click yes when prompted to disconnect and click yes when prompted to save the connection local analog display. This will save the HyperTerminal configuration.

> [!note] Note · Примечание
> The hour meter **must only** be changed when a new panel is replacing a failed panel in the field. The hour meter **must** reflect the actual hours on the engine.

To disable gear oil pressure alarm (at the prompt \*):

1. At the \* prompt, type c4d and hit Enter to disable the channel
2. Type save and press Enter. HyperTerminal will display: Wait Please/General OK/Threshold OK/Calibration/End Save Up
3. Type end and press Enter. This puts the local analog display /remote analog panel back in normal monitoring mode.
4. Disconnect the configuration serial link
5. Shut down HyperTerminal. Click yes when prompted to disconnect and click yes when prompted to save the connection local analog display. This will save the HyperTerminal configuration.

To enable the gear oil pressure alarm (at the prompt \*):

1. At the \* prompt, type c4e and hit Enter to enable the channel
2. Type wt4 and hit Enter to set the gear oil pressure alarm threshold. When prompted, enter in the threshold (will be prompted in kPa or psi depending on the display units mode) and hit Enter. The threshold is 250 psi and 1723 kPa
3. Type wtig and hit Enter to set the inhibit RPM setpoint. Below this speed, the gear oil pressure alarm will **not** trigger a low pressure alarm. When prompted, enter in the RPM threshold and hit Enter. The RPM threshold is 1100 RPM
4. Type save and press Enter. HyperTerminal will display: Wait Please/General OK/Threshold OK/Calibration/End Save Up
5. Type end and press Enter. This puts the local analog display /remote analog panel back in normal monitoring mode
6. Disconnect the configurable serial link
7. Shut down HyperTerminal. Click yes when prompted to disconnect and click yes when prompted to save the connection local analog display. This will save the HyperTerminal configuration.

Exceeded threshold alarms will be latched active until the local reset button located on the back of the safety module has been pressed or by cycling the master switch located on the front of the customer interface box.

Sensor faults can be triggered by a failed switch or faulty wiring and will **not** be latched.

If engine speed detection is unavailable due to a sensor fault, the safety module keeps engine protection shutdowns active except for low oil pressure. If the engine is shut down, either by the safety module or normal shutdown, external inhibit **must** be enabled on the safety module in order to start the engine again.

For this reason, it is important that any safety module speed sensor faults be corrected as soon as possible.

After restart, the safety module alarms can be cleared by pressing the rest button and the external inhibit can be disabled, which allows the safety module to perform engine protection (except for low oil pressure).

The speed comparator threshold is set at 85 percent of rated speed (1530 rpm for 60Hz set, or 1275 rpm for 50 Hz set). Follow the steps below to adjust the threshold:

1. Make sure the generator is off the vehicle and engine running
2. Connect and launch InPower
3. Navigate to the test folder, then to the speed override folder
4. Double-click to change engine speed reference override enable to enabled
5. The engine speed will ramp down to the override command value
6. Turn the threshold potentiometer **counterclockwise** to turn off the alarm lamp, then turn it slowly **clockwise** until the alarm lamp turns on. This is the 85 percent of rated setpoint
7. Verify the speed comparator relay is closed by checking for continuity on pins 6 and 8
8. Double click to change engine speed reference override enable to disabled
9. The engine speed will ramp up to rated speed
10. Close the connection to the module, then close InPower.

The alarm system is a completely independent engine monitoring system that uses sensors to monitor various engine parameters. As described in the local analog display section, six of these sensor are alarmed by the local analog display: Coolant temperature, left and right bank exhaust stack temperature, engine oil pressure, marine gear oil pressure (optional), and RPM. Battery voltage is also alarmed and measured by the local analog display. The remaining sensors are wired to the terminal strip in the customer interface box and **must** be alarmed by the vessel alarm system.

**Only** the base engine control system and safety system can derate or shutdown the engine.

| Alarm System Sensors |  |
|---|---|
| Description | Setpoint |
| Aftercooler Water Inlet Temperature | 71°C \[160°F\] |
| Lubricating Oil Inlet Temperature | 121°C \[250°F\] |
| Coolant Outlet Temperature | 100°C \[212°F\] |
| Intake Manifold Temperature (right bank front, rear bank rear, left bank rear) | 82°C \[180°F\] |
| Fuel Filter Outlet Pressure | 74 kPa \[10.7 psi\] |
| Fuel Filter Differential Pressure (service **only**)\* | 28 kPa \[4 psi\] |
| Lubricating Oil Pressure | 165 to 310 kPa \[24 to 45 psi\] |
| Lubricating Oil Filter Inlet Pressure | 241 kPa \[35 psi\] differential |
| Lubricating Oil Filter Outlet Pressure | 241 kPa \[35 psi\] differential |
| Lubricating Oil Filter Inlet and Outlet Pressure Sensor Check Valve | N/A |
| Coolant Pressure | 28 to 76 kPa \[4 to 11 psi\] |
| Sea Water Cooling System Pressure | To Be Determined - none in service |
| Gear Oil Pressure | OEM defined |
| Engine Speed | 1980 rpm |
| Exhaust Stack Temperature | 593°C \[1100°F\] |
| Exhaust Temperature Cylinder Number 1 (left bank), Number 8 (right bank), Number 5 (left bank), and Number 4 (right bank) | 732°C \[1350°F\] |
| Coolant Level | Shared with base engine |
| \* The fuel filter differential pressures sensor is **not** used on the latest design. |  |

| Safety System Sensors |  |
|---|---|
| Description | Setpoint |
| Lubricating Oil Pressure Switch (Low Speed Range) | 131 kPa \[19 psi\] |
| Lubricating Oil Pressure Switch (High Speed Range) | 276 kPa \[40 psi\] |
| Coolant Pressure Switch | 14 kPa \[2 psi\] |
| Coolant Temperature Switch | 220°F \[104°C\] |
| Engine Speed | 2070 rpm for auxiliary |
|  | 2280 rpm for propulsion |

### Test

> [!warning] CAUTION · Осторожно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

![[15600070.png]]

Test Connector, Self Sealing.

Test Connector, Self Sealing - To measure actual fluid pressure during engine operation, connect an adapter to the test connector. It is **not** necessary to turn the isolator valve to the OFF position due to the check valve (check valve is spring loaded (1)). This can cause an alarm.

To test the alarm system sensor, turn the isolator valve to OFF position and connect an adapter to the test connector with a controlled pressure source. Raise the pressure above the setpoint for the sensor, the slowly release the pressure until the alarm sounds.

The safety shutdown test is a procedure to demonstrate the shutdown functions of the QSK60 marine safety system.

This system is independent of both the engine alarm and engine control systems.

The safety system commands engine shutdown per the emergency stop input of the engine ECM, which drives redundant shutdown functions.

Equipment needed to conduct the tests:

- Regulated pressure source providing between 0 and 50 psi, with mating for Danfoss™ pressure manifold
- Variable temperature liquid bath capable of up to 110°C \[230F°\] for a 6 mm \[0.24 in\] diameter probe
- Frequency generator to simulate engine speed signal (rpm). Can also set safety module overspeed setpoint switch to 1475 rpm, start engine, and verify shutdown.

There are six switch inputs to the safety system that can drive a shutdown, as shown on the display panel of the safety module:

1. External shutdown command (optional input which will be a switch wired in from the vessel)
2. Low coolant pressure (switch located on the right front corner of engine, measuring temperature in left side bottom of thermostat housing)
3. High coolant temperature (switch location on the right front corner of engine, measuring temperature in left side bottom of thermostat housing)
4. Low lubricating oil pressure, low speed range (lubricating oil pressure measured at oil rifle on top of flywheel, switch is used below 1400 rpm)
5. Low lubricating oil pressure, high speed range (lubricating oil pressure measured at oil rifle on top of flywheel housing, switch is used above 1400 rpm)
6. Overspeed (measured by separate speed sensor mounted on farthest left of flywheel housing).

![[15600064.png]]

1. Shut down the engine
2. Rotate the rear-most isolation valve (1) 90 degrees **clockwise** to closed position on the manifold block mounted on the right front corner of the engine. Arrow heads will be pointing before and after rather than up and down.
3. Remove the rear-most pressure fitting cap (2) from the manifold block, and connect a regulator pressure source to the manifold port.
4. Adjust the regulated pressure source to provide at least 69 kPa \[10 psi\] into the manifold
5. Start the engine
6. Lower the regulated pressure to 6.9 kPa \[1 psi\]
7. The safety system will shutdown the engine at approximately 13.8 kPa \[2 psi\]
8. Remove the regulated pressure source, and replace the cap (2) on the manifold
9. Open the isolation valve (1) of step 2 by rotating it 90 degrees **counterclockwise**, so that the arrow heads are pointing up and down
10. Attempt to start the engine, to demonstrate it will **not** start without resetting the safety module
11. Pressure the reset button on the back of the safety module
12. Acknowledge faults on the ECM by first pressing the local analog display stop button and then the fault acknowledge button on the printed circuit board. This is for auxiliary application **only** as the Dominion ECM **must** be in stop mode, **not** Emergency stop mode to acknowledge faults.

![[15600065.png]]

1. Remove the coolant sensing element from the pocket, located on the left underside of the thermostat housing
2. Remove the P-clip bolt(s) to gain sufficient free length of the armored capillary to reach the heat bath
3. Insert the sensing element into the heat bath, with the temperature less than 99°C \[210°F\]
4. With the engine running, raise the temperature of the bath to 107°C \[225°F\]. The safety system will shut down the engine at a temperature of approximately 105°C \[221°F\]
5. Replace the P-clip bolt(s)
6. Attempt to start the engine, to demonstrate it will **not** start without resetting the safety module
7. Press the reset button on the back of the safety module.
8. Acknowledge faults on the ECM by first pressing the local analog display stop button and then the fault acknowledge button on the printed circuit board. This is for auxiliary applications **only** as the Dominion ECM **must** be in stop mode, **not** emergency stop mode to acknowledge faults.

![[15600066.png]]

1. Shut down the engine if it is in operation
2. Rotate the upper-most isolation valve (2) 90 degrees clockwise to the closed position on the manifold block mounted on the right rear corner of the engine. Arrow heads will be pointing up and down rather than before and after
3. Remove the upper-most pressure fitting cap (1) from the manifold block, and connect a regulated pressure source to the manifold port
4. Adjust the regulated pressure source to provide at least 138 kPa \[20 psi\] into the manifold
5. Start the engine and run it a idle (to be less than 1400 rpm for low speed range)
6. Lower the regulated pressure to 69 kPa \[10 psi\]
7. The safety system will shutdown the engine at approximately 103 kPa \[15 psi\]
8. Remove the regulated pressure source, and replace the cap on the manifold
9. Open the isolation valve (2) of step 2 by rotating it 90 degrees **counterclockwise**, so that the arrow heads are pointing left to right
10. Attempt to start the engine, to demonstrate it will **not** start without resetting the safety module
11. Press the reset button on the back of the safety module
12. Acknowledge faults on the ECM by first pressing the local analog display stop button and then the fault acknowledge button on the printed circuit board. This is for auxiliary applications **only** as the Dominion ECM **must** be in stop mode, **not** emergency stop mode to acknowledge faults.

![[15600067.png]]

1. Shut down the engine if it is in operation
2. Rotate the second-upper-most isolation valve (2) 90 degrees **clockwise** to the closed position on the manifold block mounted on the right rear corner of the engine. Arrow heads will be pointing up and down rather than before and after
3. Remove the second-upper-most pressure fitting cap (1) from the manifold block, and connect a regulated pressure source to the manifold port
4. Adjust the regulated pressure source to provide at least 241 kPa \[35 psi\] into the manifold
5. Start the engine and run it at rated (to be above 1400 rpm for high speed range)
6. Lower the regulated pressure to 172 kPa \[25 psi\]
7. The safety system will shutdown the engine at approximately 200 kPa \[29 psi\]
8. Remove the regulated pressure source, and replace the fitting cap (2) on the manifold
9. Open the isolation valve (2) of step 2 by rotating it 90 degrees **counterclockwise**, so that the arrow heads are pointing left and right
10. Attempt to start the engine, to demonstrate it will **not** start without resetting the safety module
11. Press the reset button on the back of the safety module
12. Acknowledge faults on the ECM by first pressing the local analog display stop button and then the fault acknowledge button the printed circuit board. This is for auxiliary application **only** as the Dominion ECM **must** be in stop mode, **not** emergency stop mode to acknowledge faults.

![[15600068.png]]

> [!note] Note · Примечание
> Another method is the set the safety module overspeed shutdown setpoint to 1475 rpm and operate the engine. The engine will shut down once the rpms increase to over 1475 rpm.

1. Connect the frequency generator to the safety system speed input
2. Disconnect the proper speed sensor from the engine harness and connect the frequency generator in its place
3. The safety system speed sensor is the left-most of three speed sensors on the top of the flywheel housing.
4. Set the frequency generator to provide a signal to the safety module of 2100 hertz, or 750 rpm (frequency = rpm x 168/60). This will activate the safety module
5. If engine was already running in step 1, reset the safety module
6. Start the engine if **not** already running
7. Increase the frequency generator output signal to 6160 Hz or 2200 rpm
8. The safety system will shut down the engine as speed passes through approximately 2070 rpm or about 5800 Hz
9. Reconnect the speed sensor for the safety system to the engine harness
10. Attempt to start the engine, to demonstrate it will **not** start without resetting the safety module
11. Press the reset button on the back of the safety module
12. Acknowledge faults on the ECM by first pressing the local analog display stop button and then the fault acknowledge button on the printed circuit board. This is for auxiliary applications **only** as the Dominion ECM **must** be in stop mode, **not** emergency stop mode to acknowledge faults.
