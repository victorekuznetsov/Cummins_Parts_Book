---
type: "Процедура"
doc: "16-t02-1001b"
title_en: "Engine Performance Troubleshooting Tree - ISM with CM876"
modified: "2015-04-23"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/16/16-t02-1001b.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/16-t02-1001b.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/16"
---

# Engine Performance Troubleshooting Tree - ISM with CM876

> [!abstract] Процедура · `16-t02-1001b`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format) · Section TT - Troubleshooting Symptoms (New Format) - Group TT · Sectopm TT - Troubleshooting Symptoms - Group TT
> **Даты:** изменён 2015-04-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/16/16-t02-1001b.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/16-t02-1001b.pdf)

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

- Engine Will **Not** Reach Rated Speed (RPM)

### How To Use This Tree

This symptom tree can be used to troubleshoot all performance based symptoms listed above. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform depending on the symptom.

### Shoptalk

Verify the engine control module (ECM) calibration is correct. Check the calibration revision history found on QuickServe™ Online for applicable fixes to the calibration stored in the ECM. If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Perform basic troubleshooting procedures. |  |
|  | **STEP 1A.** Check for active fault codes or high counts of inactive fault codes. | Active fault codes or high counts of inactive fault codes? |
|  | **STEP 1B.** Perform basic troubleshooting checks. | All steps have been verified to be correct? |
|  | **STEP 1C.** Perform INSITE™ electronic service tool Monitor Test. | 'Engine Operating State' reading a value that can cause an engine derate? |
| STEP 2. | Determination of engine symptom. |  |
|  | **STEP 2A.** Low power, poor acceleration, or poor response. | Engine symptom low power, poor acceleration, or poor response? |
|  | **STEP 2B.** Engine runs rough or misfires. | Engine symptom Engine Runs Rough or Misfires? |
|  | **STEP 2C.** Excessive black smoke. | Engine symptom Excessive Black Smoke? |
|  | **STEP 2D.** Excessive white smoke. | Engine symptom Excessive White Smoke and the engine is using coolant? |
|  | **STEP 2D-1.** Excessive white smoke. | Engine symptom Excessive White Smoke and the engine is not using coolant? |
|  | **STEP 2E.** Engine speed surge or engine speed unstable. | Engine symptom Engine Speed Surge or Engine Speed Unstable? |
|  | **STEP 2F.** Engine will not start or difficult to start, engine shuts off unexpectedly. | Symptom Engine Difficult to Start or Will Not Start, or Engine Shuts Off Unexpectedly? |
|  | **STEP 2G.** Engine run on, or will not shut down. | Engine symptom Engine Run On or Slow to Shut Down after operated at high idle for 1 minute then keyed OFF? |
| STEP 3. | No-start troubleshooting procedures. |  |
|  | **STEP 3A.** Check fuel shutoff valve voltage. | Fuel shutoff valve voltage greater than 11-VDC? |
|  | **STEP 3A-1.** Check ECM keyswitch voltage. | Keyswitch voltage equal to battery voltage? |
|  | **STEP 3A-2.** Check the fuel shutoff valve wire. | Less than 10 ohms? |
|  | **STEP 3B.** Check fuel shutoff valve resistance. | Fuel shutoff solenoid resistance 1 to 5 ohms for 6-VDC solenoids, 6 to 15 ohms for 12-VDC solenoids, 24 to 50 ohms for 24-VDC solenoids, 42 to 80 ohms for 32-VDC solenoids, 46 to 87 ohms for 36-VDC solenoids, 92 to 145 ohms for 48-VDC solenoids, 315 to 375 ohms for 74-VDC solenoids, 645 to 735 ohms for 115-VAC solenoids? |
|  | **STEP 3C.** Check fuel shutoff valve actuator disk. | Debris or damage found on the valve disc, valve seat, or actuator disc? |
|  | **STEP 3D.** Check for an engine equipped with a priming pump. | Engine uses a priming pump? |
|  | **STEP 3D-1.** Check for correct priming pump operation. | Priming pump operates after turning keyswitch ON? |
|  | **STEP 3D-2.** Check priming pump pressure. | Pump pressure meets the 69 kPa \[10 psi\] specification? |
|  | **STEP 3E.** Check for coolant in the exhaust gas recirculation (EGR) transfer tube. | Coolant present in the crossover tube? |
| STEP 4. | Fuel system checks. |  |
|  | **STEP 4A.** Check for air in the fuel. | Air bubbles visible in the sight glass? |
|  | **STEP 4B.** Check fuel inlet restriction. | Fuel inlet restriction less than the specifications? |
|  | **STEP 4C.** Check drain line restriction. | Fuel drain line restriction less than 89 mm-Hg \[3.5 in-Hg\]? |
|  | **STEP 4D.** Check fuel pump output pressure. | Fuel pressure meets the specification? |
|  | **STEP 4E.** Check fuel gear pump check valve. | Check valve installed and operating correctly? |
|  | **STEP 4F.** Check fuel supply line for restrictions. | Fuel lines free from restrictions? |
|  | **STEP 4G.** Check for plugged fuel drillings in the cylinder head. | Plastic insert removed from the fuel supply passage in the cylinder head? |
| STEP 5. | Injector diagnostics. |  |
|  | **STEP 5A.** Perform INSITE™ electronic service tool cylinder cutout test. | All cylinders pass the cylinder cutout test? |
| STEP 6. | Air handling diagnostic checks. |  |
|  | **STEP 6A.** Start engine and read fault codes. | Active fault codes? |
|  | **STEP 6B.** Check air intake restriction. | Air intake restriction greater than specification? |
|  | **STEP 6C.** Inspect the charge air cooler. | Problems found with the charge air cooler? |
|  | **STEP 6D.** Inspect the turbocharger blades for damage. | Damage found on turbocharger fins? |
|  | **STEP 6E.** Inspect the turbocharger shaft movement. | Nozzle slides evenly from stop to stop and gear teeth undamaged? |
| STEP 7. | Check EGR system for proper operation. |  |
|  | **STEP 7A.** Check for EGR related fault codes. | EGR related fault codes present? |
|  | **STEP 7B.** Check for inactive EGR differential pressure sensor fault codes. | Fault Code 1866, 2273, or 2274 active? |
|  | **STEP 7C.** Check the EGR differential pressure tubes for leaks. | Leaks detected at either the low or high EGR differential pressure tubes? |
|  | **STEP 7D.** Check the EGR differential pressure sensor adapter for leaks. | Leaks detected at the EGR differential pressure sensor adapter? |
|  | **STEP 7E.** Check the EGR differential pressure tubes for plugging. | Debris or soot found in either EGR differential pressure tube? |
|  | **STEP 7F.** Check for air leaks in the EGR system. | Air leaks found in the EGR connection tubing? |
| STEP 8. | Verify electronic features are operating correctly. |  |
|  | **STEP 8A.** Verify accelerator pedal travel. | Percent Accelerator read 0 when the accelerator is released and 100 percent when the accelerator is depressed? |
|  | **STEP 8B.** Monitor vehicle speed. | Does the vehicle speed read 0 when the vehicle is not moving? |
|  | **STEP 8C.** Verify electronic feature settings are correct. | Electronic features set correctly? |
|  | **STEP 8D.** Check ambient air pressure sensor reading. | Barometric pressure sensor reading in INSITE™ electronic service tool within 5 percent of the present local barometric pressure reading? |
|  | **STEP 8E.** Check the intake manifold pressure sensor accuracy. | INSITE™ electronic service tool reading within 17 kPa \[2.5 psi\] of mechanical gauge reading? |
| STEP 9. | Perform base engine mechanical checks. |  |
|  | **STEP 9A.** Verify overhead adjustments are correct. | Overhead settings within the reset limits? |
|  | **STEP 9B.** Verify engine brake adjustment. | Engine brake settings within the reset limits? |
|  | **STEP 9C.** Check air intake restriction. | Air intake restriction greater than 635 mm-H 2 0 \[25 in-H 2 0\] for a used air filter or 254 mm-H 2 0 \[10 in-H 2 0); for a new filter? |
|  | **STEP 9D.** Check exhaust restriction. | Exhaust restriction greater than 304.8 mm-Hg \[12.0 in-Hg\]? |
|  | **STEP 9E.** Inspect the charge-air cooler. | Pressure drop 34 kPa \[5 psi\] or less in 15 seconds? |
|  | **STEP 9F.** Verify engine blowby is within specification. | Engine blowby measurements within specification? |
|  | **STEP 9F-1.** Verify turbocharger contribution to engine blowby. | Total engine blowby drop more than 30 percent? |
| STEP 10. | Aftertreatment Checks |  |
|  | **STEP 10A.** Check for aftertreatment related fault codes. | Fault codes related to the aftertreatment system are found to be active? |
|  | **STEP 10B.** Perform basic aftertreatment troubleshooting checks. | All parts have been visually inspected, and appear to be functioning properly? |
|  | **STEP 10C.** Check for signs of internal damage to the aftertreatment system. | Visible smoke (black or white) is present during the snap throttle acceleration? |
|  | **STEP 10D.** Check exhaust restriction. | Exhaust restriction greater than 304.8 mm-Hg \[12.0 in-Hg\]? |

### STEP 1. Perform basic troubleshooting procedures.

#### STEP 1A. Check for active fault codes or high counts of inactive fault codes.

| **Conditions:** Connect INSITE™ electronic service tool Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes. Use INSITE™ electronic service tool to read the fault codes. | Active fault codes or high counts of inactive fault codes? **YES** | Go to appropriate fault code troubleshooting tree |
| Active fault codes or high counts of inactive fault codes? **NO** | 1B |  |

#### STEP 1B. Perform basic troubleshooting checks.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| The following items must be checked or verified before continuing: Verify the fuel level in the tanks Verify there have not been any changes to CPL components on the engine Verify fuel grade is correct for the application Verify the engine is operating within the recommended altitude Verify engine oil is at the correct level Verify engine parasitics have not changed Verify engine duty cycle has not changed Verify engine cranking speed is greater than 150 rpm. Verify battery voltage is adequate | All steps have been verified to be correct? **YES** | 1C |
| All steps have been verified to be correct? **NORepair:** Correct the condition and verify complaint is no longer present after repair. | Repair complete |  |

#### STEP 1C. Perform INSITE™ electronic service tool Monitor Test.

| **Conditions:** Correct INSITE™ electronic service tool Engine operating at the speed and load where the symptom occurs. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to monitor the parameter 'Engine Operating State' at the same engine operating conditions where the symptom occurs. Advanced Engine Performance Troubleshooting Techniques. [[4021686 — Advanced Engine Performance Troubleshooting Techniques\|4021686]], for a description of what "User Fueling States" or "Engine Operating State" can cause engine derates. | 'Engine Operating State' reading a value that can cause an engine derate? **YESRepair:** Determine if the engine derate is being caused by normal engine operation or by actual engine damage. Continue following troubleshooting steps as outlined in step 2 if engine damage is suspected. | 2A |
| 'Engine Operating State' reading a value that can cause an engine derate? **NO** | 2A |  |

### STEP 2. Determination of engine symptom.

#### STEP 2A. Low power, poor acceleration, or poor response.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. N/A | Engine symptom low power, poor acceleration, or poor response? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 6 - Air Handling Checks With EGR - Step 7 - EGR Checks Step 8 - Electronic Checks Step 5 - Injector Checks Step 9 - Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom low power, poor acceleration, or poor response? **NO** | 2B |  |

#### STEP 2B. Engine runs rough or misfires.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. N/A | Engine symptom Engine Runs Rough or Misfires? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 5 - Injector Checks Step 4 - Fuel System Checks Step 9 - Base Engine Checks Step 7 - EGR Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom Engine Runs Rough or Misfires? **NO** | 2C |  |

#### STEP 2C. Excessive black smoke.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. Progressive damage to the aftertreatment system has occurred if black smoke is visible. Remove the exhaust aftertreatment system from the vehicle and inspect for reuse. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[101-011-050-tr — Aftertreatment System\|Refer to Procedure 011-050 in Section 11.]] | Engine symptom Excessive Black Smoke? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 6 - Air Handling Checks Step 4 - Fuel System Checks Step 7 - EGR Checks Step 9 - Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom Excessive Black Smoke? **NO** | 2D |  |

#### STEP 2D. Excessive white smoke.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. N/A | Engine symptom Excessive White Smoke and the engine is using coolant? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: See the Coolant Loss - Internal symptom tree. | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom Excessive White Smoke and the engine is using coolant? **NO** | 2D-1 |  |

#### STEP 2D-1. Excessive white smoke.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. N/A | Engine symptom Excessive White Smoke and the engine is **not** using coolant? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 5 - Injector Checks Step 10 - Aftertreatment Checks Step 6 - Air Handling Checks Step 9 - Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom Excessive White Smoke and the engine is **not** using coolant? **NO** | 2E |  |

#### STEP 2E. Engine speed surge or engine speed unstable.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. N/A | Engine symptom Engine Speed Surge or Engine Speed Unstable? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 5 - Injector Checks Step 7 - EGR Checks Step 6 - Air Handling Checks Step 8- Electronics Checks Step 9 - Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Engine symptom Engine Speed Surge or Engine Speed Unstable? **NO** | 2F |  |

#### STEP 2F. Engine will not start or difficult to start, engine shuts off unexpectedly.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. N/A | Symptom Engine Will **Not** Start or Difficult to Start, Engine Shuts Off Unexpectedly? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 3 - No Start Checks Step 4 - Fuel System Checks Step 5 - Injector Checks Step 6 - Air Handling Checks Step 8 - Electronics Checks Step 9 - Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure |
| Symptom Engine Difficult to Start or Will **Not** Start, or Engine Shuts Off Unexpectedly? **NO** | 2G |  |

#### STEP 2G. Engine run on, or will not shut down

| **Conditions:** N/A |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. None | Engine symptom Engine Run On or Slow to Shut Down after operated at high idle for 1 minute then keyed OFF? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 5 - Injector Check Step 4 - Fuel System Checks Step 9 - Base Engine Checks | Perform the troubleshooting steps suggested in the repair procedure. |
| Engine symptom Engine Run On or Slow to Shut Down after operated at high idle for 1 minute then keyed Off? **NO** | Return to correct symptom trees. |  |

### STEP 3. No-start troubleshooting procedures.

#### STEP 3A. Check fuel shutoff valve voltage.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from the fuel shutoff valve post to engine block ground. N/A | Fuel shutoff valve voltage greater than 11-VDC? **YES** | 3B |
| Fuel shutoff valve voltage greater than 11-VDC? **NO** | 3A-1 |  |

#### STEP 3A-1. Check ECM Keyswitch Voltage

| **Conditions:** Turn keyswitch OFF Disconnect the original equipment manufacturer (OEM) harness from the ECM Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from the keyswitch input SIGNAL wire of the OEM harness to engine block ground. N/A | Keyswitch voltage equal to battery voltage? **YES** | 3A-2 |
| Keyswitch voltage equal to battery voltage? **NORepair:** Repair or replace the OEM power harness, keyswitch, or check the battery connections. Use the following procedure in the ISX CM871 and ISM CM876 Electronic Control Systems, Troubleshooting and Repair Manual, Bulletin 4021560. [[99-019-064 — Key Switch Power Supply Circuit\|Refer to Procedure 019-064 in Section 19.]] | Repair complete |  |

#### STEP 3A-2. Check the fuel shutoff valve wire.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the fuel shutoff valve wire from the valve terminal post. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the fuel shutoff valve SIGNAL pin in the ECM connector to the fuel shutoff valve eyelet. N/A | Less than 10 ohms? **YESRepair:** Replace the ECM. Use the following procedure in the ISX CM871 and ISM CM876 Electronic Control Systems, Troubleshooting and Repair Manual, Bulletin 4021560. Refer to Procedure 019-031 in Section 19. | 3B |
| Less than 10 ohms? **NORepair:** Repair or replace the engine harness. Use the following procedure in the ISX CM871 and ISM CM876 Electronic Control Systems, Troubleshooting and Repair Manual, Bulletin 4021560. Refer to Procedure 019-043 in Section 19. | Repair complete |  |

#### STEP 3B. Check fuel shutoff valve resistance

| **Conditions:** Turn keyswitch OFF Disconnect the fuel shutoff valve signal wire from the fuel shutoff solenoid Fuel shutoff valve temperature between 20 - 25°C \[68 - 77°F\]. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the fuel shutoff solenaoid post to engine block ground. The fuel shutoff solenoid must be between 20 - 25°C \[68 - 77°F\] before the use of the resistance specifications listed. | Fuel shutoff solenoid resistance: 1 to 5 ohms for 6-VDC solenoids 6 to 15 ohms for 12-VDC solenoids 24 to 50 ohms for 24-VDC solenoids 42 to 80 ohms for 32-VDC solenoids 46 to 87 ohms for 36-VDC solenoids 92 to 145 ohms for 48-VDC solenoids 315 to 375 ohms for 74-VDC solenoids 645 to 735 ohms for 115-VAC solenoids **YES** | 3C |
| Fuel shutoff solenoid resistance: 1 to 5 ohms for 6-VDC solenoids 6 to 15 ohms for 12-VDC solenoids 24 to 50 ohms for 24-VDC solenoids 42 to 80 ohms for 32-VDC solenoids 46 to 87 ohms for 36-VDC solenoids 92 to 145 ohms for 48-VDC solenoids 315 to 375 ohms for 74-VDC solenoids 645 to 735 ohms for 115-VAC solenoids **NORepair:** Replace the fuel shutoff solenoid. Use the following procedure in the ISX CM871 and ISM CM876 Electronic Control Systems, Troubleshooting and Repair Manual, Bulletin 4021560. Refer to Procedure 019-050 in Section 19. | 3C |  |

#### STEP 3C. Check fuel shutoff valve actuator disk

| **Conditions:** Turn keyswitch OFF Remove the fuel shutoff valve solenoid, valve disc, valve seat, and actuator disk. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the valve disc, valve seat, and actuator disc for dirt, metal parts, bonding separation, corrosion, cracks, or wear. N/A | Debris or damage found on the valve disc, valve seat, or actuator disc? **YESRepair:** Replace the damaged fuel shutoff valve component. Use the following procedure in the ISX CM871 and ISM CM876 Electronic Control Systems, Troubleshooting and Repair Manual, Bulletin 402156 Refer to Procedure 019-050 in Section 19. | Repair complete |
| Debris or damage found on the valve disc, valve seat, or actuator disc? **NO** | 3D |  |

#### STEP 3D. Check for an engine equipped with a priming pump.

| **Conditions:** Turn keyswitch OFF Assemble fuel shutoff valve components Turn keyswitch ON |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Listen for the lift pump operation. Listen for the priming pump operation after the keyswitch is turned to the ON position. If priming pump operation is **not** heard, inspect the unit to verify that is **not** equipped with a priming pump. **Not** all ISM engines use a priming pump and **not** all ISM engines use a priming pump that actuates at keyswitch ON. Understand which system is present on this engine before beginning this step. | Engine use a priming pump? **YES** | 3D-1 |
| Engine use a priming pump? **NO** | 4A |  |

#### STEP 3D-1. Check for correct priming pump operation.

| **Conditions:** Turn keyswitch OFF Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Listen for priming pump operation. Listen for the priming pump operation after the keyswitch is turned to the ON position. **Not** all ISM engines use a priming pump and **not** all ISM engines use a priming pump that actuates at keyswitch ON. Understand which system is present on this engine before beginning this step. | Priming pump operate after turning the keyswitch ON? **YES** | 3D-2 |
| Priming pump operate after turning the keyswitch ON? **NORepair:** Check the priming pump operation. Replace the priming pump as necessary. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-005-016-tr — Fuel Pump\|Refer to Procedure 005-016 in Section 5.]] | Repair complete |  |

#### STEP 3D-2. Check priming pump pressure.

| **Conditions:** Turn keyswitch OFF Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the pressure. Measure the priming pump pressure at the quick connect fitting located on the top of the fuel pump. | Pressure meet the 69 kPa \[10 psi\]? **YES** | 4A |
| Pressure meet the 69 kPa \[10 psi\]? **NORepair:** Replace the priming pump. ISM engines are **not** equipped with a lift pump from the factory. Reference the chassis manufacturer's repair procedure for priming pump replacement. | Repair complete |  |

#### STEP 3E. Check for coolant in the EGR transfer tube.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Remove the EGR transfer hose from the EGR cooler outlet. N/A | Coolant present in the crossover tube? **YESRepair:** See the Coolant Loss - Internal symptom tree. | Repair complete |
| Coolant present in the crossover tube? **NO** | Perform next troubleshooting procedure as outlined in Step 2 |  |

### STEP 4. Fuel system checks.

#### STEP 4A. Check for air in the fuel.

| **Conditions:** Engine operating at low idle (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect the equipment to the fuel pump as shown. N/A | Air bubbles visible in the sight glass? **YESRepair:** Locate and correct cause of air ingestion in OEM fuel supply system or damaged fuel filter sealing ring. Check the ECM cooling plate, associated plumbing, and o-ring seals for failures that can cause air ingestion. Repair or replace the malfunctioned component. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-006-006-tr — Engine Control Module Cooling Plate, Fuel Cooled\|Refer to Procedure 006-006 in Section 6.]] | Repair complete |
| Air bubbles visible in the sight glass? **NO** | 4B |  |

#### STEP 4B. Check fuel inlet restriction.

| **Conditions:** Connect a manometer, Part Number ST-1111-3, to the fuel pump supply hose. Turn keyswitch ON. Engine operating at rated speed (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel inlet restriction. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-006-020-tr — Fuel Inlet Restriction\|Refer to Procedure 006-020 in Section 6.]] | Fuel inlet restriction less than the specifications listed below? Dirty - 254 mm-Hg \[10 in-Hg\]; New - 152 mm-Hg \[6 in-Hg\] **YES** | 4C |
| Fuel inlet restriction less than the specifications listed below? Dirty - 254 mm-Hg \[10 in-Hg\]; New - 152 mm-Hg \[6 in-Hg\] **NORepair:** Locate the cause of high fuel inlet restriction. Check the prefilter and fuel supply lines. | Repair complete |  |

#### STEP 4C. Check drain line restriction.

| **Conditions:** Connect a manometer, Part Number ST-1111-3, to the fuel drain line. Turn keyswitch ON. Engine operating at rated speed (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Observe the reading on the pressure gauge. N/A | Fuel drain line restriction less than 89 mm-Hg \[3.5 in-Hg\]? **YES** | 4D |
| Fuel drain line restriction less than 89 mm-Hg \[3.5 in-Hg\]? **NORepair:** Locate cause of high fuel drain line restriction in OEM fuel return line. | Repair complete |  |

#### STEP 4D. Check fuel pump output pressure.

| **Conditions:** Connect pressure gauge on the Compuchek™ fitting of the fuel pump. Turn keyswitch ON. Engine operating at 1200 rpm (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Observe the reading on the pressure gauge. Use the following procedure in the ISM, ISMe, and QSM11 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-005-011-tr — Fuel Flow\|Refer to Procedure 005-011 in Section 5.]] Engine cranking at minimum of 150 rpm for 10 seconds: minimum of 172 kPa \[25 psi\]. Engine operating at 1200 rpm: minimum of 827 kPa \[120 psi\]. | Fuel pressure meet the specification? **YES** | 4F |
| Fuel pressure meet the specification? **NO** | 4E |  |

#### STEP 4E. Check fuel gear pump check valve.

| **Conditions:** Disconnect fuel drain line from fuel gear pump housing. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel gear pump check valve for correct installation and operation. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-005-026 — Fuel Pump Gear Pump Check Valve\|Refer to Procedure 005-026 in Section 5.]] | Check valve installed and operating correctly? **YESRepair:** Replace the fuel pump. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-005-016-tr — Fuel Pump\|Refer to Procedure 005-016 in Section 5.]] | Repair complete |
| Check valve installed and operating correctly? **NORepair:** Install the check valve correctly or replace the fuel gear pump check valve, if necessary. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-005-026 — Fuel Pump Gear Pump Check Valve\|Refer to Procedure 005-026 in Section 5.]] | Repair complete |  |

#### STEP 4F. Check fuel supply line for restrictions.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel line between the fuel pump and cylinder head for obstructions. Check the fuel line for sharp bends or kinks that could cause a restriction. N/A | Fuel lines free from restrictions? **YES** | 4G |
| Fuel lines free from restrictions? **NORepair:** Remove obstructions from fuel lines. Replace kinked or restricted lines as necessary. | Repair complete |  |

#### STEP 4G. Check for plugged fuel drillings in the cylinder head.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| If a ReCon® cylinder head was installed, check that the plastic insert has been removed from the fuel supply inlet passage in the cylinder head. N/A | Plastic insert been removed from the fuel supply passage in the cylinder head? **YES** | Perform the next troubleshooting procedure as outlined in Step 2 |
| Plastic insert been removed from the fuel supply passage in the cylinder head? **NORepair:** Remove the plastic insert from the fuel supply passage in the cylinder head. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-002-004-tr — Cylinder Head\|Refer to Procedure 002-004 in Section 2.]] | Repair complete |  |

### STEP 5. Injector diagnostics.

#### STEP 5A. Perform INSITE™ electronic service tool Cylinder Cutout test.

| **Conditions:** Connect INSITE™ electronic service tool. Operate engine at low idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform INSITE™ electronic service tool cylinder cutout test. N/A | All cylinders pass the cylinder cutout test? **YES** | Perform next troubleshooting procedure as outlined in Step 2 |
| All cylinders pass the Cylinder Cutout test? **NORepair:** Replace the injectors as needed. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] | Repair complete |  |

### STEP 6. Air handling diagnostic checks.

#### STEP 6A. Start engine and read fault codes.

| **Conditions:** Connect INSITE™ electronic service tool. Operate engine at low idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fault codes with the engine operating. Use INSITE™ electronic service tool to read the fault codes. | Active fault codes? **YES** | Appropriate fault code troubleshooting tree |
| Active fault codes? **NO** | 6B |  |

#### STEP 6B. Check air intake restriction.

| **Conditions:** N/A |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the air intake restriction. [[35-010-031-tr — Air Intake Restriction\|Refer to Procedure 010-031 in Section 10.]] | Air intake restriction greater than the specification? **YESRepair:** Correct the cause of high intake air restriction. Check for a plugged air filter or restricted air intake piping. Refer to the OEM service manual. | Repair complete. |
| Air intake restriction greater than the specification? **NO** | 6C |  |

#### STEP 6C. Inspect the charge-air cooler.

| **Conditions:** Turn engine OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the charge-air cooler for cleanliness, cracks, holes, or other damage. [[35-010-027-tr — Charge-Air Cooler\|Refer to Procedure 010-027 in Section 10.]] The pressure test and the temperature differential test can be used to verify charge-air cooler problems. | Problems found with the charge-air cooler? **YESRepair:** Repair or replace the charge-air cooler assembly. Refer to Procedure 010-027 in Section 10. | Repair complete |
| Problems found with the charge-air cooler? **NO** | 6D |  |

#### STEP 6D. Inspect the turbocharger blades for damage.

| **Conditions:** Turn engine OFF. Remove intake and exhaust connections for turbocharger. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the compressor and turbine fins for damage or wear. N/A | Damage found on turbocharger fins? **YESRepair:** Replace the turbocharger. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | Repair complete. |
| Damage found on turbocharger fins? **NO** | 6E |  |

#### STEP 6E. Inspect the turbocharger shaft movement.

| **Conditions:** Turn keyswitch OFF. Remove the variable geometry turbocharger (VGT) actuator from the turbocharger. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sector gear on the turbocharger for damaged or broken gear teeth. Move the sector gear lever on the turbocharger bearing housing up and down from stop to stop. Check for smooth movement between the stops. There will be an initial friction force that must be overcome before the actuator lever will move. Once movement is started, the actuator lever should move to the other stop position by hand. Use the following procedure in the ISM, ISMe, and QSM11 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 010-134 in Section 10. | Nozzle slides easily from stop to stop and gear teeth undamaged? **YESRepair:** Install the turbocharger actuator. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-010-134 — Variable Geometry Turbocharger Actuator, Electric\|Refer to Procedure 010-134 in Section 10.]] | Perform the next troubleshooting procedure as outlined in Step 2. |
| Nozzle slides easily from stop to stop and gear teeth undamaged? **NORepair:** A turbocharger mechanical malfunction has been detected. Inspect the turbocharger for repair and reuse, if possible. Use the following procedure in the ISM, ISMe, and QSM11 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | Repair complete. |  |

### STEP 7. Check EGR system for proper operation.

#### STEP 7A. Check for EGR related fault codes.

| **Conditions:** Turn keyswitch OFF. Wait 30 seconds Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for any EGR related fault codes. N/A | EGR related fault codes present? **YESRepair:** Troubleshoot electronic fault codes. | Appropriate fault code troubleshooting trees |
| EGR related fault codes present? **NO** | 7B |  |

#### STEP 7B. Check for inactive EGR differential pressure sensor fault codes.

| **Conditions:** Turn keyswitch ON. Connect the INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes. Use INSITE™ electronic service tool to read the fault codes | Fault Code 1866, 2273, or 2274 active? **YES** | Appropriate fault code troubleshooting tree. |
| Fault Code 1866, 2273, or 2274 active? **NO** | 7C |  |

#### STEP 7C. Check the EGR differential pressure tubes for leaks.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the lines for leaks. Leaks will be easily noticed by traces of soot. | Leaks detected at either the low or high EGR differential pressure tubes? **YESRepair:** Tighten the fittings, or replace the EGR differential pressure tube. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-011-026-tr — EGR Differential Pressure Sensor Tubes\|Refer to Procedure 011-026 in Section 11.]] | Repair complete |
| Leaks detected at either the low or high EGR differential pressure tubes? **NO** | 7D |  |

#### STEP 7D. Check the EGR differential pressure sensor adapter for leaks.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the EGR differential pressure sensor adaptor for leaks. Leaks will be easily noticed by traces of soot; however, the sensor can be removed to inspect the o-rings between the EGR differential pressure sensor and the adapter for proper sealing. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 011-028 in Section 11. | Leaks detected at the EGR differential pressure sensor adapter? **YESRepair:** Replace the EGR differential pressure sensor adapter. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-011-028-tr — EGR Differential Pressure Sensor Adapter\|Refer to Procedure 011-028 in Section 11.]] | Repair complete |
| Leaks detected at the EGR differential pressure sensor adapter? **NO** | 7E |  |

#### STEP 7E. Check the EGR differential pressure tubes for plugging.

| **Conditions:** Turn keyswitch OFF. Remove the EGR differential pressure tubes. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 011-026 in Section 11. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the EGR differential pressure tubes for restrictions, soot plugging and plugging. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 011-026 in Section 11. | Debris or soot found in either EGR differential pressure tube? **YESRepair:** Clear the debris or replace the EGR differential pressure tube. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-011-026-tr — EGR Differential Pressure Sensor Tubes\|Refer to Procedure 011-026 in Section 11.]] | Repair complete |
| Debris or soot found in either EGR differential pressure tube? **NO** | 7F |  |

#### STEP 7F. Check for air leaks in the EGR system.

| **Conditions:** N/A |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for leaks in the EGR connection tubing and connections. Soot streaks are noticeable where leaks are present. | Air leaks found in the EGR connection tubing? **YESRepair:** Repair any leaks in the EGR system. | Repair complete |
| Air leaks found in the EGR connection tubing? **NO** | Perform next troubleshooting procedure as outlined in Step 2 |  |

### STEP 8. Verify electronic features are operating correctly.

#### STEP 8A. Verify accelerator pedal travel.

| **Conditions:** Turn keyswitch ON. Connect the INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to monitor Percent Accelerator while fully depressing and releasing the accelerator pedal. N/A | Percent Accelerator read 0 when the accelerator is released and 100 percent when the accelerator is depressed? **YES** | 8B |
| Throttle Position read 0 when the accelerator is released and 100 percent when the accelerator is depressed? **NORepair:** Determine and correct cause of accelerator pedal restriction. | Repair complete |  |

#### STEP 8B. Monitor vehicle speed.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. Start the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to monitor Vehicle Speed while the vehicle is not moving. N/A | Vehicle speed read 0 when the vehicle is **not** moving? **YES** | 8C |
| Vehicle speed read 0 when the vehicle is **not** moving? **NORepair:** Check the vehicle speed sensor and circuit or locate the cause of the vehicle speed interference. | Repair complete |  |

#### STEP 8C. Verify electronic feature settings are correct.

| **Conditions:** Turn keyswitch ON. Connect the INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to verify the following adjustable parameters are correctly set: Maximum vehicle speed Powertrain protection Rear axle ratio Number of transmission tailshaft gear teeth Tire revolutions per mile Gear-down protection Cruise control droop settings Cruise control maximum vehicle speed. | Electronic features set correctly? **YES** | 8D |
| Electronic features set correctly? **NORepair:** Correct programmable features. | Repair complete |  |

#### STEP 8D. Check ambient air pressure sensor accuracy

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for correct barometric pressure reading. Compare the barometric pressure sensor reading on INSITE™ electronic service tool data monitor/logger to the current local barometric pressure. | Barometric pressure sensor reading in the INSITE™ electronic service tool within 5 percent of the present local barometric pressure reading? **YES** | 8E |
| Barometric pressure sensor reading in INSITE™ electronic service tool within 5 percent of the present local barometric pressure reading? **NORepair:** Replace the ambient air pressure sensor. Use the following procedure in the ISX CM871 and ISM CM876 Electronic Control Systems, Troubleshooting and Repair Manual, Bulletin 4021560. Refer to Procedure 019-004 in Section 19. | Repair complete |  |

#### STEP 8E. Check the intake manifold pressure sensor accuracy.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. Start and operate the engine at high idle after connecting the mechanical intake manifold pressure gauge. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect a mechanical intake manifold pressure gauge to the engine, as close to the intake manifold pressure sensor as possible. Start INSITE™ electronic service tool Data Monitor/Logger and compare INSITE™ electronic service tool reading for intake manifold pressure to the mechanical gauge. | INSITE™ electronic service tool reading within 17 kPa \[2.5 psi\] of mechanical gauge reading? **YES** | Perform the next troubleshooting procedure as outlined in Step 2 |
| INSITE™ electronic service tool reading within 17 kPa \[2.5 psi\] of mechanical gauge reading? **NORepair:** Remove and clean the intake manifold pressure sensor. Use the following procedure found in the ISX CM871 and ISM CM876 Electronic Control System, Bulletin 4021560. Refer to Procedure 019-159 in Section 19. | Repair complete |  |

### STEP 9. Perform base engine mechanical checks.

#### STEP 9A. Verify overhead adjustments are correct.

| **Conditions:** Turn keyswitch OFF. Remove valve cover. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the overhead settings. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 003-004 in Section 3. | Overhead settings within the reset limits? **YES** | 9B |
| Overhead settings within the reset limits? **NORepair:** Adjust the overhead settings. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-003-004-tr — Overhead Set\|Refer to Procedure 003-004 in Section 3.]] | Repair complete |  |

#### STEP 9B. Verify engine brake adjustment.

| **Conditions:** Turn keyswitch OFF. Remove rocker lever cover. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the engine brakes are operating correctly. Measure the engine brake settings. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 020-024 in Section 20. | Engine brake settings within the reset limits? **YES** | 9C |
| Engine brake settings within the reset limits? **NORepair:** Adjust the engine brakes settings. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-020-024-tr — Engine Brake\|Refer to Procedure 020-024 in Section 20.]] | Repair complete |  |

#### STEP 9C. Check air intake restriction.

| **Conditions:** Turn keyswitch ON Operate the engine at advertised horsepower and rpm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the intake system restriction by installintg a vacuum gauge or water manometer into the air intake system. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-010-031-tr — Air Intake Restriction\|Refer to Procedure 010-031 in Section 10.]] | Air intake restriction greater than 635 mm-H 2 0 \[25 in-H 2 O\] for a used air filter or 254 mm-H 2 O \[10 in-H 2 O\] for a new filter? **YESRepair:** Correct the cause of high intake air restriction. Check for plugged air filter or restricted air intake piping. | Repair compete |
| Air intake restriction greater than 635 mm-H 2 0 \[25 in-H 2 O\] for a used air filter or 254 mm-H 2 O \[10 in-H 2 O\] for a new filter? **NO** | 9D |  |

#### STEP 9D. Check exhaust restriction.

| **Conditions:** Install a pressure gauge into the exhaust system Turn keyswitch ON Operate the engine at advertised horsepower and rpm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check exhaust restriction. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[101-011-009-tr — Exhaust Restriction\|Refer to Procedure 011-009 in Section 11.]] | Exhaust restriction greater than specification? **YESRepair:** Repair or replace the identified exhaust system component. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[101-011-009-tr — Exhaust Restriction\|Refer to Procedure 011-009 in Section 11.]] Refer to the OEM service manual. | Repair complete |
| Exhaust restriction greater than specification? **NO** | 9F |  |

#### STEP 9E. Inspect charge-air cooler

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Pressure test the charge-air cooler. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-010-027-tr — Charge-Air Cooler\|Refer to Procedure 010-027 in Section 1.]] | Pressure drop 34 kPa \[5 psi\] or less in 15 seconds? **YES** | 9F |
| Pressure drop 34 kPa \[5 psi\] or less in 15 seconds? **NORepair:** Repair or replace the charge air cooler assembly. | Repair complete |  |

#### STEP 9F. Verify engine blowby is within specification.

| **Conditions:** Turn keyswitch OFF. Connect the appropriate orifice to the end of the blowby draft tube Start engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Load engine to rated rpm on a chassis dynamometer. Measure the engine blowby Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 014-002 in Section 14. | Engine blowby measurements within specification? **YES** | Perform the next troubleshooting procedure as outlined in Step 2 |
| Engine blowby measurements within specification? **NO** | 9F-1 |  |

#### STEP 9F-1. Verify turbocharger contribution to engine blowby.

| **Conditions:** Turn keyswitch OFF Verify oil level is full Connect the appropriate orifice to the end of the blowby draft tube Remove the turbocharger oil drain line form the block and drain into a bucket Make sure the turbocharger oil drain port in the block is plugged so no crankcase gases escape Start engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Load engine to rated rpm on a chassis dynamometer Measure the engine blowby Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 014-002 in Section 14. | Total engine blowby drop more than 30 percent? **YESRepair:** Replace the turbocharger assembly. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | Repair complete |
| Total engine blowby drop more than 30 percent? **NORepair:** Engine rebuild is possible. See the engine rebuild specifications. | Repair complete |  |

### STEP 10. Aftertreatment Checks

#### STEP 10A. Check for aftertreatment related fault codes.

| **Conditions:** Turn keyswitch ON Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to read the fault codes. Check for any aftertreatment fault codes. Specifically fault codes related to high soot in the aftertreatment diesel particulate filter, face plugging of the aftertreatment diesel oxidation catalyst, and aftertreatment diesel oxidation catalyst efficiency. | Fault codes related to the aftertreatment system are found to be active? **YES** | Appropriate fault code troubleshooting tree |
| Fault codes related to the aftertreatment system are found to be active? **NORepair:** Correct the malfunction and verify complaint is no longer present after repair. | 10B |  |

#### STEP 10B. Perform basic aftertreatment troubleshooting checks

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| The following items must be checked or verified before continuing: Check to make sure that Ultra Low Sulfur Diesel (ULSD) fuel is being used in the vehicle. Check for any fuel leaks around the aftertreatment fuel shutoff valve or aftertreatment injector components. Check for any noticeable exhaust leaks around any aftertreatment components. Check the exhaust pipes for restrictions that can create high exhaust back pressure. Check the aftertreatment sensors, wires, connectors, and harnesses for proper connections. Check the exhaust gas filter differential pressure sensor tubes for proper connections. | All parts have been inspected, and appear to be functioning properly? **YES** | 10C |
| All parts have been inspected, and appear to be functioning properly? **NORepair:** Correct the malfunction and verify complaint is no longer present after repair. | Repair complete |  |

#### STEP 10C. Check for signs of internal damage to the aftertreatment system.

| **Conditions:** Engine warmed up to normal operating temperature Vehicle must be stationary. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Quickly snap the throttle pedal accelerating the engine from low idle to high idle while checking for smoke at the exhaust outlet. Inspect the following during the snap throttle acceleration: Smoke (any color) coming out of the vehicle tailpipe Soot or signs of fuel, coolant, or oil inside the tailpipe. If the aftertreatment system is operating correctly, no visible smoke will be present during the snap throttle acceleration. Any visible smoke is an indication of a possible malfunction in the aftertreatment system. | Any visible smoke (black or white) is present during the snap throttle acceleration? **YESRepair:** Any malfunction in the aftertreatment system: Remove the exhaust gas aftertreatment system form the vehicle and inspect for reuse. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[101-011-050-tr — Aftertreatment System\|Refer to Procedure 011-050 in Section 11.]] Inspect the aftertreatment system for a potential malfunction. | Repair complete, troubleshoot the smoke complaint, use the proper TT tree steps |
| Any visible smoke (black or white) is present during the snap throttle acceleration? **NO** | 10D |  |

#### STEP 10D. Check exhaust restriction.

| **Conditions:** Install a pressure gauge into the exhaust system Turn keyswitch ON Operate the engine at advertised horsepower and rpm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check exhaust restriction by installing a pressure gauge into the exhaust system just past the turbocharger outlet. If a port is not found in the exhaust system, remove the exhaust gas temperature 1 sensor and install the pressure gauge in the temperature sensor port. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[101-011-009-tr — Exhaust Restriction\|Refer to Procedure 011-009 in Section 11.]] | Exhaust restriction greater than 304.8 mm-Hg \[12.0 in-Hg\]? **YESRepair:** Remove the exhaust aftertreatment system from the vehicle and inspect for reuse. Use the following procedure in the ISM, ISMe, and QSM11 Engines, Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[101-011-050-tr — Aftertreatment System\|Refer to Procedure 011-050 in Section 11.]] Inspect the aftertreatment system for a potential malfunction. | Repair complete |
| Exhaust restriction greater than 304.8 mm-Hg \[12.0 in-Hg\]? **NO** | Perform the next troubleshooting procedure as outlined in Step 2. |  |
