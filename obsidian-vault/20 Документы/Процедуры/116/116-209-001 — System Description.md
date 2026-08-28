---
aliases:
  - "Описание системы"
type: "Процедура"
doc: "116-209-001"
title_en: "System Description"
title_ru: "Описание системы"
modified: "2007-03-02"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
  - "4021618"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-209-001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-209-001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# System Description
**Описание системы**

> [!abstract] Процедура · `116-209-001`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]], [[4021618 — C Command Elite and C Command Elite Plus Panel System Marine Owners Manual|4021618]]
> **Секции:** Section E - Engine and System Identification · Section F - Familiarization
> **Даты:** изменён 2007-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-209-001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-209-001.pdf)

### General Information

- The Marine C Command Elite panel system is used to monitor engine operating characteristics and control local and remote start and stop functions.
- The Marine C Command Elite panel system incorporates all of the functions of the Marine C Command panel system, including customer interface box logic unit and several additional functions.
- This system receives engine data information and has the ability to receive SAE J1939 datalink information from the ECM. The Marine C Command Elite panel system is comprised of the following panels:
- Customer interface box with Diesel Control Unit
- Remote panel.

Customer Interface Box

The customer interface box is located in the engine room and receives engine data from the ECM through 16-pin, 23-pin, and 31-pin connectors. The engine receives start, stop, and engine stop commands through the customer interface box.

The customer interface box contains the following components in it:

- Customer interface box logic unit - Provides signal processing for the panel system.
- Diesel Control Unit - Provides engine control and monitoring.
- Circuit breakers - Prevents system over current draw.
- Terminal strips - Provides connection points for wires.
- Engine stop button - Allows direct engine stop from the customer interface box.

Logic Unit

The customer interface box has a logic unit labeled CLU. The customer interface box logic unit is located inside the customer interface box and controls the functions of the Marine C Command Elite panel system. This unit has the listed lamps. Except where noted, all lamps have associated relays that allow the connection of external components as determined by the OEM.

- Supply 1 lamp (K1) - Indicates voltage is present for supply 1 circuit. No customer connection.
- Supply 2 lamp (K2) - Indicates voltage is present for supply 2 circuit. No customer connection.
- Engine stop lamp (K3) - Indicates that the direct engine stop function has been initiated.
- Local mode lamp (K4) - Indicates panel system is in local mode.
- Red lamp (K5) - Indicates engine shutdown or ECM has generated a severe fault code.
- Amber lamp (K6) - Indicates when ECM has generated a fault code that will **not** shut down the engine.
- Buzzer lamp (K7) - Indicates an alarm condition is present. Can be used to activate external horn. No customer connection.
- White lamp (K8) - Indicate maintenance fault code is present.
- Running lamp (K9) - Indicates engine is running.
- 85% of rated lamp (K10) - Indicates the engine is running at 85 percent of rate rpm.

The customer interface box logic unit has a status area that has lamps that are listed below.

- Crank lamp - **Not** used in the Marine C Command Elite panel system. The Diesel Control Unit controls engine start.

- Stop lamp - Indicates a stop command is being sent to the ECM.
- Data save lamp - Indicates a data save command is being sent to the ECM.

The customer interface box logic unit has a diagnostic area with the listed lamps and switches.

- Diagnostic ON/OFF switch - Used to place the customer interface box logic unit and the ECM in diagnostic mode. Diagnostic mode can **only** be entered when the engine is stopped.
- Diagnostic ON lamp (green) - Solid ON indicates the customer interface box logic unit is in diagnostic mode (Diagnostic ON/OFF switch is ON and engine is stopped). Flashing lamp indicates the Diagnostic ON/OFF switch is ON but the engine is **not** stopped, so the customer interface box logic unit can **not** enter diagnostic mode.
- Increment/Decrement switch - Used to select the next fault code for the unit to flash out. **Only** operational in diagnostic mode.
- Red lamp - Flashes out ECM fault codes. **Only** operational in diagnostic mode.
- Amber lamp - Flashes to indicate the start of a new ECM fault code. **Only** operational in diagnostic mode.

The customer interface box logic unit has a set of three DIP switches that are used to set engine designations on multi-engine applications. These are intended to be one-time set at commissioning and are located under a cover on the front of the customer interface box logic unit.

- The Marine C Command Elite panel system is equipped with the ability to override an engine protection shutdown command from the ECM. If the engine protection override function is desired, the OEM is responsible for the installation of the switch.
- The engine protection override terminal is located on the X4 terminal strip in the customer interface box.
- When the engine protection override switch is activated a signal is sent to the ECM, through the 31-pin connector, which allows the ECM to disregard the engine protection shutdown.
- This relay also overrides Diesel Control Unit shutdowns (if enabled).

Diesel Control Unit 410

The Diesel Control Unit 410 is an electronic unit that is able to read engine data. The data can be supplied from a SAE J1939 communication data bus, and from switches and sensors. The data is displayed on a liquid crystal display.

The Diesel Control Unit 410 has:

- Adjustable set points for warning, alarm, and shutdown
- An alarm list that displays an overview for all active alarms
- A diagnostic list that displays active diagnostic messages
- Ethernet and Modicon Communication Bus channels available for communication to third parties.

It is possible to update the Diesel Control Unit firmware using a labtop.

The Diesel Control Unit 410 operates on 24 VDC and can tolerate 24 VDC (connected in error) on all input/output points, regardless of type.

The Diesel Control Unit 410 requires two power supplies. The main purpose for two power supplies is to make sure sufficient supply voltage is present upon cranking the engine. If a secondary supply was **not** available and the primary supply voltage drop was significant, it can possibly cause the reboot of the Diesel Control Unit 410.

- 320 x 240 pixel color graphic display.
- Backlight and front panel Light Emitting Diode adjust automatically with the ambient light conditions, using a light sensor in the front panel.
- Backlight can be set to 10%, half, or full intensity from the menu.
- Any button or any event (start, stop, alarm, etc) will turn the backlight on.

| Backlight Intensity |  |
|---|---|
| Ambient Light Intensity | Backlight |
| Completely Dark | 10 percent |
| Direct Sun | 100 percent |

- Alarms Dual color, red and amber Amber will be lit on warning Red will be lit on alarm If both active, red has priority over amber. Red and amber will **not** be lit simultaneously If acknowledged red and new amber, flash amber

- Start button Green lit, solid steady when engine is running 1 Hz flashing when engine is in prelubrication 2 Hz flashing when engine is cranking

  - Stop button Red lit, solid steady when engine is stopped 1 Hz flashing when engine is in stopping, if caused by normal stop (stop button, remote stop, etc.) 2 Hz flashing when engine is stopping because of a sensor configured to make the engine shutdown (overspeed, etc).

  - Power Light Emitting Diode Green lit, solid when powered Immediately 1 Hz flashing when voltage is below set point, or one of the two supplies is missing.

| Alarms/Light Emitting Diode Functional Summary |  |
|---|---|
| Amber | Red |
| Amber ECM diagnostic fault | Red ECM diagnostic fault |
| Warning Diesel Control Unit 410 panel fault | Alarm Diesel Control Unit 410 panel fault |
| Shutdown Diesel Control Unit 410 panel fault |  |

The Diesel Control Unit 410 has a 24 VDC sleep mode input. This allows the unit to be set into a mode that resembles a unit that is turned off.

- 24 VDC = system on
- 0 VDC = sleep mode

Sleep mode is controlled by the power on/off switch on the front of the customer interface box.

- Local mode No external commands work (wire terminal commands or communication commands) **Only** local panel buttons work.

- Remote mode Local and remote commands work equally.

- Automatic mode Automatic start wire inputs work. Automatic stop wire inputs work.

- Manual mode Automatic start wire inputs will **not** work. Automatic stop wire inputs will **not** work.

When changing in between any of the four modes, a dialog will appear with the description as indicated in the table below:

| Dialog Boxes When Changing Modes |  |
|---|---|
| When Changing to: | Dialog Box |
| Local mode | External commands are disabled |
| Remote mode | External commands are enabled |
| Automatic mode | Automatic start/stop is enabled |
| Manual mode | Automatic start/stop is disabled |

- Start button Press to start engine Cranking output relay is activated Diesel Control Unit 410 will continue its start attempt until engine has started, finished the start attempt, or the user has aborted the start by pressing the stop button.

  - Prelubrication Diesel Control Unit has engine prelubrication control capabilities Prelubrication cycle = Prelubrication activation signal - Await completion - Crank If the Diesel Control Unit 410 does **not** receive activation signal within 30 seconds “Start Failed, Prelube Fault” dialog is generated on the display. While prelubrication is in progress “Prelubrication in progress” dialog in generated on the display.

    - Automatic starts = The Diesel Control Unit 410 will initiate as many start attempts; according to the configured number of start attempts in the configuration menu.

  - Stop button Press to stop a running engine or abort a start sequence. Depending on configuration, the button **must** be pushed until the engine is stopped. A stop sequence can be aborted by pressing the start button. While in stopping mode “Stop in progress - press Start to cancel” dialog is generated on the display.

  - Alarm list button When pressed, displays the active alarm list and silences panel buzzer.

  - Up arrow button When pressed, moves selection up a selectable list.

  - Down arrow button When pressed, moves selection down a selectable list.

  - Menu button When pressed, opens the Diesel Control Unit 410 menu. All functions described in this document are accessible from the menu. The menu also includes Diesel Control Unit 410 configuration and test options.

  - Buzzer and buzzer off Buzzer activates when new alarms or diagnostic messages are received by the Diesel Control Unit 410. Press the Alarm list button to silence the buzzer. If a new alarm is received while in alarm list the buzzer will activate. Pushing the alarm list, button will silence the buzzer.

  - Soft buttons Change functionality depending on the actual screen. Four buttons located along the bottom of the display. Dynamic label is linked to each button.

| Soft Button Labels in Main View |  |  |  |
|---|---|---|---|
| Backlight | Local Start **Only** /All Start | Settings | User Configuration |

- Prelubrication is necessary on engines that need to build up oil pressure prior to cranking.
- If prelubrication is activated, the Diesel Control Unit will begin a sequence when the start button is pushed. Receives start command (local, remote, or automatic). Prelubrication is activated for a fixed time or until the oil pressure is acceptable. After fixed time has elasped or oil pressure is acceptable, engine will crank. If pressure is timed out, crank to start failure or prelubrication override.

Alarm Page

The alarms appear in the order they are received. When a new alarm is received, it is shown at the top of the alarm list.

The list shows all alarms from configured switches and analog inputs. These can be from physical switches, 4-20 mA type inputs, and configured set points on the SAE J1939 datalink (ECM Broadcasted) channels.

The symbol and color denotes the severity of the alarm:

- Symbol 1 = Red severity
- Symbol 2 = Amber severity
- Symbol 3 = White severity

Bold face lettering denotes alarm acknowledgement:

- Bold = Unacknowledged
- Normal = Acknowledged

Reverse background and foreground color denotes active status:

- Colored background = Active alarm
- Colored text on gray background = Inactive alarm

- Located on the alarm page, displays alarms from diesel control unit, shutdown unit and remote input/output unit (shutdown unit and remote input/output are C Command Elite Plus components **only**).
- Red = shutdown (switch closure on shutdown unit).
- Amber = alarm (alarm sensor threshold to remote input/output unit exceeded or wire breaks for shutdown unit switch inputs).
- White = warning (out of range remote input/output malfunctions on remote input/output unit sensor inputs).

- The event log stores in a separate list the last events. An event is defined as: Any new panel alarm that appears in the alarm list Any new engine diagnostic message that appears in the alarm list When alarm or diagnostic messages go to inactive When any user interaction buttons are pressed, except for up and down arrow Any command such as remote start, stop, acknowledge, etc.

The event log can contain 500 separate events. When the log is full and a new event is logged the oldest event is removed.

The event will be time stamped.

The events are listed with the last event at the top of the screen and the older events below it.

- There are four different timers with corresponding text for service intervals. All are set to off by default.
- Intervals are enabled during initial configuration. Enabling the interval starts the timer.
- When the time until next service is 10 percent of the total interval hours, a dialog appears when entering ready mode, displaying “Next Service Due” in (10 percent of total interval hours).
- If a service is overdue, a dialog box appears displaying “Service Overdue” (amount of hours overdue).
- All service interval actions are in the event log.

- COM1 - Modicon Communication Bus Parent (shutdown unit link) Immediately starts communication when shutdown unit is corrected. **Only** used in C Command Elite Plus panel system.

  - COM2 - Modicon Communication Bus Parent (input/output expansion to remote input/output unit 410) Immediately starts communication when expansion input/output expansion is connected. **Only** used in C Command Elite Plus panel system

  - COM3 - Modicon Communication Bus Child (configuration and general communication) Communication with third party equipment to communicate with the Diesel Control Unit.

  - COM4 - J1939/Controller Area Network (ECM SAE J1939 interface) Connected to the engine ECM.

  - COM5 - Controller Area Network open (third party interface) Three wire terminals (high, low, and shield)

  - COM6 - Ethernet Modicon Communication Bus/Transmission Control Protocol (general communication and web server configuration) Primarily for Ethernet Modicon Communication Bus/Transmission Control Protocol, but can be used for limited configuration of diesel control unit.

  - COM7 - Console Universal serial bus connector for processor interface.

The Marine C Command Elite panel system and C Command Elite Plus panel systems have the following inputs supplied from the ECM.

- Torque curve select signal
- Droop select signal
- SAE J1939 supply signal
- SAE J1939 return signal
- External speed command input signal
- OEM switch signal
- Intermediate speed control 3/validate switch signal
- Intermediate speed control 2 switch signal
- Engine protection override switch signal
- Diagnostic test mode switch signal
- Alternate idle/auxiliary governor select signal
- Intermediate speed control/idle increment signal
- Intermediate speed control/idle decrement signal
- Intermediate speed control 1/remote pto signal
- Fan control switch signal
- Tachometer output signal
- Frequency accelerator signal
- Accelerator pedal or lever idle validation switch off signal
- Accelerator pedal or lever idle validation switch on signal
- Maintenance signal
- Warning signal
- Engine protection stop signal
- Fan control signal
- Multiple unit synchronization switch 2 signal
- Multiple unit synchronization switch 1 signal
- Remote accelerator pedal or lever position switch signal
- Engine oil level remote reservoir signal
- Remote accelerator pedal or lever signal
- Auxiliary input/output 3 signal
- Auxiliary PWM driver signal
- Multiple unit synchronization pin 3 switch signal
- Multiple unit synchronization pin 2 switch signal
- Multiple unit synchronization pin 1 switch signal

- SAE J1939 datalink supply signal
- SAE J1939 datalink return signal
- Fault acknowledge signal
- Idle/rated switch signal
- Engine protection override switch signal
- Diagnostic test mode switch signal
- Diagnostic increment signal
- Diagnostic decrement signal
- Alternate frequency signal
- Coolant temperature meter signal
- Tachometer output signal
- Generator speed/load governing bias signal
- Low oil pressure (LOP) shutdown signal
- Run/stop switch signal
- Over speed switch shutdown signal
- Common warning signal
- Common shutdown signal
- Engine oil remote reservoir signal
- Droop adjust potentiometer signal
- Frequency adjust signal
- Oil pressure meter signal
- Multiple unit synchronization id pin 3 switch signal
- Multiple unit synchronization id pin 2 switch signal
- Multiple unit synchronization id pin 1 switch signal
- Pre-high engine temperature warning signal
- High engine temperature (HET) shutdown signal
- Pre-low oil pressure warning signal.

The diesel control unit 410 has an input/output as a standard. The following inputs and outputs are available on the unit.

| Standard Input/Output Arrangement for Diesel Control Unit 410 |  |  |  |
|---|---|---|---|
| Type | Input or Output | Number of Channels | Description |
| Fixed Functional Inputs | Input | 10 | Fixed Input |
| Configurable Fixed Functional Inputs | Input | 2 | None |
| Switch | Input | 8 | User Configurable |
| 4-20 mA | Input | 4 | User Configurable |
| PT100 | Input | 4 | User Configurable |
| Fixed 24 VDC Source 500 mA | Output | 12 | Fixed |
| Configurable Outputs 24 VDC 500 mA | Output | 4 | User Configurable (multiple relay) |
| Configurable outputs, relays | Output | 2 | User Configurable (multiple relay) |
| Pickup (Tachometer) | Input | 1 | User Configurable |
| SAE J1939 | Input | 1 | Fixed/User configurable |
| SAE J1939 Open | Output | 1 | None |
| Ethernet (Modicon Communication Bus/Transmission Control Protocol) | Input/Output | 1 | None |

The tables below are a breakdown of the type of input/output for the Diesel Control Unit 410.

| Fixed Functional Inputs (Active on 24 VDC) |  |  |  |
|---|---|---|---|
| Channel Number | Function | Active | Description |
| 1 | Remote acknowledge | 24 VDC = acknowledge | Remote acknowledge and silence alarm |
| 2 | Automatic start (power management system) | 24 VDC = start | Initiate automatic start attempts. Works in manual mode **only**. |
| 3 | Delayed automatic stop (power management system stop) | 24 VDC = stop | Works in automatic mode **only**. If power management system start and stop are active, power management system start is given priority. |
| 4 | Remote start | 24 VDC = start | None |
| 5 | Remote stop | 24 VDC = stop | None |
| 6 | Start disabled | 24 VDC = start disabled | Fail to safe = able to start. Does **not** stop a running engine, prevents a new start. |
| 7 | Prelubrication complete | 24 VDC = complete | **Must** have 24 VDC to start the engine. |
| 8 | Gearbox neutral | 24 VDC = in gear | Fail to safe = will start even if wire breaks. Gearbox is disabled with oil pressure alarm. Engine crank is disabled when in gear. |
| 9 | Manual/Automatic Automatic = power management system control. Manual = power management system control lockout. | 24 VDC = manual Open = automatic | Fail to safe = automatic If manual is selected in the diesel control unit 410 or remote panel or at wire terminal then command is manual. |
| 10 | Shutdown override | None | None |

| Configurable Fixed Functional Inputs |  |  |
|---|---|---|
| Channel Number | Function | Description |
| 1 | Configurable | Configurable from a bank of fixed functions. |
| 2 | Configurable | Configurable from a bank of fixed functions. |

| Configurable Switch Inputs (24 VDC Inputs, Warning or Alarm) |  |  |
|---|---|---|
| Channel Number | Function | Description |
| 1 | Open | Normally closed/normally open |
| 2 | Open | Normally closed/normally open |
| 3 | Open | Normally closed/normally open |
| 4 | Open | Normally closed/normally open |
| 5 | Open | Normally closed/normally open |
| 6 | Open | Normally closed/normally open |
| 7 | Open | Normally closed/normally open |

| 4-20 mA Inputs (Two Wire Terminals per Channel) |  |
|---|---|
| Channel Number | Range |
| 1 | Configurable |
| 2 | Configurable |
| 3 | Configurable |
| 4 | Configurable |

| PT100 Inputs (Three Wire Terminals per Channel) |  |
|---|---|
| Channel Number | Range |
| 1 | Configurable |
| 2 | Configurable |
| 3 | Configurable |
| 4 | Configurable |

| Fixed Functional Outputs (24 VDC Source 500 mA) |  |  |
|---|---|---|
| Channel Number | Function | Description |
| 1 | Prelubrication activation | When configured, precedes engine crank. |
| 2 | Crank (start) | None |
| 3 | Engine running | None |
| 4 | Energize to run | None |
| 5 | Energize to stop | Also used on shutdown stop in applications that are classified. |
| 6 | Energize to shutdown | Activates for shutdowns **only**. |
| 7 | Configurable | Any function. |
| 8 | Configurable | Any function. |
| 9 | Configurable | Any function. |
| 10 | Common alarm relay (three terminals) | Inclusive common warning and common diagnostics. 24 VDC = Normal (no alarm) Normally energized. |
| 11 | Common alarm relay | Normally open. |
| 12 | Common alarm | Normally closed. |

| Configurable Function Outputs |  |
|---|---|
| Channel Number | Description |
| 1 | User configurable (multiple relay) |
| 2 | User configurable (multiple relay) |
| 3 | User configurable (multiple relay) |
| 4 | User configurable (multiple relay) |

| Configurable Function Outputs - Relay |  |
|---|---|
| Channel Number | Description |
| 1 | User configurable (multiple relay) |
| 2 | User configurable (multiple relay) |

- The Diesel Control Unit 410 will read up to three sources (speed input, pickup, and tachometer) and use one for calculation and display as follows: First priority - SAE J1939 from the ECM Second priority - Physical input in shutdown unit, via communication link Third priority - Physical input on Diesel Control Unit 410 (pickup/tachometer)

The following tables have specifications of the functional inputs/outputs, and sensor inputs available for the diesel control unit 410.

| Functional Inputs |  |
|---|---|
| Input | Description |
| Fixed functional inputs | Optocoupled switch input. 0 to 2 VDC = 0 7 to 32 VDC = 1 2 to 7 VDC = undefined Over voltage protection: 40 VDC **Not** connected = 0 VDC (used with 47k ohm resistor) |
| General switch inputs | Optocoupled switch input. 0 to 2 VDC = 0 7 to 32 VDC = 1 2 to 8 VDC = undefined Over voltage protection: 40 VDC **Not** connected = 0 VDC (used with 47k ohm resistor) To be configured for: Warning/alarms/shutdowns Delay for warnings/alarms/shutdowns Normally open or Normally closed On run **only**. |

| Sensor Inputs |  |
|---|---|
| Sensor | Description |
| 4 to 20 mA sensor | Analog input 0 to 25 mA, with a guaranteed specification for 4 to 20 mA measurements Accuracy: 0.5 percent over entire range. Over voltage protection 40 VDC **Not** connected = 0 mA Alarm for: Less than 2 mA Greater than 25 mA |
| PT100 sensor | 3-wire channels Range 0 to 800° C \[0 to 1472°F\] Accuracy: 0.5 percent over entire range. |
| Pickup/Tachometer/Speed Input | 0 to 10 kHz |
| SAE J1939 | 60 VDC transceiver Wires: Supply, Return, and Shield |

| Functional Outputs |  |
|---|---|
| Output | Description |
| 24 VDC outputs, 500 mA | **Not** active = Open (47k ohm resistor to define voltage level) Active = 24 VDC to 0 VDC Polyswitch over current protection |

- Connected to the Diesel Control Unit 410, and is remote means of controlling the Diesel Control Unit 410.
- When connected to the Diesel Control Unit, remote panel will update itself with Diesel Control Unit 410 configuration files.
- Touch screen control.

- Illuminated when supply power is OK.
- Flashing 1 Hz when power is below fixed set point.

Ambient light sensor located in top right area of panel. Ambient light sensor is for display back light.

- There are four different main screens, depending on the number of diesel control units (engines) that are connected to the engine.
- The screen is viewable in direct sunlight (8.4-inch diagonal, 640 x 480 pixel transflective screen)
- The remote panel will display as follows: Type 1 - One diesel control unit is connected to the remote panel. The entire display screen is used. Type 2 - Two diesel control units are connected to the remote panel. The display screen divided into two. Type 4 - Three or four diesel control units are connected to the remote panel. The display screen is divided into four quadrants. Type 6 - Five or six diesel control units are connected to the remote panel. The display screen is divided into six quadrants.

- Ethernet Modicon Communication Bus/Transmission control protocol for communication to the Diesel Control Units.
- The remote panel will give an alarm if communication is lost with Diesel Control Unit 410 or other remote panels. RS232 for communication to optional external vessel inputs.

- Main page Start up page and will find all Diesel Control Units and list them by engine name.

  - Engine name Part of configuration of Diesel Control Unit. Each configured Diesel Control Unit will have a unique name. If two or more names are the same in Diesel Control Unit configuration, the remote unit will add a numeric value to the end of the names.

  - Ignore engine(s) On each remote panel, it will be possible to ignore one or several Diesel Control Unit panels in the network. A Diesel Control Unit that is ignored at the remote unit will be “invisible” for that remote unit.

  - Active station **Only** one remote panel will have control when more than one remote panel is in the network. An active station can execute commands such as: start, stop, and alarm acknowledge.

  - Requesting Control When an inactive remote panel requests to be active, the active station receives a dialog box for handover.

  - Remote priorities In the configuration menu the remote unit is given a priority number as follows:

| Remote Panel Priorities |  |  |  |
|---|---|---|---|
| Priority 1 (Primary Parent Remote Panel) | Priority 2 (Secondary Parent Remote Panel) | Priority 3 (Child Remote Panel) \[Factory default setting\] | Priority 4 (Public Remote Panel) |
| Can always take command from the active panel; no question asked. Note: If the user tries to execute a command, and the panel is **not** the active station, it immediately becomes the active station and executes the command. | Can take command from active panels priority 2 or 3; no question asked. If the current active panel is priority 1, that panel **must** confirm. | Can take command from active panels priority 1, 2, or 3 after confirmation at the active panel. | Disabled |
| Will handover command to priority 1 panel immediately. Can handover command to priority 2 or 3 panels, depending upon Confirmation Time-out Behavior | Will handover command to priority 1 or 2 panels immediately. Can handover command to priority 3 panels, depending upon Confirmation Time-out Behavior. | Will handover command to priority 1 or 2 panels immediately. Can handover command to priority 3 panels, depending upon Confirmation Time-out Behavior. | Will handover command to priority 1, 2, or 3 panels immediately. |

- If the present active station suddenly loses communication in the network, the first panel that asks for control will immediately become the active station.

- The remote panel has a limited configuration requirement
- The remote panel will find Diesel Control Units available on the Ethernet network and update its configuration files.

Datalink Connectors

Cummins Inc. produces many engines today that are electronically controlled. These engines have special diagnostic requirements because of the ECM in the system. To interface with these ECMs, electronic service tools have been developed, such as INSITE™ electronic service tool. INSITE™ electronic service tool interfaces with the electronic engines by means of a datalink. A datalink provides a physical means for transmitting and sorting electronic signals. A datalink consists of special electronic circuitry and electrical harnesses. Connection points for electronic service tools are also part of the datalink. Datalinks are defined by standards written by the Society of Automotive Engineers (SAE). Cummins Inc. uses two such standards for electronic service tools. One is a combination of SAE J1587/SAE J1708 and the other is SAE J1939. Engines can support one or both of these datalink standards.

The recommended datalink connector for Cummins® engines is a 9-pin Deutsch™ connector. This connector can supply SAE J1587/SAE J1708 and SAE J1939 communications and battery voltage. The following are pin-outs for the 9-pin connector:

| Pin | Signal |
|---|---|
| A | Battery Voltage 1 Return |
| B | Battery Voltage 1 Supply |
| C | SAE J1939 Datalink Supply |
| D | SAE J1939 Datalink Return |
| E | SAE J1939 Datalink Shield |
| F | **Not** Used |
| G | **Not** Used |
| H | **Not** Used |
| J | **Not** Used |

![[19400739.png]]
