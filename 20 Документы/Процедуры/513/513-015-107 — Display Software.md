---
type: "Процедура"
doc: "513-015-107"
title_en: "Display Software"
modified: "2025-05-15"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
figures: 13
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-107.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-107.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Display Software

> [!abstract] Процедура · `513-015-107`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2025-05-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-107.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-107.pdf)

### Select Service Tools

ED-4

#### Recommended Cummins® Service Tools

- USB (universal serial bus) extension cable, Part Number 5394862 (if needed for access).

#### Additional Service Items

- USB drive

ED-5 and ED-7

#### Recommended Cummins® Service Tools

- USB (universal serial bus) extension cable, Part Number 5394862 (if needed for access).

#### Additional Service Items

- USB drive

### General Information

ED-4

The Cummins® C Command Connect and Connect Premier Marine Panel System ED-4 display(s) are preloaded with software from the factory. The Cummins® ED-4 Display software and vessel personality file **must** be updated and configured prior to proper operation of the display.

> [!note] Note · Примечание
> A tag is located in the C.I.B. for referencing the software and vessel personality file file loaded in the helm and C.I.B. ED-4s during initial system installation at the original equipment manufacturer (OEM). This tag should be updated after ED-4 software or vessel personality file modification.

> [!note] Note · Примечание
> Updating software erases the configuration settings, event logs, controller area network (CAN) logs, and all vessel personality files in the ED-4.

The Cummins QuickServe® Online contains a tracking sheet and files. After entering the engine serial number or engine model search, the webpage can be found by clicking the following links: Service, Related Information, Marine Panel Firmware Updates, and ED-4.

Cummins QuickServe® Online Marine Panel Firmware Updates – ED-4, contains files and a tracking sheet with information about each file, which helps select the correct file and revision level for the component

> [!note] Note · Примечание
> The Cummins® Marine Application Engineering group updates the “Cummins ED-4 Display Software File Tracking Sheet” with file name, version, and description of the component it is intended for.

The file name format below is an example. Refer to the software file tracking sheet for specific information.

Software File Folder Name format: “AAA xxx.zip”

Where:

AAA = product name.

- ED4 = ED-4 Display Software.

xxx = Software version (examples)

- 5.5 = 505
- 5.12 = 512
- 5.30 = 530
- 5.50 = 550

The software file **must** be unzipped and saved in the root directory of the USB drive before the ED-4 can recognize it.

> [!note] Note · Примечание
> WINZIP may **not** function properly in unzipping ED-4 software files and may result in partial unzipping. The Windows Explorer Extraction Tool or WINRAR, available on the Cummins software shelf, is recommended for unzipping ED-4 software files.

Example of a typical file / folder structure of the USB drive for ED-4 software and vessel personality file.

![[15e00090.png]]

> [!note] Note · Примечание
> Except for the folder named “vessel personality file” and “LOGS”, all remaining files and folders should be removed from the USB drive prior to saving software from the Cummins QuickServe® Online.

> [!note] Note · Примечание
> Prior to installing the USB drive into an ED-4, **only** one software file / folder structure should be saved on the USB drive. Multiple software files on the USB drive may cause the ED-4 to lock up or fail the update process.

ED-5 and ED-7

The Cummins® C Command Connect and Connect Premier Marine Panel System ED-5 / ED-7 display(s) are preloaded with software packaged with vessel personality file from the factory. The Cummins® ED-5 / ED-7 display vessel personality file **must** be configured prior to proper operation of the display.

> [!note] Note · Примечание
> Updating software erases the configuration settings, event logs, controller area network (CAN) logs, in the ED-5/ED-7.

The Cummins QuickServe® Online contains a tracking sheet to ensure selection of the display vessel personality file(s) for application type. After entering the engine serial number or engine model search, the webpage can be found by clicking the following links: Service, Related Information, Marine Panel Firmware Updates, and ED-5 / ED-7.

Cummins QuickServe® Online Marine Panel Firmware Updates – ED-5 / ED-7, contains software files and a tracking sheet with information about preloaded software and vessel personality file(s) for application types, which helps select the correct file and revision level for the display use.

> [!note] Note · Примечание
> The Cummins® Marine Application Engineering group updates the “Cummins ED-5 ED-7 Display Software File Tracking Sheet” with description of Vessel Personality files / themes preloaded with the software the component it is intended for.

The file name format below is an example. Refer to the software file tracking sheet for specific information.

Software File Folder Name format: “AAA xxxxx.zip”

Where:

AAA = product name.

- ED5 / ED-7 = ED-5 / ED-7 Display Software.

xxxxx = Software version (examples)

- 0.1.0 = 010
- 0.2.0 = 020
- 0.3.0 = 030
- 0.4.0 = 040

The software file **must** be unzipped and saved in the root directory of the USB drive before the ED-5/ED-7 can recognize it.

> [!note] Note · Примечание
> WINZIP may **not** function properly in unzipping ED-5/ED-7 software files and may result in partial unzipping. The Windows Explorer Extraction Tool or WINRAR, available on the Cummins software shelf, is recommended for unzipping ED-5/ED-7 software files.

Example of a typical file / folder structure of the USB drive for ED-5/ED-7 software and vessel personality file.

![[00e00321.png]]

> [!note] Note · Примечание
> Except for the folder named “config” and “LOGS”, all remaining files and folders should be removed from the USB drive prior to saving software from the Cummins QuickServe® Online.

> [!note] Note · Примечание
> Prior to installing the USB drive into an ED-5/ED-7, **only** one software file / folder structure should be saved on the USB drive. Multiple software files on the USB drive may cause the ED-5/ED-7 to lock up or fail the update process.

### Preparatory Steps

ED-4

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury or equipment damage, this procedure must only be performed by suitably qualified service technicians.

> [!warning] CAUTION · Осторожно
> Before updating the software or vessel personality file in any control system component, verify that the vessel control system is completely operational. It is also important to test and document the configuration settings and vessel personality of the component.

![[15e00153.png]]

The software and vessel personality file information of the ED-4 display can be viewed by pressing key 5 or “Menu” on the data screen page.

Action:

- Press key 5 or “Menu”.
- Select “About” and press key 4 or “Enter”.
- Press key 3 or “vessel personality file” for vessel personality file information.
- Press key 4 or “Info” for software information.

Important information on the page.

- Part number – for software compatibility.
- SW Serial Number – Serial Number of the ED-4 display.
- SW Version – Software version loaded in display.

When finished:

Press key 5 or “Back” to exit the page.

Press key 5 or “Exit” to return to the data screen page.

Prior to software file download, document and understand the vessel performance and alarm/fault codes. Follow the alarm/fault code or the appropriate troubleshooting symptom tree in order to understand issues.

Reference the following procedures for testing and configuration setup information:

- Verify proper function. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15]].
- Download log files from the ED-4 display for future use. [[513-015-035 — Display(s) and Instrumentation|Refer to Procedure 015-035 in Section 15]].
- Document the ED-4 display software, vessel personality file, source address(s), and configuration settings. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 1]] 5.
- If needed, export the existing vessel personality file used by the ED-4. Use the following procedure to find and select ED-4 vessel personality file when updates are required. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15]].

ED-5 and ED-7

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury or equipment damage, this procedure must only be performed by suitably qualified service technicians.

> [!warning] CAUTION · Осторожно
> Before updating the software or vessel personality file in any control system component, verify that the vessel control system is completely operational. It is also important to test and document the configuration settings and vessel personality of the component.

![[00e00322.png]]

The software and vessel personality file information of the ED-5/ED-7 display can be viewed by press in the middle of data screen page or press and hold the “Enter/Select” button on the remote keypad.

Action:

- Press in the middle of the data screen or press and hold the “Enter/Select” button on the remote keypad.
- Select “About” or press “Down” to select “About” and press “Enter/Select” button on the remote keypad.
- Press “Config” or press “Down” and press “Enter/Select” button for vessel personality file information.

Important information on the page.

- Part number – for software compatibility.
- Serial Number – Serial Number of the ED-5/ED-7 display.
- Software Version – Software version loaded in display.

When finished:

Swipe left to right or use “Back”(IV) soft key on the screen or “Return/Exit” to exit the page.

Prior to software file download, document and understand the vessel performance and alarm/fault codes. Follow the alarm/fault code or the appropriate troubleshooting symptom tree in order to understand issues.

Reference the following procedures for testing and configuration setup information:

- Verify proper function. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15.]]
- Download log files from the ED-5/ED-7 display for future use. [[513-015-035 — Display(s) and Instrumentation|Refer to Procedure 015-035 in Section 15.]]
- Document the ED-5/ED-7 display software, vessel personality file, source address(s), and configuration settings. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15.]]

### Setup Information

ED-4

Access the USB port on the rear of the ED-4 display by removing the seal port.

For C.I.B. mounted ED-4 displays, use the following procedure for information on accessing the ED-4 display USB port. Refer to Procedure 015-023 in Section 15

> [!note] Note · Примечание
> It is important to verify the rubber USB seal port is properly installed after a software or vessel personality file update. If **not**, the ED-4 may be exposed to the environment and result in internal damage.

![[15e00095.png]]

ED-5 and ED-7

Access the USB port on the rear of the ED-5/ED-7 display by removing the seal port. The USB port seal should be moved 90 degrees towards the top of the display to help retain and secure the USB port seal back on the display.

> [!note] Note · Примечание
> It is important to verify the rubber USB seal port is properly installed after a software or vessel personality file update. If **not**, the ED-5/ED-7 may be exposed to the environment and result in internal damage.

![[00e00323.png]]

### Importing

ED-4

> [!note] Note · Примечание
> Prior to software update, document the ED-4 display(s) source address(s) and configuration settings. See the Preparatory Steps section above.

Each ED-4 display on the vessel has its own USB connection and the software **must** be updated separately to each.

The process of loading a software to the ED-4 display is as follows.

1. Turn the system enable switch power ON, engine OFF, and verify the ED-4 display screen is on.
2. Connect the USB drive to the ED-4 USB port.

Once the USB drive is detected by the ED-4, the following options will be shown:

1. Load vessel personality file
2. Save current vessel personality file
3. Export log(s)
4. Perform software update.

Action:

- Press key 2 or “Down” to scroll to “Load vessel personality file”.
- Press key 4 or “Choose”.

Read the prompts on the ED-4 screen during the importing process.

Do **not** remove power to the ED-4 or remove the USB drive during the import process.

> [!note] Note · Примечание
> If an alarm pop up message occurs while the USB drive is installed, press key 5 or “Close” to acknowledge and remove the message. Then, press key 5 or “Menu” to return to the USB drive options.

![[15e00128.png]]

> [!note] Note · Примечание
> Pressing key 3 or “Leave” will return to main selection screen.

To initialize software update, press and hold down keys 1 and 5 until a bright blue screen appears.

Read the prompts on the ED-4 screen during the importing process.

Do **not** remove power to the ED-4 or remove the USB drive during the import process.

> [!note] Note · Примечание
> It takes approximately 3 minutes to import software from the USB drive.

![[15e00195.png]]

Do **not** remove the USB drive from the ED-4 unless instructed to do so.

The ED-4 will cycle its power and restart after a software download is complete and the USB drive is removed.

Verify the ED-4 software is updated by accessing the “About” page. See Preparatory Steps above.

![[15e00130.png]]

ED-5 and ED-7

> [!note] Note · Примечание
> Prior to software update, document the ED-5/ED-7 display(s) source address(s) and configuration settings. See the Preparatory Steps section above.

Each ED-5/ED-7 display on the vessel has its own USB connection and the software **must** be updated separately to each.

The process of loading a software to the ED-5/ED-7 display is as follows.

1. Turn the system enable switch power ON, engine OFF, and verify the ED-5/ED-7 display screen is on.
2. Connect the USB drive to the ED-5/ED-7 USB port.

Once the USB drive is detected by the ED-5/ED-7, the following options will be shown:

1. Software update
2. Offload log files
3. Offload configuration files

Action:

- Select Software Update or “Offload Log Files” to import log files.
- Select “Offload Config Files” to import configuration settings from the ED-5/ED-7.
- Swipe left to right on the screen to exit the screen and safely ejecting the USB drive.

Read the prompts on the ED-5/ED-7 screen during the importing process.

Do **not** remove power to the ED-5/ED-7 or remove the USB drive during the import process.

> [!note] Note · Примечание
> If an alarm pop up message occurs while the USB drive is installed, Swipe left to right on the screen to acknowledge and remove the message.

![[00e00324.png]]

> [!note] Note · Примечание
> Swipe left to right on the screen or use “Back”(IV) soft key on the screen to return to main screen and safe ejection of USB drive.

To initialize software update, press Software Update. It takes approximately one minute to perform software update.

Do **not** remove power to the ED-5/ED-7 or remove the USB drive during the software update process.

![[00e00325.png]]

Do **not** remove the USB drive from the ED-5/ED-7 unless instructed to do so.

The ED-5/ED-7 will cycle its power and restart after a software download is complete and the USB drive is removed.

Verify the ED-5/ED-7 software is updated by accessing the “About” page. See Preparatory Steps above.

Once the ED-5/ED-7 restarts, follow the prompts on the display screen to calibrate the touch. After the touch calibration is complete, the data screen is loaded, and display is ready to use.

![[00e00326.png]]

### Troubleshooting

ED-4

USB Error Message

After a USB drive is connected to an ED-4, a USB error message may be noticed when plugged into a computer. This is normal due to the operating system interoperability between development environment (Linux) used to create and run the ED-4 software with the computer running on different operating system (Windows). It is **not** a functional issue, and will be how the system behaves. If software is changed due to a boot loader issue, a red screen error will display before continuing and a reboot of ED-4 will required to complete the software download process.

If unable to transfer a file from the computer to the USB drive, try the following:

Get a new file, save it to the USB drive, and try again. The file may have become corrupt or may have been modified. Files modified from an unauthorized source will **not** read correctly and can **not** be downloaded.

If there is an issue that keeps the ED-4 software from loading, try the following:

1. Verify a proper USB drive is being used. If needed, try using a different USB drive.
2. Verify the software has been unzipped on the USB drive and has the proper file structure.
3. Verify the system enable switch is ON and ED-4 display is powered up.
4. Verify the USB and extension cable, if used, is plugged in securely.
5. After installing the USB drive, leave the USB drive plugged into the display for 1 minute to allow time to recognize the USB drive.
6. After installing the USB drive, cycle power to the ED-4 using the system enable switch.
7. Try the load process again.

If the ED-4 does **not** recognize the USB drive after it is plugged in, cycle power to the ED-4 using the system enable switch.

> [!note] Note · Примечание
> If the USB drive is removed without pressing key 5 or “eject”, the ED-4 will **not** recognize the USB drive again until the power to the ED-4 is cycled.

If the USB drive is removed before the software download completes, the ED-4 will get stuck at the message “Preparing For Update...” screen message indefinitely.

If error occurs, try the following:

- Install the USB drive and try again.

> [!note] Note · Примечание
> System enable switch cycle OFF-ON can be done to reboot ED-4 with previous installed version of software.

File related failures:

- If the software file package is corrupt or incomplete on the USB drive, a blue screen will be followed by a red screen. The ED-4 will get stuck at the red screen during the software download.
- If the software file package is incomplete on the USB drive, a blue screen will flash constantly on the ED-4.
- If the software file package is incomplete on the USB drive, the ED-4 shows the message "Error During Update. Please Remove USB Drive And Retry." on a flashing red screen.

If error occurs, try the following:

- Get a new file, save it to the USB drive, and try again.

> [!note] Note · Примечание
> System enable switch cycle OFF-ON can be done to reboot ED-4 with previous installed version of software.

Process related failures requiring an ED-4 recovery:

- If the USB drive has multiple software file packages, during the download the ED-4 will get stuck at a red screen. After a system enable switch OFF-ON, the ED-4 will be stuck at a gray screen.
- If the system enable switch is pushed OFF or power is interrupted to the ED-4 before the software download completes, then the ED-4 will go into a loop of restarts showing the Cummins® Splash screen after reboot.
- If the USB drive is removed before the software download completes, the ED-4 will get stuck at the message “Updating - Please Wait…” screen message indefinitely. After a system enable OFF-ON, the ED-4 will be stuck at gray screen.

If an error occurs, recovery steps for ED-4 are:

1. Turn system enable switch OFF.
2. Load the correct ED-4 software package on the USB drive.
3. Install the USB drive.
4. Hold Key 1 and Key 5.
5. Turn system enable switch ON.
6. ED-4 will start loading the software to recover from the intermediate non-functional state the ED-4 unit had been in.

ED-5 and ED-7

If unable to transfer a file from the computer to the USB drive, try the following:

Get a new file, save it to the USB drive, and try again. The file may have become corrupt or may have been modified. Files modified from an unauthorized source will **not** read correctly and can **not** be downloaded.

During the software update process, if the Software Update option is selected and ED-5/ED-7 screen shows eject successful message this means that were problems reading the information on the USB Stick or the display is unable to load the software update.

If there is an issue that keeps the ED-5 / ED-7 software from loading, try the following:

1. Verify a proper USB drive is being used. If needed, try using a different USB drive.
2. Verify the software has been unzipped on the USB drive and has the proper file structure.
3. Verify the USB and extension cable, if used, is plugged in securely.
4. Locate the red button beside the USB port on the display.
5. Using a little screwdriver hold the red button.
6. Switch the system enable switch ON and ED-5 / ED-7 display is powered up.
7. The display shall start loading the software displaying “Updating – Please wait”.
8. Once software load is completed.

If the ED-5 / ED-7 does **not** recognize the USB drive after it is plugged in, cycle power to the ED-5 / ED-7 using the system enable switch.

If the USB drive is removed before the software download completes, the ED-5/ED-7 will get stuck at the message “Preparing For Update...” screen message indefinitely.

If error occurs, try the following:

- Install the USB drive and try again.

> [!note] Note · Примечание
> System enable switch cycle OFF-ON can be done to reboot ED-5/ED-7 with previous installed version of software.

File related failures:

- If the software file package is corrupt or incomplete on the USB drive, the ED-5/ED-7 shows the message “Error During Update. Please Remove USB Stick And Retry.” on a flashing red screen.
- If the software file package installed is incomplete, the ED-5/ED-7 shows the message “Invalid Configuration. Insert valid USB stick.”

If error occurs, try the following:

- Get a new file, save it to the USB drive, and try again.

> [!note] Note · Примечание
> System enable switch cycle OFF-ON can be done to reboot ED-5/ED-7 with previous installed version of software.

Process related failures requiring an ED-5/ED-7 recovery:

- If the system enable switch is pushed OFF or power is interrupted to the ED-5/ED-7 before the software download completes, then the ED-5/ED-7 will go into a loop of restarts showing the Cummins® Splash screen after reboot
- If the ED-5/ED-7 keeps showing “Eject USB. Successful” message when trying to upload the software.
- If the USB drive is removed before the software download completes, the ED-5/ED-7 will get stuck at the message “Updating - Please Wait…” screen message indefinitely. After a system enable OFF-ON, the ED-5/ED-7 will be stuck at gray screen.

If an error occurs, recovery steps for ED-5/ED-7 are:

- Turn system enable switch OFF.
- Load the correct ED-5/ED-7 software package on the USB drive.
- Install the USB drive.
- Using a little screwdriver hold the red button.
- Switch the system enable switch ON and ED-5 / ED-7 display is powered up.
- The display shall start loading the software displaying “Updating – Please wait”.
- Once software load is completed.

If the ED-5/ED-7 display does **not** recognize the touch screen accurately, touch screen calibration steps for ED-5/ED-7 are:

1. Turn system enable switch ON.
2. Press and hold at any location on the screen for 30 seconds.
3. The display shall load the screen to calibrate touch displaying “Calibrate Touch”.
4. Follow the screen prompts to touch each of the crosses as they appear on the screen in the different location on the screen.
5. Once the touch calibration process is completed, the display data screen will be loaded.

![[00e00327.png]]

### Finishing Steps

ED-4

> [!warning] CAUTION · Осторожно
> After updating the software or vessel personality file in any control system component, verify that the vessel control system is completely operational. It is also important to test and update the configuration settings and vessel personality of the component.

After ED-4 display software update, refer to the following procedures for configuration setup information and testing:

- It will be necessary to update the vessel personality file. Use the following procedure for information on managing vessel personalities. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15]].
- For configuration, use the following procedure. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15]]. The ED-4 display may need to be set up differently based on its location.
- For setup, use the following procedure. [[513-101-013 — General Operating Instructions|Refer to Procedure 101-013 in Section]] 1.
- All control functionality of the Cummins® Marine Controls **must** be tested before leaving the dock after a service event. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15]].

Following a software update, if there is a new alarm code or performance complaint, follow the alarm code or the appropriate troubleshooting symptom tree in order to understand if the software is working properly and is the appropriate software for the application.

If it is suspected that the software is **not** working correctly, make sure that the appropriate file was loaded for the ED-4, engine, equipment, and application.

> [!note] Note · Примечание
> The “Cummins ED-4 Display Software File Tracking Sheet” in the Cummins QuickServe® Online “Cummins ED-4 Display” provides information relating to changes made to a software file. This information can be used to establish if there is a commonality between changes made to the software and the symptoms being observed.

ED-5 and ED-7

> [!warning] CAUTION · Осторожно
> After updating the software or configuration in any control system component, verify that the vessel control system is completely operational. It is also important to test and update the configuration settings of the component.

After ED-5/ED-7 display software update, refer to the following procedures for configuration setup information and testing:

- It will be necessary to update the vessel personality file. Use the following procedure for information on managing vessel personalities. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]
- For configuration, use the following procedure. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15.]]
- For setup, use the following procedure. [[513-101-013 — General Operating Instructions|Refer to Procedure 101-013 in Section 1.]]
- All control functionality of the Cummins® Marine Controls **must** be tested before leaving the dock after a service event. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15.]]

Following a software update, if there is a new alarm code or performance complaint, follow the alarm code or the appropriate troubleshooting symptom tree in order to understand if the software is working properly and is the appropriate software for the application.
