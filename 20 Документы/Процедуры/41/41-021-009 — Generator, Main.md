---
aliases:
  - "Генератор основной"
type: "Процедура"
doc: "41-021-009"
title_en: "Generator, Main"
title_ru: "Генератор основной"
modified: "2007-05-03"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 7
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-021-009.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/41-021-009.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
---

# Generator, Main
**Генератор основной**

> [!abstract] Процедура · `41-021-009`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 21 - Main Power Generator - Group 21
> **Даты:** изменён 2007-05-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-021-009.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/41-021-009.pdf)

### General Information

Alternator - The alternator is a Newage Stamford, 4 pole, three phase, 60hz design. It is brushless rotating field design and is built to meet BS5000 Part 3 and international standards. The alternator is self-excited with excitation power from a permanent magnet generator (PMG) powered excitation system. The service alternator is, Part Number 397205. It will be connectable for varying voltage outputs. The procedure for connecting is included in the manuals which ship with the alternator.

The manufacturer's Installation, Service and Maintenance Manual is available on the manufacturer's website at: http://www.newage-avkseg.com/english/content/download/newage/manuals/uc/UC224-274English.pdf

> [!note] Note · Примечание
> To access this document, copy the URL above and paste it into your web browser address bar.

Generator Control Panels - There are five different generator control panel options consisting of four types of panels. A Classed Panel is one which is classified by a maritime classification society. These panels are referred to as “classed panels”. An Un-Classed Panel is one which has **not** been classified by a maritime classification society. These panels are referred to as the “un-classed panels”.

The following is a breakdown of the generator control panels options:

| Classed Options |  |  |  |
|---|---|---|---|
| Option Number | Panels Used | Quantity | Description |
| GP 9012 | 3976554 | 1 | Base Panel |
| GP 9013 | 3976554 | 1 | Base Panel |
| 3972970 | 1 | Remote Panel |  |
| GP 9014 | 3976554 | 1 | Base Panel |
| 3972970 | 2 | Remote Panel |  |

| Un-Classed Options |  |  |  |
|---|---|---|---|
| Option Number | Panels Used | Quantity | Description |
| GP 9023 | 3974732 | 1 | Base Panel |
| GP 9024 | 3974732 | 1 | Base Panel |
| 3976575 | 1 | Remote Panel |  |

The User's Manuals for the panels are available for download to the public for free at the Cummins Marine website. The address of the manuals is: http://marine.cummins.com/public\_cummins/content.jhtml?tlald=5&anchorld=37&contentld=43&marketld=13&menuld=1

> [!note] Note · Примечание
> To access the documents, copy the URL above and paste it into your web browser address bar.

The classed base panel mounts on the control cabinet as shown in Figure 1.

![[21900001.png]]

Figure 1, Classed Base Panel Cabinet.

1. Control Panel
2. Block Heater Indicator Button
3. Cable Connection
4. Emergency Stop Button.

Classed Base Control Panel - The classed base panel is an electronic control unit for controlling and monitoring diesel engines used as propulsion engines or generator sets. The classed base panel monitors the following data:

- Oil Pressure
- Oil Temperature
- Intake Manifold Pressure
- Coolant Temperature
- Battery Voltage
- Engine Speed
- Exhaust Temperature
- Total Engine Hours
- Number of Starts.

The panel is also equipped with an event log which records a history of the last 500 events such as alarms, startups, and shutdowns. The classed base control panel in cabinet is shown in Figure 2.

![[21900002.png]]

Figure 2, Classed Base Control Panel.

1. Digital display
2. LED indicator lights
3. Button A: Toggles between instrument view and alarm list view
4. Button B: Toggles between two instrument views
5. Alarm silence
6. Backlight on/off
7. Alarm acknowledge
8. Start button
9. Stop button.

The classed base panel has built in alarms. See Table 2.

| Table 2: Classed Base Panel Built in Alarms. |  |
|---|---|
| Alarm | Description |
| Low Battery Voltage | Low voltage at the start battery |
| Secondary Battery Low Voltage | Low voltage at the secondary battery source |
| Overspeed | Engine running faster than the overspeed set-point |
| Engine Stopped | Engine stopped for no known reason |
| Engine Failed to Stop | 60 seconds after issuing the stop command, the engine has still **not** stopped |
| Start Failure | Engine failed to start after the last start attempt |
| Pickup Failure | Unable to read the pickup signal while engine is running |
| Output Circuit Overload | Short circuit in one of the +24 volt terminals |
| Analog Sensor Failure | Detailed information on which analog channel has failed |
| Broken Wire | Detailed information on which terminal experienced the broken wire |

Operation of the Classed Base Panel - The classed base panel has several different screens or views. The views include two instrument views, alarm list view, information view, and event log view.

To toggle between instrument view and alarm list view, press button A (See Figure 2).

To toggle between two instrument views, press button B (See Figure 2).

To go to information view, press and hold button A for approximately one second.

To go to event log view, press and hold button B for approximately one second.

When connected to the classed remote panel, both the classed remote panel and the classed base panel can control the engine. However, it is possible to lock out the classed remote panel and allow control **only** from the classed base panel.

To lock out the classed remote panel:

1. Go to INFO view
2. Press and hold BUZZER ON/OFF for two seconds until a beep is heard. The screen will change to toggle Local Mode ON/OFF. When ON, this disables the remote panel commands.

Stop Button - To stop the unit, press and hold the red button labeled STOP until the unit has stopped. If the Stop Button is held for less than one half of a second, the engine will **not** stop. The control unit stops the generator set by pulling the stop solenoid. When the red LED in the stop button is lit it indicates that the control unit is pulling the stop solenoid.

Start Button - Manual start is activated with the green button labeled Start. Press and hold the button until the engine has started.

A running engine is indicated by the green LED in the Start button and the text Running in the far left status field on the Digital Display. The RPM-meter will indicate the engine speed.

Standby and Manual Mode Button - The Standby button is a toggle button, meaning that for every other keypress, the unit is set to Standby or Manual. A green LED in the Standby button indicates that the unit is set to Standby. The right most status field also indicates the chosen mode by displaying either Standby or Manual.

Acknowledge (Reset) Button - In case of alarms, a press on the acknowledge button, labeled Ackn, will reset the alarm(s). At the same time, the buzzer will be silenced. In the Alarm List view, Ackn will reset all alarms, whereas, in the Instrument view, Ackn will reset the alarm in the top of the screen **only**.

Buzzer OFF Button - Press the Buzzer OFF button to silence the built-in buzzer signal that is activated when an alarm occurs. The alarm that activated the buzzer remains active until acknowledged.

Classed Remote Panel Digital Display - The classed remote panel is a touch screen display that shows most of the data available from the classed base panel. It can also execute many of the same commands as the base panels. It connects to the supplied terminals on the engine cabinet with six wires. Four wires are for communication and two are for power supply. See Figure 3 for the Classed Remote Panel Digital Display.

![[21900003.png]]

Figure 3, Classed Remote Panel Digital Display.

1. Oil pressure gauge
2. Oil temperature gauge
3. Indicator light
4. Button to access the alarm list
5. Engine rpm
6. Navigate between pages
7. Battery voltage gauge
8. Start button
9. Stop button
10. Reset button
11. Coolant temperature gauge

The following analog values are available from the classed remote panel.

| Value Description | Range and Units |  |
|---|---|---|
| Oil Pressure | 0.0 - 6.0 Bar | 0 - 87 PSI |
| Oil Temperature | 0 - 150°C | 32 - 302°F |
| Coolant Temperature | 0 - 130°C | 32 - 266°F |
| Battery Voltage | 20 -30 Volts |  |
| Engine Speed | 0 - 2000 RPM |  |
| Exhaust Stack Temperature | 0 - 600°C | 32 - 112°F |
| Total Engine Hours | 0 - 99999 Hours |  |
| Trip Engine Hours | 0 - 999 Hours |  |
| Starter Counter | 0 - 99999 Starts |  |

The following shows the commands that can be executed with the classed remote panel.

| Command | Description |
|---|---|
| Engine Start | Brings up a dialog to confirm engine start |
| Engine Stop | Brings up a dialog to confirm engine stop. An ongoing start attempt can be cancelled by pressing stop |
| Acknowledge Alarms | Will acknowledge all pending alarms in the Classed Base Panel |
| Set to Standby | The Classed Base Panel will do automatic start attempts |
| Set to Manual | The Classed Base Panel will **not** do automatic start attempts |

The following lists the alarms shown by the Classed Remote Panel.

| Alarm Description | Comment |
|---|---|
| Low Oil Pressure | 1.7 Bar \[25 psi\] |
| High Coolant Temperature | 106°C \[223°F\] |
| Emergency Stop/Start Disabled | Manual emergency stop is operated. Start is disabled. |
| Low Coolant Pressure | 0.7 Bar \[10 psi\] |
| Power Failure | Either the primary or the secondary (backup) voltage supply to the DCU 305 R2 is too low |
| Overspeed | 50 Hz overspeed = 1725 RPM, 60 Hz overspeed = 2070 RPM |
| Oil Pressure | 2.4 Bar \[35 psi\] |
| Oil Temperature | 120°C \[248°F\] |
| Coolant Temperature | 104°C \[219°F\] |
| Start Failure | When set to Standby **only**. |

Un-Classed Base Panel - The un-classed base panel mounts in the cabinet as shown.

![[21900004.png]]

1. Engine harness connector
2. Control panel
3. Emergency stop button
4. Alarm horn
5. Cabinet power switch.

Un-Classed Base Panel Digital Display - The un-classed base panel is a comprehensive controller for single engine sets. The un-classed base panel is equipped with a graphic display showing icons, symbols and bar-graphs for intuitive operation. The un-classed base panel automatically starts and stops the engine on external signal from the un-classed remote panel or by pressing push buttons on the base panel itself. The un-classed base panel automatically checks engine conditions and protects against out-of-limit operation.

![[21900005.png]]

Un-Classed Base Panel Digital Display

1. Page Button - Cyclic selection of the display mode (MEASUREMENT\>ADJUSTMENT\>HISTORY)
2. Horn Reset Button - Deactivates the Horn
3. Mode - Cyclic backward selection of the generator set operation mode (AUT\>MAN\>OFF)
4. Mode - Cyclic forward selection of the generator set operation mode (OFF\>MAN\>AUT)
5. Start Button - Starts the generator set
6. Stop Button - Stops the generator set
7. Indicator Light - On = no alarm
8. Indicator Light - Flashing = generator failure, Steady On = Alarm still active, Off = No alarm active.
9. Fault Reset Button - Acknowledges faults and alarms
10. Enter Button - Confirm set-point value
11. Select the set-point, select the screen, or decrease the set-point value
12. Select the screen or select set-point

The following is a guide to the menus and operation of the push buttons:

To select the generator set mode, use button 3 or 4 to select the requested generator set operation mode (OFF - MAN - AUT).

Display Menus - There are two display menus available: MEASUREMENT and ADJUSTMENT. Each menu consists of several screens. Press button 1 repeatedly to select the requested menu.

To view measured data: Use button 1 repeatedly to select the MEASUREMENT menu. Use buttons 1 and 7 to select the screen with the requested data.

To view and edit set points:

1. Press button 2 repeatedly to select the adjustment menu
2. Use button 11 and 12 to select the requested set-points group
3. Press button 8 to confirm
4. Use buttons 11 and 12 to select requested set-points
5. Set points marked with an asterisk are password protected
6. Press button 10 to edit
7. Use buttons 11 and 12 to modify the set-point. When buttons 11 or 12 are pressed for two seconds, auto repeat function is activated
8. Press button 10 to confirm or button 1 to leave without change
9. Press button 1 to leave selected set-points group.

To change the display contrast: Press button 10 and either button 11 or 12 at the same time to adjust for the best display contrast.

Function Description:

OFF mode - No start of the generator set is possible. Outputs STARTER and FUEL SOLENOID are **not** energized. No reaction if buttons START or STOP are pressed.

MAN mode - START - starts the generator set.

STOP - stops the generator set.

Hints - The engine can run without load unlimited time. The controller does **not** automatically stop the running generator set in MAN mode. The controller does **not** start the generator set when binary input REM START/STOP is closed

Start-stop sequence (simplified).

MODE = MAN (Engine start/stop request is given by pressing buttons START and STOP)

MODE = AUT (Engine start/stop request is given by binary input REM START/STOP)

| State | Condition of Transition | Action | Next State |
|---|---|---|---|
| Ready | Start request | PRESTART on Prestart time counter started | Prestart |
| RPM greater than 2 or oil pressure greater than starting prestart oil |  | Stop (Stop failure) |  |
| OFF mode selected or shutdown alarm active |  | **Not** Ready |  |
| **Not** Ready | RPM less than 2, oil pressure less than starting prestart oil, no shutdown alarm active, other than OFF mode selected |  | Ready |
| Prestart | Prestart time elapsed | STARTER on, FUEL SOLENOID on, Maximum Crank time counter started | Cranking |
| Cranking | RPM greater than Start RPM | STARTER off, PRESTART off | Starting |
| D+ input activated or oil pressure detected or Generator voltage greater than 25% voltage nominal | STARTER off, PRESTART off | Cranking |  |
| Maximum Crank time elapsed, first attempt | STARTER off, FUEL SOLENOID off, STOP SOLENOID on Crank Failure pause timer started | Crank pause |  |
| Max Crank time elapsed, last attempt | STARTER off, PRESTART off | Shutdown (Start failure) |  |
| Crank pause | Crank Fail pause elapsed | STARTER on, FUEL SOLENOID on, STOP SOLENOID off, Maximum Crank time counter started | Cranking |
| Starting | 80% Nominal speed reached | READY TO LOAD on Minimum, Maximum Stabilizer Time counter started | Running |
| RPM 0 or an other shutdown condition | FUEL SOLENOID off, STOP SOLENOID on | Shutdown |  |
| 60 second Elapsed | FUEL SOLENOID off, STOP SOLENOID on | Shutdown (Start failure) |  |
| Running | Stop request | READY TO LOAD off, Cooling time timer started | Cooling |
| RPM equal to 0 or any other shutdown condition | FUEL SOLENOID off, STOP SOLENOID on | Shutdown |  |
| Cooling | Cooling time elapsed | FUEL SOLENOID off, STOP SOLENOID on | Stop |
| RPM equal to 0 or any other shutdown condition | FUEL SOLENOID off, STOP SOLENOID on | Shutdown |  |
| Start request | READY TO LOAD on | Running |  |
| Stop | RPM equal to 0, Oil pressure less than Starting PRESTART Oil |  | Ready |
|  | 60 second Elapsed |  | Stop (Stop failure) |

Hint - Threshold level for D+ input is 80 percent supply voltage.

AUT mode - The controller does **not** respond to buttons START or STOP. Engine start/stop request is given by binary input REM START/STOP.

Un-Classed Remote Panel - The un-classed remote panel consists of one maintained action, two part, illuminated push-button switch. The two part, illuminated push-button has a snap-action switching function and serves to start and stop the generator engine. See Figure 4.

![[21900006.png]]

Figure 4, Un-Classed Remote Panel.

1. Start/Stop Button
2. Generator Run Indicator Light.

Radiator - The package can be configured with three different cooling options, which includes a seawater heat exchanger, a keel cooler, or a fan drive and radiator.

Base Rail - Because the engine and alternator are being offered as a complete set, another new option is the Sub Base. The Sub Base option includes all the vibration damping and fastening hardware necessary to mount the engine and alternator onto the base rail. See Figure 5.

The base rail is Cummins Part Number 3976557, and is part of option number RB 9045 and RB 0944.

![[21900007.png]]

Figure 5, Base Rail
