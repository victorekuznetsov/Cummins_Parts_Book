---
aliases:
  - "Дерево диагностики мощностных характеристик"
type: "Процедура"
doc: "60-t02-1001"
title_en: "Engine Performance Troubleshooting Tree"
title_ru: "Дерево диагностики мощностных характеристик"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-t02-1001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-t02-1001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Performance Troubleshooting Tree
**Дерево диагностики мощностных характеристик**

> [!abstract] Процедура · `60-t02-1001`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-t02-1001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-t02-1001.pdf)

Printable Version

### Symptoms

- Engine Acceleration or Response Poor

- Cranking Fuel Pressure is Low

- Engine Operating Fuel Pressure is Low

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

- Engine Will **Not** Reach Rated Speed (RP4CM)

### How To Use This Tree

This symptom tree can be used to troubleshoot all performance based symptoms listed above. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The ECM Calibration Software Phase could possibly need to be updated to the latest Software Phase. The ECM Calibration Phase Software can be checked in INSITE™ electronic service tool, under “Features and Parameters”. Expand the selection for “System ID and Dataplate” and go to “Calibration Information”. If the software phase is earlier than shown below, recalibrate the ECM using the July 2006 INCAL™ CD-ROM, or later.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Perform basic troubleshooting procedures. |  |
|  | **STEP 1A.** Check for active fault codes or high counts of inactive fault codes. | Active fault codes or high counts of inactive fault codes? |
|  | **STEP 1B.** Perform basic troubleshooting checks. | All steps have been verified to be correct? |
| STEP 2. | Determination of engine symptom. |  |
|  | **STEP 2A.** Low power, poor acceleration, or poor response. | Is the engine symptom low power, poor acceleration, or poor response? |
|  | **STEP 2B.** Engine runs rough or misfires. | Is the engine symptom Engine Runs Rough or Misfires? |
|  | **STEP 2C.** Excessive black smoke. | Is the engine symptom Excessive Black Smoke? |
|  | **STEP 2D.** Excessive white smoke. | Is the engine symptom Excessive White Smoke and the engine is using coolant? |
|  | **STEP 2D-1.** Excessive white smoke. | Is the engine symptom Excessive White Smoke and the engine is not using coolant? |
|  | **STEP 2E.** Engine speed surge or engine speed unstable. | Is the engine symptom Engine Speed Surge or Engine Speed Unstable? |
|  | **STEP 2F.** Engine will not start or difficult to start, engine shuts off unexpectedly. | Is the symptom Engine Difficult to Start or Will Not Start, or Engine Shuts Off Unexpectedly? |
| STEP 3. | No-start troubleshooting procedures. |  |
|  | **STEP 3A.** Check fuel shutoff valve voltage. | Is the fuel shutoff valve voltage greater than 11-VDC? |
|  | **STEP 3B.** Determine if engine is equipped with a fuel control module. | Is the engine equipped with a separate fuel control module? |
|  | **STEP 3B-1.** Check the ECM connector and pins. | Dirty or damaged pins? |
|  | **STEP 3B-2.** Check the ECM keyswitch voltage. | Keyswitch voltage equal to battery voltage? |
|  | **STEP 3B-3.** Check the ECM battery supply voltage. | Voltage equal to battery voltage? |
|  | **STEP 3B-4.** Check the ECM actuator connector and pins. | Dirty or damaged pins? |
|  | **STEP 3B-5.** Check for a pin-to-pin short circuit in the engine harness. | Greater than 100k ohms? |
|  | **STEP 3B-6.** Check for a short circuit to ground in the engine harness. | Greater than 100k ohms? |
|  | **STEP 3B-7.** Check the continuity of the fuel shutoff valve circuit. | Less than 10 ohms? |
|  | **STEP 3C.** Check ground connections. | Ground connections clean and tight? |
|  | **STEP 3D.** Check the fuel shutoff valve resistance. | Is the fuel shutoff valve resistance to specification? |
|  | **STEP 3E.** Check the engine position sensor. | Is the engine position sensor installed correctly? |
| STEP 4. | Fuel system checks. |  |
|  | **STEP 4A.** Check for air in the fuel. | Are air bubbles visible in the sight glass? |
|  | **STEP 4B.** Check fuel inlet restriction. | Is fuel inlet restriction less than the specifications? |
|  | **STEP 4C.** Check drain line restriction. | Is fuel drain line restriction less than 63.5 mm Hg \[2.5 in Hg\]? |
|  | **STEP 4D.** Check pump output pressure. | Does the fuel pressure meet the specification? |
|  | **STEP 4E.** Check fuel gear pump check valve. | Is check valve installed and operating correctly? |
|  | **STEP 4F.** Check fuel supply line for restrictions. | Are fuel lines free from restrictions? |
|  | **STEP 4G.** Check for plugged fuel drillings in the cylinder head. | Has the plastic insert been removed from the fuel supply passage in the cylinder head? |
| STEP 5. | Injector diagnostics. |  |
|  | **STEP 5A.** Perform INSITE™ electronic service tool cylinder cutout test. | Do all cylinders pass the cylinder cutout test? |
| STEP 6. | Air handling diagnostic checks. |  |
|  | **STEP 6A.** Start engine and read fault codes. | Active fault codes? |
|  | **STEP 6B.** Inspect the turbocharger blades for damage. | Damage found on turbocharger fins? |
| STEP 7. | Verify electronic features are operating correctly. |  |
|  | **STEP 7A.** Verify accelerator pedal travel. | Does the throttle position read 0 when the accelerator is released and 100 percent when the accelerator is depressed? |
|  | **STEP 7B.** Check barometric pressure sensor reading. | Is the barometric pressure sensor reading in INSITE™ electronic service tool within 5 percent of the present local barometric pressure reading? |
| STEP 8. | Perform base engine mechanical checks. |  |
|  | **STEP 8A.** Verify overhead adjustments are correct. | Are the overhead settings within the reset limits? |
|  | **STEP 8B.** Are the overhead settings within the reset limits? | Is exhaust restriction between 1016 mm H 2 O \[40 in H 2 O\] or 75 mm Hg \[3.0 in Hg\] and 2082 mm H 2 O \[82 in H 2 O\] or 152 mm Hg \[6.0 in Hg\]? |
|  | **STEP 8C.** Measure turbocharger axial and radial clearance. | Are the axial and radial clearances within specification? |
|  | **STEP 8D.** Verify engine blowby is within specification. | Are the engine blowby measurements within specification? |
|  | **STEP 8D-1.** Verify turbocharger contribution to engine blowby. | Did the total engine blowby drop more than 30 percent? |

### STEP 1. Perform basic troubleshooting procedures.

#### STEP 1A. Check for active fault codes or high counts of inactive fault codes.

| **Conditions:** Connect INSITE™ electronic service tool Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes or high counts of inactive fault codes. Use INSITE™ electronic service tool to read the fault codes. | Active fault codes or high counts of inactive fault codes? **YES** | Go to appropriate fault code troubleshooting tree |
| Active fault codes or high counts of inactive fault codes? **NO** | 1B |  |

#### STEP 1B. Perform basic troubleshooting checks.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| The following items must be checked or verified before continuing: Verify the fuel level in the tanks Verify there have not been any changes to CPL components on the engine Verify fuel grade is correct for the application Verify the engine is operating within the recommended altitude Verify engine oil is at the correct level Verify engine parasitics have not changed Verify engine duty cycle has not changed Verify engine cranking speed is greater than 150 rpm. | All steps have been verified to be correct? **YES** | 2A |
| All steps have been verified to be correct? **NORepair:** Correct the condition and verify complaint is no longer present after repair. | Repair complete |  |

### STEP 2. Determination of engine symptom.

#### STEP 2A. Low power, poor acceleration, or poor response.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. Fuel System Checks Air Handling Checks Electronic Checks Injector Checks Base Engine Checks | Is the engine symptom low power, poor acceleration, or poor response? **YES** | Perform the troubleshooting steps suggested in the repair procedure |
| Is the engine symptom low power, poor acceleration, or poor response? **NO** | 2B |  |

#### STEP 2B. Engine runs rough or misfires.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Is the engine symptom Engine Runs Rough or Misfires? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Injector Checks Fuel System Checks Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Is the engine symptom Engine Runs Rough or Misfires? **NO** | 2C |  |

#### STEP 2C. Excessive black smoke.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Is the engine symptom Excessive Black Smoke? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Air Handling Checks Fuel System Checks Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Is the engine symptom Excessive Black Smoke? **NO** | 2D |  |

#### STEP 2D. Excessive white smoke.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Is the engine symptom Excessive White Smoke and the engine is using coolant? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: See the Coolant Loss - Internal symptom tree. | Perform the troubleshooting steps suggested in the repair procedure |
| Is the engine symptom Excessive White Smoke and the engine is using coolant? **NO** | 2D-1 |  |

#### STEP 2D-1. Excessive white smoke.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Is the engine symptom Excessive White Smoke and the engine is **not** using coolant? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Fuel System Checks Injector Checks Air handling checks Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Is the engine symptom Excessive White Smoke and the engine is **not** using coolant? **NO** | 2E |  |

#### STEP 2E. Engine speed surge or engine speed unstable.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Is the engine symptom Engine Speed Surge or Engine Speed Unstable? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Fuel System Checks Injector Checks EGR Differential Pressure and Exhaust Gas Pressure Checks Air Handling Checks Electronics Checks Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Is the engine symptom Engine Speed Surge or Engine Speed Unstable? **NO** | 2F |  |

#### STEP 2F. Engine will not start or difficult to start, engine shuts off unexpectedly.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Is the symptom Engine Difficult to Start or Will **Not** Start, or Engine Shuts Off Unexpectedly? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: No Start Checks Fuel System Checks Injector Checks Air Handling Checks Electronics Checks Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Is the symptom Engine Difficult to Start or Will **Not** Start, or Engine Shuts Off Unexpectedly? **NO** | Return to correct symptom tree |  |

### STEP 3. No-start troubleshooting procedures.

#### STEP 3A. Check fuel shutoff valve voltage.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from the fuel shutoff valve post to engine block ground. | Is the fuel shutoff valve voltage greater than 11-VDC? **YES** | 3B-7 |
| Is the fuel shutoff valve voltage greater than 11-VDC? **NO** | 3B |  |

#### STEP 3B. Determine if engine is equipped with a fuel control module.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Determine if the engine is equipped with a separate fuel control module. | Is the engine equipped with a separate fuel control module? **YES** | 3C |
| Is the engine equipped with a separate fuel control module? **NO** | 3B-1 |  |

#### STEP 3B-1. Check the ECM connector and pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM harness connector and ECM pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damaged Damaged connector locking tab. [[99-019-361 — Component Connector and Pin Inspection\|For general inspection techniques, refer to Procedure 019-361 (Component Connector and Pin Inspection) in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Repair the damaged harness, connector, or pins if possible. Flush the dirt, debris, or moisture from the connector pins, use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Replace the engine harness. Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19. Replace the OEM harness. Refer to the OEM troubleshooting and repair manual. Call for authorization to replace the ECM. Upon receipt of authorization, refer to Procedure 019-031 (Electronic Control Module (ECM)) in Section 19. | Repair complete |
| Dirty or damaged pins? **NO** | 3B-2 |  |

#### STEP 3B-2. Check the ECM keyswitch voltage.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the ECM. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ECM keyswitch voltage. Measure the voltage from the keyswitch input SIGNAL pin of the OEM connector to ground. Refer to the wiring diagram or circuit diagram for connector pin identification. | Keyswitch voltage equal to battery voltage? **YES** | 3B-3 |
| Keyswitch voltage equal to battery voltage? **NORepair:** Repair the OEM keyswitch circuit. Refer to Procedure 019-064 (Key Switch Battery Supply Circuit) in Section 19. | Repair complete |  |

#### STEP 3B-3. Check the ECM battery supply voltage.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM or 4-pin power harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ECM battery supply. Measure the voltage from the battery SUPPLY (+) pins of the OEM or 4-pin power harness connector to the battery SUPPLY (-) pins of the connector. Refer to the wiring diagram or circuit diagram for connector pin identification. | Voltage equal to battery voltage? **YES** | 3B-4 |
| Voltage equal to battery voltage? **NORepair:** Repair the OEM battery supply or keyswitch circuit. Refer to Procedure 019-064 (Key Switch Battery Supply Circuit) in Section 19. | Repair complete |  |

#### STEP 3B-4. Check the ECM connector and pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness or engine harness actuator connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness or engine harness actuator connector and ECM pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damaged Damaged connector locking tab. [[99-019-361 — Component Connector and Pin Inspection\|For general inspection techniques, refer to, Procedure 019-361 (Component Connector and Pin Inspection) in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Repair the damaged harness, connector, or pins if possible. Flush the dirt, debris, or moisture from the connector pins, use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Replace the engine harness. Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19. Replace the OEM harness. Refer to the OEM troubleshooting and repair manual. Call for authorization to replace the ECM. Upon receipt of authorization, refer to Procedure 019-031 (Electronic Control Module (ECM)) in Section 19. | Repair complete |
| Dirty or damaged pins? **NO** | 3B-5 |  |

#### STEP 3B-5. Check for a pin-to-pin short circuit in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness or engine harness actuator connector from the ECM. Remove the engine harness ring terminal from the fuel shutoff valve. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short circuit. Measure the resistance between the fuel shutoff valve SIGNAL pin of the engine harness or engine harness actuator connector, and all pins in the connector. Refer to the wiring diagram or circuit diagram for connector pin identification. [[99-019-360 — Resistance Measurement Using a Multimeter\|For general resistance measurement techniques, refer to Procedure 019-360 (Resistance Measurements Using a Multimeter and a Wiring Diagram) in Section 19.]] | Greater than 100k ohms? **YES** | 3B-6 |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19. | Repair complete |  |

#### STEP 3B-6. Check for a short circuit to ground in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness or engine harness actuator connector from the ECM. Remove the engine harness ring terminal from the fuel shutoff valve. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance between the fuel shutoff valve SIGNAL pin of the engine harness or engine harness actuator connector and ground. Refer to the wiring diagram or circuit diagram for connector pin identification. [[99-019-360 — Resistance Measurement Using a Multimeter\|For general resistance measurement techniques, refer to Procedure 019-360 (Resistance Measurements Using a Multimeter and a Wiring Diagram) in Section 19.]] | Greater than 100k ohms? **YES** | 3B-7 |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19. | Repair complete |  |

#### STEP 3B-7. Check the continuity of the fuel shutoff valve circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness or engine harness actuator connector from the ECM. Disconnect the fuel shutoff valve wire from the valve terminal post. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the continuity of the fuel shutoff valve circuit. Measure the resistance of the fuel shutoff valve SIGNAL circuit between the engine harness or engine harness actuator connector and the fuel shutoff valve eyelet. Refer to the wiring diagram or circuit diagram for connector pin identification. [[99-019-360 — Resistance Measurement Using a Multimeter\|For general resistance measurement techniques, refer to Procedure 019-360 (Resistance Measurements Using a Multimeter and a Wiring Diagram) in Section 19.]] | Less than 10 ohms? **YESRepair:** Call for authorization to replace the ECM. Upon receipt of authorization, refer to Procedure 019-031 (Electronic Control Module (ECM)) in Section 19. | Repair complete |
| Less than 10 ohms? **NORepair:** Repair or replace the engine harness. Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19. | Repair complete |  |

#### STEP 3C. Check ground connections.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check conditions of grounds. Check for loose, missing, or dirty ground connections at the following locations: Engine harness ground at block stud Starter to block ground strap and battery negative Chassis to engine block or battery negative. | Ground connections clean and tight? **YES** | Repair complete |
| Ground connections clean and tight? **NORepair:** Tighten and clean ground connections as needed. | Repair complete |  |

#### STEP 3D. Check the fuel shutoff valve resistance.

| **Conditions:** Turn keyswitch OFF. Remove the engine harness ring terminal from the fuel shutoff valve. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutoff valve resistance. Measure the resistance between the fuel shutoff valve ring terminal stud and engine block ground. [[99-019-360 — Resistance Measurement Using a Multimeter\|For general resistance measurement techniques, refer to Procedure 019-360 (Resistance Measurements Using a Multimeter and a Wiring Diagram) in Section 19.]] | Is the fuel shutoff solenoid resistance: 1 to 5 ohms for 6-VDC solenoids 6 to 15 ohms for 12-VDC solenoids 24 to 50 ohms for 24-VDC solenoids 42 to 80 ohms for 32-VDC solenoids 46 to 87 ohms for 36-VDC solenoids 92 to 145 ohms for 48-VDC solenoids 315 to 375 ohms for 74-VDC solenoids 645 to 735 ohms for 115-VAC solenoids? **YES** | 3I |
| Is the fuel shutoff solenoid resistance: 1 to 5 ohms for 6-VDC solenoids 6 to 15 ohms for 12-VDC solenoids 24 to 50 ohms for 24-VDC solenoids 42 to 80 ohms for 32-VDC solenoids 46 to 87 ohms for 36-VDC solenoids 92 to 145 ohms for 48-VDC solenoids 315 to 375 ohms for 74-VDC solenoids 645 to 735 ohms for 115-VAC solenoids? **NORepair:** Replace the fuel shutoff valve. Refer to Procedure 019-050 (Fuel Shutoff Valve) in Section 19. | Repair complete |  |

#### STEP 3E. Check the engine position sensor installation.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine position sensor for proper installation. Excessive air gap between the sensor and camshaft can cause incorrect speed sensor readings. | Is the engine position sensor installed correctly? **YES** | 4A |
| Is the engine position sensor installed correctly? **NORepair:** Install the engine position sensor correctly. Replace the engine position sensor, if necessary. Refer to Procedure 019-038 (Engine Position Sensor (EPS) in Section 19. | Repair complete |  |

### STEP 4. Fuel system checks.

#### STEP 4A. Check for air in the fuel.

| **Conditions:** Engine running at low idle (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect the equipment to the fuel pump as shown. | Are air bubbles visible in the sight glass? **YESRepair:** Locate and correct cause of air ingestion in the OEM fuel supply system or damaged fuel filter sealing ring. | Repair complete |
| Are air bubbles visible in the sight glass? **NO** | 4B |  |

#### STEP 4B. Check fuel inlet restriction.

| **Conditions:** Connect a manometer, Part Number ST-1111-3, to the fuel pump supply hose. Turn keyswitch ON. Engine running at rated speed. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel inlet restriction. Refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 in the Service Manual, QST30, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. | Is fuel inlet restriction less than the specifications listed below? Dirty - 254 mm Hg \[10 in Hg\]; New - 152 mm Hg \[6 in Hg\] **YES** | 4C |
| Is fuel inlet restriction less than the specifications listed below? Dirty - 254 mm Hg \[10 in Hg\]; New - 152 mm Hg \[6 in Hg\] **NORepair:** Locate the cause of high fuel inlet restriction. Check the prefilter and fuel supply lines. | Repair complete |  |

#### STEP 4C. Check drain line restriction.

| **Conditions:** Connect a manometer, Part Number ST-1111-3, to the fuel drain line. Turn keyswitch ON. Engine running at rated speed. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Observe reading on the pressure gauge. | Is fuel drain line restriction less than 63.5 mm Hg \[2.5 in Hg\]? **YES** | 4D |
| Is fuel drain line restriction less than 63.5 mm Hg \[2.5 in Hg\]? **NORepair:** Locate cause of high fuel drain line restriction in OEM fuel return line. | Repair complete |  |

#### STEP 4D. Check pump output pressure.

| **Conditions:** Connect pressure gauge on the Compuchek™ fitting of the fuel pump. Turn keyswitch ON. Engine running at 1200 rpm (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fuel pressure at 1200 rpm, or cranking if engine will not start. Read the fuel pressure while cranking if the engine will **not** start. Cranking: minimum of 172 kPa \[25 psi\] Engine running at 1200 rpm: minimum of 827 kPa \[120 psi\] | Does the fuel pressure meet the specification? **YES** | Perform next troubleshooting procedure as outlined in Step 2 |
| Does the fuel pressure meet the specification? **NO** | 4E |  |

#### STEP 4E. Check fuel gear pump check valve.

| **Conditions:** Disconnect fuel drain line from fuel gear pump housing. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel gear pump check valve for correct installation and operation. [[57-005-012-tr — Fuel Injection Pumps, In-Line\|Refer to Procedure 005-012 (Fuel Injection Pump, In-Line)) in Section 5 in the Service Manual, QST30, Bulletin 4021539.]] | Is check valve installed and operating correctly? **YES** | 4F |
| Is check valve installed and operating correctly? **NORepair:** Install the check valve correctly or replace the fuel gear pump check valve, if necessary. Refer to Procedure 005-012 (Fuel Injection Pump, In-Line)) in Section 5 in the Service Manual, QST30, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. | Repair complete |  |

#### STEP 4F. Check fuel supply line for restrictions.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel line between the fuel pump and cylinder head for obstructions. Check the fuel line for sharp bends or kinks that could cause a restriction. | Are fuel lines free from restrictions? **YES** | 4G |
| Are fuel lines free from restrictions? **NORepair:** Remove obstructions from fuel lines. Replace kinked or restricted lines as necessary. | Repair complete |  |

#### STEP 4G. Check for plugged fuel drillings in the cylinder head.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| If a ReCon® cylinder head was installed, check that the plastic insert has been removed from the fuel supply inlet passage in the cylinder head. | Has the plastic insert been removed from the fuel supply passage in the cylinder head? **YES** | Perform the next troubleshooting procedure. |
| Has plastic insert been removed from the fuel supply passage in the cylinder head? **NORepair:** Remove the plastic insert from the fuel supply passage in the cylinder head. Refer to Procedure 002-004 (Cylinder Head) in Section 2 in the Service Manual, QST30, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. | Repair complete |  |

### STEP 5. Injector diagnostics.

#### STEP 5A. Perform INSITE™ electronic service tool cylinder cutout test.

| **Conditions:** Connect INSITE™ electronic service tool Engine running at low idle |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform INSITE™ electronic service tool cylinder cutout test. | Do all cylinders pass the cylinder cutout test? **YES** | Perform next troubleshooting procedure as outlined in Step 2 |
| Do all cylinders pass the cylinder cutout test? **NORepair:** Replace the injectors as needed. Refer to Procedure 006-026 (Injector) in Section 6 in the Service Manual, QST30, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. | Repair complete |  |

### STEP 6. Air handling diagnostic checks.

#### STEP 6A. Start engine and read fault codes.

| **Conditions:** Connect INSITE™ electronic service tool. Engine running at low idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fault codes with the engine running. Use INSITE™ electronic service tool to read the fault codes. | Active fault codes? **YES** | Go to appropriate fault code troubleshooting tree |
| Active fault codes? **NO** | 6B |  |

#### STEP 6B. Inspect the turbocharger blades for damage.

| **Conditions:** Engine OFF. Remove intake and exhaust connections for turbocharger. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the compressor and turbine fins for damage or wear. | Damage found on turbocharger fins? **YESRepair:** Replace the turbocharger. [[57-010-033-tr — Turbocharger\|Refer to Procedure 010-033 (Turbocharger) in Section 10 in the Service Manual, QST30, Bulletin 4021539.]] | Repair complete |
| Damage found on turbocharger fins? **NO** | 7 |  |

### STEP 7. Verify electronic features are operating correctly.

#### STEP 7A. Verify throttle lever travel.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to monitor Percent Accelerator while fully depressing and releasing the throttle lever. | Does the Percent Throttle read 0 when the accelerator is released and 100 percent when the accelerator is depressed? **YES** | 7B |
| Does the Percent Throttle read 0 when the accelerator is released and 100 percent when the accelerator is depressed? **NORepair:** Determine and correct cause of accelerator pedal restriction. | Repair complete |  |

#### STEP 7B. Check barometric pressure sensor reading.

| **Conditions:** Connect all components. Connect INSITE electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for correct barometric pressure sensor reading. Compare the barometric pressure sensor reading on INSITE™ electronic service tool data monitor/logger to the present local barometric pressure. | Is the barometric pressure sensor reading in INSITE™ electronic service tool within 5 percent of the present local barometric pressure reading? **YES** | Perform next troubleshooting procedure as outlined in Step 2 |
| Is the barometric pressure sensor reading in INSITE™ electronic service tool within 5 percent of the present local barometric pressure reading? **NORepair:** Replace the barometric pressure sensor. Refer to Procedure 019-004 (Barometric Air Pressure Sensor) in Section 19. | Repair complete |  |

### STEP 8. Perform base engine mechanical checks.

#### STEP 8A. Verify overhead adjustments are correct.

| **Conditions:** Turn keyswitch OFF. Remove valve cover. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the overhead settings. Refer to Procedure 003-004 (Overhead Set) in Section 3 in the Service Manual, QST30, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. | Are the overhead settings within the reset limits? **YES** | 8B |
| Are the overhead settings within the reset limits? **NORepair:** Adjust the overhead settings. Refer to Procedure 003-004 (Overhead Set) in Section 3 in the Service Manual, QST30, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. | Repair complete |  |

#### STEP 8B. Check exhaust restriction.

| **Conditions:** Install a pressure gauge into the exhaust system. Turn keyswitch ON. Run engine at advertised horsepower and rpm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check exhaust restriction by installing a pressure gauge into the exhaust system just past the turbocharger outlet. Refer to Procedure 011-009 (Exhaust Restriction) in Section 11 in the Service Manual, QST30, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. | Is exhaust restriction between 1016 mm H 2 O \[40 in H 2 O\] or 75 mm Hg \[3.0 in Hg\] and 2082 mm H 2 O \[82 in H 2 O\] or 152 mm Hg \[6.0 in Hg\]? **YES** | 8C |
| Is exhaust restriction between 1016 mm H 2 O \[40 in H 2 O\] or 75 mm Hg \[3.0 in Hg\] and 2082 mm H 2 O \[82 in H 2 O\] or 152 mm Hg \[6.0 in Hg\]? **NORepair:** Repair exhaust system for source of high restriction. | Repair complete |  |

#### STEP 8C. Measure turbocharger axial and radial clearance.

| **Conditions:** Engine OFF. Disconnect exhaust and intake connections from the turbocharger. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the axial and radial clearances of the turbocharger. [[57-010-033-tr — Turbocharger\|Refer to Procedure 010-033 (Turbocharger) in Section 10 in the Service Manual, QST30, Bulletin 4021539.]] | Are the axial and radial clearances within specification? **YES** | 8D |
| Are the axial and radial clearances within specification? **NORepair:** Replace the turbocharger assembly. Refer to Procedure 010-033 (Turbocharger) in the Service Manual, QST30, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. | Repair complete |  |

#### STEP 8D. Verify engine blowby is within specification.

| **Conditions:** Turn keyswitch OFF. Connect the appropriate orifice to the end of the blowby draft tube. Start engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Load engine to rated rpm on a chassis dynamometer. Measure the engine blowby. [[57-010-033-tr — Turbocharger\|Refer to Procedure 010-033 (Turbocharger) in the Service Manual, QST30, Bulletin 4021539.]] | Are the engine blowby measurements within specification? **YES** | Repair Complete |
| Are the engine blowby measurements within specification? **NO** | 8D-1 |  |

#### STEP 8D-1. Verify turbocharger contribution to engine blowby.

| **Conditions:** Turn keyswitch OFF. Verify oil level is full. Connect the appropriate orifice to the end of the blowby draft tube. Remove turbocharger oil drain line from the block and drain into a bucket. Make sure the turbocharger oil drain port in the block is plugged so no crankcase gases escape. Start engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Replace the turbocharger assembly. [[57-010-033-tr — Turbocharger\|Refer to Procedure 010-033 (Turbocharger) in the Service Manual, QST30, Bulletin 4021539.]] | Did the total engine blowby drop more than 30 percent? **YES** | Repair complete |
| Did the total engine blowby drop more than 30 percent? **NORepair:** Engine could possibly need to be rebuilt. See the engine rebuild specifications. | Repair complete |  |
