---
type: "Процедура"
doc: "326-015-074"
title_en: "Component Software Download Tool"
modified: "2019-11-04"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4358378"
figures: 48
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-074.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-074.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/326"
---

# Component Software Download Tool

> [!abstract] Процедура · `326-015-074`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4358378 — Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick Marine Con|4358378]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2019-11-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-074.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-074.pdf)

### General Information

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury or equipment damage, this procedure must only be performed by suitably qualified service technicians.

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, do not touch the electrical supply wires or component while the testing procedure is in progress.

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, wear goggles and protective clothing.

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

Cummins® Marine Controls come with preloaded software from the factory.

Use the following procedure to find and select software when updates are required. [[326-015-075 — Component Software Management|Refer to Procedure 015-075 in Section 15.]]

### Preparatory Steps

> [!warning] CAUTION · Осторожно
> Before updating software in any control system component, verify that the Vessel Control System is completely operational. It is also important to test and document the configuration settings and vessel personality of the component, if needed.

Prior to software file download, document and understand the vessel performance and alarm/fault codes. Follow the alarm/fault code or the appropriate troubleshooting symptom tree in order to understand issues. For an inboard joystick vessel, it will also be necessary to confirm the vessel personality is working correctly and the appropriate personality for the application is being utilized. Prior to component software update, reference the following procedures for testing and configuration setup information:

- Refer to Procedure 015-051 in Section 15 for the lever control station.
- Refer to Procedure 015-052 in Section 15 for the inboard joystick.
- [[326-015-054 — Vessel Configuration|Refer to Procedure 015-054 in Section 15]] for the vessel configuration.
- Refer to Procedure 015-055 in Section 15 for the throttle control processor module.
- Refer to Procedure 015-056 in Section 15 for the thruster interface module.
- Perform a sea trial to verify proper function. Refer to Procedure 015-046 in Section 15.

### Setup Information

The following equipment is needed to connect to the component to perform a software update:

- Compatible computer
- In-Circuit Programmer (ICP) Application and USB driver
- Component Software Download Tool Kit Cummins® Part Number 5563489
- Version 4 and greater control head programming cable.

The ICP Application and USB Driver can be found at INSITE.CUMMINS.COM in the related tools section of the website or on the Cummins® software shelf.

For computer compatibility requirements, reference INSITE.CUMMINS.COM.

> [!note] Note · Примечание
> For Cummins® employees, this software application should be downloaded from the Cummins® software shelf, keyword search 'ICP'.

Once the ICP Application is installed on the computer, it can be found under the name “ICP for Windows".

![[ck800wa.png]]

**ICP Application and USB Driver Installation**

In order to load new software in the component software download tool (ICP2-Portable Programmer), Cummins® Part Number 5563489, it is necessary to install the ICP Application and USB driver in a Windows PC.

> [!note] Note · Примечание
> Do **not** connect the component software download tool (ICP2-Portable Programmer) to the computer until the ICP Aplication and USB driver are installed.

![[ck800wa.png]]

1. Download and save the ICP Application files to a suitable directory on your computer.

2. This is a zip file. Extract the files from the zip file and save them in the same directory.

3. Start the "ICPWin\_setup\_XXXX.exe program. This will install the application software on the computer. Respond to the prompts with any program installation.

> [!note] Note · Примечание
> One of the installation options is to install the ICP plug-in for the MPLAB (R) IDE. Answer “NO” - this is **not** used with the component software download tool (ICP2-Portable Programmer), Cummins® Part Number 5563489.

4. Open the “CP2102\_USB\_Certified\_Driver” directory and run the program “CP210xVCPInstaller”. Respond to the prompts as with any program installation.

5. Plug the component software download tool (ICP2-Portable Programmer) into the computer using any USB port. The computer will find the device driver and install it. Wait until the message is given that the device driver installation is complete before unplugging.

> [!note] Note · Примечание
> Connect the component software download tool (ICP2-Portable Programmer) to the same USB port each time. If it is **not**, the communications port will need to be reset for the new USB port.

![[ck800wa.png]]

**ICP Application and USB Driver Configuration**

1. Start the application – “ICP for Windows”. This will be found in the “Softlog” folder in the Start menu. During the initial startup of this program:

1. Make sure that the component software download tool (ICP2-Portable Programmer) is plugged in to the computer USB connection BEFORE you start up the “ICP for Windows” application
2. An error will pop up during the initial startup process indicating that the program “Can't Open Port”. This is normal. The communications port will be set in Step 4 below
3. The “About” information screen will pop up during the initial startup indicating that the connections should be checked. Press OK and ignore.
4. If a message appears “Newer firmware is available. Upgrade now?” - Press “NO".

![[15a00013.png]]

2. Select the program which will be used. Click on "Programmer" then "Select Programmer". Highlight the box next to "ICP2-Portable” and press “OK”.

![[15a00014.png]]

3. Select the communications port which will be used. Click on "Communication" then "RS-232/USB/Bluetooth".

![[15a00015.png]]

4. Highlight the selection indicated “Silicon Labs CP210x to USB to UART bridge” and then press “OK".

> [!note] Note · Примечание
> If a message appears “Newer firmware is available. Upgrade now?”, press “YES” and follow the on-screen instructions.

![[15a00016.png]]

5. Save the Configuration. Click on “File” then “Save Configuration” and press “Enter”. The programmer type and communication port are now saved.

![[15a00017.png]]

### Transfer

To transfer software from the computer to the component software download tool (ICP2-Portable Programmer), do the following in the order below.

1. The software, also called “Environment”, which will be loaded on the component software download tool (ICP2-Portable Programmer) should be obtained and stored on the computer. Use the following procedure to find and select software when software updates are required. [[326-015-075 — Component Software Management|Refer to Procedure 015-075 in Section 15.]]

2. Connect the component software download tool (ICP2-Portable Programmer) Cummins® Part Number 5563489 to computer using USB cable Cummins® Part Number 5299884.

3. Start the “ICP for Windows” application.

1. Two screens will appear during start up - “What's New” and “About” (ICP Family). Click “OK” to ignore these boxes.
2. During this process, the ICP for Windows application will establish communication with the component software download tool (ICP2-Portable Programmer). If this fails, the communication port will have to be reset. See Setup Information section above.

![[15a00018.png]]

4. On the Control Center box, click on the “PC-Driven” tab on the main screen.

5. On the “ICP2 Portable Environment box”, click on the button associated with the “Environment” box where the software will be stored. In the screenshot shown, the software will be stored in “Environment \#2".

![[15a00019.png]]

6. Click on “Environment” then “Transfer Environment to Programmer ….” in order to transfer the software environment from the computer to the component software download tool (ICP2-Portable Programmer. Using the normal Windows commands, browse to the location where the software environment was stored in Step 1 above, highlight the file name, and then click “Open”. A progress bar will pop up indicating that the software transfer is in progress. A popup screen will be shown when the transfer is successful.

7. When the software transfer is complete, disconnect the component software download tool (ICP2-Portable Programmer) from the computer.

![[15a00020.png]]

8. Use a label maker to document the software file name and version on the component software download tool (ICP2-Portable Programmer) in the space next to the environment number (1). [[326-015-075 — Component Software Management|Refer to Procedure 015-075 in Section 15]] for details about software file name format.

![[15a00021.png]]

### Connect

> [!warning] CAUTION · Осторожно
> Before updating software in any control system component, verify that the Vessel Control System is completely operational. It is also important to test and document the configuration settings and vessel personality (if needed) of the component. See Preparatory Steps Section above.

The process of updating software in the control system component is as follows:

1. Remove the control system component from the location where it is mounted. See below for details on each component.
2. Reconnect the control system component to boat wiring in order to power up the component prior to software download. See below for details on each component.
3. Disassemble, if necessary, the control system component to gain access to the programming pins and connect the programing cable. See below for details on each component.
4. Connect component software download tool (ICP2-Portable Programmer) to the component, and download the software from the Programmer to the control system component. See Download section below.
5. After programming, disconnect the programmer and cables from the component and reassemble, if necessary. Install the control system component.
6. If needed, configure the control system component and load vessel personality. Test and validate the control system for proper operation. See Finishing Step section.

![[ck800wa.png]]

Inboard Joystick

The joystick configuration and vessel personality should be saved for reinstallation when the software update download is complete. See Preparatory Step section.

![[15500006.png]]

1. If the programming port located on the bottom of the joystick is **not** accessible, remove the joystick. Refer to Procedure 015-052 in Section 15.

![[15500015.png]]

2. Provide power to the joystick.

If the joystick was removed, connect the yellow CANbus cable,Cummins® Part Number 5299804, in the Component Software Download Tool Kit, Cummins® Part Number 5563489, to extend power from the CANbus cable disconnected to the joystick in step 1.

Turn the system power "ON", engine OFF, to verify the joystick lights come on.

> [!note] Note · Примечание
> When using the yellow CANbus cable, Cummins® Part Number 5299804, power extension cable, the lights on the component will begin flashing approximately 15 seconds after the system power is turned on.

If there were two CANbus cables disconnected in Step 1, and no joystick lights are observed when the system power is “ON”, connect the yellow CANbus, Cummins® Part Number 5299804, to the other CANbus cable disconnected in Step 1.

Turn the system power “OFF” once power is verified to the control system component.

![[15a00022.png]]

3. Connect component programming cable, Cummins® Part Number 5299798, to the joystick programming port.

> [!note] Note · Примечание
> The joystick has an external programming port on the bottom cover. Disassembly of the joystick is **not** required for software download.

![[15a00023.png]]

4. Use component software download tool (ICP2-Portable Programmer) to download software to the component. See Download section for details.

![[ck800wa.png]]

5. If removed, install the inboard joystick. Refer to Procedure 015-052 in Section 15.

6. Configure the control system component and load vessel personality. Test and validate the control system for proper operation. See Finishing Step section.

![[15500015.png]]

Thruster Interface Module

1) Remove and disassemble the thruster interface module. Refer to Procedure 015-056 in Section 15.

![[15500011.png]]

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, do not touch the electrical supply wires or component while the testing procedure is in progress.

> [!warning] CAUTION · Осторожно
> The thruster interface module circuit board is extremely sensitive to static electricity and should not be touched. Hold the circuit board by the Deutsch™ connectors. When placing the circuit board on a surface, ensure that the surface is clean and the circuit board does not touch anything which is metal.

2) Connect the yellow CANbus cable, Cummins® Part Number 5299804, in the Component Software Download Tool Kit, Cummins® Part Number 5563489, to extend power from the CANbus cable disconnected in Step 1 to the thruster interface module.

Provide power to the thruster interface module by connecting the black 12-pin connector.

Turn the system power “ON”, engine OFF. The thruster interface power supply light (5) indicates that the circuit board is receiving power from the CAN network.

> [!note] Note · Примечание
> When using the yellow CANbus cable Cummins® Part Number 5299804 power extension cable, the lights on the component will begin flashing approximately 15 seconds after the system power is turned on.

Turn the system power “OFF” once power is verified to the control system component.

> [!note] Note · Примечание
> A portion of the thruster interface module circuit board is shielded for EMI protection. The shield cannot be removed. The lights under the shield can be viewed in the gap above the lights.

![[15900103.png]]

3) Connect component programming cable, Cummins® Part Number 5299797 (1), to the programming pins.

> [!note] Note · Примечание
> The circuit board is located between the cable pin connector.

![[15a00024.png]]

4) Use component software download tool (ICP2-Portable Programmer) to download software to the component. See Download section for details.

![[ck800wa.png]]

5) Assemble and install the thruster interface module. Refer to Procedure 015-056 in Section 15.

6) Test and validate the control system for proper operation. See Finishing Step section.

![[15500011.png]]

Version 3 and Older Lever Control Station

There are two different versions of control heads. The legacy control head version is 3 and older and the existing version is 4 and greater. Version 4 and greater control heads have an additional service port on the bottom of the device.

1) Remove the lever control station. Refer to Procedure 015-051 in Section 15.

![[15500012.png]]

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, do not touch the electrical supply wires or component while the testing procedure is in progress.

2) Provide power to the lever control station.

Follow Option A or B below, depending on the number of CANbus cables connected to the lever control station.

Option A:

If **only** one CANbus cable is connected to the lever control station:

Connect the yellow CANbus cable, Cummins® Part Number 5299804, in the Component Software Download Tool Kit, Cummins® Part Number 5299795, to extend power from the CANbus cable disconnected to the lever control station in step 1.

Option B:

If two CANbus cables are installed on the lever control station:

Determine which cable is routed to the throttle control processor module and connect the lever control station to that cable using the yellow CANbus cable, Cummins® Part Number 5299804.

If this can **not** be determined, choose one cable, and install the yellow CANbus cable, Cummins® Part Number 5299804 and turn the system power “ON” and engine OFF. If lights are observed on the lever control station when the system power is “ON”, and engine OFF, the correct cable connection has been made.

> [!note] Note · Примечание
> When using the yellow CANbus cable, Cummins® Part Number 5299804, power extension cable, the lights on the component will begin flashing approximately 15 seconds after the system power is turned on.

If no lights are on, connect the yellow CANbus cable, Cummins® Part Number 5299804, to the other CANbus cable. Once the cable is connected to the correct CANbus cable and verified it provides power to the lever control station, turn the system power “OFF".

![[15a00025.png]]

3) Connect the component programming cable to the programming pins.

The lever control station **must** be disassembled in order to access the programming pins.

Press the lever control station handles to the full ahead forward position.

Place lever control station upside down onto a soft cloth.

Rotate the lever control station so that the front of the lever control station (button pad side) is closest to you.

Remove the screws from the bottom cover.

Grasp the bottom cover/gasket and pull towards you and rotate the cover/gasket assembly 180 degrees as shown.

![[15a00026.png]]

Locate the programming pins on the lever control station circuit board with the lever control station upside down and the front of the lever control station (button pad side) towards you.

A) Two button lever control station - programming pins are located on the bottom right corner.

Connect the programming cable connector: Two button lever control station Cummins® Part Number 5299800.

The programming cable connector for the two button lever control station is orientated correctly by following the instructions on the cable connector label.

Make sure the connector connects to all pins.

![[15a00027.png]]

B) Four button lever control station - programming pins are located on the middle right side.

Connect the programming cable connector: Four button lever control station Cummins® Part Number 5299799

The programming cable connector for the four button lever control station is keyed and is orientated correctly when clicks into place. Make sure the connector connects to all pins.

![[15a00028.png]]

4) Use component software download tool (ICP2-Portable Programmer) to download software to the component. See Download section for details.

![[ck800wa.png]]

5) Assemble and install the lever control station.

Remove the yellow CANbus cable power extension from the lever control station connector.

Rotate the gasket/cover assembly back onto the bottom of the lever control station.

Make sure that the bottom cover is properly seated into the lever control station gasket.

Inspect the wires that run from the connectors to the lever control station. Make sure the wires are not “pinched” as the gasket/ cover is pushed against the bottom of the lever control station.

![[15a00029.png]]

Once the gasket/cover assembly is placed correctly and the gasket is fully seated onto the lever control station, attach the bottom cover and evenly tighten the screws in a star-shaped pattern. Make sure wires do **not** pop out and get pinched.

Once tightened, the gasket should be evenly compressed and shaped all around the lever control station.

![[15a00030.png]]

Install the lever control station. Refer to Procedure 015-051 in Section 15.

6) Configure the control system component. Test and validate the control system for proper operation. See Finishing Step section.

![[15500012.png]]

Version 4 and Greater Lever Control Station

There are two different versions of control head levers. The legacy control head lever version (1) is 3 and the existing version is 4 (2). Version 4 and greater control head levers have an additional programming port on the bottom of the device.

1. Remove the lever control station. Locate the version number on the data plate on the bottom of the lever control station. Refer to Procedure 015-051 in Section 15.

![[15e00176.png]]

2. Connect the programming cable, Cummins® Part Number 5563489, to the control head programming port. This cable is included in the Component Software Download Tool Kit, Cummins® Part Number 5563489. The programming cable is also available to purchase as a standalone cable.

3. Connect the programming cable, Cummins® Part Number 5563489, to ICP2 Portable Programmer.

> [!note] Note · Примечание
> The Version 4 and greater control lever has an external programming port on the bottom cover. Disassembly of the control lever is not required for software download.

4. Use ICP for Windows (ICP2-Portable Programmer) to download software to the component. See Download section for details.

![[ck800wa.png]]

Throttle Control Processor Module

1) Remove the throttle control processor module. Refer to Procedure 015-055 in Section 15.

![[15500009.png]]

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, do not touch the electrical supply wires or component while the testing procedure is in progress.

> [!warning] CAUTION · Осторожно
> It is critical that the appropriate jumper plug is used with the throttle control processor module and system power supply battery voltage.

2) Provide power to the throttle control processor module.

1. Connect the power extension cable, Cummins® Part Number 5299805, to reconnect power to the throttle control processor module.
2. Connect the yellow CANbus cable, Cummins® Part Number 5299804, in the Component Software Download Tool Kit, Cummins® Part Number 5299795, to extend power from the CANbus cable disconnected in Step 1 to the lever control station.
3. Insert the power jumper plug.

> [!note] Note · Примечание
> When using the yellow CANbus cable, Cummins® Part Number 5299804, power extension cable, the lights on the component will begin flashing approximately 15 seconds after the system power is turned on.

#### Throttle Control Processor Module, EEC3

- Insert the power jumper plug into the 12 pin connector labeled “CP Enable” in order to activate the processor.

Power Jumper Plug:

- EEC3 - 24 volt Cummins® Part Number 5299802
- EEC3 - 12 volt Cummins® Part Number 5299803.

#### Throttle Control Processor Module, EEC4

- Insert the power jumper plug into either the port or starboard 12 pin connector labeled “Gear Shift” in order to activate the processor.

Power Jumper Plug:

- EEC4 - Cummins® Part Number 5299801.

> [!note] Note · Примечание
> Once the jumper is plugged in, power is immediately supplied to the throttle control processor module from unswitched battery supply. The keyswitch is bypassed and no longer sends a signal to turn the power on. The throttle control processor module enable relay should audibly “click” as it powers up when the jumper is plugged in. The lights on the lever control station will begin flashing approximately 15 seconds after the jumper is plugged in.

Remove the jumper plug to turn the system power “OFF” once power is verified to the control system component.

![[15a00031.png]]

3) Connect the component programming cable to the programming pins. The throttle control processor module **must** be disassembled in order to access the programming pins. Remove the back cover from the throttle control processor module by removing the screws, mounting standoffs, and grommets.

![[15a00032.png]]

Connect the programming cable connector, Cummins® Part Number 5299799, to the programming pins. The programming pins are located on the circuit board at the middle top side opposite the external harness connectors.

![[15a00033.png]]

4) Use component software download tool (ICP2-Portable Programmer) to download software to the component. See Download Step section for details.

![[ck800wa.png]]

5) Assemble and install the throttle control processor module. Make sure the sealing gasket is positioned correctly and install the back cover to the throttle control processor module. Install the screws, mounting standoffs, and grommets.

![[15a00032.png]]

Install the throttle control processor module. Refer to Procedure 015-055 in Section 15.

6) Configure the control system component. Test and validate the control system for proper operation. See Finishing Steps section.

![[15500009.png]]

### Download

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, do not touch the electrical supply wires or component while the testing procedure is in progress.

> [!warning] CAUTION · Осторожно
> Before updating software in any control system component, verify that the Vessel Control System is completely operational. It is also important to test and document the configuration settings and vessel personality, if needed, of the component. See Preparatory Steps Section above.

The process of updating the software in the control system component is as follows:

1) Connect component software download tool (ICP2-Portable Programmer) (1) to the cable (2) connected to the programming pins on the control system component. The programming cable will vary depending on the specific component.

2) Turn the system power “ON”, engine OFF, and verify the control system component is receiving power.

![[15a00034.png]]

3) Press and release the “PWR” button (1) to activate the programmer. The “Power” light will illuminate when the programmer is on.

> [!note] Note · Примечание
> ICP2-Portable Programmer can be powered by internal batteries or by computer using the USB cable, Cummins® Part Number 5299884.

4) Press and release the “ENV” button (2) to select the programming environment which you wish to download to the component. The light for the selected environment will illuminate.

5) Press and release the “GO” button (3) to begin the download process. The “PASS” and “FAIL” lights will be illuminated while the component is being programmed.

> [!note] Note · Примечание
> When the download successfully completes, the “PASS” light will be on alone.

6) Turn the system power “OFF” to the control system component.

7) Press and release the “PWR” button to turn off the programmer. Remove component software download tool (ICP2-Portable Programmer) and cable from the component programming pins.

8) Update the datatag on the component with the software file name and version by striking through the old version and writing the new information. [[326-015-075 — Component Software Management|Refer to Procedure 015-075 in Section 15]] for details about software file name format.

9) Assemble and install the component. See section above for details.

![[15a00035.png]]

### Troubleshooting

If unable to connect the ICP Application with the ICP2-Portable Programmer, try the following:

1. Before opening the application, leave the USB cable plugged into the programmer for one minute to allow time for the computer to recognize the programmer.
2. Verify the USB cable is plugged in securely.
3. Verify the power light is coming on the ICP2-Portable Programmer.
4. Verify the correct configuration settings and USB COM port is selected. See Setup Information Step section.

![[ck800wa.png]]

If unable to transfer a file from the computer to the ICP2-Portable Programmer, try the following:

1. Verify the file has a.pj2 extension.
2. Get the file from the Marine Panel Firmware Updates - Cummins Inboard Joystick webpage (https://quickserve.cummins.com/qs3/qsol/service/marine/mpf\_joystick.html), save to a computer, and try again. The file may have become corrupt or may have been modified. Files modified from an unauthorized source will **not** read correctly and can **not** be downloaded.

> [!note] Note · Примечание
> [https://quickserve.cummins.com/qs3/qsol/service/marine/mpf\_joystick.html](https://quickserve.cummins.com/qs3/qsol/service/marine/mpf_joystick.html)

![[ck800wa.png]]

If unable to transfer a file from the ICP2-Portable Programmer to the control system component, try the following:

1. Verify the ICP2-Portable Programmer batteries are fresh or it is powered by the USB cable.
2. Verify the control system component is receiving power.
3. Verify the correct programming cable is being used for the control system component.
4. Verify the programming cable is connected properly to the programmer and the control system component programming pins.
5. Verify the correct environment is selected for download from the programmer to the control system component.
6. A.pj2 extension file from Marine Panel Firmware Updates - Cummins Inboard Joystick webpage **must** be used. Get the file from the Marine Panel Firmware Updates - Cummins Inboard Joystick webpage, save to a computer, transfer to the programmer, and try again. The file may have become corrupt or may have been modified. Files modified from an unauthorized source will **not** read correctly and can **not** be downloaded.

![[ck800wa.png]]

### Finishing Steps

> [!warning] CAUTION · Осторожно
> After updating software in any control system component, verify that the Vessel Control System is completely operational, test and update the configuration settings of the component.

After software file download, follow the alarm/fault code or the appropriate troubleshooting symptom tree in order to understand issues.

For an inboard joystick vessel, it will also be necessary to confirm the vessel personality is working correctly and is the appropriate personality for the application.

After component software update, refer to the following procedures for testing and configuration setup information:

- Refer to Procedure 015-051 in Section 15 for the lever control station.
- Refer to Procedure 015-052 in Section 15 for the inboard joystick.
- [[326-015-054 — Vessel Configuration|Refer to Procedure 015-054 in Section 15]] for the vessel configuration.
- Refer to Procedure 015-055 in Section 15 for the throttle control processor module.
- Refer to Procedure 015-056 in Section 15 for the thruster interface module.
- Perform a sea trial to verify proper function. Refer to Procedure 015-046 in Section 15.

![[ck800wa.png]]
