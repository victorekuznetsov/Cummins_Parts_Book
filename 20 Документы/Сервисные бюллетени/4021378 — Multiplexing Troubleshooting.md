---
aliases:
  - "Диагностика мультиплексирования"
type: "Сервисный бюллетень"
doc: "4021378"
title_en: "Multiplexing Troubleshooting"
title_ru: "Диагностика мультиплексирования"
released: "2011-04-25"
modified: "2019-05-07"
group: "19 - Electronic Engine Controls"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
figures: 2
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/4021378.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/4021378.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "тема/electronic-engine-controls"
---

# Multiplexing Troubleshooting
**Диагностика мультиплексирования**

> [!abstract] Сервисный бюллетень · `4021378`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Даты:** выпущен 2011-04-25 · изменён 2019-05-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/4021378.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/4021378.pdf)

## Multiplexing Troubleshooting

## Introduction

This Service Bulletin introduces the multiplexing feature and provides:

- Introduction to the new SAE J1939 multiplexing feature
- SAE J1939 multiplexing features and parameters setup using INSITE™ electronic service tool
- Fault code information associated with the multiplexing feature and general troubleshooting guidelines.

## Multiplexing

Conventional engine systems have wired connections to individual switches, sensors, and throttles for control and feedback purposes. With the introduction of the SAE J1939 multiplexing network in the vehicle industry, the numerous cables and harnesses have been reduced to a few connection points. The reduced vehicle wiring is possible in a multiplexed system because of the transmission and reception of multiple signals over the same signal bus (or data link) between modules, which have been traditionally accomplished by individual wires.

## Multiplexing Features and Parameters Setup

The multiplexing feature setup process is explained in two parts:

## Part 1: J1939 Multiplexing Features and Parameters Setup with INSITE™ Electronic Service Tool

Follow the instructions below to set up the J1939 Multiplexing features and parameters using INSITE™ electronic service tool.

1. Under the View menu (current view), select Features and Parameters or click on the Features and Parameters icon on the left side of INSITE™ electronic service tool window.
2. Locate and expand the SAE J1939 Multiplexing icon from the Features and Parameters list.
3. For each parameter, set the ”ECM Value” to enable/disable, according to the appropriate OEM settings.
4. For each enabled parameter, set the source address according to the appropriate OEM setting.

![[19803894.png]]

1. SAE J1939 Multiplexing feature
2. Enable/Disable for J1939 Multiplexing feature
3. Source address selection for ”Enabled” J1939 Multiplexing feature.

## Using INSITE™ Electronic Service Tool to Troubleshoot Multiplexing Fault Codes 285, 286, 427, or 6338

Use INSITE™ electronic service tool SAE J1939 Multiplexed Fault Data feature, located in Advanced ECM data, to determine which multiplexed component is causing the fault. This feature in INSITE™ electronic service tool will indicate which multiplexed component is **not** configured correctly. If the status column indicates “Active” for a multiplexed component, check that the engine ECM multiplexed component enables and source addresses match the OEM VECU multiplexed component. The multiplexing configuration settings can be found under SAE J1939 Multiplexing in Features and Parameters of the INSITE™ electronic service tool.

![[19r00017.png]]

1. SAE J1939 Multiplexed Fault Data
2. Faults showing parameters that are currently set incorrectly. The parameters that are currently shown as “Active” have incorrect source address information, or have been improperly set to enable or disable.

## Part 2: OEM Specific SAE J1939 Multiplexing Feature Configuration

Different OEMs have different multiplexing configurations for which components or switches can be enabled for multiplexing in the Cummins® ECM. For multiplexing to be possible, the following conditions **must** be met:

1. The OEM vehicle electronic unit and the Cummins® ECM **must** have the same components enabled for multiplexing.
2. The source address of each enabled component **must** be set to the proper value for the component or switch that was enabled.

> [!note] Note · Примечание
> The multiplexing setup procedure for the OEM vehicle electronic control unit is beyond the scope of this Service Bulletin. Contact the appropriate OEM for the required information.

## General Multiplexing Troubleshooting

A list of multiplexing fault codes, descriptions, cause of the fault code, and a brief troubleshooting procedure is provided. For a detailed description, check the fault code in the appropriate troubleshooting and repair manual.

## Fault Code 285 or 427 - SAE J1939 Multiplexing PGN Timeout Error - Abnormal Update Rate (Slow or No Communication)

This fault code occurs when a switch or component is enabled and addressed in the ECM, but the message from the OEM vehicle electronic control unit is **not** received by the ECM for one or all of the following reasons:

- The multiplexed message for a particular switch is **not** broadcast from the vehicle electronic control unit to the ECM. This can be because of a vehicle electronic control unit hardware failure or vehicle electronic control unit software setup issue. This fault can be caused by an OEM vehicle electronic control unit setup issue **only** if all components and parameters for a specific SAE J1939 parameter group names message are disabled in the OEM vehicle electronic control unit. Otherwise Fault Code 286 or 6338will be generated.
- There is a data link issue between the OEM vehicle electronic control unit and the Cummins® ECM which is **not** allowing any SAE J1939 messages (parameter group names) to be transmitted from the OEM vehicle electronic control unit to the Cummins® ECM.
- The Cummins® ECM has enabled a switch or component that is enabled correctly in the OEM vehicle electronic control unit software, but is source addressed to the incorrect OEM vehicle electronic control unit. This fault mode can occur when an ECM is replaced and a job image was **not** taken or a template saved to identify which components **must** be enabled for multiplexing and how the OEM vehicle electronic control unit source **must** be set.
- The Cummins® ECM has enabled a switch or component that is enabled incorrectly in the OEM vehicle electronic control unit software and is source addressed to the incorrect OEM vehicle electronic control unit (the OEM vehicle electronic control unit does **not** support multiplexing of the component). This fault mode can occur when an ECM is replaced and the correct template is **not** used.

## General Troubleshooting Procedure for Fault Code 285 or 427

- Verify communication is possible between the electronic service tool and the Cummins® ECM. If it is **not** possible, troubleshoot the service data link connector connection to the SAE J1939 data link and the ECM connection to the SAE J1939 data link. This is accomplished by verifying that there is a resistance value between 50 and 70 ohms when measuring the resistance between the SAE J1939 data link (+) wire and the SAE J1939 data link (-) wire on the service data link connector and the Cummins® ECM data link connector.
- If communication is possible, determine if the multiplexed component enables and the OEM vehicle electronic control unit source addresses are set correctly in the Cummins® ECM. This can be accomplished by using job images and templates that are known to be correct or by using information supplied by the appropriate OEM. This can also be accomplished by checking to see if there are wires installed on the appropriate Cummins® ECM connector for the components in question.
- If an issue is **not** found with the data link or connectors, the issue **must** be with the OEM component, vehicle electronic control unit hardware, vehicle electronic control unit software, or the vehicle electronic control unit connection to the data link.

## Fault Code 286 or 6338 - SAE J1939 Multiplexing Configuration Error - Out of Calibration

This fault code will occur when a switch or component is enabled and source addressed to be multiplexed in the Cummins® ECM, but the message from the OEM vehicle electronic control unit is **not** received by the Cummins® ECM for one or all of the following reasons:

- The Cummins® ECM has enabled and source addressed a switch or component correctly that **must** be enabled in the OEM vehicle electronic control unit according to the OEM supplied information, but is **not** enabled in the OEM vehicle electronic control unit software correctly. The OEM vehicle electronic control unit transmits the component message as **not** available, but the component **must** be enabled and available in the OEM electronic control unit.
- The Cummins® ECM has enabled a component that is **not** available to be a multiplexed component from the OEM vehicle electronic control unit, and has a device selected that is correct for all of the other multiplexed components from the OEM vehicle electronic control unit. The signal is being transmitted as ” **Not** available”.

## General Troubleshooting Procedure for Fault Code 286 or 6338

- If an issue is **not** found with the data link or connectors, the issue **must** be with an OEM component, vehicle electronic control unit hardware, vehicle electronic control unit software, or vehicle electronic control unit to the data link connection.
- If communication is possible, determine if the multiplexed components are enabled correctly and OEM vehicle electronic control unit source addresses are set correctly in the Cummins® ECM. This can be accomplished by using job images and templates that are known to be correct, or by using information supplied by the appropriate OEM. This also can be accomplished by checking to see if there are wires installed on the appropriate Cummins® ECM connector for the component's location.

## Fault Code 287 - SAE J1939 Multiplexing Accelerator Pedal or Lever Sensor System Error - Received Network Data Error

The fault code is generated when an error condition on the accelerator or idle validation switch is present. This fault code will occur for one or all of the following reasons:

- When the accelerator is depressed and the ECM reads accelerator position as greater than 0 percent, but the idle validation switch transmits a message that shows the accelerator is **not** depressed.
- When the accelerator is released and the ECM reads accelerator position as 0 percent, but the idle validation switch transmits a message that shows the accelerator is depressed.
- Accelerator signal line is shorted high or shorted low. When either component has an error, the Cummins® ECM will engage the limp home algorithm to allow the vehicle to be moved to a safe location.

> [!note] Note · Примечание
> There can be an accelerator pedal or idle validation switch message time out which will cause Fault Code 285 or 427 to become active. Fault Code 287 is **only** for true accelerator or idle validation switch circuit failures. The engine will go to idle when the accelerator pedal or the idle validation switch receives a message from the OEM vehicle electronic control unit that shows the accelerator pedal or idle validation switch as being in the **not** available state (Fault Code 286 or 6338). The limp home algorithm will be enabled when a message time out occurs (Fault Code 285 or 427) or when the accelerator pedal or the idle validation switch has an error (Fault Code 287).

## General Troubleshooting Procedure for Fault Code 287

- Determine if the multiplexed components are enabled and the OEM vehicle electronic control unit source addresses are set correctly in the Cummins® ECM. This can be accomplished by using job images and templates that are known to be correct, or by using information supplied by the appropriate OEM. This can also be accomplished by checking to see if there are wires installed on the appropriate Cummins® ECM connector for the components in question.
- If there is **not** an issue with the feature setups, the issue can be with the OEM component, vehicle electronic control unit hardware, vehicle electronic control unit software, or vehicle electronic unit connection to the data link.
- Check the connections of the accelerator pedal and idle validation switch and monitor the status with INSITE™ electronic service tool to verify the parameters are received properly by the Cummins® ECM.

## Fault Code 288 - SAE J1939 Multiplexing Remote Throttle Data Error

This fault code detects errors in the remote throttle, but does **not** detect message time out errors (Fault Code 285 or 427). This fault code will occur for one or all of the following reasons:

- When the remote accelerator has a shorted high or shorted low error detected by the vehicle electronic control unit. This fault status is transmitted to the ECM on the SAE J1939 data link, which causes the fault to occur in the ECM.
- When the remote throttle enable switch has a shorted high or shorted low error detected by the vehicle electronic control unit, the fault status is transmitted to the ECM on the SAE J1939 data link, which causes the fault code to activate in the ECM. Most OEMs will **not** incorporate fault detection on a switch. The fault code is generated when an error condition on the remote throttle circuit is present, but **not** when an error on the idle validation switch circuit is present, because remote throttles do **not** have an idle validation switch.

## General Troubleshooting Procedure for Fault Code 288

- Determine if the multiplexed components are enabled and the OEM vehicle electronic control unit source addresses are set correctly in the Cummins® ECM. This can be accomplished by using job images and templates that are known to be correct, or by using information supplied by the appropriate OEM. This can also be accomplished by checking if there are wires installed on the appropriate Cummins® ECM connector for the components in question.
- If there is **not** an issue found with the feature setups, the issue **must** be with an OEM component, vehicle electronic control unit hardware, vehicle electronic control unit software, or vehicle electronic control unit connection to the data link.

## General SAE J1939 Multiplexing Symptom Based Troubleshooting Procedure

> [!note] Note · Примечание
> This process assumes the vehicle will be using the multiplexing feature.

The following general process **must** be used to troubleshoot symptoms on a vehicle that supports SAE J1939 multiplexing feature when fault codes are **not** present. These symptoms will **only** be related to the components that can be multiplexed in a particular application. The following steps will act as a guide through a symptom based troubleshooting procedure and allow the problem to be isolated to a sensor issue, vehicle electronic control unit issue, data link issue, Cummins® ECM issue, or a combination thereof.

1. Interview the operator to determine specific symptom (examples - clutch switch **not** functioning, cruise control on/off switch **not** working, manual fan control switch **not** working, etc.). If the symptom description is vague, it will be necessary to verify the symptoms with a road test.
2. Connect an electronic service tool to the Cummins® ECM and verify that communication with the Cummins® ECM is possible.
3. If communication with the Cummins® ECM is possible, print an image to get a copy of the Cummins® ECM features and parameter settings. This will be a standard procedure for all vehicles that use the multiplexing feature in a Cummins® engine. If an ECM is replaced or is damaged and the multiplexing setup information was **not** saved, it will be difficult to get the information from the OEM.
4. If communication with the Cummins® ECM is **not** possible, check the appropriate ECM Communication Troubleshooting Tree for procedure to troubleshoot a no communication symptom. Some of the causes of no communication between the electronic service tool and the ECM are SAE J1939 data link harness or connectors have malfunctioned, switched or unswitched battery power to the ECM or data link adapter is **not** available, the data link adapter cables or connectors have malfunctioned, or the ECM calibration or hardware has malfunctioned.
5. Read the fault codes and troubleshoot any active fault codes first, using the appropriate fault code procedure. [[99-019-362 — Inactive or Intermittent Fault Code|Refer to Procedure If there are high counts of inactive fault codes, 019-362 (Inactive or Intermittent Fault Code) in Section 19 of the appropriate Electronic Control System Troubleshooting and Repair Manual.]]
6. Use the electronic service tool to monitor the multiplexed components or switches for a change of state or value that can contribute to the symptom. This information is useful in narrowing down which components are contributing to the symptom.
7. These components can be enabled and source addressed for multiplexing under the SAE J1939 multiplexing feature. If any of the components are **not** changing state, document the component and verify the components are enabled and source addressed for multiplexing. A quick check to investigate if a component is multiplexed is to inspect the wiring harness to verify that the component wires are routed to the Cummins® ECM. If wires are **not** present for the component in question, it is an indication the component or switch **must not** be multiplexed. Contact the OEM for the J1939 multiplexing settings.
8. If there are **not** any issues with ECM communication, data link adapter, harness or setup for multiplexing, the OEM **must** be contacted to determine further troubleshooting actions.

### Document History
