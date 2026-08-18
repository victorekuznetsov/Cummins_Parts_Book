---
aliases:
  - "Код 7313 — давление масла топливного насоса ниже нормы — наивысший уровень"
type: "Процедура"
doc: "122-t05-7313"
title_en: "FAULT CODE 7313 - Engine Fuel Pump Oil Pressure - Data Valid But Below Normal Operating Range - Most Severe Level"
title_ru: "Код 7313 — давление масла топливного насоса ниже нормы — наивысший уровень"
modified: "2020-05-21"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-7313.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-7313.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# FAULT CODE 7313 - Engine Fuel Pump Oil Pressure - Data Valid But Below Normal Operating Range - Most Severe Level
**Код 7313 — давление масла топливного насоса ниже нормы — наивысший уровень**

> [!abstract] Процедура · `122-t05-7313`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2020-05-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-7313.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-7313.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for primary fault codes. | Fault Code 143, 415,1362 active or inactive with more than one count in the last 25 engine hours? |
| STEP 2. | Fuel pump lubricating oil pressure sensor stuck in-range. |  |
|  | **STEP 2A.** Visually inspect the sensor for damage. | Damage found on the fuel pump lubricating oil pressure sensor, connectors, or engine wiring harness? |
|  | **STEP 2B.** Verify fuel pump lubricating oil pressure sensor's accuracy. | Sensor reading between the recommended Cummins Ⓡ electronic service tool or equivalent and the mechanical gauge is within specification? |
| STEP 3. | Check the fuel pump drive lubricating oil filter. |  |
|  | **STEP 3A.** Check for damage on the fuel pump drive lubricating oil filter. | Damaged or plugged fuel pump drive lubricating oil filter? |
| STEP 4. | Check Fuel Pump Oil Pressure. |  |
|  | **STEP 4A.** Verify oil pressure at the outlet of the fuel pump drive lubricating oil filter head. | Fuel pump oil pressure is above the minimum oil pressure? |
|  | **STEP 4B.** Verify oil pressure at the outlet of the fuel pump drive lubricating oil filter head with new oil filter installed. | Fuel pump oil pressure is above the minimum oil pressure? |
| STEP 5. | Check ECM Calibration and clear fault codes. |  |
|  | **STEP 5A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 5B.** Disable the fault code. | Fault code inactive? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for primary fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 143, 415, 1362 active or inactive with more than 1 count in the last 25 engine hours? **YES** | Troubleshoot the appropriate fault codes. |
| Fault Code 143, 415, active or inactive with more than 1 count in the last 25 engine hours? **NO** | 2A |  |

### STEP 2. Fuel pump lubricating oil pressure sensor stuck in-range.

#### STEP 2A. Visually inspect the sensor and connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel pump lubricating oil pressure sensor from the engine wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the harness connector and fuel pump lubricating oil pressure sensor connector. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361]] in Section 19. | Damage found on the fuel pump lubricating oil pressure sensor, connectors, or engine wiring harness? **YESRepair:** Repair or replace **only** the component that were found to be out of specification. Replace the fuel pump lubricating oil pressure sensor. [[56-019-679 — Fuel Pump Lubricating Oil Supply Pressure Sensor\|Refer to Procedure 019-679]] in Section 19. Repair or replace the engine wiring harness or connectors. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043]] in Section 19. | 5A |
| Damage found on the fuel pump lubricating oil pressure sensor, connectors, or engine wiring harness? **NO** | 2B |  |

#### STEP 2B. Verify fuel pump lubricating oil pressure sensor's accuracy.

| **Conditions:** Turn keyswitch OFF |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel pump oil pressure at the outlet of the fuel pump oil filter head. Refer to Procedure 019-679 in Section 19. | Sensor reading between the recommended Cummins electronic service tool or equivalent and the mechanical gauge is within specification? **YES** | 3A |
| Sensor reading between the recommended Cummins electronic service tool or equivalent and the mechanical gauge is within specification? **NORepair:** Replace the fuel pump lubricating oil pressure sensor. [[56-019-679 — Fuel Pump Lubricating Oil Supply Pressure Sensor\|Refer to Procedure 019-679]] in Section 19. | 5A |  |

### STEP 3. Check the fuel pump drive lubricating oil filter.

#### STEP 3A. Check for damage on the fuel pump drive lubricating oil filter.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel pump drive lubricating oil filter. Refer to Procedure 007-110 in the Associated Procedures Table. | Damage found on the fuel pump drive lubricating oil filter? **YESRepair:** Replace the fuel pump drive lubricating oil filter. Refer to Procedure 007-110 in the Associated Procedures Table. | 5A |
| Damage found on the fuel pump drive lubricating oil filter? **NO** | 4A |  |

### STEP 4. Check Fuel Pump Oil Pressure.

#### STEP 4A. Verify oil pressure at the outlet of the fuel pump drive lubricating oil filter head.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify oil pressure at the outlet of the fuel pump drive lubricating oil filter head. Refer to Procedure 007-110 in the Associated Procedures Table. | Fuel pump oil pressure is above the minimum oil pressure? **YES** | 5A |
| Fuel pump oil pressure is above the minimum oil pressure? **NORepair:** Replace the fuel pump drive lubricating oil filter. Refer to Procedure 007-110 in the Associated Procedures Table. | 4B |  |

#### STEP 4B. Verify oil pressure at the outlet of the fuel pump drive lubricating oil filter head with new oil filter installed.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify oil pressure at the outlet of the fuel pump oil filter head. Refer to Procedure 007-110 in the Associated Procedures Table. | Fuel pump oil pressure is above the minimum oil pressure? **YES** | 5A |
| Fuel pump oil pressure is above the minimum oil pressure? **NO** | 5A |  |

### STEP 5. Check ECM calibration and clear fault codes.

#### STEP. 5A Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 5B |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032]] in Section 19. | 5B |  |

#### STEP. 5B Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable and clear the fault code. Operate the engine within the “Conditions for Clearing the Fault Code” found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
| Fault code inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow your technical escalation process. | Escalate or call for assistance. |  |

## Associated Procedures

| Associated Procedures |  |  |  |
|---|---|---|---|
| Procedure Title | Procedure Number | Engine Model | Bulletin Number |
| Fuel Pump Drive Lubricating Oil Filter | Refer to Procedure 007-110 | QSK45 and QSK60 | 4021530 |
