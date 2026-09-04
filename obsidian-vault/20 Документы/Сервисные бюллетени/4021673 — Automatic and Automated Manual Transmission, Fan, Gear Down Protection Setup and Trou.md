---
type: "Сервисный бюллетень"
doc: "4021673"
title_en: "Automatic and Automated Manual Transmission, Fan, Gear Down Protection Setup and Troubleshooting"
released: "2007-10-16"
modified: "2016-10-14"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/4021673.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/4021673.pdf"
tags:
  - "документ/бюллетень"
---

# Automatic and Automated Manual Transmission, Fan, Gear Down Protection Setup and Troubleshooting

> [!abstract] Сервисный бюллетень · `4021673`
> **Даты:** выпущен 2007-10-16 · изменён 2016-10-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/4021673.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/4021673.pdf)

## Automatic and Automated Manual Transmission, Fan, Gear Down Protection Setup and Troubleshooting

## Introduction

This Service Bulletin provides troubleshooting information for automatic and automated manual transmissions. Various malfunctions within the Cummins Inc. system can potentially cause erratic shifting and poor shift quality complaints in vehicles equipped with automatic and automated manual transmissions. This Service Bulletin will serve as a guide to help diagnose shifting complaints that can be caused by Cummins Inc. electronic settings or other malfunctions that can cause erratic transmission performance.

This Service Bulletin contains the following sections:

- J1939 datalink communication to the transmission electronic control unit (ECU)
- Adjustable parameter descriptions for features specific to automatic and automated manual transmission performance
- Engine specific troubleshooting procedures for erratic and poor shift quality performance complaints.

## J1939 Datalink Communication

Many automatic and automated manual transmissions communicate to the Cummins® electronic control module (ECM) using the J1939 datalink network. J1939 is a standard high speed datalink that is used in the heavy duty truck industry. It allows communication between multiple ECUs that are mounted within the vehicle. ECU examples include anti-lock brake systems (ABS), electronic dash gauges, multiplexed dash switches, and transmission ECUs. The J1939 network consists of a primary backbone that can extend a maximum of 40 meters. The J1939 network can have a maximum of 30 node connections at a given time. Each node connection can have a maximum stub length of 1 meter \[39 inches\] from the primary network backbone. The Cummins® ECM and transmission ECU exchange vital performance information across this network for proper engine and transmission operation.

Loss of J1939 datalink communication between the Cummins® ECM and the transmission ECU will result in degraded transmission shifting performance. If datalink communication is lost between the Cummins® ECM and the transmission ECU, no fault code will be logged in the Cummins® ECM. The transmission ECU is responsible for logging a fault code for loss of J1939 datalink communication. This fault code will be logged within the transmission ECU and can **only** be read using a transmission-specific electronic service tool, or by flashing out the fault codes using the transmission interface.

![[19803922.png]]

Typical J1939 Datalink Configuration

## Adjustable Feature and Parameter Configuration

Shifting and erratic performance complaints can be caused by incorrect adjustable parameter configurations in the Cummins® ECM. The INSITE™ electronic service tool **must** be used to confirm that adjustable features and parameters are configured correctly. The primary adjustable parameters used to configure the transmission setup include:

- Transmission Setup
- Fan Setup
- Gear Down Protection.

## Transmission Setup

The Transmission Setup feature is used by several other features to determine if the vehicle is in the top gear or one gear down from the top gear. If the current gear ratio is within a small tolerance of the Top Gear Transmission Ratio, or the Gear Down Transmission Ratio, the ECM considers the vehicle to be in-gear at the respective gear.

## Top Gear Transmission Ratio

This parameter defines the top gear ratio of the transmission. Set this parameter to the gear ratio of the top transmission gear. The Top Gear Transmission Ratio **must** be at least 0.01 less than the Gear Down Transmission Ratio.

## Gear Down Transmission Ratio

This parameter defines the gear ratio for one gear down from the top gear. Set this parameter to the gear ratio of the gear one lower then the top gear. The Gear-Down Transmission Ratio parameter **must** be 0.01 more than the Top Gear Transmission Ratio.

## Transmission Type

The Transmission Type parameter defines the transmission type to the ECM. Set the Transmission Type parameter to the type of transmission installed as follows:

- **Manual** - A standard transmission utilizing a clutch actuated by the driver with all gear changes made by the driver.
- **Automatic** - A hydro-mechanically shifted transmission utilizing a torque converter. **Note:** The VSS Anti-Tamper feature **must not** be enabled on any vehicle with an Automatic (with torque converter) transmission. Undesirable operation and faults will result. Set the transmission type to Automatic if the transmission is one of the following:

  - Aisin (all models with a torque converter)
  - Allison (all models with a torque converter)
  - Voith (all models with a torque converter)
  - ZF (all models with a torque converter).

- **Partially Automated** - A transmission, where some, but **not** all, of the gear changes are made by the transmission without additional driver interaction. Set the transmission type to Partially Automated if the transmission is one of the following:

  - Eaton Lightning.

- **Fully Automated** - All gear changes are made by the transmission. The driver **must** actuate the clutch to launch and stop the vehicle. Set the transmission type to Fully Automated if the transmission is one of the following:

  - Eaton Autoshift
  - Meritor SureShift
  - ZF AS-tronic (Euro Markets).

- **Automated without Clutch** - All gear changes are made by the transmission and the driver does **not** actuate the clutch. The clutch is actuated automatically by the transmission. Set the transmission type to Automated without Clutch if the transmission is one of the following:

  - Eaton Ultrashift
  - ZF/Meritor AS-tronic/Freedom (US Market).

## Fan Setup

The Fan Control feature determines fan operation logic with respect to: air condition pressure switch, manual fan switch inputs, engine braking, and output signals to the fan clutch. Each function of this feature operates differently and independently.

## Fan Control

This parameter enables or disables ECM control of the fan clutch. If the ECM should control the fan clutch, set the Fan Clutch Control parameter to Enable. If the Fan Clutch Control parameter is set to Disable, the ECM will **not** control the fan.

## Fan Clutch Logic

The Fan Clutch Logic parameter determines whether the fan clutch engages the fan when receiving a high voltage signal (vehicle battery +) or a low voltage signal (ground). The ECM uses this parameter when sending a fan signal. If the ECM determines the fan should be on, the ECM checks this parameter to determine whether it will use a high or low voltage signal to drive the fan clutch. If the fan clutch engages with a high voltage signal, set this parameter to Active High. If the fan clutch engages with a low voltage signal, set this parameter to Active Low.

## Air Conditioning Pressure Switch Input

The Air Conditioner Pressure Switch Input parameter configures the fan to operate as an air conditioner condenser fan to remove heat from the air conditioner system and reduce air conditioner refrigerant pressure. The OEM installs the Air Conditioner Pressure Switch to monitor at the high-pressure side of the air conditioning system. The fan **must** be installed so that it directs airflow through the air conditioner condenser.

- **Minimum Fan On Time For Air Conditioner Pressure Switch** - This parameter defines the minimum fan-on time when operating in response to air conditioner refrigerant pressure. The ECM runs the fan when the Air Conditioner Pressure switch detects high air conditioner refrigerant pressure. The ECM runs the fan when the Air Conditioner Pressure switch detects high air conditioner refrigerant pressure. Each time the ECM engages the fan due to the Air Conditioner Pressure Switch, it will run for at least the time equal to the Minimum Fan On Time For Air Conditioner Pressure Switch parameter. Once this time expires, the ECM will no longer run the fan due to the Air Conditioner Pressure switch, if the switch indicates acceptable air conditioner pressure. However, the ECM can still run the fan due to some other feature. If the Air Conditioner Pressure Switch fails in an open circuit condition, the ECM will run the fan continuously. Longer times decrease fan cycling, shorter times can increase fuel economy and engine performance.

## Fan Control Switch

The Fan Control Switch function configures the fan to operate as an accessory fan. The fan can operate for a dash mounted manual fan switch, or any OEM determined switch. For example, the fan can operate in response to transmission fluid temperature by installing an accessory switch which opens with high transmission fluid temperature. When a switch opens, disconnecting the appropriate ECM pin from ground, the ECM commands the fan to run. Demand for fan operation, due to the accessory switch, stops when the switch reconnects the pin to ground. The feature runs the fan continuously in an open circuit failure situation. If fan operation, in response to the Fan Control Switch is desired, set the Fan Control Switch parameter to Enable. This is **only** for hard wire operation.

## Fan On with Engine Braking

The Fan On with Engine Braking function configures the fan to operate as an engine braking aid. The parasitic load of the fan increases braking power. Fan operation is demanded, after a short delay, when the engine brakes achieve the 100 percent braking level. The ECM checks the coolant temperature before engaging the fan due to engine braking to make sure the engine does **not** overcool. If fan operation in response to engine brakes is desired, set the Fan Control Engine Braking parameter to Enable.

## Fan Type

The Fan Type parameter defines the type of the fan clutch installed, allowing the ECM to configure its fan control signal. Five types of fan clutches are compatible with the Fan Control feature as defined below.

- **On/Off** - These fan clutches have two fixed operating modes, either full on/off. The ECM will command either full On or full Off with this mode.
- **Variable Speed** - These fan clutches can vary the fan speed over a wide range between off and full engagement. The fan can operate at the fan speed requested by the subsystem, regardless of engine speed, until locked up. A Variable Speed fan clutch **must** be able to utilize a pulse width modulated (PWM) signal of frequency defined by the Variable Speed Fan Frequency parameter, as the variable speed input. These fan clutches are generally hydraulically driven and are controlled by the fluid allowed to pass through the hydraulic drive.

  - **Variable Speed Fan Frequency** - This parameter determines the frequency of the PWM signal controlling the variable speed fan. The variable speed fan is **NOT** frequency controlled, so the frequency is **not** modulated. This parameter has been added to support various variable speed fan controllers which require different frequency settings. Set this parameter to the frequency (in Hz) of the PWM signal required for the variable speed fan clutch used on the vehicle.

- **Electronic Viscous without Speed Sensor** - These fan clutches use a viscous coupling to control the speed of the fan. The volume of viscous fluid in the working chamber of the viscous coupling determines the speed of the fan. The volume of fluid is controlled by the PWM Fan Control signal from the ECM.
- **Electronic Viscous with Speed Sensor** - These fan clutches also use a viscous coupling to control the speed of the fan. In addition, a speed signal from the fan drive is provided to the ECM for use in a closed loop control of the fan speed.
- **Electronic Variable Speed without Speed Sensor** - These fan clutches use the PWM Fan Control signal from the ECM to control the speed of the fan.

| Present Fan Control Types Supported by INSITE™ Electronic Service Tool |  |  |
|---|---|---|
| Fan Type | Engine Applications | Notes |
| On/Off | All | Any On/Off fan application |
| Variable Speed | All | Any Hydraulic Variable Speed |
| Electronic Viscous without Speed Sensor | ISX | Behr E-Visco |
| Electronic Viscous with Speed Sensor | N/A | Horton VMaster Ultra |
| Electronic Variable Speed with Speed Sensor | ISX | BorgWarner Cool Logic |

- **Vehicle Speed Interaction** - The Vehicle Speed Interaction parameter enables or disables vehicle speed interaction with the fan/air conditioner pressure dependency to prevent fan cycling. When the Vehicle Speed Interaction parameter is set to Enable, the ECM enables a special fan-control mode. If the Air Conditioner Pressure Switch triggers a fan event at low vehicle speed in this mode, the ECM will keep the fan On constantly until the vehicle speed exceeds a threshold (e.g. 9.7 kph \[6 mph\]), or the engine is shut down and restarted. This acts in a similar manner to the Minimum Fan On Time for Air Conditioner Pressure Switch parameter, because it does **not** affect fan activation conditions, but prevents fan shutdowns during times when the ECM otherwise would allow it. When the Vehicle Speed Interaction parameter is set to Disable, this function of the fan control feature has no effect on vehicle operation.

## Gear-Down Protection

The Gear-Down Protection feature encourages drivers to remain in the upper gear range by derating available vehicle speed in lower gears. The feature has one derate for 1-gear down from the top gear, and another derate for all gears below that. Additionally, the feature uses a different derate when the engine is under heavy and light loads. This feature will **not** affect vehicles equipped with automatic or automated manual transmissions that are operating under control of the transmission. If an automated manual transmission equipped vehicle is in manual mode, the gear-down protection will be in operation.

## Gear-Down Protection

The Gear-Down Protection parameter enables or disables the Gear-Down Protection feature. If the ECM should apply gear-down derates, set the Gear-Down Protection parameter to Enable.

- **Gear-Down Protection Heavy Load Vehicle Speed and Gear-Down Protection Light Load Vehicle Speed** - The Gear-Down Protection Heavy Load Vehicle Speed parameter and the Gear-Down Protection Light Load Vehicle Speed parameter defines the maximum vehicle speed in lower gears. Set the Gear-Down Heavy Load Vehicle Speed to maximum vehicle speed that should be achieved under heavy load in the first gear below top gear, and set the Gear-Down Light Load Vehicle Speed to the maximum vehicle speed that should be achieved under light load in the first gear below top gear. The Gear-Down Light Load Vehicle Speed parameter **must** be lower than the Gear-Down Heavy Load Vehicle Speed parameter.

## Engine Troubleshooting Procedures for Erratic Transmission Performance

Use the following troubleshooting trees to troubleshoot erratic shifting and poor shift quality with automatic and automated manual transmissions.

Many of the system checks listed below require the use of the appropriate base engine Service Manual for specific diagnostic procedures. See the service manual for specific diagnostic troubleshooting procedures.

## Check for Active Cummins® Fault Codes

- Turn keyswitch ON
- Connect INSITE™ electronic service tool

- Read the fault codes from the Cummins® ECM. All active fault codes **must** be troubleshot first before continuing the troubleshooting process.

- Confirm that no fault codes are active in the Cummins® ECM. See the appropriate fault code troubleshooting procedure for troubleshooting active fault codes.

## Check for Active Transmission Fault Codes

- Turn keyswitch ON
- Connect the transmission scan tool, or use the transmission interface to flash out the fault codes.

- Read the fault codes from the transmission ECU. All active fault codes **must** be troubleshot first before continuing the troubleshooting process.

- Confirm that no fault codes are active in the transmission ECU. Refer to the appropriate OEM transmission fault code troubleshooting procedure for troubleshooting active fault codes.

## Check the Cummins® ECM Code

- Turn keyswitch ON
- Connect INSITE™ electronic service tool.

- Verify that the ECM code that is presently installed in the Cummins® ECM is correct for the application and CPL.

- Confirm the ECM code is correct for the application and CPL.

## Check the OEM J1939 Datalink Communication

- Turn keyswitch ON
- Connect INSITE™ electronic service tool.

- Verify that J1939 datalink communication with INSITE™ electronic service tool is available at the in-cab diagnostic connector.
- If a generic fault code reader is available, read the fault codes from the transmission ECU. Verify that no fault codes are present that can indicate loss of J1939 communication between the transmission ECU and the Cummins® engine ECM.

- J1939 communication **must** be established. Use INSITE™ electronic service tool at the in-cab service tool connection. If communication with the ECM is **not** possible, troubleshoot the OEM J1939 datalink.

## Verify Electronic Feature Setting are Correct

- Turn keyswitch ON
- Connect INSITE™ electronic service tool.

- Use INSITE™ electronic service tool to verify that all adjustable features and parameters are correctly set:

  - Transmission Setup
  - Fan Setup
  - Gear-Down Protection.

- Verify that the electronic features are programmed correctly.
- See the Adjustable Feature and Parameter Configuration section of this Service Bulletin for adjustable parameter information related to the transmission operation.

## Check Engine Fan Configurations

- Turn keyswitch ON
- Connect INSITE™ electronic service tool.

- Incorrect fan configurations can possibly cause erratic shifting of automatic and automated manual transmission. Confirm the following fan configurations are correct:

  - Check to make sure the correct fan clutch is installed on the engine
  - Verify the correct fan is being used on the engine. Fans with the incorrect number of fan blades and fan sizing can cause erratic shifting
  - Verify that the fan drive ratio is correct
  - Use INSITE™ electronic service tool to verify that adjustable parameters related to the fan configuration are set correctly
  - Confirm that the fan is **not** locked on and operates correctly.

- All fan configurations are confirmed to be correct and the fan **must** be operating correctly.

## Check Fuel Inlet Restriction

- Turn keyswitch ON
- Engine running at high idle.

- Measure the fuel inlet restriction.

  - [[35-006-020-tr — Fuel Inlet Restriction|Refer to Procedure For ISM engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, ISM, ISMe and QSM11, Bulletin 3666322.]]
  - Refer to Procedure For Signature/ISX engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, Signature, ISX, and QSX15, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]].
  - Refer to Procedure For ISB and ISBe CM850 engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, ISBe, ISB, and QSB (Common Rail Fuel System), Bulletin 4021271.
  - Refer to Procedure For ISB CM2150 engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, ISB, Bulletin 4021578.
  - Refer to Procedure For ISBe CM2150 engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, ISBe and ISDe CM2150, Bulletin 4021597.
  - Refer to Procedure For ISC, ISCe, ISL, ISLe3 and ISLe4 CM850 engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Troubleshooting and Repair Manual, ISC, ISCe, QSC8.3, ISL, ISle3, ISLe4, and QSL9 Engines, Bulletin 4021418.
  - Refer to Procedure For ISC and ISL CM2150 engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, ISC and ISL CM2150, Bulletin 4021569.

- Confirm that fuel inlet restriction is within specification.
- If fuel inlet restriction is above specification, locate the cause of high fuel inlet restriction. Check the suction-side fuel filter and fuel supply lines.

  - [[35-006-020-tr — Fuel Inlet Restriction|Refer to Procedure For ISM engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, ISM, ISMe and QSM11, Bulletin 3666322.]]
  - Refer to Procedure For Signature/ISX engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, Signature, ISX, and QSX15, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]].
  - Refer to Procedure For ISB and ISBe CM850 engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, ISBe, ISB, and QSB (Common Rail Fuel System), Bulletin 4021271.
  - Refer to Procedure For ISB CM2150 engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, ISB, Bulletin 4021578.
  - Refer to Procedure For ISBe CM2150 engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, ISBe and ISDe CM2150, Bulletin 4021597.
  - Refer to Procedure For ISC, ISCe, ISL, ISLe3 and ISLe4 CM850 engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Troubleshooting and Repair Manual, ISC, ISCe, QSC8.3, ISL, ISle3, ISLe4, and QSL9 Engines, Bulletin 4021418.
  - Refer to Procedure For ISC and ISL CM2150 engines, refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, ISC and ISL CM2150, Bulletin 4021569.

## Check Fuel Drain Line Restriction

- Turn keyswitch ON
- Engine running at high idle.

- Measure the fuel drain line restriction.

  - [[35-006-012-tr — Fuel Drain Line Restriction|Refer to Procedure For ISM engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Service Manual, ISM, ISMe and QSM11, Bulletin 3666322.]]
  - [[10-006-012 — Fuel Drain Line Restriction|Refer to Procedure For Signature/ISX engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Service Manual, Signature, ISX, and QSX15, Bulletin 3666239.]]
  - Refer to Procedure For ISB and ISBe CM850 engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Service Manual, ISBe, ISB, and QSB (Common Rail Fuel System), Bulletin 4021271.
  - Refer to Procedure For ISB CM2150 engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Service Manual, ISB, Bulletin 4021578.
  - Refer to Procedure For ISBe CM2150 engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Service Manual, ISBe and ISDe CM2150, Bulletin 4021597.
  - Refer to Procedure For ISC, ISCe, ISL, ISLe3 and ISLe4 CM850 engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Troubleshooting and Repair Manual, ISC, ISCe, QSC8.3, ISL, ISle3, ISLe4, and QSL9 Engines, Bulletin 4021418.
  - Refer to Procedure For ISC and ISL CM2150 engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Service Manual, ISC and ISL CM2150, Bulletin 4021569.

- Confirm that fuel drain line restriction is within specification.
- If fuel inlet restriction is higher than specification, troubleshoot the OEM fuel return line.

  - [[35-006-012-tr — Fuel Drain Line Restriction|Refer to Procedure For ISM engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Service Manual, ISM, ISMe and QSM11, Bulletin 3666322, for additional information on troubleshooting high fuel inlet restriction.]]
  - [[10-006-012 — Fuel Drain Line Restriction|Refer to Procedure For Signature/ISX engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Service Manual, Signature, ISX, and QSX15, Bulletin 3666239, for additional information on troubleshooting high fuel inlet restriction.]]
  - Refer to Procedure For ISB and ISBe CM850 engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Service Manual, ISBe, ISB, and QSB (Common Rail Fuel System), Bulletin 4021271.
  - Refer to Procedure For ISB CM2150 engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Service Manual, ISB, Bulletin 4021578.
  - Refer to Procedure For ISBe CM2150 engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Service Manual, ISBe and ISDe CM2150, Bulletin 4021597.
  - Refer to Procedure For ISC, ISCe, ISL, ISLe3 and ISLe4 CM850 engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Troubleshooting and Repair Manual, ISC, ISCe, QSC8.3, ISL, ISle3, ISLe4, and QSL9 Engines, Bulletin 4021418.
  - Refer to Procedure For ISC and ISL CM2150 engines, refer to Procedure 006-012 (Fuel Drain Line Restriction) in Section 6 of the Service Manual, ISC and ISL CM2150, Bulletin 4021569.

## Check for Air in the Fuel

- Turn keyswitch ON
- Engine running at high idle.

- Check for air ingestion into the fuel inlet line.

  - [[35-006-003-tr — Air in Fuel|Refer to Procedure For ISM engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Service Manual, ISM, ISMe and QSM11, Bulletin 3666322, for the correct procedure for measuring for air in the fuel inlet line.]]
  - Refer to Procedure For Signature/ISX engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Service Manual, Signature, ISX, and QSX15, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]], for the correct procedure for measuring for air in the fuel inlet line.
  - Refer to Procedure For ISB and ISBe CM850 engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Service Manual, ISBe, ISB, and QSB (Common Rail Fuel System), Bulletin 4021271.
  - Refer to Procedure For ISB CM2150 engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Service Manual, ISB, Bulletin 4021578.
  - Refer to Procedure For ISBe CM2150 engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Service Manual, ISBe and ISDe CM2150, Bulletin 4021597.
  - Refer to Procedure For ISC, ISCe, ISL, ISLe3 and ISLe4 CM850 engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Troubleshooting and Repair Manual, ISC, ISCe, QSC8.3, ISL, ISle3, ISLe4, and QSL9 Engines, Bulletin 4021418.
  - Refer to Procedure For ISC and ISL CM2150 engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Service Manual, ISC and ISL CM2150, Bulletin 4021569.

- If air is found in the fuel supply, locate and correct the cause of air ingestion in the OEM fuel supply system or damaged fuel filter sealing ring.
- Check the ECM cooling plate, associated plumbing, and o-ring seals for failures that can cause air ingestion.

  - [[35-006-003-tr — Air in Fuel|Refer to Procedure For ISM engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Service Manual, ISM, ISMe and QSM11, Bulletin 3666322, for additional information on troubleshooting air in the fuel inlet line.]]
  - Refer to Procedure For Signature/ISX engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Service Manual, Signature, ISX, and QSX15, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]], for additional information on troubleshooting air in the fuel inlet line.
  - Refer to Procedure For ISB and ISBe CM850 engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Service Manual, ISBe, ISB, and QSB (Common Rail Fuel System), Bulletin 4021271.
  - Refer to Procedure For ISB CM2150 engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Service Manual, ISB, Bulletin 4021578.
  - Refer to Procedure For ISBe CM2150 engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Service Manual, ISBe and ISDe CM2150, Bulletin 4021597.
  - Refer to Procedure For ISC, ISCe, ISL, ISLe3 and ISLe4 CM850 engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Troubleshooting and Repair Manual, ISC, ISCe, QSC8.3, ISL, ISle3, ISLe4, and QSL9 Engines, Bulletin 4021418.
  - Refer to Procedure For ISC and ISL CM2150 engines, refer to Procedure 006-003 (Air in Fuel) in Section 6 of the Service Manual, ISC and ISL CM2150, Bulletin 4021569.

## Check for an Engine Misfire

- Turn keyswitch ON
- Engine running at high idle.

- Use INSITE™ electronic service tool to perform the Cylinder Performance Test found under the Engine Diagnostics Test menu.
- Interpret the results of the INSITE™ electronic service tool cylinder performance test.
- **Note:** Do **not** run the engine above 900 rpm when performing the cylinder performance test.

- Verify that all cylinders are contributing equally and that a cylinder misfire is **not** present.
- If a cylinder misfire is detected, isolate the misfiring cylinder using the Cylinder Cutout Test found under the ECM Diagnostics Test menu.

## Confirm that Fault Codes for Diesel Particulate Filter Soot Load are not Active (if equipped)

- Turn keyswitch ON
- Connect INSITE™ electronic service tool.

- Fault codes for high diesel particulate filter soot load can possibly cause erratic automatic transmission shifting.
- Confirm that Fault Codes 2639, 1921, and 1922 are **not** active.

- Confirm that the fault codes for high diesel particulate filter soot load are **not** active. See the appropriate fault code troubleshooting tree for troubleshooting information.
- If fault codes for the Diesel Particulate Filter Soot Load are active, perform a stationary regeneration to clear the fault codes.

  - [[101-014-013 — Aftertreatment Testing|Refer to Procedure For ISM engines, refer to Procedure 014-013 (Aftertreatment Testing) in Section 14 of the Service Manual, ISM, ISMe, and QSM11, Bulletin 3666322.]]
  - [[101-014-013 — Aftertreatment Testing|Refer to Procedure For ISX engines, refer to Procedure 014-013 (Aftertreatment Testing) in Section 14 of the Service Manual, Signature, ISX, and QSX15, Bulletin 3666239 for aftertreatment stationary regeneration procedures.]]
  - Refer to Procedure For ISC and ISL CM2150 engines, refer to Procedure 014-013 (Aftertreatment Testing) in Section 14 of the Service Manual, ISC and ISL CM2150, Bulletin 4021569.

## Check the Exhaust Restriction

- Install a pressure gauge into the exhaust system.
- Turn keyswitch ON
- Run the engine at advertised horsepower and rpm.

- Check the exhaust restriction by installing a pressure gauge into the exhaust system just pas the turbocharger.

  - [[101-011-009-tr — Exhaust Restriction|Refer to Procedure For ISM engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Service Manual, ISM, ISMe and QSM11, Bulletin 3666322, for the correct procedure for measuring engine exhaust restriction.]]
  - [[101-011-009-tr — Exhaust Restriction|Refer to Procedure For ISX engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Service Manual, Signature, ISX, and QSX15, Bulletin 3666239, for the correct procedure for measuring engine exhaust restriction.]]
  - Refer to Procedure For ISB and ISBe CM850 engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Service Manual, ISBe, ISB, and QSB (Common Rail Fuel System, Bulletin 4021271, for the correct procedure for measuring engine exhaust restriction.
  - Refer to Procedure For ISB CM2150 engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Service Manual, ISB, Bulletin 4021578.
  - Refer to Procedure For ISBe CM2150 engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Service Manual, ISBe and ISDe CM2150, Bulletin 4021597.
  - Refer to Procedure For ISC, ISCe, ISL, ISLe3 and ISLe4 CM850 engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Troubleshooting and Repair Manual, ISC, ISCe, QSC8.3, ISL, ISle3, ISLe4, and QSL9 Engines, Bulletin 4021418.
  - Refer to Procedure For ISC and ISL CM2150 engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Service Manual, ISC and ISL CM2150, Bulletin 4021569.

- Confirm the exhaust restriction is within specification.

  - [[101-011-009-tr — Exhaust Restriction|Refer to Procedure For ISM engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Service Manual, ISM, ISMe and QSM11, Bulletin 3666322, for the correct procedure for measuring engine exhaust restriction.]]
  - [[101-011-009-tr — Exhaust Restriction|Refer to Procedure For ISX engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Service Manual, Signature, ISX, and QSX15, Bulletin 3666239, for the correct procedure for measuring engine exhaust restriction.]]
  - Refer to Procedure For ISB and ISBe CM850 engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Service Manual, ISBe, ISB, and QSB (Common Rail Fuel System, Bulletin 4021271, for the correct procedure for measuring engine exhaust restriction.
  - Refer to Procedure For ISB CM2150 engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Service Manual, ISB, Bulletin 4021578.
  - Refer to Procedure For ISBe CM2150 engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Service Manual, ISBe and ISDe CM2150, Bulletin 4021597.
  - Refer to Procedure For ISC, ISCe, ISL, ISLe3 and ISLe4 CM850 engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Troubleshooting and Repair Manual, ISC, ISCe, QSC8.3, ISL, ISle3, ISLe4, and QSL9 Engines, Bulletin 4021418.
  - Refer to Procedure For ISC and ISL CM2150 engines, refer to Procedure 011-009 (Exhaust Restriction) in Section 11 of the Service Manual, ISC and ISL CM2150, Bulletin 4021569.

## Check the Air Intake Restriction

- Install a vacuum gauge or water manometer into the air intake system.
- Turn keyswitch ON
- Run the engine at advertised horsepower and rpm.

- Check the air intake restriction.

  - [[35-010-031-tr — Air Intake Restriction|Refer to Procedure For ISM engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Service Manual, ISM, ISMe and QSM11, Bulletin 3666322, for the correct procedure for measuring engine exhaust restriction.]]
  - Refer to Procedure For ISX engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Service Manual, Signature, ISX, and QSX15, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]], for the correct procedure for measuring engine exhaust restriction.
  - Refer to Procedure For ISB and ISBe CM850 engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Service Manual, ISBe, ISB, and QSB (Common Rail Fuel System), Bulletin 4021271.
  - Refer to Procedure For ISB CM2150 engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Service Manual, ISB CM2150, Bulletin 4021578.
  - Refer to Procedure For ISBe CM2150 engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Service Manual, ISBe and ISDe CM2150, Bulletin 4021597.
  - Refer to Procedure For ISC, ISCe, ISL, ISLe3 and ISLe4 CM850 engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Troubleshooting and Repair Manual, ISC, ISCe, QSC8.3, ISL, ISLe3, ISLe4 and QSL9 Engines, Bulletin 4021418.
  - Refer to Procedure For ISC and ISL CM2150 engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Troubleshooting and Repair Manual, ISC and ISL CM2150, Bulletin 4021569.

- Confirm that the air intake restriction is within specification.
- If the air intake restriction is higher than specification, check the vehicle air cleaner for proper maintenance. Also, check for collapsed air intake hoses.

  - [[35-010-031-tr — Air Intake Restriction|Refer to Procedure For ISM engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Service Manual, ISM, ISMe and QSM11, Bulletin 3666322, for the correct procedure for measuring engine exhaust restriction.]]
  - Refer to Procedure For ISX engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Service Manual, Signature, ISX, and QSX15, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]], for the correct procedure for measuring engine exhaust restriction.
  - Refer to Procedure For ISB and ISBe CM850 engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Service Manual, ISBe, ISB, and QSB (Common Rail Fuel System), Bulletin 4021271.
  - Refer to Procedure For ISB CM2150 engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Service Manual, ISB CM2150, Bulletin 4021578.
  - Refer to Procedure For ISBe CM2150 engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Service Manual, ISBe and ISDe CM2150, Bulletin 4021597.
  - Refer to Procedure For ISC, ISCe, ISL, ISLe3 and ISLe4 CM850 engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Troubleshooting and Repair Manual, ISC, ISCe, QSC8.3, ISL, ISLe3, ISLe4 and QSL9 Engines, Bulletin 4021418.
  - Refer to Procedure For ISC and ISL CM2150 engines, refer to Procedure 010-031 (Air Intake Restriction) in Section 10 of the Troubleshooting and Repair Manual, ISC and ISL CM2150, Bulletin 4021569.

### Document History
