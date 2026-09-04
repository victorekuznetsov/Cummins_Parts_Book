---
type: "Инструкция по установке"
doc: "5414612"
title_en: "Route Parameter Manager Kit Installation Instructions"
released: "2016-11-14"
modified: "2018-10-04"
figures: 61
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/install_inst/5414612.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/install_inst/5414612.pdf"
tags:
  - "документ/установка"
---

# Route Parameter Manager Kit Installation Instructions

> [!abstract] Инструкция по установке · `5414612`
> **Даты:** выпущен 2016-11-14 · изменён 2018-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/install_inst/5414612.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/install_inst/5414612.pdf)

## Route Parameter Manager Kit Installation Instructions

**Table of Contents**

1. Product Affected
2. Introduction
3. Parts Required
4. Installation Tools
5. Installation Instructions
6. Associated Publications

**Product Affected**

| Table 1, Product Affected |  |  |
|---|---|---|
| Engine Model | Model Year | Control Parts List (CPL) |
| ISX15 CM2350 X101 | 2013 | 3937 |
| 2015 | 4583 |  |
| 2016 | 4586 |  |
| 2016 | 4761 |  |
| X15 CM2350 X114B | 2017 | All |

**Introduction**

This document provides installation instruction and compatibly information for the Route Parameter Manager kit.

**Parts Required**

| Table 2, Required Parts |  |
|---|---|
| Part Description | Part Number |
| Kit, Route Parameter Manager | 5406053 |

**Installation Tools**

| Table 3, Required Tools for Installation |  |
|---|---|
| Tool Description | Tool Part Number |
| INLINE™ 7 Data Link Adapter Kit | 5299899 |
| Data Link Adapter For Split Network | 5394863 |
| INSITE™ Electronic Service Tool Software Kit | 3886388 |
| Cummins Guidanz™ Electronic Service Tool | - |
| Multimeter | 3164488 or equivalent |
| Electrical Test Lead Kit | 4919115 |

**Installation InstructionsPersonal Protection Equipment (PPE)**

- Completing a Job Safety Assessment (JSA) prior to performing work helps identify job safety hazards and prevent incidents.
- To reduce the possibility of personal injury, personal protective equipment (PPE) **must** be utilized. Reference General Safety Instructions Procedure 204-006 in Section I of the corresponding Service Manual.

**General Information**

- Route Parameter Manager will facilitate addition of several new fuel economy features including predictive cruise control.
- Cummins Inc. offers two solutions for Route Parameter Manager kit installation:

**Network Identification**

Three distinct installation configurations exist:

- 250K baud network installation for 2013-2015 engines
- 500K baud network installation for 2016 and newer engines
- Split network installation for 2016 and newer engines

The following **must** be completed for proper Route Parameter Manager operation:

- Route Parameter Manager hardware installed on correct vehicle data link network.
- Route Parameter Manager enabled in engine control module (ECM) configuration using INSITE™ electronic service tool Features and Parameters.

250k Baud Network Installation For 2013-2015 Engines

- Route Parameter Manager hardware is compatible with 250K baud public data link network.

500k Baud Network Installation For 2016 And Newer Engines

- Identify engine is communicating on 500K baud network with vehicle components.
- Compare DO option used on engine, where Route Parameter Manager is to be installed, with DO options listed in table. If DO option is listed, this indicates a 500k baud network. Proceed with installation.
- Route Parameter Manager hardware **must** be installed on 500K baud public data link network.

| DO Options for 500K Baud Network: International, Freightliner, and Western Star |  |
|---|---|
| 2016 Engines | 2017 Engines |
| DO10165 | DO10231 |
| DO10166 | DO10232 |
| DO10171 | DO10279 |
| DO10176 | DO10281 |
| - | DO10299 |
| - | DO10300 |

**Split Network Installation For 2016 And Newer Engines**

- Verify engine is communicating on Split network with vehicle components.
- Compare DO option used on engine, where Route Parameter Manager kit will be installed, with DO options listed in table. If DO option is listed, this indicates a split network. Proceed with installation.
- Route Parameter Manager hardware **must** be installed on 250K baud Vehicle data link network.

| DO Options for Split Network: Peterbilt, Kenworth, and Volvo |  |
|---|---|
| 2016 Engines | 2017 engines |
| DO10083 | DO10094 |
| DO10087 | DO10230 |
| DO10088 | DO10280 |
| DO10090 | DO10282 |
| - | DO10301 |

> [!note] Note · Примечание
> Trucks equipped with split network on 2016 and newer engines Cummins® communication adapter, Part Number 5394863, for Cummins INLINE™ 7 Data Link Adapter will be required to enable communication with Route Parameter Manager.

**General Preparatory Steps**

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect batteries. See equipment manufacturer service information.

![[ck800wa.png]]

**Installation Outline**

- Identify vehicle network.
- Identify original equipment manufacturer (OEM) terminating resistor location.
- Identify hardware layout in Preparation for Installation Section.
- Install Route Parameter Manager hardware.
- Verify software requirements have been met.

![[nobox.png]]

**Vehicle Network Identification**

- Identify if vehicle network is 250k, 500k, or split network using General Information section above.

![[nobox.png]]

**Terminating Resistor Location**

- Identify terminating resistor location based on information provided below and based on cab option and vehicle manufacturer.
- If cab option is **not** listed, reference OEM manuals for vehicle network terminating resistor location.

![[nobox.png]]

Peterbilt™ Terminating Resistor Location

- Vehicle network terminating resistor can be found inside dash near diagnostic connector.
- Connector located in dash behind key switch panel approximately 30 cm \[ 12 in \] up wiring harness.

![[19r99382.png]]

> [!warning] CAUTION · Осторожно
> Cummins® test leads must be used in connection points to prevent damage to OEM connectors and terminals.

Verify correct resistor has been found by checking continuity from terminating resistor connection to 9-pin service connector.

- For 2013 – 2015 engines with 250K baud network, use pins C and D on 9-pin service connector to check for continuity to terminating resistor connector.
- For 2016 and newer engines with split network, use pins F and G on 9-pin service to check for continuity to terminating resistor connector.
- Use of multimeter will be required to check continuity between terminating resistor location and 9-pin service connector.
- Cummins® Y adapter, Part Number 5394179, **must** be used for Peterbilt™ applications.

![[19400739.png]]

Volvo® Terminating Resistor Location

- Vehicle network terminating resistors is located near fuse/relay center in vehicle cab.

![[19r99381.png]]

> [!warning] CAUTION · Осторожно
> Cummins® test leads must be used in connection points to prevent damage to OEM connectors and terminals.

- Verify correct resistor found by checking continuity from terminating resistor connection to 9-pin service connector.
- For 2013 – 2015 engines with 250K baud network, use pins C and D on 9-pin service connector to check for continuity to terminating resistor connector.
- For 2016 and newer engines with split network, use pins F and G on 9-pin service to check for continuity to terminating resistor connector.
- Use multimeter to check continuity between terminating resistor location and 9-pin service connector.
- Cummins® Y adapter, Part Number 5394177, **must** be used for Volvo® applications.

![[19400739.png]]

International® Terminating Resistor Location

> [!warning] CAUTION · Осторожно
> Cummins® test leads must be used in connection points to prevent damage to OEM connectors and terminals.

- Vehicle public data link are to be accessed using splice packs located at center console.
- Verify correct splice pack by checking continuity from splice pack connection to 9-pin service connector.
- For 2013 and newer engines, use pins C and D on 9-pin service connector to check for continuity to splice pack.
- Use multimeter to check continuity between terminating resistor location and 9-pin service connector.
- Cummins® Y adapter, Part Number 5394178, must be used for International® applications.

![[19400739.png]]

Freightliner® Terminating Resistor Location

- Vehicle network terminating resistors is located in vehicle center console on passenger side of dash.

![[19r99383.png]]

> [!warning] CAUTION · Осторожно
> Cummins® test leads must be used in connection points to prevent damage to OEM connectors and terminals.

> [!note] Note · Примечание
> Freightliner is **not** utilizing split data link network in their chassis.

- For engines with 250K baud or 500K baud network, use pins C and D on the 9-pin service connector to check for continuity to terminating resistor connector.

![[19400739.png]]

- Verify correct resistor found by checking continuity from terminating resistor connection to 9-pin service connector.
- Use multimeter to check continuity between terminating resistor location and 9-pin service connector.
- Freightliner® Y adapter, Part Number, 5394177 **must** be used for Freightliner® applications.

![[nobox.png]]

Kenworth™ Terminating Resistor Location

- Vehicle network terminating resistor located inside dash behind tachometer.

![[19r99384.png]]

> [!warning] CAUTION · Осторожно
> Cummins® test leads must be used in connection points to prevent damage to OEM connectors and terminals.

Verify correct resistor found by checking continuity from terminating resistor connection to 9-pin service connector.

- For 2013 – 2015 engines with 250K baud network, use pins C and D on 9-pin service connector to check for continuity to terminating resistor connector.
- For 2016 and newer engines with split network, use pins F and G on 9-pin service to check for continuity to terminating resistor connector.
- Use multimeter to check continuity between terminating resistor location and 9-pin service connector.
- Cummins® Y adapter, Part Number 5394179, **must** be used for Kenworth™ applications.

![[19400739.png]]

**Preparation for Installation**

> [!warning] CAUTION · Осторожно
> When installing Route Parameter Manager module harness, avoid any pinch point or sharp edges of components that could cause damage.

> [!note] Note · Примечание
> Exact location of components will vary by OEM.

Need to locate following connection points:

- Location for Route Parameter Manager Module
- Public data link terminating resistor location
- Vehicle fuse panel location
- GPS antenna location and routing

![[nobox.png]]

- Route Parameter Manager Module **must** be mounted inside vehicle cab and protected from outside.
- Route Parameter Manager Module ideal mounting location is in center console of vehicle cab in foot rest area.
- Recommended mounting location of Route Parameter Manager Module is in lower center section of dashboard behind decorative covers.
- Remove dashboard decorative panels to gain access if needed. See equipment manufacturer service information.
- Verify Route Parameter Manager Module wiring harness and GPS antenna cable can reach Route Parameter Manager Module and be connected easily.
- Temporarily route data link connection trunk of Route Parameter Manager Module harness to reach terminating resistor found in previous steps. Remove dashboard decorative panels to gain access if needed. See equipment manufacturer service information.

![[19l00137.png]]

- Temporarily route power and USB trunk of route parameter harness to reach fuse panel in vehicle cab. Remove dashboard decorative panels to gain access if needed. See equipment manufacturer service information.

![[19l00136.png]]

- Verify harness is able to reach terminating resistor and fuse panel from desired Route Parameter Manager Module location.

![[nobox.png]]

- Temporarily place GPS antenna on front/top side of dashboard. Verify GPS antenna is unobstructed.

![[19l00148.png]]

- Temporarily route GPS antenna wire from GPS antenna to Route Parameter Manager Module.
- GPS cable should be routed along left side of dashboard or behind dashboard if possible.
- For dashboard decorative panels removal instructions, see equipment manufacturer service information.
- Remove any slack in wiring harness.

![[nobox.png]]

**Route Parameter Manager Hardware Installation**

After completion of temporary installation of all components and verification that all harnesses and wires can reach Route Parameter Manager Module:

- Permanently mount Route Parameter Manager Module in vehicle cab with Velcro® tape (provided in kit) or wire tie (**not** included in kit).

![[nobox.png]]

- Identify spare fuse in vehicle fuse panel, which has constant power (also referred to as “Battery”).
- Most vehicle fuse panels have fuse designation diagrams, fuse locations with switched power supply are labeled “Battery” or “Spare Battery”. Find fuse location that is **not** populated.
- Use of multimeter may be required to verify power availability at selected fuse location and powered side of fuse.

![[19r99388.png]]

- “Battery” power adapter is red wire.
- There are two fuse blade adapters available:
- Select appropriate size of fuse adapter for harness “Power” input.

![[19r99386.png]]

- Connect fuse adapter wire to Route Parameter Manager Module wiring harness blade connector, battery power connector made with red wire.
- If extra wire remains, wire **must** be coiled and tacked to prevent damage to fuse adapters.

![[19l00154.png]]

- Insert fuse adapter into selected fuse location.
- Verify fuse tapper wires are tight and supported and do **not** droop or sag.
- **Only** one side of fuse opening will have power from key switch. Insert fuse adapter into powered side of fuse mounting location.

![[19l00142.png]]

- Identify spare fuse in vehicle fuse panel, which has switched “key-on” and “key-off” power (also referred to as “ignition”).
- Most vehicle fuse panels have fuse designation diagrams, fuse locations with constant power supply are labeled “Ignition”, “Switched”, “KEYON” or “Spare Ignition”. Find fuse location that is **not** populated.

![[19r99388.png]]

- “Key-ON” power adapter is blue wire.
- There are two fuse blade adapters available:
- Select appropriate size of fuse adapter for harness “Key-ON” input.

![[19r99387.png]]

- Connect fuse adapter wire to route parameter module harness blade connector, Key-ON power connector made with blue wire.
- If extra wire remains, wire **must** be coiled and tacked to prevent damage to fuse adapters.

![[19l00154.png]]

- Insert fuse adapter into selected fuse location.
- Verify fuse tapper wires are tight, supported, and do **not** droop or sag.
- **Only** one side of fuse opening will have power from battery. Insert fuse adapter into powered side of fuse mounting location.

![[19l00142.png]]

- Mount map update USB connector next to cab fuse panel for ease of access and consistent location.
- **Always** contact equipment owner for approval prior to any modifications.

![[nobox.png]]

- Find suitable location for ground wire connection.
- Verify direct metal-to-metal contact between ground wire terminal and cab structure.
- Connect ground wire to cab ground.

> [!note] Note · Примечание
> If eyelet terminal (ground lug) is smaller, replace eyelet terminal with appropriate size.

![[19l00155.png]]

- Support Power and USB trunk of Route Parameter Manager Module harness with wire ties.
- If extra wire remains, wire **must** be coiled and secured to prevent damage.

![[nobox.png]]

- Find terminating resistor identified in Terminating Resistor Location section above.
- Remove terminating resistor from OEM public/vehicle data link harness. Do **not** discard terminating resistor.

![[19r99389.png]]

- Install OEM terminating resistor to mating side of Y-adapter, identified and selected in Terminating Resistor Location section above.
- Connect other side of Y-adapter to OEM data link harness.

![[19r99390.png]]

- Connect Y-adapter to Route Parameter Manager Module harness data link connector.
- There are two connectors on Route Parameter Manager Module harness:
- Reference General Information section to identify network speed by application.
- Connect Y-adapter to correct connector of Route Parameter Manager Module wiring harness.

> [!note] Note · Примечание
> Selection of incorrect data link network speed will cause active Fault Codes 6575 and 6753.

![[19r99391.png]]

- Support data link connection trunk of route parameter manager harness with wire ties.
- If extra wire remains, wire **must** be coiled and secured to prevent damage to fuse adapters.

![[nobox.png]]

- Clean dashboard mounting surface with alcohol swab included in kit before attaching GPS antenna.
- Attach GPS antenna to dashboard using double sided tape. GPS antenna cable **must** be pointing down once antenna is mounted on dashboard.
- GPS antenna **must** be located on dashboard near windshield to be able to receive satellite signal.
- Improper mounting of GPS antenna will cause incorrect position readings for route parameter manager.

![[19l00148.png]]

- Secure GPS antenna cable with wire ties behind dashboard covers.
- Cutting GPS antenna cable is **not** permitted.
- Mount Route Parameter Manager module with double-sided tape or wire ties to cab substructure.
- Verify Route Parameter Manager module has appropriate support and will **not** become loose over time.

![[nobox.png]]

- Connect square black connector of harness to Route Parameter Manager module.
- Verify locking lever is turned 90 degrees as connector is inserted and snaps past locking tab.

![[19l00151.png]]

- Connect blue GPS antenna connector to blue plug on Route Parameter Manager module.
- Verify GPS antenna connector has fully snapped into place.

![[19l00139.png]]

- Connect USB cable connector of wiring harness to Route Parameter Manager module.

![[19l00138.png]]

- Install all cab decorative covers removed in previous steps.
- For decorative cover installation instructions, see equipment manufacturer service information.

![[nobox.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect batteries. See equipment manufacturer service information.

![[ck800wa.png]]

**Route Parameter Manager Software Installation**

After all hardware is installed in cab, software operations **must** be performed to complete installation:

- If required, install engine control module (ECM) calibration.
- Verify engine ECM configuration settings.
- Check Route Parameter Manager module software version and update if required.
- Check Route Parameter Manager module map version and update if required.
- Check for active or inactive fault codes in ECM.

See sections below for detailed instructions to complete the steps above.

> [!note] Note · Примечание
> Map updates and Route Parameter Manager software updates are required **only** if identified as warrantable requirement in ECM Calibration Revision History on QuickServe® Online (QSOL). If update is available, but is **not** listed as warrantable requirement, consult equipment owner, as work associated with updates will be an additional charge to equipment owner.

![[nobox.png]]

**Install Engine ECM Calibration Code**

- Route Parameter Manager available in two variations:
- For engines built prior to 1 January 2017, engine ECM calibration code update is required.
- For X15 CM2350 X114B engine built after January 2017, ECM calibration code update is **not** required.
- Reference QuickServe® Online (QSOL) to acquire latest ECM calibration code availble for engine serial number (ESN).

![[nobox.png]]

**Verify Engine ECM Configuration Settings**

- If new ECM calibration is required, perform ECM calibration update first.
- After ECM calibration is installed, verify settings in Features and Parameters section and modify if settings do **not** match table below.
- INSITE™ electronic service tool version 8.1.2 is required to see correct parameters in ECM.

| Features and Parameters | Manual Transmission with Route Parameter Manager | AMT with Route Parameter Manager |
|---|---|---|
| Cruise Control | Enable | Enable |
| Predictive Cruise Control Maximum Negative Offset | 3 mph | 3 mph |
| Predictive Cruise Control Maximum Positive Offset | 3 mph | 3 mph |
| Cruise Control Version | Predictive | Predictive |

![[nobox.png]]

**Check Route Parameter Manager Module Software Version and Update**

- Turn keyswitch to OFF position.
- Connect Cummins INLINE™ 7 Data Link Adapter to vehicle service tool connector.
- Turn keyswitch to ON position.
- Launch Cummins Guidanz™ electronic service tool on mobile device and connect to Cummins INLINE™ 7 Data Link Adapter via Bluetooth connection.
- Use Cummins INLINE™ 7 Data Link Adapter serial number found behind device to pair with mobile INSITE™ device.
- Completion of Route Parameter Manager module calibration update can take up to one hour. Vehicle batteries and any handheld electronic device used should have a constant power supply for duration of procedure.

> [!note] Note · Примечание
> Cummins INSITE™ electronic service tool installed on Personal Computer will **not** be able to perform map update procedure.

> [!note] Note · Примечание
> Units equipped with split network on 2016 and newer engines Cummins® data link adapter, Part Number 5394863, for Cummins INLINE™ 7 Data Link Adapter will be required to enable communication with Route Parameter Manager Module.

![[19800470.png]]

- From main screen of Cummins Guidanz™, select “Route Parameter Manager”.

![[19l00159.png]]

- From options available on screen, select “Calibrate RPM”.

![[19l00160.png]]

- INSITE™ mobile will perform check between existing software installed in Route Parameter Manager module and software available in Cummins® database.
- If new software is available, select “Download RPM ECM Code”.
- Access to smart device storage will be required.

> [!note] Note · Примечание
> Active connection to WIFI network or cellular network data services will be required to check for ECM calibration code update availability. When using cellular network, additional data charges may apply.

![[19l00161.png]]

- Cummins Guidanz™ will download Route Parameter Module ECM calibration code to smart device storage.
- Access to smart device storage with 10 mb of storage will be required.

![[19l00162.png]]

- Select “Install RPM ECM Code” to initiate calibration download to Cummins® Route Parameter Manger module.

![[19l00163.png]]

- When calibration process is complete, Cummins Guidanz™ will perform last check between calibration available in database and calibration installed in Route Parameter Manager module.

> [!note] Note · Примечание
> Active connection to WIFI network or cellular network data services will be required to check for Route Parameter Manager module ECM calibration code update availability. When using cellular network, additional data charges may apply.

![[19l00164.png]]

- **Check Route Parameter Manager Module Map Version and Update**

- Turn keyswitch to OFF position.
- Connect Cummins INLINE™ 7 Data Link Adapter to vehicle service tool connector.
- Turn keyswitch to ON position.
- Launch Cummins Guidanz™ electronic service tool on mobile device and connect to Cummins INLINE™ 7 Data Link Adapter via Bluetooth connection.
- Use Cummins INLINE™ 7 Data Link Adapter serial number found on back of device to pair with mobile INSITE™ device.
- Completion of map update can take up to one hour. Vehicle batteries and any handheld electronic device used should have a constant power supply for duration of procedure.

> [!note] Note · Примечание
> Cummins INSITE™ electronic service tool installed on personal computer will **not** be able to perform map update procedure.

> [!note] Note · Примечание
> Units equipped with split network on 2016 and newer engines Cummins® data link adapter, Part Number 5394863, for Cummins INLINE™ 7 Data Link Adapter will be required to enable communication with Route Parameter Manager.

![[nobox.png]]

- From main screen of Cummins Guidanz™ electronic service tool, select: “Route Parameter Manager”.

![[19l00159.png]]

- From options available on screen, select: “Update RPM Maps”

![[19l00165.png]]

- Cummins Guidanz™ will perform check between existing map installed in Route Parameter Manager and map available in Cummins® database.
- If new map available, use of personal computer will be required to download map file to USB flash drive.

> [!note] Note · Примечание
> Active connection to WIFI network or cellular network data services will be required to check for the map update availability. When using cellular network additional data charges may apply.

![[19l00161.png]]

- Download map from Cummins® database. Use a personal computer to download map from link below.

> [!note] Note · Примечание
> [https://www.cummins.com/support/electronic-service-tools-support/adepttm-support](https://www.cummins.com/support/electronic-service-tools-support/adepttm-support)

- Follow on-screen instructions to complete map file download.
- Unzip map file to USB flash drive.
- Map file **must** be saved to USB flash drive in "\\eHorizon\_map\\" folder in folder root directory.

> [!note] Note · Примечание
> Creation of “eHorizon\_map” folder on USB flash drive main directory is required.

USB flash drive has minimum requirements that have to be met to function properly during map update process:

- Flash drive **must** be no bigger than 4 GB in size.
- Flash drive **must** be formatted in FAT32 partition.

![[nobox.png]]

- With keyswitch in ON position,connect USB flash drive to Route Parameter module USB cable.

For first fit installed Route Parameter Manager modules:

- For cable locations, see equipment manufacturer service information.

For aftermarket kit installed by Cummins® Service Location:

- USB cable should be located in the cab fuse box and marked “Route Parameter Module Map update”.
- Using Cummins Guidanz™ service tool select “Install Map Files” to initiate file transfer from USB flash drive to Route Parameter Manager module.
- Completion of map update can take up to one hour. Vehicle batteries and any handheld electronic device used should have a constant power supply for duration of procedure.

![[19l00168.png]]

**Check for Active or Inactive Fault Codes in Engine ECM**

- Connect INSITE™ electronic service tool and verify there are no active fault codes.
- Installation is successful if neither FC 6575 or FC 6753 come active with vehicle keyswitch ON for two minutes.
- Activation of FC 6575 and FC 6753 during installation is normal.

> [!note] Note · Примечание
> Fault Codes 6575 and 6753 will **not** light a fault lamp and can **only** be seen by reading fault codes from ECM.

![[nobox.png]]

**Finishing Steps**

- Turn keyswitch to OFF position.
- Disconnect Cummins INLINE™ 7 data link adapter from vehicle service tool connector.

![[19800470.png]]

**Associated Publications**

| Table 4, Associated Procedures |  |  |  |  |
|---|---|---|---|---|
| Manual Type | Bulletin Number | Procedure Title | Procedure | Section |
| Service Manual | [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual\|5411181]] | Route Parameter Manager Module | 019-645 | 19 |
| Route Parameter Manager Module Calibration Code | 019-647 | 19 |  |  |
| Route Parameter Manager Module Global Positioning System (GPS) Map | 019-648 | 19 |  |  |

### Document History
