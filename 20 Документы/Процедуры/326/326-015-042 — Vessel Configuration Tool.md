---
type: "Процедура"
doc: "326-015-042"
title_en: "Vessel Configuration Tool"
modified: "2020-01-24"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-042.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-042.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/326"
---

# Vessel Configuration Tool

> [!abstract] Процедура · `326-015-042`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4358378 — Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick Marine Con|4358378]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2020-01-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-042.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-042.pdf)

### General Information

The Cummins® Inboard Joystick must be tuned to the vessel it is installed in for maximum performance. Vessel joysticks come with a preloaded default personality file when ordered from the factory. New joysticks have to be updated with a tuned vessel personality file that is specific to the vessel's original equipment manufacturer (OEM) and model. It is necessary to load the most current vessel personality for the vessel. The vessel configuration tool provides the ability to upload and download personality files into a vessel's joystick. Use the following procedure to find and select vessel personalities. [[326-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]

A new version of the configuration tool has been released for the Cummins® Inboard Joystick system. Version 3 and greater is now the existing version of the tool which replaces the legacy Version 2 and older.

![[ck800wa.png]]

### Setup Information

The following equipment is needed to connect to the inboard joystick system to manage vessel personalities.

#### Option 1:

1. Compatible laptop
2. JOYSTICKCONFIG-SERVICE electronic service tool
3. USB to RS232 serial adapter cable, Cummins® Part Number 5299129
4. USB to RS232 serial adapter cable driver.

#### Option 2:

1. Compatible laptop
2. JOYSTICKCONFIG-SERVICE electronic service tool
3. PS3USBUSB to serial adapter
4. Universal serial extension cable.

The JOYSTICKCONFIG-SERVICE electronic service tool can be found at INSITE.CUMMINS.COM in the related tools section of the website or on the Cummins® software shelf under the name JOYSTICKCONFIG-SERVICE.

The JOYSTICK USB to RS232 serial adapter cable driver can be found on the Cummins® software shelf. Alternately, the computer administrator can install the driver which is preloaded into the USB to RS232 serial adapter cable, Cummins® Part Number 5299129.

If **not** using cable Part Number 5299129, an alternate cable, PS3USBUSB to Serial Adapter, can be found on the Cummins® hardware shelf. The alternate cable will automatically install the necessary driver to a Cummins® laptop. A universal serial extension cable **must** be used with the alternate cable in option 2.

The serial adapter cable plugs into a USB port on the laptop. The opposite end of the cable plugs into the thruster interface data harness service tool connection. This connection is located near the thruster interface module.

For laptop compatibility requirements, reference INSITE.CUMMINS.COM.

> [!note] Note · Примечание
> For Cummins® employees, all software should be downloaded from the Cummins® software shelf, keyword search 'joystick'.

![[ck800wa.png]]

### Troubleshooting

With Version 2 and Older Configuration Tool

If unable to connect with the tool, try the following:

1. Before opening the program, leave the adapter cable plugged in for one minute to allow time for the computer to recognize the cable.
2. Verify the key powering the Cummins® electronic throttle shift and Cummins® inboard joystick system is ON.
3. Verify the lights on the lever control station and inboard joystick are illuminated.
4. Verify the adapter cable is plugged in securely.
5. Verify the correct COM port is selected.
6. Verify the driver for the cable is properly installed.
7. Verify the thruster interface module is connected and receiving power. This can be achieved by briefly activating the thruster in either direction by moving the joystick lever.

![[15900067.png]]

If a "Configuration Tool is **not** compatible with this joystick!" message results, the JOYSTICKCONFIG-SERVICE electronic service tool version loaded on the laptop is incorrect for supporting the Cummins® inboard joystick. Reference the "Setup Information" above.

![[15900115.png]]

If **not** sure which inboard joystick the tool is connected to, try the following:

1. Click on the “Identify Joystick” (6) button to verify connection between the tool and inboard joystick. After clicking the button, the inboard joystick LED lights will flash in a circular pattern for 30 seconds.

![[15900116.png]]

If unable to download a personality file, try the following:

1. Close the program, key OFF, and unplug the adapter cable. Follow the connection steps a second time.

If connection to the Cummins® electronic throttle shift and Cummins® inboard joystick system is lost, the message box to the right will display. Try the following:

1. Close the program, key OFF, and unplug the adapter cable. Follow the connection steps a second time.

![[15900082.png]]

If reading a personality file from a computer or joystick and a “File read Failed!” or "Error" message results, try the following:

1. Verify the file has a.jst extension.
2. Get the file from the Marine Panel Firmware Updates - Cummins Inboard Joystick webpage or functional joystick on the vessel, save to a computer, and try again. The file may have become corrupt or may have been modified. Files modified from an unauthorized source will **not** read correctly and can **not** be downloaded into a joystick.

> [!note] Note · Примечание
> [https://quickserve.cummins.com/qs3/qsol/service/marine/mpf\_joystick.html](https://quickserve.cummins.com/qs3/qsol/service/marine/mpf_joystick.html)

![[15900083.png]]

If while using the tool and a “The COM Port is either not open or malfunctioning. Please fix the problem, then run the Joystick Programmer.” If a “Data Read Failed!”, “Data Write Failed!”, “Couldn't Connect to Joystick ID”, “Couldn't get settings from Joystick!”, “No Joysticks Detected! No Configuration Possible”, “Cannot use this joystick because the COM Port closed“ message results, try the following:

1. Verify the serial adapter is connected between the laptop and thruster interface data harness service tool connection.
2. Verify the correct comm port is selected for the serial adapter. Reference the “Setup” section below
3. Verify a tool connection has been established with the joystick. Reference the “Connect” section below.

![[15900117.png]]

With Version 3 and Greater Configuration Tool

If unable to connect with the tool, try the following:

1. Before opening the program, leave the adapter cable plugged in for 1 minute to allow time for the computer to recognize the cable.
2. Verify the key powering the Cummins® electronic throttle shift and Cummins® inboard joystick system is ON.
3. Verify the desired joystick is activated.
4. Verify the lights on the lever control station and inboard joystick are illuminated.
5. Verify the adapter cable is plugged in securely.
6. Verify the correct COM port is selected.
7. Verify the driver for the cable is properly installed.
8. Verify the thruster interface module is connected and receiving power. This can be achieved by briefly activating the thruster in either direction by moving the joystick lever.

If unsure which inboard joystick the tool is connected to, try the following:

- Click on the "Identify" (6) button to verify connection between the tool and inboard joystick. After clicking the button the inboard joystick LED lights will flash in a circular pattern for 30 seconds.

![[15e00194.png]]

If unable to download a personality file, try the following:

- Close the program
- Key OFF
- Unplug the adapter cable.

Follow the connection steps a second time.

If reading a personality filter from a computer or joystick and a "File read failed!" or "Error" message results, try the following:

1. Verify the file has a.ist or.joy extension
2. Retrieve the file from the INCAL™ disc or functional joystick on the vessel, save to a computer, and try again. The file may have become corrupt or may have been modified. Files modified from an unauthorized source will **not** read correctly and can **not** be downloaded into a joystick.

If while using the tool and an "Unable to communicate with joystick" message results, try the following:

1. Verify the serial adapter is connected between the laptop and thruster interface data harness service tool connection.
2. Verify the correct communication port is selected for the serial adapter. Reference the "Setup" section below.
3. Verify a tool connection has been established with the joystick. Reference the "Connect" section below.

![[15e00186.png]]

### Setup

With Version 2 and Older Configuration Tool

To establish a connection with the Cummins® inboard joystick system, do the following in the order below.

1. Plug the adapter cable into the laptop and thruster interface data harness. Allow one minute for the computer to recognize the cable
2. Turn the keyswitch that powers the Cummins® electronic throttle shift and Cummins® inboard joystick system to the ON position.
3. Open the JOYSTICKCONFIG-SERVICE electronic service tool.
4. Press the "Refresh" button (1).
5. Select the COM port from the dropdown menu (2) which identifies the COM port with the adapter cable plugged in.
6. Press “Open Comm Port” (3).
7. A pop-up box will open, saying the COM port was opened successfully. Press OK.

![[15900118.png]]

With Version 3 and Greater Configuration Tool

To establish a connection with the Cummins® inboard joystick system, perform the following below in order.

1. Plug the adapter cable, Part Number 5299129, into the laptop and thruster interface data harness. Allow 1 minute for the computer to recognize the adapter cable.
2. Turn the keyswitch that powers the Cummins® electronic throttle shift and Cummins® inboard joystick system to the ON position.
3. Activate the joystick you will be using during the configuration process. The desired joystick **must** remain active during the configuration process.
4. After desired joystick is activated, open the JOYSTICKCONFIG-SERVICE electronic service tool.
5. Select the COM port from the dropdown menu (2) which identifies the COM port with the adapter cable plugged in. Wait while the COM port is identified and connected. Typically, the tool will automatically search and connect to a TIM and activated joystick.

![[15e00164.png]]

### Connect

With Version 2 and Older Configuration Tool

Each lever control station and inboard joystick on the controller area network (CAN) has a device identification number. This can also be called the handle ID. Use the following procedure if the handle ID for a specific lever control station or inboard joystick needs to be identified. [[326-015-054 — Vessel Configuration|Refer to Procedure 015-054 in Section 15.]]

To establish a connection with an inboard joystick within the Cummins® inboard joystick system, do the following:

1. Press “Search Joystick IDs button” (4).
2. A pop-up box will open, notifying the user that joystick detection may take up to 15 seconds. Press OK.
3. A pop-up box will open, displaying the number of inboard joysticks detected within the inboard joystick system. Press OK.
4. Use the dropdown menu (5) to select the appropriate inboard joystick identification number.
5. A pop-up box will open, saying the COM port was opened successfully. Press OK.
6. Click on the “Identify Joystick” (6) button to verify connection between the tool and inboard joystick. After clicking the button, the inboard joystick LED lights will flash in a circular pattern for 30 seconds.

![[15900119.png]]

With Version 3 and Greater Configuration Tool

A new version of joystick and lever controls have been released. The legacy software for joystick is 2 and the lever control station is 3. The existing software for joystick is version 3 and greater and lever control station is version 4. Each control station and joystick will no longer come pre-configured with station IDs. Control station 4 and joystick version 3 and greater will be identified as Station ID 1. Use the following procedure is the handle ID for a specific lever control station or inboard joystick needs to be identified. [[326-015-054 — Vessel Configuration|Refer to Procedure 015-054 in Section 15.]]

To establish a connection with an inboard joystick within the Cummins® inboard joystick system, perform the following:

1. Select the desired joystick from the "Select a Joystick" dropdown menu.
2. The version of the Cummins® Thruster Interface Module (TIM) will be displayed in green when successfully connected.
3. The joystick version and ID number will show in green when successfully connected.
4. Select the "Identify Joystick" (6) button to verify connection between the tool and inboard joystick. After selecting the button the inboard joystick LED lights will flash in a circular pattern for 30 seconds.

![[15e00165.png]]

### Read

With Version 2 and Older Configuration Tool

The file name and parameters within a personality file can be read from a personality file located on a Cummins® laptop or within an inboard joystick. This information can be useful for validation purposes.

To read the parameters for a personality file installed in an inboard joystick, do the following:

1. Select the desired inboard joystick.
2. Press “Read All Joystick Parameters” (1).
3. A pop-up box will appear, displaying that the data read was successful. The pop-up box (3) will also display the software revision, hardware revision, and parameter file ID for the inboard joystick. Press OK.

> [!note] Note · Примечание
> Write down the parameter file ID so that it can be used if transferring the file to a Cummins® laptop.

After the data has been read, it can be accessed by pressing multiple buttons on the right side of the screen (2).

Use the following procedure to find and select vessel personalities. [[326-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]

![[15900120.png]]

> [!note] Note · Примечание
> Connection to the inboard joystick is **not** necessary for this step.

To read the parameters for a personality file located on a Cummins® laptop, do the following:

1. Press “Data Transfers” (1).
2. A new window will display. Press “Read Settings From File To Local Storage" (3).
3. A new window will display allowing the user to select a file. Select the appropriate personality file to be viewed and press “Open".
4. A pop-up box will appear, displaying “File read OK!” Press OK.
5. A pop-up box will appear, displaying the parameter file ID.

After the data has been read, it can be accessed by pressing multiple buttons on the right side of the screen (2).

![[15900121.png]]

> [!note] Note · Примечание
> If the values are displayed with a dash, such as -1 or -2, they are **not** accurate because these values have **not** been read from an inboard joystick or file on a Cummins® laptop. Reference the Read Step of this procedure to read values from an inboard joystick or personality file on the Cummin®s laptop to display values. This applies to all screens accessed by the buttons on the tool's main screen.

The “ Thruster Config – Joystick Type – Assoc ID” screen can be accessed by pressing the button on the screen with that name.

The joystick type, association handle ID, and number of thrusters on the vessel can be viewed. The joystick type and associated handle ID parameters can be modified.

The “THRUST-CONFIGURATION- field displays if the personality file is set up for one bow thruster or two thrusters (bow and stem).

> [!note] Note · Примечание
> Modification of any item in the drop down menu will automatically save the value to joystick or file loaded into the tool.

The “JOYSTICKTYPE” drop down box allows the user to select whether the joystick is a standalone unit or if it is associated. If a joystick is a “standalone”, it is not next to a lever control station, but located on its own helm. If a joystick is “associated”, it is next to a lever control station on the same helm. The default joystick type setting is associated.

The “ASSOCIATED HANDLE ID” drop down box allows selection of what lever control station the joystick is associated to. A joystick may only be associated to a lever control station if they are on the same helm station. The joystick association handle ID number **must** be set to the handle ID of the lever control station on the same helm to work properly. If the joystick is on its own dedicated helm, the Associated Handle ID drop down will be grayed out and **not** selectable.

Click the “help' button for more information about the screen settings.

> [!note] Note · Примечание
> The “Current Settings” table at the bottom of the screen identifies the inboard joystick type and joystick to lever control station association IDs. Clicking the “Refresh” button will update the table.

![[15900122.png]]

The “Delay / Alert Timing Parameters” screen can be accessed by pressing the button on the right side of the screen with that name.

These parameters can be read **only** for validation purposes.

Click the "help" button for more information about the screen settings.

![[15900123.png]]

The “Direct AHD/AST Motion Parameters (Y-Motion)” screen can be accessed by pressing the button on the right side of the screen with that name.

These parameters can be read **only** for validation purposes.

Click the “help' button for more information about the screen settings.

![[15900124.png]]

The “Sideways Propulsion Parameters (X-Motion)” screen can be accessed by pressing the button on the right side of the screen with that name.

These parameters can be read **only** for validation purposes.

Click the “help' button for more information about the screen settings.

![[15900125.png]]

The “Diagonal Motion Parameters (X/Y Slide Motion)” screen can be accessed by pressing the button on the right side of the screen with that name.

These parameters can be read **only** for validation purposes.

Click the “help' button for more information about the screen settings.

![[15900126.png]]

The “Rotation Motion Parameters (Z - Motion)” screen can be accessed by pressing the button on the right side of the screen with that name.

These parameters can be read **only** for validation purposes.

Click the “help' button for more information about the screen settings.

![[15900127.png]]

The “Thruster Duty Cycle Monitor” screen can be accessed by pressing the button on the screen with that name.

These parameters can be read **only** for validation purposes.

The time units are displayed in: hours:minutes:seconds.

Click the “help' button for more information about the screen settings.

> [!note] Note · Примечание
> Prior to replacing a joystick, be sure to copy the vessel personality file and reload it into the new joystick. This will transfer the thruster duty cycle monitor information into the new joystick. See Transfer section below.

![[15900128.png]]

The “Thruster Usage Warning Parameters” screen can be accessed by pressing the button on the screen with that name.

These parameters can be read **only** for validation purposes.

The time units are displayed in: hours:minutes:seconds.

Click the “help' button for more information about the screen settings.

![[15900129.png]]

With Version 3 and Greater Configuration Tool

Thruster Button Function will allow the user to select Joystick Type and Associated ID.

- The Joystick Type allows the user to select whether the joystick is a stand alone unit or an associated unit. If a joystick is a "stand alone" it is **not** next to a lever control station, but located on its own helm. If a joystick is associated, it is next to a lever control station on the same helm. If a version 3 and greater joystick and a version 4 control station are paired together at the same helm Transparent Transfer can be used. The default joystick type setting is associated.
- The Associated ID dropdown box allows selection of the lever control station the joystick is associated to. A joystick may **only** be associated to a lever control station if they are on the same helm station. The joystick association handle ID number **must** be set to the handle ID of the lever control station on the same helm to work properly. If the joystick is on its own dedicated helm the Associated Handle ID dropdown box will be grayed out and **not** selectable.
- Transparent Transfer allows the user to take control of the joystick or control head by movement or either control levers (control head) or movement of the joystick. This feature will cause the joystick to be available for operation whenever the control head is in the neutral shift position. To use the Transparent Transfer feature the joystick and control head **must** be paired together. For more information use the following procedure. [[326-015-178 — Transparent Transfer|Refer to Procedure 015-178 in Section 15.]]

To pair a joystick and control head station, perform the following:

1. Turn engine off. Make sure ETS/CIJ system is powered ON.
2. Move the joystick to full reverse position.
3. Select the following buttons in sequence indicated. These three button selections must be completed within 5 seconds.
4. When Step 3 is complete, the Alert and System light will be blinking at a 2 Hz rate (2 blinks/second).
5. The user will have 10 seconds to complete the pairing process from this time.
6. Press and release the ACTIVE/TAKE button on the control head.
7. When the pairing process is completed by pressing/releasing the ACTIVE/TAKE button, both the control head and joystick will confirm the pairing by rapidly flashing (five times) the Joystick Activation/Station Select LEDs on both the joystick and control head.

To view the Parameters select the Parameters menu. These parameters can be read **only** for validation purposes.

![[15e00166.png]]

The Thruster Duty Cycle Monitor screen can be accessed by pressing the Special Options button. These parameters can be read **only** for validation purposes. The time units are displayed in are as follows: hours: minutes: seconds. Click the Help button for more information about screen settings.

> [!note] Note · Примечание
> Before replacing a joystick, make sure to copy the vessel personality file and reload it into the new joystick. This will transfer the thruster duty cycle monitor information into the new joystick.

![[15e00167.png]]

The Thruster Usage Warning Parameters screen can be accessed by pressing the button on the screen with that name. These parameters can be read **only** for validation purposes. The time units are displayed in are as follows: hours: minutes: seconds. Select the Help button for more information about screen settings.

![[15e00168.png]]

The information tab on the right side of the main menu shows the Software, Ship, TIM, and Joystick information. The configuration tool software version is shown under the Software tab.

![[15e00169.png]]

The information tab on the right side of the main menu shows the Software, Ship, TIM, and Joystick information. The Ship tab will show how many engines and thrusters are detected on the network as well as thruster speed and type. Other information notifies the user of existing status with activation signal, retractable thruster, trolling valve, and joystick activation.

![[15e00170.png]]

The information tab on the right side of the main menu shows the Software, Ship, TIM, and Joystick information. The TIM tab shows the hardware and software version for the TIM.

![[15e00171.png]]

The information tab on the right side of the main menu shows the Software, Ship, TIM, and Joystick information. The Joystick tab shows the joystick software version (version 2 and older or version 3 and greater).

![[15e00172.png]]

### Transfer

With Version 2 and Older Configuration Tool

Select “Data Transfers” (8) on the main screen. The Data Transfers screen will open.

There are three possible personality file data transfers.

1. Transfer from joystick to computer
2. Transfer from computer to joystick
3. Transfer from joystick to joystick.

Data transfer is **always** a two step process.

Use the following procedure if the handle ID for a specific lever control station or inboard joystick needs to be identified. [[326-015-054 — Vessel Configuration|Refer to Procedure 015-054 in Section 15.]]

![[15900130.png]]

To transfer from a joystick to a computer, do the following:

1. Press “Read Settings From JS To Tool Local Storage".
2. A new window will open. Use the dropdown menu to select the appropriate inboard joystick identification number. Press OK. Write down the parameter file ID
3. Press “Save Settings From Tool Local Storage To File”. Save the file to the computer with a.jst extension. It is important to name the file with the same parameter file ID that was recorded when reading the file from the joystick.

Use the following procedure for detailed information on managing vessel personalities. [[326-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]

![[15900106.png]]

To transfer from a computer to a joystick, do the following:

1. Press “Read Settings From File To Tool Local Storage”.
2. A window will open allowing selection of a personality file stored on a computer or external thumb drive. Choose a file.
3. Press “Write Settings To JS From Tool Local Storage”.
4. A new window will open. Use the dropdown menu to select the appropriate inboard joystick identification number. Press OK.

![[15900106.png]]

To transfer from a joystick to another joystick, do the following:

1. Press “Read Settings From JS To Tool Local Storage”.
2. A new window will open. Use the dropdown menu to select the appropriate inboard joystick identification number. Press OK.
3. Press “Write Settings To JS From Tool Local Storage”.
4. A new window will open. Use the dropdown menu to select the appropriate inboard joystick identification number. Press OK.

![[15900106.png]]

After completing a personality file transfer to a joystick, a new window will automatically open to setup the joystick type and association handle ID:

1. Use the “Joystick ID” dropdown menu to select the appropriate inboard joystick identification number.
2. Use the “Joystick Type” dropdown menu to select either “stand alone” or “Associated".
3. Use the “Associated Handle ID” dropdown menu to select the appropriate lever control station identification number that the joystick will be associated to.
4. Press “Save”.

If the “Exit (without save)” button is pressed instead of “Save”, the personality file transfer and selections made in the dropdown menu boxes will not be saved to the joystick.

> [!note] Note · Примечание
> For details about the drop down menu selections and current settings table, reference the “Read” section above Thruster Config – Joystick Type – Assoc ID” screen.

![[15900131.png]]

With Version 3 and Greater Configuration Tool

The Open/Transfer Parameter File button will allow the user to open an existing parameter file or transfer existing calibration to all other joysticks on the vessel.

- Select Open/Transfer Personality File to open or transfer a personality file.

![[15e00173.png]]

To open a saved personality file, perform the following:

1. Select Open
2. An Import Joystick Personality File window will appear. Choose the desired personality file and select Open.
3. The Open Parameter File window will appear.
4. Review the changes by reviewing highlighted rows.
5. Once changes are reviewed, there are two options to Save. User can save changes to the connected joystick by selecting the Save button. The user can save the changes to all joysticks on the network by using the Save All button.

![[15e00174.png]]

To transfer a personality file to other joysticks on the vessel, perform the following:

1. Select Open/Transfer Personality File to open or transfer a personality file.
2. Select Transfer
3. The Transfer button is a one-click process which will transfer all existing identified parameters to all other connected joysticks on the boat. All parameters will be transferred to other joysticks except Joystick Type and Associated ID number which are found in the Thruster Button Function
4. The transfer function is successful once the "Transfer was successful" message appears.

![[15e00175.png]]

### Finishing Steps

With Version 2 and Older Configuration Tool

To disconnect the electronic service tool from the Cummins® inboard joystick system, do the following:

1. Click the "Close Comm Port" button and close the electronic service tool.
2. Turn the keyswitch that powers the Cummins® electronic throttle shift and Cummins® inboard joystick system to the OFF position.
3. Remove the adapter cable. Make sure the service tool port is properly sealed by installing the appropriate cap.
4. Perform a sea trial to verify proper function. Refer to Procedure 015-046 in Section 15.

With Version 3 and Greater Configuration Tool

To disconnect the electronic service tool from the Cummins® inboard joystick system, perform the following:

1. Turn the keyswitch that power the Cummins® electronic throttle shift and Cummins® inboard joystick system to the OFF position.
2. Remove the adapter cable. Verify the service tool port is properly sealed by installing the appropriate cap.
3. Perform a sea trial to verify proper function. Refer to Procedure 015-046 in Section 15.
