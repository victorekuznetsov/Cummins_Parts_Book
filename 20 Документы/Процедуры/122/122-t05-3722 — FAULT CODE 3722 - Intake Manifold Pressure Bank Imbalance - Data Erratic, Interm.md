---
aliases:
  - "Код 3722 — разбаланс давления коллекторов рядов — данные нестабильны или неверны"
type: "Процедура"
doc: "122-t05-3722"
title_en: "FAULT CODE 3722 - Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect"
title_ru: "Код 3722 — разбаланс давления коллекторов рядов — данные нестабильны или неверны"
modified: "2015-06-25"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-3722.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-3722.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# FAULT CODE 3722 - Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect
**Код 3722 — разбаланс давления коллекторов рядов — данные нестабильны или неверны**

> [!abstract] Процедура · `122-t05-3722`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-3722.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-3722.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the engine for air filter restriction. |  |
|  | **STEP 1A.** Check for engine air filter restriction. | Air filter restricted? |
| STEP 2. | Check for active fault codes. |  |
|  | **STEP 2A.** Check the engine control module (ECM) for active fault codes. | Fault Code 1433, 3131, or 5291 active? |
| STEP 3. | Check air shutoff valve. |  |
|  | **STEP 3A.** Check air shutoff valve position | Air shutoff valve closed? |
| STEP 4. | Check for a boost leak. |  |
|  | **STEP 4A.** Inspect the air intake system for leaks. | Air leak found? |
| STEP 5. | Check the turbochargers. |  |
|  | **STEP 5A.** Check turbocharger impellers for damage. | Damaged impeller blades? |
| STEP 6. | Validate the boost pressure sensor. |  |
|  | **STEP 6A.** Validate the boost pressure sensor readings. | INSITE™ electronic service tool reading is within 102 mm-Hg \[4 in-Hg\] of the mechanical gauge pressure? |
| STEP 7. | Check the injectors. |  |
|  | **STEP 7A.** Check for malfunctioning injectors. | Multiple low exhaust gas temperature readings on same bank? |
| STEP 8. | Check ECM calibration and clear fault codes. |  |
|  | **STEP 8A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 8B.** Disable the fault code. | Fault codes inactive? |

### STEP 1. Check the engine for air filter restriction.

#### STEP 1A. Check for engine air filter restriction.

| **Conditions:** Turn keyswitch OFF. Turn run/stop/auto switch to STOP position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine air filter restriction or damage that may cause excessive restriction. Use the following procedure in the K38, K50, QSK38 and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 010-059 in Section 10. | Air filter restricted? **YESRepair:** Replace the air cleaner elements. Use the following procedure in the K38, K50, QSK38 and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 010-014 in Section 10. | 2A |
| Air filter restricted? **NO** | 6A |  |

### STEP 2. Check for active fault codes.

#### STEP 2A. Check the engine control module (ECM) for active fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Run/stop/auto switch in the STOP mode. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to read the fault codes. INSITE™ electronic service tool found Fault Code 1433, 3131 or 5291 active? | Fault Code 1433, 3131, or 5291 active? **YESRepair:** Troubleshoot the active fault code(s) | Refer to the appropriate fault code troubleshooting procedure within Section TF. |
| Fault Code 1433, 3131, or 5291 active? **NO** | 3A |  |

### STEP 3. Check air shut off valve.

#### STEP 3A. Check the air shut off valve position.

| **Conditions:** Turn keyswitch OFF. Run/stop/auto switch in the STOP mode. Disconnect the engine harness connector from the ECM 60-pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the air shut off valve position. Is there a closed air shut off valve? | Air shut off valve closed? **YESRepair:** Open air shut off valve. See equipment manufacturer service information. | 4A |
| Air shut off valve closed? **NO** | 4A |  |

### STEP 4. Check for a boost leak.

#### STEP 4A. Inspect the air intake system for leaks.

| **Conditions:** Connect all components. Turn keyswitch ON. Run/stop/auto switch in the RUN mode. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the air intake system for leaks. Use the following procedure in the K38, K50, QSK38 and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 010-024 in Section 10. | Air leak found? **YESRepair:** Repair the leak. Use the following procedure in the K38, K50, QSK38 and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 010-024 in Section 10. | 5A |
| Air leak found? **NO** | 5A |  |

### STEP 5. Check the turbochargers.

#### STEP 5A. Check turbocharger impellers for damage.

| **Conditions:** Turn keyswitch OFF. Run/stop/auto switch in the STOP mode. Intake tubing removed from both turbochargers. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the turbocharger impellers. Inspect the turbocharger impeller blades for signs of damage. | Damaged impeller blades? **YESRepair:** Replace the damaged turbocharger. Use the following procedure in the K38, K50, QSK38 and QSK50 Service Manual, Bulletin 4021528. [[28-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | 6A |
| Damaged impeller blades? **NO** | 6A |  |

### STEP 6. Validate the boost pressure sensor.

#### STEP 6A. Validate the boost pressure sensor readings.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. Install a mechanical pressure gauge to the intake manifold. Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to monitor the intake manifold 1 and 2 pressure. Operate the engine under load. Compare INSITE™ electronic service tool intake manifold pressure readings with the mechanical gauge pressure. | INSITE™ electronic service tool reading is within 102 mm-Hg \[4 in-Hg\] of the mechanical gauge pressure? **YES** | 7A |
| INSITE™ electronic service tool reading is within 102 mm-Hg \[4 in-Hg\] of the mechanical gauge pressure? **NORepair:** Replace intake manifold pressure sensor. Refer to Procedure 019-061 in Section 19. | 7A |  |

### STEP 7. Check the injectors.

#### STEP 7A. Check for malfunctioning injectors.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. Turn keyswitch ON. Run/stop/auto switch in the RUN mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to monitor all exhaust gas temperature sensor readings. Look for multiple low exhaust gas temperature readings on the same bank. | Multiple low exhaust gas temperature readings on same bank? **YESRepair:** Confirm the injectors are functioning correctly. | Go to the appropriate fault code troubleshooting procedure within Section TT. |
| Multiple low exhaust gas temperature readings on same bank? **NO** | 8A |  |

### STEP 8. Check ECM calibration and clear fault codes.

#### STEP 8A. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 8B |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 8B |  |

#### STEP 8B. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair Complete |
| Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
