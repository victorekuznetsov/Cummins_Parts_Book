---
aliases:
  - "Дерево диагностики мощностных характеристик"
type: "Процедура"
doc: "105-t02-1001"
title_en: "Engine Performance Troubleshooting Tree"
title_ru: "Дерево диагностики мощностных характеристик"
modified: "2015-04-23"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-t02-1001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/105-t02-1001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/105"
---

# Engine Performance Troubleshooting Tree
**Дерево диагностики мощностных характеристик**

> [!abstract] Процедура · `105-t02-1001`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2015-04-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-t02-1001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/105-t02-1001.pdf)

Printable Version

### Symptoms

- Engine Acceleration or Response Poor

- Cranking Fuel Pressure Low

- Engine Operating Fuel Pressure Low

- Engine Difficult to Start or Will **Not** Start (Exhaust Smoke)

- Engine Difficult to Start or Will **Not** Start (No Exhaust Smoke)

- Engine Power Output Low

- Engine Runs Rough at Idle

- Engine Runs Rough or Misfires

- Engine Speed Surges at Low or High Idle

- Engine Speed Surges Under Load or in Operating Range

- Smoke, Black - Excessive

- Smoke, White - Excessive

- Engine Shuts Off or Dies Unexpectedly or Dies During Deceleration

- Engine Starts But Will **Not** Keep Running

- Engine Will **Not** Reach Rated Speed (rpm)

### How To Use This Tree

This symptom tree can be used to troubleshoot all performance based symptoms listed above. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Prior to performing INSITE™ electronic service tool EGR Valve and EGR Valve/Turbocharger Operational Test, the engine control module (ECM) Calibration Software Phase could possibly need to be updated to the latest Software Phase. The ECM Calibration Phase Software can be checked in INSITE™ electronic service tool, under 'Features and Parameters'. Expand the selection for 'System ID and Dataplate' and go to 'Calibration Information'. If the Software Phase is earlier than shown below, calibrate the ECM again using the January 2006 INCAL™ CD-ROM, or later. Engines with the Software Phase listed below or later do **not** require a recalibration.

ISM engines with CM875 (engines built after January 2004) require Software Phase 06050312.

This is a warrantable calibration change.

| Minimum and Maximum VGT Actuator Travel Specifications by CPL Number |  |  |
|---|---|---|
| CPL | Minimum Actuator Travel mm \[in\] | Maximum Actuator Travel mm \[in\] |
| 8427, 8559, 8560, 8603, 8706 | 8 mm \[0.315 in\] | 10 mm \[0.394 in\] |
| 8271, 8272, 8273, 8274, 8503, 8504, 8505, 8506, 8556, 8557, 8561, 8562 | 7 mm \[0.276 in\] | 9 mm \[0.354 in\] |
| 8377, 8558, 8563, 8572 | 10 mm \[0.394 in\] | 12 mm \[0.472 in\] |

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Perform basic troubleshooting procedures. |  |
|  | **STEP 1A.** Check for active fault codes or high counts of inactive fault codes. | Active fault codes or high counts of inactive fault codes? |
|  | **STEP 1B.** Perform basic troubleshooting checks. | All steps have been verified to be correct? |
| STEP 2. | Determination of engine symptom. |  |
|  | **STEP 2A.** Low power, poor acceleration, poor response, or engine will not reach rated speed (rpm). | Engine symptom low power, poor acceleration, poor response, or engine will **not** reach rated speed (rpm)? |
|  | **STEP 2B.** Engine runs rough or misfires. | Engine symptom Engine Runs Rough or Misfires? |
|  | **STEP 2C.** Excessive black smoke. | Engine symptom Excessive Black Smoke? |
|  | **STEP 2D.** Excessive white smoke. | Engine symptom Excessive White Smoke and the engine is using coolant? |
|  | **STEP 2D-1.** Excessive white smoke. | Engine symptom Excessive White Smoke and the engine is not using coolant? |
|  | **STEP 2E.** Engine speed surge or engine speed unstable. | Engine symptom Engine Speed Surge or Engine Speed Unstable? |
|  | **STEP 2F.** Engine will not start or difficult to start, engine shuts off unexpectedly. | Engine symptom Engine Difficult to Start or Will Not Start, or Engine Shuts Off Unexpectedly? |
| STEP 3. | No-start troubleshooting procedures. |  |
|  | **STEP 3A.** Check fuel shutoff valve voltage. | Fuel shutoff valve voltage greater than 11-VDC? |
|  | **STEP 3B.** Determine if engine is equipped with a fuel control module. | Engine equipped with a separate fuel control module? |
|  | **STEP 3B-1.** Check the ECM connector and pins. | Dirty or damaged pins? |
|  | **STEP 3B-2.** Check the ECM keyswitch voltage. | Keyswitch voltage equal to battery voltage? |
|  | **STEP 3B-3.** Check the ECM battery supply voltage. | Voltage equal to battery voltage? |
|  | **STEP 3B-4.** Check the ECM actuator connector and pins. | Dirty or damaged pins? |
|  | **STEP 3B-5.** Check for a pin-to-pin short circuit in the engine harness. | Greater than 100k ohms? |
|  | **STEP 3B-6.** Check for a short circuit to ground in the engine harness. | Greater than 100k ohms? |
|  | **STEP 3B-7.** Check the continuity of the fuel shutoff valve circuit. | Less than 10 ohms? |
|  | **STEP 3C.** Check the fuel control module and fuel control module power connector pins. | Dirty or damaged pins? |
|  | **STEP 3D.** Check for a pin-to-pin short circuit at the fuel control module. | Greater than 100k ohms? |
|  | **STEP 3E.** Check for a short circuit to ground in the engine harness. | Greater than 100k ohms? |
|  | **STEP 3F.** Check for a pin-to-pin short circuit in the engine harness. | Greater than 100k ohms? |
|  | **STEP 3G.** Check ground connections. | Ground connections clean and tight? |
|  | **STEP 3H.** Check the fuel shutoff valve resistance. | Fuel shutoff solenoid resistance 1 to 5 ohms for 6-VDC solenoids, 6 to 15 ohms for 12-VDC solenoids, 24 to 50 ohms for 24-VDC solenoids, 42 to 80 ohms for 32-VDC solenoids, 46 to 87 ohms for 36-VDC solenoids, 92 to 145 ohms for 48-VDC solenoids, 315 to 375 ohms for 74-VDC solenoids, 645 to 735 ohms for 115-VAC solenoids? |
|  | **STEP 3I.** Check the engine position sensor installation. | Engine position sensor installed correctly? |
|  | **STEP 3J.** Determine if engine is equipped with EGR. | Engine equipped with a separate fuel control module? |
|  | **STEP 3K.** Check for coolant in the EGR transfer tube. | Coolant present in the crossover tube? |
| STEP 4. | Fuel system checks. |  |
|  | **STEP 4A.** Check for air in the fuel. | Air bubbles visible in the sight glass? |
|  | **STEP 4B.** Check fuel inlet restriction. | Fuel inlet restriction less than the specifications? |
|  | **STEP 4C.** Check drain line restriction. | Fuel drain line restriction less than 89 mm-Hg \[3.5 in-Hg\]? |
|  | **STEP 4D.** Check fuel pump output pressure. | Fuel pressure meet the specification? |
|  | **STEP 4E.** Check fuel gear pump check valve. | Check valve installed and operating correctly? |
|  | **STEP 4F.** Check fuel supply line for restrictions. | Fuel lines free from restrictions? |
|  | **STEP 4G.** Check for plugged fuel drillings in the cylinder head. | Plastic insert been removed from the fuel supply passage in the cylinder head? |
| STEP 5. | Injector diagnostics. |  |
|  | **STEP 5A.** Perform INSITE™ electronic service tool cylinder cutout test. | All cylinders pass the cylinder cutout test? |
| STEP 6. | Air handling diagnostic checks. |  |
|  | **STEP 6A.** Start engine and read fault codes. | Active fault codes? |
|  | **STEP 6B.** Inspect the turbocharger blades for damage. | Damage found on turbocharger fins? |
|  | **STEP 6C.** Determination of turbocharger type. | Turbocharger a variable geometry turbocharger? |
|  | **STEP 6D.** Check the variable geometry actuator rod for correct travel. | Turbocharger actuator rod extend between the minimum and maximum actuator travel specification found in the CPL table in the Shop Talk section? |
|  | **STEP 6D-1.** Check for air leaks and inspect air lines. | Air leaks found in the system? |
|  | **STEP 6D-2.** Check the engine and vehicle grounds. | Connections tight and corrosion free? |
|  | **STEP 6D-3.** Check for air pressure at the turbocharger control valve outlet. | Vehicle air tank pressure present at the turbocharger control valve outlet? |
|  | **STEP 6D-4.** Check for air pressure at the turbocharger control valve outlet. | Pressure gauge read more than 103 kPa \[15 psi\] after 5 minutes? |
|  | **STEP 6D-5.** Check for correct turbocharger actuator travel. | Turbocharger actuator rod travel at least 12 mm \[0.472 in\]? |
|  | **STEP 6D-6.** Determine if the engine is equipped with a turbocharger control shutoff valve. | Engine equipped with a turbocharger control shutoff valve? |
|  | **STEP 6D-7.** Check for air pressure at the turbocharger control shutoff valve outlet. | Air heard escaping from the turbocharger control shutoff valve outlet? |
|  | **STEP 6D-8.** Check for air pressure at the turbocharger control shutoff valve inlet. | Air heard escaping from the turbocharger control shutoff valve inlet? |
|  | **STEP 6D-9.** Check for plugged turbocharger control shutoff valve filter. | Air leak present at the turbocharger control shutoff valve filter head? |
|  | **STEP 6D-10.** Verify the OEM air supply line is connected to the correct port on the turbocharger control valve. | Air heard escaping from the turbocharger control valve inlet? |
|  | **STEP 6E.** Perform INSITE™ electronic service tool EGR Valve/Turbocharger Operational Test. | Turbocharger Operational Test pass? |
|  | **STEP 6E-1.** Check the engine and vehicle grounds. | Connections tight and corrosion free? |
|  | **STEP 6F.** Inspect the wastegate actuator hose. | Holes or cracks found in the wastegate actuator hose? |
|  | **STEP 6G.** Inspect the wastegate actuator rod for travel. | Wastegate actuator rod move? |
|  | **STEP 6G-1.** Inspect wastegate actuator rod for travel. | Wastegate actuator rod move? |
|  | **STEP 6H.** Measure resistance of the four-stage wastegate controllers, if equipped. | Wastegate controller solenoid resistances 6 to 10 ohms for 12-VDC solenoids, 24 to 40 ohms for 24-VDC solenoids? |
|  | **STEP 6I.** Inspect four-stage wastegate controller, if equipped. | Damage or debris found on the valve disc, valve seat, or actuator disc? |
| STEP 7. | Check EGR valve for proper operation. |  |
|  | **STEP 7A.** Check for air leaks in the EGR system. | Air leaks found in the EGR connection tubing? |
|  | **STEP 7B.** Check repair history. | Record of the poppet head missing? |
|  | **STEP 7C.** Perform the EGR Valve Test. | EGR Valve Test pass? |
| STEP 8. | Verify electronic features are operating correctly. |  |
|  | **STEP 8A.** Verify accelerator pedal travel. | Percent Accelerator read 0 when the accelerator is released and 100 percent when the accelerator is depressed? |
|  | **STEP 8B.** Monitor vehicle speed. | Vehicle speed read 0 when the vehicle is not moving? |
|  | **STEP 8C.** Verify electronic feature settings are correct. | Electronic features set correctly? |
|  | **STEP 8D.** Check barometric pressure sensor reading. | Barometric pressure sensor reading in INSITE™ electronic service tool within 5 percent of the present local barometric pressure reading? |
| STEP 9. | Perform base engine mechanical checks. |  |
|  | **STEP 9A.** Verify overhead adjustments are correct. | Overhead settings within the reset limits? |
|  | **STEP 9B.** Check air intake restriction. | Air intake restriction greater than 635 mm-H 2 O \[25 in-H 2 O\]? |
|  | **STEP 9C.** Check exhaust restriction. | Exhaust restriction within specification as listed in the Service Manual? |
|  | **STEP 9D.** Inspect the charge air cooler. | Pressure drop 34 kPa \[5 psi\] or less in 15 seconds? |
|  | **STEP 9E.** Verify engine brake adjustment. | Engine brake settings within the reset limits? |
|  | **STEP 9F.** Measure turbocharger axial and radial clearance. | Axial and radial clearances within specification? |
|  | **STEP 9G.** Verify engine blowby is within specification. | Engine blowby measurements within specification? |
|  | **STEP 9G-1.** Verify turbocharger contribution to engine blowby. | Did the total engine blowby drop more than 30 percent? |
|  | **STEP 9H.** Check the static injection timing. | Is the static injection timing correct? |
| STEP 10. | Check the EGR differential pressure sensor and exhaust gas pressure sensor |  |
|  | **STEP 10A.** Check the EGR differential pressure tubes for cracks, restrictions, or leaks. | Cracks, restrictions, or leaks present? |
|  | **STEP 10B.** Check the exhaust gas pressure tubes for cracks, restrictions, or leaks. | Cracks, restrictions, or leaks present? |
| STEP 11. | Check the EGR cooler. |  |
|  | **STEP 11A.** Check the EGR cooler for fouling. | EGR cooler efficiency parameter greater than 50 percent after 4 minutes? |

### STEP 1. Perform basic troubleshooting procedures.

#### STEP 1A. Check for active fault codes or high counts of inactive fault codes.

| **Conditions:** Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes or high counts of inactive fault codes. Use INSITE™ electronic service tool to read the fault codes. | Active fault codes or high counts of inactive fault codes? **YESRepair:** See one of the following manuals: Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines, Bulletin 4021381 Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477 Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. | Go to appropriate fault code troubleshooting tree |
| Active fault codes or high counts of inactive fault codes? **NO** | 1B |  |

#### STEP 1B. Perform basic troubleshooting checks.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| The following items must be checked or verified before continuing: Verify the fuel level in the tanks Verify there have not been any changes to CPL components on the engine Verify fuel grade is correct for the application Verify the engine is operating within the recommended altitude Verify engine oil is at the correct level Verify engine parasitics have not changed Verify engine duty cycle has not changed Verify engine cranking speed is greater than 150 rpm. | All steps have been verified to be correct? **YES** | 2A |
| All steps have been verified to be correct? **NORepair:** Correct the condition and verify complaint is no longer present after repair. | Repair complete |  |

### STEP 2. Determination of engine symptom.

#### STEP 2A. Low power, poor acceleration, poor response, or engine will not reach rated speed (rpm).

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom low power, poor acceleration, poor response, or engine will **not** reach rated speed (rpm)? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 6 - Air Handling Checks With EGR - Step 7 - EGR Checks Step 8 - Electronic Checks Step 5 - Injector Checks Step 9 - Base Engine Checks With EGR - Step 10 - EGR Differential Pressure and Exhaust Gas Pressure Checks With EGR - Step 11 - Check the EGR Cooler | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom low power, poor acceleration, poor response, or engine will **not** reach rated speed (rpm)? **NO** | 2B |  |

#### STEP 2B. Engine runs rough or misfires.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom Engine Runs Rough or Misfires? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 5 - Injector Checks Step 4 - Fuel System Checks Step 9 - Base Engine Checks With EGR - Step 10 - EGR Differential Pressure and Exhaust Gas Pressure Checks With EGR - Step 11 - Check the EGR Cooler | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom Engine Runs Rough or Misfires? **NO** | 2C |  |

#### STEP 2C. Excessive black smoke.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom Excessive Black Smoke? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 6 - Air Handling Checks Step 4 - Fuel System Checks With EGR - Step 7 - EGR Checks With EGR - Step 10 - EGR Differential Pressure and Exhaust Gas Pressure Checks Step 9 - Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom Excessive Black Smoke? **NO** | 2D |  |

#### STEP 2D. Excessive white smoke.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom Excessive White Smoke and the engine is using coolant? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: See the Coolant Loss - Internal symptom tree. | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom Excessive White Smoke and the engine is using coolant? **NO** | 2D-1 |  |

#### STEP 2D-1. Excessive white smoke.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom Excessive White Smoke and the engine is **not** using coolant? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 5 - Injector Checks Step 6 - Air handling checks Step 9 - Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom Excessive White Smoke and the engine is **not** using coolant? **NO** | 2E |  |

#### STEP 2E. Engine speed surge or engine speed unstable.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom Engine Speed Surge or Engine Speed Unstable? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 5 - Injector Checks Step 10 - EGR Differential Pressure and Exhaust Gas Pressure Checks Step 6 - Air Handling Checks Step 8 - Electronics Checks Step 9 - Base Engine Checks Step 11 - Check the EGR Cooler | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom Engine Speed Surge or Engine Speed Unstable? **NO** | 2F |  |

#### STEP 2F. Engine will not start or difficult to start, engine shuts off unexpectedly.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom Engine Difficult to Start or Will **Not** Start, or Engine Shuts Off Unexpectedly? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 3 - No Start Checks Step 4 - Fuel System Checks Step 5 - Injector Checks Step 6 - Air Handling Checks Step 8 - Electronics Checks Step 9 - Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom Engine Difficult to Start or Will **Not** Start, or Engine Shuts Off Unexpectedly? **NO** | Return to correct symptom tree |  |

### STEP 3. No-start troubleshooting procedures.

#### STEP 3A. Check fuel shutoff valve voltage.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from the fuel shutoff valve post to engine block ground. | Fuel shutoff valve voltage greater than 11-VDC? **YES** | 3H |
| Fuel shutoff valve voltage greater than 11-VDC? **NO** | 3B |  |

#### STEP 3B. Determine if engine is equipped with a fuel control module.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Determine if the engine is equipped with a separate fuel control module. | Engine equipped with a separate fuel control module? **YES** | 3C |
| Engine equipped with a separate fuel control module? **NO** | 3B-1 |  |

#### STEP 3B-1. Check the ECM connector and pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM harness connector and ECM pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. See one of the following procedures: Flush the dirt, debris, or moisture from the connector pins. Use electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Replace the engine harness. Use one of the following procedures: Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-043 in Section 19. Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines Bulletin 4021381. Refer to Procedure 019-043 in Section 19. Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-043 in Section 19. Replace the OEM harness. Refer to the OEM service manual. Replace the ECM. Use one of the following procedures: Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-031 in Section 19. Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines Bulletin 4021381. Refer to Procedure 019-031 in Section 19. Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-031 in Section 19. | Repair complete |
| Dirty or damaged pins? **NO** | 3B-2 |  |

#### STEP 3B-2. Check the ECM keyswitch voltage.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the ECM. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ECM keyswitch voltage. Measure the voltage from the keyswitch input SIGNAL pin of the OEM connector to ground. Refer to the wiring diagram or circuit diagram for connector pin identification. | Keyswitch voltage equal to battery voltage? **YES** | 3B-3 |
| Keyswitch voltage equal to battery voltage? **NORepair:** Repair the OEM keyswitch circuit. Use one of the following procedures: Use the following procedure in the Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-064 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines, Bulletin 4021381. Refer to Procedure 019-064 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-064 in Section 19. | Repair complete |  |

#### STEP 3B-3. Check the ECM battery supply voltage.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM or 4-pin power harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ECM battery supply. Measure the voltage from the battery SUPPLY (+) pins of the OEM or 4-pin power harness connector to the battery SUPPLY (-) pins of the connector. Refer to the wiring diagram or circuit diagram for connector pin identification. | Voltage equal to battery voltage? **YES** | 3B-4 |
| Voltage equal to battery voltage? **NORepair:** Repair the OEM battery supply or keyswitch circuit. | Repair complete |  |

#### STEP 3B-4. Check the ECM actuator connector and pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness or engine harness actuator connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness or engine harness actuator connector and ECM pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Repair the damaged harness, connector, or pins if possible. See one of the following procedures: Flush the dirt, debris, or moisture from the connector pins. Use electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Replace the engine harness. Use one of the following procedures: Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-043 in Section 19. Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines Bulletin 4021381. Refer to Procedure 019-043 in Section 19. Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-043 in Section 19. Replace the OEM harness. Refer to the OEM service manual. Replace the ECM. Use one of the following procedures: Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-031 in Section 19. Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines Bulletin 4021381. Refer to Procedure 019-031 in Section 19. Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-031 in Section 19. | Repair complete |
| Dirty or damaged pins? **NO** | 3B-5 |  |

#### STEP 3B-5. Check for a pin-to-pin short circuit in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness or engine harness actuator connector from the ECM. Remove the engine harness ring terminal from the fuel shutoff valve. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short circuit. Measure the resistance between the fuel shutoff valve SIGNAL pin of the engine harness or engine harness actuator connector and all pins in the connector. Refer to the wiring diagram or circuit diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3B-6 |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. See one of the following procedures: Use the following procedure in the Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-043 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines Bulletin 4021381. Refer to Procedure 019-043 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-043 in Section 19. | Repair complete |  |

#### STEP 3B-6. Check for a short circuit to ground in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness or engine harness actuator connector from the ECM. Remove the engine harness ring terminal from the fuel shutoff valve. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance between the fuel shutoff valve SIGNAL pin of the engine harness or engine harness actuator connector and ground. Refer to the wiring diagram or circuit diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3B-7 |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. See one of the following procedures: Use the following procedure in the Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-043 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines Bulletin 4021381. Refer to Procedure 019-043 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-043 in Section 19. | Repair complete |  |

#### STEP 3B-7. Check the continuity of the fuel shutoff valve circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness or engine harness actuator connector from the ECM. Disconnect the fuel shutoff valve wire from the valve terminal post. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the continuity of the fuel shutoff valve circuit. Measure the resistance of the fuel shutoff valve SIGNAL circuit between the engine harness or engine harness actuator connector and the fuel shutoff valve eyelet. Refer to the wiring diagram or circuit diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YESRepair:** Replace the ECM. See one of the following procedures: Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-031 in Section 19. Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines Bulletin 4021381. Refer to Procedure 019-031 in Section 19. Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-031 in Section 19. | Repair complete |
| Less than 10 ohms? **NORepair:** Repair or replace the engine harness. See one of the following procedures: Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-043 in Section 19. Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines Bulletin 4021381. Refer to Procedure 019-043 in Section 19. Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-043 in Section 19. | Repair complete |  |

#### STEP 3C. Check the fuel control module and fuel control module power connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel control module actuator connector from the fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel control module and the fuel control module actuator connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair or replace the fuel control module harness. See one of the following procedures: Use the following procedure in the Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-043 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines Bulletin 4021381. Refer to Procedure 019-043 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-043 in Section 19. | Repair complete |
| Dirty or damaged pins? **NO** | 3D |  |

#### STEP 3D. Check for a pin-to-pin short circuit at the fuel control module.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel control module actuator connector from the fuel control module. Remove the engine harness ring terminal from the fuel shutoff valve. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short circuit. Measure the resistance between the fuel shutoff valve SIGNAL pin of the fuel control module actuator connector and all other pins in the connector. Refer to the wiring diagram or circuit diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3E |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. See one of the following procedures: Replace the engine harness. Use the following procedure in the Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-043 in Section 19. Replace the engine harness. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines Bulletin 4021381. Refer to Procedure 019-043 in Section 19. Replace the engine harness. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-043 in Section 19. | Repair complete |  |

#### STEP 3E. Check for a short circuit to ground in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel control module actuator connector from the fuel control module. Remove the engine harness ring terminal from the fuel shutoff valve. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance between the fuel shutoff valve SIGNAL pin of the engine harness fuel control module actuator connector and engine block ground. Refer to the wiring diagram or circuit diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3F |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. See one of the following procedures: Use the following procedure in the Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-043 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines Bulletin 4021381. Refer to Procedure 019-043 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-043 in Section 19. | Repair complete |  |

#### STEP 3F. Check for a pin-to-pin short circuit in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel control module actuator connector from the fuel control module. Disconnect the engine harness from the ECM. Remove the engine harness ring terminal from the fuel shutoff valve. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short circuit. Measure the resistance between the fuel shutoff valve SIGNAL pin of the engine harness fuel control module actuator connector and all pins in the engine harness engine control module connector. Refer to the wiring diagram or circuit diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3G |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. See one of the following procedures: Use the following procedure in the Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-043 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines Bulletin 4021381. Refer to Procedure 019-043 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-043 in Section 19. | Repair complete |  |

#### STEP 3G. Check ground connections.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check conditions of grounds. Check for loose, missing, or dirty ground connections at the following locations: Engine harness ground at block stud Starter to block ground strap and battery negative Chassis to engine block or battery negative. | Ground connections clean and tight? **YESRepair:** Replace the engine control module. See one of the following procedures: Use the following procedure in the Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-031 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines Bulletin 4021381. Refer to Procedure 019-031 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-031 in Section 19. | Repair complete |
| Ground connections clean and tight? **NORepair:** Tighten and clean ground connections as needed. | Repair complete |  |

#### STEP 3H. Check the fuel shutoff valve resistance.

| **Conditions:** Turn keyswitch OFF. Remove the engine harness ring terminal from the fuel shutoff valve. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutoff valve resistance. Measure the resistance between the fuel shutoff valve ring terminal stud and engine block ground. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Fuel shutoff solenoid resistance: 1 to 5 ohms for 6-VDC solenoids 6 to 15 ohms for 12-VDC solenoids 24 to 50 ohms for 24-VDC solenoids 42 to 80 ohms for 32-VDC solenoids 46 to 87 ohms for 36-VDC solenoids 92 to 145 ohms for 48-VDC solenoids 315 to 375 ohms for 74-VDC solenoids 645 to 735 ohms for 115-VAC solenoids? **YES** | 3I |
| Fuel shutoff solenoid resistance: 1 to 5 ohms for 6-VDC solenoids 6 to 15 ohms for 12-VDC solenoids 24 to 50 ohms for 24-VDC solenoids 42 to 80 ohms for 32-VDC solenoids 46 to 87 ohms for 36-VDC solenoids 92 to 145 ohms for 48-VDC solenoids 315 to 375 ohms for 74-VDC solenoids 645 to 735 ohms for 115-VAC solenoids? **NORepair:** Replace the fuel shutoff valve. See one of the following procedures: Use the following procedure in the Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-050 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines, Bulletin 4021381. Refer to Procedure 019-050 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-050 in Section 19. | Repair complete |  |

#### STEP 3I. Check the engine position sensor installation.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine position sensor for proper installation. Excessive air gap between the sensor and camshaft can cause incorrect speed sensor readings. | Engine position sensor installed correctly? **YES** | 3J |
| Engine position sensor installed correctly? **NORepair:** Install the engine position sensor correctly. Replace the engine position sensor, if necessary. See one of the following procedures: Use the following procedure in the Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-038 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines, Bulletin 4021381. Refer to Procedure 019-038 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-038 in Section 19. | Repair complete |  |

#### STEP 3J. Determine if engine is equipped with exhaust gas recirculation (EGR).

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Determine if the engine is equipped with EGR. | Engine equipped with EGR? **YES** | 3K |
| Engine equipped with EGR? **NO** | Perform next troubleshooting procedure as outlined in Step 2 |  |

#### STEP 3K. Check for coolant in the EGR transfer tube.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Remove the EGR transfer hose from the EGR cooler outlet. | Is coolant present in the crossover tube? **YESRepair:** See the Coolant Loss - Internal symptom tree. | Repair complete |
| Is coolant present in the crossover tube? **NO** | Perform next troubleshooting procedure as outlined in Step 2 |  |

### STEP 4. Fuel system checks.

#### STEP 4A. Check for air in the fuel.

| **Conditions:** Operate engine at low idle (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect the equipment to the fuel pump as shown. | Are air bubbles visible in the sight glass? **YESRepair:** Locate and correct cause of air ingestion in the OEM fuel supply system or damaged fuel filter sealing ring. | Repair complete |
| Are air bubbles visible in the sight glass? **NO** | 4B |  |

#### STEP 4B. Check fuel inlet restriction.

| **Conditions:** Connect a manometer, Part Number ST-1111-3, to the fuel pump supply hose. Turn keyswitch ON. Operate engine at rated speed. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel inlet restriction. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 006-020 in Section 6. | Is fuel inlet restriction less than the specifications listed below? Dirty - 254 mm-Hg \[10 in-Hg\]; New - 152 mm-Hg \[6 in-Hg\] **YES** | 4C |
| Is fuel inlet restriction less than the specifications listed below? Dirty - 254 mm Hg \[10 in-Hg\]; New - 152 mm-Hg \[6 in-Hg\] **NORepair:** Locate the cause of high fuel inlet restriction. Check the prefilter and fuel supply lines. | Repair complete |  |

#### STEP 4C. Check drain line restriction.

| **Conditions:** Connect a manometer, Part Number ST-1111-3, to the fuel drain line. Turn keyswitch ON. Operate engine at rated speed. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Observe reading on the pressure gauge. | Is fuel drain line restriction less than 89 mm-Hg \[3.5 in-Hg\] for Automotive Applications or less than 63.5 mm-Hg \[2.5 in-Hg\] for Industrial/Generator Applications? **YES** | 4D |
| Is fuel drain line restriction less than 89 mm-Hg \[3.5 in-Hg\] for Automotive Applications or less than 63.5 mm-Hg \[2.5 in-Hg\] for Industrial/Generator Applications? **NORepair:** Locate cause of high fuel drain line restriction in OEM fuel return line. | Repair complete |  |

#### STEP 4D. Check fuel pump output pressure.

| **Conditions:** Connect pressure gauge on the Compuchek™ fitting of the fuel pump. Turn keyswitch ON. Operate engine at 1200 rpm (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Observe the reading on the pressure gauge. Use the following procedure in the ISM, ISMe, and QSM11 Service Manual, Bulletin 3666322. Refer to Procedure 005-011 in Section 5. Cranking: minimum of 172 kPa \[25 psi\] Engine operating at 1200 rpm: minimum of 827 kPa \[120 psi\] | Does the fuel pressure meet the specification? **YES** | Perform next troubleshooting procedure as outlined in Step 2 |
| Does the fuel pressure meet the specification? **NO** | 4E |  |

#### STEP 4E. Check fuel gear pump check valve.

| **Conditions:** Disconnect fuel drain line from fuel gear pump housing. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel gear pump check valve for correct installation and operation. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 005-026 in Section 5. | Is check valve installed and operating correctly? **YES** | 4F |
| Is check valve installed and operating correctly? **NORepair:** Install the check valve correctly or replace the fuel gear pump check valve, if necessary. Use the following procedure in the Service Manual, ISM, ISMe and QSM11 Engines, Bulletin 3666322. Refer to Procedure 005-026 in Section 5. | Repair complete |  |

#### STEP 4F. Check fuel supply line for restrictions.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel line between the fuel pump and cylinder head for obstructions. Check the fuel line for sharp bends or kinks that could cause a restriction. | Are fuel lines free from restrictions? **YES** | 4G |
| Are fuel lines free from restrictions? **NORepair:** Remove obstructions from fuel lines. Replace kinked or restricted lines, as necessary. | Repair complete |  |

#### STEP 4G. Check for plugged fuel drillings in the cylinder head.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| If a ReCon® cylinder head was installed, check that the plastic insert has been removed from the fuel supply inlet passage in the cylinder head. | Has plastic insert been removed from the fuel supply passage in the cylinder head? **YES** | Replace the fuel pump. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 005-016 in Section 5. |
| Has plastic insert been removed from the fuel supply passage in the cylinder head? **NORepair:** Remove the plastic insert from the fuel supply passage in the cylinder head. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 002-004 in Section 2. | Repair complete |  |

### STEP 5. Injector diagnostics.

#### STEP 5A. Perform INSITE™ electronic service tool Cylinder Cutout Test.

| **Conditions:** Connect INSITE™ electronic service tool Operate engine at low idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the INSITE™ electronic service tool Cylinder Cutout Test. | All cylinders pass the Cylinder Cutout Test? **YES** | Perform next troubleshooting procedure as outlined in Step 2 |
| All cylinders pass the Cylinder Cutout Test? **NORepair:** Replace the injectors as needed. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 006-026 in Section 6. | Repair complete |  |

### STEP 6. Air handling diagnostic checks.

#### STEP 6A. Start engine and read fault codes.

| **Conditions:** Connect INSITE™ electronic service tool. Operate engine at low idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fault codes with the engine operating. Use INSITE™ electronic service tool to read the fault codes. | Active fault codes? **YES** | Go to appropriate fault code troubleshooting tree |
| Active fault codes? **NO** | 6B |  |

#### STEP 6B. Inspect the turbocharger blades for damage.

| **Conditions:** Turn engine OFF. Remove intake and exhaust connections for turbocharger. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the compressor and turbine fins for damage or wear. | Damage found on turbocharger fins? **YESRepair:** Replace the turbocharger. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-033 in Section 10. | Repair complete |
| Damage found on turbocharger fins? **NO** | 6C |  |

#### STEP 6C. Determination of turbocharger type.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Determine if the turbocharger is a variable geometry turbocharger. | Turbocharger a variable geometry turbocharger? **YES** | 6D |
| Turbocharger a variable geometry turbocharger? **NO** | 6F |  |

#### STEP 6D. Check the variable geometry actuator rod for correct travel.

| **Conditions:** Turn engine OFF. Turn keyswitch ON. Connect INSITE™ electronic service tool. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to perform the Turbocharger Actuator Test. Adjust the delay timer in the Turbocharger Actuator Test so that the rod movement can be observed. Select the retract actuator position with INSITE™ electronic service tool. Mark or scribe the variable geometry actuator rod at the base of the actuator. Select the extend actuator position with INSITE™ electronic service tool. Measure the rod travel by measuring the distance from the base of the turbocharger actuator to the scribe mark. Use a straight edge steel ruler. Retract and extend the turbocharger actuator at least 10 times. Examine the engine dataplate to identify the CPL number. Use the CPL number from the dataplate to identify the proper actuator travel from the CPL table in the Shop Talk section. The turbocharger actuator moves quickly and crisply. If the actuator rod movement is slow, there could be a problem with the air supply, a faulty ground connection on the engine or chassis, or mechanical problems with the variable geometry turbocharger assembly. | Turbocharger actuator rod extend between the minimum and maximum actuator travel specification found in the CPL table in the Shop Talk section? **YES** | 6E |
| Turbocharger actuator rod extend between the minimum and maximum actuator travel specification found in the CPL table in the Shop Talk section? **NO** | 6D-1 |  |

#### STEP 6D-1. Check for air leaks and inspect air lines.

| **Conditions:** Turn engine OFF. Turn keyswitch ON. Connect INSITE™ electronic service tool. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to perform the Turbocharger Actuator Test. Select the extend actuator position. Listen for air leaks at the following components: Turbocharger control valve Turbocharger control shutoff valve inlet connection, if equipped Turbocharger control shutoff valve outlet connection, if equipped Turbocharger control valve inlet connection Turbocharger control valve outlet connection Turbocharger actuator inlet connection Turbocharger actuator All air lines including the OEM supply line to turbocharger control shutoff valve, turbocharger control shutoff valve to turbocharger control valve, and turbocharger control valve to turbocharger actuator. A small amount of air could possibly be heard escaping from the turbocharger control valve during the turbocharger actuator test. This is a normal condition for the valve to achieve output regulation pressure. Do **not** replace the turbocharger control valve for this condition. | Air leaks found in the system? **YESRepair:** Repair air leaks. | Repair complete |
| Air leaks found in the system? **NO** | 6D-2 |  |

#### STEP 6D-2. Check the engine and vehicle grounds.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for loose or corroded engine, chassis, or battery ground connections. Check the engine ground connection. Check the chassis ground connections. Check the battery terminal connections. | Connections tight and corrosion free? **YES** | 6D-3 |
| Connections tight and corrosion free? **NORepair:** Tighten the connections. Tighten the loose connections and clean the terminals. Refer to the OEM service manual. | Repair complete |  |

#### STEP 6D-3. Check for air pressure at the turbocharger control valve outlet.

| **Conditions:** Turn engine OFF. Turn keyswitch ON. Connect INSITE™ electronic service tool. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the Turbocharger Actuator Test, use INSITE™ electronic service tool. Select retract actuator position. Remove the air line connection at the outlet of the turbocharger control valve. Install an M12 Compuchek™ fitting at the outlet of the turbocharger control valve. Install an air pressure gauge that is capable of reading at least 1034 kPa \[150 psi\]. Use INSITE™ electronic service tool to perform the Turbocharger Actuator Test. Select the extend actuator position. | Vehicle air tank pressure present at the turbocharger control valve outlet? **YES** | 6D-4 |
| Vehicle air tank pressure present at the turbocharger control valve outlet? **NO** | 6D-6 |  |

#### STEP 6D-4. Check for air pressure at the turbocharger control valve outlet.

| **Conditions:** Turn engine OFF. Turn keyswitch ON. Connect INSITE™ electronic service tool. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the Turbocharger Actuator Test, use INSITE™ electronic service tool. Select the retract actuator position. Remove the air line connection at the outlet of the turbocharger control valve. Install an M12 Compuchek™ fitting at the outlet of the turbocharger control valve. Install an air pressure gauge capable of reading at least 1034 kPa \[150 psi\]. | Pressure gauge read more than 103 kPa \[15 psi\] after 5 minutes? **YESRepair:** Replace the turbocharger control valve. See one of the following procedures: Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines, Bulletin 4021381. Refer to Procedure 019-388 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-388 in Section 19. | Repair complete |
| Pressure gauge read more than 103 kPa \[15 psi\] after 5 minutes? **NO** | 6D-5 |  |

#### STEP 6D-5. Check for correct turbocharger actuator travel.

| **Conditions:** Turn engine OFF. Turn keyswitch ON. Connect INSITE™ electronic service tool. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Damage to the turbocharger can result if the proper removal procedure is not followed. Remove the variable geometry actuator from the turbocharger. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-033 in Section 10. Use INSITE™ electronic service tool to perform the Turbocharger Actuator Test. Select the extend actuator position. | Turbocharger actuator rod travel at least 12 mm \[0.472 in\]? **YESRepair:** Replace the turbocharger assembly. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-033 in Section 10. | Repair complete |
| Turbocharger actuator rod travel at least 12 mm \[0.472 in\]? **NORepair:** Replace the turbocharger actuator. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-113 in Section 10. | Repair complete |  |

#### STEP 6D-6. Determine if the engine is equipped with a turbocharger control shutoff valve.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Determine if the engine is equipped with a turbocharger control shutoff valve. | Engine equipped with a turbocharger control shutoff valve? **YES** | 6D-7 |
| Engine equipped with a turbocharger control shutoff valve? **NO** | 6D-10 |  |

#### STEP 6D-7. Check for air pressure at the turbocharger control shutoff valve outlet.

| **Conditions:** Turn engine OFF. Turn keyswitch ON. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service to perform the Turbocharger Actuator Test. Select the extend actuator position. Loosen the air line connection at the turbocharger control shutoff valve outlet. | Air heard escaping from the turbocharger control shutoff valve outlet? **YESRepair:** Replace the turbocharger control shutoff valve. See one of the following procedures: Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines, Bulletin 4021381. Refer to Procedure 019-388 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-388 in Section 19. | Repair complete |
| Air heard escaping from the turbocharger control shutoff valve outlet? **NO** | 6D-8 |  |

#### STEP 6D-8. Check for air pressure at the turbocharger control shutoff valve inlet.

| **Conditions:** Turn engine OFF. Turn keyswitch ON. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the OEM air supply line is connected to the correct port on the turbocharger control shutoff valve. Loosen the air line connection at the turbocharger control shutoff valve inlet. | Air heard escaping from the turbocharger control shutoff valve inlet? **YES** | 6D-9 |
| Air heard escaping from the turbocharger control shutoff valve inlet? **NORepair:** Repair the air supply from the OEM air tanks. | Repair complete |  |

#### STEP 6D-9. Check for plugged turbocharger control shutoff valve filter.

| **Conditions:** Remove the turbocharger control shutoff valve filter. Turn keyswitch ON. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to perform the Turbocharger Actuator Test. Select the extend actuator position. Listen for an air leak at the turbocharger control shutoff valve filter head. | Air leak present at the turbocharger control shutoff valve filter head? **YESRepair:** Replace the turbocharger control shutoff valve filter. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-114 in Section 10. | Repair complete |
| Air leak present at the turbocharger control shutoff valve filter head? **NORepair:** Replace the turbocharger control shutoff valve. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines, Bulletin 4021381. Refer to Procedure 019-386 in Section 19. | Repair complete |  |

#### STEP 6D-10. Verify the OEM air supply line is connected to the correct port on the turbocharger control valve.

| **Conditions:** Turn engine OFF. Turn keyswitch ON. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the OEM air supply line is connected to the correct port on the turbocharger control valve. Loosen the air line connection at the turbocharger control valve inlet. | Air heard escaping form the turbocharger control valve inlet? **YESRepair:** Replace the turbocharger control valve. See one of the following procedures: Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines, Bulletin 4021381. Refer to Procedure 019-388 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-388 in Section 19. | Repair complete |
| Air heard escaping from the turbocharger control valve inlet? **NORepair:** Repair the air supply from the OEM air tanks. | Repair complete |  |

#### STEP 6E. Perform INSITE™ electronic service tool EGR Valve/Turbocharger Operational Test.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. Start the engine and operate at low idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Select INSITE™ electronic service tool EGR/Variable Geometry Turbocharger Operational Test. Prior to operating INSITE™ electronic service tool EGR Valve and EGR Valve/Turbocharger Operational Test, the ECM Calibration Software Phase could possibly need to be updated to the latest software phase. The ECM Calibration Phase Software can be checked in INSITE™ electronic service tool, under 'Features and Parameters'. Expand the selection for 'System ID and Dataplate' and go to 'Calibration Information'. If the software phase is earlier than shown below, recalibrate the ECM using the January 2006 INCAL™ CD-ROM, or later. Engines with the software phase listed below or later do **not** require a recalibration. ISM engines with CM875 (engines built after January 2004) require Software Phase 06050312. This is a warrantable calibration change. Choose the Turbocharger actuator option under Test Choices. | Turbocharger Operational Test pass? **YES** | Perform next troubleshooting procedure as outlined in Step 2 |
| Turbocharger Operational Test pass? **NO** | 6E-1 |  |

#### STEP 6E-1. Check the engine and vehicle grounds.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for loose or corroded engine, chassis, or battery ground connections. Check the engine ground connection. Check the chassis ground connections. Check the battery terminal connections. | Connections tight and corrosion free? **YESRepair:** Replace the variable geometry turbocharger. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-033 in Section 10. | Repair complete |
| Connections tight and corrosion free? **NORepair:** Tighten the connections. Tighten the loose connections and clean the terminals. Refer to the OEM service manual. | Verify repair Repair complete |  |

#### STEP 6F. Inspect the wastegate actuator hose.

| **Conditions:** Turn engine OFF. Remove turbocharger if wastegate actuator is inaccessible. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the integral wastegate actuator hose for cracks or holes. | Holes or cracks found in the wastegate actuator hose? **YESRepair:** Replace wastegate actuator hose. | Repair complete |
| Holes or cracks found in the wastegate actuator hose? **NO** | 6G |  |

#### STEP 6G. Inspect the wastegate actuator rod for travel.

| **Conditions:** Turn engine OFF. Remove the wastegate actuator hose from the wastegate actuator. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Apply a regulated air supply of 310 kPa \[45 psi\] to the actuator and check for actuator movement. | Wastegate actuator rod move? **YES** | 6H |
| Wastegate actuator rod move? **NO** | 6G-1 |  |

#### STEP 6G-1. Inspect wastegate actuator rod for travel.

| **Conditions:** Turn engine OFF. Remove the e-clip from the wastegate pin and disconnect the actuator rod. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Apply a regulated air supply of 310 kPa \[45 psi\] to the actuator and check for actuator movement. | Wastegate actuator rod move? **YESRepair:** Move the wastegate lever on the turbocharger back and forth and check for smooth operation. Replace the turbocharger assembly if the wastegate is seized. Use the following procedure in the Troubleshooting and Repair Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-033 in Section 10. | Repair complete |
| Wastegate actuator rod move? **NORepair:** Replace the wastegate actuator. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-050 in Section 10. | Repair complete |  |

#### STEP 6H. Measure resistance of the four-stage wastegate controllers, if equipped.

| **Conditions:** Turn engine OFF. Disconnect the ring terminals from the four-stage wastegate controllers, if equipped. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the wastegate controller post to engine block ground. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Wastegate controller solenoid resistances 6 to 10 ohms for 12-VDC solenoids, 24 to 40 ohms for 24-VDC solenoids? **YES** | 6I |
| Wastegate controller solenoid resistances 6 to 10 ohms for 12-VDC solenoids, 24 to 40 ohms for 24-VDC solenoids? **NORepair:** Replace the damaged wastegate controller. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-109 in Section 10. | Repair complete |  |

#### STEP 6I. Inspect four-stage wastegate controller, if equipped.

| **Conditions:** Turn engine OFF. Remove the four-stage wastegate controllers. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the valve disc, valve seat, and actuator disc for dirt, metal parts, bonding separation, corrosion, cracks, or wear. | Damage or debris found on the valve disc, valve seat, or actuator disc? **YESRepair:** Replace failed components. Clean dirty components | Repair complete |
| Damage or debris found on the valve disc, valve seat, or actuator disc? **NO** | Perform next troubleshooting procedure as outlined in Step 2 |  |

### STEP 7. Check EGR valve for proper operation.

#### STEP 7A. Check for air leaks in the EGR system.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for leaks in the EGR connection tubing and connections. Soot streaks can be noticeable where leaks are present. | Air leaks found in the EGR connection tubing? **YESRepair:** Repair any leaks in the EGR system. | Repair complete |
| Air leaks found in the EGR connection tubing? **NO** | 7B |  |

#### STEP 7B. Check repair history.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check with the customer for a recent EGR valve replacement. | Record of the poppet head missing? **YESRepair:** Remove the exhaust manifold and run a wire through every port to check for the missing poppet head. | 7C |
| Record of the poppet head missing? **NO** | 7C |  |

#### STEP 7C. Perform the EGR Valve Test.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform INSITE™ electronic service tool EGR Valve Test. Prior to performing INSITE™ electronic service tool EGR Valve and EGR Valve/Turbocharger Operational Test, the ECM Calibration Software Phase could possibly need to be updated to the latest software phase. The ECM Calibration Phase Software can be checked in INSITE™ electronic service tool, under 'Features and Parameters'. Expand the selection for 'System ID and Dataplate' and go to 'Calibration Information'. If the software phase is earlier than shown below, recalibrate the ECM using the January 2006 INCAL™ CD-ROM, or later. Engines with the software phase listed below or later do **not** require a recalibration. ISM engines with CM875 (engines built after January 2004) require Software Phase 06050312. This is a warrantable calibration change. Check for complete travel of the EGR valve by selecting Open Valve and verifying the EGR Valve opens 100 percent. | EGR Valve Test pass? **YES** | Perform next troubleshooting procedure as outlined in Step 2. |
| EGR Valve Test pass? **NORepair:** Replace the EGR valve. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 011-022 in Section 11. | Repair complete |  |

### STEP 8. Verify electronic features are operating correctly.

#### STEP 8A. Verify accelerator pedal travel.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to monitor percent accelerator while fully depressing and releasing the accelerator pedal. | Percent accelerator read 0 when the accelerator is released and 100 percent when the accelerator is depressed? **YES** | 8B |
| Throttle position read 0 when the accelerator is released and 100 percent when the accelerator is depressed? **NORepair:** Determine and correct cause of accelerator pedal restriction. | Repair complete |  |

#### STEP 8B. Monitor vehicle speed.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. Start the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to monitor vehicle speed while the vehicle is not moving. | Vehicle speed read 0 when the vehicle is **not** moving? **YES** | 8C |
| Vehicle speed read 0 when the vehicle is **not** moving? **NORepair:** Check the vehicle speed sensor and circuit or locate the cause of the vehicle speed interference. | Repair complete |  |

#### STEP 8C. Verify electronic feature settings are correct.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to verify the following adjustable parameters are correctly set: Maximum vehicle speed Powertrain protection Rear axle ratio Number of transmission tailshaft gear teeth Tire revolutions per mile Gear-down protection Cruise control droop settings Cruise control maximum vehicle speed. | Electronic features set correctly? **YES** | Perform next troubleshooting procedure as outlined in Step 2 |
| Electronic features set correctly? **NORepair:** Correct programmable features. | Repair complete |  |

#### STEP 8D. Check barometric pressure sensor reading.

| **Conditions:** Connect all components. Connect INSITE electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for correct barometric pressure sensor reading. Compare the barometric pressure sensor reading on INSITE™ electronic service tool data monitor/logger to the present local barometric pressure. Refer to Procedure 018-028 in Section V. | Barometric pressure sensor reading in INSITE™ electronic service tool within 5 percent of the present local barometric pressure reading? **YES** | Perform next troubleshooting procedure as outlined in Step 2 |
| Barometric pressure sensor reading in INSITE™ electronic service tool within 5 percent of the present local barometric pressure reading? **NORepair:** Replace the barometric pressure sensor. See one of the following procedures: Use the following procedure in the Troubleshooting and Repair Manual, Electronic Control System, ISM and QSM11 Engines, Bulletin 3666266. Refer to Procedure 019-004 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, ISM Engines, Bulletin 4021381. Refer to Procedure 019-004 in Section 19. Use the following procedure in the Troubleshooting and Repair Manual, CM875 Electronic Control System, ISM Engines, Bulletin 4021477. Refer to Procedure 019-004 in Section 19. | Repair complete |  |

### STEP 9. Perform base engine mechanical checks.

#### STEP 9A. Verify overhead adjustments are correct.

| **Conditions:** Turn keyswitch OFF. Remove valve cover. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the overhead settings. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 003-004 in Section 3. | Overhead settings within the reset limits? **YES** | 9B |
| Overhead settings within the reset limits? **NORepair:** Adjust the overhead settings. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 003-004 in Section 3. | Repair complete |  |

#### STEP 9B. Check air intake restriction.

| **Conditions:** Turn keyswitch ON. Run engine at advertised horsepower and rpm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the intake system restriction by installing a manometer gauge into the air intake system. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-031 in Section 10. | Air intake restriction greater than 635 mm H 2 O \[25 in H 2 O\]? **YESRepair:** Correct the cause of high intake air restriction. Check for plugged air filter or restricted air intake piping. | Repair complete |
| Air intake restriction greater than 635 mm H 2 O \[25 in H 2 O\]? **NO** | 9C |  |

#### STEP 9C. Check exhaust restriction.

| **Conditions:** Install a pressure gauge into the exhaust system. Turn keyswitch ON. Run engine at advertised horsepower and rpm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check exhaust restriction by installing a pressure gauge into the exhaust system just past the turbocharger outlet. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 011-009 in Section 11. | Exhaust restriction within specification listed in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322? **YES** | 9D |
| Exhaust restriction within specification listed in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322? **NORepair:** Repair exhaust system for source of high restriction. | Repair complete |  |

#### STEP 9D. Inspect the charge air cooler.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Pressure test the charge air cooler. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-027 in Section 10. | Pressure drop 34 kPa \[5 psi\] or less in 15 seconds? **YES** | 9E |
| Pressure drop 34 kPa \[5 psi\] or less in 15 seconds? **NORepair:** Repair the charge-air cooler. | Repair complete |  |

#### STEP 9E. Verify engine brake adjustment.

| **Conditions:** Turn keyswitch OFF. Remove valve cover. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the engine brakes are operating correctly. Measure the engine brake settings. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 003-004 in Section 3. | Engine brake settings within the reset limits? **YES** | 9F |
| Engine brake settings within the reset limits? **NORepair:** Adjust the engine brake settings. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 020-024 in Section 20. | Repair complete |  |

#### STEP 9F. Measure turbocharger axial and radial clearance.

| **Conditions:** Turn engine OFF. Disconnect exhaust and intake connections from the turbocharger. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the axial and radial clearances of the turbocharger. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-033 in Section 10. | Axial and radial clearances within specification? **YES** | 9G |
| Axial and radial clearances within specification? **NORepair:** Replace the turbocharger assembly. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-033 in Section 10. | Repair complete |  |

#### STEP 9G. Verify engine blowby is within specification.

| **Conditions:** Turn keyswitch OFF. Connect the appropriate orifice to the end of the blowby draft tube. Start engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Load engine to rated rpm on a chassis dynamometer. Measure the engine blowby. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 014-002 in Section 14. | Engine blowby measurements within specification? **YES** | 9H |
| Engine blowby measurements within specification? **NO** | 9G-1 |  |

#### STEP 9G-1. Verify turbocharger contribution to engine blowby.

> [!danger] WARNING · Опасно
> Do not run the engine for more than one minute. Severe engine damage can occur if the engine is run too long with the turbocharger oil drain line disconnected from the block.

| **Conditions:** Turn keyswitch OFF. Verify oil level is full. Connect the appropriate orifice to the end of the blowby draft tube. Remove turbocharger oil drain line from the block and drain into a bucket. Make sure the turbocharger oil drain port in the block is plugged so no crankcase gases escape. Start engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Load engine to rated rpm on a chassis dynamometer. Measure the engine blowby. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 014-002 in Section 14. | Did the total engine blowby drop more than 30 percent? **YESRepair:** Replace the turbocharger assembly. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 010-033 in Section 10. | Repair complete |
| Did the total engine blowby drop more than 30 percent? **NORepair:** Engine could possibly need to be rebuilt. | Repair complete |  |

#### STEP 9H. Check the static injection timing.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the correct static injection timing. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 006-025 in Section 6. | Is the static injection timing correct? **YES** | Perform the next troubleshooting procedure as outlined in Step 2 |
| Is the static injection timing correct? **NORepair:** Set the static injection timing to specification. Use the following procedure in the Troubleshooting and Repair Manual, ISM, ISMe and QSM11 Engines, Bulletin 3666322. Refer to Procedure 006-025 in Section 6. | Repair complete |  |

### STEP 10. Check the EGR differential pressure sensor and exhaust gas pressure sensor.

#### STEP 10A. Check the EGR differential pressure tubes for cracks, restrictions, or leaks.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the EGR differential pressure tubes for cracks, restrictions, or leaks. Soot streaks can indicate that the line is loose or cracked. | Cracks, restrictions, or leaks present? **YESRepair:** Tighten or replace the EGR differential pressure tubes. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 011-026 in Section 11. | Repair complete |
| Cracks, restrictions, or leaks present? **NO** | Repair complete |  |

#### STEP 10B. Check the exhaust gas pressure tubes for cracks, restrictions, or leaks.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the exhaust gas pressure tubes for cracks, restrictions, or leaks. Soot streaks can indicate that the line is loose or cracked. | Cracks, restrictions, or leaks present? **YESRepair:** Tighten or replace the exhaust gas pressure tubes. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 011-027 in Section 11. | Repair complete |
| Cracks, restrictions, or leaks present? **NO** | Perform the next troubleshooting procedure as outlined in Step 2 |  |

### STEP 11. Check the EGR cooler.

#### STEP 11A. Check the EGR cooler for fouling.

| **Conditions:** Turn fan control switch in OFF position. Turn air conditioning OFF. Connect INSITE™ electronic service tool. Turn keyswitch ON. Make sure coolant temperature is above 79°C \[175°F\]. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| If the effectiveness of the cooler is degraded, the cooler will **not** effectively cool the exhaust gas and will cause the EGR temperature to rise. Before performing INSITE™ electronic service tool EGR Valve and EGR Valve/Turbocharger Operational Test, make sure the ECM Calibration Software Phase is updated to the latest Software Phase. The ECM Calibration Phase Software can be checked in INSITE™ electronic service tool, under "Features and Parameters". Expand the selection for "System ID and Dataplate" and go to "Calibration Information". If the Software Phase is earlier than shown below, calibrate the ECM using the January 2006 INCAL™ CD-ROM, or later. Engines with the Software Phase listed below or later do **not** require a calibration. ISM engines with CM875 (engines built after January 2004) require Software Phase 06050312. This is a warrantable calibration change. Start the engine and set the PTO speed to 1300 rpm. Perform the EGR Valve Test in INSITE™ electronic service tool and command the EGR valve 100 percent open. Start INSITE™ electronic service tool monitor screen and monitor EGR cooler efficiency. Operate the engine at this condition for 4 minutes. After 4 minutes, record the value of EGR cooler efficiency. If the engine fan activates during this test, the test **must** be started over from the beginning. If the EGR cooler efficiency parameter is displayed as "Not Available" in INSITE™ electronic service tool, monitor Exhaust Gas Temperature (Calculated), EGR Temperature, and Engine Coolant Temperature, and record the values after 4 minutes. Use the formula (Exhaust Gas Temperature (Calculated) MINUS EGR Temperature) DIVIDED BY (Exhaust Gas Temperature (Calculated) MINUS Engine Coolant Temperature) MULTIPLED BY 100 to determine EGR cooler efficiency. | EGR cooler efficiency parameter greater than 50 percent after 4 minutes? **YES** | Perform next troubleshooting procedure as outlined in Step 2 |
| EGR cooler efficiency parameter greater than 50 percent after 4 minutes? **NORepair:** Clean or replace the EGR cooler. Use the following procedure in the Service Manual, ISM, ISMe, and QSM11 Engines, Bulletin 3666322. Refer to Procedure 011-019 in Section 11. | Repair complete |  |
