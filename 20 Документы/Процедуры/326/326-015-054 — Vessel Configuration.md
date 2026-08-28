---
type: "Процедура"
doc: "326-015-054"
title_en: "Vessel Configuration"
modified: "2024-06-25"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4358378"
figures: 39
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-054.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-054.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/326"
---

# Vessel Configuration

> [!abstract] Процедура · `326-015-054`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4358378 — Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick Marine Con|4358378]]
> **Секции:** Section 15 - Instruments and Controls
> **Даты:** изменён 2024-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-054.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-054.pdf)

### General Information

There are two different versions of lever control stations and inboard joysticks. The legacy lever control station version is all of 3 and older and the existing version is 4 and greater. The legacy inboard joystick version is all versions 2 and older and the existing version is 3 and greater. Version 3 and greater inboard joysticks and version 4 and greater lever control stations will come pre-configured from factory with Handle ID number 1. Versions 3 and older lever control station and all versions 2 and older inboard joystick have a unique handle identifier on the controller area network to distinguish each device. Existing and legacy joysticks and lever control stations are backward compatible.

**With Version 2 and older Inboard Joystick and Version 3 and older Lever Control Station**

In order for each lever control station and inboard joystick to communicate with the throttle control processor module, each device must have a unique handle identifier. If a complete system was purchased from the factory, configuration was performed by the factory. Inboard joysticks also have associated handle identification number and joystick type settings.

If a lever control station or inboard joystick was purchased separately, it will be preconfigured at the factory with a handle identifier. If two devices with the same handle identifier are installed, the system will enter alarm mode and the alarm code will be stored. One of the devices will have to be configured with a new handle identifier to resolve the issue.

If two devices have the same handle identifier, all lights on the button pad will blink immediately after the system enable switch is turned on.

**With Version 3 and greater Inboard Joystick or Version 4 and greater Lever Control Station**

Version 4 and greater lever control station and version 3 and greater inboard joystick come preconfigured from factory with handle identifier number 1.

There are four scenarios in which the lever control station and inboard joystick can be configured. The following are example situations:

![[15e00181.png]]

Inboard joystick identifier number 3 is replaced with an inboard joystick with version 3 and greater software. The new inboard joystick will need to be changed from factory setting of ID number 1 to a unique handle identifier.

#### Scenario Number 1: Inboard joystick with legacy software Version 2 and older is replaced with unit equipped with existing software version 3 or higher.

- Inboard joystick (handle identifier number 3) version 3 and greater software includes the capability for backward compatibility with legacy software Version 2 and older.
- Default handle identifier for inboard joysticks and lever control stations with new software is handle identifier number 1. New/replacement joystick with version 3 and greater will have to set a unique handle identifier before it can be used. Failure to do this will cause an immediate alarm when control system is activated.
- New or replacement joystick can be associated to lever control station (handle identifier number 1) for purpose of button activation.
- Features available with version 3 and greater software (transparent transfer) are **not** available in this application.
- This situation would apply even if multiple components – either inboard joystick or lever control station were replaced in different areas of the network.

![[15e00187.png]]

Lever control station identifier number 1 is replaced with a lever control station with version 4 and greater software. The new lever control station will need to be changed from factory setting of ID number 1 to a unique handle identifier.

#### Scenario Number 2: Lever control station with legacy software version 3 and older is replaced with unit equipped with existing software version 4 or higher.

- Lever control station version 4 and higher software includes the capability for backward compatibility with all legacy software versions of 3 and older.
- Default handle identifier for inboard joysticks/lever control stations with existing software version 4 and greater is handle identifier number 1. Replacement of a lever control station with a different handle identifier will require that the new/replacement lever control station handle identifier will have to be changed to a unique number.
- Existing joystick can be associated to new handle identifier number 1 lever control station for purpose of button activation.
- Features available with version 4 and greater software (transparent transfer) are not available in this application.
- This situation would apply even if multiple components – either control head or joystick were replaced in different areas of the network.

![[15e00182.png]]

#### Scenario Number 3: A new “set” of control devices (control lever station and inboard joystick) are added to a network where other components with existing / legacy software already exist. This could either be adding a new station, or replacing both components at an existing station.

- Control lever station version 4 and greater and inboard joystick version 3 and greater software includes the capability for backward compatibility with legacy software's. From the standpoint of the control processor, the new units will appear to operate in the same manner of the legacy software.
- At the specific station, station number 2 in this example, the control lever station and inboard joystick will be able to support the system features (transparent transfer).
- Default handle identifiers for inboard joysticks and lever control station with existing software is handle identifier number 1. In this situation, the lever control station handle identifier will need to be changed to handle identifier number 2. Failure to do this will cause an immediate alarm when control system is activated.
- The inboard joystick at station number 2 can be setup for transparent transfer with new lever control station at the same station. When setup for transparent transfer and paired with the lever control station, inboard joystick handle identifier must be set to the same handle identifier as the lever control station which it is paired with (Station ID number 2 in the situation depicted below). If it is determined to **not** use transparent transfer, then the inboard joystick must also have a unique handle identifier.

![[15e00183.png]]

#### Scenario Number 4: A control system with components which all have new software (control head version 4 and greater / inboard joystick version 3 and greater)

- In this configuration, the lever control stations and the inboard joysticks can be installed without regard to the handle identifiers. They will be set for the default handle identifier number 1.
- If the transparent transfer feature is desired, the inboard joysticks at station number 1 and number 2 **must** be paired with the lever control stations to which are installed in proximity.
- If transparent transfer is not desired, then each station can be setup with individual / unique handle identifiers –as it currently done with existing software.
- Station number 3 inboard joystick can be setup for either “Standalone” configuration or “Transparent Transfer”. (“Transparent Transfer” is the default setting). In either setting, the inboard joystick keypad will only be active when the inboard joystick (Station number 3) is the active station.

### Four Button Lever Control Station Configuration

> [!note] Note · Примечание
> Software updates to the lever control station will apply default factory configuration settings. See information below for documenting or resetting unique configuration settings.

> [!note] Note · Примечание
> Version 3 control lever stations have an ACTIVE button. Version 4 and higher have a TAKE button. The wording has changed, but functionality has stayed the same.

Follow these eight steps to apply a new handle identifier.

Action:

Move lever control station handles to FULL ASTERN positions.

Result:

No result.

![[15900084.png]]

Action:

Turn power ON to the system.

Result:

ACTIVE/INTAKE LED will begin to flash.

![[15900085.png]]

Action:

Press and hold the two center buttons (SYNC and WARM) for approximately 2 seconds until all four LEDs begin to flash. Release buttons.

Result:

All four LEDs begin to flash.

![[15900086.png]]

Action:

Press and release the SYNC button one time to select Handle Identifier Mode.

Result:

ACTIVE/INTAKE LED will begin to flash.

![[15900087.png]]

Action:

Press and release the WARM button one time to enter Handle ID Configuration.

Result:

The current handle ID will be displayed.

| **ID\#** | **LEDs ON** |
|---|---|
| 1 | ACTIVE/INTAKE |
| 2 | SYNC |
| 3 | ACTIVE/INTAKE and SYNC |
| 4 | WARM |
| 5 | ACTIVE/INTAKE and WARM |
| 6 | SYNC and WARM |

![[15900088.png]]

Action:

Press and release the SYNC button until desired handle ID is achieved. See chart below for handle identification number and corresponding LED that is illuminated.

Result:

| **ID\#** | **LEDs ON** |
|---|---|
| 1 | ACTIVE/INTAKE |
| 2 | SYNC |
| 3 | ACTIVE/INTAKE and SYNC |
| 4 | WARM |
| 5 | ACTIVE/INTAKE and WARM |
| 6 | SYNC and WARM |

![[15900087.png]]

Action:

Press and release the WARM button one time.

Result:

This action stores the handle ID in memory. All four LEDs begin to flash after ID is stored in memory.

![[15900088.png]]

Action:

Record the handle identification number on the tag located on the bottom of the lever control station.

Result:

N/A

To exit control handle configuration mode, turn system OFF and return control handles to NEUTRAL position.

![[15900091.png]]

### Two Button Lever Control Station Configuration

> [!note] Note · Примечание
> Software updates to the lever control station will apply default factory configuration settings. See information below for documenting or resetting unique configuration settings.

Follow these eight steps to apply a new handle identifier.

Action:

Move lever control station handles to FULL ASTERN positions.

Result:

No result.

![[15900084.png]]

Action:

Turn power ON to the system.

Result:

ACTIVE will begin to flash.

![[15900085.png]]

Action:

Press and hold the two center buttons (ACTIVE and WARM) for approximately 2 seconds until all four LEDs begin to flash. Release buttons.

Result:

All four LEDs begin to flash.

![[15900092.png]]

Action:

Press and release the ACTIVE button one time to select Handle Identifier Mode.

Result:

PORT NEUTRAL LED will begin to flash.

![[15900093.png]]

Action:

Press and release the WARM button one time to enter Handle ID Configuration.

Result:

The current handle ID will be displayed.

| **ID\#** | **LEDs ON** |
|---|---|
| 1 | PORT NEUTRAL |
| 2 | ACTIVE |
| 3 | PORT NEUTRAL and ACTIVE |
| 4 | WARM |
| 5 | PORT NEUTRAL and WARM |
| 6 | ACTIVE and WARM |

![[15900094.png]]

Action:

Press and release ACTIVE button until desired handle ID is achieved. See chart below for handle identification number and corresponding LED that is illuminated.

| **ID\#** | **LEDs ON** |
|---|---|
| 1 | PORT NEUTRAL |
| 2 | ACTIVE |
| 3 | PORT NEUTRAL and ACTIVE |
| 4 | WARM |
| 5 | PORT NEUTRAL and WARM |
| 6 | ACTIVE and WARM |

![[15900095.png]]

Action:

Press and release the WARM button one time.

Result:

This action stores your handle ID in memory. All four LEDs begin to flash after ID is stored in memory.

![[15900096.png]]

Action:

Record the handle identification number on the tag located on the bottom of the lever control station.

Result:

N/A

To exit control handle configuration mode, turn system OFF and return control handles to NEUTRAL position.

![[15900091.png]]

### Inboard Joystick Configuration

> [!note] Note · Примечание
> Software updates to the inboard joystick will apply default factory configuration settings. See below for documenting or resetting unique configuration settings.

Configuration Mode

Follow these steps to enter the configuration menu.

Action:

Move joystick handle to FULL ASTERN position and hold.

Result:

No result.

![[15900097.png]]

Action:

Turn power ON to the system.

Result:

No result.

![[15900085.png]]

Action:

While holding the joystick in the full astern position, press and hold the SELECT button for 3 seconds to enter configuration mode. Once configuration mode is entered, the joystick can be released.

Result:

Both the alert indicator light (red LED) and thruster indicator light (yellow LED) on the joystick will flash simultaneously to indicate you have entered the main configuration menu.

![[15900107.png]]

Configuration Menu Options Selection

Once in configuration mode, selection of the submenu is possible. The table below shows each submenu and how the corresponding indicator light on the button pad responds.

The main configuration menu is the default menu when entering configuration mode. After entering Configuration Mode, the port bow thruster button, starboard bow thruster button, alert indicator light (red LED), and thruster indicator light (yellow LED) are used to navigate the submenus.

The port bow thruster button is the menu “Next” button, and the starboard bow thruster button is the menu “Enter” button.

Press the “Next” button to cycle through selections available and monitor the alert indicator light (red LED) to determine which menu is currently selected.

See the chart below for menu selections. The menu selections are different between inboard joystick versions.

The menu selections in the Joystick Configuration Menu options table from 1 through 5 are supported in inboard joystick version 2 and older.

Menu selections from 1 through 6 are supported in inboard joystick version 3 and newer.

When the desired menu is chosen, press the “Enter” button to enter the menu selected.

| Joystick Configuration Menu Options |  |
|---|---|
| **Alert indicator light (red LED) Flashing "x" number of times:** | **Configuration Menu Selected** |
| Both LEDs Flashing | Main Configuration Menu |
| 1 | Joystick Type Menu |
| 2 | Joystick Handle Identifier Menu |
| 3 | Associated Handle ID Menu |
| 4 | Set Factory Defaults Menu |
| 5 | Hardware Verification Menu |
| 6 | Aft Facing Joystick Configuration Menu |

The joystick button pad has the following buttons and indicator lights.

1. SELECT button
2. Port Bow Thruster button
3. Starboard Bow Thruster button
4. Port Stern Thruster button
5. Starboard Stern Thruster button
6. Alert indicator light (red LED)
7. Select indicator light (green LED)
8. Thruster indicator light (yellow LED).

![[25500005.png]]

Joystick Type Selection

The joystick type menu allows selecting whether the joystick is a standalone unit on its own dedicated station or if it associated.

If a joystick is associated, it is next to a lever control station on the same helm.

After pressing the “Enter” button to get into the joystick type menu, the alert indicator light (red LED) will continue to blink one time. The thruster indicator light (yellow LED) will begin to blink indicating which item in the sub menu is selected.

Press the “Next” button to cycle through the selections. Once you have the appropriate item selected hit the “Enter” button to confirm it.

After the setting is stored you will be returned to the Main Configuration Menu (both LEDs flashing).

Inboard joysticks with software version 3 and greater will have an additional selection for Transparent Transfer. See the Transparent Transfer procedure.

The default joystick type setting is associated. Alternately, the JOYSTICKCONFIG-SERVICE electronic service tool can be used to set joystick type. [[326-015-042 — Vessel Configuration Tool|Refer to Procedure 015-042 in Section 15.]]

| **Thruster indicator light (yellow LED) Flashing "x" number of times:** | **Setting Selected** |
|---|---|
| 1 | Standalone |
| 2 | Associated |
| 3 | Transfer |

![[nobox.png]]

Joystick Handle Identification Number

The Joystick Handle Identification Selection menu allows selection of a unique identification number for each joystick.

Each device on the controller area network (CAN) must have a unique identification number. A lever control station cannot have the same identification number of another lever control station or inboard joystick.

After pressing the “Enter” button to get into the Joystick Handle Identification Selection menu, the alert indicator light (red LED) will continue to blink two times. The thruster indicator light (yellow LED) will begin to blink indicating which item in the sub menu is selected.

> [!note] Note · Примечание
> When the thruster indicator light (yellow LED) initially blinks it will indicate the current handle identification number for the inboard joystick being operated.

Press the “Next” button to cycle through the selections. When the appropriate item is selected, press the “Enter” button to confirm it. After the setting is stored, the user will be returned to the Main Configuration Menu (both LEDs flashing).

Record the new joystick handle identification number on the tag located on the bottom of the inboard joystick. The JOYSTICKCONFIG-SERVICE electronic service tool can **not** be used to set the handle identification number.

| **Thruster indicator light (yellow LED) Flashing 'x" number of times:** | **Setting Selected** |
|---|---|
| 1 | Joystick ID 1 |
| 2 | Joystick ID 2 |
| 3 | Joystick ID 3 |
| 4 | Joystick ID 4 |
| 5 | Joystick ID 5 |
| 6 | Joystick ID 6 |

![[nobox.png]]

Associated Handle Identification Number

The Associated Handle Identification Selection menu allows selection of what lever control station the joystick is associated to. A joystick may **only** be associated to a lever control station if they are on the same helm station. This will allow the user to use the lever control station and inboard joystick more efficiently by allowing the button pad on the inboard joystick to be operational while using the lever control station handles.

After pressing the “Enter” button to get into the Associated Handle Identification Selection menu, the alert indicator light (red LED) will continue to blink three times. The thruster indicator light (yellow LED) will begin to blink indicating which item in the submenu is selected.

Press the “Next” button to cycle through the selections. Once the user has selected the appropriate item, press the “Enter” button to confirm. After the setting is stored, the user will be returned to the Main Configuration Menu (both LEDs flashing).

Record the new associated handle identification number on the tag located on the bottom of the inboard joystick. Alternately, the JOYSTICKCONFIG-SERVICE electronic service tool can be used to set the associated handle identification number. [[326-015-042 — Vessel Configuration Tool|Refer to Procedure 015-042 in Section 15.]]

| **Thruster indicator light (yellow LED) Flashing 'x" number of times:** | **Setting Selected** |
|---|---|
| 1 | Associated to Handle ID 1 |
| 2 | Associated to Handle ID 2 |
| 3 | Associated to Handle ID 3 |
| 4 | Associated to Handle ID 4 |
| 5 | Associated to Handle ID 5 |
| 6 | Associated to Handle ID 6 |

![[nobox.png]]

Factory Default Selection

Selecting factory defaults on the main configuration menu and pressing the "Enter" button will revert all settings back to factory. Reference the above submenu sections to see what factory settings are for each submenu.

After the setting is stored, the user will be returned to the Main Configuration Menu (both LEDs flashing).

To exit the Main Configuration Menu, turn the system off.

![[nobox.png]]

Hardware Verification Selection

- Select hardware verification on the menu configuration and press the “Enter” button.
- Enter diagnostic mode in the inboard joystick to check the function of the button pad and the joystick handle. Refer to Procedure 015-052 in Section 15.
- To exit the Main Configuration Menu, turn the system off.

![[nobox.png]]

Aft Facing Joystick Configuration Menu

Aft facing configuration is when the inboard joystick is mounted with boat operator facing the stern of the vessel during operation.

- Select the Aft facing configuration on the menu configuration and press the “Enter” button.
- Change the joystick function to allow for an aft facing configuration.
- After the setting is stored, the Main Configuration Menu will appear (both LEDs flashing).

![[nobox.png]]

### Throttle Control Processor Module Configuration

> [!note] Note · Примечание
> Software updates to the throttle control processor module will apply default factory configuration settings. See below for documenting or resetting unique configuration settings.

The electronic throttle and shift system should **not** need any configuration as it is pre-configured from the factory. During normal operation, the boat operator has the ability to change the engine idle speed up to 10 different idle speed settings.

The engine idle speed is always reset with a key cycle event. The engine idle initial step size setting may be changed as described below on EEC3 throttle control processor modules. This setting allows for a small or large first step to allow the electronic throttle and shift system to get into the throttle range.

After the first step size, the following nine steps allow for small idle adjustments in the throttle range. For some unique installations, it may be necessary to configure additional parameters in the throttle control processor module. For these cases, contact a local Cummins® distributor application engineer.

![[nobox.png]]

To change the default engine idle initial step size setting, perform the following steps.

Action:

Move lever control station handles to FULL AHEAD positions.

Result:

No result.

![[19903699.png]]

Action:

Turn power ON to the system.

Result:

ACTIVE/INTAKE LED will begin to flash.

![[15900109.png]]

Action:

Press and release the WARM button three times.

Result:

All four LEDs will begin to flash.

![[15900090.png]]

Action:

Press and release the SYNC button six times.

Result:

SYNC and WARM LEDs will begin to flash.

![[15900110.png]]

Action:

Press and release the WARM button one time.

Result:

No LEDs will be illuminated.

![[15900111.png]]

Action:

Press and release SYNC button until desired engine idle initial step size is achieved. See chart below for engine idle initial step size and corresponding LED that is illuminated.

Result:

| **Initial Step Size** | **LEDs ON** |
|---|---|
| 0.5% of throttle range | None |
| 1% of throttle range | ACTIVE/INTAKE |
| 2% of throttle range | SYNC |
| 3% of throttle range | ACTIVE/INTAKE and SYNC |
| 4% of throttle range | WARM |
| 5% of throttle range | ACTIVE/INTAKE and WARM |
| 10% of throttle range | SYNC and WARM |
| 20% of throttle range | ACTIVE/INTAKE, SYNC and WARM |
| 30% of throttle range | TROLL |

The default engine idle initial step size setting is 4% of throttle range.

![[15900087.png]]

Action:

Press and release the WARM button one time.

Result:

Settings will be saved to memory. SYNC and WARM LEDs will be illuminated. To exit control handle configuration mode, turn system OFF and return control handles to the NEUTRAL position.

![[15900113.png]]

### Finishing Steps

Perform a sea trial to verify proper function. Refer to Procedure 015-046 in Section 15.

![[nobox.png]]
