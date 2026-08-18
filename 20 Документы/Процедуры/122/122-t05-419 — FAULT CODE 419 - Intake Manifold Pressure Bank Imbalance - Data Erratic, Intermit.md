---
aliases:
  - "Код 419 — разбаланс давления коллекторов рядов — данные нестабильны или неверны"
type: "Процедура"
doc: "122-t05-419"
title_en: "FAULT CODE 419 - Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect"
title_ru: "Код 419 — разбаланс давления коллекторов рядов — данные нестабильны или неверны"
modified: "2015-06-25"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-419.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-419.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# FAULT CODE 419 - Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect
**Код 419 — разбаланс давления коллекторов рядов — данные нестабильны или неверны**

> [!abstract] Процедура · `122-t05-419`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-419.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-419.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check air shutoff valve. |  |
|  | **STEP 1A.** Check air shutoff valve position. | Air shutoff valve actuated/closed? |
| STEP 2. | Inspect the turbocharged impeller. |  |
|  | **STEP 2A.** Inspect turbocharged impeller for damage. | Damaged impeller blades? |
| STEP 3. | Validate the boost pressure sensor. |  |
|  | **STEP 3A.** Validate boost pressure sensor readings. | INSITE™ electronic service tool reading is within 102 mm-Hg \[4 in-Hg\] of the mechanical gauge? |
| STEP 4. | Check the injectors |  |
|  | **STEP 4A.** Check for malfunctioning injectors. | Low exhaust gas temperature readings on multiple cylinders on same bank? |
| STEP 5. | Check engine control module (ECM) calibration and clear fault codes. |  |
|  | **STEP 5A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 5B.** Disable the fault code. | Fault code inactive? |

### STEP 1. Check air shut off valve.

#### STEP 1A. Check air shutoff valve position.

| **Conditions:** Turn keyswitch OFF. Turn run/stop/auto switch to STOP position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the air shut off valve position. Is there a closed air shut off valve? | Air shut off valve actuated/closed? **YESRepair:** Open air shutoff valve. See equipment manufacturer service information. | 2A |
| Air shut off valve actuated/closed? **NO** | 2A |  |

### STEP 2. Inspect the turbocharged impeller.

#### STEP 2A. Inspect turbocharged impeller for damage.

| **Conditions:** Turn keyswitch OFF/isolated. Remove intake tubing from both turbochargers. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect turbocharged impeller. Inspect turbocharger impeller blades for signs of damage. | Damaged impeller blades? **YESRepair:** Replace the turbocharger. Use the following procedure in the K38, K50, QSK38, and QSK50 Service Manual, Bulletin 4021528. [[28-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | 3A |
| Damaged impeller blades? **NO** | 3A |  |

### STEP 3. Validate boost pressure sensor readings.

#### STEP 3A. Validate boost pressure sensor readings.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. Install a mechanical pressure gauge to the intake manifold. Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the boost pressure sensor readings.. Use INSITE™ electronic service tool to monitor the intake manifold 1 and 2 pressure sensors. Compare INSITE™ electronic service tool intake manifold pressure readings with the mechanical gauge pressure. Operate the engine under load. | INSITE™ electronic service tool reading is within 102 mm-Hg \[4 in-Hg\] of the mechanical gauge pressure? **YES** | 4A |
| INSITE™ electronic service tool reading is within 102 mm-Hg \[4 in-Hg\] of the mechanical gauge pressure? **NORepair:** Replace the intake manifold pressure sensor. Refer to Procedure 019-061 in Section 19. | 4A |  |

### STEP 4. Check for injectors.

#### STEP 4A. Check for malfunctioning injectors.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. Turn run/stop/auto switch to RUN position. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for malfunctioning injectors. Use INSITE™ electronic service tool to monitor all exhaust gas temperature sensor readings. Look for multiple low exhaust gas temperature readings on the same bank. | Multiple low exhaust gas temperature readings on same bank? **YESRepair:** Confirm the injectors are functioning correctly. | Go to the appropriate fault code troubleshooting procedure within Section TT. |
| Multiple low exhaust gas temperature readings on same bank? **NO** | 5A |  |

### STEP 5. Check engine control module (ECM) calibration and clear fault codes.

#### STEP 5A. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 5B |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 5B |  |

#### STEP 5B. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair Complete |
| Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
