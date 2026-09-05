---
type: "Процедура"
doc: "377-019-648"
title_en: "Route Parameter Manager Module Global Positioning System (GPS) Map"
modified: "2018-10-04"
manuals:
  - "5411181"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-019-648.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-019-648.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Route Parameter Manager Module Global Positioning System (GPS) Map

> [!abstract] Процедура · `377-019-648`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2018-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-019-648.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-019-648.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- INLINE™ 7 Data Link Adapter Kit, Part Number 5299899
- Data link adapter for split network, Part Number 5394863
- Cummins Guidanz™ electronic service tool

#### Additional Service Items

- No additional service items required.

### General Information

> [!note] Note · Примечание
> See the following to download the latest version of the Cummins Guidanz™ electronic service tool. [https://www.cummins.com/support/electronic-service-tools-support/guidanz-support](https://www.cummins.com/support/electronic-service-tools-support/guidanz-support)

> [!note] Note · Примечание
> Due to the number of various smart handheld devices, this procedure has been written to be generic. Not all illustrations within this procedure will represent the application being worked on.

The route parameter manager GPS updates can be performed by Cummins Guidanz™ electronic service tool.

> [!note] Note · Примечание
> Route parameter manager GPS system map updates are available on a yearly basis.

### Preparatory Steps

- Turn the keyswitch to the OFF position.
- Connect the INLINE™ 7 data link adapter to the vehicle service tool connector.
- Turn the keyswitch to the ON position.
- Launch the Cummins Guidanz™ electronic service tool on a mobile device. Connect it to the INLINE™ 7 data link adapter via a Bluetooth connection.

> [!note] Note · Примечание
> INSITE™ electronic service tool can **not** perform the map update procedure.

> [!note] Note · Примечание
> It can take up to one hour to complete the map update. It is recommended there be a constant power supply to the mobile device for the duration of the procedure.

> [!note] Note · Примечание
> It is recommended to have a constant power supply to the vehicle batteries during the update procedure.

### Install

#### Check for Map Update Availability

- From the main screen of the Cummins Guidanz™ electronic service tool, select Route Parameter Manager.

![[19l00159.png]]

- From the options available, select Update RPM Maps.

![[19l00165.png]]

- Cummins Guidanz™ electronic service tool will perform a check between the current map installed in the route parameter manager module and any map available in the Cummins® database.
- If a new map file is available, use a personal computer to download the file to a Universal Serial Bus (USB) flash drive.

> [!note] Note · Примечание
> An active connection to a WI-FI or cellular network is required to check for map update availability. When using a cellular network, additional data charges can apply.

![[19l00166.png]]

#### Download the Map File to the USB Flash Drive

- Download the map from the Cummins® database. Use a personal computer to download the map from: [https://insite.cummins.com/insite/adept/](https://insite.cummins.com/insite/adept/)
- Follow the on-screen instructions to complete the map file download.
- Unzip the map file to the USB flash drive.
- Save the map file to the USB flash drive in the folder: \\eHorizon\_map\\

> [!note] Note · Примечание
> Creation of the "eHorizon\_map" file on the USB flash drive main directory can be required.

> [!note] Note · Примечание
> USB flash drives have minimum requirements which **must** be met in order to function properly during the map update process. The flash drive **must** be no bigger than 4 GB in size. The flash drive must be formatted in FAT32 partition. Maps **must** be stored in the folder "eHorizon\_map" in the root directory of the flash drive.

![[19l00167.png]]

#### Map Update

- Connect the USB flash drive to the route parameter module USB cable.
- For the first fit installed route parameter modules:
- For the Route Parameter Manager Aftermarket Kit installed by a Cummins® Authorized Repair Location:
- Using the Cummins Guidanz™ electronic service tool, select Install Map Files to initiate file transfer from the USB flash drive to the route parameter manager module.

> [!note] Note · Примечание
> It can take up to one hour to complete the map updated. It is recommended there be a constant power supply to the mobile device for the duration of the map update.

> [!note] Note · Примечание
> It is recommended to have a constant power supply to the vehicle batteries during the update procedure.

![[19l00168.png]]

- Once the map transfer is complete, restart the route parameter manager module.
- Turn the keyswitch to the OFF position. Wait 2 minutes.
- Turn the keyswitch to the ON position.

![[19l00169.png]]

- Connect the Cummins Guidanz™ electronic service tool with the route parameter manager.
- Verify map installation was successful, there are no new map updates available, and no fault codes are observed.

![[19l00170.png]]

### Finishing Steps

- Turn the keyswitch to the OFF position.
- Disconnect the INLINE™ 7 data link adapter from the vehicle service tool connector.
- Turn the keyswitch to the ON position.

![[19800470.png]]
