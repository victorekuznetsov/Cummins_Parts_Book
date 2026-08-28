---
type: "Процедура"
doc: "70-t02-1001"
title_en: "Engine Performance Troubleshooting Tree - Signature™ and ISX CM870"
modified: "2015-07-08"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/70/70-t02-1001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/70-t02-1001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/70"
---

# Engine Performance Troubleshooting Tree - Signature™ and ISX CM870

> [!abstract] Процедура · `70-t02-1001`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2015-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/70/70-t02-1001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/70-t02-1001.pdf)

Printable Version

### Symptoms

- Engine Acceleration or Response Poor

- Cranking Fuel Pressure is Low

- Engine Operating Fuel Pressure is Low

- Engine Difficult to Start or Will **Not** Start (Exhaust Smoke)

- Engine Difficult to Start or Will **Not** Start (No Exhaust Smoke)

- Engine Run On

- Engine Power Output Low

- Engine Runs Rough at Idle

- Engine Runs Rough or Misfires

- Engine Speed Surges at Low or High Idle

- Engine Speed Surges Under Load or in Operating Range

- Smoke, Black - Excessive

- Smoke, White - Excessive

- Engine Shuts Off or Dies Unexpectedly or Dies During Deceleration

- Engine Starts But Will **Not** Keep operating

- Engine Will **Not** Reach Rated Speed (rpm).

### How To Use This Tree

This symptom tree can be used to troubleshoot all performance based symptoms listed above. Start by performing Step 1 troubleshooting. Step 2 asks a series of questions and will provide a list of troubleshooting steps to perform depending on the symptom. Perform the list of troubleshooting in the sequence shown in the Specifications/Repair section of the tree.

### Shoptalk

Prior to operating INSITE™ electronic service tool exhaust gas recirculation (EGR) Valve and EGR Valve/Turbocharger Operational Test, the engine control module (ECM) Calibration Software Phase can possibly need to be updated to the latest Software Phase. The ECM Calibration Phase Software can be checked in INSITE™ electronic service tool, under 'Features and Parameters'. Expand the selection for 'System ID and Dataplate'and go to 'Calibration Information'. If the Software Phase is earlier than shown below, calibrate the ECM, use the January 2006 INCAL™ CD-ROM, or later. Engines with the Software Phase listed below or later do **not** require a calibration.

ISX engines with CM870 (engines built after January 2004) require Software Phase 06050302.

ISX engines with CM870 (engines built before January 2004) require no changes at this time.

This is a warrantable calibration change.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - 20 AWG male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3824811 - 12 AWG male Deutsch™/AMP™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Perform basic troubleshooting procedures. |  |
|  | **STEP 1A.** Check for active fault codes or high counts of inactive fault codes. | Active fault codes or high counts of inactive fault codes? |
|  | **STEP 1B.** Perform basic troubleshooting checks. | All steps have been verified to be correct? |
| STEP 2. | Determination of engine symptom. |  |
|  | **STEP 2A.** Low power, poor acceleration, or poor response. | Is the engine symptom low power, poor acceleration, or poor response? |
|  | **STEP 2B.** Engine misfire. | Is the engine symptom Engine Runs Rough or Misfires? |
|  | **STEP 2C.** Excessive black smoke. | Is the engine symptom Excessive Black Smoke? |
|  | **STEP 2D.** Excessive white smoke. | Is the engine symptom Excessive White Smoke and the engine is using coolant? |
|  | **STEP 2D-1.** Excessive white smoke. | Is the engine symptom Excessive White Smoke and the engine is not using coolant? |
|  | **STEP 2E.** Engine speed surge or engine speed unstable. | Is the engine symptom Engine Speed Surge or Engine Speed Unstable? |
|  | **STEP 2F.** Engine will not start or difficult to start. | Is the symptom Engine Difficult to Start or Will Not Start? |
|  | **STEP 2G.** Engine stalls or shuts off unexpectedly. | Is the symptom Engine Stalls or Shuts Off Unexpectedly? |
|  | **STEP 2H.** Engine run on or will not shut down. | Is the engine symptom Engine Run On or Slow to Shut Down after operated at high idle for 1 minute then keyed OFF? |
| STEP 3. | No-start troubleshooting procedures. |  |
|  | **STEP 3A.** Verify the fuel system has been primed. | Has the fuel system properly primed? |
|  | **STEP 3B.** Check fuel shutoff valve voltage. | Is the fuel shutoff valve voltage greater than 11-VDC? |
|  | **STEP 3B-1.** Check ECM keyswitch voltage. | Is the keyswitch voltage equal to battery voltage? |
|  | **STEP 3B-2.** Check the fuel shutoff valve wire. | Less than 10 ohms? |
|  | **STEP 3B-3.** Check the ECM power and ground. | Is the ECM battery supply voltage equal to the battery voltage? |
|  | **STEP 3C.** Check fuel shutoff valve resistance. | Is the fuel shutoff solenoid resistance 1 to 5 ohms for 6-VDC solenoids, 6 to 15 ohms for 12-VDC solenoids, 24 to 50 ohms for 24-VDC solenoids, 42 to 80 ohms for 32-VDC solenoids, 46 to 87 ohms for 36-VDC solenoids, 92 to 145 ohms for 48-VDC solenoids, 315 to 375 ohms for 74-VDC solenoids, 645 to 735 ohms for 115-VAC solenoids? |
|  | **STEP 3D.** Check fuel shutoff valve actuator. | Debris or damage found on the valve disc, valve seat, or actuator disc? |
|  | **STEP 3E.** Check for correct priming pump operation, if equipped. | Does the lift pump operate after turning the keyswitch ON? |
|  | **STEP 3E-1.** Check priming pump pressure. | Does pump pressure meet the 69 kPa \[10 psi\] specification? |
|  | **STEP 3F.** Check for coolant in the EGR transfer tube. | Is coolant present in the crossover tube? |
| STEP 4. | Fuel system checks. |  |
|  | **STEP 4A.** Verify the fuel system has been primed. | Has the fuel system been properly primed? |
|  | **STEP 4B.** Check for air in the fuel. | Are air bubbles visible in the coil of clear tubing? |
|  | **STEP 4C.** Check fuel inlet restriction. | Is fuel inlet restriction less than the specifications? |
|  | **STEP 4D.** Check drain line restriction. | Is fuel drain line restriction less than 229 mm-Hg \[9 in-Hg\]? |
|  | **STEP 4E.** Check rail fuel pressure. | Does the rail fuel pressure meet the specification? |
|  | **STEP 4E-1.** Check the pressure side fuel filter restriction. | Is the pressure side fuel filter pressure drop less than 517 kPa \[75 psi\]? |
|  | **STEP 4E-2.** Check 1724 kPa \[250 psi\] pressure regulator. | Is the 1724 kPa \[250 psi\] pressure regulator free of debris or damage? |
|  | **STEP 4E-3.** Check 2206 kPa \[320 psi\] or 2620 kPa \[380 psi\] pressure regulator. | Is the pressure regulator free of debris or damage? |
| STEP 5. | Injector and Actuator Diagnostics. |  |
|  | **STEP 5A.** Perform the injector check valve leak test. | Did the injector leak test detect a leaking injector? |
|  | **STEP 5B.** Perform INSITE™ electronic service tool Cylinder Performance Test. | Does performing INSITE™ electronic service tool Cylinder Performance Test isolate to a single malfunctioning injector? |
|  | **STEP 5B-1.** Perform INSITE™ electronic service tool Cylinder Performance Test at 600 rpm. | Does performing INSITE™ electronic service tool Cylinder Performance Test isolate to a single malfunctioning injector? |
|  | **STEP 5B-2.** Perform INSITE™ electronic service tool Cylinder Performance Test at 700 rpm. | Does performing INSITE™ electronic service tool Cylinder Performance Test isolate to a single malfunctioning injector? |
|  | **STEP 5B-3.** Perform INSITE™ electronic service tool Cylinder Performance Test at 800 rpm. | Does performing INSITE™ electronic service tool Cylinder Performance Test isolate to a single malfunctioning injector? |
|  | **STEP 5C.** Perform INSITE™ electronic service tool Cylinder Cutout Test. | Do all cylinders pass the cylinder cutout test? |
|  | **STEP 5C-1.** Perform INSITE™ electronic service tool Cylinder Cutout Test on both injector banks. | Can a malfunctioning bank of injectors be isolated by operating the engine on either bank of injectors? |
|  | **STEP 5C-2.** Perform INSITE™ electronic service tool Cylinder Cutout Test. | Can a malfunctioning injector be isolated by operating the engine on a single injector? |
|  | **STEP 5C-3.** Verify overhead adjustments are correct for the suspected malfunctioning injector. | Are the overhead settings within the reset limits outlines in Procedure 003-004 in Section 3? |
|  | **STEP 5D.** Swap the front and rear metering actuators. | Does the malfunctioning bank follow the metering actuator? |
|  | **STEP 5E.** Swap the front and rear timing actuators. | Does the malfunctioning bank follow the timing actuator? |
| STEP 6. | Air handling diagnostic checks. |  |
|  | **STEP 6A.** Start the engine and read the fault codes. | Active fault codes? |
|  | **STEP 6B.** Check the air intake system for leaks. | Leaks found? |
|  | **STEP 6C.** Check air intake restriction. | Restriction greater than 635 mm-H 2 O \[25 in-H 2 O\] for a used air filter or 254 mm-H 2 O \[10 in-H 2 O\] for a new filter? |
|  | **STEP 6D.** Inspect the charge-air cooler. | Problems found with the charge-air cooler? |
|  | **STEP 6E.** Check exhaust restriction. | Restriction between 518 mm-H 2 O \[20.4 in-H 2 O\] or 38 mm-Hg \[1.5 in-Hg\] and 1036 mm-H 2 O \[40.8 in-H 2 O\] or 76 mm-Hg \[3.0 in-Hg\]? |
|  | **STEP 6F.** Inspect the turbocharger blades for damage. | Damage found on turbocharger blades? |
|  | **STEP 6G.** Determine turbocharger type. | Is the turbocharger a variable geometry turbocharger? |
|  | **STEP 6H.** Check the variable geometry actuator rod for correct travel. | Does the turbocharger actuator rod extend between 10 and 12 mm \[0.394 and 0.472 in\]? |
|  | **STEP 6H-1.** Check for air leaks and inspect air lines. | Air leaks found in the system? |
|  | **STEP 6D-2.** Check the engine and vehicle grounds. | Connections tight and corrosion-free? |
|  | **STEP 6D-3.** Check for air pressure at the turbocharger control valve outlet. | Is vehicle air tank pressure present at the turbocharger control valve outlet? |
|  | **STEP 6H-4.** Check for air pressure at the turbocharger control valve outlet. | Does the pressure gauge read more than 103 kPa \[15 psi\] after 5 minutes? |
|  | **STEP 6H-5.** Check for correct turbocharger actuator travel. | Does the turbocharger actuator rod travel at least 12 mm \[0.472 in\]? |
|  | **STEP 6H-6.** Check for air pressure at the turbocharger control shutoff valve outlet. | Can air be heard escaping from the turbocharger control shutoff valve outlet? |
|  | **STEP 6H-7.** Check for air pressure at the turbocharger control shutoff valve inlet. | Can air be heard escaping from the turbocharger control shutoff valve inlet? |
|  | **STEP 6H-8.** Check for plugged turbocharger control shutoff valve filter. | Is an air leak present at the turbocharger control shutoff valve filter head? |
|  | **STEP 6I.** Perform INSITE™ electronic service tool EGR Valve/Turbocharger Operational Test. | Does the Turbocharger Operational Test pass? |
|  | **STEP 6E-1.** Check the engine and vehicle grounds. | Connections tight and corrosion-free? |
|  | **STEP 6J.** Inspect the wastegate actuator hose. | Holes or cracks found in the wastegate actuator hose? |
|  | **STEP 6K.** Inspect the wastegate actuator rod for travel. | Does the wastegate actuator rod move? |
|  | **STEP 6G-1.** Inspect wastegate actuator rod for travel. | Does the wastegate actuator rod move? |
|  | **STEP 6L.** Measure resistance of the four-stage wastegate controllers, if equipped. | Are the wastegate controller solenoid resistances between 6 to 10 ohms for 12-VDC solenoids, 24 to 40 ohms for 24-VDC solenoids? |
|  | **STEP 6M.** Inspect four-stage wastegate controller, if equipped. | Damage or debris found on the valve disc, valve seat, or actuator disc? |
| STEP 7. | Check EGR valve for proper operation. |  |
|  | **STEP 7A.** Check for air leaks in the EGR system. | Air leaks found in the EGR connection tubing? |
|  | **STEP 7B.** Check the repair history. | Is there a record of the poppet head missing? |
|  | **STEP 7C.** Perform EGR Valve Test. | Does the EGR Valve Test pass? |
| STEP 8. | Verify electronic features are operating correctly. |  |
|  | **STEP 8A.** Verify accelerator pedal travel. | Does the Accelerator Pedal read 0 when the accelerator is released and 100 percent when the accelerator is depressed? |
|  | **STEP 8B.** Monitor vehicle speed. | Does the vehicle speed read 0 when the vehicle is not moving? |
|  | **STEP 8C.** Verify electronic feature settings are correct. | Are the electronic features set correctly? |
|  | **STEP 8D.** Check the barometric pressure sensor reading. | Is the barometric pressure sensor reading in INSITE™ electronic service tool within 5 percent of the present local barometric pressure reading? |
| STEP 9. | Perform base engine mechanical checks. |  |
|  | **STEP 9A.** Verify overhead adjustments are correct. | Overhead settings within the reuse limits? |
|  | **STEP 9B.** Verify engine brake adjustment. | Engine brake settings within the reuse limits? |
|  | **STEP 9C.** Measure turbocharger axial and radial clearance. | Axial and radial clearances within specification? |
|  | **STEP 9D.** Verify engine blowby is within specification. | Engine blowby measurements within specification? |
|  | **STEP 9E.** Verify injection timing is correct. | Injection timing within specification? |
|  | **STEP 9F.** Check for a damaged vibration damper. | Vibration damper damaged or out of specification? |
| STEP 10. | Check the EGR differential pressure sensor and exhaust gas pressure sensor tubes. |  |
|  | **STEP 10A.** Check the EGR differential pressure tubes for cracks, restrictions, or leaks. | Cracks, restrictions, or leaks present? |
|  | **STEP 10B.** Check the exhaust gas pressure sensor tubes for cracks, restrictions, or leaks. | Cracks, restrictions, or leaks present? |

### STEP 1. Perform basic troubleshooting procedures.

#### STEP 1A. Check for active fault codes or high counts of inactive fault codes.

| **Conditions:** Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes or high counts of inactive fault codes. Use INSITE™ electronic service tool to read the fault codes. | Active fault codes or high counts of inactive fault codes? **YES** | Go to appropriate fault code troubleshooting tree |
| Active fault codes or high counts of inactive fault codes? **NO** | 1B |  |

#### STEP 1B. Perform basic troubleshooting checks.

| **Conditions:** n/a |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| The following items must be checked or verified before continuing: Verify the fuel level in the tanks. Verify there have not been any changes to CPL components on the engine. Verify ECM calibration is correct. Verify fuel grade is correct for the application. Verify the engine is operating within the recommended altitude. Verify engine oil is at the correct level. Verify engine parasitics have not changed. Verify engine duty cycle has not changed. Verify engine cranking speed is greater than 150 rpm. | All steps have been verified to be correct? **YES** | 2A |
| All steps have been verified to be correct? **NORepair:** Correct the condition and verify complaint is no longer present after repair. | Repair complete |  |

### STEP 2. Determination of engine symptom.

#### STEP 2A. Low power, poor acceleration, or poor response.

| **Conditions:** n/a |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. n/a | Is the engine symptom low power, poor acceleration, or poor response? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 6 - Air Handling Checks With EGR - Step 7 - EGR Checks Step 8 - Electronic Checks Step 5 - Injector Checks Step 9 - Base Engine Checks With EGR - Step 10 - EGR Differential Pressure and Exhaust Gas Pressure Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Is the engine symptom low power, poor acceleration, or poor response? **NO** | 2B |  |

#### STEP 2B. Engine misfire.

| **Conditions:** n/a |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. n/a | Is the engine symptom Engine Runs Rough or Misfires? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 5 - Injector Checks Step 4 - Fuel System Checks Step 9 - Base Engine Checks With EGR - Step 10 - EGR Differential Pressure and Exhaust Gas Pressure Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Is the engine symptom Engine Runs Rough or Misfires? **NO** | 2C |  |

#### STEP 2C. Excessive black smoke.

| **Conditions:** n/a |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. n/a | Is the engine symptom Excessive Black Smoke? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 6 - Air Handling Checks Step 4 - Fuel System Checks Step 5 - Injector Checks With EGR - Step 7 - EGR Checks With EGR - Step 10 - EGR Differential Pressure and Exhaust Gas Pressure Checks Step 9 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Is the engine symptom Excessive Black Smoke? **NO** | 2D |  |

#### STEP 2D. Excessive white smoke.

| **Conditions:** n/a |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. n/a | Is the engine symptom Excessive White Smoke and the engine is using coolant? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: See the Coolant Loss - Internal symptom tree. | Perform the troubleshooting steps suggested in the repair procedure |
| Is the engine symptom Excessive White Smoke and the engine is using coolant? **NO** | 2D-1 |  |

#### STEP 2D-1. Excessive white smoke.

| **Conditions:** n/a |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. n/a | Is the engine symptom Excessive White Smoke and the engine is **not** using coolant? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 5 - Injector Checks Step 6 - Air Handling Checks Step 9 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Is the engine symptom Excessive White Smoke and the engine is **not** using coolant? **NO** | 2E |  |

#### STEP 2E. Engine speed surge or engine speed unstable.

| **Conditions:** n/a |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. n/a | Is the engine symptom Engine Speed Surge or Engine Speed Unstable? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 4 - Fuel System Checks Step 5 - Injector Checks With EGR - Step 10 - EGR Differential Pressure and Exhaust Gas Pressure Checks Step 6 - Air Handling Checks Step 8 - Electronics Checks Step 9 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Is the engine symptom Engine Speed Surge or Engine Speed Unstable? **NO** | 2F |  |

#### STEP 2F. Engine will not start or difficult to start.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver to verify the complaint. n/a | Is the symptom Engine Difficult to Start or Will **Not** Start? **YESRepair:** Perform the steps that pertain to difficult to start or will **not** start concerns per the troubleshooting steps in the recommended order listed below: Step 3 - No Start Checks Step 4 - Fuel System Checks Step 5 - Injector Checks Step 6 - Air Handling Checks Step 8 - Electronics Checks Check the engine base timing. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 001-088 in Section 1. Step 9 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Is the symptom Engine Difficult to Start or Will **Not** Start? **NO** | 2G |  |

#### STEP 2G. Engine stalls or shuts off unexpectedly.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver to verify the complaint. n/a | Is the symptom Engine Stalls or Shuts Off Unexpectedly? **YESRepair:** Perform the steps that pertain to stalls or shuts off unexpectedly per the troubleshooting steps in the recommended order listed below: Step 3 - No Start Checks Step 4 - Fuel System Checks Step 5 - Injector Checks Step 6 - Air Handling Checks Step 8 - Electronics Checks Step 9 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Is the symptom Engine Stalls or Shuts Off Unexpectedly? **NO** | 2H |  |

#### STEP 2H. Engine run on, or will not shut down

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver and verify the complaint. n/a | Is the engine symptom Engine Run On or Slow to Shut Down after operated at high idle for 1 minute then keyed OFF? **YESRepair:** Perform the troubleshooting steps in the recommended order listed below: Step 5 - Injector Checks Step 4 - Fuel System Checks Step 9 - Base Engine Checks. | Perform the troubleshooting steps suggested in the repair procedure |
| Is the engine symptom Engine Run On or Slow to Shut Down after operated at high idle for 1 minute then keyed OFF? **NO** | Return to the appropriate symptom tree |  |

### STEP 3. No-start troubleshooting procedures.

#### STEP 3A. Verify the fuel system has been primed.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| If entering this tree after a component has been replaced in the fuel system, or after the engine was run out of fuel, verify the fuel system has been properly primed before proceeding. Verify the fuel system has been properly primed. Use the following procedure for fuel system priming information found in the Signature™, ISX, and QSX15, Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 006-015 in Section 6. | Has the fuel system been properly primed? **YES** | 3B |
| Has the fuel system been properly primed? **NORepair:** Prime the fuel system. Use the following procedure for fuel system priming information found in the Signature™, ISX, and QSX15, Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 006-015 in Section 6. | Repair complete |  |

#### STEP 3B. Check fuel shutoff valve voltage.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from the fuel shutoff valve post to engine block ground. n/a | Is the fuel shutoff valve voltage greater than 11-VDC? **YES** | 3C |
| Is the fuel shutoff valve voltage greater than 11-VDC? **NO** | 3B-1 |  |

#### STEP 3B-1. Check ECM keyswitch voltage.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from the keyswitch input SIGNAL wire of the OEM harness to engine block ground. n/a | Is the keyswitch voltage equal to battery voltage? **YES** | 3B-2 |
| Is the keyswitch voltage equal to battery voltage? **NORepair:** Repair or replace the OEM power harness, keyswitch, or check the battery connections. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334. [[99-019-064 — Key Switch Power Supply Circuit\|Refer to Procedure 019-064 in Section 19.]] | Repair complete |  |

#### STEP 3B-2. Check the fuel shutoff valve wire.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the fuel shutoff valve wire from the valve terminal post. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the fuel shutoff valve SIGNAL pin in the ECM connector to the fuel shutoff valve eyelet. Use the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3B-3 |
| Less than 10 ohms? **NORepair:** Repair or replace the engine harness. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334. Refer to Procedure 019-043 in Section 19. | Repair complete |  |

#### STEP 3B-3. Check the ECM power and ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the ECM power supply connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from the ECM battery SUPPLY (-) to the ECM battery SUPPLY (+) pins in the ECM power harness connector. n/a | Is the ECM battery supply voltage equal to the battery voltage? **YESRepair:** Replace the ECM. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334. Refer to Procedure 019-031 in Section 19. | Repair complete |
| Is the ECM battery supply voltage equal to the battery voltage? **NORepair:** Repair or replace the ECM power harness. | Repair complete |  |

#### STEP 3C. Check fuel shutoff valve resistance.

| **Conditions:** Turn keyswitch OFF. Disconnect fuel shutoff valve SIGNAL wire from the fuel shutoff solenoid. Fuel shutoff valve temperature between 20°C \[68°F\] and 25°C \[78°F\]. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the fuel shutoff solenoid post to engine block ground. The fuel shutoff solenoid **must** be between 20°C \[68°F\] and 25°C \[78°F\] before using the resistance specifications listed. | Is the fuel shutoff solenoid resistance: 1 to 5 ohms for 6-VDC solenoids 6 to 15 ohms for 12-VDC solenoids 24 to 50 ohms for 24-VDC solenoids 42 to 80 ohms for 32-VDC solenoids 46 to 87 ohms for 36-VDC solenoids 92 to 145 ohms for 48-VDC solenoids 315 to 375 ohms for 74-VDC solenoids 645 to 735 ohms for 115-VAC solenoids? **YES** | 3D |
| Is the fuel shutoff solenoid resistance: 1 to 5 ohms for 6-VDC solenoids 6 to 15 ohms for 12-VDC solenoids 24 to 50 ohms for 24-VDC solenoids 42 to 80 ohms for 32-VDC solenoids 46 to 87 ohms for 36-VDC solenoids 92 to 145 ohms for 48-VDC solenoids 315 to 375 ohms for 74-VDC solenoids 645 to 735 ohms for 115-VAC solenoids? **NORepair:** Replace the fuel shutoff solenoid. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334. Refer to Procedure 019-050 in Section 19. | Repair complete |  |

#### STEP 3D. Check fuel shutoff valve actuator.

| **Conditions:** Turn keyswitch OFF. Remove the fuel shutoff valve solenoid, valve disc, valve seat, and actuator. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the valve disc, valve seat, and actuator disc for dirt, metal debris, bonding separation, corrosion, cracks, or wear. n/a | Debris or damage found on the valve disc, valve seat, or actuator disc? **YESRepair:** Replace the damaged fuel shutoff valve component. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334. Refer to Procedure 019-050 in Section 19. | Repair complete |
| Debris or damage found on the valve disc, valve seat, or actuator disc? **NO** | 3E |  |

#### STEP 3E. Check for correct priming pump operation, if equipped.

| **Conditions:** Turn keyswitch OFF. Assemble fuel shutoff valve components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Listen for lift pump operation after the keyswitch is turned to the ON position. **Not** all ISX engines use a priming pump and **not** all priming pumps actuate at keyswitch ON. Understand which system is present on this engine before beginning this step. | Does the lift pump operate after turning the keyswitch ON? **YES** | 3E-1 |
| Does the lift pump operate after turning the keyswitch ON? **NORepair:** Check or replace the lift pump. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 005-045 in Section 5. | Repair complete |  |

#### STEP 3E-1. Check priming pump pressure.

| **Conditions:** Turn keyswitch OFF. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the priming pressure at the quick connect fitting located on the top of the integrated fuel system module (IFSM). Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 005-045 in Section 5. | Does pump pressure meet the 69 kPa \[10 psi\] specification? **YES** | 3F |
| Does pump pressure meet the 69 kPa \[10 psi\] specification? **NORepair:** Replace the lift pump. Use the following procedure in the Signature™ ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 005-045 in Section 5. | Repair complete |  |

#### STEP 3F. Check for coolant in the EGR transfer tube.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Remove the EGR transfer hose from the EGR cooler outlet. n/a | Is coolant present in the crossover tube? **YESRepair:** See the Coolant Loss - Internal symptom tree. | Repair complete |
| Is coolant present in the crossover tube? **NORepair:** Perform the next troubleshooting procedure as outlined in Step 2 | 2A |  |

### STEP 4. Fuel system checks.

#### STEP 4A. Verify the fuel system has been primed.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| If entering this tree after a component has been replaced in the fuel system, or after the engine has been run out of fuel, verify the fuel system has been properly primed before proceeding. Verify the fuel system has been properly primed. Use the following procedure for fuel system priming information found in the Signature™, ISX, and QSX15, Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 006-015 in Section 6. | Has the fuel system been properly primed? **YES** | 4B |
| Has the fuel system been properly primed? **NORepair:** Prime the fuel system. Use the following procedure for fuel system priming information found in the Signature™, ISX, and QSX15, Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 006-015 in Section 6. | repair complete |  |

#### STEP 4B. Check for air in the fuel.

| **Conditions:** Operate engine at low idle (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect the equipment to the quick-connect fitting at the fuel module as shown. Put a coil in the clear hose. Put the end of the clear hose in a clean container. Operate the engine at low idle with no load. Slightly open the valve until a steady stream of fuel is visible. | Are air bubbles visible in the coil of clear tubing? **YESRepair:** Locate and correct the cause of air ingestion in the OEM fuel supply system or damaged suction-side fuel filter sealing ring. With EGR: Check the ECM cooling plate, associated plumbing, and o-ring seals for damage that can cause air ingestion. Repair or replace the malfunctioning component. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 006-020 in Section 6. | Repair complete |
| Air bubbles visible in the coil of clear tubing? **NO** | 4C |  |

#### STEP 4C. Check fuel inlet restriction.

| **Conditions:** Connect vacuum gauge to the suction side Compuchek™ fitting. Turn keyswitch ON. Operate engine at high idle (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| If the engine uses a priming pump, wait until after the priming pump has turned off and observe the reading on the vacuum gauge. Check the fuel inlet restriction. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 006-020 n Section 6. | Is fuel inlet restriction less than the specifications listed below? Dirty - 305 mm-Hg \[12 in-Hg\]; New - 203 mm-Hg \[8 in-Hg\] **YES** | 4D |
| Is fuel inlet restriction less than the specifications listed below? Dirty - 305 mm-Hg \[12 in-Hg\]; New - 203 mm-Hg \[8 in-Hg\] **NORepair:** Locate the cause of high fuel inlet restriction. Check the suction-side fuel filter and fuel supply lines. For QSX15 **only**, check the 300 micron inlet filter screen for debris. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-005-073-tr — Integrated Fuel System Module (IFSM)\|Refer to Procedure 005-073 in Section 5.]] | Repair complete |  |

#### STEP 4D. Check drain line restriction.

| **Conditions:** Connect pressure gauge, Part Number 3375278. Turn keyswitch ON. Operate engine at high idle (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Observe reading on the pressure gauge. n/a | Is fuel drain line restriction less than 229 mm-Hg \[9 in-Hg\]? **YES** | 4E |
| Is fuel drain line restriction less than 229 mm-Hg \[9 in-Hg\]? **NORepair:** Locate cause of high fuel drain line restriction in OEM fuel return line. | Repair complete |  |

#### STEP 4E. Check rail fuel pressure.

| **Conditions:** Connect pressure gauge, Part Number 3375932, on the Compuchek™ fitting (as shown) Turn keyswitch ON. Operate engine at low idle (engine cranking if troubleshooting No-Start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the rail fuel pressure at low idle and high idle. Read the rail fuel pressure while cranking if the engine will **not** start. Cranking: greater than 689 kPa \[100 psi\] at 130 rpm for at least 10 seconds. Low idle: 1689 to 1889 kPa \[245 to 274 psi\] at 600 rpm. High idle: 1896 to 2068 kPa \[275 to 325 psi\] at 1800 rpm. With EGR Cranking: greater than 689 kPa \[100 psi\] at 130 rpm for at least 10 seconds. Low idle: 1586 to 1889 kPa \[230 to 274 psi\] at 600 rpm. High idle: 1896 to 2068 kPa \[275 to 325 psi\] at 1800 rpm. | Does the rail fuel pressure meet the specification? **YES** | Perform the next troubleshooting procedure as outlined in Step 2 |
| Does the rail fuel pressure meet the specification? **NORepair:** When cranking, make sure the fuel system is primed for at least 30 seconds. | 4E-2 With EGR 4E-1 |  |

#### STEP 4E-1. Check the pressure side fuel filter restriction.

| **Conditions:** Connect pressure gauge, Part Number 3375932, on the rail fuel pressure Compuchek™ fitting. Connect pressure gauge, Part Number 3375932, on the gear pump output pressure Compuchek™ fitting. Operate engine at high idle (engine cranking if troubleshooting no-start). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fuel pressure drop across the pressure side fuel filter at high idle or while cranking if the engine will not start. n/a | Is the pressure side fuel filter pressure drop less than 517 kPa \[75 psi\]? **YES** | 4E-2 |
| Is the pressure side fuel filter pressure drop less than 517 kPa \[75 psi\]? **NORepair:** Replace the pressure side fuel filter. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-006-015-tr — Fuel Filter (Spin-On Type)\|Refer to Procedure 006-015 in Section 6.]] | Repair complete |  |

#### STEP 4E-2. Check 1724 kPa \[250 psi\] pressure regulator.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Remove the 1724-kPa \[250-psi\] fuel pressure regulator. Inspect for debris or damage or incomplete sealing of the regulator. | Is the 1724 kPa \[250 psi\] pressure regulator free of debris or damage? **YES** | 4E-3 |
| Is the 1724 kPa \[250 psi\] pressure regulator free of debris or damage? **NORepair:** Replace 1724 kPa \[250 psi\] regulator. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-005-073-tr — Integrated Fuel System Module (IFSM)\|Refer to Procedure 005-073 in Section 5.]] | Repair complete |  |

#### STEP 4E-3. Check 2206 kPa \[320 psi\] or 2620 kPa \[380 psi\] pressure regulator.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Remove the 2206 kPa \[320 psi\] fuel pressure regulator. Inspect for debris, damage, or incomplete sealing of the regulator. With EGR Remove the 2620 kPa \[380 psi\] fuel pressure regulator. Inspect for debris, damage, or incomplete sealing of the regulator. | Is the pressure regulator free of debris or damage? **YESRepair:** Replace the fuel pump. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-005-016 — Fuel Pump\|Refer to Procedure 005-016 in Section 5.]] | Repair complete |
| Is the pressure regulator free of debris or damage? **NORepair:** Replace the 2206 kPa \[320 psi\] regulator. With EGR Replace the 2620 kPa \[380 psi\] regulator. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-005-073-tr — Integrated Fuel System Module (IFSM)\|Refer to Procedure 005-073 in Section 5.]] | Repair complete |  |

### STEP 5. Injector and Actuator Diagnostics.

#### STEP 5A. Perform the injector check valve leak test.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the injector check valve leak test to check for internal injector check valve damage. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] INSITE™ electronic service tool Injector Check Valve Diagnostics Test can be used as an initial test before performing the mechanical check outlined in Procedure 006-026 in Section 6. If INSITE™ electronic service tool does **not** detect a failed injector, perform the injector leak test. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] | Did the injector leak test detect a leaking injector? **YESRepair:** Replace the leaking injector. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] | Repair complete |
| Did the injector leak test detect a leaking injector? **NO** | 5B |  |

#### STEP 5B. Perform INSITE™ electronic service tool Cylinder Performance Test.

| **Conditions:** Troubleshoot any active fault codes before performing the test. Engine coolant temperature must be greater than 83°C \[180°F\]. Connect INSITE™ electronic service tool. Operate engine at idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform INSITE™ electronic service tool Cylinder Performance Test. ISX Signature™: There is a horizontal bar graph for each cylinder that is color coded based on current contribution state. The bar will be Blue for acceptable/pass contribution. The bar will be Red for unacceptable/fail contribution, either Low or High. Monitor the display to see if cylinders or banks drop out during a 2 minute window. A cylinder can switch from pass to fail and back to pass quickly, so monitor the screen closely. ISX CM870: During the initial 30 seconds of the Cylinder Performance Test, INSITE™ electronic service tool is checking to make sure all parameters have been met to enter the test. Once the initial Pass or Fail reading is displayed, the test is live for the next 2 minutes. Monitor the display to see if cylinders or banks drop out during this 2 minute window. A cylinder can switch from pass to fail and back to pass quickly, so monitor the screen closely. | Does performing INSITE™ electronic service tool Cylinder Performance Test identify a single malfunctioning injector? **YES** | 5C-3 |
| Does performing INSITE™ electronic service tool Cylinder Performance Test identify a single malfunctioning injector? **NO** | 5B-1 |  |

#### STEP 5B-1. Perform INSITE™ electronic service tool Cylinder Performance Test at 600 rpm.

| **Conditions:** Troubleshoot any active fault codes before performing the test. Engine coolant temperature must be greater than 83°C \[180°F\]. Connect INSITE™ electronic service tool. Operate engine at 600 rpm idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Skip this step and move on to step 5B-2 if the rpm value is the same as that used in step 5B. Adjust the low speed to 600 rpm and perform the INSITE™ electronic service tool Cylinder Performance Test. ISX Signature™: There is a horizontal bar graph for each cylinder that is color coded based on current contribution state. The bar will be Blue for acceptable/pass contribution. The bar will be Red for unacceptable/fail contribution, either Low or High. Monitor the display to see if cylinders or banks drop out during a 2 minute window. A cylinder can switch from pass to fail and back to pass quickly, so monitor the screen closely. ISX CM870: During the initial 30 seconds of the Cylinder Performance Test, INSITE™ electronic service tool is checking to make sure all parameters have been met to enter the test. Once the initial Pass or Fail reading is displayed, the test is live for the next 2 minutes. Monitor the display to see if cylinders or banks drop out during this 2 minute window. A cylinder can switch from pass to fail and back to pass quickly, so monitor the screen closely. | Does performing INSITE™ electronic service tool Cylinder Performance Test identify a single malfunctioning injector? **YES** | 5C-3 |
| Does performing INSITE™ electronic service tool Cylinder Performance Test identify a single malfunctioning injector? **NO** | 5B-2 |  |

#### STEP 5B-2. Perform INSITE™ electronic service tool Cylinder Performance Test at 700 rpm.

| **Conditions:** Troubleshoot any active fault codes before performing the test. Engine coolant temperature must be greater than 83°C \[180°F\]. Connect INSITE™ electronic service tool. Operate engine at 700 rpm idle. The idle speed may need to be adjusted to perform this test. Toggle the cruise control increment/decrement switch to see if the idle speed can be adjusted. If not, use INSITE™ electronic service tool to either enable the Adjustable Low Idle Speed feature or adjust the Low Idle Speed. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Skip this step and move on to step 5B-3 if the RPM value is the same as that used in step 5B. Adjust the low speed to 700 rpm and perform the INSITE™ electronic service tool Cylinder Performance Test. ISX Signature™: There is a horizontal bar graph for each cylinder that is color coded based on current contribution state. The bar will be Blue for acceptable/pass contribution. The bar will be Red for unacceptable/fail contribution, either Low or High. Monitor the display to see if cylinders or banks drop out during a 2 minute window. A cylinder can switch from pass to fail and back to pass quickly, so monitor the screen closely. ISX CM870: During the initial 30 seconds of the Cylinder Performance Test, INSITE™ electronic service tool is checking to make sure all parameters have been met to enter the test. Once the initial Pass or Fail reading is displayed, the test is live for the next 2 minutes. Monitor the display to see if cylinders or banks drop out during this 2 minute window. A cylinder can switch from pass to fail and back to pass quickly, so monitor the screen closely. | Does performing INSITE™ electronic service tool Cylinder Performance Test identify a single malfunctioning injector? **YES** | 5C-3 |
| Does performing INSITE™ electronic service tool Cylinder Performance Test identify a single malfunctioning injector? **NO** | 5B-3 |  |

#### STEP 5B-3. Perform INSITE™ electronic service tool Cylinder Performance Test at 800 rpm.

| **Conditions:** Troubleshoot any active fault codes before performing the test. Engine coolant temperature must be greater than 83°C \[180°F\]. Connect INSITE™ electronic service tool. Operate engine at 800 rpm idle. The idle speed may need to be adjusted to perform this test. Toggle the cruise control increment/decrement switch to see if the idle speed can be adjusted. If **not**, use INSITE™ electronic service tool to either enable the "Adjustable Low Idle Speed" feature or adjust the Low Idle Speed. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Skip this step and move on to step 5C if the rpm value is the same as that used in step 5B. Adjust the low speed to 800 rpm and perform the INSITE™ electronic service tool Cylinder Performance Test. ISX Signature™: There is a horizontal bar graph for each cylinder that is color coded based on current contribution state. The bar will be Blue for acceptable/pass contribution. The bar will be Red for unacceptable/fail contribution, either Low or High. Monitor the display to see if cylinders or banks drop out during a 2 minute window. A cylinder can switch from pass to fail and back to pass quickly, so monitor the screen closely. ISX CM870: During the initial 30 seconds of the Cylinder Performance Test, INSITE™ electronic service tool is checking to make sure all parameters have been met to enter the test. Once the initial Pass or Fail reading is displayed, the test is live for the next 2 minutes. Monitor the display to see if cylinders or banks drop out during this 2 minute window. A cylinder can switch from pass to fail and back to pass quickly, so monitor the screen closely. | Does performing INSITE™ electronic service tool Cylinder Performance Test identify a single malfunctioning injector? **YES** | 5C-3 |
| Does performing INSITE™ electronic service tool Cylinder Performance Test identify a single malfunctioning injector? **NO** | 5C |  |

#### STEP 5C. Perform INSITE™ electronic service tool Cylinder Cutout Test

| **Conditions:** Turn air conditioning OFF. Turn fan OFF. Disable any electrical loads. Operate the engine at the idle speed at which the misfire is present. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform INSITE™ electronic service tool cylinder cutout test. A failing cylinder will have no effect on engine sound and operation when cut out using this test. | Do all cylinders pass the cylinder cutout test? **YES** | 5C-1 |
| Do all cylinders pass the cylinder cutout test? **NO** | 5C-3 |  |

#### STEP 5C-1. Perform INSITE™ electronic service tool cylinder cutout test on individual injector banks.

| **Conditions:** Turn air conditioning OFF. Turn fan OFF. Disable any electrical loads. Operate the engine at the idle speed at which the misfire is present. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the INSITE™ electronic service tool cylinder cutout test. Operate the engine on the front bank of injectors identified by the cylinder cutout test by disabling the rear three cylinders 4, 5, 6 cylinders with INSITE™ electronic service tool. Operate the engine on the rear bank of injectors identified by the Cylinder Performance Test by disabling the front three cylinders (1,2,3) with INSITE™ electronic service tool. To disable one bank of cylinders with INSITE™ electronic service tool, click on the cylinder numbers associated with that bank. The front bank consists of cylinders 1, 2, and 3 and the rear bank is cylinders 4, 5, and 6. A malfunctioning bank of injectors will cause the engine to operate poorly when the opposite bank is cut out using this test. | Can a malfunctioning bank of injectors be isolated by operating the engine on either bank of injectors? **YES** | 5D |
| Can a malfunctioning bank of injectors be isolated by operating the engine on either bank of injectors? **NO** | 5C-2 |  |

#### STEP 5C-2. Perform INSITE™ electronic service tool Cylinder Cutout Test single cylinder operation.

| **Conditions:** Turn air conditioning OFF. Turn fan OFF. Disable any electrical loads. Operate the engine at the idle speed at which the misfire is present. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the INSITE™ electronic service tool cylinder cutout test. Operate the engine on the cylinder identified by the Cylinder Performance Test by disabling 5 cylinders with INSITE™ electronic service tool and **only** operating on the suspect cylinder. To disable 5 cylinders with INSITE™ electronic service tool, click on the cylinder numbers until **only** 1 cylinder is enabled. The engine should roughly maintain idle speed when operating on a single cylinder. A weak or misfiring cylinder will be detected if the engine dies or can **not** maintain idle speed when operating on a single cylinder. Continue testing all 6 cylinders by operating the engine on each individual injector. If the engine will **not** run on 1 cylinder regardless of the cylinder selected, increase the idle RPM and retest. Do **not** run the engine on 1 cylinder for an extended period of time. | Can a malfunctioning injector be isolated by operating the engine on a single injector? **YES** | 5C-3 |
| Can a malfunctioning injector be isolated by operating the engine on a single injector? **NO** | 5D |  |

#### STEP 5C-3. Verify overhead adjustments are correct for the suspected malfunctioning injector.

| **Conditions:** Turn keyswitch OFF. Remove the rocker lever cover. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 003-011 in Section 3. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the overhead settings for the suspected malfunctioning injector. Check the valve lash and injector pre-load torque before replacing the injector. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 003-004 in Section 3. | Are the overhead settings within the reset limits outlined in Procedure 003-004 in Section 3? **YESRepair:** Replace the malfunctioning injector. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] | Repair complete |
| Are the overhead settings within the reset limits outlined in Procedure 003-004 in Section 3? **NORepair:** Adjust the overhead settings. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-003-004-tr — Overhead Set\|Refer to Procedure 003-004 in Section 3.]] Perform the Cylinder Performance Test to determine if a misfire still exists after adjusting the overhead settings. | 5B |  |

#### STEP 5D. Swap the front and rear metering actuators.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the timing and metering actuators. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Swap the front and rear metering actuator to determine if the failed bank of cylinders follows a specific metering actuator. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334. Refer to Procedure 019-110 in Section 19. Perform INSITE™ electronic service tool Cylinder Performance Test. | Did the cylinder performance test find a malfunctioning bank? **YESRepair:** Replace the malfunctioning metering actuator. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334. Refer to Procedure 019-110 in Section 19. | Repair complete |
| Did the cylinder performance test find a malfunctioning bank? **NO** | 5E |  |

#### STEP 5E. Swap the front and rear timing actuators.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the timing and metering actuators. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Swap the front and rear timing actuator to determine if the failed bank of cylinders follows a specific timing actuator. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334. Refer to Procedure 019-111 in Section 19. Perform INSITE™ electronic service tool Cylinder Performance Test. | Does the malfunctioning bank follow the timing actuator? **YESRepair:** Replace the timing actuator. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334. Refer to Procedure 019-111 in Section 19. | Repair Complete |
| Does the malfunctioning bank follow the timing actuator? **NO** | Perform the next troubleshooting procedure as outlined in Step 2 |  |

### STEP 6. Air handling diagnostic checks.

#### STEP 6A. Start the engine and read the fault codes.

| **Conditions:** Connect INSITE™ electronic service tool electronic service tool. Operate the engine at low idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fault codes with the engine running. Use INSITE™ electronic service tool to read the fault codes. | Active fault codes? **YES** | Go to appropriate fault code troubleshooting tree |
| Active fault codes? **NO** | 6B |  |

#### STEP 6B. Check the air intake system for leaks.

| **Conditions:** n/a |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the air intake system for leaks. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 010-024 in Section 10. On engines equipped with a turbocharged air compressor, one often overlooked item as a source of air leaks is the air compressor intake line. The intake line supplies intake air from the intake of the engine to the air compressor. | Leaks found? **YESRepair:** Replace the damaged component. | Repair complete |
| Leaks found? **NO** | 6C |  |

#### STEP 6C. Check air intake restriction.

| **Conditions:** Turn keyswitch ON. Operate the engine at advertised horsepower and rpm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the intake system restriction by installing a vacuum gauge or water manometer into the air intake system. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 010-031 in Section 10. | Restriction greater than 635 mm-H 2 O \[25 in-H 2 O\] for a used air filter or 254 mm-H 2 O \[10 in-H 2 O\] for a new filter? **YESRepair:** Correct the cause of high intake air restriction. Check for plugged air filter or restricted air intake piping. | Repair complete |
| Restriction greater than 635 mm-H 2 O \[25 in-H 2 O\] for a used air filter or 254 mm-H 2 O \[10 in-H 2 O\] for a new filter? **NO** | 6D |  |

#### STEP 6D. Inspect the charge-air cooler.

| **Conditions:** Engine OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the charge-air cooler for cleanliness, cracks, holes, or other damage. If the initial inspection does not identify a problem, pressure test the charge air cooler. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 010-027 in Section 10. The pressure test can be used to verify charge-air cooler problems. | Problems found with the charge-air cooler? **YESRepair:** Repair or replace the charger-air cooler. Refer to the OEM service manual. | Repair complete |
| Problems found with the charge-air cooler? **NO** | 6E |  |

#### STEP 6E. Check the exhaust restriction.

| **Conditions:** Install a pressure gauge into the exhaust system. Turn keyswitch ON. Operate the engine at advertised horsepower and rpm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check exhaust restriction by installing a pressure gauge into the exhaust system just past the turbocharger outlet. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[101-011-009-tr — Exhaust Restriction\|Refer to Procedure 011-009 in Section 11.]] | Restriction between 518 mm-H 2 O \[20.4 in-H 2 O\] or 38 mm-Hg \[1.5 in-Hg\] and 1036 mm-H 2 O \[40.8 in-H 2 O\] or 76 mm-Hg \[3.0 in-Hg\]? **YES** | 6F |
| Restriction between 518 mm-H 2 O \[20.4 in-H 2 O\] or 38 mm-Hg \[1.5 in-Hg\] and 1036 mm-H 2 O \[40.8 in-H 2 O\] or 76 mm-Hg \[3.0 in-Hg\]? **NORepair:** Repair the exhaust system for the source of the high restriction. | Repair complete |  |

#### STEP 6F. Inspect the turbocharger blades for damage.

| **Conditions:** Engine OFF. Remove intake and exhaust connections for turbocharger. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the compressor and turbine blades for damage or wear. n/a | Damage found on turbocharger blades? **YESRepair:** Replace the turbocharger. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | Repair complete |
| Damage found on turbocharger blades? **NO** | 6G |  |

#### STEP 6G. Determination of turbocharger type.

| **Conditions:** n/a |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Determine if the turbocharger is a wastegated or variable geometry turbocharger. n/a | Is the turbocharger a variable geometry turbocharger? **YES** | 6H |
| Is the turbocharger a variable geometry turbocharger? **NO** | 6J |  |

#### STEP 6H. Check the variable geometry actuator rod for correct travel.

| **Conditions:** Engine OFF. Turn keyswitch ON. Connect INSITE™ electronic service tool. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. Use a straight edge steel ruler. Retract and extend the turbocharger actuator at least 10 times. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to start the Turbocharger Actuator Test. Adjust the delay timer in the Turbocharger Actuator Test so that the rod movement can be observed. Select the Retract Actuator position with INSITE™ electronic service tool. Mark or scribe the VG actuator rod at the base of the actuator. Select the Extend Actuator position with INSITE™ electronic service tool. Measure the rod travel by measuring the distance from the base of the turbocharger actuator to the scribe mark. Use a straight edge steel ruler. Retract and extend the turbocharger actuator at least 10 times. The turbocharger actuator will move quickly and crisply. If the actuator rod movement is slow, there could be a problem with the air supply, a faulty ground connection on the engine or chassis, or mechanical problems with the variable geometry turbocharger assembly. | Does the turbocharger actuator rod extend between 10 and 12 mm \[0.394 and 0.472 in\]? **YES** | 6I |
| Does the turbocharger actuator rod extend between 10 and 12 mm \[0.394 and 0.472 in\]? **NO** | 6H-1 |  |

#### STEP 6H-1. Check for air leaks and inspect air lines.

| **Conditions:** Engine OFF. Turn keyswitch ON. Connect INSITE™ electronic service tool. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to perform the Turbocharger Actuator Test. Select the Extend Actuator position. Listen for air leaks at the following components: Turbocharger control valve Turbocharger control shutoff valve inlet connection Turbocharger control shutoff valve outlet connection Turbocharger control valve inlet connection Turbocharger control valve outlet connection Turbocharger actuator inlet connection Turbocharger actuator. All air lines including the OEM supply line to the turbocharger control shutoff valve, turbocharger control shutoff valve to turbocharger control valve, and turbocharger control valve to turbocharger actuator A small amount of air could possibly be heard escaping from the turbocharger control valve during the turbocharger actuator test. This is a normal condition for the valve to achieve output regulation pressure. Do **not** replace the turbocharger control valve for this condition. | Air leaks found in the system? **YESRepair:** Repair air leaks. | Repair complete |
| Air leaks found in the system? **NO** | 6H-2 |  |

#### STEP 6H-2. Check the engine and vehicle grounds.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a loose or corroded engine, chassis, or battery ground connection. Check the engine ground connection. Check the chassis ground connections. Check the battery terminal connections. | Connections tight and corrosion-free? **YES** | 6H-3 |
| Connections tight and corrosion-free? **NORepair:** Tighten the connections. Tighten the loose connections and clean the terminals. Refer to the OEM service manual. | Repair complete |  |

#### STEP 6H-3. Check for air pressure at the turbocharger control valve outlet.

| **Conditions:** Engine OFF. Turn keyswitch ON. Connect INSITE™ electronic service tool. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to perform the Turbocharger Actutator Test. Select the Retract Actuator position. Remove the air line connection at the outlet of the turbocharger control valve. Install an M12 Compuchek™ fitting at the outlet of the turbocharger control valve. Install an air pressure gauge that is capable of reading at least 1034 kPa \[150 psi\]. Use INSITE™ electronic service tool to perform the Turbocharger Actuator Test. Select the Extend Actuator position. | Is vehicle air tank pressure present at the turbocharger control valve outlet? **YES** | 6H-4 |
| Is vehicle air tank pressure present at the turbocharger control valve outlet? **NO** | 6H-6 |  |

#### STEP 6H-4. Check for air pressure at the turbocharger control valve outlet.

| **Conditions:** Engine OFF. Turn keyswitch ON. Connect INSITE™ electronic service tool. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to perform the Turbocharger Actuator Test. Select the Retract Actuator position. Remove the air line connection at the outlet of the turbocharger control valve. Install an M12 Compuchek™ fitting at the outlet of the turbocharger control valve. Install an air pressure gauge that is capable of reading at least 1034 kPa \[150 psi\]. | Does the pressure gauge read more than 103 kPa \[15 psi\] after 5 minutes? **YESRepair:** Replace the turbocharger control valve. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334 or reference the OEM service manual. Refer to Procedure 019-388 in Section 19. | Repair complete |
| Does the pressure gauge read more than 103 kPa \[15 psi\] after 5 minutes? **NO** | 6H-5 |  |

#### STEP 6H-5. Check for correct turbocharger actuator travel.

| **Conditions:** Engine OFF. Turn keyswitch ON. Connect INSITE™ electronic service tool. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Damage to the turbocharger can result if the proper removal procedure is **not** followed. Remove the variable geometry actuator from the turbocharger. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 010-113 in Section 10. Use INSITE™ electronic service tool to perform the Turbocharger Actuator Test. Select the Extend Actuator position. | Does the turbocharger actuator rod travel at least 12 mm \[0.472 in\]? **YESRepair:** Repair the turbocharger assembly. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-010-145 — Variable Geometry Turbocharger Shroud Plate\|Refer to Procedure 010-145 in Section 10.]] | Repair complete |
| Does the turbocharger actuator rod travel at least 12 mm \[0.472 in\]? **NORepair:** Replace the turbocharger assembly. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 010-113 in Section 10. | Repair complete |  |

#### STEP 6H-6. Check for air pressure at the turbocharger control shutoff valve outlet.

| **Conditions:** Engine OFF. Turn keyswitch ON. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to perform the Turbocharger Actuator Test. Select the Extend Actuator position. Loosen the air line connection at the turbocharger control shutoff valve outlet. | Can air be heard escaping from the turbocharger control shutoff valve outlet? **YESRepair:** Replace the turbocharger control valve. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334 or reference the OEM service manual. Refer to Procedure 019-388 in Section 19. | Repair complete |
| Can air be heard escaping from the turbocharger control shutoff valve outlet? **NO** | 6H-7 |  |

#### STEP 6H-7. Check for air pressure at the turbocharger control shutoff valve inlet.

| **Conditions:** Engine OFF. Turn keyswitch ON. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the OEM air supply line is connected to the correct port on the turbocharger control shutoff valve. Loosen the air line connection at the turbocharger control shutoff valve inlet. | Can air be heard escaping from the turbocharger control shutoff valve inlet? **YES** | 6H-8 |
| Can air be heard escaping from the turbocharger control shutoff valve inlet? **NORepair:** Repair the air supply from the OEM air tanks. | Repair complete |  |

#### STEP 6H-8. Check for plugged turbocharger control shutoff valve filter.

| **Conditions:** Remove the turbocharger control shutoff valve filter. Turn keyswitch ON. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to perform the Turbocharger Actuator Test. Select the Extend Actuator position. Listen for an air leak at the turbocharger control shutoff valve filter head. | Is an air leak present at the turbocharger control shutoff valve filter head? **YESRepair:** Replace the turbocharger control shutoff valve filter. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 010-114 in Section 10. | Repair complete |
| Is an air leak present at the turbocharger control shutoff valve filter head? **NORepair:** Replace the turbocharger control shutoff valve. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334 or reference the OEM service manual. Refer to Procedure 019-386 in Section 19. | Repair complete |  |

#### STEP 6I. Perform INSITE™ Electronic Service Tool EGR Valve/Turbocharger Operational Test.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. Verify vehicle air tanks are charged to at least 586 kPa \[85 psi\] air pressure. Start the engine and run at low idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to select the EGR/VGT Operational Test. Prior to operating INSITE™ electronic service tool EGR Valve and EGR Valve/Turbocharger Operational Test, the ECM Calibration Software Phase can possibly need to be updated to the latest Software Phase. The ECM Calibration Phase Software can be checked in INSITE™ electronic service tool, under 'Features and Parameters'. Expand the selection for 'System ID and Dataplate' and go to 'Calibration Information'. If the Software Phase is earlier than shown below, calibrate the ECM, use the January 2006 INCAL™ CD-ROM, or later. Engines with the Software Phase listed below or later do **not** require a calibration. ISX engines with CM870 (engines built after January 2004) require Software Phase 06050302. ISX engines with CM870 (engines built before January 2004) require no changes at this time. This is a warrantable calibration change. Choose the Turbocharger actuator option under Test Choices. | Does the Turbocharger Operational Test pass? **YES** | Perform the next troubleshooting procedure as outlined in Step 2 |
| Does the Turbocharger Operational Test pass? **NO** | 6I-1 |  |

#### STEP 6I-1. Check the engine and vehicle grounds.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a loose or corroded engine, chassis, or battery ground connection. Check the engine ground connection. Check the chassis ground connections. Check the battery terminal connections. | Connections tight and corrosion-free? **YESRepair:** Replace the variable geometry turbocharger. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | Repair complete |
| Connections tight and corrosion-free? **NORepair:** Tighten the connections. Tighten the loose connections and clean the terminals. Refer to the OEM service manual. | Repair complete |  |

#### STEP 6J. Inspect the wastegate actuator hose.

| **Conditions:** Engine OFF. Remove turbocharger if wastegate actuator is inaccessible. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the integral wastegate actuator hose for cracks or holes. n/a | Holes or cracks found in the wastegate actuator hose? **YESRepair:** Replace wastegate actuator hose. | Repair complete |
| Holes or cracks found in the wastegate actuator hose? **NO** | 6K |  |

#### STEP 6K. Inspect the wastegate actuator rod for travel.

| **Conditions:** Engine OFF. Remove the wastegate actuator hose from the wastegate actuator. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Apply a regulated air supply of 310 kPa \[45 psi\] to the actuator and check for actuator movement. n/a | Does the wastegate actuator rod move? **YES** | 6L |
| Does the wastegate actuator rod move? **NO** | 6K-1 |  |

#### STEP 6K-1. Inspect wastegate actuator rod for travel.

| **Conditions:** Engine OFF. Remove the e-clip from the wastegate pin and disconnect the actuator rod. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Apply a regulated air supply of 310 kPa \[45 psi\] to the actuator and check for actuator movement. n/a | Does the wastegate actuator rod move? **YESRepair:** Move the wastegate lever on the turbocharger back and forth and check for smooth operation. Replace turbocharger assembly if the wastegate is seized. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | Repair complete |
| Does the wastegate actuator rod move? **NORepair:** Replace the wastegate actuator. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 010-050 in Section 10. | Repair complete |  |

#### STEP 6L. Measure resistance of the four-stage wastegate controllers, if equipped.

| **Conditions:** Engine OFF. Disconnect the ring terminals from the four-stage wastegate controllers, if equipped. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the wastegate controller post to engine block ground. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Are the wastegate controller solenoid resistances 6 to 10 ohms for 12-VDC solenoids, 24 to 40 ohms for 24-VDC solenoids? **YES** | 6M |
| Are the wastegate controller solenoid resistances 6 to 10 ohms for 12-VDC solenoids, 24 to 40 ohms for 24-VDC solenoids? **NORepair:** Replace the damaged wastegate controller. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 010-109 in Section 10. | Repair complete |  |

#### STEP 6M. Inspect four-stage wastegate controller, if equipped.

| **Conditions:** Engine OFF. Remove the four-stage wastegate controllers. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the valve disc, valve seat, and actuator disc for dirt, metal debris, bonding separation, corrosion, cracks, or wear. n/a | Damage or debris found on the valve disc, valve seat, or actuator disc? **YESRepair:** Replace or clean damaged components. | Repair complete |
| Damage or debris found on the valve disc, valve seat, or actuator disc? **NO** | Perform the next troubleshooting procedure as outlined in Step 2 |  |

### STEP 7. Check EGR valve for proper operation.

#### STEP 7A. Check for air leaks in the EGR system.

| **Conditions:** n/a |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for leaks in the EGR connection tubing and connections. Soot streaks can be noticeable where leaks are present. | Air leaks found in the EGR connection tubing? **YESRepair:** Repair any leaks in the EGR system. | Repair complete |
| Air leaks found in the EGR connection tubing? **NO** | 7B |  |

#### STEP 7B. Check repair history.

| **Conditions:** n/a |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check with the customer for a recent EGR valve replacement. n/a | Is there any record of the poppet head missing? **YESRepair:** Remove the exhaust manifold and run a wire through every port to check for the missing poppet head. | 7C |
| Is there any record of the poppet head missing? **NO** | 7C |  |

#### STEP 7C. Perform EGR Valve Test.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform INSITE™ electronic service tool EGR Valve Test. Prior to operating INSITE™ electronic service tool EGR Valve and EGR Valve/Turbocharger Operational Test, the ECM Calibration Software Phase can possibly need to be updated to the latest Software Phase. The ECM Calibration Phase Software can be checked in INSITE™ electronic service tool, under 'Features and Parameters'. Expand the selection for 'System ID and Dataplate' and go to 'Calibration Information'. If the Software Phase is earlier than shown below, calibrate the ECM, use the January 2006 INCAL™ CD-ROM, or later. Engines with the Software Phase listed below or later do **not** require a calibration. ISX engines with CM870 (engines built after January 2004) require Software Phase 06050302. ISX engines with CM870 (engines built before January 2004) require no changes at this time. This is a warrantable calibration change. Check for complete travel of the EGR valve by selecting Open Valve and verifying the EGR Valve opens 100 percent. | Does the EGR Valve Test pass? **YES** | Perform the next troubleshooting procedure as outlined in Step 2 |
| Does the EGR Valve Test pass? **NORepair:** Replace the EGR valve. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-011-022-tr — EGR Valve\|Refer to Procedure 011-022 in Section 11.]] | Repair complete |  |

### STEP 8. Verify electronic features are operating correctly.

#### STEP 8A. Verify accelerator pedal travel.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to monitor Accelerator Pedal while fully depressing and releasing the accelerator pedal. n/a | Does the Accelerator Pedal read 0 percent when the accelerator is released and 100 percent when the accelerator is depressed? **YES** | 8B |
| Does the Accelerator Pedal read 0 percent when the accelerator is released and 100 percent when the accelerator is depressed? **NORepair:** Determine and correct the cause of accelerator pedal restriction. | Repair complete |  |

#### STEP 8B. Monitor vehicle speed.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. Start the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to monitor Vehicle Speed while the vehicle is not moving. n/a | Does the vehicle speed read 0 when the vehicle is **not** moving? **YES** | 8C |
| Does the vehicle speed read 0 when the vehicle is **not** moving? **NORepair:** Check the vehicle speed sensor and circuit or locate the cause of the vehicle speed interference. | Repair complete |  |

#### STEP 8C. Verify electronic feature settings are correct.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to verify the following adjustable parameters are correctly set: Maximum vehicle speed Powertrain protection Rear axle ratio Number of transmission tailshaft gear teeth Tire revolutions per mile Gear-down protection Cruise control droop settings Cruise control maximum vehicle speed. | Are the electronic features set correctly? **YES** | Step 8D |
| Are the electronic features set correctly? **NORepair:** Correct programmable features. | Repair complete |  |

#### STEP 8D. Check the barometric pressure sensor reading.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for correct barometric pressure sensor reading. Compare the barometric pressure sensor reading in INSITE™ electronic service tool data monitor/logger to the present local barometric pressure. | Is the barometric pressure sensor reading in INSITE™ electronic service tool within 5 percent of the present local barometric pressure reading? **YES** | Perform the next troubleshooting procedure as outlined in Step 2 |
| Is the barometric pressure sensor reading in INSITE™ electronic service tool within 5 percent of the present local barometric pressure reading? **NORepair:** Replace the barometric pressure sensor. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System Signature™ and ISX Engines, Bulletin 4021334 or reference the OEM service manual. Refer to Procedure 019-004 in Section 19. | Repair complete |  |

### STEP 9. Perform base engine mechanical checks.

#### STEP 9A. Verify overhead adjustments are correct.

| **Conditions:** Turn keyswitch OFF. Remove valve cover. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the overhead settings. Valve Lash Reuse Limits: Intake valve lash: 0.102 mm \[0.004 in\] to 0.483 mm \[0.019 in\] Exhaust valve lash: 0.508 mm \[0.020 in\] to 0.813 mm \[0.032 in\]. | Overhead settings within the reuse limits? **YES** | 9B |
| Overhead settings within the reuse limits? **NORepair:** Adjust the overhead settings. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-003-004-tr — Overhead Set\|Refer to Procedure 003-004 in Section 3.]] | Repair complete |  |

#### STEP 9B. Verify engine brake adjustment.

| **Conditions:** Turn keyswitch OFF. Remove valve cover. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the engine brakes are operating correctly. Measure the engine brake settings. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 020-004 in Section 20. | Engine brake settings within the reuse limits? **YES** | 9C |
| Engine brake settings within the reuse limits? **NORepair:** Adjust the engine brake settings. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-020-004 — Engine Brake Assembly\|Refer to Procedure 020-004 in Section 20.]] | Repair complete |  |

#### STEP 9C. Measure turbocharger axial and radial clearance.

| **Conditions:** Engine OFF. Disconnect exhaust and intake connections from the turbocharger. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the axial and radial clearance of the turbocharger. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | Axial and radial clearances within specification? **YES** | 9D |
| Axial and radial clearances within specification? **NORepair:** Replace the turbocharger assembly. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | Repair complete |  |

#### STEP 9D. Verify engine blowby is within specification.

| **Conditions:** Turn keyswitch OFF. Connect the appropriate orifice to the end of the blowby draft tube. Start engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Load engine to rated rpm on a chassis dynamometer. Measure the engine blowby. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[101-014-010-tr — Crankcase Blowby, Measure\|Refer to Procedure 014-010 in Section 14.]] | Engine blowby measurements within specification? **YES** | 9E |
| Engine blowby measurements within specification? **NORepair:** Engine may need to be rebuilt. See engine rebuild specifications. | Repair complete |  |

#### STEP 9E. Verify injection timing is correct.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the injection timing is correct. Measure the injection timing. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-006-025 — Static Injection Timing\|Refer to Procedure 006-025 in Section 6.]] If the injection timing is found to be out of specification, bar the engine to "insert pin" and install the crankshaft pin. Install the appropriate injector camshaft wedge to set the correct injection timing. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-001-088-tr — Engine Base Timing\|Refer to Procedure 001-088 in Section 1.]] | Injection timing within specification? **YES** | 9F |
| Injection timing within specification? **NORepair:** Correct the injection timing. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-001-088-tr — Engine Base Timing\|Refer to Procedure 001-088 in Section 1.]] | Repair complete |  |

#### STEP 9F. Check for a damaged vibration damper.

| **Conditions:** Engine not operating. Turn engine OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Remove and visually inspect the vibration damper. Use the following procedure for vibration inspection specifications in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 001-052 in Section 1. | Vibration damper damaged or out of specification? **YESRepair:** Replace the vibration damper. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-001-052-tr — Vibration Damper, Viscous\|Refer to Procedure 001-052 in Section 1.]] | Repair complete |
| Vibration damper damaged or out of specification? **NO** | Perform the next troubleshooting procedure as outlined in Step 2 |  |

### STEP 10. Check the EGR differential pressure sensor and exhaust gas pressure sensor tubes.

#### STEP 10A. Check the EGR differential pressure tubes for cracks, restrictions, or leaks.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the EGR differential pressure tubes for cracks, restrictions, or leaks. Soot streaks can indicate that the line is loose or cracked. | Cracks, restrictions, or leaks present? **YESRepair:** Tighten or replace the EGR differential pressure tubes. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 011-026 in Section 11. | Repair complete |
| Cracks, restrictions, or leaks present? **NO** | 10B |  |

#### STEP 10B. Check the exhaust gas pressure tubes for cracks, restrictions, or leaks.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the exhaust gas pressure tubes for cracks, restrictions, or leaks. Soot streaks can indicate that the line is loose or cracked. | Cracks, restrictions, or leaks present? **YESRepair:** Tighten or replace the exhaust gas pressure tubes. Use the following procedure in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 011-027 in Section 11. | Repair complete |
| Cracks, restrictions, or leaks present? **NO** | Perform the next troubleshooting procedure as outlined in Step 2 |  |
