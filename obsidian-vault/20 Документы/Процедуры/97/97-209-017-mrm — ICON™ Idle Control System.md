---
type: "Процедура"
doc: "97-209-017-mrm"
title_en: "ICON™ Idle Control System"
modified: "2007-01-29"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 24
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-209-017-mrm.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-209-017-mrm.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# ICON™ Idle Control System

> [!abstract] Процедура · `97-209-017-mrm`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2007-01-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-209-017-mrm.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-209-017-mrm.pdf)

### General Information

Introduction

The ICON™ Idle Control System is designed to reduce excessive idle time when accomplishing the following tasks:

- The ICON™ system keeps the engine oil temperature above the minimum specification in cold weather environments. When the ICON™ system senses that the engine oil temperature is below the minimum specification, it starts the engine and lets it idle until the engine oil temperature rises to above the maximum specification.
- The ICON™ system keeps the batteries charged at all times. When the batteries drop below the minimum specification, the ICON™ system orders an engine start. The engine will idle for a minimum specified time, and will **not** shut off until the battery voltage is above maximum specification.
- The ICON™ system maintains a desired temperature inside the cab (this feature requires the cab thermostat be installed). The driver or occupant programs the thermostat to maintain a desired temperature. A temperature sensor inside the thermostat monitors the temperature inside the vehicle cab. When the temperature drops below or exceeds the set temperature (outside a specific range), the ICON™ system starts the engine and lets it idle until the specified cab temperature is reestablished.

Refer to Procedure [[97-018-025 — ICON™ System|018-025]], Specifications, for all ICON™ system specifications.

There are two versions of the ICON™ system:

- Integrated - installed at the OEM
- Aftermarket - a kit which can be installed by the distributor, dealer, or OEM.

> [!note] Note · Примечание
> The terms Integrated and Aftermarket will be used frequently throughout this manual to identify the version of the ICON™ system and information specific to that version.

The ICON™ system has with three basic modes of operation:

- Engine Mode
- Cab Comfort Mode
- Mandatory Shutdown Mode.

Engine Mode - In engine mode the engine will be shut off and restarted periodically to keep the batteries charged and the engine oil temperature above the minimum specification. The engine will restart once the engine oil temperature or the battery voltage drop below the minimum specification. When the ICON™ system starts the engine in engine mode, the engine will continue to run until both the engine oil temperature and battery voltage requirements are met.

Cab Comfort Mode - In cab comfort mode, the engine will be shut off and restarted as required to keep the batteries charged, the engine oil temperature above the minimum specification, and the cab temperature at the specified temperature. Cab temperature is controlled by the cab thermostat, which can be programmed by the operator to maintain the desired warm or cool cab temperature. The thermostat is installed inside the cab, usually mounted in the bunk area of the vehicle. Cab comfort mode will be explained in detail in the Cab Comfort Mode Feature section.

Mandatory Shutdown Mode - Mandatory shutdown mode is automatically activated whenever the other two ICON™ system modes are **not** active. Anytime the vehicle wheels stop moving (zero vehicle speed) and the parking brake is set, the ICON™ system starts a timer. If the wheels of the vehicle have **not** moved after a minimum specified time, the engine will automatically shut off. The timer's option is selected through the cab thermostat further detailed under the Cab Thermostat Setup Mode section. The mandatory shutdown mode can **not** be bypassed unless the ICON™ system is active in one of the other two modes. The ignition bus circuits will be shut off if the engine is shut off while in mandatory shutdown mode. To restart the engine after the ICON™ system has shut it off, the operator **must** turn the keyswitch from on to off, then back to on.

ICON™ idle control module (revision 19) will shut the engine down in 3 minutes when the vehicle speed is 0 kph \[0 mph\] and when the parking brake is ON. However, both module versions will shut the engine down in 15 minutes if the vehicle speed is zero and the parking brake is OFF.

Harness Identification

There are various versions of the ICON™ system. To identify if a system is an Aftermarket or **not**, inspect the bulkhead for a 14-pin connector. An Aftermarket system will have labels on this harness near the connector with a Cummins Inc. part number. See Figure 1.

![[19803820.png]]

Figure 1, ICON™ System Identification

Applications

The Aftermarket version of the ICON™ system can be installed on the following engines:

- CELECT™ Plus Engines
- ISM Series Engines
- ISM CM870 Series Engines
- ISM CM875 Series Engines
- ISX or Signature Series Engines
- ISX CM870 Series Engines
- ISX CM871 Series Engines
- ISM CM876 Series Engines.

> [!note] Note · Примечание
> The ICON™ Integrated version can **only** be installed at the OEM.

The ICON™ system is designed for use **only** with CELECT™ Plus engines (engine ECM calibration Phase 4.2 or later), ISM, ISX, and Signature engines (engine ECM calibration Phase 8.2 or later). The ICON™ system will work with all ISM CM870, ISM CM875, ISX CM870, ISM CM876, and ISX CM871 engines.

> [!note] Note · Примечание
> Cummins Inc. recommends Phase 9.3 on ISM, ISX, and Signatures engines to improve the ICON™ system operation.

### ICON™ Activation and Function

To activate the ICON™ system, perform the following steps:

- Idle the engine. Do **not** turn on the PTO. Do **not** touch the accelerator pedal.

![[15800015.png]]

- Set the parking brake.

![[15800016.png]]

- Place the transmission in neutral.

![[oi800v03.png]]

- Make sure the hood is closed.

![[15800038.png]]

- Turn the cruise control switch from the OFF position to the ON position.

> [!note] Note · Примечание
> If the switch is already on, you **must** turn it off then back on. At this point, the ICON™ lamp will start flashing quickly. This lamp flashing pattern confirms that the ICON™ system is ready to be activated.

![[gp8swku.png]]

> [!note] Note · Примечание
> The following step **must** be completed within 1 minute of turning on the cruise control switch, or the ICON™ system will be deactivated automatically.

- The ICON™ system will verify that the vehicle is in neutral. While continuously holding the clutch pedal in, shift the transmission into gear. The ICON™ lamp will flash at a slow rate (approximately 2-Hz per second). Then, shift the transmission back into neutral, and release the clutch pedal. The ICON™ lamp will light and pulse at a rate of approximately 1-Hz per second.

The ICON™ system is now active and will default to engine mode.

![[15800017.png]]

### Engine Mode Feature

> [!note] Note · Примечание
> The ICON™ system's engine start alarm, mounted on the vehicle firewall, can sound for 14 seconds prior to an automatic start initiated by the ICON™ system, depending on how it has been programmed through the cab thermostat.

Once the ICON™ system has been activated, the default mode is the engine mode. The engine will be shut off and restarted as required to keep the batteries charged and the engine oil temperature above the minimum specification. The following steps will occur automatically while the ICON™ system is in engine mode.

1. Engine rpm will slowly ramp up to the ICON™ idle speed. The ICON™ system can initially ramp the engine up to a higher rpm (ICON™ system maximum rpm) to supply a higher alternator output required to charge the batteries then lower the idle speed back down to the ICON™ idle speed.
2. The engine will run for a minimum set time if the engine oil temperature or battery voltage is low. If the battery charge and engine oil temperature is above the maximum specification, the ICON™ system will slowly ramp down the idle speed to the ICON™ system minimum rpm, or the idle speed, whichever is higher. When the lower engine speed is reached, the ICON™ system shuts down the engine after the minimum run time. If the battery is **not** charged or the engine oil is too cold, the engine will continue to run until these thresholds are met. When the engine is off, the ignition power will also be turned off.

> [!note] Note · Примечание
> The ICON™ idle speed rpm, ICON™ maximum rpm, and ICON™ minimum rpm are different than the normal idle rpm and maximum rpm settings for the engine. Refer to Procedure [[97-018-025 — ICON™ System|018-025]] for ICON™ rpm settings and to the appropriate Operations and Maintenance manual for the normal idle rpm and maximum rpm settings for your engine.

1. When the engine is **not** running, the ICON™ system remains in a wait period. During the wait period, the ICON™ lamp will remain on, pulsing at a slow rate. The ICON™ system continuously monitors the status of the engine oil temperature and the battery voltage. If the battery voltage or engine oil temperature drops below the minimum specification, the ICON™ system will restart the engine.
2. After engine restart, step 1 and step 2 will repeat with one exception; the ignition power to the accessories will remain **off** for the first 20 seconds after the engine has started and is running at the ICON™ idle speed.

### Keyless Engine Mode

Aftermarket

An enhancement to the ICON™ engine mode allows the ignition key to be removed. This optional feature is activated as previously described in ICON™ Activation and Function. In keyless engine mode, the key **must** be switched back to the OFF position, then removed before the first automatic engine shutdown occurs. Several conditions for proper function of the ICON™ system **must** be met while the keyless engine mode feature is enabled:

1. The key **must** be removed before the first automatic engine shutdown sequence occurs. If the operator removes the key after the first automatic engine shutdown has occurred, the ICON™ system will be deactivated and the engine will shut down.
2. If the accelerator pedal is depressed before the first automatic engine shutdown sequence occurs, the ICON™ system will be deactivated and shut down the engine.
3. All of the accessory devices (such as blower motors, interior lights, and so forth) should be shut off to improve battery charge. Any devices left on will operate once the ICON™ system restarts the engine, using some of the electrical energy available for accessories rather than charging the batteries. Therefore, the batteries will take longer to charge.

> [!note] Note · Примечание
> If the engine is restarted three times within 3 hours when ICON™ idle control module is revision 11 or 14 (because of low battery charge) or is restarted three times within 5 hours when ICON™ idle control module is revision 15, 16, 18, or 19 (because of low battery charge), the engine will remain running continuously. This is an indication of excessive electrical load, a defective battery charging system, or defective batteries. An ICON™ fault code will be logged. If the ICON™ system attempts to restart the engine two consecutive times and fails both times, The ICON™ system will be deactivated and a fault code will be logged. The second restart attempt occurs 1 minute after the first attempt fails.

### Cab Comfort Mode Activation and Function

> [!note] Note · Примечание
> The cab thermostat **must** be installed to activate cab comfort mode.

The ICON™ system can be put in cab comfort mode by the user when it is activated. The cab comfort mode will shut off and restart the engine as required to keep the batteries charged, keep the engine oil temperature above the minimum specification, and maintain the cab temperature at a desired level.

> [!note] Note · Примечание
> At initial turn-on of the cab thermostat, the thermostat will display the revision level of the software loaded in the thermostat, that is 01, 02, 03 and so forth.

If the thermostat is revision level 01, 02, or 06, the cab comfort mode can be deactivated by deselecting the heat or cool buttons.

If the thermostat is revision level 03, 04, or 05, the cab comfort mode can be deactivated by deselecting the heat or cool buttons, or by pushing the ON/MODE button and holding for 3 seconds.

The keyless (Aftermarket systems **only**) enhancement feature (optional in engine mode) is **not** available in cab comfort mode.

Cab temperature parameters are programmed by the user with the cab thermostat.

After performing steps 1 through 6 under the ICON™ Activation and Function section, the cab comfort mode can be activated by performing the following steps:

- Turn the cab thermostat on by pressing the ON/MODE button.

![[15800018.png]]

- Turn on the vehicle's appropriate environmental controls.

- If the cab will get hot enough to require cooling, turn on the air conditioner to the maximum setting and set the fan control to a medium setting.
- If the cab will get cold enough to require heating, turn on the heater to the maximum setting and set the fan control to a medium setting.

These settings will make certain the cab temperature is regulated efficiently.

![[15800019.png]]

- Set the cab thermostat with the desired environmental parameters. For cab thermostat programming instructions, see the Cab Thermostat Operation section.

![[15800020.png]]

### Cab Comfort Mode Feature

Once the ICON™ system has been activated, the default mode is the engine mode. When the operator turns on and sets the cab thermostat, the ICON™ system enters cab comfort mode. The cab comfort mode will shut off and restart the engine as required to keep the batteries charged, engine oil temperature above the minimum specification, and maintain the cab temperature at the desired set level. The following steps will occur automatically while the ICON™ system is in cab comfort mode:

- When the ICON™ system is activated, the engine rpm will slowly ramp up to the ICON™ idle speed. The ICON™ system can initially ramp the engine up to a higher rpm (ICON™ maximum rpm) to supply a higher alternator output then lower the idle speed back down to the ICON™ idle speed.
- The engine will run for a minimum specified time to reach the engine oil temperature and cab comfort temperature. The engine will run for a minimum amount of time if the battery voltage is low. If the battery charge and the engine oil temperature is above the maximum specification, and the cab temperature is within the set temperature parameters, the ICON™ system will slowly ramp down the idle speed to the minimum idle speed or the ICON™ idle speed (whichever is higher). When the lower engine speed is reached, the ICON™ system will shut down the engine after the initial minimum run time. If the battery is **not** charged, the engine oil is too cold, or the cab temperature is **not** within the set temperature parameters, the engine will continue to run until these thresholds are met. When the engine is off, the ignition power will also be turned off.
- When the engine is **not** running, the ICON™ system remains in a wait period. During the wait period, the ICON™ lamp will remain on, pulsing at a slow rate. The ICON™ system continuously monitors the status of the cab temperature, the engine oil temperature, and the battery voltage level. If cab temperature, engine oil temperature, or battery voltage level drops below the minimum specification, the ICON™ system will restart the engine.
- After engine restart, step 1 and step 2 will repeat with one exception; the ignition power to the accessories will remain **off** for the first 20 seconds after the engine has started and is running at the ICON™ idle speed.

> [!note] Note · Примечание
> On Aftermarket or OEM ICON™ systems, if the engine is restarted three times within 3 hours when ICON™ idle control module is revision 11 or 14 (because of low battery charge), or is restarted three times within 5 hours when ICON™ idle control module is revision 15, 16, or 18 (because of low battery charge), the engine will remain running continuously. This is an indication of excessive electrical load, a defective battery charging system, or defective batteries. An ICON™ fault code will be logged. If the ICON™ system attempts to restart the engine two consecutive times and fails both times, the ICON™ system will be deactivated and a fault code will be logged. The second restart attempt occurs 1 minute after the first attempt fails.

> [!note] Note · Примечание
> ICON™ idle control module revision 19 (regardless of mode) limits restarts to a maximum of 5 per hour.

- If the ICON™ idle control module is revision 15, 16, or 18, when the engine is started for an ICON™ system request, the thermostat will control the blowers to maintain the appropriate set point.

### ICON™ Deactivation

The preferred method of deactivating the ICON™ system is to turn off the cruise control switch. To restart the engine, after deactivating the ICON™ system, cycle the keyswitch from ON to OFF, then manually restart the engine.

After the ICON™ system has been activated in either engine mode (including keyless engine mode) or cab comfort mode, the ICON™ system will be deactivated if any of the following occurs:

1. Interlock switch open (neutral, parking, hood)
2. Vehicle speed greater than 0 mph
3. A Fault becomes active in the ICON™ system
4. (Aftermarket systems **only**) accelerator is depressed with keyswitch on or off (keyless engine mode) before first shutdown
5. Cruise control switch turned off
6. Keyswitch turned off after first shutdown
7. (Aftermarket or OEM systems **only**) keyswitch turned on when in keyless engine mode
8. (Aftermarket systems **only**) PTO is activated with keyswitch on or off (keyless engine mode) before first shutdown

### Cab Thermostat Operation

The ICON™ cab thermostat can be programmed by the operator. The ICON™ system does **not** have control over the environmental controls of the vehicle. In order for the ICON™ cab thermostat to operate correctly, the vehicle's environmental controls **must** be set correctly.

If the operator expects that the temperature inside the cab will become hotter when the engine is turned off, the operator will turn on the vehicle's air conditioner. If the operator expects that the temperature inside the cab will become colder when the engine is turned off, the operator will turn on the vehicle's heater.

> [!note] Note · Примечание
> It is important that the cab temperature controls be set correctly. On Aftermarket systems, if the ICON™ system commands the engine to start because it senses the cab is too hot and the operator has turned on the heater instead of the air conditioner, the cab thermostat will log a fault after 45 minutes or if the command to restart the engine is within 10 minutes of the last auto-cycle when the ICON™ thermostat is revision level 01 or 02. On Integrated and Aftermarket systems, the ICON™ system will log a fault after 60 minutes or if the command to restart the engine is 4 times within an hour when the ICON™ thermostat is revision level 03. The ICON™ system senses that the set temperature parameters are **not** being met, logs a fault, and can, possibly, shut the engine off. This fault does **not** exist in revision level 04, 05, and 06.

If the ICON™ thermostat is revision 03, 04, 05, or 06 the thermostat will automatically return to normal operation state once the temperature has been met.

> [!note] Note · Примечание
> The thermostat trims can also be adjusted. See the Trim Settings and instructions for Thermostat Setup Mode at the end of this section.

![[15800001.png]]

There are four buttons on the thermostat. They are:

- **ON/MODE** - This button turns the thermostat on and toggles through the different cab thermostat screens.

> [!note] Note · Примечание
> If ICON™ thermostat is revision level 03 and higher, and the thermostat is on, pressing and holding the ON/MODE button for 3 seconds will turn off the thermostat.

- **ENTER** - This button is used to enter parameter adjustments. After a selection is made by the operator, the ENTER button **must** be pushed so that the ICON™ system will remember the new parameters.

- **DOWN** - This button is used to adjust parameters by decreasing the value.
- **UP** - This button is used to adjust parameters by increasing the value.

![[15800020.png]]

When the ON/MODE button is pressed during the initial start-up of the ICON™ system, cab comfort mode is activated. The thermostat readout will show the cab temperature.

![[15800018.png]]

By pressing the ON/MODE button, the thermostat will toggle through each of the seven displays. These displays are as follows:

Inside Temperature - Displays the temperature inside the cab.

![[15800020.png]]

Outside Temperature - Displays the temperature outside the cab as read from the ambient air temperature sensor.

![[15800021.png]]

Set Point - Heat - Displays the desired temperature that has been set for heat mode. When in heat mode of operation, this is the temperature that the cab thermostat **must** sense prior to commanding the engine to shut down. This temperature can be changed by pressing the UP or DOWN button.

When the new desired temperature is displayed, the ENTER button **must** be pressed to save the new set point.

![[15800022.png]]

Set Point - Cool - Displays the temperature that has been set for cool mode. When in cool mode of operation, this is the temperature that the cab thermostat **must** sense prior to commanding the engine to shut down. This temperature can be changed by pressing the UP or DOWN button.

When the new desired temperature is displayed, the ENTER button **must** be pressed to save the new set point.

![[15800023.png]]

Range - This displays the number of degrees (Fahrenheit) the temperature is allowed to fluctuate before the engine is started.

- If the thermostat is in heat mode, this number is the number of degrees the temperature is allowed to fall below the set point before the engine is started.
- If the thermostat is in cool mode, this number is the number of degrees the temperature is allowed to rise above the set point before the engine is started.

The range is set by pressing the UP or DOWN button. The range will be either 4, 6, or 8 (degrees Fahrenheit). When the range has been selected, the ENTER button **must** be pressed to save the new parameter.

![[15800024.png]]

For example, if the set point heat and the set point cool are both set for 75°F, and the range is set to 4, then, when the thermostat is in heat mode, the vehicle will start when the cab temperature drops to 71°F. When the thermostat is in cool mode, the vehicle will start when the cab temperature reaches 79°F.

![[nobox.png]]

Heat - The word "HEAT" will be displayed if heat mode is active. Two dashes displayed indicates that Heat Mode is **not** activated. To activate the heat mode, press the ENTER button until the display reads "On" The HEAT indicator will flash if the cab thermostat requires the engine to start to achieve the heat set point.

> [!note] Note · Примечание
> If the outside temperature is above 26.6°C \[80°F\], heat mode can **not** be activated. Or, if the outside temperature is below 15.5°C \[60°F\], heat mode will automatically be activated. See the Thermostat Setup Mode - Trim Settings, later in this section, for details on the cab thermostat trim setup mode.

> [!note] Note · Примечание
> ICON™ thermostat revision level 06 features an expanded range to improve overall ICON™ efficiency. For example, if the set point heat and the set point cool are both set to 21°C \[70°F\], and the range is 4, then, when the thermostat is in heat mode, the vehicle will start when the cab temperature drops to 19°C \[66°F\] and continue to run until the cab temperature reaches 22°C \[72°F\]. When the thermostat is in cool mode, the vehicle will start when the cab temperature reaches 23°C \[74°F\] and will continue to run until the temperature had dropped to 20°C \[68°F\]. This feature is adjustable.

![[15800025.png]]

Cool - The word "COOL" will be displayed if cool mode is active. Two dashes displayed indicates that cool mode is **not** activated. To activate the cool mode, press the ENTER button until the display reads "On". The COOL indicator will flash if the cab thermostat requires the engine to start to achieve the cool set point.

> [!note] Note · Примечание
> If the outside temperature is below 15.5°C \[60°F\], cool mode can **not** be activated. Or, if the outside temperature is above 29.4°C \[85°F\], cool mode will automatically be activated. See the Thermostat Setup Mode - Trim Settings, later in this section, for details on the cab thermostat trim setup mode.

![[15800026.png]]

With the ICON™ system in cab comfort mode, the ICON™ system will monitor the engine oil temperature, monitor the battery voltage, and keep the cab temperature within the specified range that has been programmed into the ICON™ cab thermostat.

![[nobox.png]]

![[15800027.png]]

![[15800028.png]]

The two illustrations above show the thermostat display when it is in heat mode or in cool mode. The word "COOL" or "HEAT" in the bottom left corner of the display screen indicates the thermostat mode.

### ICON™ Idle Adjustment

Aftermarket

After the ICON™ system has restarted the engine, the idle speed can be adjusted by pressing the clutch pedal, or the brake pedal on ICON™ idle control module revisions 18 and 19, to decrease the engine speed, or pressing the accelerator pedal to increase the engine speed. The new ICON™ idle speed will be saved and used until it is adjusted again. Refer to Procedure [[97-018-025 — ICON™ System|018-025]] for correct specifications.

> [!note] Note · Примечание
> For optimum ICON™ system performance when in the heat mode, Cummins Inc. recommends using the higher nominal rpm idle speed setting. However, when in the cool mode, Cummins Inc. recommends a lower setting to reduce fuel consumption.

Integrated

The idle speed can be adjusted by using the INSITE™ electronic service tool. The new ICON™ idle speed will be saved and used until it is adjusted again. Refer to Procedure [[97-018-025 — ICON™ System|018-025]] for correct specifications.

> [!note] Note · Примечание
> For optimum ICON™ system performance, Cummins Inc. recommends using the high nominal rpm idle speed setting.

### Fault Code Notification

Aftermarket

The ICON™ idle control module monitors the various signals it receives to determine whether a fault condition exists with the ICON™ system. If any faults are detected, the ICON™ system logs the fault in its memory. The ICON™ lamp notifies the operator of a fault by flashing a three digit ICON™ fault code each time the keyswitch cycles from off to on. To flash a fault code, the lamp flashes a number of times for the first digit of the code; then, after a short pause, the lamp flashes out the second digit of the fault code, and again, after another short pause, flashes out the third digit of the fault code. After a longer pause, the lamp repeats the flashing sequence.

If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault until it has been corrected and then the next active fault will be flashed out.

> [!note] Note · Примечание
> The ICON™ system can **not** be activated until the fault code lamp flashing sequence is complete.

> [!note] Note · Примечание
> The ICON™ service tool will allow viewing of all of the active and inactive fault codes at the same time.

Integrated

The engine ECM monitors the various signals it receives to determine whether a fault condition exists with the ICON™ system. If any faults are detected, the engine ECM logs the fault in its memory. The faults are read using the INSITE™ electronic service tool.

### Thermostat Setup Mode

To enter the cab thermostat trim mode, first turn on the keyswitch. Press the UP or DOWN button on the cab thermostat 7 times while the software version is flashing on the cab thermostat display. You have 10 seconds to start this process.

After entering the TRIM mode, press the UP button to scroll increasingly through the trims, and press the DOWN button to scroll decreasingly through the trims. Using this process, select the trim desired to adjust. Press ENTER to save the setting.

For temperature adjustments, press the UP or DOWN button to adjust the temperature accordingly, then press ENTER to save the setting.

For Enables, press the UP or DOWN button to toggle between the "E" displayed to the immediate right of the trim number, or no "E" displayed. Press ENTER to save the setting.

To exit the thermostat trim mode, press ON/MODE button.

### Trim Settings

1. Extreme Hot

  1. Thermostat revision level 01 or 02 (Aftermarket Only)

    - Below this ambient (outside) temperature, if the cab temperature does **not** reach the desired set point within 45 minutes or if sending a cab thermostat request (start) within 10 minutes of the last auto-cycle, an E3 fault (Fault Code 469) will be logged.
    - Default Setting: 100°F

  2. Thermostat revision level 03 or 06

    - Below this ambient (outside) temperature, if the cab temperature does **not** reach the desired set point within 60 minutes or if sending four cab thermostat requests (starts) within 1 hour of the last auto-cycle, an E3 fault (Fault Code 469) will be logged.
    - Default Setting: 90°F (revision level 04 and 05)

2. Extreme Cold

  1. Thermostat revision level 01 or 02 (Aftermarket Only)

    - Above this ambient (outside) temperature, if the cab temperature does **not** reach the desired set point within 45 minutes or if sending a cab thermostat request (start) within 10 minutes of the last auto-cycle, an E3 fault (Fault Code 469) will be logged.
    - Default Setting: 0°F

  2. Thermostat revision level 03 or 06

    - Above this ambient (outside) temperature, if the cab temperature does **not** reach the desired set point within 60 minutes or if sending four cab thermostat requests (starts) within 1 hour of the last auto-cycle, an E3 fault (Fault Code 469) will be logged.
    - Default Setting: 20°F (revision level 04 and 05)

3. Auto Heat

  1. Below this ambient (outside) temperature, the thermostat will default into the heat mode when the key switch is turned on and the thermostat is on.
  2. Thermostat revision level 01 or 02 (Aftermarket Only)

    - Default Setting: 60°F

  3. Thermostat revision level 03, 04, 05, and 06

    - Default Setting: 69°F

4. Auto Cool

  1. Above this ambient (outside) temperature, the thermostat will default into the Cool Mode when the keyswitch is turned on and thermostat is on.
  2. Thermostat revision level 01, 02, or 06 (Aftermarket Only)

    - Default Setting: 85°F

  3. Thermostat revision level 03, 04 and 05

    - Default Setting: 70°F

5. Disable Heat

  1. Above this ambient (outside) temperature, the operator will **not** be able to activate the heat mode.
  2. Default Setting: 80°F (revision level 03, 04, 05, and 06)

6. Disable Cool

  1. Below this ambient (outside) temperature, the operator will **not** be able to activate the cool mode.
  2. Default Setting: 60°F (revision level 03, 04, 05, and 06)

7. Response to E3 Fault

  1. If the thermostat logs an E3 fault, enabling this trim will cause the engine to cycle between 20 minutes running and 15 minutes shutdown regardless of the cab temperature. By disabling this trim, the engine will **not** auto start, regardless of the cab temperature.
  2. Default Setting: Enabled

8. Alarm in Cab Comfort Mode, revision level 01, 02 and 03 (Aftermarket Only)

  1. Enabling this trim will allow the engine start alarm to sound prior to any auto start of the engine. Disabling this trim will turn off the engine start alarm when in cab comfort mode. Disabling this trim is **not** allowed with Integrated system.
  2. Default Setting: Enabled

> [!note] Note · Примечание
> This feature is **not** available in revision level 04, 05, and 06.

1. Automatic E3 Shutdown

  1. Thermostat will automatically turn off when thermostat has been in an E3 condition continuously for more than two hours.
  2. Default Setting: Enabled

2. Weekend Timer

  1. Thermostat will automatically turn off when thermostat has been no for more than 12 hours.
  2. Default Setting: Enabled

3. Narrower Temperature Settings

  1. Thermostat can be set to narrower temperature set points for heat and cool. These points are 68°F and 73°F.
  2. Default Setting: Disabled

4. Temperature Scale

  1. Allows for changing between Fahrenheit and Celsius temperature scales
  2. Default Setting: Fahrenheit

5. Short Idle Enable

  1. In mandatory shutdown mode, enabling this trim will allow the engine to run for a maximum of 5 minutes if idle control module is revision 11 or 13, or a maximum of 5 minutes adjustable to 18 hours if idle control module is revision 14. Disabling this trim will allow the engine to run for a maximum of 15 minutes. (Integrated systems **must** use INSITE™ electronic service tool to adjust this feature; Aftermarket systems **must** use the ICON™ service tool, ICON™ idle control module 15 and 16, to adjust this feature.)
  2. Default Setting: Disabled (Thermostat Revision 04 and 05)

> [!note] Note · Примечание
> This feature is no longer available. Mandatory shut down will be 15 minutes if vehicle speed is zero and parking brake is off. Mandatory shut down will be 5 minutes when vehicle speed is zero and parking brake is ON for ICON™ control module revision level 18. ICON™ idle control module (revision 19) will shut the engine down in 3 minutes when the vehicle speed is 0 kph \[0 mph\] and when the parking brake is ON.”

1. Efficiency Improvement Temperature Range Setting

  1. Allows an expanded range to improve overall ICON™ efficiency. For example, if the set point heat and the set point cool are both set to 21°C \[70°F\], and the range is 4, then, when the thermostat is in heat mode, the vehicle will start when the cab temperature drops to 19°C \[66°F\] and continue to run until the cab temperature reaches 22°C \[72°F\]. When the thermostat is in cool mode, the vehicle will start when the cab temperature reaches 23°C \[74°F\] and will continue to run until the temperature has dropped to 20°C \[68°F\].
  2. Default Setting: -17°C \[2°F\]

2. Prelube Enable

  1. If the vehicle is equipped with a pre-lube system, this trim configures the ICON™ system appropriately.
  2. Default Setting: Disabled

> [!note] Note · Примечание
> This feature is no longer available in revision level 04, 05, and 06.

1. Reset to Defaults

  1. Resets all the trims back to the factory default settings.
  2. Default Setting: N/A
