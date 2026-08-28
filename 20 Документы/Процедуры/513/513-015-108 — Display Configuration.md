---
type: "Процедура"
doc: "513-015-108"
title_en: "Display Configuration"
modified: "2026-05-12"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
figures: 62
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-108.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-108.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Display Configuration

> [!abstract] Процедура · `513-015-108`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2026-05-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-108.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-108.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- No recommended Cummins® service tools.

#### Additional Service Items

- No additional service items required.

### General Information

The Cummins® C Command Connect and Connect Premier Marine Panel System ED-4/ED-5/ED-7 display(s) are preloaded with software from the factory. The Cummins® ED-4 Display software and vessel personality file **must** be updated and configured prior to proper operation of the display. The Cummins® ED-5/ED-7 Display **must** be configured to select preloaded vessel personality files/themes prior to proper operation of the display.

> [!note] Note · Примечание
> Updating software erases the configuration settings, log files, and saved vessel personality files in the ED-4.

### Preparatory Steps

ED-4

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury or equipment damage, this procedure must only be performed by suitably qualified service technicians.

Prior to updating the display configuration, document and understand the vessel performance and alarm/fault codes. Follow the alarm/fault code or the appropriate troubleshooting symptom tree to understand issues.

Reference the following procedures for testing and additional configuration setup information:

- If needed, verify proper function. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15]].
- If needed, use the following procedure to find, select, save, import, or export the ED-4 vessel personality file when updates are required. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15]].
- If needed, document the operator ED-4 settings. [[513-101-013 — General Operating Instructions|Refer to Procedure 101-013 in section 1]].

ED-5 and ED-7

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury or equipment damage, this procedure must only be performed by suitably qualified service technicians.

Prior to updating the display configuration, document and understand the vessel performance and alarm/fault codes. Follow the alarm/fault code or the appropriate troubleshooting symptom tree to understand issues.

Reference the following procedures for testing and additional configuration setup information:

- If needed, verify proper function. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15.]]
- If needed, use the following procedure to find, select, save, import, or export the ED-5/ED-7 vessel personality file when updates are required. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]

### Setup Information

ED-4

The user can interact with the display through keys 1 through 5 on the front of the display.

The function of the key is shown on the ED-4 screen above the key, which changes as selections are made.

A variety of engine and vessel configuration setups can be made on the ED-4 display.

Refer to sections below for ED-4 configuration setup information.

> [!note] Note · Примечание
> The configuration of an ED-4 is different for a helm versus a customer interface box (C.I.B.). The C.I.B. ED-4 is typically setup as the gateway and parent of the system.

> [!note] Note · Примечание
> If the configuration settings of the ED-4 are changed, it is recommended to save it to internal memory as an updated vessel personality file and title. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 1]] 5.

![[00e00122.png]]

The Configuration page of the ED-4 display can be accessed by pressing key 5 or “Menu” on the data screen page.

Action:

- Press key 5 or “Menu”.
- Select “Configuration” and press key 4 or “Enter”.

To exit:

Press key 5 or “Exit” to return to the data screen page.

![[15e00131.png]]

> [!note] Note · Примечание
> Modifying ED-4 settings in the Configuration page may result in loss of functionality of the system. Accessing the Configuration page is logged in the ED-4 internal memory.

Press key 1 or “Accept” to continue.

To exit:

Press key 5 or “Back” to return to the Menu page.

Press key 5 or “Exit” to return to the data screen page.

![[15e00132.png]]

Configuration:

There are a number of items in the ED-4 Configuration page that can be accessed.

1. Device Network Settings - Used for device set up of the ED-4. This page accesses the source address of the controller area network (CAN) transceivers of the ED-4.
2. vessel personality file - Used to select vessel personality files stored in internal memory of the ED-4.
3. Screen Configuration - Used to enable or disable data screens viewed by the operator.
4. IO Configuration - Used for sensor input and outputs settings.
5. Stbd - Used for source address setup of starboard engine monitored by the ED-4(s).
6. Port - Used for source address setup of port engine monitored by the ED-4(s).

> [!note] Note · Примечание
> Items 1 to 4 configuration settings are typically controlled by the vessel personality file.

> [!note] Note · Примечание
> Setup of items 5 and 6 relate to the engine(s) or generator(s) and are important for proper functionality and data monitoring by the ED-4. There may be more or less engine(s) and/or generator(s) available on the page for setup depending on the vessel personality file loaded in the ED-4.

![[15e00133.png]]

Configuration - Device Network Settings

> [!note] Note · Примечание
> Initial Device Network Settings are controlled by the vessel personality file but may be impacted by other network devices when the ED-4(s) powers on.

Action:

- Select “Device Network Settings” and press key 4 or “Enter”.
- Select each press key 4 or “Enter” or “Change” to view.

When finished:

Press key 5 or “Back” to save the setting and exit the page.

![[15e00134.png]]

Configuration - Device Network Settings

There are four options under Device Network settings:

1. CAN Channel 1
2. CAN Channel 2 (Isolated)
3. PGN Bridging
4. Parent

> [!note] Note · Примечание
> The ED-4 parent set up will need to be updated for the system after a software and/or vessel personality file update. There will **always** be one parent in the system. The parent is typically set up in the ED-4 located in the C.I.B. See below for more details.

![[15e00196.png]]

Device Network Settings - CAN Channel 1 Settings - J1939

- Baud Rate: Should **always** be set to match the ECM broadcast rate, which is typically 250K. If the baud rate setting is incorrect, the data on the ED-4 data screen will be dashes.
- Seed Address: Used to manually set the source address of the ED-4. The range of seed address is typically 228 to 231 for the C.I.B. ED-4. The helm ED-4 seed address is typically 128 or higher. When the Preferred Address is enabled and set to a valid address in the vessel personality file, the Seed Address will be displayed as “Preferred”.
- Preferred Address: The address which will likely be used by the ED-4, if available, and is important for broadcasting when used as gateway. The address the C.I.B. ED-4 will try to claim is typically in range 228 to 231. In case of an address conflict with the preferred address, alarms will be triggered by the ED-4. Whenever the preferred address is **not** available or claimed by the ED-4, an alarm will be triggered. The Preferred Address will be shown as “Disabled” for the helm ED-4 displays.
- Perform Address Claim: Used to save the seed address or preferred address manually selected.
- Actual Address: Address claimed by the ED-4, which starts at the seed address or preferred address then increments to a unique address for each ED-4 on a common network. Address 128 is set to the ED-4 with the lowest software serial number.

![[15e00161.png]]

Device Network Settings - CAN Channel 2 Settings - NMEA 2000

- Baud Rate: Should always be set to match the ECM broadcast rate, which is typically 250K. If the baud rate setting is incorrect, the data on the ED-4 data screen will be dashes.
- Seed Address: Used to manually set the source address of the ED-4. The ED-4 seed address is typically 128 or higher. When the Preferred Address is enabled and set to a valid address in the vessel personality file, the Seed Address will be displayed as “Preferred”.
- Preferred Address: The address which will likely be used by the ED-4, if available, and is important for broadcasting when used as gateway. The address the C.I.B. ED-4 will try to claim is typically in range 228 to 231. In case of an address conflict with the preferred address, alarms will be triggered by the ED-4. Whenever the preferred address is **not** available or claimed by the ED-4, an alarm will be triggered. The Preferred Address will be shown as “Disabled” for the helm ED-4 displays.
- Perform Address Claim: Used to save the seed address or preferred manually selected.
- Actual Address: Address claimed by the ED-4, which starts at the seed address or preferred address then increments to a unique address for each ED-4 on a common network. Address 128 is set to the ED-4 with the lowest software serial number.

![[15e00162.png]]

Device Network Settings - Parent

For C Command Connect Premier, the ED-4 at the C.I.B. is typically set up as the Parent.

For C Command Connect without the C.I.B., the ED-4 located at the main station on the vessel will be setup as the Parent.

There **must** be **only** one parent per connected group network of displays.

Parent application types:

- Isolated J1939 with devices connected to J1939 - One parent per engine.
- Common J1939 - One parent per vessel.
- Independent J1939, but bridged by NMEA 2000 or twin J1939 display - One parent per vessel.

> [!note] Note · Примечание
> Prior to software and/or vessel personality file update, it is important to locate the ED-4 setup as the Parent of the system.

![[15e00138.png]]

Configuration - vessel personality file

Use the following procedure for information about “vessel personality file” in the Configuration page. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in section 15.]]

ED-4 setup and configuration setting changes are saved to the internal memory of the ED-4. To update the locally stored vessel personality file, the vessel personality file **must** be exported to USB drive and then imported back into the ED-4 and saved as a “favorite”.

> [!note] Note · Примечание
> The software controls the number of default vessel personality files stored to internal memory of the ED-4. Additional vessel personality files can be saved to the internal memory of the ED-4 by importing with a USB drive.

![[15e00139.png]]

Configuration - Screen Configuration

Action:

- Select “Screen Configuration” and press key 4 or “Enter”.
- Select each screen and press key 4 to “Enable” or “Disable”.

> [!note] Note · Примечание
> Typically there are three or more default screens available for each engine. The available data screen information is controlled by the vessel personality file.

Press key 5 or “Back” to save the setting and exit the page.

![[15e00140.png]]

Configuration - IO Configuration

The IO Configuration settings are controlled by the vessel personality file. The components/sensors listed on the page are typically non-engine related original equipment manufacturer (OEM) sensors.

Action:

- Select “IO Configuration” and press key 4 or “Enter”.
- Select each and press key 4 or “Enter”.
- There are various sensor types and ranges available.

A sensor type and range **must** be selected to turn it “On” in the page.

The proper sensor range **must** be selected for the parameter to display data correctly.

To determine the ED-4 sensor type and range that is currently configured, refer to the measurement mode on the I/O viewer page. Use the test section of the following procedure for access. [[513-015-035 — Display(s) and Instrumentation|Refer to Procedure 015-035 in Section 15]].

> [!note] Note · Примечание
> For a sensor to display data properly on the ED-4, it **must** have the correct calibration table loaded in the vessel personality file. Use the following procedure for accessing sensor information contained in the vessel personality file. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in section 15.]] The Cummins® Marine Application Engineering group creates the vessel personality files and updates the Cummins® QuickServe® Online disc or drive folder “Cummins® ED-4 Display Vessel Personality File Tracking Sheet” with file name, version, and description of the vessel, application, equipment, and vessel sensor information.

Press key 5 or “Back” to save the setting and exit the page.

![[15e00141.png]]

Configuration - Stbd (Starboard Engine)

> [!note] Note · Примечание
> The vessel personality file controls a majority of the settings for each engine, though it is important to verify the settings based on the location of the ED-4 (helm vs C.I.B.).

> [!note] Note · Примечание
> The process outlined below can be used to setup each engine available on the Configuration page.

Action:

- Select “Stbd” and press key 4 or “Enter”.
- If needed, select each and press key 4 or “Change” or “Enter”.

When Finished:

Press key 5 or “Back” to save the setting and exit the page.

![[15e00142.png]]

Configuration – ESN Selection

Action:

- Select “ESN Selection” and press key 4 or “Enter”.
- Select the ESN for engine source for broadcasting on NMEA 2000 and press key 4 to “Select".

![[15u00011.png]]

Action:

- The selected ESN for engine source is marked with “\< ---“.

> [!note] Note · Примечание
> The ESN Selection option **only** applies to ED-4 at Helm using vessel personality file.

> [!note] Note · Примечание
> The ESN Selection option applies to Helm ED-4 used for NMEA 2000 gateway. Each Helm ED-4 is used as a NMEA 2000 gateway for a single engine source.

Press key 5 or “Back” to save the setting and exit the page.

![[15u00012.png]]

Configuration – Adjust Alarms

Action:

- Select “Adjust Alarms” and press key 4 or “Enter”.

![[15e00240.png]]

- Select the alarm channel fault threshold for sensor monitored by ED-4 and press key 4 to “Edit".

![[15e00241.png]]

Action:

- The selected alarm channel fault threshold can be adjusted to press key 4 and key 3 to increment and decrement threshold value.

> [!note] Note · Примечание
> Modifying alarm channel threshold settings in “Adjust Alarms” can result in loss of diagnostic functionality.

Alarm threshold values for OEM‑supplied components **must** follow the component manufacturer's recommendations. Contact the OEM or factory Application Engineering for guidance on diagnostic alarm threshold settings.

![[15e00242.png]]

Configuration - Stbd (Starboard Engine)

There are 5 options under the engine:

1. CAN 1
2. CAN 2
3. J1939
4. NMEA 2000
5. Transmission Source

![[15e00143.png]]

Stbd (Starboard Engine) - J1939

- Source 1 - Selecting the addresses for the display to monitor.
- Source 2 - Selecting the addresses for the display to monitor.

The J1939 settings **must** be selected for the engine source. Every device on J1939 network including the engine will have a unique address (in the range of 0 to 255). In order for the display to show data from a particular engine, the source address of that engine **must** be known. The appropriate display is then configured to match this source address.

Action:

- Select “Source 1” and “Source 2” and press key 4 or “Inc” to adjust

When Finished:

Press key 5 or “Back” to save the setting and exit the page.

| Source Selections for C.I.B. ED-4 |  |  |
|---|---|---|
| Source 1 - J1939 Source Address (Engine) | Source 2 - Preferred J1939 Source Address (C.I.B. ED-4) | HMLD Engine Description |
| 0 | 0 | Starboard Outer |
| 1 | 1 | Port Outer |
| 239 | 239 | Starboard Inner |
| 240 | 240 | Port Inner |
| 234 | 234 | Genset |
| 158 | 158 | Genset |
| 179 | 179 | Genset |
| 203 | 203 | Genset |

| Source Selections for Helm ED-4 |  |  |
|---|---|---|
| Source 1 - J1939 Source Address (Engine) | Source 2 - Preferred J1939 Source Address (C.I.B. ED-4) | HMLD Engine Description |
| 0 | 228 | Starboard Outer |
| 1 | 229 | Port Outer |
| 239 | 230 | Starboard Inner |
| 240 | 231 | Port Inner |
| 234 | Not Applicable | Genset |
| 158 | Not Applicable | Genset |
| 179 | Not Applicable | Genset |
| 203 | Not Applicable | Genset |

![[15e00163.png]]

Stbd (Starboard Engine) - J1939 - J1939 Gateway

The selections in this page can be “Yes” or “No” depending on if the component/sensor is broadcasting onto J1939.

> [!note] Note · Примечание
> This **only** applies to for messages broadcasting from the ED-4.

Action:

- Select “J1939 Gateway” and press key 4 or “Config”.
- Scroll and press key 4 or “Change” to adjust.

When Finished:

Press key 5 or “Back” to save the setting and exit the page.

![[15e00145.png]]

Stbd (Starboard Engine) - NMEA 2000 - NMEA 2000 Gateway

The selections in this page can be “Yes” or “No” depending on if the component/sensor is broadcasting onto NMEA 2000.

Action:

- Select “NMEA 2000” and press key 4 or “Enter”.
- Select “NMEA 2000 Gateway” and press key 4 or “Config”.
- Scroll and press key 4 or “Change” to adjust.

When Finished:

Press key 5 or “Back” to save the setting and exit the page.

![[15e00147.png]]

Stbd (Starboard Engine) - NMEA 2000 - Engine

This page defines the engine instance that will be assigned to NMEA 2000 messages for the selected device.

Action:

- Scroll to “Engine”.
- Press key 4 or “Inc” to adjust.

When Finished:

Press key 5 or “Back” to save the setting and exit the page.

![[15e00148.png]]

> [!note] Note · Примечание
> The table information below applies to default factory vessel personality file settings. Custom vessel personality file settings can be found in the vessel personality file tracking sheet. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15]].

| Single Engine Application |  |  |  |  |
|---|---|---|---|---|
| J1939 Source Address (Reference only) | NMEA 2000 Engine Instance | Seed Address Selected | Engine Description | MUS ID Physical Jumper Pin Locations |
| 0 | 0 | 228 | Starboard/Port/Center | 1,2 |

| Twin Engine Application |  |  |  |  |
|---|---|---|---|---|
| J1939 Source Address (Reference only) | NMEA 2000 Engine Instance | Seed Address Selected | Engine Description | MUS ID Physical Jumper Pin Locations |
| 0 | 1 | 228 | Starboard | 1,2 |
| 1 | 0 | 229 | Port | 1,3 |

| Triple Engine Application |  |  |  |  |
|---|---|---|---|---|
| J1939 Source Address (Reference only) | NMEA 2000 Engine Instance | Seed Address Selected | Engine Description | MUS ID Physical Jumper Pin Locations (CM2250 ECM and newer) (\*CM850 and CM570 ECM) |
| 1 | 0 | 229 | Port | 1,3 |
| 239 or 242\* | 1 | 230 | Center | 1,2,3 |
| 0 | 2 | 228 | Starboard | 1,2 |

| Quad Engine Application |  |  |  |  |
|---|---|---|---|---|
| J1939 Source Address (Reference only) | NMEA 2000 Engine Instance | Seed Address Selected | Engine Description | MUS ID Physical Jumper Pin Locations (CM2250 ECM and newer) (\*CM850 and CM570 ECM) |
| 0 | 3 | 228 | Starboard Outer | 1,2 |
| 1 | 0 | 229 | Port Outer | 1,3 |
| 239 or 242\* | 2 | 230 | Starboard Inner | 1,2,3 |
| 240 or 243\* | 1 | 231 | Port Inner | 1,4 |
| 234 | 4 | Not Applicable | Genset | W3 and W4 **not** cut |
| 158 | 5 | Not Applicable | Genset | W3 **not** cut and W4 cut |
| 179 | 6 | Not Applicable | Genset | W3 cut and W4 **not** cut |
| 203 | 7 | Not Applicable | Genset | W3 and W4 cut |

Stbd (Starboard Engine) - NMEA 2000 - Fuel Level, Transmission Oil P, Rudder/Steering Angle

These selections define the engine instance that will be assigned to NMEA 2000 messages for the selected parameter.

Refer to the table above for setup.

> [!note] Note · Примечание
> At time production, the remaining parameters on the page are **not** utilized by the ED-4.

Action:

- Scroll to parameter.
- Press key 4 or “Inc” to adjust.

When Finished:

Press key 5 or “Back” to save the setting and exit the page.

![[15e00148.png]]

Stbd (Starboard Engine) - Transmission Source

The transmission source allows for selecting where the transmission sensors are being routed through.

1. Temperature
2. Pressure

Action:

- Select “Transmission Source” and press key 4 or “Enter”.
- Scroll and press key 4 or “Change” to adjust.

When Finished:

Press key 5 or “Back” to save the setting and exit the page(s).

![[15e00150.png]]

ED-5 and ED-7

The user can interact with the display through touch screen or through keys on the optional remote keypad.

A variety of engine and vessel configuration setups can be made on the ED-5/ED-7 display.

Refer to Setup section for ED-5/ED-7 configuration information.

![[15e00203.png]]

The Configuration page “Setup” of the ED-5/ED-7 display can be accessed by pressing in the middle of the screen or press on the “Menu”(I) icon on the data screen page or press and hold “Select/Enter” key on the data screen page to open the Menu page. The Configuration setting “Setup” is protected under the security PIN interface.

Action:

- Press the middle of the data screen page or press on the “Menu”(I) icon or press “Select/Enter” on the remote keypad.
- Select “Security”(VI), then “Change Level”, then “Diagnostic” or use the remote CAN keypad to scroll through menu and selection.
- Enter the “Security PIN”.
- Swipe left to right to access the “Setup” page.

When Finished:

- Swipe from left to right when in the Menu structure or press “Back”(IV) on the screen to exit to the data screen page.

The default security PIN to access advanced settings is “1919”. Sharing the default security PIN without proper knowledge may lead to unintended changes causing loss or erratic function.

The security PIN entry on the display is **only** available using touchscreen and can **not** be performed using remote keypad.

![[15e00204.png]]

![[15e00205.png]]

Security Pin Entry

![[15e00206.png]]

Setup Menu Selection

Setup:

There are number of items in the ED-5 / ED-7 Setup page that can be accessed.

1. Menu Mode – Used to toggle between Basic and Advanced level Setup options of the ED-5/ED-7.
2. Connections – Used for device set up of the ED-5/ED-7. This page accesses the source address of the controller area network (CAN) transceivers and Analogue Inputs configuration of the ED-5/ED-7.
3. Themes – Used to select vessel personality files / application configuration stored and adjustment of vessel personality files / application configuration stored in the memory of the ED-5/ED-7.
4. Engines – Used for source address setup of engines monitored by the ED-5/ED-7.
5. Gauge Ranges – Used to adjust the range of parameters monitored on the data screen page for ED-5/ED-7. The adjustment to the range defines the minimum and maximum value reported for the parameter on the display.
6. Local Time Offset – Used to adjust the difference in hours and minutes between UTC and the local time.
7. Backlight Level Presets – Used to adjust the backlight level presets for Dark Mode and Light Modes.
8. NMEA Switch Bank – Used to configure the remote keypad to use with the display.

Modifying ED-5/ED-7 settings in the Setup page can result in loss of functionality of the system. Accessing the Setup page is logged as an event in the ED-5/ED-7 internal memory event log.

![[15e00207.png]]

Setup - Connections

> [!note] Note · Примечание
> Initial Device Network Settings are controlled by the vessel personality file/Theme selected for the ED-5/ED-7 but can be impacted by other devices when the ED-4, or ED-5/ED-7 displays power on.

Action:

- Select “Connections”.
- Select options to enter for viewing or change.

When finished:

Swipe left to right on the screen or use “Back”(IV) soft key on the screen to exit or press “Return/Exit” key on remote keypad.

![[15e00208.png]]

Setup - Connections

There are four options under Connections settings:

1. CAN 1 Config

a. Typically associated to J1939 and used to select baud rate, set address and view existing device address and perform address claims. See below for more details.

> [!note] Note · Примечание
> Device Instance and System Instance setting are **not** required for modification, as modifying can impact device communication and data.

2. CAN 2 Config

a. Typically associated to National Marine Electronics Association (NMEA) 2000 but can also be used for J1939 and used to select baud rate, set address and view existing device address and perform address claims. See below for more details.

b. CAN channel is isolated type transceiver.

> [!note] Note · Примечание
> Device Instance and System Instance setting are **not** required for modification, as modifying can impact device communication and data.

3. UART Baud Rate

a. Used to setup the baud rate for UART protocol. At the time production UART protocol is **not** supported by ED-5/ED-7.

4. Analogue Inputs

a. Used to set when an analog input is required to be monitored with ED-5/ED-7. ED-5 / ED-7 has 1 spare analog input available for use.

![[15e00209.png]]

Device Network Settings - CAN Channel 1 Settings - J1939

- Baud Rate: Should always be set to match the ECM broadcast rate, which is typically 250K. If the baud rate setting is incorrect, the data on the ED-5/ED-7 data screen will be dashes.
- Seed Address: Used to manually set the source address of the ED-5/ED-7. The range of seed address is typically 128 or higher.
- Perform Address Claim: Used to save the seed address or preferred address manually selected.
- Actual Address: Address claimed by the ED-5/ED-7, which starts at the seed address or preferred address then increments to a unique address for each ED-5/ED-7 on a common network.
- System Instance: Used in an NMEA 2000 network to identify multiple similar products connected on the same network.
- Device Instance: Used in an NMEA 2000 network to identify multiple similar products connected on the same network.

![[15e00210.png]]

Connections - CAN Channel 2 Settings - NMEA 2000

- Baud Rate: Should always be set to match the ECM broadcast rate, which is typically 250K or when CAN transceiver is used for NMEA2000 typically baud rate is set at 250K. If the baud rate setting is incorrect, the data on the ED-5/ED-7 data screen will be dashes or NMEA2000 information gateway will **not** function.
- Seed Address: Used to manually set the source address of the ED-5/ED-7. The range of seed address is typically 128 or higher.
- Perform Address Claim: Used to save the seed address or preferred address manually selected.
- Actual Address: Address claimed by the ED-5/ED-7, which starts at the seed address or preferred address then increments to a unique address for each ED-5/ED-7 on a common network.
- System Instance: Used in an NMEA 2000 network to identify multiple similar products connected on the same network.
- Device Instance: Used in an NMEA 2000 network to identify multiple similar products connected on the same network.

![[15e00211.png]]

Connections – Analogue Inputs

The ED-5/ED-7 supports 1 spare analog input. The ED-5/ED-7 can be configured to monitor a resistive or a voltage sender.

The ED-5/ED-7 shows multiple Analogue Inputs for configuration, but the hardware only supports Analogue Input 1 for use.

![[15e00212.png]]

![[15e00213.png]]

Resistance or Voltage Input Mode Selection

Setup - Themes

ED-5/ED-7 setup and configuration settings are saved to the internal memory of the ED-5/ED-7, on the ED-5/ED-7 display vessel personality files are referred as Themes. The locally stored vessel personality file or themes are available for selection to use.

Action:

- Select “Setup”.
- Select “Themes”.

![[15e00214.png]]

There are two options under Themes:

1. Theme: This option defines the existing Vessel Personality file used on the display. The option is used to change and select the vessel personality file stored on the display.

Action:

- Select “Setup” using touchscreen or remote keypad.
- Select “Themes” using touch screen or remote keypad.
- Select “Theme” using touch screen or remote keypad.
- Select the vessel personality file from “Choose Theme” screen to use on the display.

When finished:

- Swipe left to right or use “Back”(IV) soft key on the screen to exit or press “Return/Exit” key on remote keypad to save the setting.

2. Adjust existing – Screens: This option allows adjustment of data screen, add new data screen and remove data screen.

![[15e00215.png]]

![[15e00216.png]]

Theme Selection in Theme Manager Menu

Theme Manager – Adjust existing – Screens

The display vessel personality files come pre-configured with default data screens available for each engine or application type. The available data screen is controlled by the theme or vessel personality file.

> [!note] Note · Примечание
> The screen layout parameter adjust can be done from data screen by pressing in the middle of data screen and following Step 5 below.

Action:

1. Select “Adjust Existing”.
2. Select “Screens”.
3. Select “Adjust Existing”.
4. Select screen layout to adjust parameter to display on the data screen.
5. Use “Prev” or “Next” to adjust parameter for the data screen.

![[15e00217.png]]

![[15e00218.png]]

Screens Menu in UEM Dual Engine Dashboard

![[15e00219.png]]

Adjust Setting Selection in Screen Manager

![[15e00220.png]]

Available Screen Selections in Screens Menu

![[15e00221.png]]

Parameter Adjustment

The settings are available to add a new screen layout “Add New” or remove available screen “Remove Existing” from the display configuration.

When finished:

- Swipe left to right to exit the menu or press “Return/Exit” key on remote keypad to save the setting.

![[15e00222.png]]

Setup – Engines

The vessel personality file controls most of the settings for each engine, though it is important to verify the settings.

The process outlined in Setup – Engines section can be used to setup each engine available on the Setup page.

Action:

- Select “Engines” using touch screen or remote keypad.
- If needed, select each option to change.

When Finished:

- Swipe left to right or use “Back”(IV) soft key on the screen to exit or press “Return/Exit” key on remote keypad to save the setting.

Setup – Engines

There are 3 options under the “Engines”:

1. Engine
2. Engine Settings
3. Perform Service

![[15e00223.png]]

Setup – Engines – Stbd (Engine)

Used to select the engine to monitor as per application types. The engine menu shows the list of engines based on the Vessel Personality File / Theme selected. The process outlined in Setup – Engines – Stbd (Engine) can be used to setup each engine available on the Engines Setup page.

Action:

- Select “Stbd” using touch screen or using remote keypad.

When Finished:

- Swipe left to right or use “Back”(IV) soft key on the screen to exit or press “Return/Exit” key on remote keypad to save the setting.

![[15e00224.png]]

Engine – Engine Source – Engine Settings

Action:

- Select “Engine Settings” using touch screen or using remote Keypad.

When Finished:

- Swipe left to right or use “Back”(IV) soft key on the screen to exit or press “Return/Exit” key on remote keypad to save the setting if changed.

![[15e00225.png]]

Engine Source (Stbd) - Engine Settings

There are several items in the ED-5/ED-7 Engine Settings page that can be accessed.

1. Engine Location Name
2. Source Address(s)
3. Supported PGN(s)
4. Senders and Conversions
5. User Alarms
6. Service Hours
7. Configure Trip Reset

![[15e00226.png]]

Engine (Stbd) – Source Addresses

![[15e00227.png]]

1. CAN Port 1

Action:

- Select “Source Address(s)” using touch screen or using remote keypad.
- Select “CAN Port 1” using touch screen or using remote keypad.

When Finished:

- Swipe left to right or use “Back”(IV) soft key on the screen to exit or press “Return/Exit” key on remote CAN keypad to save the setting if changed.

![[15e00228.png]]

2. CAN Port 2

- Used to enable or disable the ED-5/ED-7 transceiver. When enabled it allows to set restriction on source address for receiving data link when used for J1939 communication for twin J1939 twin engine ED-5/ED-7 display applications.
- CAN Port 2 is typically used for NMEA 2000.

Action:

- Select “Source Address(s)” using touch screen or using remote keypad.
- Select “CAN Port 2” using touch screen or using remote keypad.
- Select “Enable Port” to enable the ED-5/ED-7 transceiver.

When Finished:

- Swipe left to right or use “Back”(IV) soft key or press “Return/Exit” key on remote CAN keypad to exit and save the setting if changed.

![[15e00229.png]]

![[15e00230.png]]

Enable Port Selection in CAN Port 2 Menu

Engine (Stbd) – Supported PGNs

The selections in this page can be “Enabled” or “Disabled” and NMEA 2000 transmit instance is defined depending on if the component/sensor is broadcasting onto NMEA 2000.

Action:

- Select “Supported PGNs” using touch screen or using remote keypad.
- Select message to adjust using touch screen or using remote keypad.
- Select “Transmit CAN1” or “Transmit CAN2” to adjust “Enabled” or “Disabled” based on the application needs.
- Adjust the “Tx Instance”.

When Finished:

- Swipe left to right or use “Back”(IV) soft key on the screen to exit or press “Return/Exit” key on remote keypad to exit.

![[15e00231.png]]

![[15e00232.png]]

PGN List in Supported PGNs Menu

![[15e00233.png]]

Tx Instance Adjustment

Engine (Stbd) – User Alarms

Allows to enable and disable the alarm or lamps which are configured to trigger using display.

> [!note] Note · Примечание
> Modification of the alarm settings in User Alarms may cause loss of key functions. For instance, the Engine Protection Shutdown Override Indication triggered by display is enabled and available for configuration in the menu, modification of the Engine Protection Shutdown Override indication value would make display lose capability to indicate an override event.

Action:

- Select “User Alarms” using touch screen or using remote keypad.

When Finished:

- Swipe left to right or use “Back (4)” soft key on the screen or press “Return/Exit” key on remote keypad to exit.

![[15e00234.png]]

![[15e00235.png]]

User Alarms Menu

Engine (Stbd) – Service Hours

The feature allows to set a service interval notification after a pre-defined engine hours are accumulated.

Action:

- Select “Service Hours” using touch screen or using remote keypad.
- If needed enable the Service Hours feature, to enable select “Service Hours”.
- Set the service interval in the “Service Hours” field to set the engine hours for notification about a service event.

> [!note] Note · Примечание
> This feature is **not** enabled by default and is **not** to be confused as engine service interval.

Engine (Stbd) – Configure Trip Reset

The display configuration includes the message field associated to J1939 trip reset message which displays sends to ECM to perform trip reset operation. The operator is **not** expected to modify the fields of trip reset as modifying field can cause loss of trip reset command capability.

![[15e00236.png]]

![[15e00237.png]]

Trip Reset Configuration Menu

Setup - Backlight Level Presets

The display provides capability to toggle between Dark Mode and Light Mode. The Dark Mode is configured with lower backlight level to make it easier to see in low light. The Light Mode is configured with higher backlight level to make it easier to see in bright light.

Action:

- Select “Backlight Level Presets” using the touch screen or using remote keypad.
- Adjust the backlight level for “Dark Mode” or “Light Mode” using the increase or decrease buttons on touch screen or using right or left button on the remote keypad.

When finished:

- Swipe left to right or use “Back”(IV) soft key on the screen or press “Return/Exit” key on remote keypad to exit.

![[15e00238.png]]

![[15e00239.png]]

Backlight Level Presets Adjustment

Setup -\> NMEA Switch Bank

The display configuration includes the capability to configure the remote keypad, it provides capability to select the remote keypad from the NMEA Switch Bank menu. The keypad once connected to the display harness the keypad should appear in the default keypad list for selection. Once a remote keypad is selected the menu allows to identify the connected keypad device for situations when more than one keypad is available on the network.

The remote keypad has backlight LEDs configurable with different lighting mode available as:

- Off: LEDs remain off all the time.
- On: LEDs remain on all the time.
- On at low brightness: LEDs **only** light up when display backlight is lower than 20 percent or equal to 20 percent.
- On at high brightness: LEDs **only** light up when display backlight is above 20 percent.
- **Not** controlled: LEDs remain off all the time and is **not** controlled by the display backlight level.

Action:

- Select “Menu”.
- Select “Security”, enter valid security PIN.
- Select “Back”(IV) soft key on the screen to exit.
- Select “Setup”.
- Select “NMEA Switch Bank” using the touch screen.
- Select “Default Keypad” using the touch screen.
- Select “PKU2300M” using the touch screen.
- Select “Identify” to confirm the display is communicating with the remote keypad. The remote keypad will start blinking LEDs if communication is active.

When finished:

- Swipe left to right or use “Back”(IV) soft key on the screen to exit.

### Finishing Steps

ED-4

> [!warning] CAUTION · Осторожно
> After updating the software or vessel personality file in any control system component, verify that the Vessel Control System is completely operational.

Following a configuration update, if there is a new alarm code or performance complaint, follow the alarm code or the appropriate troubleshooting symptom tree to understand if the personality is working properly and is the appropriate personality for the application.

After ED-4 display configuration modification, refer to the following procedures for setup information and testing:

- It will be necessary to save the vessel personality file. Use the following procedure for information on vessel personalities. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15]].
- If needed for setup, use the following procedure. [[513-101-013 — General Operating Instructions|Refer to Procedure 101-013 in Section 1]].
- All control functionality of the Cummins® Marine Controls **must** be tested before leaving the dock after a service event. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15]].

ED-5 and ED-7

> [!warning] CAUTION · Осторожно
> After updating the software or vessel personality file in any control system component, verify that the Vessel Control System is completely operational.

Following a software or configuration update, if there is a new alarm code or performance complaint, follow the alarm code or the appropriate troubleshooting symptom tree to understand if the personality is working properly and is the appropriate personality for the application.

After ED-5/ED-7 display configuration modification, refer to the following procedures for setup information and testing:

- If needed for setup, use the following procedure. [[513-101-013 — General Operating Instructions|Refer to Procedure 101-013 in Section 1.]]
- All control functionality of the Cummins® Marine Controls must be tested before leaving the dock after a service event. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15.]]
