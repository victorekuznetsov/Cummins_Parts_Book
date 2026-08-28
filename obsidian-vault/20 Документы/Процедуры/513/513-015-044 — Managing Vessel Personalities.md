---
type: "Процедура"
doc: "513-015-044"
title_en: "Managing Vessel Personalities"
modified: "2025-05-12"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
figures: 17
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-044.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-044.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Managing Vessel Personalities

> [!abstract] Процедура · `513-015-044`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2025-05-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-044.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-044.pdf)

### Select Service Tools

ED-4

#### Recommended Cummins® Service Tools

- Universal serial bus (USB) extension cable, Part Number 5394862 (if needed for access).

#### Additional Service Items

- USB drive

ED-5 and ED-7

#### Recommended Cummins® Service Tools

- Universal serial bus (USB) extension cable, Part Number 5394862 (if needed for access).

#### Additional Service Items

- USB drive

### General Information

ED-4

The Cummins® C Command Connect and Connect Premier Marine Panel System ED-4 display(s) are preloaded with software from the factory. The Cummins® ED-4 display software and VPF **must** be updated and configured prior to proper operation of the display.

> [!note] Note · Примечание
> A tag is typically located in the C.I.B. for referencing the software and VPF file loaded in the helm and C.I.B. ED-4s during initial system installation at the original equipment manufacturer (OEM). This tag should be updated after ED-4 software or VPF modification.

The system **must** be set up for the vessel in which it is installed in for maximum performance. ED-4 displays **must** be updated with a VPF that is specific to the vessel OEM and model. It is necessary to load the most current VPF for the vessel. If changing a VPF for other reasons, consider the many factors that can contribute to performance such as the following:

- Vessel sensors
- ED-4 display location (C.I.B. or Helm)
- Number of engines
- Number of helm stations.

The Cummins® QuickServe® Online webpage contains a tracking sheet and files. After entering the engine serial number or engine model search, the webpage can be found by clicking the following links: Service, Related Information, Marine Panel Firmware Updates, and ED-4.

Cummins® QuickServe® Online webpage; Marine Panel Firmware Updates – ED-4, contains files and a tracking sheet with information about each file, which helps select the correct file and revision level for the component.

> [!note] Note · Примечание
> The Cummins® Marine Application Engineering group creates the vessel personality files and updates the “Cummins ED-4 Display Vessel Personality File Tracking Sheet” with file name, version, and description of the vessel, application, equipment, and vessel sensor information.

The file name format below is an example. Refer to the tracking sheet for specific information.

The VPF name format: “0000 ACSOPOS1 44DXXX.zip”

Where:

000 = ED-4 Display VPF Version (000 - Hexadecimal Index for VPF)

0 = VPF Revision

A = Source Address Strategy

C = Application Type

SO = Device 1

PO = Device 2

S1 = Special Feature

44DXXX = OEM Description

“.zip” = File Extension

> [!note] Note · Примечание
> The “Cummins ED-4 Display Vessel Personality File Tracking Sheet” contains a tab called “VPF file name key” which contains information to decipher the VPF file name format.

The VPF.zip file **must** be saved to a folder named “VPF” on the USB drive. The file does **not** need to be unzipped since the ED-4 can detect and load the file as a.zip.

Once the ED-4 is configured, the VPF can be saved, exported, and imported to other VPFs on the vessel.

Example of a typical file / folder structure of the USB drive for ED-4 software and VPF.

![[15e00090.png]]

> [!note] Note · Примечание
> The files in the folders named “VPF” and “LOGS” should be cleared on the USB drive prior to saving files from the Cummins® QuickServe® Online webpage.

> [!note] Note · Примечание
> Multiple VPF files can be saved in the “VPF” folder on the USB drive.

ED-5 and ED-7

The Cummins® C Command Connect and Connect Premier Marine Panel System ED-5/ED-7 display(s) are preloaded with software from the factory. The Cummins® ED-5/ED-7 display VPF **must** be configured prior to proper operation of the display according to needs specific to the vessel OEM and model.

If it is necessary to update the ED-5/ED-7 display software in field the Cummins® QuickServe® Online webpage contains a tracking sheet and files. After entering the engine serial number or engine model search, the webpage can be found by clicking the following links: Service, Related Information, Marine Panel Firmware Updates, and ED-5/ED-7.

Cummins® QuickServe® Online webpage; Marine Panel Firmware Updates – ED-5/ED-7, contains files and a tracking sheet with information about themes/configuration available in the software package, which helps select the correct theme to meet application need.

### Preparatory Steps

ED-4

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury or equipment damage, this procedure must only be performed by suitably qualified service technicians.

> [!warning] CAUTION · Осторожно
> Before updating the software or VPF in any control system component, verify that the Vessel Control System is completely operational. It is also important to test and document the configuration settings and vessel personality of the component.

![[15e00155.png]]

The software and VPF information of the ED-4 display can be viewed by pressing key 5 or “Menu” on the data screen page.

Action:

- Press key 5 or “Menu”.
- Select “About” and press key 4 or “Enter”.
- Press key 3 or “VPF” for VPF information.
- Press key 4 or “Info” for software information.

Important information on the page, which is hard coded in the VPF.

- The identification information stored in the VPF will display across the top of the screen.
- Version - VPF version and revision.
- Modified By - ED-4 software serial number on which the VPF was modified.
- Short Description - VPF file name.
- Long Description - VPF file name format and information about the VPF capability, such as number of engines, vessel sensors, and ED-4 location for which the VPF should be used.

> [!note] Note · Примечание
> Once the ED-4 setup and configuration settings are modified, the information in the short and long description may no longer be valid.

When finished:

Press key 5 or “Back” to exit the page.

Press key 5 or “Exit” to return to the data screen page.

Prior to VPF download, document and understand the vessel performance and alarm/fault codes. Follow the alarm/fault code or the appropriate troubleshooting symptom tree to understand issues. Reference the following procedures for testing and configuration setup information:

- Verify proper function. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15]].
- Download log files from the ED-4 display for future use. [[513-015-035 — Display(s) and Instrumentation|Refer to Procedure 015-035 in Section 15]].
- Document the ED-4 display software, VPF, source address(s), and configuration settings. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15]].
- If needed, export the existing VPF used by the ED-4. See Export section below.
- Use the following procedure to find and select ED-4 software when updates are required. [[513-015-107 — Display Software|Refer to Procedure 015-107 in Section 15]].

ED-5 and ED-7

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury or equipment damage, this procedure must only be performed by suitably qualified service technicians.

> [!warning] CAUTION · Осторожно
> Before updating the software or VPF in any control system component, verify that the Vessel Control System is completely operational. It is also important to test and document the configuration settings and vessel personality of the component.

![[00e00314.png]]

![[00e00315.png]]

The software and theme/configuration information of the ED-5/ED-7 display can be viewed by accessing Menu from the display.

Action:

- Press and hold in the middle of screen or select “Menu”(I)” icon from the screen or press and hold on the select button on remote keypad if installed.
- Select “About” for software identification.
- Select “Config” for VPF information.

Important information on the page:

- Configuration Version – will display the software configuration installed. The software package released on Cummins® QuickServe® Online Marine Firmware will be identified with this information.
- Current Theme – will display theme currently active on the ED-5/ED-7 display.

When finished:

- Swipe from left to right on the screen or use when in the Menu structure to return to last page or exit the menu.

### Setup Information

ED-4

Access the USB port on the rear of the ED-4 display by removing the seal port.

For C.I.B. mounted ED-4 displays, use the following procedure for information on accessing the ED-4 display USB port. Refer to Procedure 015-023 in Section 15

> [!note] Note · Примечание
> It is important to verify the rubber USB seal port is properly installed afterward a software or VPF update. If **not**, the ED-4 may be exposed to the environment and result in internal damage.

![[15e00095.png]]

ED-5 and ED-7

Access the USB port on the rear of the ED-5/ED-7 display by removing the seal port.

> [!note] Note · Примечание
> It is important to verify the rubber USB seal port is properly installed afterward a software update. If **not**, the ED-5/ED-7 may be exposed to the environment and result in internal damage.

![[00e00316.png]]

### Exporting

ED-4

The VPF can be exported if an ED-4 is being replaced for a service event or the configuration can be used in other ED-4 locations on the vessel.

The process of exporting the active VPF being used by the ED-4 display is as follows.

> [!note] Note · Примечание
> It is recommended that the VPF folder be cleared prior to exporting a VPF to the USB drive.

1. Turn the system enable switch power ON, engine OFF, and verify the ED-4 display screen is on.
2. Connect the USB drive to the ED-4 USB port.

Once the USB drive is detected by the ED-4, the following options will be shown:

1. Load VPF
2. Save current VPF
3. Export log(s)
4. Perform software update.

Action:

- Press key 2 or “Down” to scroll to “Save current VPF”.
- Press key 4 or “Save”.

Read the prompts on the ED-4 screen during the exporting process.

Do **not** remove power to the ED-4 or remove the USB drive during the export process.

> [!note] Note · Примечание
> If an alarm pop up message occurs while the USB drive is installed, press key 5 or “Close” to acknowledge and remove the message. Then, press key 5 or “Menu” to return to the USB drive options.

> [!note] Note · Примечание
> It takes approximately 1 minute to export a VPF from the ED-4 to the USB drive.

The file will be saved to the “VPF” folder on the USB drive. The file name will include the software serial number of the ED-4 display.

Example: exportedVPF\_33403.zip

Exporting a VPF from an ED-4 with the same software serial number will overwrite the existing VPF saved on the USB drive.

Once saved to the USB drive, it is recommended to rename the file before it is used in other ED-4(s). Refer to the format shown in the General Information section above.

![[15e00122.png]]

ED-5 and ED-7

The configuration can be exported from an ED-5/ED-7 so the configuration can be used in other ED-5/ED-7 locations on the vessel.

The process of exporting the configuration being used by the ED-5/ED-7 display is as follows.

1. Turn the system enable switch power ON, engine OFF, and verify the ED-5/ED-7 display screen is on.
2. Connect the USB drive to the ED-5/ED-7 USB port.
3. Once the USB drive is detected by the ED-5/ED-7, the following options will be shown:

![[00e00317.png]]

Action:

- Scroll to “Offload Config Files”.
- Swipe left to right to eject USB.

Read the prompts on the ED-5/ED-7 screen during the exporting process. The ED-5/ED-7 will show prompts “Config Offload. Copy Complete. Eject USB before removing.”

Do **not** remove power to the ED-5/ED-7 or remove the USB drive during the export process.

The configuration files will be saved to the “1536-software serial number\_config” folder on the USB drive. The folder name will include the software serial number of the ED-5/ED-7 display.

Example of exported configuration folder: 1536-459434\_config

Exporting configuration files from an ED-5/ED-7 with the same software serial number will overwrite the existing configuration saved on the USB drive.

Once saved to the USB drive, the configuration files can be packaged with support of customer engineering before it is used in other ED-5/ ED-7 displays.

![[00e00318.png]]

### Importing

ED-4

> [!note] Note · Примечание
> Prior to VPF update, document the ED-4 display(s) source address(s) and configuration settings. See the Preparatory Steps section above.

> [!note] Note · Примечание
> Each ED-4 display on the vessel has its own USB connection and the VPF **must** be updated separately to each.

The process of loading a VPF to the ED-4 display is as follows.

1. Turn the system enable switch power ON, engine OFF, and verify the ED-4 display screen is on.
2. Connect the USB drive to the ED-4 USB port.

Once the USB drive is detected by the ED-4, the following options will be shown:

1. Load VPF.
2. Save current VPF.
3. Export log(s).
4. Perform software update.

Action:

- Press key 2 or “Down” to scroll to “Load VPF”.
- Press key 4 or “Choose”.

Read the prompts on the ED-4 screen during the importing process.

> [!note] Note · Примечание
> Do **not** remove power to the ED-4 or remove the USB drive during the import process.

> [!note] Note · Примечание
> If an alarm pop up message occurs while the USB drive is installed, press key 5 or “Close” to acknowledge and remove the message. Then, press key 5 or “Menu” to return to the USB drive options.

![[15e00123.png]]

Select the VPF to load.

Action:

- Press key 2 or “Down” to highlight the VPF.
- Press key 4 or “Load”.

On the next screen:

- Press key 1 or “Fav” to save as the favorite in the ED-4 internal memory.
- Press key 3 or “Yes” to continue with the selection.
- Pressing key 5 or “No” will return to main selection screen.

Read the prompts on the ED-4 screen during the importing process.

> [!note] Note · Примечание
> Do **not** remove power to the ED-4 or remove the USB drive during the import process.

> [!note] Note · Примечание
> It takes approximately 5 minutes to import a VPF from the USB drive to the ED-4.

> [!note] Note · Примечание
> Pressing key 1 or “Fav” will save the selected VPF as the Favorite in the ED-4 internal memory. See Library Loading below for access and information.

![[15e00156.png]]

The ED-4 will cycle its power and restart after a VPF is imported.

> [!note] Note · Примечание
> Do **not** remove the USB drive from the ED-4 unless instructed to do so.

Action:

- Press key 5 or “Eject” to end ED-4 interface with the USB drive.

Read the prompts on the ED-4 screen, and remove the USB drive when prompted to do so.

Verify the ED-4 is using the imported VPF by accessing the “About” page. See Preparatory Steps above.

![[15e00125.png]]

### Library Loading

ED-4

The ED-4 may have VPFs stored locally.

The process of accessing the VPF library on the ED-4 is as follows.

Turn the system enable switch power ON, engine OFF, and verify the ED-4 display screen is on.

Action:

- Press key 5 or “Menu”.
- Press key 2 or “Down” to scroll to “Configuration”. Press Key 4 or “Enter”.
- Press Key 1 or “Accept”.
- Press key 2 or “Down” to scroll to “VPF”. Press Key 4 or “Enter”.
- Review the VPFs available on the ED-4 screen. Press key 2 or “Down” to scroll to the desired “VPF”. Press Key 4 or “Load”.

![[15e00126.png]]

Action:

- Press key 3 or “Yes” to continue.
- Press key 5 or “No” to cancel which returns to the previous selection screen.

If a VPF was selected as a “Favorite” while loading from a USB drive, it will be the active VPF used by the ED-4. ED-4 setup and configuration setting changes are saved to the internal memory of the ED-4. To update the locally stored VPF, the VPF **must** be exported to USB drive and then imported back into the ED-4 and saved as a “favorite”.

> [!note] Note · Примечание
> During the VPF importing, press key 1 or “Fav” to save the highlighted VPF as the favorite in the ED-4. This is typically done after configuration settings have been changed in the ED-4.

> [!note] Note · Примечание
> It takes approximately 5 minutes to load a VPF from the ED-4 memory.

> [!note] Note · Примечание
> Do **not** remove power to the ED-4 during the VPF load process.

![[15e00156.png]]

ED-5 and ED-7

The ED-5/ED-7 have VPFs/Themes stored locally.

The process of accessing the themes on the ED-5/ED-7 is as follows.

Turn the system enable switch power ON, engine OFF, and verify the ED-5/ED-7 display screen is on.

Action:

- Select “Setup”.
- Select “Themes”.

![[15e00200.png]]

Action:

- Select “Setup” using touchscreen or remote keypad.
- Select “Themes” using touch screen or remote keypad.
- Select “Theme” using touch screen or remote keypad.
- Select the vessel personality file from “Choose Theme” screen to use on the display.

![[15e00201.png]]

When finished:

- Swipe left to right or use “Back”(IV) soft key on the screen to exit or press “Return/Exit” key on remote keypad to save the setting.

![[15e00202.png]]

### Troubleshooting

ED-4

USB Error Message

After a USB drive is connected to an ED-4, a USB error message may be noticed when plugged into a computer. This is normal due to the operating system interoperability between development environment (Linux) used to create and run the ED-4 software with the computer running on a different operating system (Windows™). It is **not** a functional issue, and is how the system behaves.

If unable to transfer a file from the computer to the USB drive, try the following:

Get a new file, save it to the USB drive, and try again. The file may have become corrupt or may have been modified. Files modified from an unauthorized source will **not** read correctly and can **not** be downloaded.

If there is an issue that keeps the ED-4 VPF from loading, try the following:

1. Verify a proper USB drive is being used. If needed, try using a different USB drive.
2. Verify the folder “VPF” exists on the USB drive.
3. Verify the system enable switch is ON and ED-4 display is powered up.
4. Verify the USB and extension cable (if used) is plugged in securely.
5. After installing the USB drive, leave the USB drive plugged into the display for 1 minute to allow time to recognize the USB drive.
6. After installing the USB drive, cycle power to the ED-4 using the system enable switch.
7. Try the load process again.

If the ED-4 does **not** recognize the USB drive after it is plugged in, cycle power to the ED-4 using the system enable switch.

> [!note] Note · Примечание
> If the USB drive is removed without pressing key 5 or “eject”, the ED-4 will **not** recognize the USB drive again until the power to the ED-4 is cycled.

If the system enable switch is pushed OFF or power is interrupted to the ED-4 before the VPF download completes, the VPF will **not** be updated in the ED-4. If error occurs, try the following:

- Install the USB drive and try again.

> [!note] Note · Примечание
> System enable switch cycle OFF-ON can be done to reboot ED-4 with previous installed version of VPF.

File related failures:

- If the VPF file package has errors or an incompatible version, the ED-4 shows the message "Problem with VPF. Description in Event Log"
- If the VPF file is incomplete on the USB drive, the ED-4 will **not** provide the key “Yes” to start the upload of the VPF or “Fav” key to set the favorite VPF.

If error occurs, try the following:

- Get a new file, save it to the USB drive, and try again.

> [!note] Note · Примечание
> System enable OFF-ON can be done to reboot ED-4 with previous installed version of VPF.

Process related failures requiring an ED-4 recovery:

If the USB drive is removed before the VPF download completes, the ED-4 will get stuck at the message "Installing VPF" on screen followed by a red screen. After a system enable OFF-ON, the ED-4 will be stuck at gray screen.

If an error occurs, recovery steps for ED-4 are:

1. Turn System Enable switch OFF.
2. Load the correct ED-4 software package on the USB drive.
3. Install the USB drive.
4. Hold Key 1 and Key 5.
5. Turn System Enable switch ON.
6. ED-4 will start loading the software to recover from the intermediate non-functional state the ED-4 unit had been in.

ED-5 and ED-7

USB Error Message

After a USB drive is connected to an ED-5/ED-7, a USB error message may be noticed when plugged into a computer. This is normal due to the operating system interoperability between development environment (Linux) used to create and run the ED-5/ED-7 software with the computer running on a different operating system (Windows™). It is **not** a functional issue and is how the system behaves.

If unable to transfer a file from the computer to the USB drive, try the following:

Get a new file, save it to the USB drive, and try again. The file may have become corrupt or may have been modified. Files modified from an unauthorized source will **not** read correctly and can **not** be downloaded.

If the ED-5/ED-7 does **not** recognize the USB drive after it is plugged in, cycle power to the ED-5/ED-7 using the system enable switch and try again.

> [!note] Note · Примечание
> If the USB drive is removed without selecting Eject USB option, the ED-5/ED-7 will **not** recognize the USB drive again until the power to the ED-5/ED-7 is cycled.

> [!note] Note · Примечание
> System enable switch cycle OFF-ON can be done to reboot ED-5/ED-7 with previous installed version of VPF.

Boot loader update in the software will require the ED-5/ED-7 recovery steps to be performed.

Process related failures requiring an ED-5/ED-7 recovery:

If the USB drive is removed before the ED-5/ED-7 completed the software update or keeps showing “Eject USB Successful” message when attempting to load the software update.

If an error occurs, recovery steps for ED-5/ED-7 are:

1. Turn System Enable switch OFF.
2. Load the correct ED-5/ED-7 software package on the USB drive.
3. Install the USB drive.
4. Using a small screwdriver press and hold the red button beside the USB port.
5. Turn System Enable switch ON.
6. ED-5/ED-7 will start loading the software to recover from the intermediate non-functional state the ED-5/ED-7 unit had been in.

### Finishing Steps

ED-4

> [!warning] CAUTION · Осторожно
> After updating the software or VPF in any control system component, verify that the Vessel Control System is completely operational. It is also important to test and update the configuration settings and vessel personality of the component.

After ED-4 display VPF update, refer to the following procedures for configuration setup information and testing:

- For configuration, use the following procedure. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15]]. The ED-4 display may need to be set up differently based on its location.
- For setup, use the following procedure. [[513-101-013 — General Operating Instructions|Refer to Procedure 101-013 in Section]] 1.
- All control functionality of the Cummins® Marine Controls **must** be tested before leaving the dock after a service event. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15]].

Following a VPF update, if there is a new alarm code or performance complaint, follow the alarm code or the appropriate troubleshooting symptom tree in order to understand if the personality is working properly and is the appropriate personality for the application.

If it is suspected that the vessel personality file is **not** working correctly, be sure that the appropriate file was loaded for the engine, equipment, and application.

> [!note] Note · Примечание
> The “Cummins ED-4 Display Vessel Personality File Tracking Sheet” in the Cummins® QuickServe® Online webpage provides information relating to changes made to a vessel personality file. This information can be used to establish if there is a commonality between changes made to the personality and the symptoms being observed.

ED-5 and ED-7

> [!warning] CAUTION · Осторожно
> After updating the software or VPF in any control system component, verify that the Vessel Control System is completely operational. It is also important to test and update the configuration settings and vessel personality of the component.

After ED-5/ED-7 display configuration update, refer to the following procedures for configuration setup information and testing:

- For configuration, use the following procedure. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15.]] The ED-5/ED-7 display may need to be set up differently based on its location.
- All control functionality of the Cummins® Marine Controls **must** be tested before leaving the dock after a service event. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15.]]
