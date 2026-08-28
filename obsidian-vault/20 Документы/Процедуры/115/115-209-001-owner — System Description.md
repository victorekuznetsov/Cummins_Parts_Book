---
aliases:
  - "Описание системы"
type: "Процедура"
doc: "115-209-001-owner"
title_en: "System Description"
title_ru: "Описание системы"
modified: "2008-10-09"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
  - "41353297"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
manuals:
  - "4021589"
figures: 3
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-209-001-owner.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-209-001-owner.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "группа/115"
---

# System Description
**Описание системы**

> [!abstract] Процедура · `115-209-001-owner`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Входит в руководства:** [[4021589 — Marine C Command Panel System Owners Manual|4021589]]
> **Секции:** Section E - Engine and System Identification
> **Даты:** изменён 2008-10-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-209-001-owner.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-209-001-owner.pdf)

### General Information

The Marine C Command panel system is used to monitor basic engine operating characteristics and to control local and remote start and stop functions.

This system receives engine data information and has the ability to receive SAE J1939 data link information from the ECM. The Marine C Command panel system is comprised of the following panels:

- Customer interface box
- Engine room panel
- Remote panel.

The Marine C Command panel system can have the listed configurations:

- Customer interface box **only**
- Customer interface box and engine room panel
- Customer interface box, engine room panel, and one or more remote panels (determined by total cable length and total current draw)
- Customer interface box and one or more remote panels (determined by total cable length and total current draw).

> [!note] Note · Примечание
> If the engine room panel is **not** used, a jumper cap **must** be used at connector C7 on the customer interface box.

Customer Interface Box

The customer interface box is located in the engine room and receives engine data from the ECM through 16-pin and 31-pin connectors. The engine receives start, stop, and engine stop commands through the customer interface box.

The customer interface box contains the following components:

- Customer interface box logic unit
- Circuit breakers
- Terminal strips
- Engine stop button.

Customer interface box logic unit - Signal processing for the panel system.

Circuit breaker - Prevents system overcurrent draw.

Terminal strips - Provide connection points for wires.

Engine stop button- Allows direct engine stop from the customer interface box.

![[17800169.png]]

Customer Interface Box Configuration When Engine Room Panel is Not Used

If the panel configuration does **not** include an engine room panel, a shorting connector (1) **must** be installed at the C7 connector of the customer interface box.

Customer Interface Box

The customer interface box has a logic unit labeled CLU. The customer interface box logic unit is located inside the customer interface box and controls the functions of the Marine C Command panel system. This unit has the listed lamps. All lamps have associated relays that allow the connection of the external components, as determined by the OEM.

- Supply 1 lamp (K1)
- Supply 2 lamp (K2)
- Engine stop lamp (K3)
- Local mode lamp (K4)
- Red lamp (K5)
- Amber lamp (K6)
- Buzzer (K7)
- White lamp (K8)
- Running lamp (K9)
- 85 percent of rated lamp (K10).

Supply 1 lamp (K1) - Indicates voltage is present for supply 1 circuit.

Supply 2 lamp (K2) - Indicates voltage is present for supply 2 circuit.

Engine stop lamp (K3) - Indicates that the direct engine stop function has been initiated.

Local mode lamp (K4) - Indicates the panel system is in local mode.

Red lamp (K5) - Indicates engine shutdown or ECM has generated a severe fault code.

Amber lamp (K6) - Indicates when the ECM has generated a fault code that will **not** shut down the engine.

Buzzer (K7) - Indicates a buzzer condition is present. Can be used to activate vessel alarm horn.

White lamp (K8) - Indicates a maintenance fault code is present.

Running lamp (K9) - Indicates the engine is running.

85 percent of rated lamp (K10) - Indicates the engine is running at 85 percent of rated rpm.

The customer interface box logic unit has a status area that has lamps that are listed below:

- Crank lamp
- Stop lamp
- Data save lamp.

Crank lamp - Indicates a start command is being sent to the starter.

Stop lamp - Indicates a stop command is being sent to the ECM.

Data save lamp - Indicates a data save command is being sent to the ECM.

The customer interface box logic unit has a diagnostic area with the listed lamps and switches.

- Diagnostic ON/OFF switch
- Diagnostic ON lamp (green)
- Increment/Decrement switch
- Red lamp
- Amber lamp.

Diagnostic ON/OFF switch - Used to place the customer interface box logic unit and the ECM in the diagnostic mode. Diagnostic mode can **only** be entered when the engine is stopped.

Diagnostic ON lamp (green) - Solid ON indicates the customer interface box logic unit is in diagnostic mode (Diagnostic ON/OFF switch is ON and engine is stopped). Flashing lamp indicates the Diagnostic ON/OFF switch is ON, but the engine is **not** stopped; so the customer interface box logic unit can **not** enter diagnostic mode.

Increment/Decrement switch - Used to select next fault code for unit to flash out. **Only** operational in diagnostic mode.

Red lamp - Flashes out ECM fault codes. **Only** operational in diagnostic mode.

Amber lamp - Flashes to indicate the start of a new ECM fault code. **Only** operational in diagnostic mode.

The customer interface box logic unit has a set of DIP switches that are used to set engine designations on multi-engine applications. These are intended to be one-time set at commissioning and are located under a cover on the front of the customer interface box logic unit. The DIP switches are **not** used on the C Command panel system at this time.

Engine Protection Shutdown Manual Override

The Marine C Command panel system is equipped with the ability to override an engine protection shutdown command from the ECM. If the engine protection override function is desired, the OEM is responsible for the installation of the switch.

The engine protection override terminal is located on the X4 terminal strip in the customer interface box.

When the engine protection override switch is activated, a signal is sent to the ECM through the 31-pin connector, which allows the ECM to disregard the engine protection shutdown.

Engine Room Panel

The engine room panel is located in the engine room and is used to monitor and control the operation of the engine. This panel is equipped with an ED3 digital display. In addition, the engine room panel is equipped with buttons and lamps.

- Power switch/lamp (white)
- Local start **only** button
- Engine alarm lamp (red)
- Buzzer
- Start button
- Local start **only** lamp (yellow)
- Stop button
- Silence button.

Power switch/lamp (white) - Turns on ECM, engine room panel, and remote panel.

Local start **only** button - When button is depressed, allows start function **ONLY** from engine room panel.

Engine alarm lamp (red) - When illuminated, indicates a fault condition is present.

Buzzer - Supplies an audible fault indication.

Start button - Starts the engine.

Local start only lamp (yellow) - When illuminated, indicates the engine can **only** be started from the engine room panel.

Stop button - Stops the engine.

Silence button - Silences the buzzer when an alarm condition has been generated.

The ED3 is connected with the ECM through a SAE J1939 data link. The ED3 will indicate engine operating parameters and fault codes.

The remote panel is located per OEM specifications and is used to monitor and control the operation of the engine. This panel can be equipped with a gauge set or ED3 digital display. It is also equipped with buttons and lamps.

- Power lamp (white)
- Local start only lamp (amber)
- Engine alarm lamp (red)
- Buzzer
- Start button
- Stop button
- Silence button.

Power lamp (white) - When illuminated, indicates the remote panel has power supplied.

Local start only lamp (amber) - When illuminated, indicates the engine can **not** be started from the remote panel.

Engine alarm lamp (red) - When illuminated, indicates a fault condition is present.

Buzzer - Supplies an audible fault indication.

Start button - Allows engine start when the local start **only** lamp is **not** illuminated.

Stop button - Stops the engine.

Silence button - Silences the buzzer when an alarm condition has been generated.

ECM Supplied Signals

The Marine C Command panel system is supplied signals from the engine ECM.

- Engine oil level remote reservoir signal
- Coolant level 1 signal (keel or heat exchanger cooled)
- Remote accelerator pedal or lever position signal
- Accelerator pedal or lever position signal
- Accelerator pedal or lever idle validation switch off signal
- Accelerator pedal or lever idle validation switch on signal
- OEM switch signal
- Engine protection stop lamp signal
- Warning lamp signal
- Maintenance lamp signal
- Spare ratiometric input 1 signal
- Tachometer signal
- Diagnostic test mode signal
- Intermediate speed control/idle increment signal
- Intermediate speed control/idle decrement signal
- Intermediate speed control 1/remote PTO signal
- Intermediate speed/control 3/validate switch signal
- Engine protection override signal
- SAE J1939 data link supply signal
- SAE J1939 data link return signal.

- Engine oil level remote reservoir signal
- Coolant level 1 signal (keel or heat exchanger cooled)
- Droop adjust potentiometer signal
- Generator speed/load governing bias signal
- Run/stop switch signal
- Fault acknowledge signal
- Common shutdown lamp signal
- Common warning lamp signal
- Over speed shutdown lamp signal
- Diagnostic test mode signal
- Diagnostic increment signal
- Diagnostic decrement signal
- Alternate frequency switch signal
- Idle/rated switch signal
- Tachometer signal
- Engine protection override signal
- SAE J1939 data link supply signal
- SAE J1939 data link return signal
- Generator output frequency adjust potentiometer signal.

Datalink Connectors

Cummins Inc. produces many engines today that are electronically controlled. These engines have special diagnostic requirements because of the ECM in the system. To interface with these ECMs, electronic service tools have been developed, such as INSITE™ electronic service tool. INSITE™ electronic service tool interfaces with the electronic engines by means of a data link. A data link provides a physical means for transmitting and sorting electronic signals. A data link consists of special electronic circuitry and electrical harnesses. Connection points for electronic service tools are also part of the data link. Data links are defined by standards written by the Society of Automotive Engineers (SAE). Cummins Inc. uses two such standards for electronic service tools. One is a combination of SAE J1587/SAE J1708 and the other is SAE J1939. Engines can support one or both of these data link standards.

The recommended data link connector for Cummins® engines is a 9-pin Deutsch™ connector. This connector can supply SAE J1587/SAE J1708 and SAE J1939 communications and battery voltage. The following are pin-outs for the 9-pin connector:

| Pin | Signal |
|---|---|
| A | Battery Voltage 1 Return |
| B | Battery Voltage 1 Supply |
| C | SAE J1939 Data Link Supply |
| D | SAE J1939 Data Link Return |
| E | SAE J1939 Data Link Shield |
| F | **Not** Used |
| G | **Not** Used |
| H | **Not** Used |
| J | **Not** Used |

![[19400739.png]]

Switch Panel

![[15400069.png]]

Optional Switch Panel (Front View)

1. Shutdown override switch
2. Alternate idle switch
3. Intermediate speed control switch
4. RPM increment/decrement switch.

> [!note] Note · Примечание
> The switch panel is an optional control panel that provides easy activation of certain engine control features. It includes the above switches.
