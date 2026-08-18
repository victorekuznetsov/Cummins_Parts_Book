---
aliases:
  - "Дерево диагностики мощностных характеристик — система CM2150"
type: "Процедура"
doc: "123-t02-1001"
title_en: "Engine Performance Troubleshooting Tree - CM2150 Electronic Control System"
title_ru: "Дерево диагностики мощностных характеристик — система CM2150"
modified: "2018-12-07"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
  - "4022094"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t02-1001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t02-1001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# Engine Performance Troubleshooting Tree - CM2150 Electronic Control System
**Дерево диагностики мощностных характеристик — система CM2150**

> [!abstract] Процедура · `123-t02-1001`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]], [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2018-12-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t02-1001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t02-1001.pdf)

Printable Version

### Symptoms

- Engine Acceleration or Response Poor

- Cranking Fuel Pressure Low

- Engine Operating Fuel Pressure Low

- Engine Decelerates Slowly

- Engine Difficult to Start or Will Not Start (Exhaust Smoke)

- Engine Difficult to Start or Will Not Start (No Exhaust Smoke)

- Engine Power Output Low

- Engine Runs Rough at Idle

- Engine Runs Rough or Misfires

- Engine Speed Surges at Low or High Idle

- Engine Speed Surges Under Load or in Operating Range

- Smoke, Black - Excessive

- Smoke, White - Excessive

- Engine Shuts Off or Dies Unexpectedly or Dies During Deceleration

- Engine Starts But Will Not Keep Running

- Engine Will Not Reach Rated Speed (RPM)

- Intake Manifold Pressure (Boost) Below Normal

- Intake Manifold Pressure (Boost) Above Normal

### How To Use This Tree

This symptom tree can be used to troubleshoot all the performance-based symptoms listed above. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom. Perform the list of troubleshooting in the sequence shown in the Specifications/Repair section of the tree.

### Shoptalk

Driveability is a term that in general describes vehicle performance on the road. Driveability problems for an engine can be caused by several different factors. Some of the factors are engine-related and some are **not**. Before troubleshooting, it is important to determine the exact complaint and whether the engine has a real driveability problem, or if it simply does **not** meet driver expectations.

Low power is a term that is used in the field to describe many different performance problems. Low power is defined as the inability of the engine to produce the power necessary to move the vehicle at a speed that can be reasonably expected under the given conditions of load, grade, wind, and so on.

Poor acceleration or response is described as the inability of the vehicle to accelerate satisfactorily from a stop or from the bottom of a grade. It can also be the lag in acceleration during an attempt to pass or overtake another vehicle at conditions less than rated speed and load. Poor acceleration or response is difficult to troubleshoot, since it can be caused by several factors.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Perform basic troubleshooting procedures. |  |
|  | **STEP 1A.** Check for active fault codes or high counts of inactive fault codes. | Active fault codes or high counts of inactive fault codes? |
|  | **STEP 1B.** Perform basic troubleshooting checks. | All steps verified to be correct? |
| STEP 2. | Determination of engine symptom. |  |
|  | **STEP 2A.** Low power, poor acceleration, or poor response. | Engine symptom - Low Power, Poor Acceleration, or Poor Response? |
|  | **STEP 2B.** Engine misfire, engine speed surge, or engine speed unstable. | Engine symptom - Engine Misfire, Engine Speed Surge, or Engine Speed Unstable? |
|  | **STEP 2C.** Excessive white or black smoke. | Engine symptom - Excessive White or Black Smoke? |
|  | **STEP 2D.** Low intake manifold pressure (boost). | Engine symptom - Low Intake Manifold Pressure (boost)? |
|  | **STEP 2E.** High intake manifold pressure (boost). | Engine symptom - High Intake Manifold Pressure (boost)? |
|  | **STEP 2F.** Engine will **not** start or difficult to start, engine shuts off unexpectedly. | Engine symptom - Engine Will Not Start or Difficult to Start, Engine Shuts Off Unexpectedly? |
| STEP 3. | No-start troubleshooting procedures. |  |
|  | **STEP 3A.** Verify the operation of cold weather starting aids. | Necessary cold weather starting aids operating properly? |
|  | **STEP 3B.** Check for other fault codes that explain a no-start condition. | Any fault codes that can cause a no-start condition come active during cranking? |
|  | **STEP 3C.** Check engine speed during cranking. | Engine cranking speed greater than 150 rpm? |
|  | **STEP 3D.** Check the engine control module (ECM) keyswitch voltage. | Keyswitch voltage equal to battery voltage? |
|  | **STEP 3E.** Check the ECM battery supply voltage. | ECM battery supply voltage equal to the battery voltage? |
|  | **STEP 3F.** Check fuel rail pressure to the injectors. | Fuel rail pressure greater than 300 bar \[4351 psi\] while cranking? |
|  | **STEP 3G.** Check for fuel pressure from the gerotor pump while cranking the engine. | Fuel supply pressure greater than 500 kPa \[73 psi\]? |
|  | **STEP 3G-1.** Check the inlet fuel restriction. | Restriction higher than the specification? |
|  | **STEP 3G-2.** Check fuel lift pump pressure. | Fuel pressure 3 bar \[44 psi\] after pump operating for 30 seconds? |
|  | **STEP 3G-3.** Check if the engine starts. | Engine starts? |
|  | **STEP 3G-4.** Check for proper operation of the check valve near the fuel lift pump. | Check valve near the fuel lift pump operating properly? |
|  | **STEP 3G-5.** Check if engine starts. | Engine starts? |
|  | **STEP 3H.** Check for external fuel rail (high pressure) leakage. | Fuel rail leakage present? |
|  | **STEP 3I.** Check injector solenoid operation. | Injector tester tool show a green light? |
|  | **STEP 3J.** Measure the injector drain flow from all injectors. | Drain fuel flow from the fuel drain block greater than the specification? |
|  | **STEP 3J-1.** Isolate the injector drain flow from each of the injectors. | Drain fuel flow from the injector greater than the specification? |
|  | **STEP 3K.** Use INSITE™ electronic service tool to perform Fuel Pump Actuator Click Test. | Fuel pump actuator clicks when commanded with the diagnostic test in INSITE™ electronic service tool? |
|  | **STEP 3L.** Measure the fuel drain flow from the fuel pressure relief valve. | Drain fuel flow from the fuel pressure relief valve greater than the specification? |
| STEP 4. | Fuel system troubleshooting procedures. |  |
|  | **STEP 4A.** Check for fault codes. | Fuel system fault codes active? |
|  | **STEP 4B.** Measure the fuel inlet restriction. | Fuel inlet restriction above specifications? |
|  | **STEP 4C.** Check stage 1 fuel filter head check valves for proper operation. | Fuel filter head check valves in good condition and the passageway free of restrictions? |
|  | **STEP 4D.** Use INSITE™ electronic service tool to perform fuel pump actuator click test. | Fuel pump actuator clicks when commanded with the diagnostic test in INSITE™ electronic service tool? |
|  | **STEP 4E.** Measure the injector drain flow from all injectors. | Drain fuel flow from the fuel drain block greater than the specification? |
|  | **STEP 4E-1.** Isolate the injector drain flow from each of the injectors. | Drain fuel flow from the injector greater than the specification? |
|  | **STEP 4F.** Perform Single Cylinder Cut-out Test. | Miss or excessive smoke attributed to a single cylinder? |
|  | **STEP 4G.** Audio check for injector operation. | Miss heard from any individual injector? |
| STEP 5. | Air handling troubleshooting procedures. |  |
|  | **STEP 5A.** Inspect the turbocharger blades for damage. | Damage found on turbocharger blades? |
|  | **STEP 5B.** Check the turbocharger axial and radial clearances. | Turbocharger axial and radial bearing clearances within specification? |
|  | **STEP 5C.** Inspect the charge air cooler. | Charge air cooler free of cracks or other damage? |
|  | **STEP 5D.** Check air intake restrictions. | Air intake restriction greater than 0.635 m-H 2 O \[25 in-H 2 O\]? |
| STEP 6. | Electronic feature troubleshooting procedures. |  |
|  | **STEP 6A.** Verify throttle pedal travel. | Throttle position reads 0 percent when the throttle is released and 100 percent when the throttle is depressed? |
|  | **STEP 6B.** Check ambient air pressure sensor accuracy. | INSITE™ electronic service tool reading within 102 mm-Hg \[4 in-Hg\] of local barometric pressure? |
|  | **STEP 6C.** Check intake manifold pressure sensor accuracy. | Intake manifold pressure reading less than 102 mm-Hg \[4 in-Hg\]? |
| STEP 7. | Base engine troubleshooting procedures. |  |
|  | **STEP 7A.** Verify overhead adjustments are correct. | Overhead settings within the reset limits? |
|  | **STEP 7B.** Check exhaust restriction. | Exhaust back pressure less than 76 mm-Hg \[3 in-Hg\]? |

### STEP 1. Perform basic troubleshooting procedures.

#### STEP 1A. Check for active fault codes or high counts of inactive fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes. Use INSITE™ electronic service tool to read the fault codes. | Active fault codes or high counts of inactive fault codes? **YESRepair:** Follow the electronic fault code trees for the appropriate troubleshooting procedures. | Repair complete. |
| Active fault codes or high counts of inactive fault codes? **NO** | 1B |  |

#### STEP 1B. Perform basic troubleshooting checks.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| The following items **must** be checked or verified before continuing: Verify the fuel level in the tanks Verify there have not been any changes to control parts list (CPL) components on the engine Verify fuel grade is correct for application Verify the engine is operating within the recommended altitude Verify engine oil is at the correct level Verify engine parasitics have not changed Verify engine duty cycle has not changed Verify engine cranking speed is greater than 150 rpm Verify battery voltage is within specifications. | All steps verified to be correct? **YES** | 2A |
| All steps verified to be correct? **NORepair:** Correct the malfunction and verify complaint is no longer present after repair. | Repair complete. |  |

### STEP 2. Determination of engine symptoms.

#### STEP 2A. Low power, poor acceleration, or poor response.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the operator and verify the complaint. Interview the operator. | Engine symptom - Low Power, Poor Acceleration, or Poor Response? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 5 - Air Handling Checks Step 6 - Electronics Checks Step 7 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure. |
| Engine symptom - Low Power, Poor Acceleration, or Poor Response? **NO** | 2B |  |

#### STEP 2B. Engine misfire, engine speed surge, or engine speed unstable.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the operator and verify the complaint. Interview the operator. | Engine symptom - Engine Misfire, Engine Speed Surge, or Engine Speed Unstable? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 5 - Air Handling Checks Step 6 - Electronics Checks Step 7 - Exhaust Restriction Check. | Perform the troubleshooting steps suggested in the repair procedure. |
| Engine symptom - Engine Misfire, Engine Speed Surge, or Engine Speed Unstable? **NO** | 2C |  |

#### STEP 2C. Excessive white or black smoke.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the operator and verify the complaint. Interview the operator. | Engine symptom - Excessive White or Black Smoke? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 5 - Air Handling Checks Step 6 - Electronic System Checks Step 7 - Exhaust Restriction Check. | Perform the troubleshooting steps suggested in the repair procedure. |
| Engine symptom - Excessive White or Black Smoke? **NO** | 2D |  |

#### STEP 2D. Low intake manifold pressure (boost).

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the operator and verify the complaint. Interview the operator. | Engine symptom - Low Intake Manifold Pressure (boost)? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 5 - Air Handling Checks Step 4 - Fuel System Checks Step 7 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure. |
| Engine symptom - Low Intake Manifold Pressure (boost)? **NO** | 2E |  |

#### STEP 2E. High intake manifold pressure (boost).

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the operator and verify the complaint. Interview the operator. | Engine symptom - High Intake Manifold Pressure (boost)? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 6 - Electronics Checks Step 7 - Exhaust Restriction Check. | Perform the troubleshooting steps suggested in the repair procedure. |
| Engine symptom - High Intake Manifold Pressure (boost)? **NO** | 2F |  |

#### STEP 2F. Engine will not start or difficult to start, engine shuts off unexpectedly.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the operator and verify the complaint. Interview the operator. | Engine symptom - Engine Will **Not** Start or Difficult to Start, Engine Shuts Off Unexpectedly? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 3 - No Start Checks Step 4 - Fuel System Checks Step 5 - Air Handling Checks Step 6 - Electronics Checks. | Perform the troubleshooting steps suggested in the repair procedure. |
| Engine symptom - Engine Will **Not** Start or Difficult to Start, Engine Shuts Off Unexpectedly? **NO** | Return to correct symptom tree. |  |

### STEP 3. No-start troubleshooting procedures.

#### STEP 3A. Verify the operation of cold weather starting aids.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check cold weather starting aids. Refer to the Operation of Diesel Engines in Cold Climates, Bulletin 3379009. | Necessary cold weather starting aids operating properly? **YES** | 3B |
| Necessary cold weather starting aids operating properly? **NORepair:** Install or repair cold weather starting aids. Refer to the Operation of Diesel Engines in Cold Climates, Bulletin 3379009. | Repair complete. |  |

#### STEP 3B. Check for other fault codes that explain a no-start condition.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to read fault code information. Look for fault codes that come active during a failed start attempt and can be the cause of a no-start condition. | Any fault codes that can cause a no-start condition come active during cranking? **YESRepair:** Follow the electronic fault code trees for the appropriate troubleshooting procedures. | Repair complete. |
| Any fault codes that can cause a no-start condition come active during cranking? **NO** | 3C |  |

#### STEP 3C. Check engine speed during cranking.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to monitor engine speed and fuel rail pressure while cranking the engine. Check engine speed during cranking. Monitor fuel rail pressure during cranking, (300bar \[4351 psi\] minimum pressure is required to start the engine). If lower fuel rail pressure is observed after completing all sub-steps of Step 3, proceed to Step 5 for further fuel system troubleshooting procedures. | Engine cranking speed greater than 150 rpm? **YES** | 3D |
| Engine cranking speed greater than 150 rpm? **NORepair:** Find and correct the cause for low cranking speed. Check the batteries, engine starting motor, and accessory loads. See the Engine Will **Not** Crank or Cranks Slowly troubleshooting symptom tree. | Repair complete. |  |

#### STEP 3D. Check the ECM keyswitch voltage.

| **Conditions:** Disconnect the engine wiring harness from the ECM 50 pin connector. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the signal voltage from the keyswitch input SIGNAL wire of the engine wiring harness to the engine block ground. Measure the keyswitch voltage with the keyswitch in the ON position and also with the keyswitch in the cranking position. Refer to the circuit wiring diagram or wiring diagram for connector pin identification. | Keyswitch voltage equal to battery voltage? **YES** | 3E |
| Keyswitch voltage equal to battery voltage? **NORepair:** Repair or replace the original equipment manufacturer (OEM) power wiring harness. See equipment manufacturer service information. Repair or replace the keyswitch. Refer to Procedure 019-064 in Section 19. Check the battery connections and fuse terminals. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 013-009 in Section 13. | Repair complete. |  |

#### STEP 3E. Check the ECM battery supply voltage.

| **Conditions:** Turn keyswitch OFF. Disconnect the ECM power wiring harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from the ECM battery SUPPLY (-) pin to the ECM battery SUPPLY (+) pins in the ECM power wiring harness connector. Measure the ECM voltage with the keyswitch in the ON position and also with the keyswitch in the cranking position. Refer to the circuit diagram or wiring diagram for connector pin identification. | ECM battery supply voltage equal to the battery voltage? **YES** | 3F |
| ECM battery supply voltage equal to the battery voltage? **NORepair:** See equipment manufacturer service information. Repair or replace the ECM power wiring harness. Check the battery connections and fuse terminals. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 013-009 in Section 13. | Repair complete. |  |

#### STEP 3F. Check fuel rail pressure to the injectors.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the fuel rail pressure output pressure while cranking the engine. The cranking speed must be greater than 150 rpm for 30 seconds. | Fuel rail pressure greater than 300 bar \[4351 psi\] while cranking? **YES** | 4B |
| Fuel rail pressure greater than 300 bar \[4351 psi\] while cranking? **NO** | 3G |  |

#### STEP 3G. Check for fuel pressure from the gerotor pump while cranking the engine.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Attempt to start the engine by engaging the engine starting motor for at least 30 continuous seconds. Use INSITE™ electronic service tool to monitor fuel pressure. | Fuel supply pressure greater than 500 kPa \[73 psi\]? **YES** | 3H |
| Fuel supply pressure greater than 500 kPa \[73 psi\]? **NO** | 3G-1 |  |

#### STEP 3G-1. Check the inlet fuel restriction.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel restriction and stage 1 filter restriction. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-020 in Section 6. | Restriction higher than the specification? **YESRepair:** If the inlet restriction is higher than specifications, see equipment manufacturer service information to determine the source of the high restriction. If the stage 1 filter restriction is higher than specifications, replace the stage 1 filter. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-015 in Section 6. | Repair complete. |
| Restriction higher than the specification? **NO** | 3G-2 |  |

#### STEP 3G-2. Check fuel lift pump pressure.

| **Conditions:** Turn keyswitch ON. Attach a fuel pressure gauge to the fuel filter head stage one filter outlet. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the fuel lift pump output pressure. Turn keyswitch ON, but engine not operating. Listen for the fuel lift pump to operate. The pump will operate at keyswitch ON then shut OFF. | Fuel pressure 3 bar \[44 psi\] after pump operating for 30 seconds? **YESRepair:** Replace the air bleed check valve. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-020 in Section 6. | 3G-3 |
| Fuel pressure 3 bar \[44 psi\] after pump operating for 30 seconds? **NO** | 3G-4 |  |

#### STEP 3G-3. Check if engine starts.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check if engine starts. Attempt to start the engine. | Engine starts? **YESRepair:** The replacement of the air bleed check valve in the previous step corrected the problem. | Repair complete. |
| Engine starts? **NORepair:** Replace the fuel pump. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 005-016 in Section 5. | Repair complete. |  |

#### STEP 3G-4. Check for proper operation of the check valve near the fuel lift pump.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the check valve for proper operation. Turn keyswitch ON, but engine not operating. | Check valve near the fuel lift pump operating correctly? **YESRepair:** Replace the air bleed check valve. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-020 in Section 6. | 3G-5 |
| Check valve near the fuel lift pump operating correctly? **NORepair:** Replace the air check valve near the fuel lift pump. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-008 in Section 6. | Repair complete |  |

#### STEP 3G-5. Check if engine starts.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check if engine starts. Attempt to start the engine. | Engine starts? **YESRepair:** The replacement of the air bleed check valve in the previous step corrected the problem. | Repair complete. |
| Engine starts? **NORepair:** Replace the fuel lift pump. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 005-045 in Section 6. | Repair complete. |  |

#### STEP 3H. Check for external fuel rail (high-pressure) leaks.

| **Conditions:** Crank the engine to develop fuel pressure. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel rail for leaks. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-051 in Section 6. | Fuel rail leakage present? **YESRepair:** Replace any components associated with the leak. | Repair complete. |
| Fuel rail leakage present? **NO** | 3I |  |

#### STEP 3I. Check injector solenoid operation.

| **Conditions:** Turn keyswitch ON. Attach the injector tester, Part Number 2892293, to an injector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Test all injectors using the injector tester tool. Turn the keyswitch ON, and attach the injector tester tool to the 2 pin injector connector. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-026 in Section 6. | Injector tester tool show a green light? **YES** | 3J |
| Injector tester tool show a green light? **NORepair:** Replace the malfunctioning injector. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-026 in Section 6. | Repair complete. |  |

#### STEP 3J. Measure the injector drain flow from all injectors.

| **Conditions:** Crank engine to at least 150 rpm. Unplug all injectors. Connect appropriate service tools to measure injector drain flow at the fuel drain block. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the injector return fuel drain flow at the fuel drain block. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-026 in Section 6. | Drain fuel flow from the fuel drain block greater than the specification? **YES** | 3J-1 |
| Drain fuel flow from the fuel drain block greater than the specification? **NO** | 3K |  |

#### STEP 3J-1. Isolate the injector drain flow from each of the injectors.

| **Conditions:** Crank engine to at least 150 rpm. Unplug all injectors. Connect appropriate service tools to measure injector drain flow at each cylinder head. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the injector return fuel drain flow at the fuel drain block. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-026 in Section 6. | Drain fuel flow from the injector greater than the specification? **YESRepair:** Replace any malfunctioning injectors. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-026 in Section 6. | Repair complete. |
| Drain fuel flow from the injector greater than the specification? **NO** | 3K |  |

#### STEP 3K. Use INSITE™ electronic service tool to perform the Fuel Pump Actuator Click Test.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the Fuel Pump Actuator Click Test. Use INSITE™ electronic service tool to perform the Fuel Pump Actuator Click Test. | Fuel pump actuator clicks when commanded with the diagnostic test in INSITE™ electronic service tool? **YES** | 3L |
| Fuel pump actuator clicks when commanded with the diagnostic test in INSITE™ electronic service tool? **NORepair:** Replace the fuel pump actuator. Refer to Procedure 019-117 in Section 19. | Repair complete. |  |

#### STEP 3L. Measure the fuel drain flow from the fuel pressure relief valve.

| **Conditions:** Crank engine to at least 150 rpm. Unplug all injectors. Connect appropriate service tools to measure fuel drain flow from the fuel pressure relief valve. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the injector return fuel drain flow at the fuel drain block. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-061 in Section 6. | Drain fuel flow from the fuel pressure relief valve greater than the specification? **YESRepair:** Replace the fuel pressure relief valve. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-061 in Section 6. | Repair complete. |
| Drain fuel flow from the fuel pressure relief valve greater than the specification? **NORepair:** Replace the fuel pump. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 005-016 in Section 5. | Repair complete. |  |

### STEP 4. Fuel system troubleshooting procedures.

#### STEP 4A. Check for fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to read the fault code information. Determine if there are active fuel system fault codes related to the complaint. | Fuel system fault codes active? **YESRepair:** Follow the electronic fault code trees for the appropriate troubleshooting procedures. | Repair complete. |
| Fuel system fault codes active? **NO** | 4B |  |

#### STEP 4B. Measure the fuel inlet restriction.

| **Conditions:** Check for fuel inlet restriction. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-020 in Section 6. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the fuel inlet restriction. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-020 in Section 6. | Fuel inlet restriction above specification? **YESRepair:** Find and correct the cause of the high inlet restriction. Look for plugged OEM fuel filters, or screens, a restricted lift pump bypass check valve, pinched OEM fuel lines or a restricted stand pipe in the OEM fuel tank. | Repair complete. |
| Fuel inlet restriction above specification? **NO** | 4C |  |

#### STEP 4C. Check stage 1 fuel filter head check valves for proper operation.

| **Conditions:** Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-008 in Section 6. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check fuel filter head check valves for proper operation. The check valve prevents back-flow of fuel through the first stage filter during priming and operation when installed properly. A stuck check valve will not allow fuel flow from the lift pump to prime the engine. | Fuel filter head check valves in good condition and the passageway free of restrictions? **YES** | 4D |
| Fuel filter head check valves in good condition and the passageway free of restrictions? **NORepair:** Replace the fuel check valve. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-008 in Section 6. | Repair complete. |  |

#### STEP 4D. Use INSITE™ electronic service tool to perform the fuel pump actuator click test.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the fuel pump actuator click test. Use INSITE™ electronic service tool to perform the fuel pump actuator click test. | Fuel pump actuator clicks when commanded with the diagnostic test in INSITE™ electronic service tool? **YES** | 4E |
| Fuel pump actuator clicks when commanded with the diagnostic test in INSITE™ electronic service tool? **NORepair:** Replace the fuel pump actuator. Refer to Procedure 019-117 in Section 19. | Repair complete. |  |

#### STEP 4E. Measure the injector drain flow from all injectors.

| **Conditions:** Crank engine to at least 150 rpm. Unplug all injectors. Connect appropriate service tools to measure injector drain flow at the fuel drain block. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the injector return fuel drain flow at the fuel drain block. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-026 in Section 6. | Drain fuel flow from the fuel drain block greater than the specification? **YES** | 4E-1 |
| Drain fuel flow from the fuel drain block greater than the specification? **NO** | 4G |  |

#### STEP 4E-1. Isolate the injector drain flow from each of the injectors.

| **Conditions:** Crank engine to at least 150 rpm. Unplug all injectors. Connect appropriate service tools to measure injector drain flow at each cylinder head. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the injector return fuel drain flow at the cylinder head. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-026 in Section 6. | Drain fuel flow from the injector greater than the specification? **YESRepair:** Replace any malfunctioning injectors. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-026 in Section 6. | Repair complete. |
| Drain fuel flow from the injector greater than the specification? **NO** | 4G |  |

#### STEP 4F. Perform single cylinder cut-out test.

| **Conditions:** Turn keyswitch ON. Operate engine at low idle. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform Single Cylinder Cut-out Test. Operate the engine at load. Use INSITE™ electronic service tool to perform the Cylinder Cut-out Test to disable individual injectors. | Miss or excessive smoke attributed to a single cylinder? **YESRepair:** Look for a cause of the complaint, including valve lash and excessive crankcase pressure, that can indicate power cylinder damage or camshaft lobe wear. If no other damage is found, replace the injector in the cylinder that was identified using the single cylinder cut-out test. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-026 in Section 6. | Repair complete. |
| Miss or excessive smoke attributed to a single cylinder? **NO** | 4G |  |

#### STEP 4G. Audio check for injector operation.

| **Conditions:** Turn keyswitch ON. Operate engine at idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform an audio check on each injector to verify proper operation. With the engine running at idle, use a mechanic's stethoscope (Snap-On™, Part Number GA111D, or similar) to identify any individual injector improper operation. | Can a miss be heard from any individual injector? **YESRepair:** Replace any malfunctioning injectors. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 006-026 in Section 6. | Repair complete. |
| Can a miss be heard from any individual injector? **NO** | 2A |  |

### STEP 5. Air handling troubleshooting procedures.

#### STEP 5A. Inspect the turbocharger blades for damage.

| **Conditions:** Turn keyswitch OFF. Remove the intake and exhaust pipes from the turbocharger. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the compressor and turbine blades for damage or wear. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 010-033 in Section 10. | Damage found on turbocharger blades? **YESRepair:** Replace the turbocharger assembly. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. [[20-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | Repair complete. |
| Damage found on turbocharger blades? **NO** | 5B |  |

#### STEP 5B. Check the turbocharger axial and radial clearances.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the turbocharger for correct axial and radial clearance. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure s 010-033 in Section 10. | Turbocharger axial and radial bearing clearances within specification? **YES** | 5C |
| Turbocharger axial and radial bearing clearances within specification? **NORepair:** Replace the turbocharger assembly. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. [[20-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | Repair complete. |  |

#### STEP 5C. Inspect the charge air cooler.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the charge air cooler. Inspect the charge air cooler for damage. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 010-027 in Section 10. | Charge air cooler free of cracks or other damage? **YES** | 5D |
| Charge air cooler free of cracks or other damage? **NORepair:** Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. [[20-010-027 — Charge-Air Cooler\|Refer to Procedure 010-027 in Section 10.]] | Repair complete |  |

#### STEP 5D. Check air intake restriction.

| **Conditions:** Turn keyswitch OFF. Install a vacuum gauge or water manometer in the air intake piping. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check air intake system restriction. Install a vacuum gauge into the air intake system. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 010-031 in Section 10. | Air intake restriction greater than 0.635 m-H 2 O \[25 in-H 2 O\]? **YES** | Repair complete. |
| Air intake restriction greater than 0.635 m-H 2 O \[25 in-H 2 O\]? **NO** | 2A |  |

### STEP 6. Electronic feature troubleshooting procedures.

#### STEP 6A. Verify throttle pedal travel.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify throttle pedal travel. Use INSITE™ electronic service tool to monitor throttle position while fully depressing and releasing the throttle pedal. | Throttle position reads 0 percent when the throttle is released and 100 percent when the throttle is depressed? **YES** | 6B |
| Throttle position reads 0 percent when the throttle is released and 100 percent when the throttle is depressed? **NORepair:** Determine and correct the cause of the throttle pedal restriction. | Repair complete. |  |

#### STEP 6B. Check ambient air pressure sensor accuracy.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to monitor the barometric air pressure. Compare INSITE™ electronic service tool barometric pressure readings with the local barometric pressure. | INSITE™ electronic service tool reading within 102 mm-Hg \[4 in-Hg\] of local barometric pressure? **YES** | 6C |
| INSITE™ electronic service tool reading within 102 mm-Hg \[4 in-Hg\] of local barometric pressure? **NORepair:** Replace the barometric pressure sensor. Refer to Procedure 019-004 in Section 19. | Repair complete. |  |

#### STEP 6C. Check intake manifold pressure sensor accuracy.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check intake manifold pressure sensor accuracy. Use INSITE™ electronic service tool to monitor the value of intake manifold pressure without the engine operating. | Intake manifold pressure reading less than 102 mm-Hg \[4 in-Hg\]? **YES** | 7A |
| Intake manifold pressure reading less than 102 mm-Hg \[4 in-Hg\]? **NORepair:** Replace the intake manifold pressure sensor. Refer to Procedure 019-061 in Section 19. | Repair complete |  |

### STEP 7. Base engine troubleshooting procedures.

#### STEP 7A. Verify overhead adjustments are correct.

| **Conditions:** Turn keyswitch OFF. Remove the rocker lever cover. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 003-011 in Section 3. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the overhead setting. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 003-006 in Section 3. | Overhead settings within the reset limits? **YES** | 7B |
| **Overhead** settings within the reset limits? **NORepair:** Adjust the overhead settings. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. [[20-003-006-tr — Overhead Set (OBC)\|Refer to Procedure 003-006 in Section 3.]] | Repair complete. |  |

#### STEP 7B. Check exhaust restriction.

| **Conditions:** Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Refer to Procedure 011-009 in Section 11. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the exhaust system back pressure. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. [[20-011-009 — Exhaust Restriction\|Refer to Procedure 011-009 in Section 11.]] | Exhaust back pressure less than 76 mm-Hg \[3 in-Hg\]? **YES** | 2A |
| Exhaust back pressure less than 76 mm-Hg \[3 in-Hg\]? **NORepair:** Inspect exhaust system for source of high restriction. | Repair complete. |  |
