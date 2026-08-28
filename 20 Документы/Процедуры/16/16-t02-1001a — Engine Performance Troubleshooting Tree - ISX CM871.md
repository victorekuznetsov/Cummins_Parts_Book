---
type: "Процедура"
doc: "16-t02-1001a"
title_en: "Engine Performance Troubleshooting Tree - ISX CM871"
modified: "2014-03-27"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/16/16-t02-1001a.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/16-t02-1001a.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/16"
---

# Engine Performance Troubleshooting Tree - ISX CM871

> [!abstract] Процедура · `16-t02-1001a`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section TT - Troubleshooting Symptoms · Section TT - Troubleshooting Symptoms (New Format) · Sectopm TT - Troubleshooting Symptoms
> **Даты:** изменён 2014-03-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/16/16-t02-1001a.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/16-t02-1001a.pdf)

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

- Engine Starts But Will **Not** Keep Operating

- Engine Will **Not** Reach Rated Speed (rpm)

- Engine Run-on or Will **Not** Shut Down.

### How To Use This Tree

This symptom tree can be used to troubleshoot all performance-based symptoms listed above. Start by performing Step 1 troubleshooting. Step 2 asks a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom. Perform the list of troubleshooting in the sequence shown in the Specifications/Repair section of the tree.

### Shoptalk

Verify the engine control module (ECM) calibration is correct. Check the calibration revision history found on QuickServe™ Online for applicable fixes to the calibration stored in the ECM. If necessary, calibrate the ECM. Use the following procedure in the Troubleshooting and Repair Manual, CM871 and CM876 Electronic Control Systems, ISX and ISM Engines, Bulletin 4021560. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Perform basic troubleshooting procedures. |  |
|  | **STEP 1A.** Check for active fault codes or high counts of inactive fault codes. | Active fault codes or high counts of inactive fault codes? |
|  | **STEP 1B.** Perform basic troubleshooting checks. | All steps verified to be correct? |
|  | **STEP 1C.** Perform INSITE™ electronic service tool monitor test. | 'Engine Operating State' reading a value that can cause an engine derate? |
|  | **STEP 1D.** Check engine pressure sensors for accuracy. | Pressures within specification? |
| STEP 2. | Determination of engine symptom. |  |
|  | **STEP 2A.** Low power, poor acceleration, or poor response. | Engine symptom - Low Power, Poor Acceleration, or Poor Response? |
|  | **STEP 2B.** Engine misfire. | Engine symptom - Engine Misfires? |
|  | **STEP 2C.** Excessive black smoke. | Engine symptom - Excessive Black Smoke? |
|  | **STEP 2D.** Excessive white smoke. | Engine symptom - Excessive White Smoke and Engine is Using Coolant? |
|  | **STEP 2D-1.** Excessive white smoke. | Engine symptom - Excessive White Smoke and Engine is Using Coolant? |
|  | **STEP 2E.** Engine speed surge or engine speed unstable. | Engine symptom - Engine Speed Surge or Engine Speed Unstable? |
|  | **STEP 2F.** Engine will not start or difficult to start. | Engine symptom - Engine Difficult to Start or Will **Not** Start? |
|  | **STEP 2G.** Engine stalls or shuts off unexpectedly. | Engine symptom - Engine Stalls or Shuts Off Unexpectedly? |
|  | **STEP 2H.** Engine run-on or will not shut down. | Engine symptom - Engine Run-On or Slow to Shut Down after operating at high idle for 1 minute then keyed OFF? |
| STEP 3. | No-start troubleshooting procedures. |  |
|  | **STEP 3A.** Verify the fuel system has primed. | Fuel system been properly primed? |
|  | **STEP 3B.** Check fuel shutoff valve voltage. | Fuel shutoff valve voltage greater than 11-VDC (volts of direct current)? |
|  | **STEP 3B-1.** Check the keyswitch voltage. | Keyswitch voltage equal to battery voltage? |
|  | **STEP 3B-2.** Check the fuel shutoff valve wire. | Less than 10 ohms? |
|  | **STEP 3B-3.** Check the ECM power and ground. | ECM battery supply voltage equal to the battery voltage? |
|  | **STEP 3C.** Check fuel shutoff valve resistance. | Fuel shutoff solenoid resistance: 1 to 5 ohms for 6-VDC solenoids; 6 to 15 ohms for 12-VDC solenoids; 24 to 50 ohms for 24-VDC solenoids; 42 to 80 ohms for 32-VDC solenoids; 46 to 87 ohms for 36-VDC solenoids; 92 to 145 ohms for 48-VDC solenoids; 315 to 375 ohms for 74-VDC solenoids; or 645 to 735 ohms for 115-VAC solenoids? |
|  | **STEP 3D.** Check the fuel shutoff valve actuator. | Debris or damage found on the valve disc, valve seat, or actuator disc? |
|  | **STEP 3E.** Check for correct priming pump operation, if equipped. | Lift pump operates after turning the keyswitch ON? |
|  | **STEP 3E-1.** Check priming pump pressure. | Pump pressure meets the 69 kPa \[10 psi\] specification? |
|  | **STEP 3F.** Check for coolant in the exhaust gas recirculation (EGR) transfer tube. | Coolant present in the crossover tube? |
| STEP 4. | Fuel system checks. |  |
|  | **STEP 4A.** Verify the fuel system has been primed. | Fuel system properly primed? |
|  | **STEP 4B.** Check for air in the fuel. | Air bubbles visible in the coil of clear tubing? |
|  | **STEP 4C.** Check for fuel inlet restriction. | Fuel inlet restriction less than the specifications listed? Dirty - 305 mm-Hg \[12 in-Hg\]; New - 203 mm-Hg \[8 in-Hg\] |
|  | **STEP 4D.** Check for drain line restriction. | Fuel drain line restriction less than 229 mm-Hg \[9 in-Hg\]? |
|  | **STEP 4E.** Check rail fuel pressure. | Rail fuel pressure meets the specification? |
|  | **STEP 4E-1.** Check the pressure side fuel filter restriction | Pressure-side fuel filter pressure drop less than 517 kPa \[75 psi\]? |
|  | **STEP 4E-2.** Check 1724 kPa \[250 psi\] pressure regulator. | 1724 kPa \[250 psi\] pressure regulator free of debris or damage? |
|  | **STEP 4E-3.** Check 2206 kPa \[320 psi\] or 2620 kPa \[380 psi\] pressure regulator. | Pressure regulator free of debris or damage? |
| STEP 5. | Injector and Actuator Diagnostics. |  |
|  | **STEP 5A.** Perform the Injector Check Valve Leak Tst. | Injector Leak Test detects a leaking injector? |
|  | **STEP 5B.** Perform INSITE™ electronic service tool Cylinder Performance Test. | INSITE™ electronic service tool Cylinder Performance Test identifies a single malfunctioning injector? |
|  | **STEP 5B-1.** Perform INSITE™ electronic service tool Cylinder Performance Test at 600 rpm. | INSITE™ electronic service tool Cylinder Performance Test identifies a single malfunctioning injector? |
|  | **STEP 5B-2.** Perform INSITE™ electronic service tool Cylinder Performance Test at 700 rpm. | INSITE™ electronic service tool Cylinder Performance Test identifies a single malfunctioning injector? |
|  | **STEP 5B-3.** Perform INSITE™ electronic service tool Cylinder Performance Test at 800 rpm. | INSITE™ electronic service tool Cylinder Performance Test identifies a single malfunctioning injector? |
|  | **STEP 5C.** Perform INSITE™ electronic service tool Cylinder Cutout Test. | Cylinders pass the Cylinder Cutout Test? |
|  | **STEP 5C-1.** Perform INSITE™ electronic service tool Cylinder Cutout Test on both injector banks. | Malfunctioning bank of injectors isolated by operating the engine on either bank of injectors? |
|  | **STEP 5C-2.** Perform INSITE™ electronic service tool Cylinder Cutout Test. | Malfunctioning injector isolated by operating the engine on a single injector? |
|  | **STEP 5C-3.** Verify overhead adjustments are correct for the suspected malfunctioning injector. | Overhead settings within the reset limits outlines in Procedure 003-004 in Section 3? |
|  | **STEP 5D.** Swap the front and rear metering actuators. | Cylinder Performance Test finds a malfunctioning bank? |
|  | **STEP 5E.** Swap the front and rear timing actuators. | Malfunctioning bank follows the timing actuator? |
|  | **STEP 5F.** Perform the Timing Actuator Flow Test. | Timing Actuator Flow Test finds a malfunctioning actuator? |
|  | **STEP 5G.** Monitor the engine percent load value with INSITE™ electronic service tool. (Perform this step for troubleshooting low power only.) | Engine percent load value consistently above 8 percent? |
| STEP 6. | Air handling diagnostic checks. |  |
|  | **STEP 6A.** Start the engine and read the fault codes. | Active fault codes? |
|  | **STEP 6B.** Check air intake restriction. | Air intake restriction greater than 635 mm-H 2 O \[25 in-H 2 O\] for a used air filter or 254 mm-H 2 O \[10 in-H 2 O\] for a new filter? |
|  | **STEP 6C.** Inspect the charge-air cooler. | Pressure drop 34 kPa \[5 psi\] or less in 15 seconds? |
|  | **STEP 6D.** Inspect the turbocharger blades for damage. | Damage found on turbocharger blades? |
|  | **STEP 6E.** Inspect the turbocharger shaft movement. | Nozzle slides evenly from stop to stop and gear teeth undamaged? |
| STEP 7. | Check exhaust gas recirculation (EGR) valve for proper operation. |  |
|  | **STEP 7A.** Check for exhaust gas recirculation (EGR)-related fault codes. | EGR-related fault codes present? |
|  | **STEP 7B.** Check for inactive EGR differential pressure sensor fault codes. | Fault Code 1866, 2273, or 2274 active? |
|  | **STEP 7C.** Check the EGR differential pressure tubes for leaks. | Leaks detected at either the low or high EGR differential pressure tubes? |
|  | **STEP 7D.** Check the EGR differential pressure sensor adapter for leaks. | Leaks detected at the EGR differential pressure sensor adapter? |
|  | **STEP 7E.** Check the EGR differential pressure tubes for plugging. | Debris or soot found in either EGR differential pressure tube? |
|  | **STEP 7F.** Check for air leaks in the EGR system. | Leaks found in the EGR connection tubing? |
| STEP 8. | Verify electronic features are operating correctly. |  |
|  | **STEP 8A.** Verify accelerator pedal travel. | Accelerator pedal reads 0 when the accelerator is released and 100 percent when the accelerator is depressed? |
|  | **STEP 8B.** Monitor vehicle speed. | Vehicle speed reads 0 when the vehicle is not moving? |
|  | **STEP 8C.** Verify electronic feature settings are correct. | Electronic features set correctly? |
|  | **STEP 8D.** Check the intake manifold pressure sensor accuracy. | INSITE™ electronic service tool reading within 17 kPa \[2.5 psi\] of mechanical gauge reading? |
| STEP 9. | Perform base engine mechanical checks. |  |
|  | **STEP 9A.** Verify injection timing is correct. | Injection timing correct? |
|  | **STEP 9B.** Verify overhead adjustments are correct. | Overhead settings within the reset limits? |
|  | **STEP 9C.** Verify engine brake adjustment. | Engine brake settings within the reset limits? |
|  | **STEP 9D.** Verify crankshaft tone wheel is not loose. | Crankshaft tone wheel loose? |
|  | **STEP 9E.** Check exhaust restriction. | Exhaust restriction greater than 305 mm-Hg \[12.0 in-Hg\]? |
|  | **STEP 9F.** Verify engine blowby is within specification. | Engine blowby measurements within specification? |
| STEP 10. | Aftertreatment checks. |  |
|  | **STEP 10A.** Check for aftertreatment-related fault codes. | Fault codes related to the aftertreatment system found to be active? |
|  | **STEP 10B.** Perform basic aftertreatment troubleshooting checks. | All parts inspected and appear to be functioning properly? |
|  | **STEP 10C.** Check for signs of internal damage to the aftertreatment system. | Any visible smoke (black or white) present during the snap throttle acceleration? |
|  | **STEP 10D.** Check exhaust restriction. | Exhaust restriction greater than 305 mm-Hg \[12.0 in-Hg\]? |

### STEP 1. Perform basic troubleshooting procedures.

#### STEP 1A. Check for active fault codes or high counts of inactive fault codes.

| **Conditions:** Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes or high counts of inactive fault codes. Use INSITE™ electronic service tool to read the fault codes. | Active fault codes or high counts of inactive fault codes? **YES** | Go to appropriate fault code troubleshooting tree |
| Active fault codes or high counts of inactive fault codes? **NO** | 1B |  |

#### STEP 1B. Perform basic troubleshooting checks.

| **Conditions:** N/A |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| The following items must be checked or verified before continuing: Verify the fuel level in the tanks. Verify there have not been any changes to CPL components on the engine. Verify fuel grade is correct for the application. Verify the engine is operating within the recommended altitude. Verify engine oil is at the correct level. Verify engine parasitics have not changed. Verify engine duty cycle has not changed. Verify engine cranking speed is greater than 150 rpm. Verify battery voltage is within specification. | All steps verified to be correct? **YES** | 1C |
| All steps verified to be correct? **NORepair:** Correct the out-of-specification item and verify complaint is no longer present after repair. | Repair complete |  |

#### STEP 1C. Perform INSITE™ electronic service tool monitor test.

| **Conditions:** Connect INSITE™ electronic service tool. Operate engine at the speed and load where the symptom occurs. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to monitor the parameter 'Engine Operating State' at the same engine operating conditions where the symptom occurs. Refer to Advanced Engine Performance Troubleshooting Techniques, Bulletin [[4021686 — Advanced Engine Performance Troubleshooting Techniques\|4021686]], for a description of what "User Fueling States (Engine Operating States)" can cause engine derates. | 'Engine Operating State' reading a value that can cause an engine derate? **YESRepair:** Determine if the engine derate is being caused by normal engine operation or by actual engine damage. Continue following troubleshooting steps as outlined in Step 2 if an engine failure is suspected. | 2A |
| 'Engine Operating State' reading a value that can cause an engine derate? **NO** | 1D |  |

#### STEP 1D. Check engine pressure sensors for accuracy.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use an electronic service tool to monitor the following pressure values: Barometric pressure: INSITE™ electronic service tool reading within 51 mm-Hg \[2 in-Hg\] of local barometric pressure? Intake manifold pressure: INSITE™ electronic service tool reading between -77 mm-Hg \[-3 in-Hg\] and 77 mm-Hg \[3 in-Hg\]? EGR differential pressure: INSITE™ electronic service tool reading for EGR delta pressure 0 kPa \[0 psi\]? Exhaust gas pressure: INSITE™ electronic service tool reading within ± 102 mm-Hg \[± 4 in-Hg\] of local ambient air pressure? Aftertreatment diesel particulate filter (DPF) differential pressure: INSITE™ electronic service tool reading 0 ± 3 kPa \[0 ± 0.89 in-Hg\]? | Pressures within specification? **YES** | 2A |
| Pressures within specification? **NORepair:** Replace the pressure sensor that was reading out of specification. Reference the appropriate sensor procedure. | Repair complete. |  |

### STEP 2. Determination of engine symptom.

#### STEP 2A. Low power, poor acceleration, or poor response.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom Low Power, Poor Acceleration, or Poor Response? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 6 - Air Handling Checks Step 7 - EGR Checks Step 10 - Aftertreatment Checks Step 8 - Electronic Checks Step 5 - Injector Checks Step 9 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom Low Power, Poor Acceleration, or Poor Response? **NO** | 2B |  |

#### STEP 2B. Engine misfire.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom - Engine Misfires? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 5 - Injector Checks Step 4 - Fuel System Checks Step 9 - Base Engine Checks Step 7 - EGR Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom - Engine Misfires? **NO** | 2C |  |

#### STEP 2C. Excessive black smoke.

| **Conditions:** Disconnect the exhaust pipe from the aftertreatment inlet. Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the exhaust smoke. Perform two snap accelerations from low to high idle. Hold the engine at high idle for 5 seconds. A small puff of black smoke upon acceleration that clears at a steady high idle speed is normal. To perform a Snap Acceleration Test, it can be necessary to temporarily adjust the Maximum Engine Speed with No vehicle speed sensor (VSS) parameter in INSITE™ electronic service tool to the high idle speed of the engine. Progressive damage to the aftertreatment system has occurred if black smoke is visible. Remove the exhaust aftertreatment system from the vehicle and inspect for reuse. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Inspect the aftertreatment system for potential damage. [[101-011-049-tr — Aftertreatment Diesel Oxidation Catalyst\|Refer to Procedure 011-049 in Section 11.]] | Engine symptom - Excessive Black Smoke? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 6 - Air Handling Checks Step 7 - EGR Checks Step 4 - Fuel System Checks Step 5 - Injector and Actuator Diagnostics Step 9 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom - Excessive Black Smoke? **NO** | 2D |  |

#### STEP 2D. Excessive white smoke.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom - Excessive White Smoke and the Engine is Using Coolant? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: See the Coolant Loss - Internal trobleshooting symptom tree. | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom - Excessive White Smoke and the Engine is Using Coolant? **NO** | 2D-1 |  |

#### STEP 2D-1. Excessive white smoke.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom - Excessive White Smoke and the Engine is **not** Using Coolant? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 5 - Injector Checks Step 10 - Aftertreatment Checks Step 6 - Air Handling Checks Step 9 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom - Excessive White Smoke and the Engine is **not** Using Coolant? **NO** | 2E |  |

#### STEP 2E. Engine speed surge or engine speed unstable.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom - Engine Speed Surge or Engine Speed Unstable? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 5 - Injector Checks Step 7 - EGR Checks Step 6 - Air Handling Checks Step 8 - Electronics Checks Step 9 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom - Engine Speed Surge or Engine Speed Unstable? **NO** | 2F |  |

#### STEP 2F. Engine will not start or difficult to start.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom - Engine Difficult to Start or Will **Not** Start? **YESRepair:** Perform the troubleshooting steps that pertain to difficult to start or will **not** start concerns per the troubleshooting steps in the recommended order listed below: Step 3 - No Start Checks Step 4 - Fuel System Checks Step 5 - Injector Checks Step 6 - Air Handling Checks Step 8 - Electronics Checks Check the engine base timing. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 001-088 in Section 1. Step 9 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom - Engine Difficult to Start or Will **Not** Start? **NO** | 2G |  |

#### STEP 2G. Engine stalls or shuts off unexpectedly.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom - Engine Stalls or Shuts Off Unexpectedly? **YESRepair:** Perform the troubleshooting steps that pertain to stalls or shuts off unexpectedly per the troubleshooting steps in the recommended order listed below: Step 3 - No Start Checks Step 4 - Fuel System Checks Step 5 - Injector Checks Step 6 - Air Handling Checks Step 8 - Electronics Checks Step 9 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom - Engine Stalls or Shuts Off Unexpectedly? **NO** | 2H |  |

#### STEP 2H. Engine run-on or will **not** shut down.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. | Engine symptom - Engine Run-On or Slow to Shut Down after operating at high idle for 1 minute then keyed OFF? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 5 - Injector Checks Step 4 - Fuel System Checks Step 9 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom - Engine Run-On or Slow to Shut Down after operating at high idle for 1 minute then keyed OFF? **NO** | Return to appropriate symptom tree |  |

### STEP 3. No-start troubleshooting procedures.

#### STEP 3A. Verify the fuel system has been primed.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the fuel system has been primed. If entering this tree after a component has been replaced in the fuel system, or after the engine has been run out of fuel, verify the fuel system has been properly primed before proceeding. Use the following procedure for fuel system priming found in the Signature™, ISX, and QSX Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 006-015 in Section 6. | Fuel system properly primed? **YES** | 3B |
| Fuel system properly primed? **NORepair:** Prime the fuel system. Use the following procedure for fuel system priming found in the Signature™, ISX, and QSX Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 006-015 in Section 6. | Repair complete |  |

#### STEP 3B. Check fuel shutoff valve voltage.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from the fuel shutoff valve post to engine block ground. | Fuel shutoff valve voltage greater than 11-VDC? **YES** | 3C |
| Fuel shutoff valve voltage greater than 11-VDC? **NO** | 3B-1 |  |

#### STEP 3B-1. Check ECM keyswitch voltage.

| **Conditions:** Turn keyswitch OFF. Disconnect the original equipment manufacturer (OEM) harness from the ECM. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from the keyswitch input SIGNAL wire of the OEM harness to engine block ground. | Keyswitch voltage equal to battery voltage? **YES** | 3B-2 |
| Keyswitch voltage equal to battery voltage? **NORepair:** Repair or replace the OEM power harness, or keyswitch, or check the battery connections. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. [[99-019-064 — Key Switch Power Supply Circuit\|Refer to Procedure 019-064 in Section 19.]] | Repair complete |  |

#### STEP 3B-2. Check the fuel shutoff valve wire.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the fuel shutoff valve wire from the valve terminal post. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the fuel shutoff valve SIGNAL pin in the ECM connector to the fuel shutoff valve eyelet. Use the following procedure for general resistance measurement techniques. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YESRepair:** Replace the ECM. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. Refer to Procedure 019-031 in Section 19. | 3B-3 |
| Less than 10 ohms? **NORepair:** Repair or replace the engine harness. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. Refer to Procedure 019-043 in Section 19. | Repair complete |  |

#### STEP 3B-3. Check the ECM power and ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the ECM power supply connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from the ECM battery SUPPLY (-) pins to the ECM battery SUPPLY (+) pins in the ECM power harness connector. | ECM battery supply voltage equal to the battery voltage? **YESRepair:** Replace the ECM. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. Refer to Procedure 019-031 in Section 19. | Repair complete |
| ECM battery supply voltage equal to the battery voltage? **NO** | Repair complete |  |

#### STEP 3C. Check fuel shutoff valve resistance.

| **Conditions:** Turn keyswitch OFF. Disconnect fuel shutoff valve SIGNAL wire from the fuel shutoff solenoid. Be sure fuel shutoff valve temperature is between 20°C \[68°F\] and 25°C \[78°F\]. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the fuel shutoff solenoid post to engine block ground. The fuel shutoff solenoid **must** be between 20°C \[68°F\] and 25°C \[78°F\] before using the resistance specifications listed. Use the following procedure for general resistance measurement techniques. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Fuel shutoff solenoid resistance: 1 to 5 ohms for 6-VDC solenoids 6 to 15 ohms for 12-VDC solenoids 24 to 50 ohms for 24-VDC solenoids 42 to 80 ohms for 32-VDC solenoids 46 to 87 ohms for 36-VDC solenoids 92 to 145 ohms for 48-VDC solenoids 315 to 375 ohms for 74-VDC solenoids 645 to 735 ohms for 115-VAC solenoids? **YES** | 3D |
| Fuel shutoff solenoid resistance: 1 to 5 ohms for 6-VDC solenoids 6 to 15 ohms for 12-VDC solenoids 24 to 50 ohms for 24-VDC solenoids 42 to 80 ohms for 32-VDC solenoids 46 to 87 ohms for 36-VDC solenoids 92 to 145 ohms for 48-VDC solenoids 315 to 375 ohms for 74-VDC solenoids 645 to 735 ohms for 115-VAC solenoids? **NORepair:** Replace the fuel shutoff solenoid. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. Refer to Procedure 019-050 in Section 19. | Repair complete |  |

#### STEP 3D. Check fuel shutoff valve actuator.

| **Conditions:** Turn keyswitch OFF. Remove the fuel shutoff valve solenoid, valve disc, valve seat, and actuator. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the valve disc, valve seat, and actuator disc for dirt, metal debris, bonding separation, corrosion, cracks, or wear. | Debris or damage found on the valve disc, valve seat, or actuator disc? **YESRepair:** Replace the damaged fuel shutoff valve component. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. Refer to Procedure 019-050 in Section 19. | Repair complete |
| Debris or damage found on the valve disc, valve seat, or actuator disc? **NO** | 3E |  |

#### STEP 3E. Check for correct priming pump operation, if equipped.

| **Conditions:** Turn keyswitch OFF. Assemble fuel shutoff valve components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Listen for lift pump operation after the keyswitch is turned to the ON position. **Not** all ISX engines use a priming pump and **not** all priming pumps actuate at keyswitch ON. Verify the type of pump system on the engine before beginning this step. | Lift pump operates after turning the keyswitch ON or does the engine **not** use a priming pump? **YES** | 3E-1 |
| Lift pump operates after turning the keyswitch ON or does the engine **not** use a priming pump? **NORepair:** Check or replace lift pump. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 005-045 in Section 5. | Repair complete |  |

#### STEP 3E-1. Check priming pump pressure.

| **Conditions:** Turn keyswitch OFF. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the priming pressure at the quick connect fitting located on the top of the integrated fuel system module (IFSM). Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 005-045 in Section 5. | Pump pressure meets the 69 kPa \[10 psi\] specification? **YES** | 3F |
| Pump pressure meets the 69 kPa \[10 psi\] specification? **NO** | Replace the lift pump. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 005-045 in Section 5. |  |

#### STEP 3F. Check for coolant in the EGR transfer tube.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Remove the EGR transfer hose from the EGR cooler outlet. | Coolant present in the crossover tube? **YESRepair:** See the Coolant Loss - Internal symptom tree. | Repair complete |
| Coolant present in the crossover tube? **NORepair:** Perform the next troubleshooting procedure as outlined in Step 2 | 2A |  |

### STEP 4. Fuel system checks.

#### STEP 4A. Verify the fuel system has been primed.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the fuel system has been primed. If entering this tree after a component has been replaced in the fuel system, or after the engine has been emptied of fuel, verify the fuel system has been properly primed before proceeding. Use the following procedure for fuel system priming found in the Signature™, ISX, and QSX Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 006-015 in Section 6. | Fuel system been properly primed? **YES** | 4B |
| Fuel system been properly primed? **NORepair:** Prime the fuel system. Use the following procedure for fuel system priming found in the Signature™, ISX, and QSX Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 006-015 in Section 6. | Repair complete |  |

#### STEP 4B. Check for air in the fuel.

| **Conditions:** Operate the engine at low idle (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect the equipment to the quick-connect fitting at the fuel module as shown. Put a coil in the clear hose. Put the end of the clear hose in a clean container. Operate the engine at low idle with no load. Slightly open the valve until a steady stream of fuel is visible. | Air bubbles visible in the coil of clear tubing? **YESRepair:** Locate and correct the cause of air ingestion in the OEM fuel supply system or damaged fuel filter sealing ring. With EGR Check the ECM cooling plate, associated plumbing, and o-ring seals for malfunctions that can cause air ingestion. Repair or replace the malfunctioning component. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 006-006 in Section 6. | Repair complete |
| Air bubbles visible in the coil of clear tubing? **NO** | 4C |  |

#### STEP 4C. Check fuel inlet restriction.

| **Conditions:** Connect a vacuum gauge to the suction side Compuchek™ fitting. Turn keyswitch ON. Operate the engine at high idle (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| If the engine uses a priming pump, wait until after the priming pump has turned off and observe the reading on the vacuum gauge. Check the fuel inlet restriction. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 006-020 in Section 6. | Fuel inlet restriction less than the specifications listed below? Dirty - 305 mm-Hg \[12 in-Hg\]; - New - 203 mm-Hg \[8 in-Hg\] **YES** | 4D |
| Fuel inlet restriction less than the specifications listed below? Dirty - 305 mm-Hg \[12 in-Hg\]; - New - 203 mm-Hg \[8 in-Hg\] **NORepair:** Locate the cause of high fuel inlet restriction. Check the suction-side fuel filter, fuel supply lines, and inlet check valve. | Repair complete |  |

#### STEP 4D. Check drain line restriction.

| **Conditions:** Connect pressure gauge, Part Number 3375278. Turn keyswitch ON. Operate the engine at high idle (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Observe reading on the pressure gauge. | Fuel drain line restriction less than 229 mm-Hg \[9 in-Hg\]? **YES** | 4E |
| Fuel drain line restriction less than 229 mm-Hg \[9 in-Hg\]? **NORepair:** Locate the cause of high fuel drain line restriction in the OEM fuel return line. | Repair complete |  |

#### STEP 4E. Check rail fuel pressure.

| **Conditions:** Connect pressure gauge, Part Number 3375932, on the Compuchek™ fitting (as shown). Turn keyswitch ON. Operate the engine at low idle (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the rail fuel pressure at low idle and high idle. Read the rail fuel pressure while cranking if the engine will **not** start. Cranking: greater than 689 kPa \[100 psi\] at 130 rpm for at least 10 seconds. Low idle: 1589 to 1889 kPa \[230 to 274 psi\] at 600 rpm. High idle: 1896 to 2068 kPa \[275 to 325 psi\] at 1800 rpm. | Rail fuel pressure meet the specification? **YES** | Perform the next troubleshooting procedure as outlined in Step 2 |
| Rail fuel pressure meet the specification? **NO** | 4E-1 with EGR 4E-2 |  |

#### STEP 4E-1. Check the pressure side fuel filter restriction.

| **Conditions:** Connect pressure gauge, Part Number 3375932, on the rail fuel pressure Compuchek™ fitting. Connect pressure gauge, Part Number 3375932, on the gear pump output pressure Compuchek™ fitting. Operate the engine at high idle (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fuel pressure drop across the pressure side fuel filter at high idle or while cranking if the engine will not start. | Pressure-side fuel filter pressure drop less than 517 kPa \[75 psi\]? **YES** | 4E-2 |
| Pressure-side fuel filter pressure drop less than 517 kPa \[75 psi\]? **NORepair:** Replace the pressure side fuel filter. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-006-015-tr — Fuel Filter (Spin-On Type)\|Refer to Procedure 006-015 in Section 6.]] | Repair complete |  |

#### STEP 4E-2. Check 1724 kPa \[250 psi\] pressure regulator.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Remove the 1724 kPa \[250 psi\] fuel pressure regulator. Inspect for debris or damage or incomplete sealing of the regulator. | 1724 kPa \[250 psi\] pressure regulator free of debris or damage? **YES** | 4E-3 |
| 1724 kPa \[250 psi\] pressure regulator free of debris or damage? **NORepair:** Replace 1724 kPa \[250 psi\] regulator. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-005-073-tr — Integrated Fuel System Module (IFSM)\|Refer to Procedure 005-073 in Section 5.]] | Repair complete |  |

#### STEP 4E-3. Check 2206 kPa \[320 psi\] or 2620 kPa \[380 psi\] pressure regulator.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Remove the 2206 kPa \[320 psi\] fuel pressure regulator. Inspect for debris, damage, or incomplete sealing of the regulator. | Pressure regulator free of debris or damage? **YESRepair:** Replace the gear pump module. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-005-016 — Fuel Pump\|Refer to Procedure 005-016 in Section 5.]] | Repair complete |
| Pressure regulator free of debris or damage? **NORepair:** Replace 2620 kPa \[380 psi\] regulator. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-005-073-tr — Integrated Fuel System Module (IFSM)\|Refer to Procedure 005-073 in Section 5.]] | Repair complete |  |

### STEP 5. Injector and Actuator Diagnostics.

#### STEP 5A. Perform the Injector Check Valve Leak Test.

| **Conditions:** - |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform thePerform the Injector Check Valve Leak Test to check for internal injector check valve damage. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] | Injector leak test detects a leaking injector? **YESRepair:** Replace the leaking injector. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] | Repair complete |
| Injector leak test detects a leaking injector? **NO** | 5B |  |

#### STEP 5B. Perform INSITE™ electronic service tool Cylinder Performance Test.

| **Conditions:** Troubleshoot any active fault codes before performing the test. Note that engine coolant temperature must be greater than 83°C \[180°F\]. Connect INSITE™ electronic service tool. Idle engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the INSITE™ electronic service tool Cylinder Performance Test. During the initial 30 seconds of the Cylinder Performance Test, INSITE™ electronic service tool is checking to make sure all parameters have been met to enter the test. Once the initial Pass or Fail reading is displayed, the test is live for the next 2 minutes. Monitor the display to see if cylinders or banks drop out during this 2 minute window. A cylinder can switch from pass to fail and back to pass quickly, so monitor the screen closely. | INSITE™ electronic service tool Cylinder Performance Test identifies a single malfunctioning injector? **YES** | 5C-3 |
| INSITE™ electronic service tool Cylinder Performance Test identifies a single malfunctioning injector? **NO** | 5B-1 |  |

#### STEP 5B-1. Perform INSITE™ electronic service tool Cylinder Performance Test at 600 rpm.

| **Conditions:** Troubleshoot any active fault codes before performing the test. Note that engine coolant temperature must be greater than 83°C \[180°F\]. Connect INSITE™ electronic service tool. Idle engine at 600 rpm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Skip this step and move on to step 5B-2 if the rpm value is the same as that used in step 5B. Adjust the low speed to 600 rpm and perform INSITE™ electronic service tool Cylinder Performance Test. During the initial 30 seconds of the Cylinder Performance Test, INSITE™ electronic service tool is checking to make sure all parameters have been met to enter the test. Once the initial Pass or Fail reading is displayed, the test is live for the next 2 minutes. Monitor the display to see if cylinders or banks drop out during this 2 minute window. A cylinder can switch from pass to fail and back to pass quickly, so monitor the screen closely. | INSITE™ electronic service tool Cylinder Performance Test identifies a single malfunctioning injector? **YES** | 5C-3 |
| INSITE™ electronic service tool Cylinder Performance Test identifies a single malfunctioning injector? **NO** | 5B-2 |  |

#### STEP 5B-2. Perform INSITE™ electronic service tool Cylinder Performance Test at 700 rpm.

| **Conditions:** Troubleshoot any active fault codes before performing the test. Note that engine coolant temperature must be greater than 83°C \[180°F\]. Connect INSITE™ electronic service tool. Idle engine at 700 rpm. The idle speed may need to be adjusted to perform this test. Toggle the cruise control increment/decrement switch to see if the idle speed can be adjusted. If **not**, use INSITE™ electronic service tool to either enable the Adjustable Low Idle Speed feature or adjust the Low Idle Speed. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Skip this step and move on to step 5B-3 if the RPM value is the same as that used in step 5B. Adjust the low speed to 700 rpm and perform INSITE™ electronic service tool Cylinder Performance Test. During the initial 30 seconds of the Cylinder Performance Test, INSITE™ electronic service tool is checking to make sure all parameters have been met to enter the test. Once the initial Pass or Fail reading is displayed, the test is live for the next 2 minutes. Monitor the display to see if cylinders or banks drop out during this 2 minute window. A cylinder can switch from pass to fail and back to pass quickly, so monitor the screen closely. | INSITE™ electronic service tool Cylinder Performance Test identifies a single malfunctioning injector? **YES** | 5C-3 |
| INSITE™ electronic service tool Cylinder Performance Test identifies a single malfunctioning injector? **NO** | 5B-3 |  |

#### STEP 5B-3. Perform INSITE™ electronic service tool Cylinder Performance Test at 800 rpm.

| **Conditions:** Troubleshoot any active fault codes before performing the test. Note that engine coolant temperature must be greater than 83°C \[180°F\]. Connect INSITE™ electronic service tool. Idle engine at 800 rpm. The idle speed may need to be adjusted to perform this test. Toggle the cruise control increment/decrement switch to see if the idle speed can be adjusted. If **not**, use INSITE™ electronic service tool to either enable the "Adjustable Low Idle Speed" feature or adjust the Low Idle Speed. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Skip this step and move on to step 5C if the rpm value is the same as that used in step 5B. Adjust the low speed to 800 rpm and perform INSITE™ electronic service tool Cylinder Performance Test. During the initial 30 seconds of the Cylinder Performance Test, INSITE™ electronic service tool is checking to make sure all parameters have been met to enter the test. Once the initial Pass or Fail reading is displayed, the test is live for the next 2 minutes. Monitor the display to see if cylinders or banks drop out during this 2 minute window. A cylinder can switch from pass to fail and back to pass quickly, so monitor the screen closely. | INSITE™ electronic service tool Cylinder Performance Test identifies a single malfunctioning injector? **YES** | 5C-3 |
| INSITE™ electronic service tool Cylinder Performance Test identifies a single malfunctioning injector? **NO** | 5C |  |

#### STEP 5C. Perform INSITE™ electronic service tool Cylinder Cutout Test

| **Conditions:** Turn air conditioning OFF. Turn fan OFF. Disable any electrical loads. Idle engine at the engine speed at which the misfire is present. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform INSITE™ electronic service tool cylinder cutout test. A failing cylinder will have no effect on engine sound and operation when cut out using this test. | All cylinders pass the cylinder cutout test? **YES** | 5C-1 |
| All cylinders pass the cylinder cutout test? **NO** | 5C-3 |  |

#### STEP 5C-1. Perform INSITE™ electronic service tool Cylinder Cutout Test on individual injector banks.

| **Conditions:** Turn air conditioning OFF. Turn fan OFF. Disable any electrical loads. Engine idling at the engine speed at which the misfire is present. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform INSITE™ electronic service tool Cylinder Cutout Test. Operate the engine on the front bank of injectors identified by the cylinder cutout test by disabling the rear three cylinders 4, 5, 6 cylinders with INSITE™ electronic service tool. Operate the engine on the rear bank of injectors identified by the Cylinder Performance Test by disabling the front three cylinders (1,2,3) with INSITE™ electronic service tool. To disable one bank of cylinders with INSITE™ electronic service tool, click on the cylinder numbers associated with that bank. The front bank consists of cylinders 1, 2, and 3 and the rear bank is cylinders 4, 5, and 6. A malfunctioning bank of injectors will cause the engine to run poorly when the opposite bank is cut out using this test. | Malfunctioning bank of injectors isolated by operating the engine on either bank of injectors? **YES** | 5D |
| Malfunctioning bank of injectors isolated by operating the engine on either bank of injectors? **NO** | 5C-2 |  |

#### STEP 5C-2. Perform INSITE™ electronic service tool Cylinder Cutout Test single cylinder operation.

| **Conditions:** Turn air conditioning OFF. Turn fan OFF. Disable any electrical loads. Idle engine at the engine speed at which the misfire is present. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform INSITE™ electronic service tool cylinder cut out test. Operate the engine on the cylinder identified by the Cylinder Performance Test by disabling five cylinders with INSITE™ electronic service tool and **only** operating on the suspect cylinder. To disable five cylinders with INSITE™ electronic service tool, click on the cylinder numbers until **only** one cylinder is enabled. The engine should roughly maintain idle speed when operating on a single cylinder. A weak or misfiring cylinder will be detected if the engine dies or can **not** maintain idle speed when operating on a single cylinder. Continue testing all six cylinders by operating the engine on each individual injector. If the engine will **not** run on one cylinder regardless of the cylinder selected, increase the idle RPM and retest. Do **not** operate the engine on one cylinder for an extended period of time. | Malfunctioning injector isolated by operating the engine on a single injector? **YES** | 5C-3 |
| Malfunctioning injector isolated by operating the engine on a single injector? **NO** | 5D |  |

#### STEP 5C-3. Verify overhead adjustments are correct for the suspected malfunctioning injector.

| **Conditions:** Turn keyswitch OFF. Remove the rocker lever cover. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 003-011 in Section 3. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the overhead settings for the suspected malfunctioning injector. Check the valve lash and injector pre-load torque before replacing the injector. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 003-004 in Section 3. | Overhead settings within the reset limits outlined in Procedure 003-004? **YESRepair:** Replace the malfunctioning injector. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] | Repair complete |
| Overhead settings within the reset limits outlined in Procedure 003-004? **NORepair:** Adjust the overhead settings. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-003-004-tr — Overhead Set\|Refer to Procedure 003-004 in Section 3.]] Perform the Cylinder Performance Test to determine if a misfire still exists after adjusting the overhead settings. | 5B |  |

#### STEP 5D. Swap the front and rear metering actuators.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the timing and metering actuators. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Swap the front and rear metering actuators to determine if the malfunctioning bank of cylinders follows a specific metering actuator. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. Refer to Procedure 019-110 in Section 19. Perform INSITE™ electronic service tool Cylinder Performance Test. | Cylinder Performance Test finds a malfunctioning bank? **YESRepair:** Replace the malfunctioning metering actuator. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. Refer to Procedure 019-110 in Section 19. | Repair complete |
| Cylinder Performance Test finds a malfunctioning bank? **NO** | 5E |  |

#### STEP 5E. Swap the front and rear timing actuators

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the timing and metering actuators. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Swap the front and rear timing actuators to determine if the malfunctioning bank of cylinders follows a specific timing actuator. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. Refer to Procedure 019-111 in Section 19. Perform INSITE™ electronic service tool Cylinder Performance Test. | Malfunctioning bank follows the timing actuator? **YESRepair:** Replace the timing actuator. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. Refer to Procedure 019-111 in Section 19. | Repair complete |
| Malfunctioning bank follows the timing actuator? **NO** | 5F |  |

#### STEP 5F. Perform the Timing Actuator Flow Test

| **Conditions:** Turn air conditioning OFF. Turn fan OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the Timing Actuator Flow Test. Use the following procedure found in the Signature, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 005-239 in Section 5. Perform the flow test on each bank. | Timing Actuator Flow Test finds a malfunctioning actuator? **YESRepair:** Replace the timing actuator. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. Refer to Procedure 019-111 in Section 19. | Repair complete |
| Timing Actuator Flow Test finds a malfunctioning actuator? **NO** | 5G |  |

#### STEP 5G. Monitor the engine percent load value with INSITE™ electronic service tool. (Perform this step for troubleshooting low power **only**.)

| **Conditions:** Connect INSITE™ electronic service tool. Idle the engine at operating temperature. Operate engine at no load. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Monitor the engine percent load value with INSITE™ electronic service tool with the engine operating at idle. | Engine percent load value consistently above 8 percent? **YESRepair:** Replace both metering actuators. Use the following procedure in the CM871 and CM876 Electronic Control Systems, ISX and ISM Engines Troubleshooting and Repair Manual, Bulletin 4021560. Refer to Procedure 019-110 in Section 19. | Repair complete |
| Engine percent load value consistently above 8 percent? **NO** | Perform the next troubleshooting procedure as outlined in Step 2 |  |

### STEP 6. Air handling diagnostic checks.

#### STEP 6A. Start the engine and read the fault codes.

| **Conditions:** Connect INSITE™ electronic service tool. Operate engine at low idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fault codes with the engine operating. Use INSITE™ electronic service tool to read the fault codes. | Active fault codes? **YES** | Go to appropriate fault code troubleshooting tree |
| Active fault codes? **NO** | 6B |  |

#### STEP 6B. Check air intake restriction.

| **Conditions:** Turn keyswitch ON. Run engine at advertised horsepower and rpm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the intake system restriction by installing a vacuum gauge or water manometer into the air intake system. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 010-031 in Section 10. | Air intake restriction greater than 635 mm-H 2 O \[25 in-H 2 O\] for a used air filter or 254 mm-H 2 O \[10 in-H 2 O\] for a new filter? **YESRepair:** Correct the cause of high intake air restriction. Check for a plugged air filter or restricted air intake piping. | Repair complete |
| Air intake restriction greater than 635 mm-H 2 O \[25 in-H 2 O\] for a used air filter or 254 mm-H 2 O \[10 in-H 2 O\] for a new filter? **NO** | 6C |  |

#### STEP 6C. Inspect the charge-air cooler

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Pressure test the charge-air cooler. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 010-027 in Section 10. | Pressure drop 34 kPa \[5 psi\] or less in 15 seconds? **YES** | 6D |
| Pressure drop 34 kPa \[5 psi\] or less in 15 seconds? **NORepair:** Repair the charge-air cooler assembly. Refer to the OEM service manual. | Repair complete |  |

#### STEP 6D. Inspect the turbocharger blades for damage.

| **Conditions:** Turn engine OFF. Remove intake and exhaust connections from turbocharger. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the compressor and turbine fins for damage or wear. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | Damage found on turbocharger blades? **YESRepair:** Replace the turbocharger. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | Repair complete |
| Damage found on turbocharger blades? **NO** | 6E |  |

#### STEP 6E. Inspect the turbocharger shaft movement.

| **Conditions:** Turn keyswitch OFF. Remove VGT actuator from the turbocharger. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sector gear on the turbocharger for damaged or broken gear teeth. Move the sector gear lever on the turbocharger bearing housing up and down from stop to stop. Check for smooth movement between the stops. There will be an initial friction force that **must** be overcome before the actuator lever will move. Once movement is started, the actuator lever should move to the other stop position by hand. Use the following procedure in the Signature™, ISX and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-010-134 — Variable Geometry Turbocharger Actuator, Electric\|Refer to Procedure 010-134 in Section 10.]] | Nozzle slides evenly from stop to stop and gear teeth undamaged? **YESRepair:** Install the turbocharger actuator. Use the following procedure in the Signature™, ISX and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-010-134 — Variable Geometry Turbocharger Actuator, Electric\|Refer to Procedure 010-134 in Section 10.]] | Perform the next troubleshooting procedure as outlined in Step 2. |
| Nozzle slides evenly from stop to stop and gear teeth undamaged? **NORepair:** A turbocharger mechanical malfunction has been detected. Inspect the turbocharger for repair and reuse, if possible. Use the following procedure in the Signature™, ISX and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-010-145 — Variable Geometry Turbocharger Shroud Plate\|Refer to Procedure 010-145 in Section 10.]] | Repair complete |  |

### STEP 7. Check EGR valve for proper operation.

#### STEP 7A. Check for EGR-related fault codes

| **Conditions:** Turn keyswitch OFF. Wait 30 seconds. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for any EGR-related fault codes. | EGR-related fault codes present? **YESRepair:** Troubleshoot electronic fault codes. | Appropriate fault code troubleshooting trees |
| EGR-related fault codes present? **NO** | 7B |  |

#### STEP 7B. Check for inactive EGR differential pressure sensor fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1866, 2273, or 2274 active? **YES** | Appropriate fault code troubleshooting tree |
| Fault Code 1866, 2273, or 2274 active? **NO** | 7C |  |

#### STEP 7C. Check the EGR differential pressure tubes for leaks.

| **Conditions:** Note leaks by traces of soot. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the lines for leaks. | Leaks detected at either the low or high EGR differential pressure tubes? **YESRepair:** Tighten the fittings or replace the EGR differential pressure tube. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 011-026 in Section 11. | Repair complete |
| Leaks detected at either the low or high EGR differential pressure tubes? **NO** | 7D |  |

#### STEP 7D. Check the EGR differential pressure sensor adapter for leaks.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the EGR differential pressure sensor adapter for leaks. Leaks will be easily noted by traces of soot. If necessary remove the sensor to inspect the o-rings between the EGR differential pressure sensor and the adapter for proper sealing. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 011-028 in Section 11. | Leaks detected at the EGR differential pressure sensor adapter? **YESRepair:** Replace the EGR differential pressure sensor adapter. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 011-028 in Section 11. | Repair complete |
| Leaks detected at the EGR differential pressure sensor adapter? **NO** | 7E |  |

#### STEP 7E. Check the EGR differential pressure tubes for plugging.

| **Conditions:** Turn keyswitch OFF. Remove the EGR differential pressure tubes. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the EGR differential pressure tubes for restrictions, soot plugging, and plugging. | Debris or soot found in either EGR differential pressure tube? **YESRepair:** Clear the debris or replace the EGR differential pressure tube. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 011-026 in Section 11. Remove the exhaust aftertreatment system from the vehicle and inspect for reuse. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 011-050 in Section 11. | Repair complete |
| Debris or soot found in either EGR differential pressure tube? **NO** | 7F |  |

#### STEP 7F. Check for air leaks in the EGR system.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for leaks in the EGR connection tubing and connections. Soot streaks are noticeable where leaks are present. | Leaks found in the EGR connection tubing? **YESRepair:** Repair any leaks in the EGR system. | Repair complete |
| Leaks found in the EGR connection tubing? **NO** | Perform the next troubleshooting procedure as outlined in Step 2 |  |

### STEP 8. Verify electronic features operating correctly.

#### STEP 8A. Verify accelerator pedal travel.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| With INSITE™ electronic service tool, monitor accelerator pedal while fully depressing and releasing the accelerator pedal. | Accelerator pedal reads 0 percent when the accelerator is released and 100 percent when the accelerator is depressed? **YES** | 8B |
| Accelerator pedal reads 0 percent when the accelerator is released and 100 percent when the accelerator is depressed? **NORepair:** Determine and correct the cause of accelerator pedal restriction. | Repair complete |  |

#### STEP 8B. Monitor vehicle speed.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. Start the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| With INSITE™ electronic service tool, monitor vehicle speed while the vehicle is not moving. | Vehicle speed reads 0 when the vehicle is **not** moving? **YES** | 8C |
| Vehicle speed reads 0 when the vehicle is **not** moving? **NORepair:** Check the vehicle speed sensor and circuit or locate the cause of the vehicle speed interference. | Repair complete |  |

#### STEP 8C. Verify electronic feature settings are correct.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| With INSITE™ electronic service tool, verify the following adjustable parameters are correctly set: Maximum vehicle speed Powertrain protection Rear axle ratio Number of transmission tailshaft gear teeth Tire revolutions per mile Gear-down protection Cruise control droop settings Cruise control maximum vehicle speed. | Electronic features set correctly? **YES** | 8D |
| Electronic features set correctly? **NORepair:** Correct programmable features. | Repair complete |  |

#### STEP 8D. Check the intake manifold pressure sensor accuracy.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. Start and operate the engine at high idle after connecting the mechanical intake manifold pressure gauge. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect a mechanical intake manifold pressure gauge to the engine, as close to the intake manifold pressure sensor as possible. Start INSITE™ electronic service tool Data Monitor/Logger and compare INSITE™ electronic service tool reading for intake manifold pressure to the mechanical gauge. | INSITE™ electronic service tool reading within 17 kPa \[2.5 psi\] of mechanical gauge reading? **YES** | Perform the next troubleshooting procedure as outlined in Step 2 |
| INSITE™ electronic service tool reading within 17 kPa \[2.5 psi\] of mechanical gauge reading? **NORepair:** Remove and clean the intake manifold pressure sensor. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. Refer to Procedure 019-159 in Section 19. | Repair complete |  |

### STEP 9. Perform base engine mechanical checks.

#### STEP 9A. Verify injection timing is correct.

| **Conditions:** Turn keyswitch OFF. Remove valve cover. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify injection timing is correct. Measure the injection timing. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-006-025 — Static Injection Timing\|Refer to Procedure 006-025]] in Section 6. If the injection timing is found to be out of specification, bar the engine to "insert pin" and install the crankshaft pin. Install the appropriate injector camshaft wedge to set the correct injection timing. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-001-088-tr — Engine Base Timing\|Refer to Procedure 001-088 in Section 1.]] | Injection timing correct? **YES** | 9B |
| Injection timing correct? **NORepair:** Correct the injection timing. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-001-088-tr — Engine Base Timing\|Refer to Procedure 001-088 in Section 1.]] | Repair complete |  |

#### STEP 9B. Verify overhead adjustments are correct.

| **Conditions:** Turn keyswitch OFF. Remove valve cover. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the overhead settings. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-003-004-tr — Overhead Set\|Refer to Procedure 003-004 in Section 3.]] | Overhead settings within the reset limits? **YES** | 9C |
| Overhead settings within the reset limits? **NORepair:** Adjust the overhead settings. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-003-004-tr — Overhead Set\|Refer to Procedure 003-004 in Section 3.]] | Repair complete |  |

#### STEP 9C. Verify engine brake adjustment.

| **Conditions:** Turn keyswitch OFF. Remove valve cover. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the engine brakes are operating correctly. Measure the engine brake settings. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 020-004 in Section 20. | Engine brake settings within the reset limits? **YES** | 9D |
| Engine brake settings within the reset limits? **NORepair:** Adjust the engine brake settings. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-020-004 — Engine Brake Assembly\|Refer to Procedure 020-004 in Section 20.]] | Repair complete |  |

#### STEP 9D. Verify crankshaft tone wheel is not loose.

| **Conditions:** Unplug the crankshaft position sensor. Operate the engine at idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Operate the engine with the crankshaft position sensor unplugged and identify if idle quality improves. If idle quality improves, remove the oil pan and inspect the crankshaft tone wheel to see if it is loose. | Crankshaft tone wheel loose? **YESRepair:** Repair the tone wheel. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 001-069 in Section 1. | Repair complete |
| Crankshaft tone wheel loose? **NO** | 9E |  |

#### STEP 9E. Check exhaust restriction.

| **Conditions:** Install a pressure gauge into the exhaust system. Turn keyswitch ON. Run engine at advertised horsepower and rpm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check exhaust restriction. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[101-011-009-tr — Exhaust Restriction\|Refer to Procedure 011-009 in Section 11.]] | Exhaust restriction greater than specification? **YESRepair:** Repair or replace the identified exhaust system component. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[101-011-009-tr — Exhaust Restriction\|Refer to Procedure 011-009 in Section 11]]. Refer to the OEM service manual. | Repair complete |
| Exhaust restriction greater than specification? **NO** | 9F |  |

#### STEP 9F. Verify engine blowby is within specification.

| **Conditions:** Turn keyswitch OFF. Connect the appropriate orifice to the end of the blowby draft tube. Start engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Load engine to rated rpm on a chassis dynamometer. Measure the engine blowby. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[101-014-010-tr — Crankcase Blowby, Measure\|Refer to Procedure 014-010 in Section 14.]] | Engine blowby measurements within specification? **YES** | Perform the next troubleshooting procedure as outlined in Step 2 |
| Engine blowby measurements within specification? **NORepair:** Engine may need to be rebuilt. See the engine specifications. | Repair complete |  |

### STEP 10. Aftertreatment checks.

#### STEP 10A. Check for aftertreatment-related fault codes.

| **Conditions:** Turn keyswitch OFF. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to read the fault codes. Check for any aftertreatment fault codes, specifically fault codes related to high soot in the aftertreatment particulate trap, face plugging of the aftertreatment catalyst, and aftertreatment catalyst efficiency. | Fault codes related to the aftertreatment system found to be active? **YES** | Appropriate fault code troubleshooting tree |
| Fault codes related to the aftertreatment system found to be active? **NO** | 10B |  |

#### STEP 10B. Perform basic aftertreatment troubleshooting checks.

| **Conditions:** - |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| The following items must be checked or verified before continuing: Check to make sure that Ultra Low Sulfur Diesel fuel is being used in the vehicle. Check for any fuel leaks around the aftertreatment fuel shutoff valve or aftertreatment injector components. Check for any noticeable exhaust leaks around any aftertreatment components. Check the exhaust pipes for restrictions that can create high exhaust back pressure. Check the aftertreatment sensors, wires, connectors, and harnesses for proper connections. Check the exhaust gas filter differential pressure sensor tubes for proper connections. | All parts inspected and appear to be functioning properly? **YES** | 10C |
| All parts inspected and appear to be functioning properly? **NORepair:** Correct the damage and verify the complaint is no longer present after repair. | Repair complete |  |

#### STEP 10C. Check for signs of internal damage to the aftertreatment system.

| **Conditions:** Operate engine to normal operating temperature. Be sure the vehicle is stationary. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Quickly snap the throttle pedal accelerating the engine from low idle to high idle while checking for smoke at the exhaust outlet. Inspect for the following during the Snap Throttle Acceleration Test. Smoke (any color) coming out of the vehicle tailpipe. Soot or signs of fuel, coolant, or oil inside the tailpipe. If the aftertreatment system is operating correctly, no visible smoke will be present during snap throttle acceleration. Any visible smoke is an indication of a possible malfunction in the aftertreatment system. | Visible smoke (black or white) present during the Snap Throttle Acceleration Test? **YESRepair:** Damage in the aftertreatment system. Remove the exhaust gas aftertreatment system from the vehicle and inspect for reuse. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[101-011-050-tr — Aftertreatment System\|Refer to Procedure 011-050 in Section 11.]] | Repair complete. Troubleshoot the smoke complaint, use the proper TT tree steps |
| Visible smoke (black or white) present during the Snap Throttle Acceleration Test? **NO** | 10D |  |

#### STEP 10D. Check exhaust restriction.

| **Conditions:** Install a pressure gauge into the exhaust system. Turn keyswitch ON. Operate engine at advertised horsepower and rpm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check exhaust restriction by installing a pressure gauge into the exhaust system just past the turbocharger outlet. If a port is **not** found in the exhaust system, remove the exhaust gas temperature 1 sensor and install the pressure gauge in the temperature sensor port. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[101-011-009-tr — Exhaust Restriction\|Refer to Procedure 011-009 in Section 11.]] | Exhaust restriction greater than 305 mm-Hg \[12.0 in-Hg\]? **YESRepair:** Remove the exhaust aftertreatment system from the vehicle and inspect for reuse. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[101-011-049-tr — Aftertreatment Diesel Oxidation Catalyst\|Refer to Procedure 011-049 in Section 11.]] | Repair complete |
| Exhaust restriction greater than 305 mm-Hg \[12.0 in-Hg\]? **NO** | Perform the next troubleshooting procedure as outlined in Step 2 |  |
