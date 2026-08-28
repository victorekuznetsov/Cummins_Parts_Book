---
aliases:
  - "Инструкции по эксплуатации — обзор"
type: "Процедура"
doc: "300-101-999"
title_en: "Operating Instructions - Overview"
title_ru: "Инструкции по эксплуатации — обзор"
modified: "2025-05-15"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4332828"
  - "4332829"
figures: 110
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-101-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-101-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
---

# Operating Instructions - Overview
**Инструкции по эксплуатации — обзор**

> [!abstract] Процедура · `300-101-999`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]], [[4332829 — Marine C Command HD Elite Panel System Owners Manual|4332829]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2025-05-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-101-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-101-999.pdf)

### General Information

The C Command HD Elite ™ is the premium version of the customer interface box (C.I.B.)

- The C.I.B. is a common point for engine and vessel connections.
- The C.I.B. provides connections to the engine control module (ECM) through Deutsch™ connectors at the bottom of the C.I.B. panel.
- Communication protocols are opened through Society of Automotive Engineers (SAE) J1939 Ethernet and Modbus™ connections. This communication allows for accurate updates of engine statistics.
- No engine room panel is required because the C.I.B. functions as a local control panel.
- Supports all C Command HD™ and C Command HD Elite™ remote options.
- Full color displays on the diesel control unit 410 (E) and remote panel.
- Remote panel touch screens capable of monitoring up to eight engines.
- Capable of integrating six vessel-supplied inputs.
- The C Command HD Elite™ panel systems support feature meets Marine Society requirement for Class approvals.
- The diesel control unit 410(E) includes modules for safety and alarm system requirements.
- Includes sensors, switches, and harnesses to meet Type Approved requirements. Additional vessel inputs available to meet requirements are **not** yet supported.

The combination of these features provides a very flexible and stable platform for engine control and diagnostics.

**Customer Interface Box**

Isolators are required for the installation of the C.I.B. panel. Engine mounted panels are **not** permitted.

The C.I.B. contains the most basic functions which are required by all system configurations. Most functions in the C.I.B are performed by the C.I.B integrated diesel control unit 410(E) control panel and the C.I.B logic unit. The diesel control unit 410(E) is a microprocessor controlled unit that performs the extended functions of the C Command Elite™ panel systems. The control logic unit contains relays, diodes, resistors, switches, microcontroller, and power management capabilities.

The C.I.B is a mandatory option that is delivered with every engine, and is designed to function when connected to the vessel, whether or **not** a Cummins Inc. provided remote panel is supplied.

The C.I.B is capable of accepting power from two independent power supplies, but **only** one is required for normal operation. The second power supply is intended to be a backup for the primary power supply in the event of a primary power supply malfunction or to fulfill marine society requirements in the case of C Command HD Elite™.

A power switch relay automatically switches between the primary and secondary power supplies with any primary malfunction. In addition to the power supply switching, the C.I.B. also conditions and distributes the power received by the vessel power supply. It is capable of detecting under-voltage, over-voltage, under-current, over-current, and reverse-current for each of the vessel power inputs.

Some C.I.B. may use a redundant power selector instead of a power switch relay. The redundant power selector is a power distributor for both the primary and secondary power supply. Its purpose is to effortlessly switch between the primary and secondary power supply to provide a constant output voltage. It can communicate with the vessel operator to notify when the power supply has changed between the two sources.

> [!warning] CAUTION · Осторожно
> The C.I.B. is not protected from AC power sources. Damage can occur if AC power is applied to the C.I.B.

The primary and secondary power supplies are also isolated from each other in the circuitry of the C.I.B. This makes sure there is protection from ground faults and galvanic issues. The C.I.B power management system is designed to supply power for **only** Cummins Inc. supplied devices. Vessel connections are primary connected to the X1 terminal strip inside the C.I.B.

The C Command Elite™ panel system requires both power supplies to be connected.

The Ethernet switch is included in the C.I.B for remote panel and vessel networking connections.

Cummins Inc. supplies the sensors and connections for the C Command HD Elite™ panel system.

The C.I.B. is connected to the ECM through a main wiring harness that connects to the C.I.B. at connectors C1 and C2.

> [!note] Note · Примечание
> Power for customer-supplied devices is **not** allowed to be connected to the C.I.B vessel terminal strip.

The connections are as follows:

- ECM unswitched power
- ECM switched power
- J1939 data link
- Diagnostic lamp output
- Analog outputs (speed, pressure, and temperature)
- Speed control
- Idle control
- Remote sensors.

Diesel Control Unit

![[15400076.png]]

![[19c91599.png]]

Diesel Control Unit 410

Diesel Control Unit 410E

C.I.B. Integrated Control Panel Diesel Control Unit:

All control and monitoring can be achieved at the diesel control unit full-color display on the C.I.B. No separate engine room panel is necessary or provided. See the illustration for a close-up of the diesel control unit.

The diesel control unit communicates with the ECM via the J1939 bus to the ECM. This display allows the operator to view a selection of parameters as well as full text descriptions of ECM fault codes. The C Command™ ED-3/ED-4 (if equipped) **must** be configured as described for C Command™ parameters if connected to the C Command HD Elite™ system. Engine command and monitoring is controlled via both hard and soft keys located on the diesel control unit display.

The diesel control unit outputs all signals to the C.I.B. Ethernet switch. The Ethernet output is then routed to any remote panels that are present on the vessel. Each diesel control unit will be assigned an Engine Number (IP) for recognition on the vessel network. The configuration of this number will be requested the first time the diesel control unit is powered up. This number can also be changed from the diesel control unit main menu, if necessary. In addition, with the use of the web-based configuration interface, the diesel control unit can also be assigned a text name.

Any additional inputs from the vessel need to be configured at the diesel control unit. The diesel control unit controls what is displayed on the remote panel screens.

Shutdown Unit

![[19c91600.png]]

C.I.B. Integrated Control Panel Remote Input/Output Unit

The shutdown unit is an independent component within the C.I.B.

There are LED indicators on the unit face for status and fault codes.

Switch conditions are available on remote panels as well as on Modbus™ and data link. The reset button on the unit face acknowledges faults and enables shutdown functionality.

The safety system requirement from the marine agencies is met with the use of the shutdown unit. The shutdown unit provides secondary engine protection by shutting down the engine if any critical parameters are exceeded. With the exception of engine speed, these signals are provided to the shutdown unit as switch closures based on the exceeded condition.

The shutdown unit has five Cummins® dedicated channels for safety system shutdown use. Three additional switch inputs are provided for vessel initiated shutdowns.

The shutdown unit communicates system faults through the use of amber LEDs for individual input channels. Red LEDs are used to communicate a parameter has been exceeded and an in-process engine shutdown. A shutdown override function is available on the shutdown unit. In C Command HD Elite Marine Panel System PS107 applications, the shutdown override function is available through the Diesel Control Unit (DCU) and Engine Control Module (ECM).

This function disables all engine protections provided by the shutdown unit, with the exception of engine overspeed protection. The shutdown unit may be configured so that other protections will continue to be enabled when the shutdown override function is in use.

A reset function is included as part of the shutdown unit as well. In the event of a shutdown unit based shutdown, the shutdown unit must be reset in order to allow for engine restart. This function can be utilized by the reset button located on the shutdown face front face.

All Quantum® system engines are equipped with the same sensors/switches for the safety system. The following table is a description of the shutdown unit channels and their function.

| Shutdown Unit Descriptions |  |  |
|---|---|---|
| Quantity | Type | Description |
| 2 | Speed Sensor | Overspeed speed range for switches |
| 5 | Switch Input (normally open) | Cummins® dedicated shutdowns: coolant temperature, coolant pressure, lubricating oil pressure (low-speed range), lubricating oil pressure (high-speed range), remote engine stop |
| 3 | Switch (normally open) | Additional vessel shutdowns |
| 2 | Switch (normally open) | Shutdown override contact reset button |
| Note: Three shutdown input channels are available. |  |  |

Remote Panel

The remote panel **must** be mounted in a protected enclosure or console. The remote panel installation kit includes all hardware and seals.

The remote panel is the main engine display available on the C Command Elite™ panel systems. Alarms are displayed as on the diesel control unit 410(E) unit and include a full text description of the alarm or fault. The remote panel includes all of the functionality available at the diesel control unit 410(E) unit, including engine start and stop.

Remote panel features:

- Automatically scans for connected engines (diesel control units)
- Up to eight diesel control units may be connected to one remote panel via Ethernet network
- Displays engine parameters as displayed on each diesel control unit (Content dependent on diesel control unit)
- Capability to start and stop multiple engines from a single remote panel
- Capability to display alarm status for multiple engines from a single remote panel
- Displays service interval timer, as on diesel control unit
- Alarm broadcasting to the remote panel may be disabled (in the case of a manned engine room).

Like the diesel control unit, the functions of the remote panel are accessed with a combination of hard and soft keys. The difference is that the remote panel has a touch screen interface, so rather than pressing buttons below a soft option, the operator **must** press the function text directly. The hard keys function in the same manner as the diesel control unit, with **only** one difference. A Home hard key has been added to ease navigation through the touch screen pages. Also, like the diesel control unit, the remote panel **must** be assigned an IP number in order to properly be recognized by the vessel network. This unique IP number will allow for several remote panels to be installed on a vessel network without conflict. Additionally, each remote panel can be assigned a station name to more easily distinguish the location of each remote and which station is in present control. The remote panel can be used to view the status of any of the engines that it has been set up to monitor, without any interaction with other remote panels in the vessel network. To perform control functions, the remote panel **must** be in Active Station Mode.

![[15400079.png]]

The remote panel can be assigned a panel location. The panel location is selected from a list in the remote panel system configuration menu. The location will be shown in the upper right hand corner of the display to denote which location is the active station. The following are remote panel locations:

- Bridge
- Port wing station
- Starboard wing station
- Tower
- Engine control room
- Aft station
- Bow station
- Other.

### New Connection

Diesel Control Unit

![[25900001.png]]

Connectors at Bottom of C.I.B.

The C Command™ C.I.B. has the following connectors at the bottom of the cabinet:

- C1 - 47 pin Deutsch™ connector
- C2 - 31 pin Deutsch™ connector
- C51 - service connector

Connector C1 is responsible for providing engine information from the ECM. Connector C2 is responsible for providing alarm and safety sensor data.

![[15400081.png]]

Remote Panel

Connection to the remote panel must be made through the Ethernet connection so the remote can communicate with the diesel control unit.

### Setup

Diesel Control Unit

The following is an overview of the diesel control unit power wizard process.

The diesel control unit will power up in conjunction with the C.I.B. power switch. During the first power up, the diesel control unit will enter the power on wizard. The panel system operates on 24 VDC.

The setup wizard will prompt the user to input the basic data necessary to configure the diesel control unit for the engine type, engine location, and application. The wizard will also allow the operator to set a custom password to protect higher level settings to be changed.

![[15400082.png]]

1. Select a language:

1. Choose from available languages.
2. Press OK to confirm.

![[15400083.png]]

2. Choose administrator password.

1. Input default password (1234).
2. Input new password.
3. Re-enter new password for validation.
4. Press OK to confirm.

![[15400084.png]]

3. Select an IP number:

1. View default IP number for the diesel control unit.
2. Change the value to required IP for vessel network.
3. Press Save to commit the value.
4. Press Exit to go to the next step.

> [!note] Note · Примечание
> Devices can **not** have identical IP addresses in an Ethernet network.

This value becomes the engine identification number for the remote panel. A name can also be assigned to the engine with the web browser based tool.

![[15400085.png]]

4. Load Configuration

1. Highlight "Model" selection box.
2. Press Edit to change the value.
3. Use arrow soft keys to move between options.
4. Press OK to save change.
5. Press Down arrow hard key to highlight the next selection.
6. Repeat steps "a" through "d" for Heat Exchanger, Type Approved, and Engine Application.
7. Press the Load soft key to commit the configuration to the diesel control unit.
8. Press Yes to load the new configuration or press Cancel to return to the setup menu.

After configuration, the operator should return to the Home page on the diesel control unit.

![[15400086.png]]

Remote Panel

The following is an overview of the Remote Panel Power Wizard process.

The remote panel will also power up in conjunction with the C.I.B. power switch.

During the first power up, the remote panel will also enter its power on wizard.

The setup wizard will prompt the user to input the basic data necessary to configure the remote panel for the Language, Location, IP Address, and Monitored Engine(s). It will also allow the user to set a custom password to protect higher level settings to be changed.

The remote panel power on wizard is very similar to the diesel control unit power on wizard. The main difference is that most of the options for the remote panel are set by diesel control unit configuration. The information that is required for initial setup is much less than for the diesel control unit.

![[15400087.png]]

1. Select a language.

1. Choose from available languages.
2. Press OK to confirm.

![[15400088.png]]

2. Choose administrator password.

1. Input default password (1243).
2. Input new password.
3. Re-enter new password for validation.
4. Press OK to confirm.

![[15400089.png]]

3. Select an IP number.

1. View default IP number for the diesel control unit
2. Change the value to required IP for vessel network.
3. Press Save to commit the value.
4. Press Exit to go to the next step.

> [!note] Note · Примечание
> Devices can **not** have identical IP addresses in an Ethernet network.

This value becomes the engine identification number for the remote panel. A name can also be assigned to the engine with the web-browser based tool.

![[15400090.png]]

4. Select panel location name.

1. Choose from available panel names.
2. Press OK to confirm.

After configuration, the operator should return to the Home page on the diesel control unit.

![[15400091.png]]

5. Select engine(s) to monitor.

1. Available engine(s) will be listed by IP number and engine name, if set.
2. Check select box for engine(s) that remote panel is intended to monitor.
3. Press OK to confirm

> [!note] Note · Примечание
> Presently **only** single engine monitoring is available. Multiple engine monitoring is planned.

![[15400092.png]]

6. Remote panel complete.

1. Cummins Inc. remote panel information screen will be shown on the display.
2. Remote panel is ready for system commands.

After configuration, the operator should return to the Home page on the diesel control unit.

![[15400093.png]]

### Viewing Data

Diesel Control Unit

The display of the diesel control unit is divided into three functional areas:

- Main screen
- Status Bar
- Soft Key Indication.

These areas are shown in the illustration.

![[15400094.png]]

The present status of the system is represented in the top area of the screen. The Status Bar is separated into six fields. Text and graphics are used to provide at-a-glance evaluation of the system state in these fields.

1. Diesel control unit Present Status
2. Diesel control unit Service Mode
3. Diesel control unit Local/Remote Mode
4. Diesel control unit Override Shutdown Mode
5. Diesel control unit Manual/Automatic Mode
6. Diesel control unit All OK Mode.

The following tables define the possible field contents.

![[15400095.png]]

Field 1 of the status bar is used to display the present operating status of the diesel control unit. A text message will be displayed that reflects the mode of operation that the diesel control unit is performing. A list of these messages and what they represent can be found in the diesel control unit Status Messages table.

| Field 1 Diesel Control Unit Status Messages |  |
|---|---|
| Message | Comments |
| Ready | Ready for engine start |
| About to start | When automatic start in automatic mode |
| Prelube | Manual or automatic prelube |
| Cranking | Cranking attempt n if n\>1 for automatic mode |
| Awaiting run | Start request made but awaiting release |
| Awaiting next start attempt | Delay between start attempts |
| Running | Engine running |
| Delayed stop | Automatic stop signal received in automatic mode |
| Cooling | Cool down mode after delayed stop |
| Running | Lost the **only** source of run indication |
| Stopping | Stop request made |
| Stopped RPM \< 5 | RPM \< 5 |
| Blocked | Blocked from running |
| Extended stopping | Pre-programmed stop delay, 50 seconds. Engine can **not** be started in this state |
| Start disabled |  |

Fields 2 through 6 of the status bar are used to denote the diesel control unit active modes. A graphic representation of the active mode(s) will be displayed in the indicator boxes. The function of each field is described below in the Status Bar Indicators table.

| Field 2 - 6 Diesel Control Unit Status Messages |  |  |
|---|---|---|
| Field | Name | Description |
| 2 | Service | Wrench - service interval/maintenance alarm active |
| 3 | Local/remote | L - Local start only mode active |
| 4 | Shutdown/Override | SO - Shutdown override active |
| 5 | Manual/Automatic | M - Manual start/stop mode active |
| 6 | All OK | Green - No active or unacknowledged red/amber faults present |

The most comprehensive area of the display is in the Main Screen. It is responsible for representing available engine data and all menu content. The information in this area changes with the selected function. Some information can continue off of the Main Screen area. In this case, the arrow keys on the side of the diesel control unit can be used to advance the screen/cursor up or down. Additionally, while in the engine data viewing screens, there are multiple data templates that can be scrolled through with the use of the arrow keys.

![[15400094.png]]

### Page Navigation

Diesel Control Unit

This button provides access into the Main Menu of the diesel control unit. From this menu, the user can access additional information from the diesel control unit that is **not** contained in the default display screens. The user can also access troubleshooting screens and programming screens for the diesel control unit as well. The menu is separated into several levels. From each level, a specific list of sub-levels is available. The user navigates this list of levels with a combination of hard and soft key presses. A list of the available options from this menu, along with brief descriptions of their function, can be found in diesel control unit Main Menu Option Levels table.

Fields 2 through 6 of the status bar are used to denote the diesel control unit active modes. A graphical representation of the active mode(s) will be displayed in the indicator boxes. The function of each field is described below in the Status Bar Indicators table.

| Diesel Main Menu Option Levels |  |  |  |  |
|---|---|---|---|---|
| Top Level | 2nd Level | 3rd Level | 4th Level | Description |
| Screen backlight | Automatic 10 percent, 50 percent, 100 percent |  |  | In automatic, diesel control unit uses a photo sensitive feedback from the front panel |
| Language |  |  |  | Select language |
| Units |  |  |  | Select units (Metric/U.S.) Display unit |
| Counters | Dialog that display counters. Option to reset trip values. |  |  | From ECM if available; from diesel control unit if **not**. Shall include: - Total hours: minutes - Trip hours: minutes (since start) - Trip hour: minutes (resettable) - Start counter - Fuel consumption counters Option to reset the fuel consumption trip counter, originated from J1939 or calculated values. |
| Automatic/Manual |  |  |  | Displays and "M" in the diesel control status bar |
| Local/Remote |  |  |  | Displays an "L" in the diesel control unit status bar. |
| Prelube Override | Yes, No |  |  | Record all changes as events in the Log. If selecting “Yes” a dialog will appear “Are you sure you want to select Prelube Override? Yes, Cancel” When in Prelube Override, continues in state CRANKING after Prelube Activation signal. When active, will display “Prelube Override” in the LCD. When engine has been running for \>10 sec, or reached Start Failure Alarm, this shall reset back to “No” (do **not** want to stay in Prelube Override). The configuration will determine if this menu item is available or **not**. This menu option disappears if Configuration - Prelube Installed - No. |
| Start Disabled |  |  |  | Start can be disabled in the menu or from external input. While in this mode; if user presses the Start button, a dialog will inform that: "Start Disable". Dialog disappears after 2 seconds. |
| Troubleshooting | Tabular list of status for all available diesel control unit functions |  |  | Use Tab soft key to navigate status pages |
| Event Log | Displays the Event Log |  |  | Use soft keys to filter/sort events |
| Engine Service Interval | Tabular list of all programmed service events |  |  | Displays time left until programmed interval. Interval value can be programmed from Configuration option |
| Connect a PC | Displays IP address of the diesel control unit. Toggle Enabled tick box and Save to activate |  |  | Enables DHCP server in the diesel control unit to allow for communication with Service PC. |
| Version Information |  |  |  | diesel control unit 410 Firmware, Hardware, Colibri, etc.; RIO 410(E) Firmware, Hardware (x4); SDU410 Firmware, Hardware |
| Configuration | Password Dialog |  |  | If Password is set. In the event of a lost/ forgotten password, an encrypted password is shown here that can be decrypted by Cummins Inc. or Auto-Maskin. |
|  | Password Configuration |  |  |  |
|  | Load Configuration | Configuration Wizard |  | Load configuration based on wizard profile |
|  | Interface Design | Form List | Template Design Pages | Change/Add Screen Template content |
|  | Automatic Start/ Stop Config | Dialog with settings |  | Number of start attempts, etc |
|  | Language | English |  | Select the language to be used. |

Screen Backlight:

The operator in manual mode can choose the backlight illumination from 10, 50, or 100 percent settings.

In Automatic mode, the diesel control unit uses a photo sensitive feedback from the front panel.

![[15400097.png]]

Language:

The operator can view what language the diesel control unit will display.

Choices of language:

The language can be set in the diesel control unit power on wizard. Reference the setup portion of this procedure.

![[15400098.png]]

Units:

The operator can toggle between metric and U.S. values in measurements.

![[15400099.png]]

Counters:

The operator has the option to reset trip values. The screen displays a dialog that displays counters.

Values are from the ECM, if available, and from the diesel control unit if **not**. The counters include:

- Total hours: minutes
- Trip hours: minutes (since start)
- Trip hour: minutes (resettable)
- Start counter
- Fuel consumption counters.

Option to reset the fuel consumption trip counters, originated from J1939 or calculated values.

![[15400100.png]]

Automatic/Manual:

The Automatic/Manual setting is displayed in field (5) of the status bar.

The Select button will toggle between Manual and Automatic.

Local/Remote:

The Local/Remote setting is displayed in field (3) of the status bar.

The Select button will toggle between Local and Remote.

![[15400095.png]]

Prelube Override:

The operator can toggle between Yes and No.

Record all changes as events occur in the Log.

If selecting “Yes” a dialog shall appear “Are you sure you want to select Prelube Override? Yes/Cancel”

When in Prelube Override, continues in state CRANKING after Prelube Activation signal.

When active, shall display “Prelube Override” in the LCD. When engine has been running for \>10 sec, or reached Start Failure Alarm, this shall reset back to “No” (do **not** want to stay in Prelube Override).

> [!note] Note · Примечание
> The configuration shall determine if this menu item is available or **not**, if configured with no prelube installed. the menu will **not** appear.

This menu option disappears if Configuration - Prelube Installed - No.

![[15400103.png]]

Start Disabled: Start can be disabled in the menu or from an external input.

While in this mode, if the user presses the Start button, a dialog shall inform that: “Start Disabled”. The dialog disappears after 2 seconds.

![[15400104.png]]

Troubleshooting:

Displays a tabular list of status for all available diesel control unit functions.

Use the tab button to navigate through the screen displays.

The functions are:

- Troubleshooting diesel control unit
- Troubleshooting RIO \#1
- Troubleshooting RIO \#2
- Troubleshooting RIO \#3
- Troubleshooting RIO \#4.

![[15400105.png]]

The tab screens for the troubleshooting functions are:

- Supply
- Switch
- 4-20 mA
- PT100
- Com
- Output
- Input
- Run Sources
- Button Test.

The tab screens are the same for all functions.

![[15400096.png]]

Event Log:

The operator can use the soft keys to filter or sort events in this mode.

The tab screens are:

- Oldest
- Newest
- Most Severe.

![[15400106.png]]

Engine Overspeed Test:

The operator can configure the class vessel to allow for this test.

![[15400107.png]]

Engine Service Interval:

This is a tabular list of all programmed service events. It displays time left until programmed interval. The interval value can be programmed for the Configuration Menu in this procedure.

The tab screens are:

- Service 1
- Service 2
- Service 3
- Service 4.

The operator can confirm the maintenance interval by pressing the Service Done button.

If the Service Done button is pressed, the maintenance interval will advance to the next interval.

![[15400108.png]]

Connect to PC:

Displays the IP address of the diesel control unit.

Toggle Enabled tick box and Save to activate.

Enables DHCP server in diesel control unit to allow for communication with Service PC.

![[15400109.png]]

Version Information:

Displays the following information for the operator:

- Hardware Version
- Software Version
- IP Number.

Details can be displayed at anytime by pressing the Detail button. The details include:

- diesel control unit 410(E) Firmware, Hardware, Colibri, etc.
- RIO 410 Firmware, Hardware (x4)
- SDU 410 Firmware, Hardware.

![[15400110.png]]

The screen illustrates template design pages and forms list.

The operator can change user defined screens and other screens can be adjusted.

![[15400111.png]]

Configuration Menu

The following steps are for diesel control unit configuration.

This screen displays dialog for the password.

In the event of a lost or forgotten password, an encrypted password can be obtained from a Cummins® Authorized Repair Location.

This directs the operator to the Configuration Menu.

![[15400112.png]]

The operator can set which language the diesel control unit will display by using the up and down arrow keys.

The default language is English.

![[15400098.png]]

The following steps are Miscellaneous under the Configuration Menu.

The operator **must** enter a pin code before the Miscellaneous configuration parameters can be changed.

The parameters include:

- Automatic Buzzer Off
- Fuel Consumption
- Speed Relays
- Counter Source
- Start/Stop Buttons
- Network Configuration
- Factory Reset.

![[15400112.png]]

Automatic Buzzer Off:

The automatic buzzer times out after 12 hours for commissioning.

The internal (and external if configured) buzzer will sound once **only** and then turn off.

The operator can toggle between inactive and active.

![[15400114.png]]

Fuel Consumption:

Cummins Inc. recommends adjusting Calculate Fuel Consumption parameters. Fuel consumption inaccuracies can occur.

![[15400115.png]]

Speed Relays:

The operator can enable one or all four of the speed relay outputs.

- Enabled
- Engine speed level
- Update Event Log.

The settings are the same for all four relays.

![[15400116.png]]

Counter Source:

Cummins Inc. recommends this parameter to be set to J1939. The diesel control unit will be able to read input from the ECM.

Engine hours configuration lets you offset broadcast J1939 hours locally on the display.

![[15400117.png]]

Start/Stop Buttons:

The operator can toggle between Latched and Hold modes by pressing the Select button.

Hold to Start:

To start the engine, the operator **must** press and hold the start button until the engine is running. When the engine speed has reached 500 rpm, the engine run signal will become active and the starter will automatically be disengaged. If the engine speed falls below 100 rpm, the run signal will become inactive, thus allowing another start attempt. If the start button is released at any point prior to the engine running, the start process will terminate.

Latched Start:

To start the engine, the operator first **must** press the start button. Upon pressing the start button, the diesel control unit will prompt the operator with a start confirmation message “Are you sure?” The operator **must** then press the soft button labeled “Start” to begin the start sequence. The operator is also offered a “Cancel” soft button in the event the start button press was accidental.

![[15400118.png]]

Network Configuration:

Enter any value from 2 to 254 in the right-most tick box, where the right-most two digits represent the engine number.

For example: Enter 101 for engine number 1.

- Current IP - save changes
- Change IP - use Save button.

![[15400119.png]]

> [!warning] CAUTION · Осторожно
> All present configuration settings will be lost by performing a Factory Reset.

Factory Reset:

Removes the present configuration and restores the factory default settings. The diesel control unit will startup the first power sequence at the next power-up.

![[15400120.png]]

The operator can configure the diesel control unit source(s) for the speed sensor rpm by using the Select button.

- Speed Sensor Configuration
- Pickup 1 pulse/rev
- Pickup 2 pulse/rev
- Update DCU -\> SDU
- Update SDU -\> DCU.

A note will be displayed stating changes are applied to the shutdown unit directly.

![[15400121.png]]

The screen displays present values of the Engine Manufacturer/Type.

![[15400122.png]]

The operator can enable or set the prelube parameter.

The following parameters can be set:

- Oscillating on/off - check tick box
- On time
- Off time
- Pre Start
- Until Pressure Timeout
- Action Upon Timeout
- Override Allowed - check tick box.

The operator can choose how many minutes between prelube cycles when checking the tick box on the oscillating prelube. This function can also speed up the prelube at the start of the engine.

![[15400123.png]]

The operator can enable external components (i.e. RIO, SDU, etc.) through the external hardware option screen display. External hardware in use:

- RIO \#1 - if active, a tick box will appear
- RIO \#2 - if active, a tick box will appear
- RIO \#3 - if active, a tick box will appear
- RIO \#4 - if active, a tick box will appear
- SDU - if active, a tick box will appear.

The C Command Elite™ system C.I.B. will have a single RIO and SDU installed.

![[15400124.png]]

The operator can enable/setup Service Interval Messages by selecting one of four service interval tabs:

Service 1

The following parameters are the same on all four service intervals.

- Enabled - check tick box
- First Service At
- Then Service Every
- Pre-Warning Enable - check tick box
- SDU - if active, a tick box will appear.

Service 2, 3, and 4, can be set up like Service 1.

![[15400125.png]]

The operator can enable/setup I/O channel for the diesel control unit display and/or monitoring.

The I/O options menu contains the following parameters:

Engine Speed - D + R (diesel control unit and RP)

- Sensor
- Display
- Alarming
- Other
- Preview.

Switch Inputs

- Switch Inputs 1 through 8 (E = Event Log is active)4-20 mA Inputs (tab screens are the same as Engine Speed)

PT100 Inputs (PT100 1 through 4) (tab screens are the same as Engine Speed)

J1939 Inputs

- Percentage Load - D + R (diesel control unit and RP)
- Air Filter Differential
- Air Inlet Pressure
- Auxiliary Pressure
- Barometric Pressure
- Battery Voltage
- Boost Pressure.

![[15400126.png]]

The operator can use the Template Design Pages and change/add screen template content. The operator can choose the default template or create an operator defined template.

> [!note] Note · Примечание
> The display will view operator defined screens **only**.

![[15400111.png]]

Factory Reset

The operator can reset the parameters values to the factory default settings.

![[15400120.png]]

Connect to PC

The following steps are for the diesel control unit main menu connecting to a PC with website interface. The website interface for the diesel control unit will configure the remote panel parameters when the files are uploaded. The remote panel uses the diesel control unit parameters set by the operator on the Connect to PC menu.

![[15400129.png]]

Counters

A list of data the diesel control unit receives from the J1939 data link.

![[15400130.png]]

Prelube Override

This function is set by default by the manufacturer.

![[15400131.png]]

Start Disabled

![[15400132.png]]

Troubleshooting

The following parameters can be set:

- Supply
- Switch
- 4-20 mA
- PT100
- Communication
- Output
- Input
- Run Sources.

For example: The supply values are shown in the illustration.

![[15400133.png]]

Event Log

There are several parameters the operator can view from this function:•

- All Events
- Alarms **Only**
- User Interaction **Only**
- Commands **Only**
- Sequence **Only**.

![[15400134.png]]

The operator can save this file by choosing Save on the menu.

![[15400135.png]]

Engine Service Interval

![[15400136.png]]

Version Information

![[15400137.png]]

Configuration

The operator can upload the file once configured.

![[15400138.png]]

Interface Design

![[15400139.png]]

Configuration Menu

The operator can change a password from the configuration menu.

![[15400140.png]]

The operator can upload the configuration file.

![[15400141.png]]

The operator can design how the display views data by choosing a different template or creating a user template.

![[15400142.png]]

The operator can set different parameters for the Automatic Start/Stop configuration.

![[15400143.png]]

The language setting defaults to English. The operator can change the language for all channels or specific channels.

![[15400144.png]]

The following parameters can be set using the Miscellaneous menu:

- Auto Buzzer Off - The operator can toggle between Yes and No.

![[15400145.png]]

Fuel Consumption

![[15400146.png]]

Counters Source

![[15400147.png]]

Start/Stop Buttons - The operator can set the button to hold for start and stop.

![[15400148.png]]

Factory Reset

![[15400149.png]]

The operator can set the parameters on the speed sensor inputs to the shutdown unit.

![[15400150.png]]

The operator can change the engines name and view which type of engine application and manufacturer. The manufacturer **always** defaults to Cummins Inc.

The diesel control unit name is also the engine name.

![[15400151.png]]

The operator can set the parameters of the prelube start and stop.

![[15400152.png]]

The screen displays which type of hardware and which software version is being used.

![[15400154.png]]

The operator can change service intervals by choosing the submit soft button when parameters have been set.

![[15400155.png]]

The operator can change service intervals by choosing the submit soft button when parameters have been set.

![[15400155.png]]

The I/O configuration consists of the following parameters:

- Engine Speed Inputs
- Switch Inputs
- 4-20 mA Inputs
- PT100 Inputs
- J1939 Inputs
- Differential Inputs
- 24 VDC Input and Outputs
- Special Input (used by original equipment manufacturer (OEM))
- On-Panel Relay Outputs
- Off-Panel Relay Outputs
- Remote I/O Unit (Speed Relays).

**Only** a few of the parameters are shown in the following illustrations. All parameter choices remain the same.

![[15400156.png]]

4-20 mA Inputs

![[15400157.png]]

24 VDC Inputs or Outputs - The operator can set up to four 24 VDC outputs.

![[15400158.png]]

Remote Panel

The remote panel main menu consists of the following functions:

- Active Station
- Backlight
- Units
- Wallpaper
- Language
- Calibrate Touch Screen
- System Configuration
- Information
- Troubleshooting.

![[15400159.png]]

Active Station:

The operator can view which station is active or inactive by looking in the upper right hand corner of the remote panel display. The operator can request this station to be Active.

![[15400160.png]]

Backlight:

The operator can adjust the intensity of the backlight.

This process is the same as for the diesel control unit.

![[15400161.png]]

Units:

The operator can toggle between metric and U.S. measurement values.

![[15400162.png]]

Language:

The language setting defaults to English.

![[15400163.png]]

Wallpaper:

The operator can choose one of three wallpapers for the display.

![[15400164.png]]

Calibration Touch Screen:

The operator can calibrate the touch screen by touching the tick boxes on the screen. The tick boxes are located in each corner and the center of the display.

![[15400165.png]]

System Configuration:

For the operator to change the system configuration, a password **must** be entered (default 1234). If the password is lost or forgotten, contact a Cummins® Authorized Repair Location to regain access. The following parameters can be adjusted:

- Password
- Priority Selection
- Alarms
- Acknowledgement of Alarms
- Confirmation Timeout Behavior
- Panel Location
- Date and Time
- IP Address
- Diesel Control Unit Connections
- Factory Reset.

![[15400166.png]]

Priority Selection

The operator can give a brief description of each 1, 2, or 3.

Active station priority capabilities are described on the selection screen.

![[15400167.png]]

Alarms

The operator can disable all of the alarms at this active station Yes \[No\]. Selecting Yes inhibits all alarms on this station.

![[15400168.png]]

Acknowledgement of Alarms

Alarms can **not** be silenced or acknowledged on the remote panel, but **must** be silenced and acknowledged on the diesel control unit at the engine.

![[15400169.png]]

Confirmation Timeout Behavior

The operator can set the timeout from 10 to 255 seconds \[10\]. The default is hand over control upon timeout. The operator can deny transfer upon timeout.

![[15400170.png]]

Panel Location

This station can be named the following:

- Bridge
- Port Wing Station
- Starboard Wing Station
- Tower
- Engine Control Room
- Engine Room
- Aft Station
- Bow Station
- Other.

![[15400171.png]]

IP Address

The operator can change the IP address of the remote panel in the network.

![[15400172.png]]

diesel control unit Connections

This screen is dialog that displays scan process and results. List available diesel control unit C.I.B. panels in the network, and select (check the tick box) for each. The default setting for this parameter is “none are ignored”. Specific diesel control units in the network can be ignored.

![[15400173.png]]

Version Information:

The version information can be displayed by the operator.

![[15400174.png]]

Troubleshooting:

The operator can use the Troubleshooting from the main menu to view different parameters of the engine.

The tab screens consist are:

- Supply
- Switch
- 4-20 mA
- PT100
- Communication
- Output
- Input
- Run Sources
- Button Test.

![[15400176.png]]

Supply:

This screen displays the power source to the remote panel.

![[15400177.png]]

Switch:

This screen displays the eight switch inputs to the shutdown unit. These switches are normally open.

![[15400178.png]]

4-20 mA:

The 4-20 mA circuits are typically for pressure sensors. This screen displays each one of the 4-20 mA circuits and whether they are in use or **not** in use.

![[15400179.png]]

PT100:

The PT100 circuits are typically for temperature sensors. This screen displays the status of each circuit.

![[15400180.png]]

Com:

This screen displays the communication link between the shutdown unit and multiple RIO circuits to the remote panel display.

![[15400181.png]]

Output:

This screen displays the Inactive or Active status of each output circuit.

![[15400182.png]]

Input:

This screen displays the Inactive or Active status of each input circuit.

![[15400183.png]]

Run Sources:

This screen displays the status on each source circuit and whether or **not** the function has been configured **.**

![[15400184.png]]

Button Test:

This screen displays the status of each one of the buttons.

![[15400185.png]]
