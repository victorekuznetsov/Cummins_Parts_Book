---
type: "Процедура"
doc: "513-015-035"
title_en: "Display(s) and Instrumentation"
modified: "2025-07-08"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
figures: 60
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-035.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-035.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Display(s) and Instrumentation

> [!abstract] Процедура · `513-015-035`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2025-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-035.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-035.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- USB extension cable, Part Number 5394862 (if needed for access).

#### Additional Service Items

- USB drive.

### General Information

The display used for the Marine C Command Connect and Connect Premier Panel System is called an ED-4/ED-5/ED-7. The ED-4 is required for the customer interface box (C.I.B.) in the premier option. The ED-4/ED-5/ED-7 at the helm is an option and some boat builders may choose **not** to use one. Original equipment manufacturers (OEM) have the option to use one or more ED-4s in multiple engine applications. The ED-4/ED-5/ED-7 has the ability to display multiple engine information at one time.

The ED-4/ED-5/ED-7 display is **only** supplied by Cummins Inc. and is designed to operate at nominal battery voltage of 12 or 24 volts.

The ED-4/ED-5/ED-7 display is connected to the engine control module (ECM) through a Society of Automotive Engineers (SAE) J1939 data link. The display will indicate engine operating parameters and fault codes. The display is the gateway for relaying engine ECM information to National Marine Electronics Association (NMEA) 2000, if equipped. The display requires a unique software load for the C Command Connect and Connect Premier Panel System and is **not** common with other Cummins® controls systems.

The display software name and version can be found in the “About” menu screen.

The display is preloaded with software and is updateable. The ED-4 display's software and vessel personality file **must** be updated for each vessel application at initial install by the OEM or, if replaced, during a service event. The ED-5/ED-7 display is preloaded with software and **only** requires selection of preloaded personality file/themes from the display.

Software and vessel personality file are loaded using the USB connection on the rear of the ED-4 /ED-5/ED-7.

ED-4

![[15e00022.png]]

ED-4 Display

Do **not** press the button (1) located below the USB port on the rear of the ED-4 display. Pressing the button may affect performance and software/vessel personality files loaded in the ED-4.

Use the following procedures for ED-4 recovery steps.

- [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]
- [[513-015-107 — Display Software|Refer to Procedure 015-107 in Section 15.]]

![[15e00154.png]]

Multifunction Display:

The multifunction display is connected with the engine ECM through a J1939 or NMEA 2000 data link.

The multifunction display will indicate engine operating parameters and fault information.

The multifunction display is typically **not** supplied by Cummins Inc. See equipment manufacturer service information for service, setup, or software updates.

![[15d00958.png]]

### Test

ED-4

The user can interact with the display through keys (1) through (5) on the front of the display.

The function of the key is shown on the ED-4 screen above the key, which changes as selections are made.

A variety of diagnostics can be performed with the ED-4 display.

![[00e00122.png]]

The Diagnostics page on the Main Menu page of the ED-4 display can be accessed by pressing key 5 or “Menu” on the data screen page.

Action:

- Press key 5 or “Menu”

When Finished:

- Press key 5 or “Exit” to return to the data screen page.

![[15e00080.png]]

There are a number of items in the ED-4 Diagnostics page that can be accessed.

1. Advanced Alarms – used for viewing additional details about alarms
2. Data Log and View – used to view and log data
3. Lamp Diagnostic – used to view lamps
4. Demo Data – places the display in demo mode
5. Demo Alarm - places the display in demo alarm mode.

> [!note] Note · Примечание
> Do **not** leave “Demo Data” or “Demo Alarm” selections enabled in the Diagnostics page. Doing so will cause false data and alarms messages to be shown on the ED-4 display data screen.

![[15e00081.png]]

Diagnostics - Advanced Alarms

To obtain more information on an alarm or to view all alarms received by the ED-4, go to the “Advanced Alarms” in the Diagnostics page.

> [!note] Note · Примечание
> Once a system fault is corrected, it may take up to 60 seconds for the alarm code to disappear on the ED-4 display.

![[00e00131.png]]

Diagnostics – Advanced Alarms

Typical information shown in the Advanced Alarms page:

1. Status and number of system faults
2. Description of the fault
3. SPN of fault
4. FMI of fault
5. Engine hours at the time the fault occurred **Note:** The engine hours will reset to current engine hours broadcasted by the ECM after a key cycle.
6. Cummins fault code (FC) or alarm code (AC) number
7. Source detecting the fault
8. Count of fault occurrences.

> [!note] Note · Примечание
> If the count of fault occurrences is **not** known, the value of 127 will be shown by the ED-4. This value will be seen for all alarm codes and generator faults.

Action:

- Select “Menu”, then “Diagnostics”, then “Advanced Alarms”.
- Press key 1 or “Previous” to scroll.
- Press key 2 or “Next” to scroll.

![[15e00083.png]]

Diagnostics - Advanced Alarms

Pressing key 4 or “DM2” in the “Advanced Alarms” page will populate the ED-4 with inactive faults codes saved by the engine ECM.

> [!note] Note · Примечание
> The DM2 alarms will appear as Active on the ED-4 screen, even though they are inactive in the engine ECM.

The DM2 messages shown on the ED-4 will disappear after approximately 2 minutes or after a system enable switch power cycle.

INSITE™ electronic service tool can be used to clear all inactive fault codes from the engine ECM.

When Finished:

- Press key 5 or “Close” to remove the alarm pop up message.
- Press key 5 or “Back” to exit the page.

![[15e00084.png]]

Diagnostics - Data Log and View

To data log or view data monitored by the ED-4, go to the “Data Log and View” in the Diagnostics page.

Action:

- Press key 4 or “Enter”.

When Finished:

- Press key 5 or “Back” to exit the page.

![[15e00085.png]]

Diagnostics - Data Log and View

There are a number of items in the ED-4 Data Log and View page that can be accessed.

1. CAN Viewer and Logger - used for viewing and logging controller area network (CAN) data link information.
2. Parameter Logger - used to view and log parameter data. This features is not enabled at product launch.
3. I/O Viewer - used to view OEM sensor input and output information.
4. Parameter Viewer - used to view data received from various components.

![[15e00086.png]]

Data Log and View - CAN Viewer and Logger

In the “Data Log and View” page, enter the “CAN Viewer and Logger” page.

Action:

- Press key 4 or “View"

After entering the page. CAN data can be viewed live on the display in real time.

In this page, ED-4 has the capability of viewing, logging, and exporting CAN data.

When Finished:

- Press key 5 or “Back” to exit the page.

![[15e00087.png]]

Data Log and View - CAN Viewer and Logger

To view basic information about the ED-4 CAN network, enter the “Stats” page.

Action:

- Press key 4 or “Stats”

After entering the page. CAN data can be viewed live on the display in real time.

CAN 1 is J1939 data link network.

CAN 2 is typically the NMEA 2000 data link network.

If there is an issue with the ED-4 or CAN data link network, there may be values other than 0 shown for Bit Error Count Rx (receive) and Bit Error Count Tx (transmit).

When Finished:

- Press key 5 or “Back” to exit the page.

![[15e00088.png]]

Data Log and View - CAN Viewer and Logger

Data logging is helpful for determining if the J1939 and/or NMEA 2000 network is working properly.

> [!note] Note · Примечание
> It is important to verify the gateway ED-4 is receiving J1939 messages from the engine ECM before using ED-4 data logging to troubleshoot NMEA 2000 or J1939 issues at the MFD.

When logging, the data is stored on the ED-4 up to 20,000 frames.

- It is important to log and export CAN data from the ED-4 that is set up as the gateway for the J1939 and/or NMEA 2000 data or receiving and/or transmitting J1939 data. On the C Command Connect Premier option, the gateway will **always** be the ED-4 in the C.I.B. Enter the ED-4 Configuration page to determine if the ED-4 is set up as a gateway for the system.

![[15e00087.png]]

Data Log and View - CAN Viewer and Logger

To log CAN data:

- Press key 3 or “Record”
- If troubleshooting CAN data link issues, it is recommended to allow the ED-4 to capture 20,000 frames of data before pressing key 3 or “Stop”. The ED-4 will automatically stop recording after 20,000 frames, which is approximately 2 minutes. If additional datalogging is needed to capture an event, the record key will need to be pressed again.
- The log file will save to the ED-4 internal memory.

![[15e00087.png]]

To extract the log, insert a USB drive into the back of the ED-4.

Once the USB drive is detected by the ED-4:

- Press key 2 or “Down” and select “Extract Log(s)”.
- Press key 4 or “Save”.
- When finished, press Key 5 or “Eject”.

The log file will be saved in the “LOGS” folder automatically created on the USB drive.

> [!note] Note · Примечание
> It is recommend to save and remove log files from the LOGS folder on the USB drive before exporting log files from the ED-4.

![[15e00091.png]]

The saved log file(s) can be analyzed.

Log files are compressed into a zip file on the USB drive called "Logs\_XXXXX.zip".

- Extract the zip file using a decompression tool such as WinZip™ or comparable software.

The XXXXX in "Logs\_XXXXX.zip" and "Canlog\_XXXXX\_\#.asc" represents the software serial number for the ED-4 from which the CAN log was exported.

The \# in "Canlog\_XXXXX\_\#.asc" represents the order in which the CAN logs were created. For example, the first CAN log file saved will be "CAN\_XXXXX\_1.asc" and the second one saved will be "Canlog\_XXXXX\_2.asc" and so on.

It is important to utilize the most recent index log file for analysis of the signals being broadcast.

> [!note] Note · Примечание
> The date and time stamp on the log files will **not** be correct since the ED-4 is **not** capable of determining the actual date and time.

![[15e00090.png]]

To analyze the data, open the "Canlog\_XXXXX\_\#.asc" file(s) in Excel and perform the following data format.

1. Select “Delimited”
2. Select “Space Delimited”.

![[15e00093.png]]

After formatting, review the data in Excel.

1. CAN Network Fields
2. PGN Fields.

It is possible to examine the logged data stored in the ASC file and determine if the parameter is being transmitted appropriately from the ED-4 gateway to the NMEA 2000 network and J1939.

Example:

To determine if the “Transmission” parameters are being broadcast properly on CAN NMEA 2000 network, hold down the Control key in Excel and press F to perform a search for “F205”. If this parameter is **not** found in the spreadsheet, then the ED-4 is **not** broadcasting the transmission parameters properly. Load the appropriate VPF into the ED-4 to be sure that the network settings are set up correctly for the vessel.

If all parameters are being broadcast correctly, then the OEM MFD is either **not** configured properly or there is an issue in the OEM NMEA 2000 or J1939 wiring to the MFD.

![[15e00094.png]]

Review the data in Excel.

1. CAN Network Fields
2. PGN Fields.

CAN Message Example (all hex values): XX **F004** \#\#.

- The "XX" prior to the PGN number includes the priority of the message. This is any two digit number, followed by 4 digit PGN.
- The 4 digit PGN number is valuable for determining if the ED-4 is broadcasting the signal properly.
- The \#\# after the PGN number represents the two digit address number of the J1939 or NMEA 2000 device which are broadcasting the signals.

| **CAN Network Fields(0 = CAN1)** (**1 = CAN2)** | **CAN Message(XX =** | **Parameter Information** |
|---|---|---|
| 0 | XXF004\#\# | Engine Parameters |
| 0 | XXFECA\#\# | DM1 (Diagnostic Message 1) |
| 0 | XXF10D\#\# | Rudder Angle |
| 0 | XXFEF8\#\# | Transmission |
| 0 | XXFEFC\#\# | Fuel Level |
| 1 | XXF200\#\# | Engine Parameters |
| 1 | XXF201\#\# | Engine Parameters |
| 1 | XXF10D\#\# | Rudder Angle |
| 1 | XXF205\#\# | Transmission |
| 1 | XXF211\#\# | Fuel Level |

If parameter information is **not** found in the log file, troubleshoot by determining if the correct VPF file is loaded in the ED-4 and there are **not** issues with the J1939 data link.

If parameter information is found in the log file, consult the OEM for troubleshooting support of the MFD.

> [!note] Note · Примечание
> Some MFDs may **not** be compatible or capable of receiving CAN message information from the ED-4.

![[15e00094.png]]

Data Log and View - Parameter Logger

Parameter Logger functionality is **not** enabled at time of product launch.

![[15e00096.png]]

Data Log and View - I/O Viewer

In the “Data Log and View” page, enter the “I/O Viewer” page.

Action:

- Press key 4 or “View.
- Press key 2 or “Next” to view the available sensor information.

After entering the page, OEM sensor data can be viewed live on the display in real time.

The units in the Parameter Viewer page are fixed and are **not** impacted by the user Units selection setting. All pressure values are absolute.

> [!note] Note · Примечание
> There is a pressure difference reading of approximately 2 kPa \[0.29 psi\] between C.I.B. ED-4 and Helm ED-4 due to message broadcast tolerances.

When Finished:

- Press key 5 or “Back” to exit the page.

![[15e00097.png]]

Data Log and View - I/O Viewer

The following information is available on the I/O viewer page and can be useful during troubleshooting. The VPF controls the functionality and vessel sensor set up parameters displayed on the page.

1. Input or output designated with a component/sensor name for the parameter.
2. The connector and pin location on the back of the ED-4 that the sensor is pinned to. See the C Command Connect wiring diagram to determine the ED-4 pin connector location to the C.I.B.
3. Measurement Mode
4. Raw Value - the data value the ED-4 is receiving. If dashes are seen, then the ED-4 is **not** receiving signal data from the component/sensor.
5. Raw value destination information of the data. If dashes are seen, then the ED-4 is **not** passing signal data for the component/sensor.
6. Output - component/sensor range.

Use the following procedure for accessing sensor information contained in the VPF. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15]]. The Cummins® Marine Application Engineering group creates the VPF and updates the Cummins® INCAL™ disc or drive folder “Cummins ED-4 Display Vessel Personality File Tracking Sheet” with file name, version, and description of the vessel, application, equipment, and vessel sensor information.

![[15e00098.png]]

Data Log and View - I/O Viewer

The process below can be performed to confirm the ED-4 chip has **not** failed and the analog input channels are working properly.

Action:

1. Power up the ED-4 with the Secondary connector unplugged from the rear of the ED-4.
2. Press key 5 or “Menu”.
3. Scroll to "Configuration" and press key 4 or "Enter".
4. Press key 1 or "Accept" on the Warning screen.
5. Scroll to "IO Configuration" and press key 4 or "Enter".
6. Scroll to option "AI6-Custom 1" and press key 4 or "Enter".
7. Scroll to "Resistance (0-500)" and press key 4 or "Enter" to turn “On” the setting.
8. Press key 5 or “Back” to the Main Menu Screen.
9. Access “I/O Viewer” page under “Menu -\> “Diagnostics” -\> “Data Log and View”.
10. Scroll to “I/O Viewer” press key 4 or “View”.
11. Press key 2 or “Next” to "AI6-Custom 1" I/O Viewer page.
12. Confirm that “Measurement Mode, Resistance” is seen. Check that the raw value for resistance seen is approximately 1100 ohms. If the raw resistance value is below 1000 ohms, this would typically indicate a failed ED-4 display with analog I/O issues. The normal open circuit resistance on analog input pins for a known good ED-4 is typically above 1100 ohms.
13. Change back the “AI6-Custom 1” setting made in Step 7 by following the next steps.
14. Press key 5 or “Back” to the Main Menu Screen.
15. Scroll to "Configuration" and press key 4 or "Enter".
16. Press key 1 or "Accept" on the Warning screen.
17. Scroll to "IO Configuration" and press key 4 or "Enter".
18. Scroll to option "AI6-Custom 1" and press key 4 or "Enter".
19. Select "Off" and press key 4 or "Enter".

When Finished:

- Press key 5 or “Back” to return to the Menu page.
- Press key 5 or “Exit” to return to the data screen page.

![[15e00099.png]]

Data Log and View - Parameter Viewer

In the “Data Log and View” page, enter the “Parameter Viewer” page.

The number in the bracket (1) signifies the engine or device the parameter data signal is being received from.

The number is in sequence to the engines listed on the ED-4 “Configuration” page. For example, if Stbd and Port are listed, then Stbd is device 1 and Port is device 2 on the parameter viewer page.

Action:

- Press key 4 or “View.
- Press key 2 or “Next” to view parameters.
- Press key 4 or “Device” to view the parameters for the different engines/devices the ED-4 is monitoring. Use the following procedure to determine the ED-4 setup. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15.]]

When Finished:

- Press key 5 or “Back” to exit the page.

![[15e00100.png]]

The tank profile can be configured if the fluid tank is being monitored through the ED-4.

The fluid tank profile can be changed by pressing key 5 or “Menu” on the data screen page.

#### Action

- Press key 5 or “Menu”
- Select “Configuration” and press key 4 or “Enter"
- Press key 1 or “Accept”
- Select “Device and press key 4 or “Enter” (NOTE: Device could be any of Starboard, Port, Starboard-Outer, Port-Inner)
- Select “Tank Profile” and press key 4 or “Enter"
- Select appropriate fluid to be configured
- Press key 4 or “Setup"
- Press key 4 or “Start".

The fuel, engine oil, coolant, fresh water, wastewater and black water tanks can be configured with the ED-4, if vessel permits.

A message will appear on the ED4 display which will ask to confirm tank is empty before proceeding configuration.

![[15e00189.png]]

The fluid tank profile can be changed by pressing key 5 or “Menu” on the data screen page, if configured tank levels are known at 25%, 50% & 75% of tank capacity. The fuel, engine oil, coolant, fresh water, wastewater and black water tanks can be configured with the ED-4, if vessel permits and VPF supports the input for configuration.

#### Action:

- Press key 5 or “Menu”
- Select “Configuration” and press key 4 or “Enter”
- Press key 1 or “Accept"
- Select “Device” and press key 4 or “Enter” (NOTE: Device could be any of Starboard, Port, Starboard-Outer, Port-Inner)
- Select “Tank Profile” and press key 4 or “Enter”
- Select fluid type to be configured
- Press key 4 or “Setup”
- Press key 2 or “Down"
- Press key 4 or “Start”
- Select “Tank Volume"
- Press key 4 or “Inc” and key 3 or “Dec” to enter “Tank Volume"
- Press key 2 or “Down"
- Press key 4 or “Inc” and key 3 or “Dec” to enter 25% tank level known at “Point 1”
- Press key 2 or “Down"
- Press key 4 or “Inc” and key 3 or “Dec” to enter 50% tank level known at “Point 2”
- Press key 2 or “Down”
- Press key 4 or “Inc” and key 3 or “Dec” to enter 75% tank level known at “Point 3"

If equipped, the brightness of the ED-4 display can be changed by pressing key 3 or “Function” on the data screen page.

#### Action:

- Press key 3 or "Function"
- Press key 3 or "Dimmer"
- Press key 4 or "Brighter"

The percent brightness of the display is shown in the Brightness row and ranges from 10 to 100%.

Press key 5 or “Exit” to save the setting and exit the brightness setting.

![[15e00190.png]]

If equipped, the trip reset of the ED-4 can be changed by pressing key 3 or “Function” on the data screen page.

#### Action:

- Press key 3 or "Function"
- Press key 2 or "Down"
- Press key 4 of "Choose"
- Press key 4 or "Send"

If feature is available, pressing “send” will reset the trip information. A warning message will appear after pressing “Send” to notify that the trip reset message was sent.

Press key 5 or “Back” to save the setting and exit the trip reset setting.

![[15e00191.png]]

Data Log and View - Parameter Viewer

The software controls the parameters displayed on the page; therefore, some parameters may or may **not** be representative of the product the system is connected to.

At the time of product launch, the Parameter Viewer page contains all parameters the ED-4 is capable of monitoring; It is **not** tailored for each marine application.

After entering the page, parameter data can be viewed live on the display in real time and can be useful during troubleshooting. If dashes are seen, then the ED-4 is **not** receiving signal data for the parameter. Possible data signal issues may include an issue with the component or an issue with the data link.

The units in the Parameter Viewer page are fixed and are **not** impacted by the user Units selection setting. All pressure values are absolute.

> [!note] Note · Примечание
> There is a pressure difference reading of approximately 2 kPA \[0.29 psi\] between CIB ED-4 and Helm ED-4 due to message broadcast tolerances.

![[15e00101.png]]

ED-5 and ED-7

The user can interact with the display touch screen or through remote keypad installed standalone near the display.

The function of the display touch screen and remote keypad.

1. Press in the middle of the data screen to open the Menu page or press on the “Menu”(I) soft key to open the Menu page.
2. Press any space of the data screen to open the data screen edit page.
3. Swipe from right to left or left to right when on the data screen to scroll.
4. Swipe from left to right on the screen when in the Menu structure to return to last page or exit the menu or press on the “Back”(IV) button on the data screen to return to the last page.
5. Press on the “Alarm”(III) soft key to open the Alarms page.
6. Press “Backlight”(II) soft key to open the backlight control page.

![[00e00328.png]]

![[00u00146.png]]

1. Key 1 (Up) - Press key 1 to scroll up.
2. Key 2 (Left) – Press key 2 to scroll left.
3. Key 3 (Enter / Select) –
4. Key 4 (Down) - Press key 4 to scroll down.
5. Key 5 (Right) - Press key 5 to scroll right.
6. Key 6 (Return / Exit) - Press key 6 to exit screen prompts, exit screen editor, exit menu page or to go back to previous menu level and while on data screen press key 6 once to enter the active alarm page.
7. Hold Key 1 (Up) and Key 4 (Down) for 3 seconds to access the soft keys on the screen. Once the soft keys are highlighted using key 3 (Enter / Select) to access the function.

A variety of diagnostics can be performed with the ED-5/ED-7 display.

The Diagnostics page is part of the advanced settings and is protected by a security PIN. The Main Menu page of the ED-5/ED-7 display can be accessed by pressing the middle of the data screen page or use “Menu”(I) soft key on the screen or press and hold key 3 or “Select/Enter” on the remote keypad.

Action:

- Press the middle of the data screen page or press and hold key 3 or “Select/Enter” on the remote keypad.
- Select “Security”, then “Change Level”, then “Diagnostic” or use the remote keypad to scroll through menu and selection.
- Enter the “Security PIN”. Default security PIN to access advanced settings is “1919”.
- Swipe right to left to access the Diagnostics page.

Sharing the default security PIN without proper knowledge can lead to unintended changes causing loss or erratic function.

The security PIN entry on the display is **only** available using touchscreen and cannot be performed using CAN keypad.

When Finished:

- Swipe from left to right when in the Menu structure to exit to the data screen page.

![[00e00330.png]]

![[00e00331.png]]

Security Pin Entry

![[00e00332.png]]

Diagnostics Page

There are number of items in the ED-5 and ED-7 Diagnostics page that can be accessed.

1. CAN Viewer – used to view and log data
2. DB Viewer – used to view data
3. Alarm Viewer – used for viewing additional details about alarms
4. Device Information – used to devices on the network
5. Demo Data – places the display in demo mode

Do **not** leave “Demo Data” selections enabled in the Diagnostics page. Doing so will cause false data and alarms messages to be shown on the ED-5/ED-7 display data screen.

![[00e00333.png]]

CAN Viewer

CAN Viewer data logging is helpful for determining if the J1939 and/or NMEA 2000 network is working properly.

It is important to verify the gateway ED-5/ED-7 is receiving J1939 messages from the engine ECM before using ED-5/ED-7 data logging to troubleshoot NMEA 2000 or J1939 issues at the MFD.

When logging, the data is stored on the ED-5/ED-7 up to 40,000 frames.

- It is important to log data from the ED-5/ED-7 set up as the gateway for receiving the J1939 data.

![[00e00334.png]]

Data Log and View - CAN Viewer and Logger

To log CAN data:

- Select “Logger”, then “Save to display”.
- Press key 3 or “Record”
- If troubleshooting CAN data link issues, it is recommended to allow the ED-5/ED-7 to capture 40,000 frames of data before pressing key 3 or “Stop”. The ED-5 and ED-7 will automatically stop recording after 20,000 frames, which is approximately 2 minutes. If additional datalogging is needed to capture an event, the record key will need to be pressed again.
- The log file will save to the ED-5 and ED-7 internal memory.

![[00e00335.png]]

To extract the log, insert a USB drive into the back of the ED-5/ED-7.

Once the USB drive is detected by the ED-5/ED-7:

- Select “Offload Log(s)”.
- When finished, exit the USB Detected screen by swiping left to right.

The log file will be saved in the “1536-Serial Number” folder automatically created on the USB drive. Serial Number is unique to device and can be accessed from “About” screen.

The saved log file(s) can be analyzed.

Log files are stored into a folder on the USB drive called “1536-Serial Number”.

The CAN log file saved will be “canLog.asc”.

![[00e00336.png]]

To analyze the data, open the “canLog.asc” file(s) in Excel and perform the following data format.

1. Select “Delimited”.
2. Select “Space Delimited"

![[00e00337.png]]

After formatting, review the data in Excel.

1. CAN Network Fields
2. PGN Fields.

If all parameters are being broadcast correctly, then the OEM MFD is either **not** configured properly or there is an issue in the OEM NMEA 2000 or J1939 wiring to the MFD.

![[00e00338.png]]

Review the data in Excel.

1. CAN Network Fields
2. PGN Fields.

CAN Message Example (all hex values): XXF004\#\#.

- The "XX" prior to the PGN number includes the priority of the message. This is any two digit number, followed by 4 digit PGN.
- The 4 digit PGN number is valuable for determining if the ED-5 and ED-7 is broadcasting the signal properly.
- The \#\# after the PGN number represents the two digit address number of the J1939 or NMEA 2000 device which are broadcasting the signals.

| CAN Network Fields (1 = CAN1) (2 = CAN2) | CAN Message (XX =) | Parameter Information |
|---|---|---|
| 1 | XXF004\#\# | Engine Parameters |
| 1 | XXFECA\#\# | DM1 (Diagnostic Message 1) |
| 1 | XXF10D\#\# | Rudder Angle |
| 1 | XXFEF8\#\# | Transmission |
| 1 | XXFEFC\#\# | Fuel Level |
| 2 | XXF200\#\# | Engine Parameters |
| 2 | XXF201\#\# | Engine Parameters |
| 2 | XXF10D\#\# | Rudder Angle |
| 2 | XXF205\#\# | Transmission |
| 2 | XXF211\#\# | Fuel Level |

If parameter information is not found in the log file, troubleshoot by determining if the correct configuration is loaded in the ED-5/ED-7 and there are **not** issues with the J1939 data link.

If parameter information is found in the log file, consult the OEM for troubleshooting support of the MFD.

> [!note] Note · Примечание
> Some MFDs may **not** be compatible or capable of receiving CAN message information from the ED-5/ED-7.

Diagnostics - Advanced Alarms

To obtain more information on an alarm or to view all alarms received by the ED-5/ED-7, go to the “Advanced Alarms” in the Diagnostics page. Once a system fault is corrected, it can take up to 60 seconds for the alarm code to disappear on the ED-5/ED-7 display.

![[00e00339.png]]

Diagnostics – Alarm Viewer

Typical information shown in the Alarm Viewer page:

1. Status and number of system faults
2. Description of the fault
3. SPN/FMI of fault
4. Cummins® fault code (FC) or alarm code (AC) number
5. Source detecting the fault
6. Engine hours at the time the fault occurred
7. Occurrence Count
8. Manufacturer Information
9. Duration since alarm become active

The engine hours and duration since alarm become active will reset to current engine hours broadcasted by the ECM after a key cycle and duration time after a key cycle.

> [!note] Note · Примечание
> If the count of fault occurrences is **not** known, the value of 127 will be shown by the ED-5 and ED-7. This value will be seen for all alarm codes and generator faults.

Action:

- Select “Menu”, then “Diagnostics”, then “Alarm Viewer”.
- Press “Prev” to scroll.
- Press “Next” to scroll.

![[00e00340.png]]

Diagnostics - Alarm Viewer

- Pressing “Historic” in the “Alarm Viewer” page.
- Pressing “Req.” will populate the ED-5/ED-7 with inactive faults codes saved by the engine ECM.

The DM2/DM54 alarms will appear as Active on the ED-5/ED-7 screen, even though they are inactive in the engine ECM.

The DM2/DM54 messages shown on the ED-5/ED-7 will disappear after approximately 2 minutes or after a system enable switch power cycle.

INSITE™ electronic service tool can be used to clear all inactive fault codes from the engine ECM.

When Finished:

- Swipe from left to right or when in the Menu structure or “Return/Exit” button on the remote keypad to exit to the data screen page.

![[00e00341.png]]

Diagnostics – DB Viewer

To view data monitored by the ED-5/ED-7, go to the “DB Viewer” in the Diagnostics page. The number in the parenthesis signifies the engine or device the parameter data is being received from.

The number is in sequence to the engines listed on the ED-5/ED-7 “Setup” page. For example, if Stbd and Port are listed, then Stbd is device 2 and Port is device 1 on the parameter viewer page.

Action:

- Select “DB Viewer” using touch screen or “Select/Enter” button on the remote CAN keypad.
- Use up and down button to scroll through the list of parameters.
- Press “Change Instance” to view the parameters for the different engines/devices the ED-5/ED-7 is monitoring. Use the following procedure to determine the ED-5/ED-7 setup. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15.]]

When Finished:

- Swipe from left to right or use “Back”(IV) button on the screen or when in the Menu structure or “Return/Exit” button on the remote keypad to exit to the data screen page.

![[00e00342.png]]

![[00e00343.png]]

DB Viewer Screen and Parameters

Diagnostics – Device Information

To view other devices connected on the CAN network with the ED-5/ED-7, go to the “Device Information” in the Diagnostics page. The page shows the options for CAN1 and CAN2 to view list of other devices, respective source address and manufacturer identifier.

Action:

- Select “Device Information” using touch screen or “Select/Enter” button on the remote keypad.
- Select “CAN1” using touch screen or “Select/Enter” button on the remote keypad.

When Finished:

- Swipe from left to right or use “Back”(IV) button on the screen or when in the Menu structure or “Return/Exit” button on the remote keypad to exit to the data screen page.

![[00e00344.png]]

![[00e00345.png]]

Device Information Page

Brightness Control

The brightness of the ED-5/ED-7 display can be changed by pressing in the middle of the data screen page or pressing the “Backlight”(II) soft key on the data screen or press and hold “Select/Enter” button of the remote keypad while on the data screen page. The brightness control feature includes configurable backlight levels as “Dark Mode” and “Light Mode”. The “Dark Mode” is pre-configured as 20 percent and “Light Mode” is pre-configured as 90 percent.

Action:

- Press “Preferences” or select “Preferences” using the remote keypad.
- Press “-“ to decrease the brightness level.
- Press “+” to increase the brightness level

![[00e00346.png]]

![[00e00347.png]]

Adjusting Brightness Settings

The brightness of the display is shown in the Backlight row and ranges from 10 to 100 percent, with 10 percent being minimum brightness level and 100 percent being maximum brightness level.

Swipe left to right or press “Back”(IV) button on the screen or press “Return/Exit” key to save the setting and exit the brightness setting.

> [!note] Note · Примечание
> The brightness change when performed on ED-4 and change is transmitted to ED-5/ED-7, the brightness level on ED-5 / ED-7 can show differently considering the difference in the display hardware's.

Trip Information

The trip reset function can be accessed from the Diagnostics page.

Action:

- Press the middle of the data screen page or press & hold key 4 or “Select/Enter” on the remote keypad.
- Select “Trip Information”(VII) or use the remote keypad to scroll through menu for selection.
- Select device to access trip information received from the device.
- Select “Trip Information Reset” to send trip reset message.

If feature is available, pressing “send” will reset the trip information. A warning message will appear after pressing “Send” to notify that the trip reset message was sent.

Swipe left to right or use “Back”(IV) button on the screen or press “Return/Exit” key to save the setting and exit the trip information.

![[00e00348.png]]

![[00e00349.png]]

Trip Information Selection Screen

![[00e00350.png]]

Trip Information Reset Screen

### Preparatory Steps

ED-4

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Document display software. [[513-015-107 — Display Software|Refer to Procedure 015-107 in Section 15.]]
- Document and save VPF. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15]].
- Check the configuration information. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15]].
- Check the general operating instructions settings. [[513-101-013 — General Operating Instructions|Refer to Procedure 101-013 in Section 1]].
- Remove the ED-4 display from the C.I.B., if required. Refer to Procedure 015-023 in Section 15.
- Disconnect the batteries. See equipment manufacturer service information.

ED-5 and ED-7

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Document display software. [[513-015-107 — Display Software|Refer to Procedure 015-107 in Section 15.]]
- Document and save VPF. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]
- Check the configuration information. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15.]]
- Check the general operating instructions settings. [[513-101-013 — General Operating Instructions|Refer to Procedure 101-013 in Section 1.]]
- Disconnect the batteries. See equipment manufacturer service information.

### Remove

ED-4

Disconnect the harness connectors from the ED-4 display.

1. Primary (gray)
2. Secondary (black).

![[15e00151.png]]

Remove the plastic mounting stud nuts.

Remove the ED-4 from the helm.

> [!note] Note · Примечание
> It is recommended that the plastic studs and nuts are used to mount the ED-4 to the helm. If different mounting hardware is used, it is important to use the proper length screws for mounting the ED-4. The ED-4 will be damaged if too long of screws are used.

![[15e00103.png]]

ED-5 and ED-7

Disconnect the harness connectors from the ED-5/ED-7 display.

1. CAN1.
2. AUX.

Remove the plastic mounting stud nuts.

Remove the ED-5/ED-7 from the helm.

It is recommended that the plastic studs and nuts are used to mount the ED-5/ED-7 to the helm. It is **not** recommended to use different mounting hardware as the unit will be damaged due to long screws.

![[00j00457.png]]

### Inspect

Inspect the ED-4 and mounting seal.

Replace the ED-4 if damaged.

Damage to the mounting seal may be due to improper installation at the helm mounting location or mounting surface condition.

![[15e00068.png]]

### Install

ED-4

Insert the ED-4 into the helm opening.

Secure the ED-4 with the plastic mounting studs and nuts. Do **not** over-tighten the nuts. Hand-tighten **only**.

> [!note] Note · Примечание
> It is recommended that the plastic studs and nuts are used to mount the ED-4 to the helm. If different mounting hardware is used, it is important to use the proper length screws for mounting the ED-4. The ED-4 will be damaged if too long of screws are used.

> [!note] Note · Примечание
> The ED-4 installed in the CIB requires unique fasteners that **must** be reused. Use the following procedure for installation information. Refer to Procedure 015-023 in Section 15.

![[15e00103.png]]

Inspect the harness connectors before installation.

Connect the harness connectors to the ED-4 display.

1. Primary (gray)
2. Secondary (black).

Verify the harness connections are **not** excessively stressed.

![[15e00151.png]]

ED-5 and ED-7

Insert the ED-5/ED-7 into the helm opening.

Secure the ED-5/ED-7 with the plastic mounting studs and nuts. Do **not** overtighten the nuts. Hand-tighten **only**.

![[00j00458.png]]

Inspect the harness connectors before installation.

Connect the harness connectors to the ED-5/ED-7 display.

1. CAN1.
2. AUX.

Verify the harness connections are **not** excessively stressed and **not** overtighten the connections to the display.

![[00j00457.png]]

### Finishing Steps

ED-4

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Install the ED-4 display onto the C.I.B., if removed. Refer to Procedure 015-023 in Section 15.
- Connect the batteries. See equipment manufacturer service information.
- If the ED-4 display is replaced, the display software and VPF **must** be updated.
- Check the configuration information. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15.]]
- Check the general operating instructions settings. [[513-101-013 — General Operating Instructions|Refer to Procedure 101-013 in Section 1]].
- Perform system test to verify proper function. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15.]]

ED-5 and ED-7

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. See equipment manufacturer service information.
- If the ED-5/ED-7 display is replaced, the display software and VPF **must** be updated.
- Check the configuration information. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15.]]
- Check the general operating instructions settings. [[513-101-013 — General Operating Instructions|Refer to Procedure 101-013 in Section 1.]]
- Perform system test to verify proper function. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15.]]
