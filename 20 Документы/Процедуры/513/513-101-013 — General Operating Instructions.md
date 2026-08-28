---
aliases:
  - "Общие инструкции по эксплуатации"
type: "Процедура"
doc: "513-101-013"
title_en: "General Operating Instructions"
title_ru: "Общие инструкции по эксплуатации"
modified: "2025-06-11"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
  - "5411481"
figures: 61
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-101-013.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-101-013.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# General Operating Instructions
**Общие инструкции по эксплуатации**

> [!abstract] Процедура · `513-101-013`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]], [[5411481 — C Command Connect and Connect Premier Marine Panel System PS102, PS103 and PS108|5411481]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2025-06-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-101-013.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-101-013.pdf)

### General Information

ED-4

The C Command Connect and Connect Premier Marine Panel System is used to monitor basic vessel sensors, engine operating characteristics, and to control engine start and stop functions.

The C Command Connect and Connect Premier Marine Panel System is comprised of the following components the operator can interface with, which may or may **not** be supplied by Cummins Inc.:

- System enable switch (Cummins® or original equipment manufacturer (OEM)-supplied)
- Start switch (Cummins® or OEM-supplied)
- Stop switch (Cummins® or OEM-supplied)
- External alarm horn (Cummins® or OEM-supplied)
- Customer interface box (C.I.B.) (Cummins®-supplied **only**)
- Display (Cummins® or OEM-supplied).

> [!note] Note · Примечание
> The ED-4 display is **only** supplied by Cummins Inc.

> [!warning] CAUTION · Осторожно
> If a non-Cummins® supplied engine instrumentation and/or alarm system is utilized, it is the owner's responsibility to verify the engine alarm communication (visual and audible) to the operator is enabled and functional while operating the engine. • This includes aftermarket additions or modifications to the engine instrumentation and/or alarm system. • Be aware that software updates to non-Cummins® supplied engine instrumentation may inadvertently disable the engine instrumentation and/or alarm functionality. • Cummins Inc. is not responsible for failures or damage resulting from use of engine instrumentation and alarm systems that are not supplied by a Cummins® factory.

The system enable switch turns on the Cummins® C Command Connect and Connect Premier Marine Panel System. It is typically located at the main helm station and can either be the vessel's main key switch or wired separately to a remote toggle switch.

The control system and engine control module (ECM) receives switched battery input from the system enable switch when the switch is pushed to the ON position. The switch is used to send a "wake" signal to the engine ECM. The switch can also be used to shut off the engine by removing power from the entire control system.

> [!note] Note · Примечание
> If equipped, battery disconnect switch(s) should be left energized one minute after system enable switch off. Failure to do so may cause improper ECM power downs resulting in interruptions of trip data writing to long term memory.

The Cummins®-supplied switch is shown.

![[00e00117.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damage to the starting motor, do not engage the starting motor for more than 30 seconds. Wait 2 minutes between each attempt to start (electrical starting motors only).

> [!warning] CAUTION · Осторожно
> Unless the engine is equipped with starter lock out capability, activating the start switch while the engine is running will engage the starter and may result in engine damage.

PS102

The start switch is typically located on the helm panel.

The switch is pressed and held to start the engine. Typically, the switch is held for less than 5 seconds to start the engine.

A single quick press of the start switch will engage the starter, but will **not** start the engine.

Some engines are equipped with an engine starting motor protection feature. If the starting motor is engaged for 30 or more seconds, without the engine starting, the starter will be locked out from operating, allowing for proper cooling of the starting motor for 2 minutes.

The Cummins®-supplied switch is shown.

![[00e00118.png]]

The stop switch is typically located on the helm panel.

The Cummins®-supplied switch has a light that illuminates when an engine stop signal is engaged. The light will illuminate if an engine stop signal is engaged at any stop switch location on the vessel.

The stop switch is pressed and held to stop the engine. Typically the stop switch should be held for 5 seconds to stop the engine.

A single quick press of the stop switch will interrupt the system enable signal to the engine ECM, but will **not** stop the engine.

The Cummins®-supplied switch is shown.

![[00e00119.png]]

PS103

The start switch is typically located on the helm panel.

A single quick press up (2) of the start / stop switch (1) will engage the starter, and start the engine.

If the starting motor is engaged for 30 or more seconds, without the engine starting, the starter will be locked out from operating, allowing for proper cooling of the starting motor for 2 minutes.

The Cummins®-supplied switch is shown.

![[00v00097.png]]

> [!warning] CAUTION · Осторожно
> The engine must have adequate oil pressure within 15 seconds after starting. If the WARNING lamp indicating low oil pressure has not gone out or there is no oil pressure indicated on a gauge within 15 seconds, shut off the engine immediately to avoid engine damage. The low oil pressure troubleshooting procedure is located in Troubleshooting Symptoms (Section TS).

![[eg8gask.png]]

Idle the engine 3 to 5 minutes before operating with a load.

![[oi800v02.png]]

External Alarm Horn:

The external alarm horn is connected to the helm harness and is typically located behind the dash.

The ED-4 display also has an internal audible alarm horn. The internal alarm horn does **not** meet Cummins® requirements. Therefore, the external horn is mandatory.

The alarm horn is an audible warning to the operator for select vessel, engine, and transmission sensor fault conditions.

The audible alarm horns can **not** be disabled.

The following audible alarms will be heard for fault severities:

- Warning - a single instance of multiple short beeps; Typically three beeps.
- Critical - repeating cycle of a longer constant tone.

![[00e00120.png]]

There are two configurations of the C.I.B.

1. C Command Connect
2. C Command Connect Premier.

The Premier configuration contains a Cummins®-supplied ED-4 display.

![[15e00014.png]]

Each engine will have its own C.I.B.

The C.I.B. contains the following:

1. Engine start and stop switch
2. ED-4 display (Connect Premier option **only**)
3. Circuit breakers
4. Battery positive connection lug
5. Polytetrafluoroethylene sealed membrane vent
6. Battery negative connection lug
7. J1939 3 pin connection
8. Main extension wiring harness connection
9. OEM sensor wiring harness connection, if equipped (Connect Premier option **only**)
10. National Marine Electronics Association (NMEA) 2000® connection (Connect Premier option **only**)
11. OEM interface wiring harness connection
12. Engine interface wiring harness connection.

![[15e00015.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damage to the starting motor, do not engage the starting motor for more than 30 seconds. Wait 2 minutes between each attempt to start (electrical starting motors only).

PS102

CIB Engine Start/Stop Switch:

The C Command Connect and Connect Premier start/stop switch is located on the C.I.B.

The C.I.B. engine start/stop switch (1) is a 2-way momentary switch.

The start side of the switch (2) is pressed and held to start the engine. Typically, the switch is held for less than 5 seconds to start the engine.

A single quick press of the start switch will engage the starter, but will **not** start the engine.

> [!note] Note · Примечание
> Some engines are equipped with an Engine Starting Motor Protection feature. If the starting motor is engaged for 30 or more seconds, without the engine starting, the starter will be locked out from operating, allowing for proper cooling of the starting motor for 2 minutes.

The stop side of the switch (3) is pressed and held to stop the engine. Typically the stop switch should be held for 5 seconds to stop the engine.

A single quick press of the stop switch will interrupt the system enable signal to the engine ECM and interrupt combustion, but will **not** stop the engine.

The start/stop switch has lights that illuminate when an engine start or stop signal is engaged.

The lights will illuminate if an engine start or stop signal is engaged at any start or stop switch location on the vessel.

![[00e00121.png]]

PS103

C.I.B. Engine Start/Stop Switch:

The C Command Connect and Connect Premier start/stop switch is located on the C.I.B.

The C.I.B. engine start/stop switch (1) is a 2-way momentary switch.

A single quick press up (2) of the start / stop switch (1) will engage the starter, and start the engine.

> [!note] Note · Примечание
> If the starting motor is engaged for 30 or more seconds, without the engine starting, the starter will be locked out from operating, allowing for proper cooling of the starting motor for 2 minutes.

If engine is running, a single quick press up (2) of the start/stop switch (1) will stop the engine.

The start/stop switch has lights that illuminate when an engine start or stop signal is engaged.

The lights will illuminate if an engine start or stop signal is engaged at any start or stop switch location on the vessel.

![[00e00173.png]]

C.I.B. ED-4 Display:

The ED-4 display is only supplied by Cummins. The ED-4 display (1) is connected with the ECM through a Society of Automotive Engineers (SAE) J1939 data link. The display will indicate engine operating parameters and fault codes. The display is the gateway for relaying engine ECM information to NMEA 2000®.

When mounted at the C.I.B., the display requires a unique software load for the C Command Connect Premier Panel System and is **not** common with other Cummins® controls systems.

The display software name and version can be found in the “About” menu screen.

The display comes preloaded with software and is updateable.

When mounted at the C.I.B., the display's vessel personality file will need to be updated for each vessel application at initial install by the OEM or, if replaced, during a service event.

> [!note] Note · Примечание
> Contact a Cummins® distributor for ED-4 display software and vessel personality file updates.

![[15e00021.png]]

ED-4 Display (Helm Mounted):

> [!note] Note · Примечание
> The ED-4 display is **only** supplied by Cummins.

The display is typically connected to the ECM through a SAE J1939 data link. The display will indicate engine operating parameters and fault codes. The display is the gateway for relaying engine ECM information to NMEA 2000®. When mounted at the helm, the display requires a unique software load for the C Command Connect and Connect Premier Marine Panel System and is **not** common with other Cummins® controls systems.

The display software name and version can be found in the “About” menu screen.

The display comes preloaded with software and is updateable.

When mounted at the helm, the display's vessel personality file will need to be updated for each vessel application at initial install by the OEM or, if replaced, during a service event.

> [!note] Note · Примечание
> Contact a Cummins® distributor for ED-4 display software and vessel personality file updates.

![[15e00022.png]]

The ED-4 display is an LCD that provides information to the operator.

The user can interact with the display through keys (1 through 5) on the front of the display.

The function of the key is shown on the ED-4 screen above the key, which changes as selections are made.

A variety of engine and vessel data, fault/alarm codes, diagnostics, and configuration setups can be viewed on the ED-4 display.

Reference the sections below for general ED-4 access and setup information.

Contact a Cummins® distributor for setup information located in the Configuration page.

> [!note] Note · Примечание
> Modifying ED-4 settings in the Configuration page is **not** recommended. Doing so may result in loss of functionality of the system. Accessing the Configuration page is logged in the ED-4 internal memory.

![[00e00122.png]]

When the system enable switch is pressed, the ED-4 powers on. While powering on, the Cummins® splash screen is shown.

> [!note] Note · Примечание
> The ED-4 may take up to 15 seconds to complete the power-on sequence and establish communication with other ED-4s in the system.

![[00e00123.png]]

Once the power-on sequence completes, the data screen page will display data.

> [!note] Note · Примечание
> Dashed lines indicate data is **not** being received for the given parameter or the vessel is **not** equipped to monitor it.

The ED-4 engine and vessel data will vary with application, but typically include:

- Engine speed
- System battery voltage
- Engine coolant temperature
- Engine oil pressure
- Transmission gear oil pressure and temperature
- Rudder angle
- Percent engine load
- Engine hours
- Fuel rate
- Fuel level.

Press key 1 or “Next” to view additional data screens.

![[00e00124.png]]

The display mode of the ED-4 can be changed by pressing key 2 or “Mode” on the data screen page.

Action:

- Press key 2 or “Mode”.

The display modes are controlled by the VPF. For example, it allows the operator to change screens for single engine, twin engine, and generator set.

![[00e00124.png]]

The software and vessel personality file information of the ED-4 display can be viewed by pressing key 5 or “Menu” on the data screen page.

Action:

- Press key 5 or “Menu”
- Select “About” and press key 4 or “Enter”
- Press key 3 or “VPF” for VPF information
- Press key 4 or “Info” for software information.

Press key 5 or “Back” to exit the page.

Press key 5 or “Exit” to return to the data screen page.

![[00e00126.png]]

When an engine or vessel fault condition becomes active, an alarm pop up screen will appear on the ED-4 data screen indicating a fault is present.

The ED-4 **only** provides select alarm pop up messages on the data screen depending on the engine and vessel application against which the operator would need to take action.

The alarm pop message notification is controlled by the vessel personality file loaded in the ED-4.

> [!note] Note · Примечание
> **Only** engine or vessel fault conditions that require defined actions will display on the ED-4 data screen as an alarm pop up message.

![[00e00127.png]]

When an alarm pop up message is shown, details about each fault can be viewed by pressing the ED-4 keys.

Press key 1 or “Previous”

Press key 2 or “Next”

Press key 5 or “Close” to remove the alarm pop up message.

> [!note] Note · Примечание
> To acknowledge an alarm pop up message and silence the audible alarm, press key 5 or “Close”.

> [!note] Note · Примечание
> ED-4(s) can only acknowledge and silence alarms for the engine they are connected to. Depending on network system connections, it can be necessary to acknowledge alarms on multiple ED-4s in order to acknowledge faults from multiple engines. This can include accessing the C.I.B. ED-4(s) located in the engine room if an ED-4(s) is not installed at the helm.

![[00e00127.png]]

Typical information shown on the data screen alarm pop up message:

1. Status and number of system faults
2. Brief description of the fault and recommended action
3. Type of fault (warning or critical)
4. Source detecting the fault
5. Cummins fault code (FC) or alarm code (AC).

Typically, FCs are associated with Cummins® engine sensors, while ACs are associated with vessel sensors.

![[00e00129.png]]

Once an alarm pop up message has been acknowledged by the operator, the message will disappear.

The alarm bell lamp (1) will **not** disappear until 30 seconds after all faults go inactive.

The alarm pop up message can be brought back up on the screen for review by pressing key 4 or “Alarms”.

![[00e00130.png]]

> [!note] Note · Примечание
> The ED-4 Diagnostics page should **only** be used under the guidance of an authorized Cummins technician.

> [!note] Note · Примечание
> Do **not** enable the “Demo Data” or “Demo Alarm” selections in the Diagnostics page. Doing so will cause false data and alarm messages to be shown on the ED-4 display data screen.

![[00e00131.png]]

MFD (Multifunction Display) (Helm-Mounted):

The MFD is connected with the engine ECM through a J1939 or NMEA 2000® data link.

The MFD will indicate engine operating parameters and fault information.

The MFD is typically **not** supplied by Cummins Inc. See equipment manufacturer service information for service, setup, or software updates.

![[15d00958.png]]

ED-5 and ED-7

ED-5/ED-7 Display (Helm Mounted):

The ED-5/ED-7 display **must** be supplied by Cummins due to software compatibility.

The display is typically connected to the ECM through a SAE J1939 data link. The display will indicate engine operating parameters and fault codes. The display is the gateway for relaying engine ECM information to NMEA 2000® protocol.

The display software name and version can be found in the “About” menu screen.

The ED-5/ED-7 display comes from the factory with software and configuration installed. The ED-5/ED-7 display **must** be configured by the OEM when installed for each vessel. If the ED-5/ED-7 display is replaced during a service event, the software and configuration for each vessel **must** be installed.

Contact a Cummins® authorized repair location for ED-5/ED-7 display software updates. The ED-5/ED-7 displays use the same software package.

![[00e00284.png]]

The ED-5/ED-7 display is a touchscreen interface that provides information to the operator.

The user can interact with the display through touchscreen interface of the display or through an optional remote keypad device.

There are different symbols on the ED-5/ED-7 display interface and menu structure.

1. Menu
2. Backlight
3. Alarm
4. Back
5. Preferences
6. Security
7. Trip Information
8. Decrease
9. Increase

![[00e00285.png]]

The engine and vessel data, fault/alarm codes, diagnostics, and configuration setups can be viewed on the ED-5/ED-7 display. Reference the sections below for general ED-5/ED-7 access and setup information. Contact a Cummins® authorized repair location for setup information located in the Security page protected with a PIN. Modifying the ED-5/ED-7 Security settings in the Main Menu can result in loss of functionality of the system.

![[00e00286.png]]

When the system enable switch is pressed, the ED-5/ED-7 powers on. While powering on, the Cummins® splash screen is shown.

> [!note] Note · Примечание
> The ED-5/ED-7 can take up to 10 seconds to complete the power-on sequence and establish communication with other ED-4/ED-5/ED-7 displays in the system.

![[00e00287.png]]

Once the power-on sequence completes, the data screen page will display data.

Dashed lines indicate data is **not** being received for the given parameter or the vessel is **not** equipped to monitor the parameter data.

The ED-5/ED-7 engine and vessel data will vary with application, but typically include:

- Engine speed
- System battery voltage
- Engine coolant temperature
- Engine oil pressure
- Engine boost pressure
- Intake Manifold temperature
- Transmission gear oil pressure and temperature
- Rudder angle
- Percent engine load
- Engine hours
- Fuel rate
- Fuel level

Swipe the screen left to right or right to left on the screen to view additional data screens.

![[00e00288.png]]

The software and configuration information of the ED-5/ED-7 display can be viewed by touch and hold in the center of the screen or press on the “Menu” (I) on the data screen page.

Action:

- Touch and hold in the center of the screen or press the “Menu” (I).
- Select “About” for software information
- Select “Config” for configuration information.

Swipe the screen left to right or use the “Back” (IV) soft key on the screen to exit the page.

![[00e00289.png]]

When an engine or vessel fault condition becomes active, an alarm pop up screen will appear on the ED-5/ED-7 data screen indicating a fault is present.

**Only** engine or vessel fault conditions that require defined actions will display on the ED-5/ED-7 data screen as an alarm pop up message.

![[00e00290.png]]

When an alarm pop up message is shown and more than one fault code is active, details about each fault can be viewed by swiping the screen left to right.

- Press “Prev”
- Press “Next”

Swipe on the screen left to right or use the “Back”(IV) soft key on the screen to exit the alarm pop up message.

To acknowledge an alarm pop up message and silence the audible alarm, Swipe left to right or use the “Back”(IV) soft key or return button on remote keypad to exit the alarm pop up message.

ED-5/ED-7 displays can only acknowledge and silence alarms for the engine to which they are connected. Depending on network system connections, it can be necessary to acknowledge alarms on multiple ED-5/ED-7 displays to acknowledge faults from multiple engines.

Typical information shown on the data screen alarm pop up message:

1. Status and number of system faults
2. Brief description of the fault and recommended action
3. Type of fault (warning or critical)
4. Source detecting the fault
5. Cummins® fault code (FC) or alarm code (AC).

Typically, fault codes are associated with Cummins® engine sensors, while ACs are associated with vessel sensors.

![[00e00291.png]]

Once an alarm pop up message has been acknowledged by the operator, the pop up message is closed and can be brought back up on screen by pressing the “Alarm”(III) soft key on the screen. The ED-5/ED-7 Diagnostics page should **only** be used under the guidance of a Cummins®-authorized service provider. Enabling the “Demo Data” selections in the Diagnostics page will cause false data and alarm messages to be shown on the ED-5/ED-7 display data screen. The Advanced alarm screen shows additional details related to the active fault code – J1939 SPN, J1939 FMI, Cummins® Fault Code, source of fault code, manufacturer identification, engine hours, occurrence count. Time since alarm is the time elapsed since the fault code became active and is counted locally on the display and will update at every instance of display restart.

![[00e00292.png]]

### Setup

PS102

The brightness of the ED-4 display can be changed by pressing key 3 or “Light” on the data screen page.

Action:

- Press key 3 or “Light”
- Press key 1 or “Dimmer”
- Press key 2 or “Brighter”.

The percent brightness of the display is shown above key 3 and ranges from 10 to 100%.

Press key 5 or “Back” to save the setting and exit the brightness setting.

![[00e00132.png]]

PS103

The brightness of the ED-4 display can be changed by pressing key 3 or “Function” on the data screen page.

#### Action:

- Press key 3 or “Function”
- Press key 3 or “Dimmer”
- Press key 4 or “Brighter”.

The percent brightness of the display is shown in the Brightness row and ranges from 10 to 100%.

Press key 5 or “Exit” to save the setting and exit the brightness setting.

![[15e00190.png]]

If equipped, the trip reset of the ED-4 can be changed by pressing key 3 or “Function” on the data screen page.

#### Action:

- Press key 3 or “Function”
- Press key 2 or “Down”
- Press key 4 or “Choose”
- Press key 4 or “Send”.

If feature is available, pressing “send” will reset the trip information. A warning message will appear after pressing “Send” to notify that the trip reset message was sent.

Press key 5 or “Back” to save the setting and exit the trip reset setting.

![[15e00191.png]]

The fluid tank profile can be changed by pressing key 5 or “Menu” on the data screen page.

#### Action:

- Press key 5 or “Menu”
- Select “Configuration” and press key 4 or “Enter”
- Press key 1 or “Accept”
- Select “Device and press key 4 or “Enter” (NOTE: Device could be any of Starboard, Port, Starboard-Outer, Port-Inner)
- Select “Tank Profile” and press key 4 or “Enter”
- Select appropriate fluid to be configured
- Press key 4 or “Setup”
- Press key 4 or “Start”.

The fuel, engine oil, coolant, fresh water, wastewater and black water tanks can be configured with the ED-4, if vessel permits.

A message will appear on the ED-4 display which will ask to confirm tank is empty before proceeding configuration.

![[00e00176.png]]

The fluid tank profile can be changed by pressing key 5 or “Menu” on the data screen page, if configured tank levels are known at 25%, 50% & 75% of tank capacity. The fuel, engine oil, coolant, fresh water, wastewater and black water tanks can be configured with the ED4, if vessel permits and VPF supports the input for configuration.

#### Action:

- Press key 5 or “Menu”
- Select “Configuration” and press key 4 or “Enter”
- Press key 1 or “Accept”
- Select “Device” and press key 4 or “Enter” (NOTE: Device could be any of Starboard, Port, Starboard-Outer, Port-Inner)
- Select “Tank Profile” and press key 4 or “Enter”
- Select fluid type to be configured
- Press key 4 or “Setup”
- Press key 2 or “Down”
- Press key 4 or “Start”
- Select “Tank Volume”
- Press key 4 or “Inc” and key 3 or “Dec” to enter “Tank Volume”
- Press key 2 or “Down”
- Press key 4 or “Inc” and key 3 or “Dec” to enter 25% tank level known at “Point 1”
- Press key 2 or “Down”
- Press key 4 or “Inc” and key 3 or “Dec” to enter 50% tank level known at “Point 2”
- Press key 2 or “Down”
- Press key 4 or “Inc” and key 3 or “Dec” to enter 75% tank level known at “Point 3”

The Main Menu page of the ED-4 display can be accessed by pressing key 5 or “Menu” on the data screen page.

#### Action:

- Press key 5 or “Menu”.

Press key 5 or “Exit” to return to the data screen page.

![[00e00133.png]]

The language of the ED-4 display can be changed by pressing key 5 or “Menu” on the data screen page.

Action:

- Press key 5 or “Menu”
- Select “Language” and press key 4 or “Change”
- Select the preferred language and press key 4 or “Enter”.

Press key 5 or “Back” to save the setting and exit the page.

Press key 5 or “Exit” to return to the data screen page.

![[00e00134.png]]

The units of the ED-4 display can be changed by pressing key 5 or “Menu” on the data screen page.

Action:

- Press key 5 or “Menu”
- Select “Units” and press key 4 or “Enter”
- Select each parameter and press key 4 or “Change” to view the desired units.

Press key 5 or “Back” to save the setting and exit the page.

Press key 5 or “Exit” to return to the data screen page.

![[00e00135.png]]

The key tone of the ED-4 display can be changed to ON or OFF by pressing key 5 or “Menu” on the data screen page.

Action:

- Press key 5 or “Menu”
- Select “Key Tone” and press key 4 or “Change”.

Press key 5 or “Exit” to save the setting and exit the page.

![[00e00136.png]]

Contact a Cummins distributor for setup information located in the Configuration® page.

> [!note] Note · Примечание
> Modifying ED-4 settings in the Configuration page is **not** recommended. Doing so may result in loss of functionality of the C Command system. Accessing the Configuration page is logged in the ED-4 internal memory.

![[00e00137.png]]

PS108

The brightness menu of the ED-5/ED-7 display can be changed by pressing “Backlight”(II)” on the data screen page or touch and hold in the center of the screen or by pressing the “Menu”(I) on the data screen page.

Action:

- Access “Menu”(I)
- Select “Preferences”(V)
- In the “Backlight” option, select “Increase”(IX) or “Decrease”(VIII) backlight of the display from range 10 to 100.

Swipe left to right on screen or use the “Back”(IV) soft key to exit and save the setting. The setting once saved gets shared with other ED-7/ED-5 and ED-4s displays on the network. See additional graphics below of the preferences menu and backlight setting.

![[00e00294.png]]

![[00e00295.png]]

Preferences Menu

![[00e00293.png]]

Setting Backlight Option in Preferences Menu

The trip information of the ED-5/ED-7 is shown in the “Trip Information” on the menu screen page.

Action:

- Touch and hold in the center of the data screen or Press “Menu”(I) on the data screen page.
- Press “Trip Information”(VII) in the menu page.

![[00e00296.png]]

Pressing “Trip Information Reset” will reset the trip information. A warning message will appear after pressing “Trip Information Reset” to notify that the trip reset message was sent.

Swipe left to right or use “Back”(IV) soft key on the screen to exit the trip reset setting.

![[00e00297.png]]

The language of the ED-5/ED-7 display can be changed by “Language” option in the “Preferences”(V)) option in the “Menu”(I).

Action:

- Touch and hold in the center of the data screen or Press “Menu”(I) icon on the data screen page.
- Select “Preferences”(V)”.
- Select “Language”.
- Select the preferred language.

Swipe left to right to save or use ”Back”(IV) soft key on the screen to exit the language setting. See additional graphics below listing all available language options.

![[00e00298.png]]

![[00e00299.png]]

Language Selection

The units of the ED-5/ED-7 display can be changed by “Units” option in the “Preferences”(V) option in the “Menu”.

Action:

- Touch and hold in the center of the data screen or Press “Menu”(I) icon on the data screen page.
- Select “Preferences”(V).
- Select “Units”.
- Select the desired units for each parameter unit family to change or option to change between US and Metric unit family.

Swipe left to right or use ”Back”(IV) soft key on the screen to save and exit the Units setting. See additional graphics below listing all available units for each parameter family.

![[00e00300.png]]

![[00e00301.png]]

Units Selection

The key tone of the ED-5/ED-7 display can be changed to “Bleep” option in the “Preferences”(V) option in the “Menu”.

Action:

- Touch and hold in the center of the data screen or Press “Menu”(I) icon on the data screen page.
- Select “Preferences”(V).
- Select “Bleep” or the value to change.

Swipe on the screen left to right or use “Back“(IV) soft key to save and exit the bleep setting. See additional graphics below for bleep tone selection in the Preferences Menu.

![[00e00302.png]]

![[00e00303.png]]

Bleep Tone Selection in Preferences Menu

The ED-5/ED-7 display provides PIN protection with a 4-digit number that prevents someone unauthorized to change advanced configuration of the display. The PIN protection can be accessed from “Menu”(I) on the data screen page. The default security level is “User” level with limited capability, for advanced level user needs to access “Diagnostic” level with factory saved PIN.

The default security PIN to access advanced settings is “1919”. Sharing the default security PIN without proper knowledge may lead to unintended changes causing loss or erratic function.

Action:

- Touch and hold in the center of the data screen or press icon on the data screen page.
- Select “Security”(VI) icon.
- Select “Change Level”.
- Select “Diagnostic”.
- Enter the PIN using the number pad provided on the display screen.
- Select “OK”.

Swipe left to right or use “Back”(IV) soft key on the screen to save, exit the security menu and access the diagnostic menu. See additional graphics below for Security menu selections and security pin entry.

![[00e00304.png]]

![[00e00305.png]]

Change Level Selection in Security Menu

![[00e00306.png]]

Diagnostic Selection in Security Menu

![[00e00307.png]]

Security Pin Entry

The application configuration or theme of the ED-5/ED-7 display can be changed by accessing “Themes” from the PIN protected option in the security menu.

User **must** know the valid PIN to access the Diagnostic security level.

Action:

- Touch and hold in the center of the data screen or Press “Menu”(I) icon on the data screen page.
- Select “Security”(VI).
- Select “Change Level”.
- Select “Diagnostic”.
- Enter the PIN using the number pad provided on the display screen.
- Select “OK”.
- Swipe left to right to exit the PIN protection screen.
- Select “Setup”.
- Select “Themes”.
- Select “Theme”.
- Choose theme based on vessel application.

Swipe left to right or use the “Back”(IV) soft key on the screen to save, exit the security menu and access the diagnostic menu.

The supported ED-5/ED-7 display themes compatible with vessel application configuration can be accessed from Cummins QuickServe® Online Marine Panel Firmware Updates. See additional graphics below for Themes menu selections.

![[00e00308.png]]

![[00e00309.png]]

Themes in Setup Menu

![[00e00310.png]]

Theme Selection in Theme Manager Menu

![[00e00311.png]]

Available Themes
