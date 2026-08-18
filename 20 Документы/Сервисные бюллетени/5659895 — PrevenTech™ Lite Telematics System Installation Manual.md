---
aliases:
  - "Руководство по установке телематики PrevenTech™ Lite"
type: "Сервисный бюллетень"
doc: "5659895"
title_en: "PrevenTech™ Lite Telematics System Installation Manual"
title_ru: "Руководство по установке телематики PrevenTech™ Lite"
released: "2020-10-12"
modified: "2024-03-19"
group: "17 - Miscellaneous"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
figures: 20
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5659895.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/5659895.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "тема/miscellaneous"
---

# PrevenTech™ Lite Telematics System Installation Manual
**Руководство по установке телематики PrevenTech™ Lite**

> [!abstract] Сервисный бюллетень · `5659895`
> **Раздел Cummins:** 17 - Miscellaneous
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Даты:** выпущен 2020-10-12 · изменён 2024-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5659895.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/5659895.pdf)

## PrevenTech™ Lite Telematics System Installation Manual

**Table of Contents**

- System and Hardware Overview
- Installation
- Installation Instructions: PrevenTech™ Lite Telematics Hardware
- APPENDIX A: Telematics Box Hardware Specifications
- APPENDIX B: Installation Examples
- APPENDIX C: WIFI Transmission
- APPENDIX D: Waste Electrical and Electronic Equipment Statement

**System and Hardware Overview**

This instruction manual details the installation of the PrevenTech™ Lite telematics system. While efforts have been made to make this manual as comprehensive as possible, installations **must** be tailored to the particular application/equipment model.

The PrevenTech™ Lite Kit contains the following hardware:

- PrevenTech™ Lite telematics box
- Cellular/GPS/WIFI antenna
- Main wiring harness
- Antenna mounting hardware

The PrevenTech™ Lite kit does not contain all the hardware needed for the installation. SIM cards and connection wiring harnesses **must** be purchased separately.

![[17r00859.png]]

Figure 1, PrevenTech™ Lite Kit Hardware

Environmental and physical requirements operation and storage requirements:

| **Table 1, Operation and Storage Requirements** |  |
|---|---|
| **Operation** | **Storage** |
| Circuitry Operation Temperature Range | -5°C to +60°C (23 °F to 140 ˚F) |
| Storage Temperature Range | -30°C to +80°C (86 °F to 176 ˚F) |
| Humidity | Up to 95% - non-condensing |

**Pre-Installation Steps**

Prior to taking the PrevenTech™ Lite hardware to customer site, a bench test must be performed to verify that system is functional and procured SIM card is compatible with system.

1. Register box by contacting CPS team at connectedsol.support@cummins.com. On PrevenTech™ Lite box, provide ID and IMEI numbers. Also, needed are engine serial number (ESN), ECM calibration, hp rating, equipment OEM/model, unit number, location/mine site, and SIM card information.

![[17r00860.png]]

Figure 2, Identification label on Bottom of PrevenTech™ Lite Box

2. Remove telematics box cover and verify that SW2 dip switches are switched off (towards inner position or to left if harness connector is located on top). These switches are internal resistors that are **not** needed.

> [!note] Note · Примечание
> Do **not** change dipswitches on the component labeled SW1 as it will prevent unit from operating.

![[17r00861.png]]

Figure 3, Interior of PrevenTech™ Lite Box (Dip Switch Location Highlighted)

3. Procure 4G GSM SIM card (Micro 3FF size). Verify that there is adequate 4G coverage in the area. When activating the card, the IMEI number on the box label is required. Recommend that the customer and equipment is registered and access to www.preventech.cummins.com is activated. If the customer has **not** ordered SIM cards with active data plan, use a compatible SIM card with activated data plan for operational validation.

4. Install SIM card with contact facing down and notched tab facing outer side of device.

![[17r00862.png]]

Figure 4, Interior of PrevenTech™ Lite Box with SIM Card Installed

5. Inspect and make sure internal batteries are installed and connected.

![[17r00863.png]]

Figure 5, PrevenTech™ Lite Internal Batteries

6. Connect antenna to Telematics box and place in an elevated position to get cellular signal.

7. Connect wiring harness to box. Connect VINPUT lead to 12/24 V power source and GND lead to negative connection. Apply power. After 5 minutes, the green light should be Steady On. The red light should be Flashing (2 seconds OFF – 0 to 5 seconds ON). If the red light is Steady On, it means that there is no cell connectivity. If this occurs, reference Appendix A for troubleshooting.

8. Determine J1939 CAN Bus connection strategy. There are a couple different methods to connect to the engine J1939 CAN Bus. The strategy chosen determines what peripheral hardware needs to be ordered.

- Option 1: Node off OEM J1939 CAN Bus

![[17r00864.png]]

Figure 6, CAN Bus Node

- Option 2: Extend Engine Backbone to Telematics Box Harness

![[17r00865.png]]

Figure 7, Extension Wiring Harness

Connect CAN0 channel on device harness.

9. General installation hardware is not included in the kit. Items required to perform complete installation that are not included in the kit. These items will vary depending on application/model type.

- Zip ties
- Fuse holders
- 3 Amp fuse
- Various electrical terminals/butt splices
- Industrial Velcro
- Gland Nuts
- Additional 18 AWG Wire (if extension of wiring harness leads needed)

**Industrial Procedures**

1. Select J1939 Public CAN Bus 3-Pin Connection.

- It is possible for engines and equipment to have multiple CAN networks within their architecture – Public vs. Private. Identifying the Public J1939 CAN Bus is essential prior to installation of the PrevenTech™ Lite telematics box. To verify the correct CAN Bus has been selected, contact the equipment OEM. Alternatively, check continuity between the selected 3-pin connector and the 9-Pin service connector.

Verify J1939 CAN Bus resistance by measuring between Positive and Negative terminal on the 9-Pin service connector (Pins C and D in figure below). If resistance measurement is 120 ohms, an additional terminating resistor **must** be added to the backbone. If the resistance measurement is less than 60 ohms, then a resistor **must** be removed.

![[17r00866.png]]

Figure 8, Connector Pin Diagram

3. Install PrevenTech™ Lite Telematics box.

- Installation location must meet the following environment criteria:
- Mount Telematics box using either industrial grade Velcro or mounting hardware. Note that if Velcro is used, verify identification label on the back of the PrevenTech™ Lite box is **not** covered. This information might be needed later for identification.

![[17r00867.png]]

Figure 9, Velcro Applied to Rear of PrevenTech™ Lite Telematics Box

4. Connect wiring harness.

- The PrevenTech™ Lite wiring harness has several wires that are not used in the existing configuration. Make the following connections:

![[17r00868.png]]

Figure 10, Harness Breakout

- Connect wiring harness to PrevenTech™ Lite Telematics Box by inserting connector and pushing in lock tab.

![[17r00869.png]]

Figure 11, PrevenTech™ Lite Wiring Harness Connection to PrevenTech™ Lite Telematics Box

5. Install antenna.

- GSM/GP/WIFI antenna **must** be installed on the outside of the equipment, with direct line of sight to the sky.
- Installed at least 40 cm from equipment operator.
- Consider wiring harness routing strategy and proximity to PrevenTech™ Lite Telematics Box.
- Route antenna connectors through gasket, bracket, and retaining nut.
- Secure to bracket and mount using two U-bolts provided.
- Route antenna connectors to PrevenTech™ Lite Telematics box and match the connectors to the correct port on the box.

![[17r00870.png]]

Figure 12, Antenna Harness Connected to Telematics Box and Antenna Mount on Exterior of Application

- Create a strain relief by allowing at least 1 foot of cabling between the antennae ports and the placement of the strain relief.
- Secure wiring harness along route using P-Clips or zip ties. Excess wiring harness should be neatly coiled up and secured to prevent from interfering with other components.

6. Apply power and verify that LED lights are on in accordance with the following tables. If LEDs do not give proper indication, reference Appendix A for troubleshooting steps.

- The green LED will turn on after approximately 30 seconds as the power has been supplied. If the equipment is receiving frames through the CAN0 port, the LED will flash at high speed indicating transmission.

| **Green LED Indicator – CAN Operation** |  |
|---|---|
| **State** | **Indication** |
| Steady on | Operating system initialized |
| Flashing | Data is being transmitted on CAN0 |
| Off | Operating system not initialized |

- The red LED is used to indicate the communication status of the device. During first couple minutes since device has been powered, LED will be off. If the Telematics box has not achieved connectivity, the LED will light up steadily. In contrast, if 4G/GSM connectivity is stable, the LED will flash every 2 seconds.

| **Red LED Indicator – Network Connection** |  |
|---|---|
| **State** | **Indication** |
| Steady on | No 4G/GSM connectivity |
| Flashing (2 seconds OFF – 0 to 0.5 seconds ON) | Stable 4G/GSM connectivity |
| Off | Only first couple minutes after powered on |

- The blue LED is used to indicate Central Processing Unit (CPU) activity status. During the first couple minutes since device has been powered, LED will be off. If Telematics box has achieved connectivity LED with flash dependent on CPU activity. In contrast, if Telematics box LED will be off when connectivity has not been achieved.

| **Blue LED Indicator – CPU Operation** |  |
|---|---|
| **State** | **Indication** |
| Steady on | Operating system initializing |
| Flashing (dependent on CPU activity) | CPU activity |
| Off | Operating system not initialized |

7. After equipment registration is verified, use PrevenTech™ dashboard to verify GPS location and communication is active. If communication cannot be established, perform troubleshooting steps or contact Cummins CARE.

**APPENDIX A: Troubleshooting**

STEP 1A. Check for faulty equipment visibility on PrevenTech™ dashboard.

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Log on to PrevenTech™ dashboard, https://preventech.cummins.com; Check dashboard for operation | Is equipment in question visible on dashboard? **Yes** | **2A** |
| Is equipment in question visible on dashboard? **No** | **1B** |  |

STEP 1B. Check for visibility of other equipment on PrevenTech™ dashboard.

| **Conditions**: While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check dashboard for visibility of other equipment | Is other equipment visible on dashboard? **YesNote:** Not an issue with dashboard | **2A** |
| Is other equipment visible on dashboard? **No** | **Contact:** PrevenTech™ Regional Support Contact or care.cummins.com |  |

STEP 2. Identify state of LEDs.

STEP 2A. Green LED flashing

| **Conditions:** While equipment is on **Note:** 30 seconds after power is supplied; PrevenTech™ Lite Telematics box green LED will start to flash at high speed when receiving frames through PrevenTech™ Lite Telematics J1939 connection |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect green LED | Is green LED flashing? **YesNote:** Data is being transmitted on PrevenTech™ Lite Telematics box J1939 connection; PrevenTech™ Lite Telematics box should be connected to engine's J1939 connection, reference step **5A** | **2C** |
| Is green LED flashing? **No** | **2B** |  |

STEP 2B. Green LED steady on

| Inspect green LED | Is green LED steady on? **YesNote:** Operating System initialized | **5A** |
|---|---|---|
| Is green LED steady on? **NoNote:** Operating System not initialized | **3A** |  |

STEP 2C. Red LED flashing

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect red LED | Is red LED flashing? **YesNote:** Stable internet connectivity | **Check dashboard configuration informationContact:** PrevenTech™ Regional Support Contact or care.cummins.com |
| Is red LED flashing? **No** | **2D** |  |

STEP 2D. Red LED steady on

| **Conditions:** While equipment is on **Note:** Red LED will be off for the first 5 minutes after power has been supplied to PrevenTech™ Lite telematics box |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect red LED | Is red LED steady on? **YesNote:** No internet connectivity | **6A** |
| Is red LED steady on? **No** | **3A** |  |

Step 2E. Blue LED Flashing

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect blue LED | Is blue LED Flashing? **Yes** | **CPU activity presentRepair Complete** |
| Is blue LED flashing? **No** | **2F** |  |

Step 2F. Blue LED Off

| **Conditions:** While equipment |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect blue LED | Is blue LED off? **No** | **Operating System is initializingRepair Complete** |
| Is blue LED off? **Yes** | **3A** |  |

STEP 3. Identify state of power supply.

> [!note] Note · Примечание
> PrevenTech™ Lite Telematics box internal cartridge battery will hold charge for a period of time after external power has been removed and will function as intended. When troubleshooting the external power supply, disconnect PrevenTech™ Lite Telematics box internal cartridge battery. If needed, refer to Step 4 for PrevenTech™ Lite Telematics box internal battery fault finding, i.e., data time stamp variation on PrevenTech™ dashboard.

STEP 3A. Fuse condition

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect inline fuse | Is fuse open? **YesRepair:** Replace fuse | **Repair Complete** |
| Is fuse open? **No** | **3B** |  |

STEP 3B. Power supply, ignition, and chassis ground wire condition

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Carefully inspect main harness wiring condition Reference Appendix H above. | Are power supply, ignition, and chassis ground wires in good condition with no damage, i.e. no tears? **Yes** | **3C** |
| Are power supply, ignition, and chassis ground wires in good condition with no damage? **NoRepair:** Replace PrevenTech™ Lite telematics box main harness | **Repair Complete** |  |

STEP 3C. Power supply, ignition, and chassis ground connections

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Carefully inspect main harness connections | Are power supply, ignition, and chassis ground wires connected? **Yes** | **3D** |
| Are power supply, ignition, and chassis ground wires connected? **NoRepair:** Connect wire(s) that are not connected | **Repair Complete** |  |

STEP 3D. Main harness connection to PrevenTech™ Lite Telematics box

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect main harness connection to PrevenTech™ Lite telematics box. Reference Step 5 in Installation Instructions: PrevenTech™ Lite Telematics Hardware above. | Is the main harness connected securely to PrevenTech™ Lite telematics box? **Yes** | **3E** |
| Is the main harness connected securely to PrevenTech™ Lite telematics box? **NoRepair:** Connect and securely lock main harness | **Repair Complete** |  |

STEP 3E. Condition of LED(s) internal wiring

| **Conditions:** While power is supplied to PrevenTech™ Lite telematics box |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect LED(s) internal wiring, | Are LED(s) on? **NoRepair:** Replace PrevenTech™ Lite telematics box | **Repair complete** |

STEP 4. PrevenTech™ Lite internal battery conditions

STEP 4A. Internal clock (round) battery condition

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check dashboard data time stamps. | Is there ambiguity in the data time stamp/real time clock? **YesNote:** Replace round battery, Reference Figure 5 above. Turn on device and check PrevenTech™ dashboard for functionality | **Repair Complete** |

STEP 5. Equipment J1939 connections

STEP 5A. Inspect equipment and PrevenTech™ Lite Telematics box J1939 connection

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect PrevenTech™ Lite Telematics box J1939 connection with equipment | Is PrevenTech™ Lite Telematics box J1939 plug connected to equipment's J1939 public data connection? **Yes** | **5C** |
| Is PrevenTech™ Lite Telematics box J1939 plug connected to equipment's J1939 public data connection? **No** | **5B** |  |

STEP 5B. Equipment J1939 Public Connection

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure continuity from 9-pin service connector to 3-pin Deutsch connector | Was continuity confirmed? **YesRepair:** Connect PrevenTech™ Lite telematics box J1939 connection to public data J1939 connection on equipment | **Repair Complete** |
| Was continuity confirmed? **NoNote:** Repeat this step until equipment J1939 public connection is located | **Repeat Step** |  |

STEP 5C. Measure equipment resistance

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disconnect the J1939 connection; using the equipment J1939 or 9 Pin service connector measure the equipment resistance, reference Figure 8 above. | Is the measured resistance 60 Ohms? **Yes** | **5E** |
|  | Is the measured resistance 60 Ohms? **No** | **5D** |

STEP 5D. Inspect J1939 backbone terminal resistors

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect J1939 connection terminal resistors; measure resistance. Note: ONLY two 120 Ohms resistors needed in parallel on backbone to achieve a total resistance of 60 Ohms | Is the measured resistance in each resistor 120 Ohms? **Yes** | **5E** |
| Is the measured resistance in each resistor 120 Ohms? **NoRepair:** Discard and replace resistor(s) | **Repair Complete** |  |

STEP 5E. Measure PrevenTech™ Lite Telematics box resistance

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure resistance on PrevenTech™ Lite J1939 connection, reference Figure 8 above. | Is the measured resistance approximately 50 K-Ohms? **No** | **5F** |
| Is the measured resistance approximately 50 K-Ohms? **YesNote:** No PrevenTech™ Lite telematics resistance issue | **Repair Complete** |  |

STEP 5F. PrevenTech™ Lite Telematics box resistance correction

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure resistance on PrevenTech™ Lite J1939 connection | Is the measured resistance approximately 0 Ohms? **YesNote:** Short in box **Repair:** Replace PrevenTech™ Lite Telematics box | **Repair Complete** |
| Is the measured resistance approximately 120 Ohms? **YesRepair:** Ensure internal resistance dip switches are all to the right of the battery. Reference Step 13 in Installation Instructions: PrevenTech™ Lite Telematics Hardware above. | **Repair Complete** |  |

STEP 6. Data transmission to PrevenTech™ dashboard

STEP 6A. Antennae connections

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect antennae connections on PrevenTech™ Lite telematics box, reference Step 5 in Installation Instructions: PrevenTech™ Lite Telematics Hardware above | Are the antennae wires connect securely and correct to PrevenTech™ Lite telematics box? **Yes** | **6B** |
| Are the antennae wires connect securely and correct to PrevenTech™ Lite telematics box? **NoRepair:** Correctly wire the antennae wires to the correct ports and securely connect. | **Repair Complete** |  |

STEP 6B. Condition of antennae wires

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect wires between PrevenTech™ Lite telematics box and antennae round transmitter, reference Step 5 in Installation Instructions: PrevenTech™ Lite Telematics Hardware above | Are one or more antennae wires damaged, i.e. abrasion to conduit, round transmitter physical damage? **YesRepair:** Replace and route antennae to PrevenTech™ Lite Telematics box | **Repair Complete** |
| Are one or more antennae wires damaged, i.e. abrasion to conduit, round transmitter physical damage? **No** | **6C** |  |

STEP 6C. SIM card status

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Remove SIM card Reference Figure 4 above. | Are SIM card and PrevenTech™ Lite telematics box motherboard contacts dirty or dull? **YesRepair:** Clean all contacts, reinstall SIM, and check for data transmission | **Repair Complete** |
| Are SIM card and PrevenTech™ Lite telematics box motherboard contacts dirty or dull? **No** | **6D** |  |

STEP 6D. SIM card data

| **Conditions:** While equipment is off **Note:** Consider using a mobile phone compatible with SIM card, same network provider, to check data functionality; if data transmission is established, replacement of PrevenTech™ Lite telematics box may be necessary |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check data usage with network provider | Has data plan maximum limit been reached? **YesRepair** May consider upgrading to a higher data plan | **Repair Complete** |
| Has data plan maximum limit been reached? **NoRepair:** Corrupt SIM card; obtain another SIM card and re-configure PrevenTech™ Lite Telematics box | **Repair Complete** |  |

**APPENDIX B: Installation Examples**

The following pictures document some of the installations conducted on various applications. These are for reference only. Each installation requires evaluation to determine what the correct strategy is for that particular unit.

![[17r00871.png]]

Figure 13, Connecting into J1939 CAN Bus using Gender Changer and Y Connector

![[17r00872.png]]

Figure 14, Complete System Layout.

**APPENDIX C: WIFI Transmission**

EMD Configuration Utility

EMD is a downloadable configuration program that will be needed to configure mesh network to Telematics device.

Follow the steps below to download the program:

1. Go to [https://www.emd.io/downloads/](https://www.emd.io/downloads/)
2. Click on second prompt called: (Windows Portable, 32bit).
3. Use WinZip and open the program.
4. Password: emd

Connect computer to device using a USB to RS-232 modem adapter and available RS-232 connection on device harness.

![[17r00873.png]]

Figure 15, Device Harness RS-232 Connection.

Launch EMD configuration utility and wait until dialog box appears asking for a serial port to use for communication with device, by default device will communicate at 115200 bps. Select appropriate and click OK button.

![[17r00874.png]]

Figure 16, EMD Configuration Utility Window.

A window pops up asking for a device password. Input correct password and click OK.

> [!note] Note · Примечание
> Password of the device **must** be obtained by contacting PrevenTech™ team.

![[17r00875.png]]

Figure 17, Device Password Input Window.

DNS Server information required from customer's IT department to link devices:

- Mode: Switch to Manual
- IP Address:
- Network Mask:
- Gateway:
- DNS1:
- DNS2:

Under the Network Tab input information gathered in appropriate locations and click Apply.

![[17r00876.png]]

Figure 18, Network Configuration Window.

Alternate WIFI Connection

- Mine site dependent. If the customer would like to use a hard wire connection to an external WIFI hub for transmission, a compatible M8 to RJ45 connection wire (length is dependent on equipment setup) will need to be purchased and connected to Telematics box via M8 Ethernet connector available on device.

![[17r00877.png]]

Figure 19, M8 Ethernet Port Connection.

**APPENDIX D: Waste Electrical and Electronic Equipment Statement**

Electrical and electronic equipment (EEE) and batteries contain materials, components and substances that may be hazardous and present a risk to human health and the environment when waste electrical and electronic equipment (WEEE) and batteries are **not** handled correctly.

Electrical and electronic equipment and batteries are marked with the crossed-out wheeled bin symbol indicating that electrical and electronic equipment and batteries should **not** be disposed of in the regular household waste stream but need to be collected separately. In case batteries contain more than 0,0005% mercury (Hg), 0,002% cadmium (Cd) or 0,004% lead (Pb) (by weight), the corresponding chemical symbol is displayed on the battery. See Figure 20.

![[18r00017.png]]

Figure 20, Waste Type Icons. Left: WEEE; Right: Batteries.

> [!note] Note · Примечание
> The bar below the WEEE bin at left in Figure 20 is recommended to include to prove that a product was made after the 13 August 2005. Alternatively, a date can be included.

Consumers have an important role in recycling this equipment and contributing to the protection of the environment. Follow local recycling regulations to reduce adverse environmental impact in connection with disposal of WEEE and batteries and to increase opportunities for reuse, recycling, and recovery of WEEE and batteries. To facilitate this, free collection points are available in many areas. Users are responsible for removing personal data from electronic devices prior to disposal. If possible, remove old batteries or accumulators from the electronic device before returning for recycling.

### Document History
