---
aliases:
  - "Код 214 — высокая температура масла — выше нормы — наивысший уровень"
type: "Процедура"
doc: "82-t05-214"
title_en: "FAULT CODE 214 - Engine Oil Temperature High - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Код 214 — высокая температура масла — выше нормы — наивысший уровень"
modified: "2019-07-01"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-214.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-214.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# FAULT CODE 214 - Engine Oil Temperature High - Data Valid But Above Normal Operating Range - Most Severe Level
**Код 214 — высокая температура масла — выше нормы — наивысший уровень**

> [!abstract] Процедура · `82-t05-214`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-07-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-214.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-214.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | High coolant temperature causing high oil temperature. |  |
|  | **STEP 1A.** Check high coolant temperature fault code. | High engine coolant temperature fault codes? |
| STEP 2. | Lubricating oil thermostat is malfunctioning. |  |
|  | **STEP 2A.** Check the lubricating oil thermostat for proper operation. | Thermostat operating correctly? |
| STEP 3. | Lubricating oil cooler is malfunctioning or restricted. |  |
|  | **STEP 3A.** Check the lubricating oil cooler. | Debris found in the lubricating oil cooler? |
| STEP 4. | Lubricating oil cooler is leaking. |  |
|  | **STEP 4A.** Check for lubricating oil cooler leaks. | Lubricating oil cooler leaks during the pressure test or damage observed during inspection? |
| STEP 5. | Check ECM calibration and clear fault codes. |  |
|  | **STEP 5A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 5B.** Disable the fault code. | Fault code inactive? |

### STEP 1. High coolant temperature causing high oil temperature.

#### STEP 1A. Check high coolant temperature fault code.

| **Conditions:** Turn keyswitch ON. Connect the recommended Cummins® electronic service tool, or equivalent. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check high coolant temperature fault code. Check to make certian that high engine coolant temperatures are not causing the high oil temperature symptoms. | High engine coolant temperature fault codes? **YES** | Troubleshoot any high engine coolant temperature fault codes. |
| High engine coolant temperature fault codes? **NO** | 2A |  |

### STEP 2. Lubricating oil thermostat is malfunctioning.

#### STEP 2A. Check the lubricating oil thermostat for proper operation.

| **Conditions:** N/A |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the lubricating oil thermostat for proper operation. Check the lubricating oil thermostat for proper operation. Refer to Procedure 007-039 in the Associated Procedures Table. | Thermostat operating correctly? **YES** | 3A |
| Thermostat operating correctly? **NORepair:** Replace the lubricating oil thermostat. Refer to Procedure 007-039 in the Associated Procedures Table. | 5A |  |

### STEP 3. Lubricating oil cooler is malfunctioning or restricted.

#### STEP 3A. Check the lubricating oil cooler.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the lubricating oil cooler. Inspect the lubricating oil cooler for debris. Refer to Procedure 007-003 in the Associated Procedures Table. | Debris found in the lubricating oil cooler? **YESRepair:** Clean or replace the lubricating oil cooler. Refer to Procedure 007-003 in the Associated Procedures Table. | 5A |
| Debris found in the lubricating oil cooler? **NO** | 4A |  |

### STEP 4. Lubricating oil cooler leaking.

#### STEP 4A. Check for lubricating oil cooler leaks.

| **Conditions:** N/A |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for lubricating oil cooler leaks. Pressure test the lubricating oil cooler. Refer to Procedure 007-003 in the Associated Procedures Table. | Lubricating oil cooler leaks during the pressure test or damage observed during inspection? **YESRepair:** Replace the lubricating oil cooler. Refer to Procedure 007-003 in the Associated Procedures Table. Replace the lubricating oil cooler element, mounting plate gasket or o-ring. Refer to Procedure 007-003 in the Associated Procedures Table. | 5A |
| Lubricating oil cooler leaks during the pressure test or damage observed during inspection? **NO** | 5A |  |

### STEP 5. Check ECM calibration and clear fault codes.

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
| Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
| Fault code inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or Call for assistance. |  |

## Associated Procedures

| Associated Procedures |  |  |  |
|---|---|---|---|
| Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
| Lubricating Oil Thermostat | [[35-007-039-tr — Lubricating Oil Thermostat\|Refer to Procedure 007-039]] | ISM, ISMe, and QSM11 | [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]] |
| Lubricating Oil Cooler | [[35-007-003-tr — Lubricating Oil Cooler\|Refer to Procedure 007-003]] | ISM, ISMe, and QSM11 | [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]] |
